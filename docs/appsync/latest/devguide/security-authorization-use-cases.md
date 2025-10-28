# Access control use cases for securing requests

and responses

In the [Security](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security") section you learned about the different
Authorization modes for protecting your API and an introduction was given on Fine Grained Authorization
mechanisms to understand the concepts and flow. Since AWS AppSync allows you to perform logic full operations on
data through the use of GraphQL Resolver [Mapping templates](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview"), you can protect
data on read or write in a very flexible manner using a combination of user identity, conditionals, and data
injection.

If you’re not familiar with editing AWS AppSync Resolvers, review the [programming
guide](resolver-mapping-template-reference-programming-guide.md#aws-appsync-resolver-mapping-template-reference-programming-guide "resolver-mapping-template-reference-programming-guide.md#aws-appsync-resolver-mapping-template-reference-programming-guide").

## Overview

Granting access to data in a system is traditionally done through an [Access control matrix](https://en.wikipedia.org/wiki/Access_Control_Matrix "https://en.wikipedia.org/wiki/Access_Control_Matrix") where the
intersection of a row (resource) and column (user/role) is the permissions granted.

AWS AppSync uses resources in your own account and threads identity (user/role)
information into the GraphQL request and response as a [context
object](resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference "resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference"), which you can use in the resolver. This means that permissions can be
granted appropriately either on write or read operations based on the resolver logic. If
this logic is at the resource level, for example only certain named users or groups can
read/write to a specific database row, then that “authorization metadata” must be
stored. AWS AppSync does not store any data so therefore you must store this authorization
metadata with the resources so that permissions can be calculated. Authorization
metadata is usually an attribute (column) in a DynamoDB table, such as an **owner** or list of users/groups. For example there could be
**Readers** and **Writers** attributes.

From a high level, what this means is that if you are reading an individual item from
a data source, you perform a conditional `#if () ... #end` statement in the
response template after the resolver has read from the data source. The check will
normally be using user or group values in `$context.identity` for membership
checks against the authorization metadata returned from a read operation. For multiple
records, such as lists returned from a table `Scan` or `Query`,
you’ll send the condition check as part of the operation to the data source using
similar user or group values.

Similarly when writing data you’ll apply a conditional statement to the action (like a
`PutItem` or `UpdateItem` to see if the user or group making a
mutation has permission. The conditional again will many times be using a value in
`$context.identity` to compare against authorization metadata on that
resource. For both request and response templates you can also use custom headers from
clients to perform validation checks.

## Reading data

As outlined above the authorization metadata to perform a check must be stored with a
resource or passed in to the GraphQL request (identity, header, etc.). To demonstrate
this suppose you have the DynamoDB table below:

![DynamoDB table with ID, Data, PeopleCanAccess, GroupsCanAccess, and Owner columns.](images/auth.png)

The primary key is `id` and the data to be accessed is `Data`. The other columns are
examples of checks you can perform for authorization. `Owner` would be a `String`
while `PeopleCanAccess` and `GroupsCanAccess` would be `String Sets` as
outlined in the [Resolver mapping
template reference for DynamoDB](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb").

In the [resolver mapping template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview") the diagram shows how the response
template contains not only the context object but also the results from the data source.
For GraphQL queries of individual items, you can use the response template to check if
the user is allowed to see these results or return an authorization error message. This
is sometimes referred to as an “Authorization filter”. For GraphQL queries returning
lists, using a Scan or Query, it is more performant to perform the check on the request
template and return data only if an authorization condition is satisfied. The
implementation is then:

1. GetItem - authorization check for individual records. Done using `#if()
... #end` statements.
2. Scan/Query operations - authorization check is a
   `"filter":{"expression":...}` statement. Common checks are
   equality (`attribute = :input`) or checking if a value is in a list
   (`contains(attribute, :input)`).

In #2 the `attribute` in both statements represents the column name of the
record in a table, such as `Owner` in our above example. You can alias this
with a `#` sign and use `"expressionNames":{...}` but it’s not
mandatory. The `:input` is a reference to the value you’re comparing to the
database attribute, which you will define in `"expressionValues":{...}`.
You’ll see these examples below.

### Use case: owner can read

Using the table above, if you only wanted to return data if `Owner ==
 Nadia` for an individual read operation (`GetItem`) your
template would look like:

```
#if($context.result["Owner"] == $context.identity.username)
    $utils.toJson($context.result)
#else
    $utils.unauthorized()
#end
```

A couple things to mention here which will be re-used in the remaining sections.
First, the check uses `$context.identity.username` which will be the
friendly user sign-up name if Amazon Cognito user pools is used and will be the user identity
if IAM is used (including Amazon Cognito Federated Identities). There are other values to
store for an owner such as the unique “Amazon Cognito identity” value, which is useful when
federating logins from multiple locations, and you should review the options
available in the [Resolver
Mapping Template Context Reference](resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference "resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference").

Second, the conditional else check responding with
`$util.unauthorized()` is completely optional but recommended as a
best practice when designing your GraphQL API.

### Use case: hardcode specific access

```
// This checks if the user is part of the Admin group and makes the call
#foreach($group in $context.identity.claims.get("cognito:groups"))
    #if($group == "Admin")
        #set($inCognitoGroup = true)
    #end
#end
#if($inCognitoGroup)
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    },
    "attributeValues" : {
        "owner" : $util.dynamodb.toDynamoDBJson($context.identity.username)
        #foreach( $entry in $context.arguments.entrySet() )
            ,"${entry.key}" : $util.dynamodb.toDynamoDBJson($entry.value)
        #end
    }
}
#else
    $utils.unauthorized()
#end
```

### Use case: filtering a list of results

In the previous example you were able to perform a check against
`$context.result` directly as it returned a single item, however some
operations like a scan will return multiple items in
`$context.result.items` where you need to perform the authorization
filter and only return results that the user is allowed to see. Suppose the
`Owner` field had the Amazon Cognito IdentityID this time set on the record,
you could then use the following response mapping template to filter to only show
those records that the user owned:

```
#set($myResults = [])
#foreach($item in $context.result.items)
    ##For userpools use $context.identity.username instead
    #if($item.Owner == $context.identity.cognitoIdentityId)
        #set($added = $myResults.add($item))
    #end
#end
$utils.toJson($myResults)
```

### Use case: multiple people can read

Another popular authorization option is to allow a group of people to be able to
read data. In the example below the `"filter":{"expression":...}` only
returns values from a table scan if the user running the GraphQL query is listed in
the set for `PeopleCanAccess`.

```
{
    "version" : "2017-02-28",
    "operation" : "Scan",
    "limit": #if(${context.arguments.count}) $util.toJson($context.arguments.count) #else 20 #end,
    "nextToken": #if(${context.arguments.nextToken})  $util.toJson($context.arguments.nextToken) #else null #end,
    "filter":{
        "expression": "contains(#peopleCanAccess, :value)",
        "expressionNames": {
                "#peopleCanAccess": "peopleCanAccess"
        },
        "expressionValues": {
                ":value": $util.dynamodb.toDynamoDBJson($context.identity.username)
        }
    }
}
```

### Use case: group can read

Similar to the last use case, it may be that only people in one or more groups
have rights to read certain items in a database. Use of the `"expression":
 "contains()"` operation is similar however it’s a logical-OR of all the
groups that a user might be a part of which needs to be accounted for in the set
membership. In this case we build up a `$expression` statement below for
each group the user is in and then pass this to the filter:

```
#set($expression = "")
#set($expressionValues = {})
#foreach($group in $context.identity.claims.get("cognito:groups"))
    #set( $expression = "${expression} contains(groupsCanAccess, :var$foreach.count )" )
    #set( $val = {})
    #set( $test = $val.put("S", $group))
    #set( $values = $expressionValues.put(":var$foreach.count", $val))
    #if ( $foreach.hasNext )
    #set( $expression = "${expression} OR" )
    #end
#end
{
    "version" : "2017-02-28",
    "operation" : "Scan",
    "limit": #if(${context.arguments.count}) $util.toJson($context.arguments.count) #else 20 #end,
    "nextToken": #if(${context.arguments.nextToken})  $util.toJson($context.arguments.nextToken) #else null #end,
    "filter":{
        "expression": "$expression",
        "expressionValues": $utils.toJson($expressionValues)
    }
}
```

## Writing data

Writing data on mutations is always controlled on the request mapping template. In the
case of DynamoDB data sources, the key is to use an appropriate
`"condition":{"expression"...}"` which performs validation against the
authorization metadata in that table. In [Security](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security"), we provided an example you can use to check the
`Author` field in a table. The use cases in this section explore more use
cases.

### Use case: multiple owners

Using the example table diagram from earlier, suppose the
`PeopleCanAccess` list

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    },
    "update" : {
        "expression" : "SET meta = :meta",
        "expressionValues": {
            ":meta" : $util.dynamodb.toDynamoDBJson($ctx.args.meta)
        }
    },
    "condition" : {
        "expression"       : "contains(Owner,:expectedOwner)",
        "expressionValues" : {
            ":expectedOwner" : $util.dynamodb.toDynamoDBJson($context.identity.username)
        }
    }
}
```

### Use case: group can create new record

```
#set($expression = "")
#set($expressionValues = {})
#foreach($group in $context.identity.claims.get("cognito:groups"))
    #set( $expression = "${expression} contains(groupsCanAccess, :var$foreach.count )" )
    #set( $val = {})
    #set( $test = $val.put("S", $group))
    #set( $values = $expressionValues.put(":var$foreach.count", $val))
    #if ( $foreach.hasNext )
    #set( $expression = "${expression} OR" )
    #end
#end
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key" : {
        ## If your table's hash key is not named 'id', update it here. **
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
        ## If your table has a sort key, add it as an item here. **
    },
    "attributeValues" : {
        ## Add an item for each field you would like to store to Amazon DynamoDB. **
        "title" : $util.dynamodb.toDynamoDBJson($ctx.args.title),
        "content": $util.dynamodb.toDynamoDBJson($ctx.args.content),
        "owner": $util.dynamodb.toDynamoDBJson($context.identity.username)
    },
    "condition" : {
        "expression": $util.toJson("attribute_not_exists(id) AND $expression"),
        "expressionValues": $utils.toJson($expressionValues)
    }
}
```

### Use case: group can update existing

record

```
#set($expression = "")
#set($expressionValues = {})
#foreach($group in $context.identity.claims.get("cognito:groups"))
    #set( $expression = "${expression} contains(groupsCanAccess, :var$foreach.count )" )
    #set( $val = {})
    #set( $test = $val.put("S", $group))
    #set( $values = $expressionValues.put(":var$foreach.count", $val))
    #if ( $foreach.hasNext )
    #set( $expression = "${expression} OR" )
    #end
#end
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    },
    "update":{
                "expression" : "SET title = :title, content = :content",
        "expressionValues": {
            ":title" : $util.dynamodb.toDynamoDBJson($ctx.args.title),
            ":content" : $util.dynamodb.toDynamoDBJson($ctx.args.content)
        }
    },
    "condition" : {
        "expression": $util.toJson($expression),
        "expressionValues": $utils.toJson($expressionValues)
    }
}
```

## Public and private records

With the conditional filters you can also choose to mark data as private, public or
some other Boolean check. This can then be combined as part of an authorization filter
inside the response template. Using this check is a nice way to temporarily hide data or
remove it from view without trying to control group membership.

For example suppose you added an attribute on each item in your DynamoDB table called
`public` with either a value of `yes` or `no`. The
following response template could be used on a `GetItem` call to only display
data if the user is in a group that has access AND if that data is marked as
public:

```
#set($permissions = $context.result.GroupsCanAccess)
#set($claimPermissions = $context.identity.claims.get("cognito:groups"))

#foreach($per in $permissions)
    #foreach($cgroups in $claimPermissions)
        #if($cgroups == $per)
            #set($hasPermission = true)
        #end
    #end
#end

#if($hasPermission && $context.result.public == 'yes')
    $utils.toJson($context.result)
#else
    $utils.unauthorized()
#end
```

The above code could also use a logical OR (`||`) to allow people to read
if they have permission to a record or if it’s public:

```
#if($hasPermission || $context.result.public == 'yes')
    $utils.toJson($context.result)
#else
    $utils.unauthorized()
#end
```

In general, you will find the standard operators `==`, `!=`,
`&&`, and `||` helpful when performing authorization
checks.

## Real-time data

You can apply Fine Grained Access Controls to GraphQL subscriptions at the time a
client makes a subscription, using the same techniques described earlier in this
documentation. You attach a resolver to the subscription field, at which point you can
query data from a data source and perform conditional logic in either the request or
response mapping template. You can also return additional data to the client, such as
the initial results from a subscription, as long as the data structure matches that of
the returned type in your GraphQL subscription.

### Use case: user can

subscribe to specific conversations only

A common use case for real-time data with GraphQL subscriptions is building a
messaging or private chat application. When creating a chat application that has
multiple users, conversations can occur between two people or among multiple people.
These might be grouped into “rooms”, which are private or public. As such, you would
only want to authorize a user to subscribe to a conversation (which could be one to
one or among a group) for which they have been granted access. For demonstration
purposes, the sample below shows a simple use case of one user sending a private
message to another. The setup has two Amazon DynamoDB tables:

- Messages table: (primary key) `toUser`, (sort key)
  `id`
- Permissions table: (primary key) `username`

The Messages table stores the actual messages that get sent via a GraphQL
mutation. The Permissions table is checked by the GraphQL subscription for
authorization at client connection time. The example below assumes you are using the
following GraphQL schema:

```
input CreateUserPermissionsInput {
    user: String!
    isAuthorizedForSubscriptions: Boolean
}

type Message {
    id: ID
    toUser: String
    fromUser: String
    content: String
}

type MessageConnection {
    items: [Message]
    nextToken: String
}

type Mutation {
    sendMessage(toUser: String!, content: String!): Message
    createUserPermissions(input: CreateUserPermissionsInput!): UserPermissions
    updateUserPermissions(input: UpdateUserPermissionInput!): UserPermissions
}

type Query {
    getMyMessages(first: Int, after: String): MessageConnection
    getUserPermissions(user: String!): UserPermissions
}

type Subscription {
    newMessage(toUser: String!): Message
        @aws_subscribe(mutations: ["sendMessage"])
}

input UpdateUserPermissionInput {
    user: String!
    isAuthorizedForSubscriptions: Boolean
}

type UserPermissions {
    user: String
    isAuthorizedForSubscriptions: Boolean
}

schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
}
```

Some of the standard operations, such as `createUserPermissions()`, are
not covered below to illustrate the subscription resolvers, but are standard
implementations of DynamoDB resolvers. Instead, we’ll focus on subscription
authorization flows with resolvers. To send a message from one user to another,
attach a resolver to the `sendMessage()` field and select the **Messages** table data source with the following request
template:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key" : {
        "toUser" : $util.dynamodb.toDynamoDBJson($ctx.args.toUser),
        "id" : $util.dynamodb.toDynamoDBJson($util.autoId())
    },
    "attributeValues" : {
        "fromUser" : $util.dynamodb.toDynamoDBJson($context.identity.username),
        "content" : $util.dynamodb.toDynamoDBJson($ctx.args.content),
    }
}
```

In this example, we use `$context.identity.username`. This returns user
information for AWS Identity and Access Management or Amazon Cognito users. The response template is a simple
passthrough of `$util.toJson($ctx.result)`. Save and go back to the
schema page. Then attach a resolver for the `newMessage()` subscription,
using the **Permissions** table as a data source and
the following request mapping template:

```
{
    "version": "2018-05-29",
    "operation": "GetItem",
    "key": {
        "username": $util.dynamodb.toDynamoDBJson($ctx.identity.username),
    },
}
```

Then use the following response mapping template to perform your authorization
checks using data from the **Permissions**
table:

```
#if(! ${context.result})
    $utils.unauthorized()
#elseif(${context.identity.username} != ${context.arguments.toUser})
    $utils.unauthorized()
#elseif(! ${context.result.isAuthorizedForSubscriptions})
    $utils.unauthorized()
#else
##User is authorized, but we return null to continue
    null
#end
```

In this case, you’re doing three authorization checks. The first ensures that a
result is returned. The second ensures that the user isn’t subscribing to messages
that are meant for another person. The third ensures that the user is allowed to
subscribe to any fields, by checking a DynamoDB attribute of
`isAuthorizedForSubscriptions` stored as a `BOOL`.

To test things out, you could sign in to the AWS AppSync console using Amazon Cognito user
pools and a user named “Nadia”, and then run the following GraphQL
subscription:

```
subscription AuthorizedSubscription {
    newMessage(toUser: "Nadia") {
        id
        toUser
        fromUser
        content
    }
}
```

If in the **Permissions** table there is a record for
the `username` key attribute of `Nadia` with
`isAuthorizedForSubscriptions` set to `true`, you’ll see a
successful response. If you try a different `username` in the
`newMessage()` query above, an error will be returned.
