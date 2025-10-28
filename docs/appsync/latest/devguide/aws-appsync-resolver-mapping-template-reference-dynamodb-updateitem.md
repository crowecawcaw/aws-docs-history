# UpdateItem

The `UpdateItem` request mapping document enables you to tell the
AWS AppSync DynamoDB resolver to make a `UpdateItem` request to DynamoDB and allows you to
specify the following:

- The key of the item in DynamoDB
- An update expression describing how to update the item in DynamoDB
- Conditions for the operation to succeed
  The `UpdateItem` mapping document has the following structure:

```
{
    "version" : "2018-05-29",
    "operation" : "UpdateItem",
    "customPartitionKey" : "foo",
    "populateIndexFields" : boolean value,
    "key": {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "update" : {
        "expression" : "someExpression",
        "expressionNames" : {
           "#foo" : "foo"
       },
       "expressionValues" : {
           ":bar" : ... typed value
       }
    },
    "condition" : {
        ...
    },
    "_version" : 1
}
```

The fields are defined as follows:

## UpdateItem fields

**`version`**

The template definition version. `2017-02-28` and
`2018-05-29` are currently supported. This value is
required.

**`operation`**

The DynamoDB operation to perform. To perform the `UpdateItem`
DynamoDB operation, this must be set to `UpdateItem`. This
value is required.

**`key`**

The key of the item in DynamoDB. DynamoDB items may have a single hash key,
or a hash key and sort key, depending on the table structure. For more
information about specifying a “typed value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This value is required.

**`update`**

The `update` section lets you specify an update expression
that describes how to update the item in DynamoDB. For more information
about how to write update expressions, see the [DynamoDB UpdateExpressions documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md"). This section is
required.

The `update` section has three components:

**`expression`**

The update expression. This value is required.

**`expressionNames`**

The substitutions for expression attribute
_name_ placeholders, in the form of
key-value pairs. The key corresponds to a name placeholder used
in the `expression`, and the value must be a string
corresponding to the attribute name of the item in DynamoDB. This
field is optional, and should only be populated with
substitutions for expression attribute name placeholders used in
the `expression`.

**`expressionValues`**

The substitutions for expression attribute
_value_ placeholders, in the form of
key-value pairs. The key corresponds to a value placeholder used
in the `expression`, and the value must be a typed
value. For more information about how to specify a “typed
value”, see [Type system (request mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.md"). This must be
specified. This field is optional, and should only be populated
with substitutions for expression attribute value placeholders
used in the `expression`.

**`condition`**

A condition to determine if the request should succeed or not, based
on the state of the object already in DynamoDB. If no condition is
specified, the `UpdateItem` request updates the existing entry
regardless of its current state. For more information about conditions,
see [Condition expressions](aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md "aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.md"). This value is optional.

**`_version`**

A numeric value that represents the latest known version of an item.
This value is optional. This field is used for _Conflict Detection_ and is only
supported on versioned data sources.

**`customPartitionKey`**

When enabled, this string value modifies the format of the
`ds_sk` and `ds_pk` records used by the delta
sync table when versioning has been enabled (for more information, see
[Conflict detection and sync](conflict-detection-and-sync.md "conflict-detection-and-sync.md") in the
_AWS AppSync Developer Guide_). When enabled, the processing of
the `populateIndexFields` entry is also enabled. This field is
optional.

**`populateIndexFields`**

A boolean value that, when enabled **along with
the `customPartitionKey`**, creates new entries
for each record in the delta sync table, specifically in the
`gsi_ds_pk` and `gsi_ds_sk` columns. For more
information, see [Conflict detection and sync](conflict-detection-and-sync.md "conflict-detection-and-sync.md") in the
_AWS AppSync Developer Guide_. This field is optional.

The item updated in DynamoDB is automatically converted into GraphQL and JSON primitive
types and is available in the mapping context (`$context.result`).

For more information about DynamoDB type conversion, see [Type system (response mapping)](aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md "aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.md").

For more information about response mapping templates, see [Resolver mapping
template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview").

## Example 1

The following example is a mapping template for the GraphQL mutation `upvote(id:
 ID!)`.

In this example, an item in DynamoDB has its `upvotes` and
`version` fields incremented by 1.

```
{
    "version" : "2017-02-28",
    "operation" : "UpdateItem",
    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    },
    "update" : {
        "expression" : "ADD #votefield :plusOne, version :plusOne",
        "expressionNames" : {
            "#votefield" : "upvotes"
        },
        "expressionValues" : {
            ":plusOne" : { "N" : 1 }
        }
    }
}
```

## Example 2

The following example is a mapping template for a GraphQL mutation
`updateItem(id: ID!, title: String, author: String, expectedVersion:
 Int!)`.

This is a complex example that inspects the arguments and dynamically generates the
update expression that only includes the arguments that have been provided by the
client. For example, if `title` and `author` are omitted, they are
not updated. If an argument is specified but its value is `null`, then that
field is deleted from the object in DynamoDB. Finally, the operation has a condition, which
verifies whether the item currently in DynamoDB has the `version` field set to
`expectedVersion`:

```
{
    "version" : "2017-02-28",

    "operation" : "UpdateItem",

    "key" : {
        "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    },

    ## Set up some space to keep track of things we're updating **
    #set( $expNames  = {} )
    #set( $expValues = {} )
    #set( $expSet = {} )
    #set( $expAdd = {} )
    #set( $expRemove = [] )

    ## Increment "version" by 1 **
    $!{expAdd.put("version", ":newVersion")}
    $!{expValues.put(":newVersion", { "N" : 1 })}

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

                #if( $entry.key == "ups" || $entry.key == "downs" )
                    $!{expValues.put(":${entry.key}", { "N" : $entry.value })}
                #else
                    $!{expValues.put(":${entry.key}", { "S" : "${entry.value}" })}
                #end
            #end
        #end
    #end

    ## Start building the update expression, starting with attributes we're going to SET **
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

    ## Continue building the update expression, adding attributes we're going to ADD **
    #if( !${expAdd.isEmpty()} )
        #set( $expression = "${expression} ADD" )
        #foreach( $entry in $expAdd.entrySet() )
            #set( $expression = "${expression} ${entry.key} ${entry.value}" )
            #if ( $foreach.hasNext )
                #set( $expression = "${expression}," )
            #end
        #end
    #end

    ## Continue building the update expression, adding attributes we're going to REMOVE **
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
            ":expectedVersion" : $util.dynamodb.toDynamoDBJson($ctx.args.expectedVersion)
        }
    }
}
```

For more information about the DynamoDB `UpdateItem` API, see the [DynamoDB
API documentation](../../../amazondynamodb/latest/APIReference/API_UpdateItem.md "../../../amazondynamodb/latest/APIReference/API_UpdateItem.md").
