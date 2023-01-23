class Sentence:
    """
    Represents a single sentence in both languages
    """
    
    def __init__(self, id: int, japanese: str, english: str) -> None:
        self.id = id
        self.japanese = japanese
        self.english = english