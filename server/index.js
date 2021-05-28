const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { makeExecutableSchema } = require('@graphql-tools/schema');

 const typeDefs = `
 type FragA {
     a: Int!
     added: Int!
 }
 type FragB {
     b: String!
     addedAlso: Int!
 }
 union Data = FragA | FragB
 type testFragResult {
     type: String!
     data: Data!
 }

 type Query {
   hello: String
   helloName(name: String!): String!
   testFrag: testFragResult!
 }
`;

const resolvers = {
  Query: {
    hello: () => {
      return 'Hello world!';
    },
    helloName: (info, args) => {
      return `Hello ${args.name}!`;
    },
    testFrag: () => {
        const isA =  Math.random() < 0.5;
        if (isA) {
            return {
                type: 'a',
                data: {
                    a: 5,
                    added: 1
                },
            };
        }
        return {
            type: 'b',
            data: {
                b: `I'm b!`,
                addedAlso: 6
            },
        };
    }, 
  },
  Data: {
    __resolveType(obj) {
      if(obj.a){
        return 'FragA';
      }
      if(obj.b){
        return 'FragB';
      }
      return null; // GraphQLError is thrown
    },
  },
}

const schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});
 
var app = express();
app.use('/graphql', graphqlHTTP({
  schema: schema,
  graphiql: true,
}));
app.listen(4000);
console.log('Running a GraphQL API server at http://localhost:4000/graphql');