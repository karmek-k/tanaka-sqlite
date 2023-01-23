import unittest

from .sentence import SentenceParser


class TestSentenceParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = SentenceParser()

    def test_parses_correct_sentence(self) -> None:
        input = r'A: ムーリエルは２０歳になりました。	Muiriel is 20 now.#ID=1282_4707'

        result = self.parser.parseLine(input)

        self.assertEqual(result.id, 12824707)
        self.assertEqual(result.japanese, 'ムーリエルは２０歳になりました。')
        self.assertEqual(result.english, 'Muiriel is 20 now.')

