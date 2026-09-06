

# Creating basic queries (VTL)
<a name="configuring-resolvers"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers-js.html).

GraphQL resolvers connect the fields in a type’s schema to a data source. Resolvers are the mechanism by which requests are fulfilled. AWS AppSync can automatically create and connect resolvers from a schema or create a schema and connect resolvers from an existing table without you needing to write any code.

Resolvers in AWS AppSync use JavaScript to convert a GraphQL expression into a format the data source can use. Alternatively, mapping templates can be written in [Apache Velocity Template Language (VTL)](https://velocity.apache.org/engine/2.0/vtl-reference.html) to convert a GraphQL expression into a format the data source can use.

This section will show you how to configure resolvers using VTL. An introductory tutorial-style programming guide for writing resolvers can be found in [Resolver mapping template programming guide](resolver-mapping-template-reference-programming-guide.md#aws-appsync-resolver-mapping-template-reference-programming-guide), and helper utilities available to use when programming can be found in [Resolver mapping template context reference](resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference). AWS AppSync also has built-in test and debug flows that you can use when you’re editing or authoring from scratch. For more information, see [Test and debug resolvers](test-debug-resolvers.md#aws-appsync-test-debug-resolvers).

We recommend following this guide before attempting to to use any of the aforementioned tutorials.

In this section, we will walk through how to create a resolver, add a resolver for mutations, and use advanced configurations.

## Create your first resolver
<a name="create-your-first-resolver"></a>

Following the examples from the previous sections, the first step is to create a resolver for your `Query` type.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

   1. In the **APIs dashboard**, choose your GraphQL API.

   1. In the **Sidebar**, choose **Schema**.

1. On the right-hand side of the page, there's a window called **Resolvers**. This box contains a list of the types and fields as defined in your **Schema** window on the left-hand side of the page. You're able to attach resolvers to fields. For example, under the **Query** type, choose **Attach** next to the `getTodos` field.

1. On the **Create Resolver** page, choose the data source you created in the [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) guide. In the **Configure mapping templates** window, you can choose both the generic request and response mapping templates using the drop-down list to the right or write your own.
**Note**  
The pairing of a request mapping template to a response mapping template is called a unit resolver. Unit resolvers are typically meant to perform rote operations; we recommend using them only for singular operations with a small number of data sources. For more complex operations, we recommend using pipeline resolvers, which can execute multiple operations with multiple data sources sequentially.  
For more information about the difference between request and response mapping templates, see [Unit resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-overview.html#unit-resolvers).  
For more information about using pipeline resolvers, see [Pipeline resolvers](pipeline-resolvers.md#aws-appsync-pipeline-resolvers).

1. For common use cases, the AWS AppSync console has built-in templates that you can use for getting items from data sources (e.g., all item queries, individual lookups, etc.). For example, on the simple version of the schema from [Designing your schema](designing-your-schema.md#aws-appsync-designing-your-schema) where `getTodos` didn’t have pagination, the request mapping template for listing items is as follows:

   ```
   {
       "version" : "2017-02-28",
       "operation" : "Scan"
   }
   ```

1. You always need a response mapping template to accompany the request. The console provides a default with the following passthrough value for lists:

   ```
   $util.toJson($ctx.result.items)
   ```

   In this example, the `context` object (aliased as `$ctx`) for lists of items has the form `$context.result.items`. If your GraphQL operation returns a single item, it would be `$context.result`. AWS AppSync provides helper functions for common operations, such as the `$util.toJson` function listed previously, to format responses properly. For a full list of functions, see [Resolver mapping template utility reference](resolver-util-reference.md#aws-appsync-resolver-mapping-template-util-reference).

1. Choose **Save Resolver**.

------
#### [ API ]

1. Create a resolver object by calling the [`CreateResolver`](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateResolver.html) API.

1. You can modify your resolver's fields by calling the [`UpdateResolver`](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateResolver.html) API.

------
#### [ CLI ]

1. Create a resolver by running the [`create-resolver`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html) command.

   You'll need to type in 6 parameters for this particular command:

   1. The `api-id` of your API.

   1. The `type-name` of the type that you want to modify in your schema. In the console example, this was `Query`.

   1. The `field-name` of the field that you want to modify in your type. In the console example, this was `getTodos`.

   1. The `data-source-name` of the data source you created in the [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) guide.

   1. The `request-mapping-template`, which is the body of the request. In the console example, this was:

      ```
      {
          "version" : "2017-02-28",
          "operation" : "Scan"
      }
      ```

   1. The `response-mapping-template`, which is the body of the response. In the console example, this was:

      ```
      $util.toJson($ctx.result.items)
      ```

   An example command may look like this:

   ```
   aws appsync create-resolver --api-id abcdefghijklmnopqrstuvwxyz --type-name Query --field-name getTodos --data-source-name TodoTable --request-mapping-template "{ "version" : "2017-02-28", "operation" : "Scan", }" --response-mapping-template ""$"util.toJson("$"ctx.result.items)"
   ```

   An output will be returned in the CLI. Here's an example:

   ```
   {
       "resolver": {
           "kind": "UNIT",
           "dataSourceName": "TodoTable",
           "requestMappingTemplate": "{ version : 2017-02-28, operation : Scan, }",
           "resolverArn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/Query/resolvers/getTodos",
           "typeName": "Query",
           "fieldName": "getTodos",
           "responseMappingTemplate": "$util.toJson($ctx.result.items)"
       }
   }
   ```

1. To modify a resolver's fields and/or mapping templates, run the [`update-resolver`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-resolver.html) command.

   With the exception of the `api-id` parameter, the parameters used in the `create-resolver` command will be overwritten by the new values from the `update-resolver` command.

------

## Adding a resolver for mutations
<a name="adding-a-resolver-for-mutations"></a>

The next step is to create a resolver for your `Mutation` type.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

   1. In the **APIs dashboard**, choose your GraphQL API.

   1. In the **Sidebar**, choose **Schema**.

1. Under the **Mutation** type, choose **Attach** next to the `addTodo` field.

1. On the **Create Resolver** page, choose the data source you created in the [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) guide.

1. In the **Configure mapping templates** window, you'll need to modify the request template because this is a mutation where you’re adding a new item to DynamoDB. Use the following request mapping template:

   ```
   {
       "version" : "2017-02-28",
       "operation" : "PutItem",
       "key" : {
           "id" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
       },
       "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args)
   }
   ```

1. AWS AppSync automatically converts arguments defined in the `addTodo` field from your GraphQL schema into DynamoDB operations. The previous example stores records in DynamoDB using a key of `id`, which is passed through from the mutation argument as `$ctx.args.id`. All of the other fields you pass through are automatically mapped to DynamoDB attributes with `$util.dynamodb.toMapValuesJson($ctx.args)`.

   For this resolver, use the following response mapping template:

   ```
   $util.toJson($ctx.result)
   ```

   AWS AppSync also supports test and debug workflows for editing resolvers. You can use a mock `context` object to see the transformed value of the template before invoking. Optionally, you can view the full request execution to a data source interactively when you run a query. For more information, see [Test and debug resolvers](test-debug-resolvers.md#aws-appsync-test-debug-resolvers) and [Monitoring and logging](monitoring.md#aws-appsync-monitoring).

1. Choose **Save Resolver**.

------
#### [ API ]

You can also do this with APIs by utilizing the commands in the [Create your first resolver](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html#create-your-first-resolver) section and the parameter details from this section.

------
#### [ CLI ]

You can also do this in the CLI by utilizing the commands in the [Create your first resolver](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html#create-your-first-resolver) section and the parameter details from this section.

------

At this point, if you’re not using the advanced resolvers you can begin using your GraphQL API as outlined in [Using your API](using-your-api.md#aws-appsync-using-your-api).

## Advanced resolvers
<a name="advanced-resolvers"></a>

If you are following the Advanced section and you’re building a sample schema in [Designing your schema](designing-your-schema.md#aws-appsync-designing-your-schema) to do a paginated scan, use the following request template for the `getTodos` field instead:

```
{
    "version" : "2017-02-28",
    "operation" : "Scan",
    "limit": $util.defaultIfNull(${ctx.args.limit}, 20),
    "nextToken": $util.toJson($util.defaultIfNullOrBlank($ctx.args.nextToken, null))
}
```

For this pagination use case, the response mapping is more than just a passthrough because it must contain both the *cursor* (so that the client knows what page to start at next) and the result set. The mapping template is as follows:

```
{
    "todos": $util.toJson($context.result.items),
    "nextToken": $util.toJson($context.result.nextToken)
}
```

The fields in the preceding response mapping template should match the fields defined in your `TodoConnection` type.

For the case of relations where you have a `Comments` table and you’re resolving the comments field on the `Todo` type (which returns a type of `[Comment]`), you can use a mapping template that runs a query against the second table. To do this, you must have already created a data source for the `Comments` table as outlined in [Attaching a data source](attaching-a-data-source.md#aws-appsync-getting-started-build-a-schema-from-scratch).

**Note**  
We’re using a query operation against a second table for illustrative purposes only. You could use another operation against DynamoDB instead. In addition, you could pull the data from another data source, such as AWS Lambda or Amazon OpenSearch Service, because the relation is controlled by your GraphQL schema.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

   1. In the **APIs dashboard**, choose your GraphQL API.

   1. In the **Sidebar**, choose **Schema**.

1. Under the **Todo** type, choose **Attach** next to the `comments` field.

1. On the **Create Resolver** page, choose your **Comments** table data source. The default name for the **Comments** table from the quickstart guides is `AppSyncCommentTable`, but it may vary depending on what name you gave it.

1. Add the following snippet to your request mapping template:

   ```
   {
       "version": "2017-02-28",
       "operation": "Query",
       "index": "todoid-index",
       "query": {
           "expression": "todoid = :todoid",
           "expressionValues": {
               ":todoid": {
                   "S": $util.toJson($context.source.id)
               }
           }
       }
   }
   ```

1. The `context.source` references the parent object of the current field that’s being resolved. In this example, `source.id` refers to the individual `Todo` object, which is then used for the query expression.

   You can use the passthrough response mapping template as follows:

   ```
   $util.toJson($ctx.result.items)
   ```

1. Choose **Save Resolver**.

1. Finally, back on the **Schema** page in the console, attach a resolver to the `addComment` field, and specify the data source for the `Comments` table. The request mapping template in this case is a simple `PutItem` with the specific `todoid` that is commented on as an argument, but you use the `$utils.autoId()` utility to create a unique sort key for the comment as follows:

   ```
   {
       "version": "2017-02-28",
       "operation": "PutItem",
       "key": {
           "todoid": { "S": $util.toJson($context.arguments.todoid) },
           "commentid": { "S": "$util.autoId()" }
       },
       "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args)
   }
   ```

   Use a passthrough response template as follows:

   ```
   $util.toJson($ctx.result)
   ```

------
#### [ API ]

You can also do this with APIs by utilizing the commands in the [Create your first resolver](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html#create-your-first-resolver) section and the parameter details from this section.

------
#### [ CLI ]

You can also do this in the CLI by utilizing the commands in the [Create your first resolver](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html#create-your-first-resolver) section and the parameter details from this section.

------