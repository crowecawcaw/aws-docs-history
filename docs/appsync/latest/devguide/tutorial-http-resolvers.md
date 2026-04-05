# Using HTTP resolvers in AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](tutorials-js.md "tutorials-js.md").

AWS AppSync enables you to use supported data sources (that is, AWS Lambda, Amazon DynamoDB,
Amazon OpenSearch Service, or Amazon Aurora) to perform various operations, in addition to any arbitrary HTTP
endpoints to resolve GraphQL fields. After your HTTP endpoints are available, you can connect
to them using a data source. Then, you can configure a resolver in the schema to perform
GraphQL operations such as queries, mutations, and subscriptions. This tutorial walks you
through some common examples.

In this tutorial you use a REST API (created using Amazon API Gateway and Lambda) with an
AWS AppSync GraphQL endpoint.

## One-Click Setup

If you want to automatically set up a GraphQL endpoint in AWS AppSync with an HTTP
endpoint configured (using Amazon API Gateway and Lambda), you can use the following AWS CloudFormation
template :

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/http/http-full.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/http/http-full.yaml")

## Creating a REST API

You can use the following AWS CloudFormation template to set up a REST endpoint that works for
this tutorial:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/http/http-api-gw.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/http/http-api-gw.yaml")

The AWS CloudFormation stack performs the following steps:

1. Sets up a Lambda function that contains your business logic for your
   microservice.
2. Sets up an API Gateway REST API with the following endpoint/method/content type
   combination:

| API Resource Path | HTTP Method | Supported Content Type |
| ----------------- | ----------- | ---------------------- |
| /v1/users         | POST        | application/json       |
| /v1/users         | GET         | application/json       |
| /v1/users/1       | GET         | application/json       |
| /v1/users/1       | PUT         | application/json       |
| /v1/users/1       | DELETE      | application/json       |

## Creating Your GraphQL API

To create the GraphQL API in AWS AppSync:

- Open the AWS AppSync console and choose **Create
  API**.
- For the API name, type `UserData`.
- Choose **Custom schema**.
- Choose **Create**.

The AWS AppSync console creates a new GraphQL API for you using the API key
authentication mode. You can use the console to set up the rest of the GraphQL API and run
queries on it for the remainder of this tutorial.

## Creating a GraphQL Schema

Now that you have a GraphQL API, let’s create a GraphQL schema. From the schema editor
in the AWS AppSync console, make sure you schema matches the following schema:

```
schema {
    query: Query
    mutation: Mutation
}

type Mutation {
    addUser(userInput: UserInput!): User
    deleteUser(id: ID!): User
}

type Query {
    getUser(id: ID): User
    listUser: [User!]!
}

type User {
    id: ID!
    username: String!
    firstname: String
    lastname: String
    phone: String
    email: String
}

input UserInput {
    id: ID!
    username: String!
    firstname: String
    lastname: String
    phone: String
    email: String
}
```

## Configure Your HTTP Data Source

To configure your HTTP data source, do the following:

- On the **DataSources** tab, choose **New**, and then type a friendly name for the data source (for
  example, `HTTP`).
- In **Data source type**, choose **HTTP**.
- Set the endpoint to the API Gateway endpoint that is created. Make sure that you don’t
  include the stage name as part of the endpoint.

**Note:** At this time only public endpoints are supported by
AWS AppSync.

**Note:** For more information about the certifying
authorities that are recognized by the AWS AppSync service, see [Certificate Authorities (CA)
Recognized by AWS AppSync for HTTPS Endpoints](http-cert-authorities.md#aws-appsync-http-certificate-authorities "http-cert-authorities.md#aws-appsync-http-certificate-authorities").

## Configuring Resolvers

In this step, you connect the http data source to the **getUser** query.

To set up the resolver:

- Choose the **Schema** tab.
- In the **Data types** pane on the right under the
  **Query** type, find the **getUser** field and choose **Attach**.
- In **Data source name**, choose **HTTP**.
- In **Configure the request mapping template**, paste
  the following code:

```
{
    "version": "2018-05-29",
    "method": "GET",
    "params": {
        "headers": {
            "Content-Type": "application/json"
        }
    },
    "resourcePath": $util.toJson("/v1/users/${ctx.args.id}")
}
```

- In **Configure the response mapping template**, paste
  the following code:

```
## return the body
#if($ctx.result.statusCode == 200)
    ##if response is 200
    $ctx.result.body
#else
    ##if response is not 200, append the response to error block.
    $utils.appendError($ctx.result.body, "$ctx.result.statusCode")
#end
```

- Choose the **Query** tab, and then run the following
  query:

```
query GetUser{
    getUser(id:1){
        id
        username
    }
}
```

This should return the following response:

```
{
    "data": {
        "getUser": {
            "id": "1",
            "username": "nadia"
        }
    }
}
```

- Choose the **Schema** tab.
- In the **Data types** pane on the right under
  **Mutation**, find the **addUser** field and choose **Attach**.
- In **Data source name**, choose **HTTP**.
- In **Configure the request mapping template**, paste
  the following code:

```
{
    "version": "2018-05-29",
    "method": "POST",
    "resourcePath": "/v1/users",
    "params":{
      "headers":{
        "Content-Type": "application/json",
      },
      "body": $util.toJson($ctx.args.userInput)
    }
}
```

- In **Configure the response mapping template**, paste
  the following code:

```
## Raise a GraphQL field error in case of a datasource invocation error
#if($ctx.error)
    $util.error($ctx.error.message, $ctx.error.type)
#end
## if the response status code is not 200, then return an error. Else return the body **
#if($ctx.result.statusCode == 200)
    ## If response is 200, return the body.
    $ctx.result.body
#else
    ## If response is not 200, append the response to error block.
    $utils.appendError($ctx.result.body, "$ctx.result.statusCode")
#end
```

- Choose the **Query** tab, and then run the following
  query:

```
mutation addUser{
    addUser(userInput:{
        id:"2",
        username:"shaggy"
    }){
        id
        username
    }
}
```

This should return the following response:

```
{
    "data": {
        "getUser": {
        "id": "2",
        "username": "shaggy"
        }
    }
}
```

## Invoking AWS Services

You can use HTTP resolvers to set up a GraphQL API interface for AWS services. HTTP
requests to AWS must be signed with the [Signature Version 4
process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") so that AWS can identify who sent them. AWS AppSync calculates the
signature on your behalf when you associate an IAM role with the HTTP data source.

You provide two additional components to invoke AWS services with HTTP resolvers:

- An IAM role with permissions to call the AWS service APIs
- Signing configuration in the data source

For example, if you want to call the [ListGraphqlApis operation](../APIReference/API_ListGraphqlApis.md "../APIReference/API_ListGraphqlApis.md") with HTTP resolvers, you first [create an IAM
role](attaching-a-data-source.md#aws-appsync-getting-started-build-a-schema-from-scratch "attaching-a-data-source.md#aws-appsync-getting-started-build-a-schema-from-scratch") that AWS AppSync assumes with the following policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "appsync:ListGraphqlApis"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Next, create the HTTP data source for AWS AppSync. In this example, you call
AWS AppSync in the US West (Oregon) Region. Set up the following HTTP configuration in a
file named `http.json`, which includes the signing region and service
name:

```
{
    "endpoint": "https://appsync.us-west-2.amazonaws.com/",
    "authorizationConfig": {
        "authorizationType": "AWS_IAM",
        "awsIamConfig": {
            "signingRegion": "us-west-2",
            "signingServiceName": "appsync"
        }
    }
}
```

Then, use the AWS CLI to create the data source with an associated role as
follows:

```
aws appsync create-data-source --api-id <API-ID> \
                               --name AWSAppSync \
                               --type HTTP \
                               --http-config file:///http.json \
                               --service-role-arn <ROLE-ARN>
```

When you attach a resolver to the field in the schema, use the following request mapping
template to call AWS AppSync:

```
{
    "version": "2018-05-29",
    "method": "GET",
    "resourcePath": "/v1/apis"
}
```

When you run a GraphQL query for this data source, AWS AppSync signs the request using
the role you provided and includes the signature in the request. The query returns a list
of AWS AppSync GraphQL APIs in your account in that AWS Region.
