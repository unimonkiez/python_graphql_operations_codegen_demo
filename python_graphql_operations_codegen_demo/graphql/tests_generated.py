import python_graphql_operations_codegen_demo.graphql_generated.types_generated as Types

# flake8: noqa

from typing import List, Optional, AsyncGenerator
from dataclasses import dataclass
from dataclasses import asdict
from gql import Client, WebsocketsTransport, AIOHTTPTransport, RequestsHTTPTransport, gql
from dacite import from_dict, Config
from enum import Enum


def _get_client_sync() -> Client:
  transport = RequestsHTTPTransport(url="http://localhost:4000/graphql")
  client = Client(transport=transport, fetch_schema_from_transport=False)
  return client


def _get_client_async() -> Client:
  transport = AIOHTTPTransport(url="http://localhost:4000/graphql")
  client = Client(transport=transport, fetch_schema_from_transport=False)
  return client


def _get_client_subscriptions() -> Client:
  transport = WebsocketsTransport(url="ws://localhost:4000/graphql")
  client = Client(transport=transport, fetch_schema_from_transport=False)
  return client


_gql_simple_query_gql = gql("""
query simple_query {
  hello
}

""")


@dataclass
class SimpleQueryResponse:

  hello: Optional[str]
  

__GQL_CODEGEN_SimpleQueryResponse__ = SimpleQueryResponse



def execute_simple_query_gql() -> SimpleQueryResponse:
  client = _get_client_sync()
  variables={
    
  }
  variables_no_none = {k:v for k,v in variables.items() if v is not None}

  response_dict = client.execute_sync(
    _gql_simple_query_gql,
    variable_values=variables_no_none,
  )
  return from_dict(data_class=SimpleQueryResponse, data=response_dict, config=Config(cast=[Enum]))



async def execute_async_simple_query_gql() -> SimpleQueryResponse:
  client = _get_client_async()
  variables={
    
  }
  variables_no_none = {k:v for k,v in variables.items() if v is not None}

  response_text_promise = client.execute_async(
    _gql_simple_query_gql,
    variable_values=variables_no_none,
  )
  response_dict = await response_text_promise
  return from_dict(data_class=SimpleQueryResponse, data=response_dict, config=Config(cast=[Enum]))


_gql_query_with_parameter_gql = gql("""
query query_with_parameter($name: String!) {
  helloName(name: $name)
}

""")


@dataclass
class QueryWithParameterResponse:

  helloName: str
  

__GQL_CODEGEN_QueryWithParameterResponse__ = QueryWithParameterResponse



def execute_query_with_parameter_gql(name: str) -> QueryWithParameterResponse:
  client = _get_client_sync()
  variables={
    "name": name,
  }
  variables_no_none = {k:v for k,v in variables.items() if v is not None}

  response_dict = client.execute_sync(
    _gql_query_with_parameter_gql,
    variable_values=variables_no_none,
  )
  return from_dict(data_class=QueryWithParameterResponse, data=response_dict, config=Config(cast=[Enum]))



async def execute_async_query_with_parameter_gql(name: str) -> QueryWithParameterResponse:
  client = _get_client_async()
  variables={
    "name": name,
  }
  variables_no_none = {k:v for k,v in variables.items() if v is not None}

  response_text_promise = client.execute_async(
    _gql_query_with_parameter_gql,
    variable_values=variables_no_none,
  )
  response_dict = await response_text_promise
  return from_dict(data_class=QueryWithParameterResponse, data=response_dict, config=Config(cast=[Enum]))


_gql_query_with_optional_parameter_gql = gql("""
query query_with_optional_parameter($name: String = \"UV\") {
  helloName(name: $name)
}

""")


@dataclass
class QueryWithOptionalParameterResponse:

  helloName: str
  

__GQL_CODEGEN_QueryWithOptionalParameterResponse__ = QueryWithOptionalParameterResponse



def execute_query_with_optional_parameter_gql(name: str = None) -> QueryWithOptionalParameterResponse:
  client = _get_client_sync()
  variables={
    "name": name,
  }
  variables_no_none = {k:v for k,v in variables.items() if v is not None}

  response_dict = client.execute_sync(
    _gql_query_with_optional_parameter_gql,
    variable_values=variables_no_none,
  )
  return from_dict(data_class=QueryWithOptionalParameterResponse, data=response_dict, config=Config(cast=[Enum]))



async def execute_async_query_with_optional_parameter_gql(name: str = None) -> QueryWithOptionalParameterResponse:
  client = _get_client_async()
  variables={
    "name": name,
  }
  variables_no_none = {k:v for k,v in variables.items() if v is not None}

  response_text_promise = client.execute_async(
    _gql_query_with_optional_parameter_gql,
    variable_values=variables_no_none,
  )
  response_dict = await response_text_promise
  return from_dict(data_class=QueryWithOptionalParameterResponse, data=response_dict, config=Config(cast=[Enum]))
