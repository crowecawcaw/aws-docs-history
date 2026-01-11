# Using pipeline resolvers in

AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](tutorials-js.md "tutorials-js.md").

AWS AppSync provides a simple way to wire a GraphQL field to a single data source through
unit resolvers. However, executing a single operation might not be enough. Pipeline resolvers
offer the ability to serially execute operations against data sources. Create functions in
your API and attach them to a pipeline resolver. Each function execution result is piped to
the next until no function is left to execute. With pipeline resolvers you can now build more
complex workflows directly in AWS AppSync. In this tutorial, you build a simple pictures viewing
app, where users can post and view pictures posted by their friends.

## One-Click Setup

If you want to automatically set up the GraphQL endpoint in AWS AppSync with all the
resolvers configured and the necessary AWS resources, you can use the following AWS CloudFormation
template :

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](/images/appsync/latest/devguide/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/pipeline/pipeline-resolvers-full.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/pipeline/pipeline-resolvers-full.yaml")

This stack creates the following resources in your account:

- IAM Role for AWS AppSync to access the resources in your account
- 2 DynamoDB tables
- 1 Amazon Cognito user pool
- 2 Amazon Cognito user pool groups
- 3 Amazon Cognito user pool users
- 1 AWS AppSync API

At the end of the AWS CloudFormation stack creation process you receive one email for
each of the three Amazon Cognito users that were created. Each email contains a temporary
password that you use to log in as an Amazon Cognito user to the AWS AppSync console. Save
the passwords for the remainder of the tutorial.

## Manual Setup

If you prefer to manually go through a step-by-step process through the AWS AppSync
console, follow the setup process below.

### Setting Up Your Non AWS AppSync Resources

The API communicates with two DynamoDB tables: a **pictures** table that stores pictures and a **friends** table that stores relationships between users. The API is
configured to use Amazon Cognito user pool as authentication type. The following CloudFormation stack sets
up these resources in the account.

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](/images/appsync/latest/devguide/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/pipeline/pipeline-resolvers-resources-only.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/pipeline/pipeline-resolvers-resources-only.yaml")

At the end of the AWS CloudFormation stack creation process you receive one email for
each of the three Amazon Cognito users that were created. Each email contains a
temporary password that you use to log in as an Amazon Cognito user to the AWS AppSync
console. Save the passwords for the remainder of the tutorial.

### Creating Your GraphQL API

To create the GraphQL API in AWS AppSync:

1. Open the AWS AppSync console and choose **Build From
   Scratch** and choose **Start**.
2. Set the name of the API to `AppSyncTutorial-PicturesViewer`.
3. Choose **Create**.

The AWS AppSync console creates a new GraphQL API for you using the API key
authentication mode. You can use the console to set up the rest of the GraphQL API and
run queries against it for the rest of this tutorial.

### Configuring The GraphQL API

You need to configure the AWS AppSync API with the Amazon Cognito user pool that you
just created.

1. Choose the **Settings** tab.
2. Under the **Authorization Type** section, choose
   _Amazon Cognito User Pool_.
3. Under **User Pool Configuration**, choose
   **US-WEST-2** for the _AWS Region_.
4. Choose the **AppSyncTutorial-UserPool** user
   pool.
5. Choose **DENY** as _Default Action_.
6. Leave the **AppId client regex** field
   blank.
7. Choose **Save**.

The API is now set up to use Amazon Cognito user pool as its authorization
type.

### Configuring Data Sources

for the DynamoDB Tables

After the DynamoDB tables have been created, navigate to your AWS AppSync GraphQL API in
the console and choose the **Data Sources** tab. Now,
you’re going to create a datasource in AWS AppSync for each of the DynamoDB tables that you
just created.

1. Choose the **Data source** tab.
2. Choose **New** to create a new data source.
3. For the data source name, enter `PicturesDynamoDBTable`.
4. For data source type, choose **Amazon DynamoDB
   table**.
5. For region, choose **US-WEST-2**.
6. From the list of tables, choose the **AppSyncTutorial-Pictures**DynamoDB table.
7. In the **Create or use an existing role** section,
   choose **Existing role**.
8. Choose the role that was just created from the CloudFormation template. If you
   did not change the _ResourceNamePrefix_,
   the name of the role should be **AppSyncTutorial-DynamoDBRole**.
9. Choose **Create**.

Repeat the same process for the **friends** table, the
name of the DynamoDB table should be **AppSyncTutorial-Friends** if you did not change the _ResourceNamePrefix_ parameter at the time of
creating the CloudFormation stack.

### Creating the GraphQL Schema

Now that the data sources are connected to your DynamoDB tables, let’s create a GraphQL
schema. From the schema editor in the AWS AppSync console, make sure your schema matches
the following schema:

```
schema {
    query: Query
    mutation: Mutation
}

type Mutation {
    createPicture(input: CreatePictureInput!): Picture!
    @aws_auth(cognito_groups: ["Admins"])
    createFriendship(id: ID!, target: ID!): Boolean
    @aws_auth(cognito_groups: ["Admins"])
}

type Query {
    getPicturesByOwner(id: ID!): [Picture]
    @aws_auth(cognito_groups: ["Admins", "Viewers"])
}

type Picture {
    id: ID!
    owner: ID!
    src: String
}

input CreatePictureInput {
    owner: ID!
    src: String!
}
```

Choose **Save Schema** to save your schema.

Some of the schema fields have been annotated with the _@aws_auth_ directive. Since the API default action
configuration is set to _DENY_, the API
rejects all users that are not members of the groups mentioned inside the _@aws_auth_ directive. For more information about how
to secure your API, you can read the [Security](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security") page. In this case, only admin users have access to the _Mutation.createPicture_ and _Mutation.createFriendship_ fields, while users that
are members of either _Admins_ or _Viewers_ groups can access the _Query.getPicturesByOwner_ field. All other users
don’t have access.

### Configuring Resolvers

Now that you have a valid GraphQL schema and two data sources, you can attach
resolvers to the GraphQL fields on the schema. The API offers the following
capabilities:

- Create a picture via the _Mutation.createPicture_ field
- Create friendship via the _Mutation.createFriendship_ field
- Retrieve a picture via the _Query.getPicture_ field

#### Mutation.createPicture

From the schema editor in the AWS AppSync console, on the right side choose
**Attach Resolver** for `createPicture(input:
 CreatePictureInput!): Picture!`. Choose the DynamoDB*PicturesDynamoDBTable* data source. In the
**request mapping template** section, add the
following template:

```
#set($id = $util.autoId())

{
    "version" : "2018-05-29",

    "operation" : "PutItem",

    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($id),
        "owner": $util.dynamodb.toDynamoDBJson($ctx.args.input.owner)
    },

    "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args.input)
}
```

In the **response mapping template** section, add the
following template:

```
#if($ctx.error)
    $util.error($ctx.error.message, $ctx.error.type)
#end
$util.toJson($ctx.result)
```

The create picture functionality is done. You are saving a picture in the
**Pictures** table, using a randomly generated UUID
as id of the picture, and using the Cognito username as owner of the picture.

#### Mutation.createFriendship

From the schema editor in the AWS AppSync console, on the right side choose
**Attach Resolver** for `createFriendship(id:
 ID!, target: ID!): Boolean`. Choose the DynamoDB**FriendsDynamoDBTable** data source. In the **request
mapping template** section, add the following template:

```
#set($userToFriendFriendship = { "userId" : "$ctx.args.id", "friendId": "$ctx.args.target" })
#set($friendToUserFriendship = { "userId" : "$ctx.args.target", "friendId": "$ctx.args.id" })
#set($friendsItems = [$util.dynamodb.toMapValues($userToFriendFriendship), $util.dynamodb.toMapValues($friendToUserFriendship)])

{
    "version" : "2018-05-29",
    "operation" : "BatchPutItem",
    "tables" : {
        ## Replace 'AppSyncTutorial-' default below with the ResourceNamePrefix you provided in the CloudFormation template
        "AppSyncTutorial-Friends": $util.toJson($friendsItems)
    }
}
```

Important: In the **BatchPutItem** request template,
the exact name of the DynamoDB table should be present. The default table name is
_AppSyncTutorial-Friends_. If you are
using the wrong table name, you get an error when AppSync tries to assume the
provided role.

For the sake of simplicity in this tutorial, proceed as if the friendship request
has been approved and save the relationship entry directly into the **AppSyncTutorialFriends** table.

Effectively, you’re storing two items for each friendship as the relationship is
bi-directional. For more details about Amazon DynamoDB best practices to represent
many-to-many relationships, see [DynamoDB Best Practices](../../../amazondynamodb/latest/developerguide/bp-adjacency-graphs.md "../../../amazondynamodb/latest/developerguide/bp-adjacency-graphs.md") .

In the **response mapping template** section, add the
following template:

```
#if($ctx.error)
    $util.error($ctx.error.message, $ctx.error.type)
#end
true
```

Note: Make sure your request template contains the right table name. The default
name is _AppSyncTutorial-Friends_, but your
table name might differ if you changed the CloudFormation **ResourceNamePrefix** parameter.

#### Query.getPicturesByOwner

Now that you have friendships and pictures, you need to provide the ability for
users to view their friends’ pictures. To satisfy this requirement, you need to first
check that the requester is friend with the owner, and finally query for the
pictures.

Because this functionality requires two data source operations, you’re going to
create two functions. The first function, **isFriend**,
checks whether the requester and the owner are friends. The second function,
**getPicturesByOwner**, retrieves the requested
pictures given an owner ID. Let’s look at the execution flow below for the proposed
resolver on the _Query.getPicturesByOwner_
field:

1. Before mapping template: Prepare the context and field input
   arguments.
2. isFriend function: Checks whether the requester is the owner of the picture.
   If not, it checks whether the requester and owner users are friends by doing a
   DynamoDB GetItem operation on the friends table.
3. getPicturesByOwner function: Retrieves pictures from the Pictures table
   using a DynamoDB Query operation on the _owner-index_ Global Secondary Index.
4. After mapping template: Maps picture result so DynamoDB attributes map
   correctly to the expected GraphQL type fields.

Let’s first create the functions.

##### isFriend Function

1. Choose the **Functions** tab.
2. Choose **Create Function** to create a
   function.
3. For the data source name, enter `FriendsDynamoDBTable`.
4. For the function name, enter _isFriend_.
5. Inside the request mapping template text area, paste the following
   template:

```
#set($ownerId = $ctx.prev.result.owner)
#set($callerId = $ctx.prev.result.callerId)

## if the owner is the caller, no need to make the check
#if($ownerId == $callerId)
    #return($ctx.prev.result)
#end

{
    "version" : "2018-05-29",

    "operation" : "GetItem",

    "key" : {
        "userId" : $util.dynamodb.toDynamoDBJson($callerId),
        "friendId" : $util.dynamodb.toDynamoDBJson($ownerId)
    }
}
```

6. Inside the response mapping template text area, paste the following
   template:

```
#if($ctx.error)
    $util.error("Unable to retrieve friend mapping message: ${ctx.error.message}", $ctx.error.type)
#end

## if the users aren't friends
#if(!$ctx.result)
    $util.unauthorized()
#end

$util.toJson($ctx.prev.result)
```

7. Choose **Create Function**.

Result: You’ve created the **isFriend**
function.

##### getPicturesByOwner function

1. Choose the **Functions** tab.
2. Choose **Create Function** to create a
   function.
3. For the data source name, enter
   `PicturesDynamoDBTable`.
4. For the function name, enter `getPicturesByOwner`.
5. Inside the request mapping template text area, paste the following
   template:

```
{
    "version" : "2018-05-29",

    "operation" : "Query",

    "query" : {
        "expression": "#owner = :owner",
        "expressionNames": {
            "#owner" : "owner"
        },
        "expressionValues" : {
            ":owner" : $util.dynamodb.toDynamoDBJson($ctx.prev.result.owner)
        }
    },

    "index": "owner-index"
}
```

6. Inside the response mapping template text area, paste the following
   template:

```
#if($ctx.error)
    $util.error($ctx.error.message, $ctx.error.type)
#end

$util.toJson($ctx.result)
```

7. Choose **Create Function**.

Result: You’ve created the **getPicturesByOwner**
function. Now that the functions have been created, attach a pipeline resolver to
the _Query.getPicturesByOwner_
field.

From the schema editor in the AWS AppSync console, on the right side choose
**Attach Resolver** for
`Query.getPicturesByOwner(id: ID!): [Picture]`. On the following
page, choose the **Convert to pipeline resolver**
link that appears underneath the data source drop-down list. Use the following for
the before mapping template:

```
#set($result = { "owner": $ctx.args.id, "callerId": $ctx.identity.username })
$util.toJson($result)
```

In the **after mapping template** section, use the
following:

```
#foreach($picture in $ctx.result.items)
    ## prepend "src://" to picture.src property
    #set($picture['src'] = "src://${picture['src']}")
#end
$util.toJson($ctx.result.items)
```

Choose **Create Resolver**. You have successfully
attached your first pipeline resolver. On the same page, add the two functions you
created previously. In the functions section, choose **Add A
Function** and then choose or type the name of the first function,
**isFriend**. Add the second function by following
the same process for the **getPicturesByOwner**
function. Make sure the **isFriend** function appears
first in the list followed by the **getPicturesByOwner** function. You can use the up and down arrows to
rearrange to order of execution of the functions in the pipeline.

Now that the pipeline resolver is created and you’ve attached the functions,
let’s test the newly created GraphQL API.

## Testing Your GraphQL API

First, you need to populate pictures and friendships by executing a few mutations using
the admin user you created. On the left side of the AWS AppSync console, choose the **Queries** tab.

### createPicture Mutation

1. In AWS AppSync console, choose the **Queries**
   tab.
2. Choose **Login With User Pools**.
3. On the modal, enter the Cognito Sample Client ID that was created by the
   CloudFormation stack for example, 37solo6mmhh7k4v63cqdfgdg5d).
4. Enter the user name you passed as parameter to the CloudFormation stack.
   Default is **nadia**.
5. Use the temporary password that was sent to the email you provided as parameter
   to the CloudFormation stack (for example, _UserPoolUserEmail_).
6. Choose Login. You should now see the button renamed to **Logout nadia**, or whatever user name you chose when creating the
   CloudFormation stack (that is, _UserPoolUsername_).

Let’s send a few _createPicture_ mutations
to populate the pictures table. Execute the following GraphQL query inside the
console:

```
mutation {
  createPicture(input:{
    owner: "nadia"
    src: "nadia.jpg"
  }) {
    id
    owner
    src
  }
}
```

The response should look like below:

```
{
  "data": {
    "createPicture": {
      "id": "c6fedbbe-57ad-4da3-860a-ffe8d039882a",
      "owner": "nadia",
      "src": "nadia.jpg"
    }
  }
}
```

Let’s add a few more pictures:

```
mutation {
  createPicture(input:{
    owner: "shaggy"
    src: "shaggy.jpg"
  }) {
    id
    owner
    src
  }
}
```

```
mutation {
  createPicture(input:{
    owner: "rex"
    src: "rex.jpg"
  }) {
    id
    owner
    src
  }
}
```

You’ve added three pictures using **nadia** as the admin
user.

### createFriendship Mutation

Let’s add a friendship entry. Execute the following mutations in the console.

Note: You must still be logged in as the admin user (the default admin user is
**nadia**).

```
mutation {
  createFriendship(id: "nadia", target: "shaggy")
}
```

The response should look like:

```
{
  "data": {
    "createFriendship": true
  }
}
```

**nadia** and **shaggy** are
friends. **rex** is not friends with anybody.

### getPicturesByOwner Query

For this step, log in as the **nadia** user using
Cognito User Pools, using the credentials set up in the beginning of this tutorial. As
**nadia**, retrieve the pictures owned by **shaggy**.

```
query {
    getPicturesByOwner(id: "shaggy") {
        id
        owner
        src
    }
}
```

Since **nadia** and **shaggy** are friends, the query should return the corresponding
picture.

```
{
  "data": {
    "getPicturesByOwner": [
      {
        "id": "05a16fba-cc29-41ee-a8d5-4e791f4f1079",
        "owner": "shaggy",
        "src": "src://shaggy.jpg"
      }
    ]
  }
}
```

Similarly, if **nadia** attempts to retrieve her own
pictures, it also succeeds. The pipeline resolver has been optimized to avoid running
the **isFriend** GetItem operation in that case. Try the
following query:

```
query {
    getPicturesByOwner(id: "nadia") {
        id
        owner
        src
    }
}
```

If you enable logging on your API (in the **Settings**
pane), set the debug level to **ALL**, and run the same
query again, it returns logs for the field execution. By looking at the logs, you can
determine whether the **isFriend** function returned early
at the **Request Mapping Template** stage:

```
{
  "errors": [],
  "mappingTemplateType": "Request Mapping",
  "path": "[getPicturesByOwner]",
  "resolverArn": "arn:aws:appsync:us-west-2:XXXX:apis/XXXX/types/Query/fields/getPicturesByOwner",
  "functionArn": "arn:aws:appsync:us-west-2:XXXX:apis/XXXX/functions/o2f42p2jrfdl3dw7s6xub2csdfs",
  "functionName": "isFriend",
  "earlyReturnedValue": {
    "owner": "nadia",
    "callerId": "nadia"
  },
  "context": {
    "arguments": {
      "id": "nadia"
    },
    "prev": {
      "result": {
        "owner": "nadia",
        "callerId": "nadia"
      }
    },
    "stash": {},
    "outErrors": []
  },
  "fieldInError": false
}
```

The _earlyReturnedValue_ key represents the
data that was returned by the _#return_
directive.

Finally, even though **rex** is a member of the
**Viewers** Cognito UserPool Group, and because
**rex** isn’t friends with anybody, he won’t be able to
access any of the pictures owned by **shaggy** or **nadia**. If you log in as **rex**
in the console and execute the following query:

```
query {
    getPicturesByOwner(id: "nadia") {
        id
        owner
        src
    }
}
```

You get the following unauthorized error:

```
{
  "data": {
    "getPicturesByOwner": null
  },
  "errors": [
    {
      "path": [
        "getPicturesByOwner"
      ],
      "data": null,
      "errorType": "Unauthorized",
      "errorInfo": null,
      "locations": [
        {
          "line": 2,
          "column": 9,
          "sourceName": null
        }
      ],
      "message": "Not Authorized to access getPicturesByOwner on type Query"
    }
  ]
}
```

You have successfully implemented complex authorization using pipeline
resolvers.
