
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):

    def operate(self, text: str = None, params: Dict = None) -> str:
        return ""

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize