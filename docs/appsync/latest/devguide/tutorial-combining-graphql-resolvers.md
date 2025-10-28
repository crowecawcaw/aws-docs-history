# Combining GraphQL resolvers in

AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](tutorials-js.md "tutorials-js.md").

Resolvers and fields in a GraphQL schema have 1:1 relationships with a large degree of
flexibility. Because a data source is configured on a resolver independently of a schema,
you have the ability for GraphQL types to be resolved or manipulated through different data
sources, mixing and matching on a schema to best meet your needs.

The following example scenarios demonstrate how to mix and match data sources in your
schema. Before you begin, we recommend that you are familiar with setting up data sources and
resolvers for AWS Lambda, Amazon DynamoDB, and Amazon OpenSearch Service as described in the previous
tutorials.

## Example schema

The following schema has a type of `Post` with 3 `Query` operations
and 3 `Mutation` operations defined:

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

In this example you would have a total of 6 resolvers to attach. One possible way
would to have all of these come from an Amazon DynamoDB table, called `Posts`,
where `AllPosts` runs a scan and `searchPosts` runs a query, as
outlined in the [DynamoDB Resolver Mapping Template Reference](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb"). However, there are
alternatives to meet your business needs, such as having these GraphQL queries resolve
from Lambda or OpenSearch Service.

## Alter data through resolvers

You might have the need to return results from a database such as DynamoDB (or Amazon
Aurora) to clients with some of the attributes changed. This might be due to formatting
of the data types, such as timestamp differences on clients, or to handle backwards
compatibility issues. For illustrative purposes, in the following example, an
AWS Lambda function manipulates the up-votes and down-votes for blog posts by
assigning them random numbers each time the GraphQL resolver is invoked:

```
'use strict';
const doc = require('dynamodb-doc');
const dynamo = new doc.DynamoDB();

exports.handler = (event, context, callback) => {
    const payload = {
        TableName: 'Posts',
        Limit: 50,
        Select: 'ALL_ATTRIBUTES',
    };

    dynamo.scan(payload, (err, data) => {
        const result = { data: data.Items.map(item =>{
            item.ups = parseInt(Math.random() * (50 - 10) + 10, 10);
            item.downs = parseInt(Math.random() * (20 - 0) + 0, 10);
            return item;
        }) };
        callback(err, result.data);
    });
};
```

This is a perfectly valid Lambda function and could be attached to the
`AllPosts` field in the GraphQL schema so that any query returning all
the results gets random numbers for the ups/downs.

## DynamoDB and OpenSearch Service

For some applications, you might perform mutations or simple lookup queries against
DynamoDB, and have a background process transfer documents to OpenSearch Service. You can then simply
attach the `searchPosts` Resolver to the OpenSearch Service data source and return search
results (from data that originated in DynamoDB) using a GraphQL query. This can be
extremely powerful when adding advanced search operations to your applications such
keyword, fuzzy word matches or even geospatial lookups. Transferring data from DynamoDB
could be done through an ETL process or alternatively you can stream from DynamoDB using
Lambda. You can launch a complete example of this using the following AWS CloudFormation stack in
the US West 2 (Oregon) Region in your AWS account:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/multipledatasource/appsyncesdbstream.yml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/multipledatasource/appsyncesdbstream.yml")

The schema in this example lets you add posts using a DynamoDB resolver as
follows:

```
mutation add {
    putPost(author:"Nadia"
        title:"My first post"
        content:"This is some test content"
        url:"https://aws.amazon.com/appsync/"
    ){
        id
        title
    }
}
```

This writes data to DynamoDB which then streams data via Lambda to Amazon OpenSearch Service which you
could search for all posts by different fields. For example, since the data is in
Amazon OpenSearch Service you can search either the author or content fields with free-form text, even
with spaces, as follows:

```
query searchName{
    searchAuthor(name:"   Nadia   "){
        id
        title
        content
    }
}

query searchContent{
    searchContent(text:"test"){
        id
        title
        content
    }
}
```

Because the data is written directly to DynamoDB, you can still perform efficient list or
item lookup operations against the table with the `allPosts{...}` and
`singlePost{...}` queries. This stack uses the following example code for
DynamoDB streams:

**Note:** This code is for example only.

```
var AWS = require('aws-sdk');
var path = require('path');
var stream = require('stream');

var esDomain = {
    endpoint: 'https://opensearch-domain-name.REGION.es.amazonaws.com',
    region: 'REGION',
    index: 'id',
    doctype: 'post'
};

var endpoint = new AWS.Endpoint(esDomain.endpoint)
var creds = new AWS.EnvironmentCredentials('AWS');

function postDocumentToES(doc, context) {
    var req = new AWS.HttpRequest(endpoint);

    req.method = 'POST';
    req.path = '/_bulk';
    req.region = esDomain.region;
    req.body = doc;
    req.headers['presigned-expires'] = false;
    req.headers['Host'] = endpoint.host;

    // Sign the request (Sigv4)
    var signer = new AWS.Signers.V4(req, 'es');
    signer.addAuthorization(creds, new Date());

    // Post document to ES
    var send = new AWS.NodeHttpClient();
    send.handleRequest(req, null, function (httpResp) {
        var body = '';
        httpResp.on('data', function (chunk) {
            body += chunk;
        });
        httpResp.on('end', function (chunk) {
            console.log('Successful', body);
            context.succeed();
        });
    }, function (err) {
        console.log('Error: ' + err);
        context.fail();
    });
}

exports.handler = (event, context, callback) => {
    console.log("event => " + JSON.stringify(event));
    var posts = '';

    for (var i = 0; i < event.Records.length; i++) {
        var eventName = event.Records[i].eventName;
        var actionType = '';
        var image;
        var noDoc = false;
        switch (eventName) {
            case 'INSERT':
                actionType = 'create';
                image = event.Records[i].dynamodb.NewImage;
                break;
            case 'MODIFY':
                actionType = 'update';
                image = event.Records[i].dynamodb.NewImage;
                break;
            case 'REMOVE':
            actionType = 'delete';
                image = event.Records[i].dynamodb.OldImage;
                noDoc = true;
                break;
        }

        if (typeof image !== "undefined") {
            var postData = {};
            for (var key in image) {
                if (image.hasOwnProperty(key)) {
                    if (key === 'postId') {
                        postData['id'] = image[key].S;
                    } else {
                        var val = image[key];
                        if (val.hasOwnProperty('S')) {
                            postData[key] = val.S;
                        } else if (val.hasOwnProperty('N')) {
                            postData[key] = val.N;
                        }
                    }
                }
            }

            var action = {};
            action[actionType] = {};
            action[actionType]._index = 'id';
            action[actionType]._type = 'post';
            action[actionType]._id = postData['id'];
            posts += [
                JSON.stringify(action),
            ].concat(noDoc?[]:[JSON.stringify(postData)]).join('\n') + '\n';
        }
    }
    console.log('posts:',posts);
    postDocumentToES(posts, context);
};
```

You can then use DynamoDB streams to attach this to a DynamoDB table with a primary key of
`id`, and any changes to the source of DynamoDB would stream into your OpenSearch Service
domain. For more information about configuring this, see the [DynamoDB Streams documentation](../../../amazondynamodb/latest/developerguide/Streams.md "../../../amazondynamodb/latest/developerguide/Streams.md").
