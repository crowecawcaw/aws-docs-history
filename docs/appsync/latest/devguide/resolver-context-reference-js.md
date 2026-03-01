# AWS AppSync JavaScript resolver context object reference

AWS AppSync defines a set of variables and functions for working with request and response
handlers. This makes logical operations on data easier with GraphQL. This document describes
those functions and provides examples.

## Accessing the `context`

The `context` argument of a request and response handler is an object that
holds all of the contextual information for your resolver invocation. It has the following
structure:

```
type Context = {
  arguments: any;
  args: any;
  identity: Identity;
  source: any;
  error?: {
    message: string;
    type: string;
  };
  stash: any;
  result: any;
  prev: any;
  request: Request;
  info: Info;
};
```

###### Note

You will often find that the `context` object is referred to as
`ctx`.

Each field in the `context` object is defined as follows:

### `context` fields

**`arguments`**

A map that contains all GraphQL arguments for this field.

**`identity`**

An object that contains information about the caller. For more information
about the structure of this field, see [Identity](#aws-appsync-resolver-context-reference-identity-js "#aws-appsync-resolver-context-reference-identity-js").

**`source`**

A map that contains the resolution of the parent field.

**`stash`**

The stash is an object that is made available inside each resolver and
function handler. The same stash object lives through a single resolver run.
This means that you can use the stash to pass arbitrary data across request and
response handlers and across functions in a pipeline resolver.

###### Note

You cannot delete or replace the entire stash, but you can add, update,
delete, and read properties of the stash.

You can add items to the stash by modifying one of the code examples
below:

```
//Example 1
ctx.stash.newItem = { key: "something" }

//Example 2
Object.assign(ctx.stash, {key1: value1, key2: value})
```

You can remove items from the stash by modifying the code below:

```
delete ctx.stash.key
```

**`result`**

A container for the results of this resolver. This field is available only
to response handlers.

For example, if you're resolving the `author` field of the
following query:

```
query {
    getPost(id: 1234) {
        postId
        title
        content
        author {
            id
            name
        }
    }
}
```

Then the full `context` variable is available when a response
handler is evaluated:

```
{
  "arguments" : {
    id: "1234"
  },
  "source": {},
  "result" : {
      "postId": "1234",
      "title": "Some title",
      "content": "Some content",
      "author": {
        "id": "5678",
        "name": "Author Name"
      }
  },
  "identity" : {
      "sourceIp" : ["x.x.x.x"],
      "userArn" : "arn:aws:iam::123456789012:user/appsync",
      "accountId" : "666666666666",
      "user" : "AIDAAAAAAAAAAAAAAAAAA"
  }
}
```

**`prev.result`**

The result of whatever previous operation was executed in a pipeline
resolver.

If the previous operation was the pipeline resolver's request handler, then
`ctx.prev.result` represents that evaluation result and is made
available to the first function in the pipeline.

If the previous operation was the first function, then
`ctx.prev.result` represents the evaluation result of the first
function response handler and is made available to the second function in the
pipeline.

If the previous operation was the last function, then
`ctx.prev.result` represents the evaluation result of the last
function and is made available to the pipeline resolver's response
handler.

**`info`**

An object that contains information about the GraphQL request. For the
structure of this field, see [Info](#aws-appsync-resolver-context-reference-info-js "#aws-appsync-resolver-context-reference-info-js").

### Identity

The `identity` section contains information about the caller. The shape of
this section depends on the authorization type of your AWS AppSync API.

For more information about AWS AppSync security options, see [Authorization and authentication](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security").

**`API_KEY` authorization**

The `identity` field isn't populated.

**`AWS_LAMBDA` authorization**

The `identity` has the following form:

```
type AppSyncIdentityLambda = {
  resolverContext: any;
};
```

The `identity` contains the `resolverContext` key,
containing the same `resolverContext` content returned by the Lambda
function authorizing the request.

**`AWS_IAM` authorization**

The `identity` has the following form:

```
type AppSyncIdentityIAM = {
  accountId: string;
  cognitoIdentityPoolId: string;
  cognitoIdentityId: string;
  sourceIp: string[];
  username: string;
  userArn: string;
  cognitoIdentityAuthType: string;
  cognitoIdentityAuthProvider: string;
};
```

**`AMAZON_COGNITO_USER_POOLS` authorization**

The `identity` has the following form:

```
type AppSyncIdentityCognito = {
  sourceIp: string[];
  username: string;
  groups: string[] | null;
  sub: string;
  issuer: string;
  claims: any;
  defaultAuthStrategy: string;
};
```

Each field is defined as follows:

**`accountId`**

The AWS account ID of the caller.

**`claims`**

The claims that the user has.

**`cognitoIdentityAuthType`**

Either authenticated or unauthenticated based on the identity type.

**`cognitoIdentityAuthProvider`**

A comma-separated list of external identity provider information used in
obtaining the credentials used to sign the request.

**`cognitoIdentityId`**

The Amazon Cognito identity ID of the caller.

**`cognitoIdentityPoolId`**

The Amazon Cognito identity pool ID associated with the caller.

**`defaultAuthStrategy`**

The default authorization strategy for this caller (`ALLOW` or
`DENY`).

**`issuer`**

The token issuer.

**`sourceIp`**

The source IP address of the caller that AWS AppSync receives. If the request
doesn't include the `x-forwarded-for` header, the source IP value
contains only a single IP address from the TCP connection. If the request
includes a `x-forwarded-for` header, the source IP is a list of IP
addresses from the `x-forwarded-for` header, in addition to the IP
address from the TCP connection.

**`sub`**

The UUID of the authenticated user.

**`user`**

The IAM user.

**`userArn`**

The Amazon Resource Name (ARN) of the IAM user.

**`username`**

The user name of the authenticated user. In the case of
`AMAZON_COGNITO_USER_POOLS` authorization, the value of _username_ is the value of attribute
_cognito:username_. In the case of
`AWS_IAM` authorization, the value of _username_ is the value of the AWS user
principal. If you're using IAM authorization with credentials vended from
Amazon Cognito identity pools, we recommend that you use
`cognitoIdentityId`.

### Access request headers

AWS AppSync supports passing custom headers from clients and accessing them in your
GraphQL resolvers by using `ctx.request.headers`. You can then use the header
values for actions such as inserting data into a data source or authorization checks.
You can use single or multiple request headers using `$curl` with an API key
from the command line, as shown in the following examples:

**Single header example**

Suppose you set a header of `custom` with a value of `nadia`
like the following:

```
curl -XPOST -H "Content-Type:application/graphql" -H "custom:nadia" -H "x-api-key:<API-KEY-VALUE>" -d '{"query":"mutation { createEvent(name: \"demo\", when: \"Next Friday!\", where: \"Here!\") {id name when where description}}"}' https://<ENDPOINT>/graphql
```

This could then be accessed with `ctx.request.headers.custom`. For
example, it might be in the following code for DynamoDB:

```
"custom": util.dynamodb.toDynamoDB(ctx.request.headers.custom)
```

**Multiple header example**

You can also pass multiple headers in a single request and access these in the
resolver handler. For example, if the `custom` header is set with two
values:

```
curl -XPOST -H "Content-Type:application/graphql" -H "custom:bailey" -H "custom:nadia" -H "x-api-key:<API-KEY-VALUE>" -d '{"query":"mutation { createEvent(name: \"demo\", when: \"Next Friday!\", where: \"Here!\") {id name when where description}}"}' https://<ENDPOINT>/graphql
```

You could then access these as an array, such as
`ctx.request.headers.custom[1]`.

###### Note

AWS AppSync doesn't expose the cookie header in
`ctx.request.headers`.

### Access the request custom domain name

AWS AppSync supports configuring a custom domain that you can use to access your GraphQL
and real-time endpoints for your APIs. When making a request with a custom domain name,
you can get the domain name using `ctx.request.domainName`.

When using the default GraphQL endpoint domain name, the value is
`null`.

### Info

The `info` section contains information about the GraphQL request. This
section has the following form:

```
type Info = {
  fieldName: string;
  parentTypeName: string;
  variables: any;
  selectionSetList: string[];
  selectionSetGraphQL: string;
};
```

Each field is defined as follows:

**`fieldName`**

The name of the field that is currently being resolved.

**`parentTypeName`**

The name of the parent type for the field that is currently being
resolved.

**`variables`**

A map which holds all variables that are passed into the GraphQL
request.

**`selectionSetList`**

A list representation of the fields in the GraphQL selection set. Fields
that are aliased are referenced only by the alias name, not the field name. The
following example shows this in detail.

**`selectionSetGraphQL`**

A string representation of the selection set, formatted as GraphQL schema
definition language (SDL). Although fragments aren't merged into the selection
set, inline fragments are preserved, as shown in the following example.

###### Note

`JSON.stringify` will not include `selectionSetGraphQL` and
`selectionSetList` in the string serialization. You must reference
these properties directly.

For example, if you are resolving the `getPost` field of the following
query:

```
query {
  getPost(id: $postId) {
    postId
    title
    secondTitle: title
    content
    author(id: $authorId) {
      authorId
      name
    }
    secondAuthor(id: "789") {
      authorId
    }
    ... on Post {
      inlineFrag: comments: {
        id
      }
    }
    ... postFrag
  }
}

fragment postFrag on Post {
  postFrag: comments: {
    id
  }
}
```

Then the full `ctx.info` variable that is available when processing a
handler might be:

```
{
  "fieldName": "getPost",
  "parentTypeName": "Query",
  "variables": {
    "postId": "123",
    "authorId": "456"
  },
  "selectionSetList": [
    "postId",
    "title",
    "secondTitle"
    "content",
    "author",
    "author/authorId",
    "author/name",
    "secondAuthor",
    "secondAuthor/authorId",
    "inlineFragComments",
    "inlineFragComments/id",
    "postFragComments",
    "postFragComments/id"
  ],
  "selectionSetGraphQL": "{\n  getPost(id: $postId) {\n    postId\n    title\n    secondTitle: title\n    content\n    author(id: $authorId) {\n      authorId\n      name\n    }\n    secondAuthor(id: \"789\") {\n      authorId\n    }\n    ... on Post {\n      inlineFrag: comments {\n        id\n      }\n    }\n    ... postFrag\n  }\n}"
}
```

`selectionSetList` exposes only fields that belong to the current type. If
the current type is an interface or union, only selected fields that belong to the
interface are exposed. For example, given the following schema:

```
type Query {
    node(id: ID!): Node
}

interface Node {
    id: ID
}

type Post implements Node {
    id: ID
    title: String
    author: String
}

type Blog implements Node {
    id: ID
    title: String
    category: String
}
```

And the following query:

```
query {
    node(id: "post1") {
        id
        ... on Post {
            title
        }

        ... on Blog {
            title
        }
    }
}
```

When calling `ctx.info.selectionSetList` at the `Query.node`
field resolution, only `id` is exposed:

```
"selectionSetList": [
    "id"
]
```
