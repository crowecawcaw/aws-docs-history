# Using Amazon OpenSearch Service resolvers in AWS AppSync

AWS AppSync supports using Amazon OpenSearch Service from domains that you have provisioned in your own
AWS account, provided they don’t exist inside a VPC. After your domains are provisioned, you
can connect to them using a data source, at which point you can configure a resolver in the
schema to perform GraphQL operations such as queries, mutations, and subscriptions. This
tutorial will take you through some common examples.

For more information, see our [JavaScript resolver function reference for OpenSearch](resolver-reference-elasticsearch-js.md "resolver-reference-elasticsearch-js.md").

## Create a new OpenSearch Service domain

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

You can launch the following AWS CloudFormation stack in the US-West-2 (Oregon) Region in your AWS
account:

[![Blue button labeled "Launch Stack" with an arrow icon indicating an action to start.](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/ESResolverCFTemplate.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https://s3.us-west-2.amazonaws.com/awsappsync/resources/elasticsearch/ESResolverCFTemplate.yaml")

## Configure a data source for OpenSearch Service

After the OpenSearch Service domain is created, navigate to your AWS AppSync GraphQL API and choose the **Data Sources** tab. Choose **Create data source** and
enter a friendly name for the data source such as “`oss`”. Then, choose **Amazon OpenSearch domain** for **Data source type**,
choose the appropriate Region, and you should see your OpenSearch Service domain listed. After selecting it, you can
either create a new role, and AWS AppSync will assign the role-appropriate permissions, or you can choose an
existing role, which has the following inline policy:

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

Additionally, the OpenSearch Service domain has its own **Access Policy** that you can
modify through the Amazon OpenSearch Service console. You must add a policy similar to the one below with the appropriate
actions and resources for the OpenSearch Service domain. Note that the **Principal** will be
the AWS AppSync data source role, which can be found in the IAM console if you let said console create
it.

## Connecting a resolver

Now that the data source is connected to your OpenSearch Service domain, you can connect it to your GraphQL schema with
a resolver as shown in the following example:

```
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
```

Note that there is a user-defined `Post` type with a field of `id`. In the following
examples, we assume there is a process (which can be automated) for putting this type into your OpenSearch Service
domain, which would map to a path root of `/post/_doc` where `post` is the index. From
this root path, you can perform individual document searches, wildcard searches with `/id/post*`,
or multi-document searches with a path of `/post/_search`. For example, if you have another type
called `User`, you can index documents under a new index called `user`, then perform
searches with a **path** of `/user/_search`.

From the **Schema** editor in the AWS AppSync console, modify the preceding
`Posts` schema to include a `searchPosts` query:

```
type Query {
  getPost(id: ID!): Post
  allPosts: [Post]
  searchPosts: [Post]
}
```

Save the schema. In the **Resolvers** pane, find `searchPosts` and
choose **Attach**. Choose your OpenSearch Service data source and save the resolver. Update
your resolver's code using the snippet below:

```
import { util } from '@aws-appsync/utils'

/**
 * Searches for documents by using an input term
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the request
 */
export function request(ctx) {
	return {
		operation: 'GET',
		path: `/post/_search`,
		params: { body: { from: 0, size: 50 } },
	}
}

/**
 * Returns the fetched items
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the result
 */
export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type)
	}
	return ctx.result.hits.hits.map((hit) => hit._source)
}
```

This assumes that the preceding schema has documents that have been indexed in OpenSearch Service under the
`post` field. If you structure your data differently, you’ll need to update
accordingly.

## Modifying your searches

The preceding resolver request handler performs a simple query for all records. Suppose you want to search
by a specific author. Furthermore, suppose you want that author to be an argument defined in your GraphQL
query. In the **Schema** editor of the AWS AppSync console, add an
`allPostsByAuthor` query:

```
type Query {
  getPost(id: ID!): Post
  allPosts: [Post]
  allPostsByAuthor(author: String!): [Post]
  searchPosts: [Post]
}
```

In the **Resolvers** pane, find `allPostsByAuthor` and choose
**Attach**. Choose the OpenSearch Service data source and use the following code:

```
import { util } from '@aws-appsync/utils'

/**
 * Searches for documents by `author`
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the request
 */
export function request(ctx) {
	return {
		operation: 'GET',
		path: '/post/_search',
		params: {
			body: {
				from: 0,
				size: 50,
				query: { match: { author: ctx.args.author } },
			},
		},
	}
}

/**
 * Returns the fetched items
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the result
 */
export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type)
	}
	return ctx.result.hits.hits.map((hit) => hit._source)
}
```

Note that the `body` is populated with a term query for the `author` field, which is
passed through from the client as an argument. Optionally, you could use prepopulated information, such as
standard text.

## Adding data to OpenSearch Service

You may want to add data to your OpenSearch Service domain as the result of a GraphQL mutation. This is a powerful
mechanism for searching and other purposes. Because you can use GraphQL subscriptions to [make your data real-time](aws-appsync-real-time-data.md "aws-appsync-real-time-data.md"), it can serve as a mechanism for
notifying clients of updates to data in your OpenSearch Service domain.

Return to the **Schema** page in the AWS AppSync console and select **Attach** for the `addPost()` mutation. Select the OpenSearch Service data source again
and use the following code:

```
import { util } from '@aws-appsync/utils'

/**
 * Searches for documents by `author`
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the request
 */
export function request(ctx) {
	return {
		operation: 'PUT',
		path: `/post/_doc/${ctx.args.id}`,
		params: { body: ctx.args },
	}
}

/**
 * Returns the inserted post
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the result
 */
export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type)
	}
	return ctx.result
}
```

Like before, this is an example of how your data might be structured. If you have different field names or
indices, you need to update the `path` and `body`. This example also shows how to use
`context.arguments`, which can also be written as `ctx.args`, in your request
handler.

## Retrieving a single document

Finally, if you want to use the `getPost(id:ID)` query in your schema to return an individual
document, find this query in the **Schema** editor of the AWS AppSync console and
choose **Attach**. Select the OpenSearch Service data source again and use the following
code:

```
import { util } from '@aws-appsync/utils'

/**
 * Searches for documents by `author`
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the request
 */
export function request(ctx) {
	return {
		operation: 'GET',
		path: `/post/_doc/${ctx.args.id}`,
	}
}

/**
 * Returns the post
 * @param {import('@aws-appsync/utils').Context} ctx the context
 * @returns {*} the result
 */
export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type)
	}
	return ctx.result._source
}
```

## Perform queries and mutations

You should now be able to perform GraphQL operations against your OpenSearch Service domain.
Navigate to the **Queries** tab of the AWS AppSync console
and add a new record:

```
mutation AddPost {
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

You’ll see the result of the mutation on the right. Similarly, you can now run a `searchPosts`
query against your OpenSearch Service domain:

```
query search {
    searchPosts {
        id
        title
        author
        content
    }
}
```

## Best practices

- OpenSearch Service should be for querying data, not as your primary database. You may want
  to use OpenSearch Service in conjunction with Amazon DynamoDB as outlined in [Combining GraphQL
  Resolvers](tutorial-combining-graphql-resolvers-js.md "tutorial-combining-graphql-resolvers-js.md").
- Only give access to your domain by allowing the AWS AppSync service role to
  access the cluster.
- You can start small in development, with the lowest-cost cluster, and then
  move to a larger cluster with high availability (HA) as you move into
  production.
