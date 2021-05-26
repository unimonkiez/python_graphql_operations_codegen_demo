# flake8: noqa
from typing import Optional, List, Union, Any, Literal
from enum import Enum
from dataclasses import dataclass

ScalarID = str
ScalarString = str
ScalarBoolean = bool
ScalarInt = int
ScalarFloat = float

class Query:
  __typename: Optional[Literal["Query"]]
  hello: Optional[ScalarString]
  helloName: ScalarString

__GQL_CODEGEN_Query__ = Query


class QueryHelloNameArgs:
  name: ScalarString

__GQL_CODEGEN_QueryHelloNameArgs__ = QueryHelloNameArgs
