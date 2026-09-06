

# Creating basic queries (JavaScript)
<a name="configuring-resolvers-js"></a>

GraphQL resolvers connect the fields in a type’s schema to a data source. Resolvers are the mechanism by which requests are fulfilled.

Resolvers in AWS AppSync use JavaScript to convert a GraphQL expression into a format the data source can use. Alternatively, mapping templates can be written in [Apache Velocity Template Language (VTL)](https://velocity.apache.org/engine/2.0/vtl-reference.html) to convert a GraphQL expression into a format the data source can use.

This section describes how to configure resolvers using JavaScript. The [Resolver tutorials (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials-js.html) section provides in-depth tutorials on how to implement resolvers using JavaScript. The [Resolver reference (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html) section provides an explanation of utility operations that can be used with JavaScript resolvers.

We recommend following this guide before attempting to use any of the aforementioned tutorials.

In this section, we will walk through how to create and configure resolvers for queries and mutations.

**Note**  
This guide assumes you have created your schema and have at least one query or mutation. If you're looking for subscriptions (real-time data), then see [this](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-data.html) guide.

In this section, we'll provide some general steps for configuring resolvers along with an example that uses the schema below:

```
// schema.graphql file

input CreatePostInput {
  title: String
  date: AWSDateTime
}

type Post {
  id: ID!
  title: String
  date: AWSDateTime
}

type Mutation {
  createPost(input: CreatePostInput!): Post
}

type Query {
  getPost: [Post]
}
```

## Creating basic query resolvers
<a name="create-basic-query-resolver-js"></a>

This section will show you how to make a basic query resolver.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

   1. In the **APIs dashboard**, choose your GraphQL API.

   1. In the **Sidebar**, choose **Schema**.

1. Enter the details of your schema and data source. See the [Designing your schema](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html) and [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) sections for more information.

1. Next to the **Schema** editor, There's a window called **Resolvers**. This box contains a list of the types and fields as defined in your **Schema** window. You can attach resolvers to fields. You will most likely be attaching resolvers to your field operations. In this section, we'll look at simple query configurations. Under the **Query** type, choose **Attach** next to your query's field.

1. On the **Attach resolver** page, under **Resolver type**, you can choose between pipeline or unit resolvers. For more information about these types, see [Resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-components.html). This guide will make use of `pipeline resolvers`.
**Tip**  
When creating pipeline resolvers, your data source(s) will be attached to the pipeline function(s). Functions are created after you create the pipeline resolver itself, which is why there's no option to set it in this page. If you're using a unit resolver, the data source is tied directly to the resolver, so you would set it in this page.

   For **Resolver runtime**, choose `APPSYNC_JS` to enable the JavaScript runtime.

1. You can enable [caching](https://docs.aws.amazon.com/appsync/latest/devguide/enabling-caching.html) for this API. We recommend turning this feature off for now. Choose **Create**.

1. On the **Edit resolver** page, there's a code editor called **Resolver code** that allows you to implement the logic for the resolver handler and response (before and after steps). For more information, see the [JavaScript resolvers overview](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-overview-js.html). 
**Note**  
In our example, we're just going to leave the request blank and the response set to return the last data source result from the [context](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference-js.html):  

   ```
   import {util} from '@aws-appsync/utils';
   
   export function request(ctx) {
       return {};
   }
   
   export function response(ctx) {
       return ctx.prev.result;
   }
   ```

   Below this section, there's a table called **Functions**. Functions allow you to implement code that can be reused across multiple resolvers. Instead of constantly rewriting or copying code, you can store the source code as a function to be added to a resolver whenever you need it. 

   Functions make up the bulk of a pipeline's operation list. When using multiple functions in a resolver, you set the order of the functions, and they will be run in that order sequentially. They are executed after the request function runs and before the response function begins.

   To add a new function, under **Functions**, choose **Add function**, then **Create new function**. Alternatively, you may see a **Create function** button to choose instead.

   1. Choose a data source. This will be the data source on which the resolver acts.
**Note**  
In our example, we're attaching a resolver for `getPost`, which retrieves a `Post` object by `id`. Let's assume we already set up a DynamoDB table for this schema. Its partition key is set to the `id` and is empty.

   1. Enter a `Function name`.

   1. Under **Function code**, you'll need to implement the function's behavior. This might be confusing, but each function will have its own local request and response handler. The request runs, then the data source invocation is made to handle the request, then the data source response is processed by the response handler. The result is stored in the [context](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference-js.html) object. Afterward, the next function in the list will run or will be passed to the after step response handler if it's the last one. 
**Note**  
In our example, we're attaching a resolver to `getPost`, which gets a list of `Post` objects from the data source. Our request function will request the data from our table, the table will pass its response to the context (ctx), then the response will return the result in the context. AWS AppSync's strength lies in its interconnectedness with other AWS services. Because we're using DynamoDB, we have a [suite of operations](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html) to simplify things like this. We have some boilerplate examples for other data source types as well.  
Our code will look like this:  

      ```
      import { util } from '@aws-appsync/utils';
      
      /**
       * Performs a scan on the dynamodb data source
       */
      export function request(ctx) {
        return { operation: 'Scan' };
      }
      
      /**
       * return a list of scanned post items
       */
      export function response(ctx) {
        return ctx.result.items;
      }
      ```
In this step, we added two functions:  
`request`: The request handler performs the retrieval operation against the data source. The argument contains the context object (`ctx`), or some data that is available to all resolvers performing a particular operation. For example, it might contain authorization data, the field names being resolved, etc. The return statement performs a [`Scan`](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html#js-aws-appsync-resolver-reference-dynamodb-scan) operation (see [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html) for examples). Because we're working with DynamoDB, we're allowed to use some of the operations from that service. The scan performs a basic fetch of all items in our table. The result of this operation is stored in the context object as a `result` container before being passed to the response handler. The `request` is run before the response in the pipeline.
`response`: The response handler that returns the output of the `request`. The argument is the updated context object, and the return statement is `ctx.prev.result`. At this point in the guide, you may not be familiar with this value. `ctx` refers to the context object. `prev` refers to the previous operation in the pipeline, which was our `request`. The `result` contains the result(s) of the resolver as it moves through the pipeline. If you put it all together, `ctx.prev.result` is returning the result of the last operation performed, which was the request handler.

   1. Choose **Create** after you're done.

1. Back on the resolver screen, under **Functions**, choose the **Add function** drop-down and add your function to your functions list.

1. Choose **Save** to update the resolver.

------
#### [ CLI ]

**To add your function**
+ Create a function for your pipeline resolver using the `[create-function](https://docs.aws.amazon.com/cli/latest/reference/appsync/create-function.html)` command.

  You'll need to enter a few parameters for this particular command:

  1. The `api-id` of your API.

  1. The `name` of the function in the AWS AppSync console.

  1. The `data-source-name`, or the name of the data source the function will use. It must already be created and linked to your GraphQL API in the AWS AppSync service.

  1. The `runtime`, or environment and language of the function. For JavaScript, the name must be `APPSYNC_JS`, and the runtime, `1.0.0`.

  1. The `code`, or request and response handlers of your function. While you can type it in manually, it's far easier to add it to a .txt file (or a similar format) and then pass it in as the argument. 
**Note**  
Our query code will be in a file passed in as the argument:  

     ```
     import { util } from '@aws-appsync/utils';
     
     /**
      * Performs a scan on the dynamodb data source
      */
     export function request(ctx) {
       return { operation: 'Scan' };
     }
     
     /**
      * return a list of scanned post items
      */
     export function response(ctx) {
       return ctx.result.items;
     }
     ```

  An example command may look like this:

  ```
  aws appsync create-function \
  --api-id abcdefghijklmnopqrstuvwxyz \
  --name get_posts_func_1 \
  --data-source-name table-for-posts \
  --runtime name=APPSYNC_JS,runtimeVersion=1.0.0 \
  --code file://~/path/to/file/{filename}.{fileType}
  ```

  An output will be returned in the CLI. Here's an example:

  ```
  {
      "functionConfiguration": {
          "functionId": "ejglgvmcabdn7lx75ref4qeig4",
          "functionArn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/functions/ejglgvmcabdn7lx75ref4qeig4",
          "name": "get_posts_func_1",
          "dataSourceName": "table-for-posts",
          "maxBatchSize": 0,
          "runtime": {
              "name": "APPSYNC_JS",
              "runtimeVersion": "1.0.0"
          },
          "code": "{{Code output goes here}}"
      }
  }
  ```
**Note**  
Make sure you record the `functionId` somewhere as this will be used to attach the function to the resolver.

**To create your resolver**
+ Create a pipeline function for `Query` by running the `[create-resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html)` command.

  You'll need to enter a few parameters for this particular command:

  1. The `api-id` of your API.

  1. The `type-name`, or the special object type in your schema (Query, Mutation, Subscription).

  1. The `field-name`, or the field operation inside the special object type you want to attach the resolver to.

  1. The `kind`, which specifies a unit or pipeline resolver. Set this to `PIPELINE` to enable pipeline functions.

  1. The `pipeline-config`, or the function(s) to attach to the resolver. Make sure you know the `functionId` values of your functions. Order of listing matters.

  1. The `runtime`, which was `APPSYNC_JS` (JavaScript). The `runtimeVersion` currently is `1.0.0`.

  1. The `code`, which contains the before and after step handlers.
**Note**  
Our query code will be in a file passed in as the argument:  

     ```
     import { util } from '@aws-appsync/utils';
     
     /**
      * Sends a request to `put` an item in the DynamoDB data source
      */
     export function request(ctx) {
       const { id, ...values } = ctx.args;
       return {
         operation: 'PutItem',
         key: util.dynamodb.toMapValues({ id }),
         attributeValues: util.dynamodb.toMapValues(values),
       };
     }
     
     /**
      * returns the result of the `put` operation
      */
     export function response(ctx) {
       return ctx.result;
     }
     ```

  An example command may look like this:

  ```
  aws appsync create-resolver \
  --api-id abcdefghijklmnopqrstuvwxyz \
  --type-name Query \
  --field-name getPost \
  --kind PIPELINE \
  --pipeline-config functions=ejglgvmcabdn7lx75ref4qeig4 \
  --runtime name=APPSYNC_JS,runtimeVersion=1.0.0 \
  --code file:///path/to/file/{filename}.{fileType}
  ```

  An output will be returned in the CLI. Here's an example:

  ```
  {
      "resolver": {
          "typeName": "Mutation",
          "fieldName": "getPost",
          "resolverArn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/Mutation/resolvers/getPost",
          "kind": "PIPELINE",
          "pipelineConfig": {
              "functions": [
                  "ejglgvmcabdn7lx75ref4qeig4"
              ]
          },
          "maxBatchSize": 0,
          "runtime": {
              "name": "APPSYNC_JS",
              "runtimeVersion": "1.0.0"
          },
          "code": "{{Code output goes here}}"
      }
  }
  ```

------
#### [ CDK ]

**Tip**  
Before you use the CDK, we recommend reviewing the CDK's [official documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html) along with AWS AppSync's [CDK reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync-readme.html).  
The steps listed below will only show a general example of the snippet used to add a particular resource. This is **not** meant to be a working solution in your production code. We also assume you already have a working app.

A basic app will need the following things:

1. Service import directives

1. Schema code

1. Data source generator

1. Function code

1. Resolver code

From the [Designing your schema](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html) and [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) sections, we know that the stack file will include the import directives of the form:

```
import * as {{x}} from '{{x}}'; # import wildcard as the 'x' keyword from 'x-service'
import {{{a}}, {{b}}, ...} from '{{c}}'; # import {specific constructs} from 'c-service'
```

**Note**  
In previous sections, we only stated how to import AWS AppSync constructs. In real code, you'll have to import more services just to run the app. In our example, if we were to create a very simple CDK app, we would at least import the AWS AppSync service along with our data source, which was a DynamoDB table. We would also need to import some additional constructs to deploy the app:  

```
import * as cdk from 'aws-cdk-lib';
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';
```
To summarize each of these:  
`import * as cdk from 'aws-cdk-lib';`: This allows you to define your CDK app and constructs such as the stack. It also contains some useful utility functions for our application like manipulating metadata. If you're familiar with this import directive, but are wondering why the cdk core library is not being used here, see the [Migration](https://docs.aws.amazon.com/cdk/v2/guide/migrating-v2.html) page.
`import * as appsync from 'aws-cdk-lib/aws-appsync';`: This imports the [AWS AppSync service](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync-readme.html).
`import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';`: This imports the [DynamoDB service](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_dynamodb-readme.html).
`import { Construct } from 'constructs';`: We need this to define the root [construct](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html).

The type of import depends on the services you're calling. We recommend looking at the CDK documentation for examples. The schema at the top of the page will be a separate file in your CDK app as a `.graphql` file. In the stack file, we can associate it with a new GraphQL using the form:

```
const add_api = new appsync.GraphqlApi(this, 'graphQL-example', {
  name: 'my-first-api',
  schema: appsync.SchemaFile.fromAsset(path.join(__dirname, 'schema.graphql')),
});
```

**Note**  
In the scope `add_api`, we're adding a new GraphQL API using the `new` keyword followed by `appsync.GraphqlApi(scope: Construct, id: string , props: GraphqlApiProps)`. Our scope is `this`, the CFN id is `graphQL-example`, and our props are `my-first-api` (name of the API in the console) and `schema.graphql` (the absolute path to the schema file).

To add a data source, you'll first have to add your data source to the stack. Then, you need to associate it with the GraphQL API using the source-specific method. The association will happen when you make your resolver function. In the meantime, let's use an example by creating the DynamoDB table using `dynamodb.Table`:

```
const add_ddb_table = new dynamodb.Table(this, 'posts-table', {
  partitionKey: {
    name: 'id',
    type: dynamodb.AttributeType.STRING,
  },
});
```

**Note**  
If we were to use this in our example, we'd be adding a new DynamoDB table with the CFN id of `posts-table` and a partition key of `id (S)`.

Next, we need to implement our resolver in the stack file. Here's an example of a simple query that scans for all items in a DynamoDB table:

```
const add_func = new appsync.AppsyncFunction(this, 'func-get-posts', {
  name: 'get_posts_func_1',
  add_api,
  dataSource: add_api.addDynamoDbDataSource('table-for-posts', add_ddb_table),
  code: appsync.Code.fromInline(`
      export function request(ctx) {
        return { operation: 'Scan' };
      }

      export function response(ctx) {
        return ctx.result.items;
      }
  `),
  runtime: appsync.FunctionRuntime.JS_1_0_0,
});

new appsync.Resolver(this, 'pipeline-resolver-get-posts', {
  add_api,
  typeName: 'Query',
  fieldName: 'getPost',
  code: appsync.Code.fromInline(`
      export function request(ctx) {
        return {};
      }

      export function response(ctx) {
        return ctx.prev.result;
      }
 `),
  runtime: appsync.FunctionRuntime.JS_1_0_0,
  pipelineConfig: [add_func],
});
```

**Note**  
First, we created a function called `add_func`. This order of creation may seem a bit counterintuitive, but you have to create the functions in your pipeline resolver before you make the resolver itself. A function follows the form:  

```
AppsyncFunction(scope: Construct, id: string, props: AppsyncFunctionProps)
```
Our scope was `this`, our CFN id was `func-get-posts`, and our props contained the actual function details. Inside props, we included:  
The `name` of the function that will be present in the AWS AppSync console (`get_posts_func_1`).
The GraphQL API we created earlier (`add_api`).
The data source; this is the point where we link the data source to the GraphQL API value, then attach it to the function. We take the table we created (`add_ddb_table`) and attach it to the GraphQL API (`add_api`) using one of the `GraphqlApi` methods ([`addDynamoDbDataSource`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.GraphqlApi.html#addwbrdynamowbrdbwbrdatawbrsourceid-table-options)). The id value (`table-for-posts`) is the name of the data source in the AWS AppSync console. For a list of source-specific methods, see the following pages:  
[ DynamoDbDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.DynamoDbDataSource.html) 
 [ EventBridgeDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.EventBridgeDataSource.html) 
 [ HttpDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.HttpDataSource.html) 
 [ LambdaDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.LambdaDataSource.html) 
 [ NoneDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.NoneDataSource.html) 
 [ OpenSearchDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.OpenSearchDataSource.html) 
 [ RdsDataSource ](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.RdsDataSource.html) 
The code contains our function's request and response handlers, which is a simple scan and return.
The runtime specifies that we want to use the APPSYNC\_JS runtime version 1.0.0. Note that this is currently the only version available for APPSYNC\_JS.
Next, we need to attach the function to the pipeline resolver. We created our resolver using the form:  

```
Resolver(scope: Construct, id: string, props: ResolverProps)
```
Our scope was `this`, our CFN id was `pipeline-resolver-get-posts`, and our props contained the actual function details. Inside the props, we included:  
The GraphQL API we created earlier (`add_api`).
The special object type name; this is a query operation, so we simply added the value `Query`.
The field name (`getPost`) is the name of the field in the schema under the `Query` type.
The code contains your before and after handlers. Our example just returns whatever results were in the context after the function performed its operation.
The runtime specifies that we want to use the APPSYNC\_JS runtime version 1.0.0. Note that this is currently the only version available for APPSYNC\_JS.
The pipeline config contains the reference to the function we created (`add_func`).

------

To summarize what happened in this example, you saw an AWS AppSync function that implemented a request and response handler. The function was responsible for interacting with your data source. The request handler sent a `Scan` operation to AWS AppSync, instructing it on what operation to perform against your DynamoDB data source. The response handler returned the list of items (`ctx.result.items`). The list of items was then mapped to the `Post` GraphQL type automatically. 

## Creating basic mutation resolvers
<a name="creating-basic-mutation-resolvers-js"></a>

This section will show you how to make a basic mutation resolver.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

   1. In the **APIs dashboard**, choose your GraphQL API.

   1. In the **Sidebar**, choose **Schema**.

1. Under the **Resolvers** section and the **Mutation** type, choose **Attach** next to your field.
**Note**  
In our example, we're attaching a resolver for `createPost`, which adds a `Post` object to our table. Let's assume we're using the same DynamoDB table from the last section. Its partition key is set to the `id` and is empty.

1. On the **Attach resolver** page, under **Resolver type**, choose `pipeline resolvers`. As a reminder, you can find more information about resolvers [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-components.html). For **Resolver runtime**, choose `APPSYNC_JS` to enable the JavaScript runtime.

1. You can enable [caching](https://docs.aws.amazon.com/appsync/latest/devguide/enabling-caching.html) for this API. We recommend turning this feature off for now. Choose **Create**.

1. Choose **Add function**, then choose **Create new function**. Alternatively, you may see a **Create function** button to choose instead.

   1. Choose your data source. This should be the source whose data you will manipulate with the mutation.

   1. Enter a `Function name`.

   1. Under **Function code**, you'll need to implement the function's behavior. This is a mutation, so the request will ideally perform some state-changing operation on the invoked data source. The result will be processed by the response function.
**Note**  
`createPost` is adding, or "putting", a new `Post` in the table with our parameters as the data. We could add something like this:   

      ```
      import { util } from '@aws-appsync/utils';
      
      /**
       * Sends a request to `put` an item in the DynamoDB data source
       */
      export function request(ctx) {
        return {
          operation: 'PutItem',
          key: util.dynamodb.toMapValues({id: util.autoId()}),
          attributeValues: util.dynamodb.toMapValues(ctx.args.input),
        };
      }
      
      /**
       * returns the result of the `put` operation
       */
      export function response(ctx) {
        return ctx.result;
      }
      ```
In this step, we also added `request` and `response` functions:  
`request`: The request handler accepts the context as the argument. The request handler return statement performs a [`PutItem`](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html#js-aws-appsync-resolver-reference-dynamodb-putitem) command, which is a built-in DynamoDB operation (see [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-2.html) or [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.WritingData) for examples). The `PutItem` command adds a `Post` object to our DynamoDB table by taking the partition `key` value (automatically generated by `util.autoid()`) and `attributes` from the context argument input (these are the values we will pass in our request). The `key` is the `id` and `attributes` are the `date` and `title` field arguments. They're both preformatted through the [`util.dynamodb.toMapValues`](https://docs.aws.amazon.com/appsync/latest/devguide/dynamodb-helpers-in-util-dynamodb-js.html#utility-helpers-in-toMap-js) helper to work with the DynamoDB table.
`response`: The response accepts the updated context and returns the result of the request handler.

   1. Choose **Create** after you're done.

1. Back on the resolver screen, under **Functions**, choose the **Add function** drop-down and add your function to your functions list.

1. Choose **Save** to update the resolver.

------
#### [ CLI ]

**To add your function**
+ Create a function for your pipeline resolver using the `[create-function](https://docs.aws.amazon.com/cli/latest/reference/appsync/create-function.html)` command.

  You'll need to enter a few parameters for this particular command:

  1. The `api-id` of your API.

  1. The `name` of the function in the AWS AppSync console.

  1. The `data-source-name`, or the name of the data source the function will use. It must already be created and linked to your GraphQL API in the AWS AppSync service.

  1. The `runtime`, or environment and language of the function. For JavaScript, the name must be `APPSYNC_JS`, and the runtime, `1.0.0`.

  1. The `code`, or request and response handlers of your function. While you can type it in manually, it's far easier to add it to a .txt file (or a similar format) then pass it in as the argument. 
**Note**  
Our query code will be in a file passed in as the argument:  

     ```
     import { util } from '@aws-appsync/utils';
     
     /**
      * Sends a request to `put` an item in the DynamoDB data source
      */
     export function request(ctx) {
       return {
         operation: 'PutItem',
         key: util.dynamodb.toMapValues({id: util.autoId()}),
         attributeValues: util.dynamodb.toMapValues(ctx.args.input),
       };
     }
     
     /**
      * returns the result of the `put` operation
      */
     export function response(ctx) {
       return ctx.result;
     }
     ```

  An example command may look like this:

  ```
  aws appsync create-function \
  --api-id abcdefghijklmnopqrstuvwxyz \
  --name add_posts_func_1 \
  --data-source-name table-for-posts \
  --runtime name=APPSYNC_JS,runtimeVersion=1.0.0 \
  --code file:///path/to/file/{filename}.{fileType}
  ```

  An output will be returned in the CLI. Here's an example:

  ```
  {
      "functionConfiguration": {
          "functionId": "vulcmbfcxffiram63psb4dduoa",
          "functionArn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/functions/vulcmbfcxffiram63psb4dduoa",
          "name": "add_posts_func_1",
          "dataSourceName": "table-for-posts",
          "maxBatchSize": 0,
          "runtime": {
              "name": "APPSYNC_JS",
              "runtimeVersion": "1.0.0"
          },
          "code": "{{Code output foes here}}"
      }
  }
  ```
**Note**  
Make sure you record the `functionId` somewhere as this will be used to attach the function to the resolver.

**To create your resolver**
+ Create a pipeline function for `Mutation` by running the `[create-resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html)` command.

  You'll need to enter a few parameters for this particular command:

  1. The `api-id` of your API.

  1. The `type-name`, or the special object type in your schema (Query, Mutation, Subscription).

  1. The `field-name`, or the field operation inside the special object type you want to attach the resolver to.

  1. The `kind`, which specifies a unit or pipeline resolver. Set this to `PIPELINE` to enable pipeline functions.

  1. The `pipeline-config`, or the function(s) to attach to the resolver. Make sure you know the `functionId` values of your functions. Order of listing matters.

  1. The `runtime`, which was `APPSYNC_JS` (JavaScript). The `runtimeVersion` currently is `1.0.0`.

  1. The `code`, which contains the before and after step.
**Note**  
Our query code will be in a file passed in as the argument:  

     ```
     import { util } from '@aws-appsync/utils';
     
     /**
      * Sends a request to `put` an item in the DynamoDB data source
      */
     export function request(ctx) {
       const { id, ...values } = ctx.args;
       return {
         operation: 'PutItem',
         key: util.dynamodb.toMapValues({ id }),
         attributeValues: util.dynamodb.toMapValues(values),
       };
     }
     
     /**
      * returns the result of the `put` operation
      */
     export function response(ctx) {
       return ctx.result;
     }
     ```

  An example command may look like this:

  ```
  aws appsync create-resolver \
  --api-id abcdefghijklmnopqrstuvwxyz \
  --type-name Mutation \
  --field-name createPost \
  --kind PIPELINE \
  --pipeline-config functions=vulcmbfcxffiram63psb4dduoa \
  --runtime name=APPSYNC_JS,runtimeVersion=1.0.0 \
  --code file:///path/to/file/{filename}.{fileType}
  ```

  An output will be returned in the CLI. Here's an example:

  ```
  {
      "resolver": {
          "typeName": "Mutation",
          "fieldName": "createPost",
          "resolverArn": "arn:aws:appsync:us-west-2:107289374856:apis/abcdefghijklmnopqrstuvwxyz/types/Mutation/resolvers/createPost",
          "kind": "PIPELINE",
          "pipelineConfig": {
              "functions": [
                  "vulcmbfcxffiram63psb4dduoa"
              ]
          },
          "maxBatchSize": 0,
          "runtime": {
              "name": "APPSYNC_JS",
              "runtimeVersion": "1.0.0"
          },
          "code": "{{Code output goes here}}"
      }
  }
  ```

------
#### [ CDK ]

**Tip**  
Before you use the CDK, we recommend reviewing the CDK's [official documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html) along with AWS AppSync's [CDK reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync-readme.html).  
The steps listed below will only show a general example of the snippet used to add a particular resource. This is **not** meant to be a working solution in your production code. We also assume you already have a working app.
+ To make a mutation, assuming you're in the same project, you can add it to the stack file like the query. Here's a modified function and resolver for a mutation that adds a new `Post` to the table:

  ```
  const add_func_2 = new appsync.AppsyncFunction(this, 'func-add-post', {
    name: 'add_posts_func_1',
    add_api,
    dataSource: add_api.addDynamoDbDataSource('table-for-posts-2', add_ddb_table),
        code: appsync.Code.fromInline(`
            export function request(ctx) {
              return {
                operation: 'PutItem',
                key: util.dynamodb.toMapValues({id: util.autoId()}),
                attributeValues: util.dynamodb.toMapValues(ctx.args.input),
              };
            }
  
            export function response(ctx) {
              return ctx.result;
            }
        `), 
    runtime: appsync.FunctionRuntime.JS_1_0_0,
  });
  
  new appsync.Resolver(this, 'pipeline-resolver-create-posts', {
    add_api,
    typeName: 'Mutation',
    fieldName: 'createPost',
        code: appsync.Code.fromInline(`
            export function request(ctx) {
              return {};
            }
  
            export function response(ctx) {
              return ctx.prev.result;
            }
        `),
    runtime: appsync.FunctionRuntime.JS_1_0_0,
    pipelineConfig: [add_func_2],
  });
  ```
**Note**  
Since this mutation and the query are similarly structured, we'll just explain the changes we made to make the mutation.   
In the function, we changed the CFN id to `func-add-post` and name to `add_posts_func_1` to reflect the fact that we're adding `Posts` to the table. In the data source, we made a new association to our table (`add_ddb_table`) in the AWS AppSync console as `table-for-posts-2` because the `addDynamoDbDataSource` method requires it. Keep in mind, this new association is still using the same table we created earlier, but we now have two connections to it in the AWS AppSync console: one for the query as `table-for-posts` and one for the mutation as `table-for-posts-2`. The code was changed to add a `Post` by generating its `id` value automatically and accepting a client's input for the rest of the fields.  
In the resolver, we changed the id value to `pipeline-resolver-create-posts` to reflect the fact that we're adding `Posts` to the table. To reflect the mutation in the schema, the type name was changed to `Mutation`, and the name, `createPost`. The pipeline config was set to our new mutation function `add_func_2`.

------

To summarize what's happening in this example, AWS AppSync automatically converts arguments defined in the `createPost` field from your GraphQL schema into DynamoDB operations. The example stores records in DynamoDB using a key of `id`, which is automatically created using our `util.autoId()` helper. All of the other fields you pass to the context arguments (`ctx.args.input`) from requests made in the AWS AppSync console or otherwise will be stored as the table's attributes. Both the key and the attributes are automatically mapped to a compatible DynamoDB format using the `util.dynamodb.toMapValues(values)` helper.

AWS AppSync also supports test and debug workflows for editing resolvers. You can use a mock `context` object to see the transformed value of the template before invoking it. Optionally, you can view the full request to a data source interactively when you run a query. For more information, see [Test and debug resolvers (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/test-debug-resolvers-js.html) and [Monitoring and logging](https://docs.aws.amazon.com/appsync/latest/devguide/monitoring.html#aws-appsync-monitoring).

## Advanced resolvers
<a name="advanced-resolvers-js"></a>

If you are following the optional pagination section in [Designing your schema](designing-your-schema.md#aws-appsync-designing-your-schema), you still need to add your resolver to your request to make use of pagination. Our example used a query pagination called `getPosts` to return only a portion of the things requested at a time. Our resolver's code on that field may look like this:

```
/**
 * Performs a scan on the dynamodb data source
 */
export function request(ctx) {
  const { limit = 20, nextToken } = ctx.args;
  return { operation: 'Scan', limit, nextToken };
}

/**
 * @returns the result of the `put` operation
 */
export function response(ctx) {
  const { items: posts = [], nextToken } = ctx.result;
  return { posts, nextToken };
}
```

In the request, we pass in the context of the request. Our `limit` is {{20}}, meaning we return up to 20 `Posts` in the first query. Our `nextToken` cursor is fixed to the first `Post` entry in the data source. These are passed to the args. The request then performs a scan from the first `Post` up to the scan limit number. The data source stores the result in the context, which is passed to the response. The response returns the `Posts` it retrieved, then sets the `nextToken` is set to the `Post` entry right after the limit. The next request is sent out to do the exact same thing but starting at the offset right after the first query. Keep in mind that these sorts of requests are done sequentially and not in parallel.