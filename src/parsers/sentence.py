from enum import Enum

from ..entities import Sentence


class SentenceParser:
    """
    Parser responsible for processing Tanaka Corpus sentences
    (lines starting with `A: `).

    
    ```python
    parser = SentenceParser()
    sentence = parser.parseLine('A: ムーリエルは２０歳になりました。	Muiriel is 20 now.#ID=1282_4707')

    # sentence == Sentence(12824707, 'ムーリエルは２０歳になりました。', 'Muiriel is 20 now.')
    ```
    """
    class ParsingMode(Enum):
        JAPANESE = 1
        ENGLISH = 2
        ID = 3
        PASS_ID = 4

    def __init__(self) -> None:
        pass

    def parseLine(self, line: str) -> Sentence:
        """
        Converts a single line to a `Sentence` object.
        """

        if line.startswith('A: '):
            line = line[3:]

        parsed = self.assignChars(line)
        
        japanese = ''.join(parsed['japanese'])
        english = ''.join(parsed['english'])
        
        # id as an int, without the underscore
        id = int(filter(lambda c: c.isdigit(), parsed['id']))

        return Sentence(id, japanese, english)
    
    def assignChars(self, line: str) -> dict:
        """
        Creates a dictionary with character arrays assigned by certain modes.
        """

        parsed = {}
        mode = self.ParsingMode.JAPANESE

        for char in line:
            shouldSave = True

            # TODO: extract somewhere else
            if char == '\t':
                mode = self.ParsingMode.ENGLISH
                shouldSave = False
            elif mode == self.ParsingMode.PASS_ID:
                if char == '=':
                    mode = self.ParsingMode.ID
                
                shouldSave = False

            if shouldSave:
                modeName = mode.name.lower()

                parsed.setdefault(modeName, [])
                parsed[modeName].append(char)
        
        return parsed

