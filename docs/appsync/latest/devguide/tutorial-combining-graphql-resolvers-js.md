# Combining GraphQL resolvers in AWS AppSync

Resolvers and fields in a GraphQL schema have 1:1 relationships with a large degree of flexibility. Because a
data source is configured on a resolver independently of a schema, you have the ability to resolve or manipulate
your GraphQL types through different data sources, allowing you to mix and match a schema to best meet your
needs.

The following scenarios demonstrate how to mix and match data sources in your schema. Before you begin, you
should be familiar with configuring data sources and resolvers for AWS Lambda, Amazon DynamoDB, and Amazon OpenSearch Service.

## Example schema

The following schema has a type of `Post` with three `Query` and
`Mutation` operations each:

```
type Post {
    id: ID!
    author: String!
    title: String
    content: String
    url: String
    ups: Int
    downs: Int
    version: Int!
}

type Query {
    allPost: [Post]
    getPost(id: ID!): Post
    searchPosts: [Post]
}

type Mutation {
    addPost(
        id: ID!,
        author: String!,
        title: String,
        content: String,
        url: String
    ): Post
    updatePost(
        id: ID!,
        author: String!,
        title: String,
        content: String,
        url: String,
        ups: Int!,
        downs: Int!,
        expectedVersion: Int!
    ): Post
    deletePost(id: ID!): Post
}
```

In this example, you would have a total of six resolvers with each needing a data source. One way to solve
this issue would be to hook these up to a single Amazon DynamoDB table, called `Posts`, in which the
`AllPost` field runs a scan and the `searchPosts` field runs a query (see [JavaScript
resolver function reference for DynamoDB](js-resolver-reference-dynamodb.md "js-resolver-reference-dynamodb.md")). However, you aren't limited to Amazon DynamoDB; different data
sources like Lambda or OpenSearch Service exist to meet your business requirements.

## Altering data through resolvers

You may need to return results from a third-party database that's not directly supported by AWS AppSync data
sources. You may also have to perform complex modifications on the data before it's returned to the API
client(s). This could be caused by the improper formatting of the data types, such as timestamp differences
on clients, or the handling of backwards compatibility issues. In this case, connecting AWS Lambda functions
as a data source to your AWS AppSync API is the appropriate solution. For illustrative purposes, in the following
example, an AWS Lambda function manipulates data fetched from a third-party data store:

```
export const handler = (event, context, callback) => {
    // fetch data
    const result = fetcher()

    // apply complex business logic
    const data = transform(result)

    // return to AppSync
    return data
};
```

This is a perfectly valid Lambda function and could be attached to the `AllPost` field in the
GraphQL schema so that any query returning all the results gets random numbers for the ups/downs.

## DynamoDB and OpenSearch Service

For some applications, you might perform mutations or simple lookup queries against DynamoDB and have a
background process transfer documents to OpenSearch Service. You could simply attach the `searchPosts` resolver
to the OpenSearch Service data source and return search results (from data that originated in DynamoDB) using a GraphQL
query. This can be extremely powerful when adding advanced search operations to your applications such
keyword, fuzzy word matches, or even geospatial lookups. Transferring data from DynamoDB could be done through
an ETL process, or alternatively, you could stream from DynamoDB using Lambda.

To get started with these particular data sources, see our [DynamoDB](tutorial-dynamodb-resolvers-js.md "tutorial-dynamodb-resolvers-js.md") and [Lambda](tutorial-lambda-resolvers-js.md "tutorial-lambda-resolvers-js.md") tutorials.

For example, using the schema from our previous tutorial, the following mutation adds an item to
DynamoDB:

```
mutation addPost {
  addPost(
    id: 123
    author: "Nadia"
    title: "Our first post!"
    content: "This is our first post."
    url: "https://aws.amazon.com/appsync/"
  ) {
    id
    author
    title
    content
    url
    ups
    downs
    version
  }
}
```

This writes data to DynamoDB, which then streams data via Lambda to Amazon OpenSearch Service, which you then use to search for
posts by different fields. For example, since the data is in Amazon OpenSearch Service, you can search either the author or
content fields with free-form text, even with spaces, as follows:

```
query searchName{
    searchAuthor(name:"   Nadia   "){
        id
        title
        content
    }
}

---------- or ----------

query searchContent{
    searchContent(text:"test"){
        id
        title
        content
    }
}
```

Because the data is written directly to DynamoDB, you can still perform efficient list or item lookup
operations against the table with the `allPost{...}` and `getPost{...}` queries. This
stack uses the following example code for DynamoDB streams:

###### Note

This Python code is an example and isn't meant to be used in production code.

```
import boto3
import requests
from requests_aws4auth import AWS4Auth

region = '' # e.g. us-east-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = '' # the OpenSearch Service domain, e.g. https://search-mydomain.us-west-1.es.amazonaws.com
index = 'lambda-index'
datatype = '_doc'
url = host + '/' + index + '/' + datatype + '/'

headers = { "Content-Type": "application/json" }

def handler(event, context):
    count = 0
    for record in event['Records']:
        # Get the primary key for use as the OpenSearch ID
        id = record['dynamodb']['Keys']['id']['S']

        if record['eventName'] == 'REMOVE':
            r = requests.delete(url + id, auth=awsauth)
        else:
            document = record['dynamodb']['NewImage']
            r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
        count += 1
    return str(count) + ' records processed.'
```

You can then use DynamoDB streams to attach this to a DynamoDB table with a primary key of
`id`, and any changes to the source of DynamoDB would stream into your OpenSearch Service
domain. For more information about configuring this, see the [DynamoDB Streams documentation](../../../amazondynamodb/latest/developerguide/Streams.md "../../../amazondynamodb/latest/developerguide/Streams.md").
