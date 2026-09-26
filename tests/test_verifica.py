"""Tests for romana-clara/scripts/verifica.py. Run: python -m unittest discover tests"""

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "romana-clara" / "scripts"))
import verifica  # noqa: E402

LETTER = (
    "În vederea asigurării respectării prevederilor legale în materie, se aduce la "
    "cunoștința solicitantului faptul că, urmare a analizării documentației depuse, "
    "s-a constatat că aceasta este incompletă, motiv pentru care se va proceda la "
    "suspendarea termenului de soluționare până la momentul completării, urmând ca, "
    "în situația în care completarea nu este efectuată în termen de 30 de zile de la "
    "data comunicării prezentei, cererea să fie clasată."
)
PROCEDURE = ("Prezenta procedură are ca scop stabilirea modalității de realizare a "
             "activității de verificare a documentelor.")
REWRITE = """**Dosarul dumneavoastră este incomplet.**

Am analizat documentele pe care le-ați depus.

**Ce trebuie să faceți:** completați dosarul în 30 de zile de la data la care ați primit această scrisoare.

Dacă nu completați dosarul în acest termen, clasăm cererea.

Până când completați dosarul, termenul de soluționare este suspendat.
"""


def rules(text):
    findings, _ = verifica.run(text)
    return [f.rule for f in findings]


def find(text, rule):
    findings, _ = verifica.run(text)
    return [f for f in findings if f.rule == rule]


class WordCount(unittest.TestCase):
    """SKILL.md Section 8, checked against the numbers the skill itself states."""

    def test_letter_is_64_words(self):
        self.assertEqual(verifica.count_words(LETTER), 64)

    def test_procedure_is_15_words(self):
        self.assertEqual(verifica.count_words(PROCEDURE), 15)

    def test_rewrite_longest_is_13_words(self):
        _, stats = verifica.run(REWRITE)
        self.assertEqual(stats["longest"], 13)

    def test_number_with_unit_is_one_word(self):              # 8.2
        self.assertEqual(verifica.count_words("Plătiți în 30 de zile."), 3)
        self.assertEqual(verifica.count_words("Plătiți în 15 zile lucrătoare."), 4)

    def test_legal_citation_is_one_word(self):                # 8.3
        self.assertEqual(
            verifica.count_words("Vezi art. 36 alin. (2) din Legea nr. 24/2000 acum."), 3)

    def test_code_span_is_one_word(self):                     # 8.1
        self.assertEqual(verifica.count_words(verifica.mask("Rulați `git status --short` acum.")), 3)

    def test_institution_name_is_one_word(self):              # 8.5
        self.assertEqual(
            verifica.count_words("Trimiteți cererea la Agenția Națională de Administrare Fiscală."), 4)


class Sentences(unittest.TestCase):

    def test_etc_ends_a_sentence(self):
        units = [s for _, s in verifica.sentences("Aduceți acte, dosare etc. Apoi semnați.")]
        self.assertEqual(len(units), 2)

    def test_abbreviation_does_not_split(self):
        units = [s for _, s in verifica.sentences("Conform art. 5 alin. (2), plătiți taxa.")]
        self.assertEqual(len(units), 1)

    def test_list_items_counted_separately(self):             # 8.7
        units = verifica.sentences("Aveți nevoie de:\n- buletin\n- cerere semnată\n")
        self.assertEqual(len(units), 3)


class Mechanical(unittest.TestCase):

    def test_cedilla_found_and_fixed(self):
        [f] = find("Configuraţia este corectă, dar lipsește ceva aici.", "7.2")
        self.assertEqual(f.fix, "Configurația")
        self.assertEqual(f.tier, "N")

    def test_comma_below_is_clean(self):
        self.assertNotIn("7.2", rules("Configurația și setările sunt corecte."))

    def test_missing_diacritics_unambiguous_only(self):
        hits = [f.text for f in find("Am plecat fara bagaje, dar cu tine până la pana roții.", "7.1")]
        self.assertEqual(hits, ["fara"])

    def test_undiacriticized_document_reported_once(self):
        text = ("Acest document nu are diacritice deloc si trebuie corectat inainte "
                "de trimitere catre client, fara exceptie, daca se poate azi.")
        self.assertEqual(len(find(text, "7.1")), 1)

    def test_code_is_untouchable(self):
        self.assertEqual(rules("Rulați `echo sa facut; etc.` în terminal."), [])

    def test_s_a_hyphen(self):
        self.assertIn("7.13", rules("Ieri sa decis amânarea."))
        self.assertNotIn("7.13", rules("Casa sa este mare."))

    def test_si_sau(self):
        self.assertIn("inlocuiri.md §9", rules("Trimiteți cererea și/sau dosarul."))

    def test_ca_si_only_before_c(self):
        self.assertIn("7.6", rules("Lucrează ca și coordonator."))
        self.assertNotIn("7.6", rules("Este la fel ca și anul trecut."))

    def test_datorita_negative(self):
        self.assertIn("7.5", rules("Datorită întârzierii, am pierdut trenul."))
        self.assertNotIn("7.5", rules("Datorită ajutorului, am terminat."))


class PeCare(unittest.TestCase):
    """Rule 7.4. Only the unambiguous shape is flagged."""

    def test_missing_pe(self):
        self.assertIn("7.4", rules("Cartea care am citit-o este bună."))

    def test_correct_forms_not_flagged(self):
        for s in ("Cartea pe care am citit-o este bună.",
                  "Omul care l-a ajutat a plecat.",
                  "Fata care a văzut-o a râs.",
                  "Noi, care am plecat primii, am ajuns."):
            with self.subTest(s=s):
                self.assertNotIn("7.4", rules(s))


class Density(unittest.TestCase):

    def test_procedure_cascade_five_links(self):              # SKILL.md intro
        links, _ = verifica.cascade(PROCEDURE)
        self.assertEqual(links, 5)

    def test_letter_cascade_four_nouns(self):                 # Exemplu complet
        links, chain = verifica.cascade(LETTER)
        self.assertEqual((links, chain), (3, "vederea asigurării respectării prevederilor"))

    def test_procedure_nominals(self):                        # verificare.md worked case
        self.assertEqual(verifica.nominal_hits(PROCEDURE),
                         ["stabilirea", "realizare", "verificare"])

    def test_ordinary_words_not_nominals(self):
        self.assertEqual(verifica.nominal_hits("Fiecare funcție care pare mare are o poziție."), [])

    def test_rewrite_is_clean(self):
        self.assertEqual(verifica.run(REWRITE)[0], [])


class Consistency(unittest.TestCase):

    def test_rotated_synonyms(self):
        hits = find("Verificați setările. Apoi confirmați parametrii.", "1.5")
        self.assertEqual(len(hits), 2)                        # verify set + settings set
        self.assertTrue(all(f.candidate for f in hits))

    def test_one_term_is_clean(self):
        self.assertNotIn("1.5", rules("Verificați setările. Apoi verificați din nou setările."))

    def test_valid_adjective_not_a_verb(self):
        self.assertNotIn("1.5", rules("Verificați datele. Data nu este validă."))


class Cli(unittest.TestCase):

    def run_cli(self, text, *args):
        sys.stdin = io.StringIO(text)
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                code = verifica.main([*args, "-"])
        finally:
            sys.stdin = sys.__stdin__
        return code, buf.getvalue()

    def test_exit_codes(self):
        self.assertEqual(self.run_cli(REWRITE)[0], 0)
        self.assertEqual(self.run_cli(LETTER)[0], 1)

    def test_json_output(self):
        code, out = self.run_cli(LETTER, "--json")
        data = json.loads(out)
        self.assertEqual(data[0]["stats"]["longest"], 64)
        self.assertTrue(all({"rule", "tier", "line"} <= set(f) for f in data[0]["findings"]))


if __name__ == "__main__":
    unittest.main()
