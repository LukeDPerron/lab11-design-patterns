
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):

    def operate(self, text: str = None, params: Dict = None) -> str:
        if(text[0].isalnum() == False):
            word = ""
            for k in range (0, len(text), 1):
                word += text[k]
                if(text[k].isalnum()):
                    word = word.upper() + "."
                    return word
                
        text = text.strip().split()
        if len(text) > 2:
            return text[0][0] + ". " + text[1][0] + ". " + text[2][0] + "."
        elif (len(text) == 1):
            return text[0][0] + ". " + text[1][0] + "."

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize