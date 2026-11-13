from dataclasses import dataclass

@dataclass
class Step:
     id : int
     instruction: str
     expected_result: str

