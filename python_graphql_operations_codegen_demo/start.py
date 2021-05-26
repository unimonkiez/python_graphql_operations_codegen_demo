import asyncio
from python_graphql_operations_codegen_demo.graphql.tests_generated import execute_query_with_optional_parameter_gql

async def start_async() -> None:
    res = execute_query_with_optional_parameter_gql(name="sdf")
    print(res.helloName)

def start() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_async())