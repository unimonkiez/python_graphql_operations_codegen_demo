# flake8: noqa
from typing import Optional, List, Union, Any, Literal
from enum import Enum

ScalarID = str
ScalarString = str
ScalarBoolean = bool
ScalarInt = int
ScalarFloat = float
  # The `Upload` scalar type represents a file upload.
ScalarUpload = Any


class CacheControlScope(Enum):
  Public = 'PUBLIC'
  Private = 'PRIVATE'

__GQL_CODEGEN_CacheControlScope__ = CacheControlScope

class Character:
  __typename: Optional[Literal["Character"]]
  # The id of the character.
  id: Optional[ScalarID]
  # The name of the character.
  name: Optional[ScalarString]
  # The status of the character ('Alive', 'Dead' or 'unknown').
  status: Optional[ScalarString]
  # The species of the character.
  species: Optional[ScalarString]
  # The type or subspecies of the character.
  type: Optional[ScalarString]
  # The gender of the character ('Female', 'Male', 'Genderless' or 'unknown').
  gender: Optional[ScalarString]
  # The character's origin location
  origin: Optional["__GQL_CODEGEN_Location__"]
  # The character's last known location
  location: Optional["__GQL_CODEGEN_Location__"]
  """
  Link to the character's image.
  All images are 300x300px and most are medium shots or portraits since they are intended to be used as avatars.
  """
  image: Optional[ScalarString]
  # Episodes in which this character appeared.
  episode: List[Optional["__GQL_CODEGEN_Episode__"]]
  # Time at which the character was created in the database.
  created: Optional[ScalarString]

__GQL_CODEGEN_Character__ = Character

class Characters:
  __typename: Optional[Literal["Characters"]]
  info: Optional["__GQL_CODEGEN_Info__"]
  results: Optional[List[Optional["__GQL_CODEGEN_Character__"]]]

__GQL_CODEGEN_Characters__ = Characters

class Episode:
  __typename: Optional[Literal["Episode"]]
  # The id of the episode.
  id: Optional[ScalarID]
  # The name of the episode.
  name: Optional[ScalarString]
  # The air date of the episode.
  air_date: Optional[ScalarString]
  # The code of the episode.
  episode: Optional[ScalarString]
  # List of characters who have been seen in the episode.
  characters: List[Optional["__GQL_CODEGEN_Character__"]]
  # Time at which the episode was created in the database.
  created: Optional[ScalarString]

__GQL_CODEGEN_Episode__ = Episode

class Episodes:
  __typename: Optional[Literal["Episodes"]]
  info: Optional["__GQL_CODEGEN_Info__"]
  results: Optional[List[Optional["__GQL_CODEGEN_Episode__"]]]

__GQL_CODEGEN_Episodes__ = Episodes

class FilterCharacter:
  name: Optional[ScalarString]
  status: Optional[ScalarString]
  species: Optional[ScalarString]
  type: Optional[ScalarString]
  gender: Optional[ScalarString]

__GQL_CODEGEN_FilterCharacter__ = FilterCharacter

class FilterEpisode:
  name: Optional[ScalarString]
  episode: Optional[ScalarString]

__GQL_CODEGEN_FilterEpisode__ = FilterEpisode

class FilterLocation:
  name: Optional[ScalarString]
  type: Optional[ScalarString]
  dimension: Optional[ScalarString]

__GQL_CODEGEN_FilterLocation__ = FilterLocation

class Info:
  __typename: Optional[Literal["Info"]]
  # The length of the response.
  count: Optional[ScalarInt]
  # The amount of pages.
  pages: Optional[ScalarInt]
  # Number of the next page (if it exists)
  next: Optional[ScalarInt]
  # Number of the previous page (if it exists)
  prev: Optional[ScalarInt]

__GQL_CODEGEN_Info__ = Info

class Location:
  __typename: Optional[Literal["Location"]]
  # The id of the location.
  id: Optional[ScalarID]
  # The name of the location.
  name: Optional[ScalarString]
  # The type of the location.
  type: Optional[ScalarString]
  # The dimension in which the location is located.
  dimension: Optional[ScalarString]
  # List of characters who have been last seen in the location.
  residents: List[Optional["__GQL_CODEGEN_Character__"]]
  # Time at which the location was created in the database.
  created: Optional[ScalarString]

__GQL_CODEGEN_Location__ = Location

class Locations:
  __typename: Optional[Literal["Locations"]]
  info: Optional["__GQL_CODEGEN_Info__"]
  results: Optional[List[Optional["__GQL_CODEGEN_Location__"]]]

__GQL_CODEGEN_Locations__ = Locations

class Query:
  __typename: Optional[Literal["Query"]]
  # Get a specific character by ID
  character: Optional["__GQL_CODEGEN_Character__"]
  # Get the list of all characters
  characters: Optional["__GQL_CODEGEN_Characters__"]
  # Get a list of characters selected by ids
  charactersByIds: Optional[List[Optional["__GQL_CODEGEN_Character__"]]]
  # Get a specific locations by ID
  location: Optional["__GQL_CODEGEN_Location__"]
  # Get the list of all locations
  locations: Optional["__GQL_CODEGEN_Locations__"]
  # Get a list of locations selected by ids
  locationsByIds: Optional[List[Optional["__GQL_CODEGEN_Location__"]]]
  # Get a specific episode by ID
  episode: Optional["__GQL_CODEGEN_Episode__"]
  # Get the list of all episodes
  episodes: Optional["__GQL_CODEGEN_Episodes__"]
  # Get a list of episodes selected by ids
  episodesByIds: Optional[List[Optional["__GQL_CODEGEN_Episode__"]]]

__GQL_CODEGEN_Query__ = Query


class QueryCharacterArgs:
  id: ScalarID

__GQL_CODEGEN_QueryCharacterArgs__ = QueryCharacterArgs


class QueryCharactersArgs:
  page: Optional[ScalarInt]
  filter: Optional[FilterCharacter]

__GQL_CODEGEN_QueryCharactersArgs__ = QueryCharactersArgs


class QueryCharactersByIdsArgs:
  ids: List[ScalarID]

__GQL_CODEGEN_QueryCharactersByIdsArgs__ = QueryCharactersByIdsArgs


class QueryLocationArgs:
  id: ScalarID

__GQL_CODEGEN_QueryLocationArgs__ = QueryLocationArgs


class QueryLocationsArgs:
  page: Optional[ScalarInt]
  filter: Optional[FilterLocation]

__GQL_CODEGEN_QueryLocationsArgs__ = QueryLocationsArgs


class QueryLocationsByIdsArgs:
  ids: List[ScalarID]

__GQL_CODEGEN_QueryLocationsByIdsArgs__ = QueryLocationsByIdsArgs


class QueryEpisodeArgs:
  id: ScalarID

__GQL_CODEGEN_QueryEpisodeArgs__ = QueryEpisodeArgs


class QueryEpisodesArgs:
  page: Optional[ScalarInt]
  filter: Optional[FilterEpisode]

__GQL_CODEGEN_QueryEpisodesArgs__ = QueryEpisodesArgs


class QueryEpisodesByIdsArgs:
  ids: List[ScalarID]

__GQL_CODEGEN_QueryEpisodesByIdsArgs__ = QueryEpisodesByIdsArgs

