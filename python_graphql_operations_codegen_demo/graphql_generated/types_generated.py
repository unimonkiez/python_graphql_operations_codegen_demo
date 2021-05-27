# flake8: noqa
from typing import Optional, List, Union, Any, Literal
from enum import Enum
from dataclasses import dataclass

ScalarID = str
ScalarString = str
ScalarBoolean = bool
ScalarInt = int
ScalarFloat = float

Data = Union["__GQL_CODEGEN_FragA__", "__GQL_CODEGEN_FragB__"]
__GQL_CODEGEN_Data__ = Data

class FragA:
  __typename: Optional[Literal["FragA"]]
  a: ScalarInt
  added: ScalarInt

__GQL_CODEGEN_FragA__ = FragA

class FragB:
  __typename: Optional[Literal["FragB"]]
  b: ScalarString
  addedAlso: ScalarInt

__GQL_CODEGEN_FragB__ = FragB

class Query:
  __typename: Optional[Literal["Query"]]
  hello: Optional[ScalarString]
  helloName: ScalarString
  testFrag: "__GQL_CODEGEN_TestFragResult__"

__GQL_CODEGEN_Query__ = Query


class QueryHelloNameArgs:
  name: ScalarString

__GQL_CODEGEN_QueryHelloNameArgs__ = QueryHelloNameArgs

class TestFragResult:
  __typename: Optional[Literal["testFragResult"]]
  type: ScalarString
  data: "__GQL_CODEGEN_Data__"

__GQL_CODEGEN_TestFragResult__ = TestFragResult
