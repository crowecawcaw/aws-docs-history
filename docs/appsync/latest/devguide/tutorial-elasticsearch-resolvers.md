# Using Amazon OpenSearch Service

resolvers in AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider
using the APPSYNC_JS runtime and its guides [here](tutorials-js.md "tutorials-js.md").

AWS AppSync supports using Amazon OpenSearch Service from domains that you have provisioned in your own
AWS account, provided they don’t exist inside a VPC. After your domains are provisioned,
you can connect to them using a data source, at which point you can configure a resolver in
the schema to perform GraphQL operations such as queries, mutations, and subscriptions. This
tutorial will take you through some common examples.

For more information, see the [Resolver Mapping
Template Reference for OpenSearch](resolver-mapping-template-reference-elasticsearch.md#aws-appsync-resolver-mapping-template-reference-elasticsearch "resolver-mapping-template-reference-elasticsearch.md#aws-appsync-resolver-mapping-template-reference-elasticsearch").

## One-Click Setup

To automatically set up a GraphQL endpoint in AWS AppSync with Amazon OpenSearch Service configured you
can use this AWS CloudFormation template:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/appsynces.yml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/appsynces.yml")

After the AWS CloudFormation deployment completes you can skip directly to [running GraphQL
queries and mutations](#tutorial-elasticsearch-resolvers-perform-queries-mutations "#tutorial-elasticsearch-resolvers-perform-queries-mutations").

## Create a New OpenSearch Service Domain

To get started with this tutorial, you need an existing OpenSearch Service domain. If you don’t have
one, you can use the following sample. Note that it can take up to 15 minutes for an
OpenSearch Service domain to be created before you can move on to integrating it with an AWS AppSync
data source.

```
aws cloudformation create-stack --stack-name AppSyncOpenSearch \
--template-url https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/ESResolverCFTemplate.yaml \
--parameters ParameterKey=OSDomainName,ParameterValue=ddtestdomain ParameterKey=Tier,ParameterValue=development \
--capabilities CAPABILITY_NAMED_IAM
```

You can launch the following AWS CloudFormation stack in the US West 2 (Oregon) region in your
AWS account:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/ESResolverCFTemplate.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/ESResolverCFTemplate.yaml")

## Configure Data Source for OpenSearch Service

After the OpenSearch Service domain is created, navigate to your AWS AppSync GraphQL API and choose
the **Data Sources** tab. Choose **New** and enter a friendly name for the data source, such as “oss”. Then
choose **Amazon OpenSearch domain** for **Data source type**, choose the appropriate region, and you
should see your OpenSearch Service domain listed. After selecting it you can either create a new role
and AWS AppSync will assign the role-appropriate permissions, or you can choose an
existing role, which has the following inline policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1234234",
 "Effect": "Allow",
 "Action": [
 "es:ESHttpDelete",
 "es:ESHttpHead",
 "es:ESHttpGet",
 "es:ESHttpPost",
 "es:ESHttpPut"
 ],
 "Resource": [
 "arn:aws:es:us-east-1:111122223333:domain/democluster/*"
 ]
 }
 ]
}`

```

You’ll also need to set up a trust relationship with AWS AppSync for that role:

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

Additionally, the OpenSearch Service domain has it’s own **Access
Policy** which you can modify through the Amazon OpenSearch Service console. You will need
to add a policy similar to the following, with the appropriate actions and resource for
the OpenSearch Service domain. Note that the **Principal** will be the
AppSync data source role, which if you let the console create this, can be found in the
IAM console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/APPSYNC_DATASOURCE_ROLE"
 },
 "Action": [
 "es:ESHttpDelete",
 "es:ESHttpHead",
 "es:ESHttpGet",
 "es:ESHttpPost",
 "es:ESHttpPut"
 ],
 "Resource": "arn:aws:es:us-east-1:111122223333:domain/DOMAIN_NAME/*"
 }
 ]
}`

```

## Connecting a Resolver

Now that the data source is connected to your OpenSearch Service domain, you can connect it to your
GraphQL schema with a resolver, as shown in the following example:

```
 schema {
   query: Query
   mutation: Mutation
 }

 type Query {
   getPost(id: ID!): Post
   allPosts: [Post]
 }

 type Mutation {
   addPost(id: ID!, author: String, title: String, url: String, ups: Int, downs: Int, content: String): AWSJSON
 }

type Post {
  id: ID!
  author: String
  title: String
  url: String
  ups: Int
  downs: Int
  content: String
}
...
```

Note that there is a user-defined `Post` type with a field of
`id`. In the following examples, we assume there is a process (which can
be automated) for putting this type into your OpenSearch Service domain, which would map to a path
root of `/post/_doc`, where `post` is the index. From this root
path, you can perform individual document searches, wildcard searches with
`/id/post*`, or multi-document searches with a path of
`/post/_search`. For example, if you have another type called
`User`, you can index documents under a new index called
`user`, then perform searches with a **path** of `/user/_search`.

From the schema editor in the AWS AppSync console, modify the preceding
`Posts` schema to include a `searchPosts` query:

```
type Query {
  getPost(id: ID!): Post
  allPosts: [Post]
  searchPosts: [Post]
}
```

Save the schema. On the right side, for `searchPosts`, choose **Attach resolver**. In the **Action
menu**, choose **Update runtime**, then choose
**Unit Resolver (VTL only)**. Then, choose your OpenSearch Service
data source. Under the **request mapping template**
section, select the drop-down for **Query posts** to get a
base template. Modify the `path` to be `/post/_search`. It should
look like the following:

```
{
    "version":"2017-02-28",
    "operation":"GET",
    "path":"/post/_search",
    "params":{
        "headers":{},
        "queryString":{},
        "body":{
            "from":0,
            "size":50
        }
    }
}
```

This assumes that the preceding schema has documents that have been indexed in OpenSearch Service
under the `post` field. If you structure your data differently, then you’ll
need to update accordingly.

Under the **response mapping template** section, you need
to specify the appropriate `_source` filter if you want to get back the data
results from an OpenSearch Service query and translate to GraphQL. Use the following template:

```
[
    #foreach($entry in $context.result.hits.hits)
    #if( $velocityCount > 1 ) , #end
    $utils.toJson($entry.get("_source"))
    #end
]
```

## Modifying Your Searches

The preceding request mapping template performs a simple query for all records.
Suppose you want to search by a specific author. Further, suppose you want that author
to be an argument defined in your GraphQL query. In the schema editor of the AWS AppSync
console, add an `allPostsByAuthor` query:

```
type Query {
  getPost(id: ID!): Post
  allPosts: [Post]
  allPostsByAuthor(author: String!): [Post]
  searchPosts: [Post]
}
```

Now choose **Attach resolver** and select the OpenSearch Service data
source, but use the following example in the **response mapping
template**:

```
{
    "version":"2017-02-28",
    "operation":"GET",
    "path":"/post/_search",
    "params":{
        "headers":{},
        "queryString":{},
        "body":{
            "from":0,
            "size":50,
            "query":{
                "match" :{
                    "author": $util.toJson($context.arguments.author)
                }
            }
        }
    }
}
```

Note that the `body` is populated with a term query for the
`author` field, which is passed through from the client as an argument.
You could optionally have prepopulated information, such as standard text, or even use
other [utilities](resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference "resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference").

If you’re using this resolver, fill in the **response mapping
template** with the same information as the previous example.

## Adding Data to OpenSearch Service

You may want to add data to your OpenSearch Service domain as the result of a GraphQL mutation. This
is a powerful mechanism for searching and other purposes. Because you can use GraphQL
subscriptions to [make your data
real-time](aws-appsync-real-time-data.md "aws-appsync-real-time-data.md"), it serves as a mechanism for notifying clients of updates to data
in your OpenSearch Service domain.

Return to the **Schema** page in the AWS AppSync console
and select **Attach resolver** for the
`addPost()` mutation. Select the OpenSearch Service data source again and use the
following **response mapping template** for the
`Posts` schema:

```
{
    "version":"2017-02-28",
    "operation":"PUT",
    "path": $util.toJson("/post/_doc/$context.arguments.id"),
    "params":{
        "headers":{},
        "queryString":{},
        "body":{
            "id": $util.toJson($context.arguments.id),
            "author": $util.toJson($context.arguments.author),
            "ups": $util.toJson($context.arguments.ups),
            "downs": $util.toJson($context.arguments.downs),
            "url": $util.toJson($context.arguments.url),
            "content": $util.toJson($context.arguments.content),
            "title": $util.toJson($context.arguments.title)
        }
    }
}
```

As before, this is an example of how your data might be structured. If you have
different field names or indexes, you need to update the `path` and
`body` as appropriate. This example also shows how to use
`$context.arguments` to populate the template from your GraphQL mutation
arguments.

Before moving on, use the following response mapping template, which will return the
result of the mutation operation or error information as output:

```
#if($context.error)
    $util.toJson($ctx.error)
#else
    $util.toJson($context.result)
#end
```

## Retrieving a Single Document

Finally, if you want to use the `getPost(id:ID)` query in your schema to
return an individual document, find this query in the schema editor of the AWS AppSync
console and choose **Attach resolver**. Select the OpenSearch Service
data source again and use the following mapping template:

```
{
    "version":"2017-02-28",
    "operation":"GET",
    "path": $util.toJson("post/_doc/$context.arguments.id"),
    "params":{
        "headers":{},
        "queryString":{},
        "body":{}
    }
}
```

Because the `path` above uses the `id` argument with an empty
body, this returns the single document. However, you need to use the following response
mapping template, because now you’re returning a single item and not a list:

```
$utils.toJson($context.result.get("_source"))
```

## Perform

Queries and Mutations

You should now be able to perform GraphQL operations against your OpenSearch Service domain.
Navigate to the **Queries** tab of the AWS AppSync console
and add a new record:

```
mutation addPost {
    addPost (
        id:"12345"
        author: "Fred"
        title: "My first book"
        content: "This will be fun to write!"
        url: "publisher website",
        ups: 100,
        downs:20
       )
}
```

You’ll see the result of the mutation on the right. Similarly, you can now run a
`searchPosts` query against your OpenSearch Service domain:

```
query searchPosts {
    searchPosts {
        id
        title
        author
        content
    }
}
```

## Best Practices

- OpenSearch Service should be for querying data, not as your primary database. You may want
  to use OpenSearch Service in conjunction with Amazon DynamoDB as outlined in [Combining GraphQL
  Resolvers](tutorial-combining-graphql-resolvers.md#aws-appsync-tutorial-combining-graphql-resolvers "tutorial-combining-graphql-resolvers.md#aws-appsync-tutorial-combining-graphql-resolvers").
- Only give access to your domain by allowing the AWS AppSync service role to
  access the cluster.
- You can start small in development, with the lowest-cost cluster, and then
  move to a larger cluster with high availability (HA) as you move into
  production.
