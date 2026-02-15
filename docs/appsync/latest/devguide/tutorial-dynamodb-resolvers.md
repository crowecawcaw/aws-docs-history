# Creating a simple post application using DynamoDB resolvers

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](tutorials-js.md "tutorials-js.md").

This tutorial shows how you can bring your own Amazon DynamoDB tables to AWS AppSync and connect
them to a GraphQL API.

You can let AWS AppSync provision DynamoDB resources on your behalf. Or, if you prefer, you can connect your existing
tables to a GraphQL schema by creating a data source and a resolver. In either case, you’ll be able to read and
write to your DynamoDB database through GraphQL statements and subscribe to real-time data.

There are specific configuration steps that need to be completed in order for GraphQL statements to be
translated to DynamoDB operations, and for responses to be translated back into GraphQL. This tutorial outlines the
configuration process through several real-world scenarios and data access patterns.

## Setting up your DynamoDB tables

To begin this tutorial, first you need to follow the steps below to provision AWS resources.

1. Provision AWS resources using the following AWS CloudFormation template in the CLI:

```
aws cloudformation create-stack \
    --stack-name AWSAppSyncTutorialForAmazonDynamoDB \
    --template-url https://s3.us-west-2.amazonaws.com/awsappsync/resources/dynamodb/AmazonDynamoDBCFTemplate.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```

Alternatively, you can launch the following CloudFormation stack in the US-West 2 (Oregon) region in your AWS
account.

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](/images/appsync/latest/devguide/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/dynamodb/AmazonDynamoDBCFTemplate.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/dynamodb/AmazonDynamoDBCFTemplate.yaml")

This creates the following:

    * A DynamoDB table called `AppSyncTutorial-Post` that will hold `Post` data.
    * An IAM role and associated IAM managed policy to allow AWS AppSync to interact with the
     `Post` table.

2. To see more details about the stack and the created resources, run the following CLI command:

```
aws cloudformation describe-stacks --stack-name AWSAppSyncTutorialForAmazonDynamoDB
```

3. To delete the resources later, you can run the following:

```
aws cloudformation delete-stack --stack-name AWSAppSyncTutorialForAmazonDynamoDB
```

## Creating your GraphQL API

To create the GraphQL API in AWS AppSync:

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose **Create
      API**.

2. Under the **Customize your API or import from Amazon DynamoDB** window,
   choose **Build from scratch**.
   1. Choose **Start** to the right of the same window.

3. In the **API name** field, set the name of the API to
   `AWSAppSyncTutorial`.
4. Choose **Create**.

The AWS AppSync console creates a new GraphQL API for you using the API key authentication mode. You can use the
console to set up the rest of the GraphQL API and run queries against it for the rest of this tutorial.

## Defining a basic post API

Now that you have created an AWS AppSync GraphQL API, you can set up a basic schema that allows the basic
creation, retrieval, and deletion of post data.

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose the API you just created.

2. In the **Sidebar**, choose **Schema**.
   1. In the **Schema** pane, replace the contents with the following
      code:

   ```
   schema {
       query: Query
       mutation: Mutation
   }

   type Query {
       getPost(id: ID): Post
   }

   type Mutation {
       addPost(
           id: ID!
           author: String!
           title: String!
           content: String!
           url: String!
       ): Post!
   }

   type Post {
       id: ID!
       author: String
       title: String
       content: String
       url: String
       ups: Int!
       downs: Int!
       version: Int!
   }
   ```

3. Choose **Save**.

This schema defines a `Post` type and operations to add and get `Post` objects.

## Configuring the Data Source for the DynamoDB

Tables

Next, link the queries and mutations defined in the schema to the `AppSyncTutorial-Post`DynamoDB
table.

First, AWS AppSync needs to be aware of your tables. You do this by setting up a data source in
AWS AppSync:

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose your GraphQL API.
   2. In the **Sidebar**, choose **Data
      Sources**.

2. Choose **Create data source**.
   1. For **Data source name**, enter in `PostDynamoDBTable`.
   2. For **Data source type**, choose **Amazon DynamoDB
      table**.
   3. For **Region**, choose **US-WEST-2**.
   4. For **Table name**, choose the **AppSyncTutorial-Post** DynamoDB table.
   5. Create
      a new IAM role (recommended) or choose an existing role that has the `lambda:invokeFunction`
      IAM permission. Existing roles need a trust policy, as explained in the [Attaching a data source](attaching-a-data-source.md "attaching-a-data-source.md") section.

   The following is an example IAM policy that has the required permissions to perform operations on the
   resource:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [ "lambda:invokeFunction" ],
    "Resource": [
    "arn:aws:lambda:us-east-1:111122223333:function:myFunction",
    "arn:aws:lambda:us-east-1:111122223333:function:myFunction:*"
    ]
    }
    ]
    }`

   ```

3. Choose **Create**.

## Setting up the addPost resolver (DynamoDB

PutItem)

After AWS AppSync is aware of the DynamoDB table, you can link it to individual queries and mutations by defining
**Resolvers**. The first resolver you create is the `addPost` resolver,
which enables you to create a post in the `AppSyncTutorial-Post` DynamoDB table.

A resolver has the following components:

- The location in the GraphQL schema to attach the resolver. In this case, you are setting up a resolver on
  the `addPost` field on the `Mutation` type. This resolver will be invoked when the
  caller calls `mutation { addPost(...){...} }`.
- The data source to use for this resolver. In this case, you want to use the `PostDynamoDBTable`
  data source you defined earlier, so you can add entries into the `AppSyncTutorial-Post` DynamoDB
  table.
- The request mapping template. The purpose of the request mapping template is to take the incoming request
  from the caller and translate it into instructions for AWS AppSync to perform against DynamoDB.
- The response mapping template. The job of the response mapping template is to take the response from DynamoDB
  and translate it back into something that GraphQL expects. This is useful if the shape of the data in DynamoDB is
  different to the `Post` type in GraphQL, but in this case they have the same shape, so you just
  pass the data through.

To set up the resolver:

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose your GraphQL API.
   2. In the **Sidebar**, choose **Data
      Sources**.

2. Choose **Create data source**.
   1. For **Data source name**, enter in `PostDynamoDBTable`.
   2. For **Data source type**, choose **Amazon DynamoDB
      table**.
   3. For **Region**, choose **US-WEST-2**.
   4. For **Table name**, choose the **AppSyncTutorial-Post** DynamoDB table.
   5. Create
      a new IAM role (recommended) or choose an existing role that has the `lambda:invokeFunction`
      IAM permission. Existing roles need a trust policy, as explained in the [Attaching a data source](attaching-a-data-source.md "attaching-a-data-source.md") section.

   The following is an example IAM policy that has the required permissions to perform operations on the
   resource:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [ "lambda:invokeFunction" ],
    "Resource": [
    "arn:aws:lambda:us-west-2:123456789012:function:myFunction",
    "arn:aws:lambda:us-west-2:123456789012:function:myFunction:*"
    ]
    }
    ]
    }`

   ```

3. Choose **Create**.
4. Choose the **Schema** tab.
5. In the **Data types** pane on the right, find the **addPost** field on the **Mutation** type, and then choose **Attach**.
6. In the **Action menu**, choose **Update
   runtime**, then choose **Unit Resolver (VTL only)**.
7. In **Data source name**, choose **PostDynamoDBTable**.
8. In **Configure the request mapping template**, paste the following:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },
    "attributeValues" : {
        "author" : $util.dynamodb.toDynamoDBJson($context.arguments.author),
        "title" : $util.dynamodb.toDynamoDBJson($context.arguments.title),
        "content" : $util.dynamodb.toDynamoDBJson($context.arguments.content),
        "url" : $util.dynamodb.toDynamoDBJson($context.arguments.url),
        "ups" : { "N" : 1 },
        "downs" : { "N" : 0 },
        "version" : { "N" : 1 }
    }
}
```

**Note:** A _type_ is specified on all the keys and
attribute values. For example, you set the `author` field to `{ "S" :
 "${context.arguments.author}" }`. The `S` part indicates to AWS AppSync and DynamoDB that the
value will be a string value. The actual value gets populated from the `author` argument.
Similarly, the `version` field is a number field because it uses `N` for the type.
Finally, you’re also initializing the `ups`, `downs` and `version`
field.

For this tutorial you’ve specified that the GraphQL `ID!` type, which indexes the new item that
is inserted to DynamoDB, comes as part of the client arguments. AWS AppSync comes with a utility for automatic ID
generation called `$utils.autoId()` which you could have also used in the form of `"id" : {
 "S" : "${$utils.autoId()}" }`. Then you could simply leave the `id: ID!` out of the schema
definition of `addPost()` and it would be inserted automatically. You won’t use this technique for
this tutorial, but you should consider it as a good practice when writing to DynamoDB tables.

For more information about mapping templates, see the [Resolver Mapping Template Overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview")
reference documentation. For more information about GetItem request mapping, see the [GetItem](aws-appsync-resolver-mapping-template-reference-dynamodb-getitem.md "aws-appsync-resolver-mapping-template-reference-dynamodb-getitem.md") reference
documentation. For more information about types, see the [Type System (Request
Mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md") reference documentation. 9. In **Configure the response mapping template**, paste the following:

```
$utils.toJson($context.result)
```

**Note:** Because the shape of the data in the `AppSyncTutorial-Post`
table exactly matches the shape of the `Post` type in GraphQL, the response mapping template just
passes the results straight through. Also note that all of the examples in this tutorial use the same response
mapping template, so you only create one file. 10. Choose **Save**.

### Call the API to Add a Post

Now that the resolver is set up, AWS AppSync can translate an incoming `addPost` mutation to a
DynamoDB PutItem operation. You can now run a mutation to put something in the table.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following mutation:

```
mutation addPost {
  addPost(
    id: 123
    author: "AUTHORNAME"
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

- Choose **Execute query** (the orange play button).
- The results of the newly created post should appear in the results pane to the right of the query pane.
  It should look similar to the following:

```
{
  "data": {
    "addPost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our first post!",
      "content": "This is our first post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

Here’s what happened:

- AWS AppSync received an `addPost` mutation request.
- AWS AppSync took the request, and the request mapping template, and generated a request mapping document.
  This would have looked like:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key" : {
        "id" : { "S" : "123" }
    },
    "attributeValues" : {
        "author": { "S" : "AUTHORNAME" },
        "title": { "S" : "Our first post!" },
        "content": { "S" : "This is our first post." },
        "url": { "S" : "https://aws.amazon.com/appsync/" },
        "ups" : { "N" : 1 },
        "downs" : { "N" : 0 },
        "version" : { "N" : 1 }
    }
}
```

- AWS AppSync used the request mapping document to generate and execute a DynamoDB`PutItem`
  request.
- AWS AppSync took the results of the `PutItem` request and converted them back to GraphQL
  types.

```
{
    "id" : "123",
    "author": "AUTHORNAME",
    "title": "Our first post!",
    "content": "This is our first post.",
    "url": "https://aws.amazon.com/appsync/",
    "ups" : 1,
    "downs" : 0,
    "version" : 1
}
```

- Passed it through the response mapping document, which just passed it through unchanged.
- Returned the newly created object in the GraphQL response.

## Setting Up the getPost Resolver

(DynamoDB GetItem)

Now that you’re able to add data to the `AppSyncTutorial-Post`DynamoDB table, you
need to set up the `getPost` query so it can retrieve that data from the
`AppSyncTutorial-Post` table. To do this, you set up another resolver.

- Choose the **Schema** tab.
- In the **Data types** pane on the right, find the
  **getPost** field on the **Query** type, and then choose **Attach**.
- In the **Action menu**, choose **Update
  runtime**, then choose **Unit Resolver (VTL only)**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    }
}
```

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

- Choose **Save**.

### Call the API to Get a Post

Now the resolver has been set up, AWS AppSync knows how to translate an incoming `getPost` query to
a DynamoDB`GetItem` operation. You can now run a query to retrieve the post you created earlier.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following:

```
query getPost {
  getPost(id:123) {
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

- Choose **Execute query** (the orange play button).
- The post retrieved from DynamoDB should appear in the results pane to the right of the query pane. It
  should look similar to the following:

```
{
  "data": {
    "getPost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our first post!",
      "content": "This is our first post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

Here’s what happened:

- AWS AppSync received a `getPost` query request.
- AWS AppSync took the request, and the request mapping template, and generated a request mapping document.
  This would have looked like:

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "id" : { "S" : "123" }
    }
}
```

- AWS AppSync used the request mapping document to generate and execute a DynamoDB GetItem request.
- AWS AppSync took the results of the `GetItem` request and converted it back to GraphQL
  types.

```
{
    "id" : "123",
    "author": "AUTHORNAME",
    "title": "Our first post!",
    "content": "This is our first post.",
    "url": "https://aws.amazon.com/appsync/",
    "ups" : 1,
    "downs" : 0,
    "version" : 1
}
```

- Passed it through the response mapping document, which just passed it through unchanged.
- Returned the retrieved object in the response.

Alternatively, take the following example:

```
query getPost {
  getPost(id:123) {
    id
    author
    title
  }
}
```

If your `getPost` query only needs the `id`, `author`, and
`title`, you can change your request mapping template to use projection expressions to specify only
the attributes that you want from your DynamoDB table to avoid unnecessary data transfer from DynamoDB to AWS AppSync. For
example, the request mapping template may look like the snippet below:

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    },
    "projection" : {
     "expression" : "#author, id, title",
     "expressionNames" : { "#author" : "author"}
    }
}
```

## Create an updatePost Mutation

(DynamoDB UpdateItem)

So far you can create and retrieve `Post` objects in DynamoDB. Next, you’ll set up
a new mutation to allow us to update object. You’ll do this using the UpdateItem DynamoDB
operation.

- Choose the **Schema** tab.
- In the **Schema** pane, modify the `Mutation`
  type to add a new `updatePost` mutation as follows:

```
type Mutation {
    updatePost(
        id: ID!,
        author: String!,
        title: String!,
        content: String!,
        url: String!
    ): Post
    addPost(
        author: String!
        title: String!
        content: String!
        url: String!
    ): Post!
}
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **updatePost** field on the **Mutation** type and then choose **Attach**.
- In the **Action menu**, choose **Update
  runtime**, then choose **Unit Resolver (VTL only)**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },
    "update" : {
        "expression" : "SET author = :author, title = :title, content = :content, #url = :url ADD version :one",
        "expressionNames": {
            "#url" : "url"
        },
        "expressionValues": {
            ":author" : $util.dynamodb.toDynamoDBJson($context.arguments.author),
            ":title" : $util.dynamodb.toDynamoDBJson($context.arguments.title),
            ":content" : $util.dynamodb.toDynamoDBJson($context.arguments.content),
            ":url" : $util.dynamodb.toDynamoDBJson($context.arguments.url),
            ":one" : { "N": 1 }
        }
    }
}
```

**Note:** This resolver is using the DynamoDB UpdateItem, which
is significantly different from the PutItem operation. Instead of writing the entire item,
you’re just asking DynamoDB to update certain attributes. This is done using DynamoDB Update
Expressions. The expression itself is specified in the `expression` field in
the `update` section. It says to set the `author`,
`title`, `content` and url attributes, and then increment the
`version` field. The values to use do not appear in the expression itself;
the expression has placeholders that have names starting with a colon, which are then
defined in the `expressionValues` field. Finally, DynamoDB has reserved words that
cannot appear in the `expression`. For example, `url` is a reserved
word, so to update the `url` field you can use name placeholders and define
them in the `expressionNames` field.

For more info about `UpdateItem` request mapping, see the [UpdateItem](aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem.md "aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem.md") reference documentation. For more information about how to write
update expressions, see the [DynamoDB UpdateExpressions documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md").

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

### Call the API to Update a Post

Now the resolver has been set up, AWS AppSync knows how to translate an incoming
`update` mutation to a DynamoDB`Update` operation. You can now run a
mutation to update the item you wrote earlier.

- Choose the **Queries** tab.
- In **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation updatePost {
  updatePost(
    id:"123"
    author: "A new author"
    title: "An updated author!"
    content: "Now with updated content!"
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

- Choose **Execute query** (the orange play
  button).
- The updated post in DynamoDB should appear in the results pane to the right of the
  query pane. It should look similar to the following:

```
{
  "data": {
    "updatePost": {
      "id": "123",
      "author": "A new author",
      "title": "An updated author!",
      "content": "Now with updated content!",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 2
    }
  }
}
```

In this example, the `ups` and `downs` fields were not modified
because the request mapping template did not ask AWS AppSync and DynamoDB to do anything with
those fields. Also, the `version` field was incremented by 1 because you asked
AWS AppSync and DynamoDB to add 1 to the `version` field.

## Modifying the

updatePost Resolver (DynamoDB UpdateItem)

This is a good start to the `updatePost` mutation, but it has two main
problems:

- If you want to update just a single field, you have to update all of the
  fields.
- If two people are modifying the object, you could potentially lose information.

To address these issues, you’re going to modify the `updatePost` mutation to
only modify arguments that were specified in the request, and then add a condition to the
`UpdateItem` operation.

1. Choose the **Schema** tab.
2. In the **Schema** pane, modify the
   `updatePost` field in the `Mutation` type to remove the
   exclamation marks from the `author`, `title`, `content`,
   and `url` arguments, making sure to leave the `id` field as is. This
   will make them optional argument. Also, add a new, required `expectedVersion`
   argument.

```
type Mutation {
    updatePost(
        id: ID!,
        author: String,
        title: String,
        content: String,
        url: String,
        expectedVersion: Int!
    ): Post
    addPost(
        author: String!
        title: String!
        content: String!
        url: String!
    ): Post!
}
```

3. Choose **Save**.
4. In the **Data types** pane on the right, find the
   **updatePost** field on the **Mutation** type.
5. Choose **PostDynamoDBTable** to open the existing
   resolver.
6. In **Configure the request mapping template**, modify the
   request mapping template as follows:

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },

    ## Set up some space to keep track of things you're updating **
    #set( $expNames  = {} )
    #set( $expValues = {} )
    #set( $expSet = {} )
    #set( $expAdd = {} )
    #set( $expRemove = [] )

    ## Increment "version" by 1 **
    $!{expAdd.put("version", ":one")}
    $!{expValues.put(":one", { "N" : 1 })}

    ## Iterate through each argument, skipping "id" and "expectedVersion" **
    #foreach( $entry in $context.arguments.entrySet() )
        #if( $entry.key != "id" && $entry.key != "expectedVersion" )
            #if( (!$entry.value) && ("$!{entry.value}" == "") )
                ## If the argument is set to "null", then remove that attribute from the item in DynamoDB **

                #set( $discard = ${expRemove.add("#${entry.key}")} )
                $!{expNames.put("#${entry.key}", "$entry.key")}
            #else
                ## Otherwise set (or update) the attribute on the item in DynamoDB **

                $!{expSet.put("#${entry.key}", ":${entry.key}")}
                $!{expNames.put("#${entry.key}", "$entry.key")}
                $!{expValues.put(":${entry.key}", { "S" : "${entry.value}" })}
            #end
        #end
    #end

    ## Start building the update expression, starting with attributes you're going to SET **
    #set( $expression = "" )
    #if( !${expSet.isEmpty()} )
        #set( $expression = "SET" )
        #foreach( $entry in $expSet.entrySet() )
            #set( $expression = "${expression} ${entry.key} = ${entry.value}" )
            #if ( $foreach.hasNext )
                #set( $expression = "${expression}," )
            #end
        #end
    #end

    ## Continue building the update expression, adding attributes you're going to ADD **
    #if( !${expAdd.isEmpty()} )
        #set( $expression = "${expression} ADD" )
        #foreach( $entry in $expAdd.entrySet() )
            #set( $expression = "${expression} ${entry.key} ${entry.value}" )
            #if ( $foreach.hasNext )
                #set( $expression = "${expression}," )
            #end
        #end
    #end

    ## Continue building the update expression, adding attributes you're going to REMOVE **
    #if( !${expRemove.isEmpty()} )
        #set( $expression = "${expression} REMOVE" )

        #foreach( $entry in $expRemove )
            #set( $expression = "${expression} ${entry}" )
            #if ( $foreach.hasNext )
                #set( $expression = "${expression}," )
            #end
        #end
    #end

    ## Finally, write the update expression into the document, along with any expressionNames and expressionValues **
    "update" : {
        "expression" : "${expression}"
        #if( !${expNames.isEmpty()} )
            ,"expressionNames" : $utils.toJson($expNames)
        #end
        #if( !${expValues.isEmpty()} )
            ,"expressionValues" : $utils.toJson($expValues)
        #end
    },

    "condition" : {
        "expression"       : "version = :expectedVersion",
        "expressionValues" : {
            ":expectedVersion" : $util.dynamodb.toDynamoDBJson($context.arguments.expectedVersion)
        }
    }
}
```

7. Choose **Save**.

This template is one of the more complex examples. It demonstrates the power and
flexibility of mapping templates. It loops through all of the arguments, skipping over
`id` and `expectedVersion`. If the argument is set to something, it
asks AWS AppSync and DynamoDB to update that attribute on the object in DynamoDB. If the attribute is
set to null, it asks AWS AppSync and DynamoDB to remove that attribute from the post object. If an
argument wasn’t specified, it leaves the attribute alone. It also increments the
`version` field.

Also, there is a new `condition` section. A condition expression enables you
tell AWS AppSync and DynamoDB whether or not the request should succeed based on the state of the
object already in DynamoDB before the operation is performed. In this case, you only want the
`UpdateItem` request to succeed if the `version` field of the item
currently in DynamoDB exactly matches the `expectedVersion` argument.

For more information about condition expressions, see the [Condition Expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md") reference documentation.

### Call the API to Update a Post

Let’s try updating the `Post` object with the new resolver:

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation updatePost {
  updatePost(
    id:123
    title: "An empty story"
    content: null
    expectedVersion: 2
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

- Choose **Execute query** (the orange play
  button).
- The updated post in DynamoDB should appear in the results pane to the right of the
  query pane. It should look similar to the following:

```
{
  "data": {
    "updatePost": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 3
    }
  }
}
```

In this request, you asked AWS AppSync and DynamoDB to update the `title` and
`content` field only. It left all the other fields alone (other than
incrementing the `version` field). You set the `title` attribute to a
new value, and removed the `content` attribute from the post. The
`author`, `url`, `ups`, and `downs` fields
were left untouched.

Try executing the mutation request again, leaving the request exactly as is. You should
see a response similar to the following:

```
{
  "data": {
    "updatePost": null
  },
  "errors": [
    {
      "path": [
        "updatePost"
      ],
      "data": {
        "id": "123",
        "author": "A new author",
        "title": "An empty story",
        "content": null,
        "url": "https://aws.amazon.com/appsync/",
        "ups": 1,
        "downs": 0,
        "version": 3
      },
      "errorType": "DynamoDB:ConditionalCheckFailedException",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "message": "The conditional request failed (Service: AmazonDynamoDBv2; Status Code: 400; Error Code: ConditionalCheckFailedException; Request ID: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ)"
    }
  ]
}
```

The request fails because the condition expression evaluates to false:

- The first time you ran the request, the value of the `version` field of
  the post in DynamoDB was `2`, which matched the `expectedVersion`
  argument. The request succeeded, which meant the `version` field was
  incremented in DynamoDB to `3`.
- The second time you ran the request, the value of the `version` field of
  the post in DynamoDB was `3`, which did not match the
  `expectedVersion` argument.

This pattern is typically called _optimistic locking_.

A feature of an AWS AppSync DynamoDB resolver is that it returns the current value of the post
object in DynamoDB. You can find this in the `data` field in the `errors`
section of the GraphQL response. Your application can use this information to decide how it
should proceed. In this case, you can see the `version` field of the object in
DynamoDB is set to `3`, so you could just update the `expectedVersion`
argument to `3` and the request would succeed again.

For more information about handling condition check failures, see the [Condition Expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md") mapping template reference documentation.

## Create

upvotePost and downvotePost Mutations (DynamoDB UpdateItem)

The `Post` type has `ups` and `downs` fields to enable
record upvotes and downvotes, but so far the API doesn’t let us do anything with them. Let’s
add some mutations to let us upvote and downvote the posts.

- Choose the **Schema** tab.
- In the **Schema** pane, modify the `Mutation`
  type to add new `upvotePost` and `downvotePost` mutations as
  follows:

```
type Mutation {
    upvotePost(id: ID!): Post
    downvotePost(id: ID!): Post
    updatePost(
        id: ID!,
        author: String,
        title: String,
        content: String,
        url: String,
        expectedVersion: Int!
    ): Post
    addPost(
        author: String!,
        title: String!,
        content: String!,
        url: String!
    ): Post!
}
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **upvotePost** field on the **Mutation** type, and then choose **Attach**.
- In the **Action menu**, choose **Update
  runtime**, then choose **Unit Resolver (VTL only)**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },
    "update" : {
        "expression" : "ADD ups :plusOne, version :plusOne",
        "expressionValues" : {
            ":plusOne" : { "N" : 1 }
        }
    }
}
```

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created `downvotePost` field on the **Mutation**
  type, and then choose **Attach**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },
    "update" : {
        "expression" : "ADD downs :plusOne, version :plusOne",
        "expressionValues" : {
            ":plusOne" : { "N" : 1 }
        }
    }
}
```

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

- Choose **Save**.

### Call the API to upvote and

downvote a Post

Now the new resolvers have been set up, AWS AppSync knows how to translate an incoming
`upvotePost` or `downvote` mutation to DynamoDB UpdateItem operation.
You can now run mutations to upvote or downvote the post you created earlier.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation votePost {
  upvotePost(id:123) {
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

- Choose **Execute query** (the orange play
  button).
- The post is updated in DynamoDB and should appear in the results pane to the right of
  the query pane. It should look similar to the following:

```
{
  "data": {
    "upvotePost": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 6,
      "downs": 0,
      "version": 4
    }
  }
}
```

- Choose **Execute query** a few more times. You should
  see the `ups` and `version` field incrementing by 1 each time you
  execute the query.
- Change the query to call the `downvotePost` mutation as follows:

```
mutation votePost {
  downvotePost(id:123) {
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

- Choose **Execute query** (the orange play button). This
  time, you should see the `downs` and `version` field incrementing
  by 1 each time you execute the query.

```
{
  "data": {
    "downvotePost": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 6,
      "downs": 4,
      "version": 12
    }
  }
}
```

## Setting Up the deletePost

Resolver (DynamoDB DeleteItem)

The next mutation you want to set up is to delete a post. You’ll do this using the
`DeleteItem` DynamoDB operation.

- Choose the **Schema** tab.
- In the **Schema** pane, modify the `Mutation`
  type to add a new `deletePost` mutation as follows:

```
type Mutation {
    deletePost(id: ID!, expectedVersion: Int): Post
    upvotePost(id: ID!): Post
    downvotePost(id: ID!): Post
    updatePost(
        id: ID!,
        author: String,
        title: String,
        content: String,
        url: String,
        expectedVersion: Int!
    ): Post
    addPost(
        author: String!,
        title: String!,
        content: String!,
        url: String!
    ): Post!
}
```

This time you made the `expectedVersion` field optional, which is explained
later when you add the request mapping template.

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **delete** field on the **Mutation** type, and then choose **Attach**.
- In the **Action menu**, choose **Update
  runtime**, then choose **Unit Resolver (VTL only)**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "DeleteItem",
    "key": {
        "id": $util.dynamodb.toDynamoDBJson($context.arguments.id)
    }
    #if( $context.arguments.containsKey("expectedVersion") )
        ,"condition" : {
            "expression"       : "attribute_not_exists(id) OR version = :expectedVersion",
            "expressionValues" : {
                ":expectedVersion" : $util.dynamodb.toDynamoDBJson($context.arguments.expectedVersion)
            }
        }
    #end
}
```

**Note:** The `expectedVersion` argument is an
optional argument. If the caller set an `expectedVersion` argument in the
request, the template adds a condition that only allows the `DeleteItem`
request to succeed if the item is already deleted or if the `version` attribute
of the post in DynamoDB exactly matches the `expectedVersion`. If left out, no
condition expression is specified on the `DeleteItem` request. It succeeds
regardless of the value of `version`, or whether or not the item exists in
DynamoDB.

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

**Note:** Even though you’re deleting an item, you can return
the item that was deleted, if it was not already deleted.

- Choose **Save**.

For more info about `DeleteItem` request mapping, see the [DeleteItem](aws-appsync-resolver-mapping-template-reference-dynamodb-deleteitem.md "aws-appsync-resolver-mapping-template-reference-dynamodb-deleteitem.md") reference documentation.

### Call the API to Delete a Post

Now the resolver has been set up, AWS AppSync knows how to translate an incoming
`delete` mutation to a DynamoDB`DeleteItem` operation. You can now run
a mutation to delete something in the table.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation deletePost {
  deletePost(id:123) {
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

- Choose **Execute query** (the orange play
  button).
- The post is deleted from DynamoDB. Note that AWS AppSync returns the value of the item
  that was deleted from DynamoDB, which should appear in the results pane to the right of the
  query pane. It should look similar to the following:

```
{
  "data": {
    "deletePost": {
      "id": "123",
      "author": "A new author",
      "title": "An empty story",
      "content": null,
      "url": "https://aws.amazon.com/appsync/",
      "ups": 6,
      "downs": 4,
      "version": 12
    }
  }
}
```

The value is only returned if this call to `deletePost` was the one that
actually deleted it from DynamoDB.

- Choose **Execute query** again.
- The call still succeeds, but no value is returned.

```
{
  "data": {
    "deletePost": null
  }
}
```

Now let’s try deleting a post, but this time specifying an `expectedValue`.
First though, you’ll need to create a new post because you’ve just deleted the one you’ve
been working with so far.

- In the **Queries** pane, paste the following
  mutation:

```
mutation addPost {
  addPost(
    id:123
    author: "AUTHORNAME"
    title: "Our second post!"
    content: "A new post."
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

- Choose **Execute query** (the orange play
  button).
- The results of the newly created post should appear in the results pane to the right
  of the query pane. Note down the `id` of the newly created object because you
  need it in just a moment. It should look similar to the following:

```
{
  "data": {
    "addPost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our second post!",
      "content": "A new post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

Now let’s try to delete that post, but put in the wrong value for
`expectedVersion`:

- In the **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation deletePost {
  deletePost(
    id:123
    expectedVersion: 9999
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

- Choose **Execute query** (the orange play
  button).

```
{
  "data": {
    "deletePost": null
  },
  "errors": [
    {
      "path": [
        "deletePost"
      ],
      "data": {
        "id": "123",
        "author": "AUTHORNAME",
        "title": "Our second post!",
        "content": "A new post.",
        "url": "https://aws.amazon.com/appsync/",
        "ups": 1,
        "downs": 0,
        "version": 1
      },
      "errorType": "DynamoDB:ConditionalCheckFailedException",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "message": "The conditional request failed (Service: AmazonDynamoDBv2; Status Code: 400; Error Code: ConditionalCheckFailedException; Request ID: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ)"
    }
  ]
}
```

The request failed because the condition expression evaluates to false: the value
for `version` of the post in DynamoDB does not match the
`expectedValue` specified in the arguments. The current value of the object
is returned in the `data` field in the `errors` section of the
GraphQL response.

- Retry the request, but correct the `expectedVersion`:

```
mutation deletePost {
  deletePost(
    id:123
    expectedVersion: 1
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

- Choose **Execute query** (the orange play
  button).
- This time the request succeeds, and the value that was deleted from DynamoDB is
  returned:

```
{
  "data": {
    "deletePost": {
      "id": "123",
      "author": "AUTHORNAME",
      "title": "Our second post!",
      "content": "A new post.",
      "url": "https://aws.amazon.com/appsync/",
      "ups": 1,
      "downs": 0,
      "version": 1
    }
  }
}
```

- Choose **Execute query** again.
- The call still succeeds, but this time no value is returned because the post was
  already deleted in DynamoDB.

```
{
  "data": {
    "deletePost": null
  }
}
```

## Setting Up the allPost

Resolver (DynamoDB Scan)

So far the API is only useful if you know the `id` of each post you want to
look at. Let’s add a new resolver that returns all the posts in the table.

- Choose the **Schema** tab.
- In the **Schema** pane, modify the `Query`
  type to add a new `allPost` query as follows:

```
type Query {
    allPost(count: Int, nextToken: String): PaginatedPosts!
    getPost(id: ID): Post
}
```

- Add a new `PaginationPosts` type:

```
type PaginatedPosts {
    posts: [Post!]!
    nextToken: String
}
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **allPost** field on the **Query** type, and then choose **Attach**.
- In the **Action menu**, choose **Update
  runtime**, then choose **Unit Resolver (VTL only)**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "Scan"
    #if( ${context.arguments.count} )
        ,"limit": $util.toJson($context.arguments.count)
    #end
    #if( ${context.arguments.nextToken} )
        ,"nextToken": $util.toJson($context.arguments.nextToken)
    #end
}
```

This resolver has two optional arguments: `count`, which specifies the
maximum number of items to return in a single call, and `nextToken`, which can
be used to retrieve the next set of results (you’ll show where the value for
`nextToken` comes from later).

- In **Configure the response mapping template**, paste the
  following:

```
{
    "posts": $utils.toJson($context.result.items)
    #if( ${context.result.nextToken} )
        ,"nextToken": $util.toJson($context.result.nextToken)
    #end
}
```

**Note:** This response mapping template is different from
all the others so far. The result of the `allPost` query is a
`PaginatedPosts`, which contains a list of posts and a pagination token. The
shape of this object is different to what is returned from the AWS AppSync DynamoDB
Resolver: the list of posts is called `items` in the AWS AppSync DynamoDB
Resolver results, but is called `posts` in `PaginatedPosts`.

- Choose **Save**.

For more information about `Scan` request mapping, see the [Scan](aws-appsync-resolver-mapping-template-reference-dynamodb-scan.md "aws-appsync-resolver-mapping-template-reference-dynamodb-scan.md")
reference documentation.

### Call the API to Scan All Posts

Now the resolver has been set up, AWS AppSync knows how to translate an incoming
`allPost` query to a DynamoDB`Scan` operation. You can now scan the
table to retrieve all the posts.

Before you can try it out though, you need to populate the table with some data because
you’ve deleted everything you’ve worked with so far.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following
  mutation:

```
mutation addPost {
  post1: addPost(id:1 author: "AUTHORNAME" title: "A series of posts, Volume 1" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post2: addPost(id:2 author: "AUTHORNAME" title: "A series of posts, Volume 2" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post3: addPost(id:3 author: "AUTHORNAME" title: "A series of posts, Volume 3" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post4: addPost(id:4 author: "AUTHORNAME" title: "A series of posts, Volume 4" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post5: addPost(id:5 author: "AUTHORNAME" title: "A series of posts, Volume 5" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post6: addPost(id:6 author: "AUTHORNAME" title: "A series of posts, Volume 6" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post7: addPost(id:7 author: "AUTHORNAME" title: "A series of posts, Volume 7" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post8: addPost(id:8 author: "AUTHORNAME" title: "A series of posts, Volume 8" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
  post9: addPost(id:9 author: "AUTHORNAME" title: "A series of posts, Volume 9" content: "Some content" url: "https://aws.amazon.com/appsync/" ) { title }
}
```

- Choose **Execute query** (the orange play
  button).

Now, let’s scan the table, returning five results at a time.

- In the **Queries** pane, paste the following
  query:

```
query allPost {
  allPost(count: 5) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- The first five posts should appear in the results pane to the right of the query
  pane. It should look similar to the following:

```
{
  "data": {
    "allPost": {
      "posts": [
        {
          "id": "5",
          "title": "A series of posts, Volume 5"
        },
        {
          "id": "1",
          "title": "A series of posts, Volume 1"
        },
        {
          "id": "6",
          "title": "A series of posts, Volume 6"
        },
        {
          "id": "9",
          "title": "A series of posts, Volume 9"
        },
        {
          "id": "7",
          "title": "A series of posts, Volume 7"
        }
      ],
      "nextToken": "eyJ2ZXJzaW9uIjoxLCJ0b2tlbiI6IkFRSUNBSGo4eHR0RG0xWXhUa1F0cEhXMEp1R3B0M1B3eThOSmRvcG9ad2RHYjI3Z0lnRkJEdXdUK09hcnovRGhNTGxLTGdMUEFBQUI1akNDQWVJR0NTcUdTSWIzRFFFSEJxQ0NBZE13Z2dIUEFnRUFNSUlCeUFZSktvWklodmNOQVFjQk1CNEdDV0NHU0FGbEF3UUJMakFSQkF6ajFodkhKU1paT1pncTRaUUNBUkNBZ2dHWnJiR1dQWGxkMDB1N0xEdGY4Z2JsbktzRjRua1VCcks3TFJLcjZBTFRMeGFwVGJZMDRqOTdKVFQyYVRwSzdzbVdtNlhWWFVCTnFIOThZTzBWZHVkdDI2RlkxMHRqMDJ2QTlyNWJTUWpTbWh6NE5UclhUMG9KZWJSQ2JJbXBlaDRSVlg0Tis0WTVCN1IwNmJQWWQzOVhsbTlUTjBkZkFYMVErVCthaXZoNE5jMk50RitxVmU3SlJ5WmpzMEFkSGduM3FWd2VrOW5oeFVVd3JlK1loUks5QkRzemdiMDlmZmFPVXpzaFZ4cVJRbC93RURlOTcrRmVJdXZNby9NZ1F6dUdNbFRyalpNR3FuYzZBRnhwa0VlZTFtR0FwVDFISElUZlluakptYklmMGUzUmcxbVlnVHVSbDh4S0trNmR0QVoraEhLVDhuNUI3VnF4bHRtSnlNUXBrZGl6KzkyL3VzNDl4OWhrMnVxSW01ZFFwMjRLNnF0dm9ZK1BpdERuQTc5djhzb0grVytYT3VuQ2NVVDY4TVZ1Wk5KYkRuSEFSSEVlaTlVNVBTelU5RGZ6d2pPdmhqWDNJMWhwdWUrWi83MDVHVjlPQUxSTGlwZWZPeTFOZFhwZTdHRDZnQW00bUJUK2c1eC9Ec3ZDbWVnSDFDVXRTdHVuU1ZFa2JpZytQRC9oMUwyRTNqSHhVQldaa28yU256WUc0cG0vV1RSWkFVZHZuQT09In0="
    }
  }
}
```

You got five results and a `nextToken` that you can use to get the next set
of results.

- Update the `allPost` query to include the `nextToken` from the
  previous set of results:

```
query allPost {
  allPost(
    count: 5
    nextToken: "eyJ2ZXJzaW9uIjoxLCJ0b2tlbiI6IkFRSUNBSGo4eHR0RG0xWXhUa1F0cEhXMEp1R3B0M1B3eThOSmRvcG9ad2RHYjI3Z0lnRlluNktJRWl6V0ZlR3hJOVJkaStrZUFBQUI1akNDQWVJR0NTcUdTSWIzRFFFSEJxQ0NBZE13Z2dIUEFnRUFNSUlCeUFZSktvWklodmNOQVFjQk1CNEdDV0NHU0FGbEF3UUJMakFSQkF5cW8yUGFSZThnalFpemRCTUNBUkNBZ2dHWk1JODhUNzhIOFVUZGtpdFM2ZFluSWRyVDg4c2lkN1RjZzB2d1k3VGJTTWpSQ2U3WjY3TkUvU2I1dWNETUdDMmdmMHErSGJSL0pteGRzYzVEYnE1K3BmWEtBdU5jSENJdWNIUkJ0UHBPWVdWdCtsS2U5L1pNcWdocXhrem1RaXI1YnIvQkt6dU5hZmJCdE93NmtoM2Jna1BKM0RjWWhpMFBGbmhMVGg4TUVGSjBCcXg3RTlHR1V5N0tUS0JLZlV3RjFQZ0JRREdrNzFYQnFMK2R1S2IrVGtZZzVYMjFrc3NyQmFVTmNXZmhTeXE0ZUJHSWhqZWQ5c3VKWjBSSTc2ZnVQdlZkR3FLNENjQmxHYXhpekZnK2pKK1FneEU1SXduRTNYYU5TR0I4QUpmamR2bU1wbUk1SEdvWjlMUUswclczbG14RDRtMlBsaTNLaEVlcm9pem5zcmdINFpvcXIrN2ltRDN3QkJNd3BLbGQzNjV5Nnc4ZnMrK2FnbTFVOUlKOFFrOGd2bEgySHFROHZrZXBrMWlLdWRIQ25LaS9USnBlMk9JeEVPazVnRFlzRTRUU09HUlVJTkxYY2MvdW1WVEpBMUthV2hWTlAvdjNlSnlZQUszbWV6N2h5WHVXZ1BkTVBNWERQdTdjVnVRa3EwK3NhbGZOd2wvSUx4bHNyNDVwTEhuVFpyRWZvVlV1bXZ5S2VKY1RUU1lET05hM1NwWEd2UT09In0="
  ) {
    posts {
      id
      author
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- The remaining four posts should appear in the results pane to the right of the query
  pane. There is no `nextToken` in this set of results because you’ve paged
  through all nine posts, with none remaining. It should look similar to the
  following:

```
{
  "data": {
    "allPost": {
      "posts": [
        {
          "id": "2",
          "title": "A series of posts, Volume 2"
        },
        {
          "id": "3",
          "title": "A series of posts, Volume 3"
        },
        {
          "id": "4",
          "title": "A series of posts, Volume 4"
        },
        {
          "id": "8",
          "title": "A series of posts, Volume 8"
        }
      ],
      "nextToken": null
    }
  }
}
```

## Setting Up the

allPostsByAuthor Resolver (DynamoDB Query)

In addition to scanning DynamoDB for all posts, you can also query DynamoDB to retrieve posts
created by a specific author. The DynamoDB table you created earlier already has a
`GlobalSecondaryIndex` called `author-index` you can use with a
DynamoDB`Query` operation to retrieve all posts created by a specific author.

- Choose the **Schema** tab.
- In the **Schema** pane, modify the `Query`
  type to add a new `allPostsByAuthor` query as follows:

```
type Query {
    allPostsByAuthor(author: String!, count: Int, nextToken: String): PaginatedPosts!
    allPost(count: Int, nextToken: String): PaginatedPosts!
    getPost(id: ID): Post
}
```

**Note:** This uses the same `PaginatedPosts` type
that you used with the `allPost` query.

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **allPostsByAuthor** field on the **Query** type, and then choose **Attach**.
- In the **Action menu**, choose **Update
  runtime**, then choose **Unit Resolver (VTL only)**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "Query",
    "index" : "author-index",
    "query" : {
      "expression": "author = :author",
        "expressionValues" : {
          ":author" : $util.dynamodb.toDynamoDBJson($context.arguments.author)
        }
    }
    #if( ${context.arguments.count} )
        ,"limit": $util.toJson($context.arguments.count)
    #end
    #if( ${context.arguments.nextToken} )
        ,"nextToken": "${context.arguments.nextToken}"
    #end
}
```

Like the `allPost` resolver, this resolver has two optional arguments:
`count`, which specifies the maximum number of items to return in a single
call, and `nextToken`, which can be used to retrieve the next set of results
(the value for `nextToken` can be obtained from a previous call).

- In **Configure the response mapping template**, paste the
  following:

```
{
    "posts": $utils.toJson($context.result.items)
    #if( ${context.result.nextToken} )
        ,"nextToken": $util.toJson($context.result.nextToken)
    #end
}
```

**Note:** This is the same response mapping template that you
used in the `allPost` resolver.

- Choose **Save**.

For more information about `Query` request mapping, see the [Query](aws-appsync-resolver-mapping-template-reference-dynamodb-query.md "aws-appsync-resolver-mapping-template-reference-dynamodb-query.md")
reference documentation.

### Call the API to Query All

Posts by an Author

Now the resolver has been set up, AWS AppSync knows how to translate an incoming
`allPostsByAuthor` mutation to a DynamoDB`Query` operation against the
`author-index` index. You can now query the table to retrieve all the posts by
a specific author.

Before you do that, however, let’s populate the table with some more posts, because
every post so far has the same author.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following
  mutation:

```
mutation addPost {
  post1: addPost(id:10 author: "Nadia" title: "The cutest dog in the world" content: "So cute. So very, very cute." url: "https://aws.amazon.com/appsync/" ) { author, title }
  post2: addPost(id:11 author: "Nadia" title: "Did you know...?" content: "AppSync works offline?" url: "https://aws.amazon.com/appsync/" ) { author, title }
  post3: addPost(id:12 author: "Steve" title: "I like GraphQL" content: "It's great" url: "https://aws.amazon.com/appsync/" ) { author, title }
}
```

- Choose **Execute query** (the orange play
  button).

Now, let’s query the table, returning all posts authored by `Nadia`.

- In the **Queries** pane, paste the following
  query:

```
query allPostsByAuthor {
  allPostsByAuthor(author: "Nadia") {
    posts {
      id
      title
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- All the posts authored by `Nadia` should appear in the results pane to
  the right of the query pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "10",
          "title": "The cutest dog in the world"
        },
        {
          "id": "11",
          "title": "Did you know...?"
        }
      ],
      "nextToken": null
    }
  }
}
```

Pagination works for `Query` just the same as it does for `Scan`.
For example, let’s look for all posts by `AUTHORNAME`, getting five at a
time.

- In the **Queries** pane, paste the following
  query:

```
query allPostsByAuthor {
  allPostsByAuthor(
    author: "AUTHORNAME"
    count: 5
  ) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- All the posts authored by `AUTHORNAME` should appear in the results pane
  to the right of the query pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "6",
          "title": "A series of posts, Volume 6"
        },
        {
          "id": "4",
          "title": "A series of posts, Volume 4"
        },
        {
          "id": "2",
          "title": "A series of posts, Volume 2"
        },
        {
          "id": "7",
          "title": "A series of posts, Volume 7"
        },
        {
          "id": "1",
          "title": "A series of posts, Volume 1"
        }
      ],
      "nextToken": "eyJ2ZXJzaW9uIjoxLCJ0b2tlbiI6IkFRSUNBSGo4eHR0RG0xWXhUa1F0cEhXMEp1R3B0M1B3eThOSmRvcG9ad2RHYjI3Z0lnSExqRnVhVUR3ZUhEZ2QzNGJ2QlFuY0FBQUNqekNDQW9zR0NTcUdTSWIzRFFFSEJxQ0NBbnd3Z2dKNEFnRUFNSUlDY1FZSktvWklodmNOQVFjQk1CNEdDV0NHU0FGbEF3UUJMakFSQkF5Qkg4Yk1obW9LVEFTZHM3SUNBUkNBZ2dKQ3dISzZKNlJuN3pyYUVKY1pWNWxhSkNtZW1KZ0F5N1dhZkc2UEdTNHpNQzJycTkwZHFJTFV6Z25wck9Gd3pMS3VOQ2JvUXc3VDI5eCtnVExIbGg4S3BqbzB1YjZHQ3FwcDhvNDVmMG9JbDlmdS9JdjNXcFNNSXFKTXZ1MEVGVWs1VzJQaW5jZGlUaVRtZFdYWlU1bkV2NkgyRFBRQWZYYlNnSmlHSHFLbmJZTUZZM0FTdmRIL0hQaVZBb1RCMk1YZkg0eGJOVTdEbjZtRFNhb2QwbzdHZHJEWDNtODQ1UXBQUVNyUFhHemY0WDkyajhIdlBCSWE4Smcrb0RxbHozUVQ5N2FXUXdYWWU2S0h4emI1ejRITXdEdXEyRDRkYzhoMi9CbW10MzRMelVGUVIyaExSZGRaZ0xkdzF5cHJZdFZwY3dEc1d4UURBTzdOcjV2ZEp4VVR2TVhmODBRSnp1REhXREpTVlJLdDJwWmlpaXhXeGRwRmNod1BzQ3d2aVBqMGwrcWFFWU1jMXNQbENkVkFGem43VXJrSThWbS8wWHlwR2xZb3BSL2FkV0xVekgrbGMrYno1ZEM2SnVLVXdtY1EyRXlZeDZiS0Izbi9YdUViWGdFeU5PMWZTdE1rRlhyWmpvMVpzdlYyUFRjMzMrdEs0ZDhkNkZrdjh5VVR6WHhJRkxIaVNsOUx6VVdtT3BCaWhrTFBCT09jcXkyOHh1UmkzOEM3UFRqMmN6c3RkOUo1VUY0azBJdUdEbVZzM2xjdWg1SEJjYThIeXM2aEpvOG1HbFpMNWN6R2s5bi8vRE1EbDY3RlJraG5QNFNhSDBpZGI5VFEvMERLeFRBTUdhcWpPaEl5ekVqd2ZDQVJleFdlbldyOGlPVkhScDhGM25WZVdvbFRGK002N0xpdi9XNGJXdDk0VEg3b0laUU5lYmZYKzVOKy9Td25Hb1dyMTlWK0pEb2lIRVFLZ1cwMWVuYjZKUXo5Slh2Tm95ZzF3RnJPVmxGc2xwNlRHa1BlN2Rnd2IrWT0ifQ=="
    }
  }
}
```

- Update the `nextToken` argument with the value returned from the previous
  query as follows:

```
query allPostsByAuthor {
  allPostsByAuthor(
    author: "AUTHORNAME"
    count: 5
    nextToken: "eyJ2ZXJzaW9uIjoxLCJ0b2tlbiI6IkFRSUNBSGo4eHR0RG0xWXhUa1F0cEhXMEp1R3B0M1B3eThOSmRvcG9ad2RHYjI3Z0lnSExqRnVhVUR3ZUhEZ2QzNGJ2QlFuY0FBQUNqekNDQW9zR0NTcUdTSWIzRFFFSEJxQ0NBbnd3Z2dKNEFnRUFNSUlDY1FZSktvWklodmNOQVFjQk1CNEdDV0NHU0FGbEF3UUJMakFSQkF5Qkg4Yk1obW9LVEFTZHM3SUNBUkNBZ2dKQ3dISzZKNlJuN3pyYUVKY1pWNWxhSkNtZW1KZ0F5N1dhZkc2UEdTNHpNQzJycTkwZHFJTFV6Z25wck9Gd3pMS3VOQ2JvUXc3VDI5eCtnVExIbGg4S3BqbzB1YjZHQ3FwcDhvNDVmMG9JbDlmdS9JdjNXcFNNSXFKTXZ1MEVGVWs1VzJQaW5jZGlUaVRtZFdYWlU1bkV2NkgyRFBRQWZYYlNnSmlHSHFLbmJZTUZZM0FTdmRIL0hQaVZBb1RCMk1YZkg0eGJOVTdEbjZtRFNhb2QwbzdHZHJEWDNtODQ1UXBQUVNyUFhHemY0WDkyajhIdlBCSWE4Smcrb0RxbHozUVQ5N2FXUXdYWWU2S0h4emI1ejRITXdEdXEyRDRkYzhoMi9CbW10MzRMelVGUVIyaExSZGRaZ0xkdzF5cHJZdFZwY3dEc1d4UURBTzdOcjV2ZEp4VVR2TVhmODBRSnp1REhXREpTVlJLdDJwWmlpaXhXeGRwRmNod1BzQ3d2aVBqMGwrcWFFWU1jMXNQbENkVkFGem43VXJrSThWbS8wWHlwR2xZb3BSL2FkV0xVekgrbGMrYno1ZEM2SnVLVXdtY1EyRXlZeDZiS0Izbi9YdUViWGdFeU5PMWZTdE1rRlhyWmpvMVpzdlYyUFRjMzMrdEs0ZDhkNkZrdjh5VVR6WHhJRkxIaVNsOUx6VVdtT3BCaWhrTFBCT09jcXkyOHh1UmkzOEM3UFRqMmN6c3RkOUo1VUY0azBJdUdEbVZzM2xjdWg1SEJjYThIeXM2aEpvOG1HbFpMNWN6R2s5bi8vRE1EbDY3RlJraG5QNFNhSDBpZGI5VFEvMERLeFRBTUdhcWpPaEl5ekVqd2ZDQVJleFdlbldyOGlPVkhScDhGM25WZVdvbFRGK002N0xpdi9XNGJXdDk0VEg3b0laUU5lYmZYKzVOKy9Td25Hb1dyMTlWK0pEb2lIRVFLZ1cwMWVuYjZKUXo5Slh2Tm95ZzF3RnJPVmxGc2xwNlRHa1BlN2Rnd2IrWT0ifQ=="
  ) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- The remaining posts authored by `AUTHORNAME` should appear in the results
  pane to the right of the query pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "8",
          "title": "A series of posts, Volume 8"
        },
        {
          "id": "5",
          "title": "A series of posts, Volume 5"
        },
        {
          "id": "3",
          "title": "A series of posts, Volume 3"
        },
        {
          "id": "9",
          "title": "A series of posts, Volume 9"
        }
      ],
      "nextToken": null
    }
  }
}
```

## Using Sets

Up to this point the `Post` type has been a flat key/value object. You can also
model complex objects with the AWS AppSyncDynamoDB resolver, such as sets, lists, and maps.

Let’s update the `Post` type to include tags. A post can have 0 or more tags,
which are stored in DynamoDB as a String Set. You’ll also set up some mutations to add and remove
tags, and a new query to scan for posts with a specific tag.

- Choose the **Schema** tab.
- In the **Schema** pane, modify the `Post` type
  to add a new `tags` field as follows:

```
type Post {
  id: ID!
  author: String
  title: String
  content: String
  url: String
  ups: Int!
  downs: Int!
  version: Int!
  tags: [String!]
}
```

- In the **Schema** pane, modify the `Query`
  type to add a new `allPostsByTag` query as follows:

```
type Query {
  allPostsByTag(tag: String!, count: Int, nextToken: String): PaginatedPosts!
  allPostsByAuthor(author: String!, count: Int, nextToken: String): PaginatedPosts!
  allPost(count: Int, nextToken: String): PaginatedPosts!
  getPost(id: ID): Post
}
```

- In the **Schema** pane, modify the `Mutation`
  type to add new `addTag` and `removeTag` mutations as
  follows:

```
type Mutation {
  addTag(id: ID!, tag: String!): Post
  removeTag(id: ID!, tag: String!): Post
  deletePost(id: ID!, expectedVersion: Int): Post
  upvotePost(id: ID!): Post
  downvotePost(id: ID!): Post
  updatePost(
    id: ID!,
    author: String,
    title: String,
    content: String,
    url: String,
    expectedVersion: Int!
  ): Post
  addPost(
    author: String!,
    title: String!,
    content: String!,
    url: String!
  ): Post!
}
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **allPostsByTag** field on the **Query** type, and then choose **Attach**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "Scan",
    "filter": {
      "expression": "contains (tags, :tag)",
        "expressionValues": {
          ":tag": $util.dynamodb.toDynamoDBJson($context.arguments.tag)
        }
    }
    #if( ${context.arguments.count} )
        ,"limit": $util.toJson($context.arguments.count)
    #end
    #if( ${context.arguments.nextToken} )
        ,"nextToken": $util.toJson($context.arguments.nextToken)
    #end
}
```

- In **Configure the response mapping template**, paste the
  following:

```
{
    "posts": $utils.toJson($context.result.items)
    #if( ${context.result.nextToken} )
        ,"nextToken": $util.toJson($context.result.nextToken)
    #end
}
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **addTag** field on the **Mutation** type, and then choose **Attach**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },
    "update" : {
        "expression" : "ADD tags :tags, version :plusOne",
        "expressionValues" : {
            ":tags" : { "SS": [ $util.toJson($context.arguments.tag) ] },
            ":plusOne" : { "N" : 1 }
        }
    }
}
```

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **removeTag** field on the **Mutation** type, and then choose **Attach**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
    },
    "update" : {
        "expression" : "DELETE tags :tags ADD version :plusOne",
        "expressionValues" : {
            ":tags" : { "SS": [ $util.toJson($context.arguments.tag) ] },
            ":plusOne" : { "N" : 1 }
        }
    }
}
```

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

- Choose **Save**.

### Call the API to Work with Tags

Now that you’ve set up the resolvers, AWS AppSync knows how to translate incoming
`addTag`, `removeTag`, and `allPostsByTag` requests into
DynamoDB`UpdateItem` and `Scan` operations.

To try it out, let’s select one of the posts you created earlier. For example, let’s use
a post authored by `Nadia`.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following
  query:

```
query allPostsByAuthor {
  allPostsByAuthor(
    author: "Nadia"
  ) {
    posts {
      id
      title
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- All of Nadia’s posts should appear in the results pane to the right of the query
  pane. It should look similar to the following:

```
{
  "data": {
    "allPostsByAuthor": {
      "posts": [
        {
          "id": "10",
          "title": "The cutest dog in the world"
        },
        {
          "id": "11",
          "title": "Did you known...?"
        }
      ],
      "nextToken": null
    }
  }
}
```

- Let’s use the one with the title `"The cutest dog in the world"`. Note
  down its `id` because you’ll use it later.

Now let’s try adding a `dog` tag.

- In the **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation addTag {
  addTag(id:10 tag: "dog") {
    id
    title
    tags
  }
}
```

- Choose **Execute query** (the orange play
  button).
- The post is updated with the new tag.

```
{
  "data": {
    "addTag": {
      "id": "10",
      "title": "The cutest dog in the world",
      "tags": [
        "dog"
      ]
    }
  }
}
```

You can add more tags as follows:

- Update the mutation to change the `tag` argument to
  `puppy`.

```
mutation addTag {
  addTag(id:10 tag: "puppy") {
    id
    title
    tags
  }
}
```

- Choose **Execute query** (the orange play
  button).
- The post is updated with the new tag.

```
{
  "data": {
    "addTag": {
      "id": "10",
      "title": "The cutest dog in the world",
      "tags": [
        "dog",
        "puppy"
      ]
    }
  }
}
```

You can also delete tags:

- In the **Queries** pane, paste the following mutation.
  You’ll also need to update the `id` argument to the value you noted down
  earlier.

```
mutation removeTag {
  removeTag(id:10 tag: "puppy") {
    id
    title
    tags
  }
}
```

- Choose **Execute query** (the orange play
  button).
- The post is updated and the `puppy` tag is deleted.

```
{
  "data": {
    "addTag": {
      "id": "10",
      "title": "The cutest dog in the world",
      "tags": [
        "dog"
      ]
    }
  }
}
```

You can also search for all posts that have a tag:

- In the **Queries** pane, paste the following
  query:

```
query allPostsByTag {
  allPostsByTag(tag: "dog") {
    posts {
      id
      title
      tags
    }
    nextToken
  }
}
```

- Choose **Execute query** (the orange play
  button).
- All posts that have the `dog` tag are returned as follows:

```
{
  "data": {
    "allPostsByTag": {
      "posts": [
        {
          "id": "10",
          "title": "The cutest dog in the world",
          "tags": [
            "dog",
            "puppy"
          ]
        }
      ],
      "nextToken": null
    }
  }
}
```

## Using Lists and Maps

In addition to using DynamoDB sets, you can also use DynamoDB lists and maps to model complex
data in a single object.

Let’s add the ability to add comments to posts. This will be modeled as a list of map
objects on the `Post` object in DynamoDB.

**Note:** in a real application, you would model comments in
their own table. For this tutorial, you’ll just add them in the `Post`
table.

- Choose the **Schema** tab.
- In the **Schema** pane, add a new `Comment`
  type as follows:

```
type Comment {
    author: String!
    comment: String!
}
```

- In the **Schema** pane, modify the `Post` type
  to add a new `comments` field as follows:

```
type Post {
  id: ID!
  author: String
  title: String
  content: String
  url: String
  ups: Int!
  downs: Int!
  version: Int!
  tags: [String!]
  comments: [Comment!]
}
```

- In the **Schema** pane, modify the `Mutation`
  type to add a new `addComment` mutation as follows:

```
type Mutation {
  addComment(id: ID!, author: String!, comment: String!): Post
  addTag(id: ID!, tag: String!): Post
  removeTag(id: ID!, tag: String!): Post
  deletePost(id: ID!, expectedVersion: Int): Post
  upvotePost(id: ID!): Post
  downvotePost(id: ID!): Post
  updatePost(
    id: ID!,
    author: String,
    title: String,
    content: String,
    url: String,
    expectedVersion: Int!
  ): Post
  addPost(
    author: String!,
    title: String!,
    content: String!,
    url: String!
  ): Post!
}
```

- Choose **Save**.
- In the **Data types** pane on the right, find the newly
  created **addComment** field on the **Mutation** type, and then choose **Attach**.
- In **Data source name**, choose **PostDynamoDBTable**.
- In **Configure the request mapping template**, paste the
  following:

```
{
  "version" : "2017-02-28",
  "operation" : "UpdateItem",
  "key" : {
    "id" : $util.dynamodb.toDynamoDBJson($context.arguments.id)
  },
  "update" : {
    "expression" : "SET comments = list_append(if_not_exists(comments, :emptyList), :newComment) ADD version :plusOne",
    "expressionValues" : {
      ":emptyList": { "L" : [] },
      ":newComment" : { "L" : [
        { "M": {
          "author": $util.dynamodb.toDynamoDBJson($context.arguments.author),
          "comment": $util.dynamodb.toDynamoDBJson($context.arguments.comment)
          }
        }
      ] },
      ":plusOne" : $util.dynamodb.toDynamoDBJson(1)
    }
  }
}
```

This update expression will append a list containing our new comment to the existing
`comments` list. If the list doesn’t already exist, it will be
created.

- In **Configure the response mapping template**, paste the
  following:

```
$utils.toJson($context.result)
```

- Choose **Save**.

### Call the API to Add a Comment

Now that you’ve set up the resolvers, AWS AppSync knows how to translate incoming
`addComment` requests into DynamoDB`UpdateItem` operations.

Let’s try it out by adding a comment to the same post you added the tags to.

- Choose the **Queries** tab.
- In the **Queries** pane, paste the following
  query:

```
mutation addComment {
  addComment(
    id:10
    author: "Steve"
    comment: "Such a cute dog."
  ) {
    id
    comments {
      author
      comment
    }
  }
}
```

- Choose **Execute query** (the orange play
  button).
- All of Nadia’s posts should appear in the results pane to the right of the query
  pane. It should look similar to the following:

```
{
  "data": {
    "addComment": {
      "id": "10",
      "comments": [
        {
          "author": "Steve",
          "comment": "Such a cute dog."
        }
      ]
    }
  }
}
```

If you execute the request multiple times, multiple comments will be appended to the
list.

## Conclusion

In this tutorial, you’ve built an API that lets us manipulate Post objects in DynamoDB using
AWS AppSync and GraphQL. For more information, see the [Resolver Mapping Template
Reference](resolver-mapping-template-reference.md#aws-appsync-resolver-mapping-template-reference "resolver-mapping-template-reference.md#aws-appsync-resolver-mapping-template-reference").

To clean up, you can delete the AppSync GraphQL API from the console.

To delete the DynamoDB table and the IAM role you created for this tutorial, you can run
the following to delete the `AWSAppSyncTutorialForAmazonDynamoDB` stack, or visit
the CloudFormation console and delete the stack:

```
aws cloudformation delete-stack \
    --stack-name AWSAppSyncTutorialForAmazonDynamoDB
```
