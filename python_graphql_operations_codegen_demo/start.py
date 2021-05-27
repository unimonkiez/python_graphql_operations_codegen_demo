from python_graphql_operations_codegen_demo.graphql.tests_generated import execute_fragment_gql, execute_inline_fragments_gql


def start() -> None:
    res = execute_fragment_gql()
    print(res.testFrag.type)