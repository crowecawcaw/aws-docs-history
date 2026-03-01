# AWS AppSync resolver mapping template context reference

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider
using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

AWS AppSync defines a set of variables and functions for working with resolver mapping
templates. This makes logical operations on data easier with GraphQL. This document describes
those functions and provides examples for working with templates.

## Accessing the `$context`

The `$context` variable is a map that holds all of the contextual information
for your resolver invocation. It has the following structure:

```
{
   "arguments" : { ... },
   "source" : { ... },
   "result" : { ... },
   "identity" : { ... },
   "request" : { ... },
   "info": { ... }
}
```

###### Note

If you're trying to access a dictionary/map entry (such as an entry in
`context`) by its key to retrieve the value, the Velocity Template
Language (VTL) lets you directly use the notation
`<dictionary-element>.<key-name>`. However, this might not
work for all cases, such as when the key names have special characters (for example, an
underscore "\_"). We recommend that you always use
`<dictionary-element>.get("<key-name>")` notation.

Each field in the `$context` map is defined as follows:

### `$context` fields

**`arguments`**

A map that contains all GraphQL arguments for this field.

**`identity`**

An object that contains information about the caller. For more
information about the structure of this field, see [Identity](#aws-appsync-resolver-context-reference-identity "#aws-appsync-resolver-context-reference-identity").

**`source`**

A map that contains the resolution of the parent field.

**`stash`**

The stash is a map that is made available inside each resolver and
function mapping template. The same stash instance lives through a single
resolver execution. This means that you can use the stash to pass arbitrary
data across request and response mapping templates, and across functions in
a pipeline resolver. The stash exposes the same methods as the [Java
Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html "https://docs.oracle.com/javase/8/docs/api/java/util/Map.html") data structure.

**`result`**

A container for the results of this resolver. This field is available
only to response mapping templates.

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

Then the full `$context` variable that is available when
processing a response mapping template might be:

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

If the previous operation was the pipeline resolver's Before mapping
template, then `$ctx.prev.result` represents the output of the
evaluation of the template and is made available to the first function in
the pipeline.

If the previous operation was the first function, then
`$ctx.prev.result` represents the output of the first function
and is made available to the second function in the pipeline.

If the previous operation was the last function, then
`$ctx.prev.result` represents the output of the last function
and is made available to the pipeline resolver's After mapping
template.

**`info`**

An object that contains information about the GraphQL request. For the
structure of this field, see [Info](#aws-appsync-resolver-context-reference-info "#aws-appsync-resolver-context-reference-info").

### Identity

The `identity` section contains information about the caller. The shape of
this section depends on the authorization type of your AWS AppSync API.

For more information about AWS AppSync security options, see [Authorization and authentication](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security").

**`API_KEY` authorization**

The `identity` field isn't populated.

**`AWS_LAMBDA` authorization**

The `identity` contains the `resolverContext` key,
containing the same `resolverContext` content returned by the Lambda
function authorizing the request.

**`AWS_IAM` authorization**

The `identity` has the following form:

```
{
    "accountId" : "string",
    "cognitoIdentityPoolId" : "string",
    "cognitoIdentityId" : "string",
    "sourceIp" : ["string"],
    "username" : "string", // IAM user principal
    "userArn" : "string",
    "cognitoIdentityAuthType" : "string", // authenticated/unauthenticated based on the identity type
    "cognitoIdentityAuthProvider" : "string" // the auth provider that was used to obtain the credentials
}
```

**`AMAZON_COGNITO_USER_POOLS` authorization**

The `identity` has the following form:

```
{
    "sub" : "uuid",
    "issuer" : "string",
    "username" : "string"
    "claims" : { ... },
    "sourceIp" : ["x.x.x.x"],
    "defaultAuthStrategy" : "string"
}
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
GraphQL resolvers by using `$context.request.headers`. You can then use the
header values for actions such as inserting data into a data source or authorization
checks. You can use single or multiple request headers using `$curl` with an
API key from the command line, as shown in the following examples:

**Single header example**

Suppose you set a header of `custom` with a value of `nadia`
like the following:

```
curl -XPOST -H "Content-Type:application/graphql" -H "custom:nadia" -H "x-api-key:<API-KEY-VALUE>" -d '{"query":"mutation { createEvent(name: \"demo\", when: \"Next Friday!\", where: \"Here!\") {id name when where description}}"}' https://<ENDPOINT>/graphql
```

This could then be accessed with `$context.request.headers.custom`. For
example, it might be in the following VTL for DynamoDB:

```
"custom": $util.dynamodb.toDynamoDBJson($context.request.headers.custom)
```

**Multiple header example**

You can also pass multiple headers in a single request and access these in the
resolver mapping template. For example, if the `custom` header is set with
two values:

```
curl -XPOST -H "Content-Type:application/graphql" -H "custom:bailey" -H "custom:nadia" -H "x-api-key:<API-KEY-VALUE>" -d '{"query":"mutation { createEvent(name: \"demo\", when: \"Next Friday!\", where: \"Here!\") {id name when where description}}"}' https://<ENDPOINT>/graphql
```

You could then access these as an array, such as
`$context.request.headers.custom[1]`.

###### Note

AWS AppSync doesn't expose the cookie header in
`$context.request.headers`.

### Access the request custom domain name

AWS AppSync supports configuring a custom domain that you can use to access your GraphQL
and real-time
endpoints
for your APIs. When making a request with a custom domain name, you can get the domain
name using `$context.request.domainName`.

When using the default GraphQL endpoint domain name, the value is
`null`.

### Info

The `info` section contains information about the GraphQL request. This
section has the following form:

```
{
    "fieldName": "string",
    "parentTypeName": "string",
    "variables": { ... },
    "selectionSetList": ["string"],
    "selectionSetGraphQL": "string"
}
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

When using `$utils.toJson()` on `context.info`, the values
that `selectionSetGraphQL` and `selectionSetList` return are
not serialized by default.

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

Then the full `$context.info` variable that is available when processing a
mapping template might be:

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

When calling `$ctx.info.selectionSetList` at the `Query.node`
field resolution, only `id` is exposed:

```
"selectionSetList": [
    "id"
]
```

## Sanitizing inputs

Applications must sanitize untrusted inputs to prevent any external party from using an
application outside of its intended use. As the `$context` contains user inputs
in properties such as `$context.arguments`, `$context.identity`,
`$context.result`, `$context.info.variables`, and
`$context.request.headers`, care must be taken to sanitize their values in
mapping templates.

Since mapping templates represent JSON, input sanitization takes the form of escaping
JSON reserved characters from strings that represent user inputs. It is best practice to
use the `$util.toJson()` utility to escape JSON reserved characters from
sensitive string values when placing them into a mapping template.

For example, in the following Lambda request mapping template, because we accessed an
unsafe customer input string (`$context.arguments.id`), we wrapped it with
`$util.toJson()` to prevent unescaped JSON characters from breaking the JSON
template.

```
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "getPost",
        "postId": $util.toJson($context.arguments.id)
    }
}
```

As opposed to the mapping template below, where we directly insert
`$context.arguments.id` without sanitization. This does not work for strings
containing unescaped quotation marks or other JSON reserved characters, and can leave your
template open to failure.

```
## DO NOT DO THIS
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "getPost",
        "postId": "$context.arguments.id" ## Unsafe! Do not insert $context string values without escaping JSON characters.
    }
}
```
