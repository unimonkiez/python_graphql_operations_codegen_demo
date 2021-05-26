import python_graphql_operations_codegen_demo.graphql_generated.types_generated as Types

# flake8: noqa

from typing import List, Optional
from dataclasses import dataclass
from gql import Client, WebsocketsTransport, AIOHTTPTransport, RequestsHTTPTransport, gql
from dacite import from_dict


def _get_client_sync() -> Client:
  transport = RequestsHTTPTransport(url="https://rickandmortyapi.com/graphql")
  client = Client(transport=transport, fetch_schema_from_transport=False)
  return client


def _get_client_async() -> Client:
  transport = AIOHTTPTransport(url="https://rickandmortyapi.com/graphql")
  client = Client(transport=transport, fetch_schema_from_transport=False)
  return client


def _get_client_subscriptions() -> Client:
  transport = WebsocketsTransport(url="wss://rickandmortyapi.com/graphql")
  client = Client(transport=transport, fetch_schema_from_transport=False)
  return client


_gql_get_characters_gql = gql("""
query get_characters {
  characters {
    results {
      name
    }
  }
}

""")


@dataclass
class GetCharactersResponse:

  @dataclass
  class CharactersSelection:
  
    @dataclass
    class CharacterSelection:
    
      name: str
      
    
    __GQL_CODEGEN_CharacterSelection__ = CharacterSelection
    
    results: List[CharacterSelection]
    
  
  __GQL_CODEGEN_CharactersSelection__ = CharactersSelection
  
  characters: CharactersSelection
  

__GQL_CODEGEN_GetCharactersResponse__ = GetCharactersResponse



def execute_get_characters_gql() -> GetCharactersResponse:
  client = _get_client_sync()

  response_dict = client.execute_sync(
    _gql_get_characters_gql,
    variable_values={
      
    },
  )
  return from_dict(data_class=GetCharactersResponse, data=response_dict)



async def execute_async_get_characters_gql() -> GetCharactersResponse:
  client = _get_client_async ()

  response_text_promise = client.execute_async(
    _gql_get_characters_gql,
    variable_values={
      
    },
  )
  response_dict = await response_text_promise
  return from_dict(data_class=GetCharactersResponse, data=response_dict)


_gql_get_character_gql = gql("""
query get_character($id: ID!) {
  character(id: $id) {
    name
  }
}

""")


@dataclass
class GetCharacterResponse:

  @dataclass
  class CharacterSelection:
  
    name: str
    
  
  __GQL_CODEGEN_CharacterSelection__ = CharacterSelection
  
  character: CharacterSelection
  

__GQL_CODEGEN_GetCharacterResponse__ = GetCharacterResponse



def execute_get_character_gql(id: str) -> GetCharacterResponse:
  client = _get_client_sync()

  response_dict = client.execute_sync(
    _gql_get_character_gql,
    variable_values={
      "id": id,
    },
  )
  return from_dict(data_class=GetCharacterResponse, data=response_dict)



async def execute_async_get_character_gql(id: str) -> GetCharacterResponse:
  client = _get_client_async ()

  response_text_promise = client.execute_async(
    _gql_get_character_gql,
    variable_values={
      "id": id,
    },
  )
  response_dict = await response_text_promise
  return from_dict(data_class=GetCharacterResponse, data=response_dict)
