
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):

    def operate(self, text: str = None, params: Dict = None) -> str:
        if(text[0].isalnum() == False): #if the first letter is not a number or alphabetical character
            if text[0] != " ": #if the first letter is not space
                word = "" #give an empty word
                for k in range (0, len(text), 1): #traverse each character in text
                    word += text[k] #adding the original string back
                    if(text[k].isalnum()): #if we get to an alphabetical or numeral character, 
                        word = word.upper() + "." #end it and return it with that uppercased with .
                        return word
            else:    #if the first letter is a space
                text = text.strip().split() #split it into an array of each separate word
                if len(text) > 2: 
                    return text[0][0] + ". " + text[1][0] + ". " + text[2][0] + "."
                elif (len(text) == 1):
                    return text[0][0] + ". " + text[1][0] + "."
        else:    #if the first letter is a space
            text = text.strip().split() #split it into an array of each separate word
            if len(text) > 2: 
                return text[0][0] + ". " + text[1][0] + ". " + text[2][0] + "."
            elif (len(text) == 2):
                return text[0][0] + ". " + text[1][0] + "."
            else:
                return text[0][0] + ". "


    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize