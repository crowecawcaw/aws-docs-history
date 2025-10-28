# Using AWS Lambda resolvers in AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](tutorials-js.md "tutorials-js.md").

You can use AWS Lambda with AWS AppSync to resolve any GraphQL field. For example, a GraphQL
query might send a call to an Amazon Relational Database Service (Amazon RDS) instance, and a GraphQL mutation might write
to an Amazon Kinesis stream. In this section, we'll show you how to write a Lambda function that
performs business logic based on the invocation of a GraphQL field operation.

## Create a Lambda function

The following example shows a Lambda function written in `Node.js` that
performs different operations on blog posts as part of a blog post application.

```
exports.handler = (event, context, callback) => {
    console.log("Received event {}", JSON.stringify(event, 3));
    var posts = {
         "1": {"id": "1", "title": "First book", "author": "Author1", "url": "https://amazon.com/", "content": "SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1", "ups": "100", "downs": "10"},
         "2": {"id": "2", "title": "Second book", "author": "Author2", "url": "https://amazon.com", "content": "SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT", "ups": "100", "downs": "10"},
         "3": {"id": "3", "title": "Third book", "author": "Author3", "url": null, "content": null, "ups": null, "downs": null },
         "4": {"id": "4", "title": "Fourth book", "author": "Author4", "url": "https://www.amazon.com/", "content": "SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4", "ups": "1000", "downs": "0"},
         "5": {"id": "5", "title": "Fifth book", "author": "Author5", "url": "https://www.amazon.com/", "content": "SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT", "ups": "50", "downs": "0"} };

    var relatedPosts = {
        "1": [posts['4']],
        "2": [posts['3'], posts['5']],
        "3": [posts['2'], posts['1']],
        "4": [posts['2'], posts['1']],
        "5": []
    };

    console.log("Got an Invoke Request.");
    switch(event.field) {
        case "getPost":
            var id = event.arguments.id;
            callback(null, posts[id]);
            break;
        case "allPosts":
            var values = [];
            for(var d in posts){
                values.push(posts[d]);
            }
            callback(null, values);
            break;
        case "addPost":
            // return the arguments back
            callback(null, event.arguments);
            break;
        case "addPostErrorWithData":
            var id = event.arguments.id;
            var result = posts[id];
            // attached additional error information to the post
            result.errorMessage = 'Error with the mutation, data has changed';
            result.errorType = 'MUTATION_ERROR';
            callback(null, result);
            break;
        case "relatedPosts":
            var id = event.source.id;
            callback(null, relatedPosts[id]);
            break;
        default:
            callback("Unknown field, unable to resolve" + event.field, null);
            break;
    }
};
```

This Lambda function retrieves a post by ID, adds a post, retrieves a list of posts,
and fetches related posts for a given post.

**Note:** The Lambda function uses the `switch`
statement on `event.field` to determine which field is currently being
resolved.

Create this Lambda function using the AWS Management Console or an AWS CloudFormation stack.
To create the function from a CloudFormation stack, you can use the following AWS Command Line Interface
(AWS CLI) command:

```
aws cloudformation create-stack --stack-name AppSyncLambdaExample \
--template-url https://s3.us-west-2.amazonaws.com/awsappsync/resources/lambda/LambdaCFTemplate.yaml \
--capabilities CAPABILITY_NAMED_IAM
```

You can also launch the AWS CloudFormation stack in the US West (Oregon) AWS Region in your
AWS account from here:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/lambda/LambdaCFTemplate.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/lambda/LambdaCFTemplate.yaml")

## Configure a data source for

Lambda

After you create the Lambda function, navigate to your GraphQL API in the AWS AppSync
console, and then choose the **Data Sources** tab.

Choose **Create data source**, enter a friendly **Data source
name** (for example, `Lambda`), and then for
**Data source type**, choose **AWS Lambda
function**. For **Region**, choose the same Region as your
function. (If you created the function from the provided CloudFormation stack, the function
is probably in **US-WEST-2**.) For **Function ARN**,
choose the Amazon Resource Name (ARN) of your Lambda function.

After choosing your Lambda function, you can either create a new AWS Identity and Access Management (IAM) role
(for which AWS AppSync assigns the appropriate permissions) or choose an existing role
that has the following inline policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:LAMBDA_FUNCTION"
 }
 ]
}`

```

You must also set up a trust relationship with AWS AppSync for the IAM role as
follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "appsync.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Create

a GraphQL schema

Now that the data source is connected to your Lambda function, create a GraphQL
schema.

From the schema editor in the AWS AppSync console, make sure that your schema matches
the following schema:

```
schema {
    query: Query
    mutation: Mutation
}

type Query {
    getPost(id:ID!): Post
    allPosts: [Post]
}

type Mutation {
    addPost(id: ID!, author: String!, title: String, content: String, url: String): Post!
}

type Post {
    id: ID!
    author: String!
    title: String
    content: String
    url: String
    ups: Int
    downs: Int
    relatedPosts: [Post]
}
```

## Configure resolvers

Now that you've registered a Lambda data source and a valid GraphQL schema, you can
connect your GraphQL fields to your Lambda data source using resolvers.

To create a resolver, you'll need mapping templates. To learn more about mapping
templates, see [Resolver Mapping Template Overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview").

For more information about Lambda mapping templates, see [Resolver mapping template reference for Lambda](resolver-mapping-template-reference-lambda.md#aws-appsync-resolver-mapping-template-reference-lambda "resolver-mapping-template-reference-lambda.md#aws-appsync-resolver-mapping-template-reference-lambda").

In this step, you attach a resolver to the Lambda function for the following fields:
`getPost(id:ID!): Post`, `allPosts: [Post]`, `addPost(id:
 ID!, author: String!, title: String, content: String, url: String): Post!`,
and `Post.relatedPosts: [Post]`.

From the schema editor in the AWS AppSync console, on the right side, choose **Attach Resolver** for `getPost(id:ID!):
 Post`.

Then, in the **Action menu**, choose **Update
runtime**, then choose **Unit Resolver (VTL only)**.

Afterward, choose your Lambda data source. In the **request mapping template**
section, choose **Invoke And Forward Arguments**.

Modify the `payload` object to add the field name. Your template should
look like the following:

```
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "getPost",
        "arguments":  $utils.toJson($context.arguments)
    }
}
```

In the **response mapping template** section, choose
**Return Lambda Result**.

In this case, use the base template as-is. It should look like the following:

```
$utils.toJson($context.result)
```

Choose **Save**. You have successfully attached your
first resolver. Repeat this operation for the remaining fields as follows:

For `addPost(id: ID!, author: String!, title: String, content: String, url:
 String): Post!` request mapping template:

```
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "addPost",
        "arguments":  $utils.toJson($context.arguments)
    }
}
```

For `addPost(id: ID!, author: String!, title: String, content: String, url:
 String): Post!` response mapping template:

```
$utils.toJson($context.result)
```

For `allPosts: [Post]` request mapping template:

```
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "allPosts"
    }
}
```

For `allPosts: [Post]` response mapping template:

```
$utils.toJson($context.result)
```

For `Post.relatedPosts: [Post]` request mapping template:

```
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "relatedPosts",
        "source":  $utils.toJson($context.source)
    }
}
```

For `Post.relatedPosts: [Post]` response mapping template:

```
$utils.toJson($context.result)
```

## Test your GraphQL API

Now that your Lambda function is connected to GraphQL resolvers, you can run some
mutations and queries using the console or a client application.

On the left side of the AWS AppSync console, choose **Queries**, and then paste in the following code:

### addPost Mutation

```
mutation addPost {
    addPost(
        id: 6
        author: "Author6"
        title: "Sixth book"
        url: "https://www.amazon.com/"
        content: "This is the book is a tutorial for using GraphQL with AWS AppSync."
    ) {
        id
        author
        title
        content
        url
        ups
        downs
    }
}
```

### getPost Query

```
query getPost {
    getPost(id: "2") {
        id
        author
        title
        content
        url
        ups
        downs
    }
}
```

### allPosts Query

```
query allPosts {
    allPosts {
        id
        author
        title
        content
        url
        ups
        downs
        relatedPosts {
            id
            title
        }
    }
}
```

## Returning errors

Any given field resolution can result in an error. With AWS AppSync, you can raise
errors from the following sources:

- Request or response mapping template
- Lambda function

### From the mapping template

To raise intentional errors, you can use the `$utils.error` helper
method from the Velocity Template Language (VTL) template. It takes as argument an
`errorMessage`, an `errorType`, and an optional
`data` value. The `data` is useful for returning extra
data back to the client when an error occurs. The `data` object is added
to the `errors` in the GraphQL final response.

The following example shows how to use it in the `Post.relatedPosts:
 [Post]` response mapping template:

```
$utils.error("Failed to fetch relatedPosts", "LambdaFailure", $context.result)
```

This yields a GraphQL response similar to the following:

```
{
    "data": {
        "allPosts": [
            {
                "id": "2",
                "title": "Second book",
                "relatedPosts": null
            },
            ...
        ]
    },
    "errors": [
        {
            "path": [
                "allPosts",
                0,
                "relatedPosts"
            ],
            "errorType": "LambdaFailure",
            "locations": [
                {
                    "line": 5,
                    "column": 5
                }
            ],
            "message": "Failed to fetch relatedPosts",
            "data": [
                {
                  "id": "2",
                  "title": "Second book"
                },
                {
                  "id": "1",
                  "title": "First book"
                }
            ]
        }
    ]
}
```

Where `allPosts[0].relatedPosts` is _null_ because of the error and the `errorMessage`,
`errorType`, and `data` are present in the
`data.errors[0]` object.

### From the Lambda function

AWS AppSync also understands errors that the Lambda function throws. The Lambda
programming model lets you raise _handled_
errors. If the Lambda function throws an error, AWS AppSync fails to resolve the
current field. Only the error message returned from Lambda is set in the response.
Currently, you can't pass any extraneous data back to the client by raising an error
from the Lambda function.

**Note**: If your Lambda function raises an _unhandled_ error, AWS AppSync uses the error
message that Lambda set.

The following Lambda function raises an error:

```
exports.handler = (event, context, callback) => {
    console.log("Received event {}", JSON.stringify(event, 3));
    callback("I fail. Always.");
};
```

This returns a GraphQL response similar to the following:

```
{
    "data": {
        "allPosts": [
            {
                "id": "2",
                "title": "Second book",
                "relatedPosts": null
            },
            ...
        ]
    },
    "errors": [
        {
            "path": [
                "allPosts",
                0,
                "relatedPosts"
            ],
            "errorType": "Lambda:Handled",
            "locations": [
                {
                    "line": 5,
                    "column": 5
                }
            ],
            "message": "I fail. Always."
        }
    ]
}
```

## Advanced use case: Batching

The Lambda function in this example has a `relatedPosts` field that returns
a list of related posts for a given post. In the example queries, the
`allPosts` field invocation from the Lambda function returns five posts.
Because we specified that we also want to resolve `relatedPosts` for each
returned post, the `relatedPosts` field operation is invoked five
times.

```
query allPosts {
    allPosts {   // 1 Lambda invocation - yields 5 Posts
        id
        author
        title
        content
        url
        ups
        downs
        relatedPosts {   // 5 Lambda invocations - each yields 5 posts
            id
            title
        }
    }
}
```

While this might not sound substantial in this specific example, this compounded
over-fetching can quickly undermine the application.

If you were to fetch `relatedPosts` again on the returned related
`Posts` in the same query, the number of invocations would increase
dramatically.

```
query allPosts {
    allPosts {   // 1 Lambda invocation - yields 5 Posts
        id
        author
        title
        content
        url
        ups
        downs
        relatedPosts {   // 5 Lambda invocations - each yield 5 posts = 5 x 5 Posts
            id
            title
            relatedPosts {  // 5 x 5 Lambda invocations - each yield 5 posts = 25 x 5 Posts
                id
                title
                author
            }
        }
    }
}
```

In this relatively simple query, AWS AppSync would invoke the Lambda function 1 + 5 + 25
= 31 times.

This is a fairly common challenge and is often called the N+1 problem (in this case, N
= 5), and it can incur increased latency and cost to the application.

One approach to solving this issue is to batch similar field resolver requests
together. In this example, instead of having the Lambda function resolve a list of
related posts for a single given post, it could instead resolve a list of related posts
for a given batch of posts.

To demonstrate this, let's switch the `Post.relatedPosts: [Post]` resolver
to a batch-enabled resolver.

On the right side of the AWS AppSync console, choose the existing
`Post.relatedPosts: [Post]` resolver. Change the request mapping template
to the following:

```
{
    "version": "2017-02-28",
    "operation": "BatchInvoke",
    "payload": {
        "field": "relatedPosts",
        "source":  $utils.toJson($context.source)
    }
}
```

Only the `operation` field has changed from `Invoke` to
`BatchInvoke`. The payload field now becomes an array of whatever is
specified in the template. In this example, the Lambda function receives the following as
input:

```
[
    {
        "field": "relatedPosts",
        "source": {
            "id": 1
        }
    },
    {
        "field": "relatedPosts",
        "source": {
            "id": 2
        }
    },
    ...
]
```

When `BatchInvoke` is specified in the request mapping template, the Lambda
function receives a list of requests and returns a list of results.

Specifically, the list of results must match the size and order of the request payload
entries so that AWS AppSync can match the results accordingly.

In this batching example, the Lambda function returns a batch of results as
follows:

```
[
    [{"id":"2","title":"Second book"}, {"id":"3","title":"Third book"}],   // relatedPosts for id=1
    [{"id":"3","title":"Third book"}]                                                             // relatedPosts for id=2
]
```

The following Lambda function in Node.js demonstrates this batching functionality for
the `Post.relatedPosts` field as follows:

```
exports.handler = (event, context, callback) => {
    console.log("Received event {}", JSON.stringify(event, 3));
    var posts = {
         "1": {"id": "1", "title": "First book", "author": "Author1", "url": "https://amazon.com/", "content": "SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1", "ups": "100", "downs": "10"},
         "2": {"id": "2", "title": "Second book", "author": "Author2", "url": "https://amazon.com", "content": "SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT", "ups": "100", "downs": "10"},
         "3": {"id": "3", "title": "Third book", "author": "Author3", "url": null, "content": null, "ups": null, "downs": null },
         "4": {"id": "4", "title": "Fourth book", "author": "Author4", "url": "https://www.amazon.com/", "content": "SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4", "ups": "1000", "downs": "0"},
         "5": {"id": "5", "title": "Fifth book", "author": "Author5", "url": "https://www.amazon.com/", "content": "SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT", "ups": "50", "downs": "0"} };

    var relatedPosts = {
        "1": [posts['4']],
        "2": [posts['3'], posts['5']],
        "3": [posts['2'], posts['1']],
        "4": [posts['2'], posts['1']],
        "5": []
    };

    console.log("Got a BatchInvoke Request. The payload has %d items to resolve.", event.length);
    // event is now an array
    var field = event[0].field;
    switch(field) {
        case "relatedPosts":
            var results = [];
            // the response MUST contain the same number
            // of entries as the payload array
            for (var i=0; i< event.length; i++) {
                console.log("post {}", JSON.stringify(event[i].source));
                results.push(relatedPosts[event[i].source.id]);
            }
            console.log("results {}", JSON.stringify(results));
            callback(null, results);
            break;
        default:
            callback("Unknown field, unable to resolve" + field, null);
            break;
    }
};
```

### Returning individual errors

The previous examples show that it's possible to return a single error from the
Lambda function or raise an error from the mapping templates. For batched
invocations, raising an error from the Lambda function flags an entire batch as
failed. This might be acceptable for specific scenarios where an irrecoverable error
occurs, such as a failed connection to a data store. However, in cases where some
items in the batch succeed and others fail, it's possible to return both errors and
valid data. Because AWS AppSync requires the batch response to list elements matching
the original size of the batch, you must define a data structure that can
differentiate valid data from an error.

For example, if the Lambda function is expected to return a batch of related posts,
you could choose to return a list of `Response` objects where each object
has optional _data_, _errorMessage_, and _errorType_ fields. If the _errorMessage_ field is present, it means that
an error occurred.

The following code shows how you could update the Lambda function:

```
exports.handler = (event, context, callback) => {
    console.log("Received event {}", JSON.stringify(event, 3));
    var posts = {
         "1": {"id": "1", "title": "First book", "author": "Author1", "url": "https://amazon.com/", "content": "SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1 SAMPLE TEXT AUTHOR 1", "ups": "100", "downs": "10"},
         "2": {"id": "2", "title": "Second book", "author": "Author2", "url": "https://amazon.com", "content": "SAMPLE TEXT AUTHOR 2 SAMPLE TEXT AUTHOR 2 SAMPLE TEXT", "ups": "100", "downs": "10"},
         "3": {"id": "3", "title": "Third book", "author": "Author3", "url": null, "content": null, "ups": null, "downs": null },
         "4": {"id": "4", "title": "Fourth book", "author": "Author4", "url": "https://www.amazon.com/", "content": "SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4 SAMPLE TEXT AUTHOR 4", "ups": "1000", "downs": "0"},
         "5": {"id": "5", "title": "Fifth book", "author": "Author5", "url": "https://www.amazon.com/", "content": "SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT AUTHOR 5 SAMPLE TEXT", "ups": "50", "downs": "0"} };

    var relatedPosts = {
        "1": [posts['4']],
        "2": [posts['3'], posts['5']],
        "3": [posts['2'], posts['1']],
        "4": [posts['2'], posts['1']],
        "5": []
    };

    console.log("Got a BatchInvoke Request. The payload has %d items to resolve.", event.length);
    // event is now an array
    var field = event[0].field;
    switch(field) {
        case "relatedPosts":
            var results = [];
            results.push({ 'data': relatedPosts['1'] });
            results.push({ 'data': relatedPosts['2'] });
            results.push({ 'data': null, 'errorMessage': 'Error Happened', 'errorType': 'ERROR' });
            results.push(null);
            results.push({ 'data': relatedPosts['3'], 'errorMessage': 'Error Happened with last result', 'errorType': 'ERROR' });
            callback(null, results);
            break;
        default:
            callback("Unknown field, unable to resolve" + field, null);
            break;
    }
};
```

For this example, the following response mapping template parses each item of the
Lambda function and raises any errors that occur:

```
#if( $context.result && $context.result.errorMessage )
    $utils.error($context.result.errorMessage, $context.result.errorType, $context.result.data)
#else
    $utils.toJson($context.result.data)
#end
```

This example returns a GraphQL response similar to the following:

```
{
  "data": {
    "allPosts": [
      {
        "id": "1",
        "relatedPostsPartialErrors": [
          {
            "id": "4",
            "title": "Fourth book"
          }
        ]
      },
      {
        "id": "2",
        "relatedPostsPartialErrors": [
          {
            "id": "3",
            "title": "Third book"
          },
          {
            "id": "5",
            "title": "Fifth book"
          }
        ]
      },
      {
        "id": "3",
        "relatedPostsPartialErrors": null
      },
      {
        "id": "4",
        "relatedPostsPartialErrors": null
      },
      {
        "id": "5",
        "relatedPostsPartialErrors": null
      }
    ]
  },
  "errors": [
    {
      "path": [
        "allPosts",
        2,
        "relatedPostsPartialErrors"
      ],
      "errorType": "ERROR",
      "locations": [
        {
          "line": 4,
          "column": 9
        }
      ],
      "message": "Error Happened"
    },
    {
      "path": [
        "allPosts",
        4,
        "relatedPostsPartialErrors"
      ],
      "data": [
        {
          "id": "2",
          "title": "Second book"
        },
        {
          "id": "1",
          "title": "First book"
        }
      ],
      "errorType": "ERROR",
      "locations": [
        {
          "line": 4,
          "column": 9
        }
      ],
      "message": "Error Happened with last result"
    }
  ]
}
```

### Configuring the maximum batching

size

By default, when using `BatchInvoke`, AWS AppSync sends requests to your
Lambda function in batches of up to five items. You can configure the maximum batch
size of your Lambda resolvers.

To configure the maximum batching size on a resolver, use the following command in
the AWS Command Line Interface (AWS CLI):

```
$ aws appsync create-resolver --api-id <api-id> --type-name Query --field-name relatedPosts \
 --request-mapping-template "<template>" --response-mapping-template "<template>" --data-source-name "<lambda-datasource>" \
 --max-batch-size X
```

###### Note

When providing a request mapping template, you must use the
`BatchInvoke` operation to use batching.

You can also use the following command to enable and configure batching on Direct
Lambda Resolvers:

```
$ aws appsync create-resolver --api-id <api-id> --type-name Query --field-name relatedPosts \
 --data-source-name "<lambda-datasource>" \
 --max-batch-size X
```

### Maximum batching size configuration

with VTL templates

For Lambda Resolvers that have VTL in-request templates, the maximum batch size
will have no effect unless they have directly specified it as a
`BatchInvoke` operation in VTL. Similarly, if you are performing a
top-level mutation, batching is not conducted for mutations because the GraphQL
specification requires parallel mutations to be executed sequentially.

For example, take the following mutations:

```
type Mutation {
    putItem(input: Item): Item
    putItems(inputs: [Item]): [Item]
}

```

Using the first mutation, we can create 10 `Items` as shown in the
snippet below:

```
mutation MyMutation {
    v1: putItem($someItem1) {
        id,
        name
    }
    v2: putItem($someItem2) {
        id,
        name
    }
    v3: putItem($someItem3) {
        id,
        name
    }
    v4: putItem($someItem4) {
        id,
        name
    }
    v5: putItem($someItem5) {
        id,
        name
    }
    v6: putItem($someItem6) {
        id,
        name
    }
    v7: putItem($someItem7) {
        id,
        name
    }
    v8: putItem($someItem8) {
        id,
        name
    }
    v9: putItem($someItem9) {
        id,
        name
    }
    v10: putItem($someItem10) {
        id,
        name
    }
}
```

In this example, the `Items` will not be batched in a group of 10 even
if the maximum batch size is set to 10 in the Lambda Resolver. Instead, they will
execute sequentially according to the GraphQL specification.

To perform an actual batch mutation, you may follow the example below using the
second mutation:

```
mutation MyMutation {
    putItems([$someItem1, $someItem2, $someItem3,$someItem4, $someItem5, $someItem6,
    $someItem7, $someItem8, $someItem9, $someItem10]) {
    id,
    name
    }
}
```

For more information about using batching with Direct Lambda Resolvers, see [Direct Lambda Resolvers](resolver-mapping-template-reference-lambda.md#direct-lambda-resolvers "resolver-mapping-template-reference-lambda.md#direct-lambda-resolvers").
