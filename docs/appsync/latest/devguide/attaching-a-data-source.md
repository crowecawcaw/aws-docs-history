# Attaching a data source in AWS AppSync

Data sources are resources in your AWS account that GraphQL APIs can interact with. AWS AppSync supports a
multitude of data sources like AWS Lambda, Amazon DynamoDB, relational databases (Amazon Aurora Serverless), Amazon OpenSearch Service, and
HTTP endpoints. An AWS AppSync API can be configured to interact with multiple data sources, enabling you to
aggregate data in a single location. AWS AppSync can use existing AWS resources from your account or provision
DynamoDB tables on your behalf from a schema definition.

The following section will show you how to attach a data source to your GraphQL API.

## Types of data sources

Now that you have created a schema in the AWS AppSync console, you can attach a data source to it. When
you initially create an API, there's an option to provision an Amazon DynamoDB table during the creation of the
predefined schema. However, we won't be covering that option in this section. You can see an example of this in
the [Launching a
schema](schema-launch-start.md "schema-launch-start.md") section.

Instead, we'll be looking at all of the data sources AWS AppSync supports. There are many factors that go
into picking the right solution for your application. The sections below will provide some additional context
for each data source. For general information about data sources, see [Data sources](data-source-components.md "data-source-components.md").

### Amazon DynamoDB

Amazon DynamoDB is one of AWS' main storage solutions for scalable applications. The core component of DynamoDB
is the **table**, which is simply a collection of data. You will typically
create tables based on entities like `Book` or `Author`. Table entry information is
stored as **items**, which are groups of fields that are unique to each entry.
A full item represents a row/record in the database. For example, an item for a `Book` entry
might include `title` and `author` along with their values. The individual fields like
the `title` and `author` are called **attributes**, which
are akin to column values in relational databases.

As you can guess, tables will be used to store data from your application. AWS AppSync allows you to hook up
your DynamoDB tables to your GraphQL API to manipulate data. Take this [use case](https://aws.amazon.com/blogs/mobile/new-real-time-multi-group-app-with-aws-amplify-graphql-build-a-twitter-community-clone/ "https://aws.amazon.com/blogs/mobile/new-real-time-multi-group-app-with-aws-amplify-graphql-build-a-twitter-community-clone/") from the _Front-end web and mobile blog_. This
application lets users sign up for a social media app. Users can join groups and upload posts that are
broadcasted to other users subscribed to the group. Their application stores user, post, and user group
information in DynamoDB. The GraphQL API (managed by AWS AppSync) interfaces with the DynamoDB table. When a user makes
a change in the system that will be reflected on the front-end, the GraphQL API retrieves these changes and
broadcasts them to other users in real time.

### AWS Lambda

Lambda is an event-driven service that automatically builds the necessary resources to run code as a
response to an event. Lambda uses **functions**, which are group statements
containing the code, dependencies, and configurations for executing a resource. Functions automatically
execute when they detect a **trigger**, a group of activities that invoke your
function. A trigger could be anything like an application making an API call, an AWS service in your
account spinning up a resource, etc. When triggered, functions will process **events**, which are JSON documents containing the data to modify.

Lambda is good for running code without having to provision the resources to run it. Take this [use
case](https://aws.amazon.com/blogs/mobile/building-a-graphql-api-with-java-and-aws-lambda/ "https://aws.amazon.com/blogs/mobile/building-a-graphql-api-with-java-and-aws-lambda/") from the _Front-end web and mobile blog_. This use case is
a bit similar to the one showcased in the DynamoDB section. In this application, the GraphQL API is responsible
for defining the operations for things like adding posts (mutations) and fetching that data (queries). To
implement the functionality of their operations (e.g., `getPost ( id: String ! ) : Post`,
`getPostsByAuthor ( author: String ! ) : [ Post ]`), they use Lambda functions to process
inbound requests. Under _Option 2: AWS AppSync with Lambda resolver_, they use
the AWS AppSync service to maintain their schema and link a Lambda data source to one of the operations. When the
operation is called, Lambda interfaces with the Amazon RDS proxy to perform the business logic on the
database.

### Amazon RDS

Amazon RDS lets you quickly build and configure relational databases. In Amazon RDS, you'll create a generic
**database instance** that will serve as the isolated database environment
in the cloud. In this instance, you'll use a **DB engine**, which is the actual
RDBMS software (PostgreSQL, MySQL, etc.). The service offloads much of the backend work by providing
scalability using AWS' infrastructure, security services such as patching and encryption, and lowered
administrative costs for deployments.

Take the same [use
case](https://aws.amazon.com/blogs/mobile/building-a-graphql-api-with-java-and-aws-lambda/ "https://aws.amazon.com/blogs/mobile/building-a-graphql-api-with-java-and-aws-lambda/") from the Lambda section. Under _Option 3: AWS AppSync with Amazon RDS resolver_, another option presented is linking the GraphQL API in AWS AppSync to Amazon RDS
directly. Using a [data API](../../../AmazonRDS/latest/AuroraUserGuide/data-api.md "../../../AmazonRDS/latest/AuroraUserGuide/data-api.md"), they associate the database with the GraphQL API. A resolver is attached to a field
(usually a query, mutation, or subscription) and implements the SQL statements needed to access the
database. When a request calling the field is made by the client, the resolver executes the statements
and returns the response.

### Amazon EventBridge

In EventBridge, you'll create **event buses**, which are pipelines that receive
events from services or applications you attach (the **event source**) and
process them based on a set of rules. An **event** is some state change in
an execution environment, while a **rule** is a set of filters for events. A
rule follows an **event pattern**, or metadata of an event's state change
(id, Region, account number, ARN(s), etc.). When an event matches the event pattern, EventBridge will send the
event across the pipeline to the destination service (**target**) and
trigger the action specified in the rule.

EventBridge is good for routing state-changing operations to some other service. Take this [use case](https://aws.amazon.com/blogs/mobile/appsync-eventbridge/ "https://aws.amazon.com/blogs/mobile/appsync-eventbridge/") from the _Front-end web and mobile blog_. The example depicts an e-commerce solution that
has several teams maintaining different services. One of these services provides order updates to the
customer at each step of the delivery (order placed, in progress, shipped, delivered, etc.) on the
front-end. However, the front-end team managing this service doesn't have direct access to the ordering
system data as that's maintained by a separate backend team. The backend team's ordering system is also
described as a black box, so it's hard to glean information about the way they're structuring their data.
However, the backend team did set up a system that published order data through an event bus managed by
EventBridge. To access the data coming from the event bus and route it to the front-end, the front-end team created
a new target pointing to their GraphQL API sitting in AWS AppSync. They also created a rule to only send data
relevant to the order update. When an update is made, the data from the event bus is sent to the GraphQL
API. The schema in the API processes the data, then passes it to the front-end.

### None data sources

If you aren't planning on using a data source, you can set it to `none`. A `none`
data source, while still explicitly categorized as a data source, isn't a storage medium. Typically, a
resolver will invoke one or more data sources at some point to process the request. However, there are
situations where you may not need to manipulate a data source. Setting the data source to `none`
will run the request, skip the data invocation step, then run the response.

Take the same [use case](https://aws.amazon.com/blogs/mobile/appsync-eventbridge/ "https://aws.amazon.com/blogs/mobile/appsync-eventbridge/") from
the EventBridge section. In the schema, the mutation processes the status update, then sends it out to subscribers.
Recalling how resolvers work, there's usually at least one data source invocation. However, the data in this
scenario was already sent automatically by the event bus. This means there's no need for the mutation to
perform a data source invocation; the order status can simply be handled locally. The mutation is set to
`none`, which acts as a pass-through value with no data source invocation. The schema is then
populated with the data, which is sent out to subscribers.

### OpenSearch

Amazon OpenSearch Service is a suite of tools to implement full-text searching, data visualization, and logging. You can
use this service to query the structured data you've uploaded.

In this service, you'll create instances of OpenSearch. These are called **nodes**. In a node, you'll be adding at least one **index**.
Indices conceptually are a bit like tables in relational databases. (However, OpenSearch isn't ACID
compliant, so it shouldn't be used that way). You'll populate your index with data that you upload to the
OpenSearch service. When your data is uploaded, it will be indexed in one or more shards that exist in the
index. A **shard** is like a partition of your index that contains some of your
data and can be queried separately from other shards. Once uploaded, your data will be structured as JSON
files called **documents**. You can then query the node for data in the
document.

### HTTP endpoints

You can use HTTP endpoints as data sources. AWS AppSync can send requests to the endpoints with the
relevant information like params and payload. The HTTP response will be exposed to the resolver, which will
return the final response after it finishes its operation(s).

## Adding a data source

If you created a data source, you can link it to the AWS AppSync service and, more specifically, the
API.

Console

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. Choose your API in the **Dashboard**.
   2. In the **Sidebar**, choose **Data
      Sources**.

2. Choose **Create data source**.
   1. Give your data source a name. You can also give it a description, but that's
      optional.
   2. Choose your **Data source type**.
   3. For DynamoDB, you'll have to choose your Region, then the table in the Region. You can
      dictate interaction rules with your table by choosing to make a new generic table role or
      importing an existing role for the table. You can enable [versioning](conflict-detection-and-sync.md "conflict-detection-and-sync.md"),
      which can automatically create versions of data for each request when multiple clients are
      trying to update data at the same time. Versioning is used to keep and maintain multiple
      variants of data for conflict detection and resolution purposes. You can also enable
      automatic schema generation, which takes your data source and generates some of the CRUD,
      `List`, and `Query` operations needed to access it in your
      schema.

   For OpenSearch, you'll have to choose your Region, then the domain (cluster) in the
   Region. You can dictate interaction rules with your domain by choosing to make a new
   generic table role or importing an existing role for the table.

   For Lambda, you'll have to choose your Region, then the ARN of the Lambda function in
   the Region. You can dictate interaction rules with your Lambda function by choosing to
   make a new generic table role or importing an existing role for the table.

   For HTTP, you'll have to enter your HTTP endpoint.

   For EventBridge, you'll have to choose your Region, then the event bus in the Region.
   You can dictate interaction rules with your event bus by choosing to make a new generic
   table role or importing an existing role for the table.

   For RDS, you'll have to choose your Region, then the secret store (username and
   password), database name, and schema.

   For none, you will add a data source with no actual data source. This is for handling
   resolvers locally rather than through an actual data source.

   ###### Note

   If you're importing existing roles, they need a trust policy. For more information,
   see the [IAM trust policy](#iam-trust-policy.title "#iam-trust-policy.title").

3. Choose **Create**.

###### Note

Alternatively, if you're creating a DynamoDB data source, you can go to the **Schema** page in the console, choose **Create
Resources** at the top of the page, then fill out a predefined model to convert
into a table. In this option, you will fill out or import the base type, configure the basic
table data including the partition key, and review the schema changes.

CLI

- Create your data source by running the [`create-data-source`](../../../cli/latest/reference/appsync/create-data-source.md "../../../cli/latest/reference/appsync/create-data-source.md") command.

You'll need to enter a few parameters for this particular command:

    1. The `api-id` of your API.
    2. The `name` of your table.
    3. The `type` of data source. Depending on the data source type you choose, you
     may need to enter a `service-role-arn` and a `-config` tag.

An example command may look like this:

```
 aws appsync create-data-source --api-id abcdefghijklmnopqrstuvwxyz --name data_source_name --type data_source_type --service-role-arn arn:aws:iam::107289374856:role/role_name --[data_source_type]-config {params}
```

CDK

###### Tip

Before you use the CDK, we recommend reviewing the CDK's [official documentation](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") along
with AWS AppSync's [CDK
reference](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md").

The steps listed below will only show a general example of the snippet used to add a particular
resource. This is **not** meant to be a working solution in your
production code. We also assume you already have a working app.

To add your particular data source, you'll need to add the construct to your stack file. A list of
data source types can be found here:

- [DynamoDbDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")
- [EventBridgeDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")
- [HttpDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")
- [LambdaDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")
- [NoneDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")
- [OpenSearchDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")
- [RdsDataSource](../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_appsync.md")

1. In general, you may have to add the import directive to the service you're using. For
   example, it may follow the forms:

```
import * as `x` from '`x`'; # import wildcard as the 'x' keyword from 'x-service'
import {`a`, `b`, ...} from '`c`'; # import {specific constructs} from 'c-service'
```

For example, here's how you could import the AWS AppSync and DynamoDB services:

```
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
```

2. Some services like RDS require some additional setup in the stack file before creating the
   data source (e.g., VPC creation, roles, and access credentials). Consult the examples in the
   relevant CDK pages for more information.
3. For most data sources, especially AWS services, you'll be creating a new instance of the
   data source in your stack file. Typically, this will look like the following:

```
const `add_data_source_func` = new `service_scope`.`resource_name`(scope: Construct, id: string, props: data_source_props);
```

For example, here's an example Amazon DynamoDB table:

```
const add_ddb_table = new dynamodb.Table(this, 'Table_ID', {
  partitionKey: {
    name: 'id',
    type: dynamodb.AttributeType.STRING,
  },
  sortKey: {
    name: 'id',
    type: dynamodb.AttributeType.STRING,
  },
  tableClass: dynamodb.TableClass.STANDARD,
});
```

###### Note

Most data sources will have at least one required prop (will be denoted **without** a `?` symbol). Consult the CDK documentation to
see which props are needed. 4. Next, you need to link the data source to the GraphQL API. The recommended method is to add
it when you make a function for your pipeline resolver. For instance, the snippet below is a
function that scans all elements in a DynamoDB table:

```
const add_func = new appsync.AppsyncFunction(this, 'func_ID', {
  name: 'func_name_in_console',
  add_api,
  **dataSource: add\_api.addDynamoDbDataSource('data\_source\_name\_in\_console', add\_ddb\_table),**
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
```

In the `dataSource` props, you can call the GraphQL API (`add_api`) and
use one of its built-in methods (`addDynamoDbDataSource`) to make the association
between the table and the GraphQL API. The arguments are the name of this link that will exist
in the AWS AppSync console (`data_source_name_in_console` in this example) and the table
method (`add_ddb_table`). More on this topic will be revealed in the next section
when you start making resolvers.

There are alternative methods for linking a data source. You could technically add
`api` to the props list in the table function. For example, here's the snippet
from step 3 but with an `api` props containing a GraphQL API:

```
const **add\_api** = new appsync.GraphqlApi(this, 'API_ID', {
  ...
});

const add_ddb_table = new dynamodb.Table(this, 'Table_ID', {

 ...

  **api: add\_api**
});
```

Alternatively, you can call the `GraphqlApi` construct separately:

```
const add_api = new appsync.GraphqlApi(this, 'API_ID', {
  ...
});

const add_ddb_table = new dynamodb.Table(this, 'Table_ID', {
  ...
});
**const link\_data\_source = add\_api.addDynamoDbDataSource('data\_source\_name\_in\_console', add\_ddb\_table);**
```

We recommend only creating the association in the function's props. Otherwise, you'll either
have to link your resolver function to the data source manually in the AWS AppSync console (if you
want to keep using the console value `data_source_name_in_console`) or create a
separate association in the function under another name like
`data_source_name_in_console_2`. This is due to limitations in how the props
process information.

###### Note

You'll have to redeploy the app to see your changes.

### IAM trust policy

If you’re using an existing IAM role for your data source, you need to grant that role the appropriate
permissions to perform operations on your AWS resource, such as `PutItem` on an Amazon DynamoDB
table. You also need to modify the trust policy on that role to allow AWS AppSync to use it for resource
access as shown in the following example policy:

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

You can also add conditions to your trust policy to limit access to the data source as desired.
Currently, `SourceArn` and `SourceAccount` keys can be used in these conditions. For
example, the following policy limits access to your data source to the account
`123456789012`:

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
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 }
 }
 }
 ]
}`

```

Alternatively, you can limit access to a data source to a specific API, such as
`abcdefghijklmnopq`, using the following policy:

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
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:appsync:us-west-2:123456789012:apis/abcdefghijklmnopq"
 }
 }
 }
 ]
}`

```

You can limit access to all AWS AppSync APIs from a specific region, such as `us-east-1`, using
the following policy:

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
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:appsync:us-east-1:123456789012:apis/*"
 }
 }
 }
 ]
}`

```

In the next section ([Configuring Resolvers](resolver-config-overview.md "resolver-config-overview.md")), we'll add our resolver business logic and attach it to the fields in our
schema to process the data in our data source.

For more information regarding role policy configuration, see [Modifying a role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md") in the
_IAM User Guide_.

For more information regarding cross-account access of AWS Lambda resolvers for AWS AppSync, see [Building cross-account
AWS Lambda resolvers for AWS AppSync](https://aws.amazon.com/blogs/mobile/appsync-lambda-cross-account/ "https://aws.amazon.com/blogs/mobile/appsync-lambda-cross-account/").
