# Merging APIs in AWS AppSync

As the use of GraphQL expands within an organization, trade-offs between API ease-of-use and
API development velocity can arise. On the one hand, organizations adopt AWS AppSync and GraphQL to
simplify application development. This gives developers a flexible API they can use to securely
access, manipulate, and combine data from one or more data domains with a single network call.
On the other hand, teams within an organization that are responsible for the different data
domains combined into a single GraphQL API endpoint may want the ability to create, manage, and
deploy API updates independent of each other. This increases their development velocities.

To resolve this tension, the AWS AppSync Merged APIs feature allows teams from different data
domains to independently create and deploy AWS AppSync APIs (e.g., GraphQL schemas, resolvers, data
sources, and functions), that can then be combined into a single, merged API. This gives
organizations the ability to maintain a simple to use, cross domain API, and a way for the
different teams that contribute to that API the ability to quickly and independently make API
updates.

The following diagram shows the merged API workflow:

![Diagram showing the merged API workflow with multiple source APIs being combined into a single merged API endpoint](images/merged-api-workflow.png)
Using Merged APIs, organizations can import the resources of multiple, independent source
AWS AppSync APIs into a single AWS AppSync Merged API endpoint. To do this, AWS AppSync allows you to create a
list of source AWS AppSync APIs, and then merge all of the metadata associated with the source
APIs including schema, types, datasources, resolvers, and functions, into a new AWS AppSync merged
API.

During merges, there's the possibility that a merge conflict will occur due to
inconsistencies in the source API data content such as type naming conflicts when combining
multiple schemas. For simple use cases where no definitions in the source APIs conflict, there's
no need to modify the source API schemas. The resulting Merged API simply imports all types,
resolvers, data sources and functions from the original source AWS AppSync APIs. For complex use
cases where conflicts arise, the users/teams will have to resolve the conflicts through various
means. AWS AppSync provides users with several tools and examples that can reduce merge conflicts.

Subsequent merges that are configured in AWS AppSync will propagate changes made in the source
APIs to the associated Merged API.

## Merged APIs and Federation

There are many solutions and patterns in the GraphQL community for combining GraphQL
schemas and enabling team collaboration through a shared graph. AWS AppSync Merged APIs adopt a
_build time_ approach to schema composition, where source
APIs are combined into a separate, Merged API. An alternative approach is to layer a _run time_ router across multiple source APIs or sub-graphs. In this
approach, the router receives a request, references a combined schema that it maintains as
metadata, constructs a request plan, and then distributes request elements across its
underlying sub-graphs/servers. The following table compares the AWS AppSync Merged API build-time
approach with router-based, run-time approaches to GraphQL schema composition:

|                                           |                                                                                                       |                                                                                                                                                                                     |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature                                   | AppSync Merged API                                                                                    | Router-based solutions                                                                                                                                                              |
| Sub-graphs managed independently          | Yes                                                                                                   | Yes                                                                                                                                                                                 |
| Sub-graphs addressable independently      | Yes                                                                                                   | Yes                                                                                                                                                                                 |
| Automated schema composition              | Yes                                                                                                   | Yes                                                                                                                                                                                 |
| Automated conflict detection              | Yes                                                                                                   | Yes                                                                                                                                                                                 |
| Conflict resolution via schema directives | Yes                                                                                                   | Yes                                                                                                                                                                                 |
| Supported sub-graph servers               | AWS AppSync\*                                                                                         | Varies                                                                                                                                                                              |
| Network complexity                        | Single, merged API means no extra network hops.                                                       | Multi-layer architecture requires query planning and<br>delegation, sub-query parsing and serialization/deserialization, and reference resolvers<br>in sub-graphs to perform joins. |
| Observability support                     | Built-in monitoring, logging, and tracing. A single, Merged<br>API server means simplified debugging. | Build-your-own observability across router and all associated<br>sub-graph servers. Complex debugging across distributed system.                                                    |
| Authorization support                     | Built in support for multiple authorization modes.                                                    | Build-your-own authorization rules.                                                                                                                                                 |
| Cross account security                    | Built-in support for cross-AWS cloud account<br>associations.                                         | Build-your-own security model.                                                                                                                                                      |
| Subscriptions support                     | Yes                                                                                                   | No                                                                                                                                                                                  |

\* AWS AppSync Merged APIs can only be associated with AWS AppSync source APIs. If you need support
for schema composition across AWS AppSync and non-AWS AppSync sub-graphs, you can connect one or more
AWS AppSync GraphQL and/or Merged APIs into a router-based solution. For example, see the reference
blog for adding AWS AppSync APIs as a sub-graph using a router-based architecture with Apollo
Federation v2: [Apollo GraphQL Federation with AWS AppSync](https://aws.amazon.com/blogs/mobile/federation-appsync-subgraph/ "https://aws.amazon.com/blogs/mobile/federation-appsync-subgraph/").

###### Topics

- [Merged API conflict resolution](#merged-api-conflict-resolution "#merged-api-conflict-resolution")
- [Configuring schemas](#configuring-schemas-merged-api "#configuring-schemas-merged-api")
- [Configuring authorization modes](#configuring-authorization-merged-api "#configuring-authorization-merged-api")
- [Configuring execution roles](#execution-roles-merged-api "#execution-roles-merged-api")
- [Configuring cross-account Merged APIs using
  AWS RAM](#cross-account-merged-api "#cross-account-merged-api")
- [Merging](#merges "#merges")
- [Additional support for Merged APIs](#merge-api-additional-support "#merge-api-additional-support")
- [Merged API limitations](#merged-api-limits "#merged-api-limits")
- [Merged API considerations](#merged-api-considerations "#merged-api-considerations")
- [Creating Merged APIs](#creating-merged-api "#creating-merged-api")

## Merged API conflict resolution

In the event of a merge conflict, AWS AppSync provides users with several tools and examples to
help troubleshoot the issue(s).

### Merged API schema directives

AWS AppSync has introduced several GraphQL directives that can be used to- reduce or resolve
conflicts across source APIs:

- _@canonical_: This directive sets the precedence of types/fields
  with similar names and data. If two or more source APIs have the same GraphQL type or
  field, one of the APIs can annotate their type or field as _canonical_, which will be prioritized during the merge. Conflicting
  types/fields that aren't annotated with this directive in other source APIs are ignored
  when merged.
- _@hidden_: This directive encapsulates certain types/fields to
  remove it from the merging process. Teams may want to remove or hide specific types or
  operations in the source API so only internal clients can access specific typed data.
  With this directive attached, types or fields are not merged into the Merged API.
- _@renamed_: This directive changes the names of types/fields to reduce naming
  conflicts. There are situations where different APIs have the same type or field name. However, they all
  need to be available in the merged schema. A simple way to include them all in the Merged API is to rename
  the field to something similar but different.

To show the utility schema directives provide, consider the following example:

In this example, let's assume that we want to merge two source APIs. We're given two
schemas that create and retrieve posts (e.g., comment section or social media posts).
Assuming that the types and fields are very similar, there's a high chance for conflict
during a merge operation. The snippets below show the types and fields of each
schema.

The first file, called _Source1.graphql_, is a GraphQL
schema that allows a user to create `Posts` using the `putPost`
mutation. Each `Post` contains a title and an ID. The ID is used to reference the
`User`, or poster's information (email and address), and the
`Message`, or the payload (content). The `User` type is annotated
with the _@canonical_ tag.

```
# This snippet represents a file called Source1.graphql

type Mutation {
    putPost(id: ID!, title: String!): Post
}

type Post {
    id: ID!
    title: String!
}

type Message {
   id: ID!
   content: String
}

type User @canonical {
   id: ID!
   email: String!
   address: String!
}

type Query {
    singlePost(id: ID!): Post
    getMessage(id: ID!): Message
}
```

The second file, called _Source2.graphql_, is a GraphQL
schema that does very similar things as _Source1.graphql_.
However, notice that the fields of each type are different. When merging these two schemas,
there will be merge conflicts because of these differences.

Also note how _Source2.graphql_ also contains several
directives to reduce these conflicts. The `Post` type is annotated with a
_@hidden_ tag to obfuscate itself during the merge
operation. The `Message` type is annotated with the _@renamed_ tag to modify the type name to `ChatMessage` in the event
of a naming conflict with another `Message` type.

```
# This snippet represents a file called Source2.graphql

type Post @hidden  {
    id: ID!
    title: String!
    internalSecret: String!
}

type Message @renamed(to: "ChatMessage") {
   id: ID!
   chatId: ID!
   from: User!
   to: User!
}

# Stub user so that we can link the canonical definition from Source1
type User {
   id: ID!
}

type Query {
    getPost(id: ID!): Post
    getMessage(id: ID!): Message @renamed(to: "getChatMessage")
}
```

When the merge occurs, the result will produce the `MergedSchema.graphql`
file:

```
# This snippet represents a file called MergedSchema.graphql

type Mutation {
    putPost(id: ID!, title: String!): Post
}

# Post from Source2 was hidden so only uses the Source1 definition.
type Post {
    id: ID!
    title: String!
}

# Renamed from Message to resolve the conflict
type ChatMessage {
   id: ID!
   chatId: ID!
   from: User!
   to: User!
}

type Message {
   id: ID!
   content: String
}

# Canonical definition from Source1
type User {
   id: ID!
   email: String!
   address: String!
}

type Query {
    singlePost(id: ID!): Post
    getMessage(id: ID!): Message

    # Renamed from getMessage
    getChatMessage(id: ID!): ChatMessage
}
```

Several things occurred in the merge:

- The `User` type from _Source1.graphql_
  was prioritized over the `User` from _Source2.graphql_ due to the _@canonical_
  annotation.
- The `Message` type from _Source1.graphql_ was included in the merge. However, the
  `Message` from _Source2.graphql_ had a
  naming conflict. Due to its _@renamed_ annotation, it
  was also included in the merge but with the alternative name
  `ChatMessage`.
- The `Post` type from _Source1.graphql_
  was included, but the `Post` type from _Source2.graphql_ wasn't. Normally, there would be a conflict on this type,
  but because the `Post` type from _Source2.graphql_ had a _@hidden_
  annotation, its data was obfuscated and not included in the merge. This resulted in no
  conflicts.
- The `Query` type was updated to include the contents from both files.
  However, one `GetMessage` query was renamed to `GetChatMessage`
  due to the directive. This resolved the naming conflict between the two queries with the
  same name.

There's also the case of no directives being added to a conflicting type. Here, the
merged type will include the union of all fields from all source definitions of that type.
For instance, consider the following example:

This schema, called _Source1.graphql_, allows for
creating and retrieving `Posts`. The configuration is similar to the previous
example, but with less information.

```
# This snippet represents a file called Source1.graphql

type Mutation {
    putPost(id: ID!, title: String!): Post
}

type Post  {
    id: ID!
    title: String!
}

type Query {
    getPost(id: ID!): Post
}
```

This schema, called _Source2.graphql_, allows for
creating and retrieving `Reviews` (e.g., movie rating or restaurant reviews).
`Reviews` are associated with the `Post` of the same ID value.
Together, they contain the title, post ID, and payload message of the full review
post.

When merging, there will be a conflict between the two `Post` types. Because
there are no annotations to resolve this issue, the default behavior is to perform a union
operation on the conflicting types.

```
# This snippet represents a file called Source2.graphql

type Mutation {
    putReview(id: ID!, postId: ID!, comment: String!): Review
}

type Post  {
    id: ID!
    reviews: [Review]
}

type Review {
   id: ID!
   postId: ID!
   comment: String!
}

type Query {
    getReview(id: ID!): Review
}
```

When the merge occurs, the result will produce the `MergedSchema.graphql`
file:

```
# This snippet represents a file called MergedSchema.graphql

type Mutation {
    putReview(id: ID!, postId: ID!, comment: String!): Review
    putPost(id: ID!, title: String!): Post
}

type Post  {
    id: ID!
    title: String!
    reviews: [Review]
}

type Review {
   id: ID!
   postId: ID!
   comment: String!
}

type Query {
    getPost(id: ID!): Post
    getReview(id: ID!): Review
}
```

Several things occurred in the merge:

- The `Mutation` type faced no conflicts and was merged.
- The `Post` type fields were combined via union operation. Notice how the
  union between the two produced a single `id`, a `title`, and a
  single `reviews`.
- The `Review` type faced no conflicts and was merged.
- The `Query` type faced no conflicts and was merged.

### Managing resolvers on shared

types

In the above example, consider the case where _Source1.graphql_ has configured a unit resolver on `Query.getPost`,
which uses a DynamoDB data source named `PostDatasource`. This resolver will return
the `id` and `title` of a `Post` type. Now, consider
_Source2.graphql_ has configured a pipeline resolver on
`Post.reviews`, which runs two functions. `Function1` has a
`None` data source attached to perform custom authorization checks.
`Function2` has a DynamoDB data source attached to query the `reviews`
table.

```
query GetPostQuery {
    getPost(id: "1") {
        id,
        title,
        reviews
    }
}
```

When the query above is run by a client to the Merged API endpoint, the AWS AppSync service
first runs the unit resolver for `Query.getPost` from `Source1`, which
calls the `PostDatasource` and returns the data from DynamoDB. Then, it runs the
`Post.reviews` pipeline resolver in which `Function1` performs
custom authorization logic and `Function2` returns the reviews given the
`id` found in `$context.source`. The service processes the request
as a single GraphQL run, and this simple request will only require a single request
token.

### Managing resolver conflicts on

shared types

Consider the following case where we also implement a resolver on
`Query.getPost` in order to provide multiple fields at a time beyond the field
resolver in `Source2`. _Source1.graphql_ may
look like this:

```
# This snippet represents a file called Source1.graphql

type Post  {
    id: ID!
    title: String!
    date: AWSDateTime!
}

type Query {
    getPost(id: ID!): Post
}
```

_Source2.graphql_ may look like this:

```
# This snippet represents a file called Source2.graphql

type Post  {
  id: ID!
  content: String!
  contentHash: String!
  author: String!
}

type Query {
    getPost(id: ID!): Post
}
```

Attempting to merge these two schemas will generate a merge error because AWS AppSync Merged
APIs don't allow multiple source resolvers to be attached to the same field. In order to
resolve this conflict, you can implement a field resolver pattern that would require
_Source2.graphql_ to add a separate type that will define
the fields that it owns from the `Post` type. In the following example, we add a
type called `PostInfo`, which contains the content and author fields that will be
resolved by _Source2.graphql_. _Source1.graphql_ will implement the resolver attached to
`Query.getPost`, while _Source2.graphql_ will
now attach a resolver to `Post.postInfo`to ensure that all data can be
successfully retrieved:

```
type Post  {
  id: ID!
  postInfo: PostInfo
}

type PostInfo {
   content: String!
   contentHash: String!
   author: String!
}

type Query {
    getPost(id: ID!): Post
}
```

While resolving such a conflict requires source API schemas to be rewritten and,
potentially, clients to change their queries, the advantage of this approach is that
ownership of merged resolvers remains clear across source teams.

## Configuring schemas

Two parties are responsible for configuring the schemas to create a Merged API:

- **Merged API owners** - Merged API owners must configure
  the Merged API's authorization logic and advanced settings like logging, tracing, caching,
  and WAF support.
- **Associated source API owners** - Associated API owners
  must configure the schemas, resolvers, and datasources that make up the Merged API.

Because your Merged API’s schema is created from the schemas of your associated source
APIs, it's **read only**. This means changes to the schema must
be initiated in your source APIs. In the AWS AppSync console, you can toggle between your Merged
schema and the individual schemas of the source APIs included in your Merged API using the
drop-down list above the **Schema** window.

## Configuring authorization modes

Multiple authorization modes are available to protect your Merged API. To learn more about
authorization modes in AWS AppSync, see [Authorization
and authentication](security-authz.md "security-authz.md").

The following authorization modes are available to use with Merged APIs:

- **API key**: The simplest authorization strategy. All
  requests must include an API key under the `x-api-key` request header. Expired
  API keys are kept for 60 days after the expiration date.
- **AWS Identity and Access Management (IAM)**: The AWS
  IAM authorization strategy authorizes all requests that are **sigv4
  signed**.
- **Amazon Cognito User Pools**: Authorize your users via Amazon Cognito
  User Pools to achieve more fine-grained control.
- **AWS Lambda Authorizers**: A serverless function that allows you to authenticate
  and authorize access to your AWS AppSync API using custom logic.
- **OpenID Connect**: This authorization type enforces OpenID connect (OIDC)
  tokens provided by an OIDC-compliant service. Your application can leverage users and privileges defined by
  your OIDC provider for controlling access.

The authorization modes of a Merged API are configured by the Merged API owner. At the
time of a merge operation, the Merged API must include the primary authorization mode
configured on a source API either as its own primary authorization mode or as a secondary
authorization mode. Otherwise, it will be incompatible, and the merge operation will fail with
a conflict. When using multi-auth directives in the source APIs, the merging process is able
to automatically merge these directives into the unified endpoint. In the case where the
primary authorization mode of the source API doesn't match the primary authorization mode of
the Merged API, it will automatically add these auth directives to ensure that the
authorization mode for the types in the source API is consistent.

## Configuring execution roles

When you create a Merged API, you need to define a service role. An AWS service role
is an AWS Identity and Access Management (IAM) role that is used by AWS services to perform tasks on your
behalf.

In this context, it's necessary for your Merged API to run resolvers that access data
from the data sources configured in your source APIs. The required service role for this is
the `mergedApiExecutionRole`, and it must have explicit access to run requests on
source APIs included in your merged API via the `appsync:SourceGraphQL` IAM
permission. During the run of a GraphQL request, the AWS AppSync service will assume this service
role and authorize the role to perform the `appsync:SourceGraphQL` action.

AWS AppSync supports allowing or denying this permission on specific top-level fields within
the request like how the IAM authorization mode works for IAM APIs. For non-top-level
fields, AWS AppSync requires you to define the permission on the source API ARN itself. In order
to restrict access to specific non-top-level fields in the Merged API, we recommend
implementing custom logic within your Lambda or hiding the source API fields from the Merged
API using the _@hidden_ directive. If you want to allow the
role to perform all data operations within a source API, you can add the policy below. Note
that the first resource entry allows access to all top-level fields and the second entry
covers child resolvers that authorize on the source API resource itself:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [ "appsync:SourceGraphQL"],
 "Resource": [
 "arn:aws:appsync:us-west-2:123456789012:apis/YourSourceGraphQLApiId/*",
 "arn:aws:appsync:us-west-2:123456789012:apis/YourSourceGraphQLApiId"]
 }]
}`

```

If you want to limit the access to only a specific top-level field, you can use a policy
like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [ "appsync:SourceGraphQL"],
 "Resource": [
 "arn:aws:appsync:us-west-2:123456789012:apis/YourSourceGraphQLApiId/types/Query/fields/<Field-1>",
 "arn:aws:appsync:us-west-2:123456789012:apis/YourSourceGraphQLApiId"]
 }]
}`

```

You can also use the AWS AppSync console API creation wizard to generate a service role to
allow your Merged API to access resources configured in source APIs that are in the same
account as your merged API. In the case where your source APIs are not in the same account
as your merged API, you must first share your resources using AWS Resource Access Manager
(AWS RAM).

## Configuring cross-account Merged APIs using

AWS RAM

When you create a Merged API, you can optionally associate source APIs from other
accounts that have been shared via AWS Resource Access Manager (AWS RAM). AWS RAM helps you
share your resources securely across AWS accounts, within your organization or
organizational units (OUs), and with IAM roles and users.

AWS AppSync integrates with AWS RAM in order to support configuring and accessing source APIs
across multiple accounts from a single Merged API. AWS RAM allows you to create a resource
share, or a container of resources and the permission sets that will be shared for each of
them. You can add AWS AppSync APIs to a resource share in AWS RAM. Within a resource share, AWS AppSync
provides three different permission sets that can be associated with an AWS AppSync API in
RAM:

1. `AWSRAMPermissionAppSyncSourceApiOperationAccess`: The default permission set that's added
   when sharing an AWS AppSync API in AWS RAM if no other permission is specified. This permission set is used for
   sharing a source AWS AppSync API with a Merged API owner. This permission set includes the permission for
   `appsync:AssociateMergedGraphqlApi` on the source API as well as the
   `appsync:SourceGraphQL` permission required to access the source API resources at runtime.
2. `AWSRAMPermissionAppSyncMergedApiOperationAccess`: This permission set
   should be configured when sharing a Merged API with a source API owner. This permission
   set will give the source API the ability to configure the Merged API including the
   ability to associate any source APIs owned by the target principal to the Merged API and
   to read and update the source API associations of the Merged API.
3. `AWSRAMPermissionAppSyncAllowSourceGraphQLAccess`: This permission set
   allows the `appsync:SourceGraphQL` permission to be used with an AWS AppSync API.
   It is intended to be used for sharing a source API with a Merged API owner. In contrast
   to the default permission set for source API operation access, this permission set only
   includes the runtime permission `appsync:SourceGraphQL`. If a user opts to
   share the Merged API operation access to a source API owner, they will also need to
   share this permission from the source API to the Merged API owner in order to have
   runtime access through the Merged API endpoint.

AWS AppSync also supports customer-managed permissions. When one of the provided AWS-managed
permissions doesn't work, you can create your own customer-managed permission.
Customer-managed permissions are managed permissions that you author and maintain by
precisely specifying which actions can be performed under which conditions with resources
shared using AWS RAM. AWS AppSync allows you to choose from the following actions when creating
your own permission:

1. `appsync:AssociateSourceGraphqlApi`
2. `appsync:AssociateMergedGraphqlApi`
3. `appsync:GetSourceApiAssociation`
4. `appsync:UpdateSourceApiAssociation`
5. `appsync:StartSchemaMerge`
6. `appsync:ListTypesByAssociation`
7. `appsync:SourceGraphQL`

Once you have properly shared a source API or Merged API in AWS RAM and, if necessary, the
resource share invitation has been accepted, it will be visible in the AWS AppSync console when
you create or update the source API associations on your Merged API. You can also list all
AWS AppSync APIs that have been shared using AWS RAM with your account regardless of the permission
set by calling the `ListGraphqlApis` operation provided by AWS AppSync and using the
`OTHER_ACCOUNTS` owner filter.

###### Note

Sharing via AWS RAM requires the caller in AWS RAM to have permission to perform the
`appsync:PutResourcePolicy` action on any API that is being shared.

## Merging

### Managing merges

Merged APIs are meant to support team collaboration on a unified AWS AppSync endpoint. Teams
can independently evolve their own isolated source GraphQL APIs in the backend while the
AWS AppSync service manages the integration of the resources into the single Merged API endpoint
in order to reduce friction in collaboration and decrease development lead times.

### Auto-merges

Source APIs associated with your AWS AppSync Merged API can be configured to automatically
merge (auto-merge) into the Merged API after any changes are made to the source API. This
ensures that the changes from the source API are always propagated to the Merged API
endpoint in the background. Any change in the source API schema will be updated in the
Merged API so long as it does not introduce a merge conflict with an existing definition in
the Merged API. If the update in the source API is updating a resolver, data source, or
function, the imported resource will also be updated.When a new conflict is introduced that
cannot be automatically resolved (auto-resolved), the Merged API schema update is rejected
due to an unsupported conflict during the merge operation. The error message is available in
the console for each source API association that has a status of `MERGE_FAILED`.
You can also inspect the error message by calling the `GetSourceApiAssociation`
operation for a given source API association using the AWS SDK or using the AWS CLI like
so:

```
aws appsync get-source-api-association --merged-api-identifier <Merged API ARN> --association-id <SourceApiAssociation id>
```

This will produce a result in the following format:

```
{
    "sourceApiAssociation": {
        "associationId": "<association id>",
        "associationArn": "<association arn>",
        "sourceApiId": "<source api id>",
        "sourceApiArn": "<source api arn>",
        "mergedApiArn": "<merged api arn>",
        "mergedApiId": "<merged api id>",
        "sourceApiAssociationConfig": {
            "mergeType": "MANUAL_MERGE"
        },
        "sourceApiAssociationStatus": "MERGE_FAILED",
        "sourceApiAssociationStatusDetail": "Unable to resolve conflict on object with name title: Merging is not supported for fields with different types."
    }
}
```

### Manual merges

The default setting for a source API is a manual merge. To merge any changes that have
occurred in the source APIs since the Merged API was last updated, the source API owner can
invoke a manual merge from the AWS AppSync console or via the `StartSchemaMerge`
operation available in the AWS SDK and AWS CLI.

## Additional support for Merged APIs

### Configuring subscriptions

Unlike router-based approaches to GraphQL schema composition, AWS AppSync Merged APIs provide
built-in support for GraphQL subscriptions. All subscription operations defined in your
associated source APIs will automatically merge and function in your Merged API without
modification. To learn more about how AWS AppSync supports subscriptions via serverless
WebSockets connection, see [Real-time data](aws-appsync-real-time-data.md "aws-appsync-real-time-data.md").

### Configuring observability

AWS AppSync Merged APIs provide built-in logging, monitoring and metrics via [Amazon
CloudWatch](monitoring.md "monitoring.md"). AWS AppSync also provides built-in support for tracing via [AWS X-Ray](x-ray-tracing.md "x-ray-tracing.md").

### Configuring custom domains

AWS AppSync Merged APIs provide built-in support for using custom domains with your Merged
API's [GraphQL
and Real-time endpoints](custom-domain-name.md "custom-domain-name.md").

### Configuring caching

AWS AppSync Merged APIs provide built-in support for optionally caching request-level and/or
resolver-level responses as well as response compression. To learn more, see [Caching
and compression](enabling-caching.md "enabling-caching.md").

### Configuring private APIs

AWS AppSync Merged APIs provide built-in support for Private APIs that limit access to your
Merged API’s GraphQL and Real-time endpoints to traffic originating from [VPC
endpoints that you can configure](using-private-apis.md "using-private-apis.md").

### Configuring firewall rules

AWS AppSync Merged APIs provide built-in support for AWS WAF, which enables you to protect
your APIs by defining [web
application firewall rules](WAF-Integration.md "WAF-Integration.md").

### Configuring audit logs

AWS AppSync Merged APIs provide built-in support for AWS CloudTrail, which enables you to
[configure and manage audit logs](cloudtrail-logging.md "cloudtrail-logging.md").

## Merged API limitations

When developing Merged APIs, take note of the following rules:

1. A Merged API cannot be a source API for another Merged API.
2. A source API cannot be associated with more than one Merged API.
3. The default size limit for a Merged API schema document is 10 MB.
4. The default number of source APIs that can be associated with a Merged API is 10. However, you can request
   a limit increase if you need more than 10 source APIs in your Merged API.

## Merged API considerations

When designing and implementing Merged APIs, consider the following:

Merging multiple source APIs into a single endpoint can increase the size and complexity of your
GraphQL schema and queries. As your merged schema grows, queries may need to traverse multiple
resolvers to fulfill a single request, which can add latency to your overall
request time. For example, a query that accesses fields from multiple source APIs may require
AWS AppSync to execute resolvers from each source API in sequence, with each resolver adding to the
total response time.

We strongly recommend that you test your Merged APIs thoroughly during development and
under realistic load conditions to ensure they meet your business requirements. Pay specific
attention to:

- The depth and complexity of your merged schema, particularly queries that access
  fields across multiple source APIs.
- The number of resolvers that must execute to fulfill common query
  patterns.
- The performance characteristics of your data sources and resolvers under expected
  load.
- The impact of network latency when accessing resources across multiple source
  APIs.

Consider implementing performance optimizations such as caching, batching data source
requests, and designing your source API schemas to minimize the number of resolver
executions required for common operations.

## Creating Merged APIs

**To create a Merged API in the console**

1. Sign in to the AWS Management Console and open the [AWS AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **Dashboard** , choose **Create
      API**.

2. Choose **Merged API**, then choose **Next**.
3. In the **Specify API details** page, enter in the
   following information:
   1. Under **API Details**, enter in the following
      information:
      1. Specify your merged API’s **API name**. This
         field is a way to label your GraphQL API to conveniently distinguish it from other
         GraphQL APIs.
      2. Specify the **Contact details**. This field is
         optional and attaches a name or group to the GraphQL API. It’s not linked to or
         generated by other resources and works much like the API name field.

   2. Under **Service role**, you must attach an IAM
      execution role to your merged API so that AWS AppSync can securely import and use your
      resources at runtime. You can choose to **Create and use a new
      service role**, which will allow you to specify the policies and resources
      that AWS AppSync will use. You can also import an existing IAM role by choosing **Use an existing service role**, then selecting the role from
      the drop-down list.
   3. Under **Private API configuration**, you can choose
      to enable private API features. Note that this choice cannot be changed after creating
      the merged API. For more information about private APIs, see [Using
      AWS AppSync Private APIs](using-private-apis.md "using-private-apis.md").

   Choose **Next** after you're done.

4. Next, you must add the GraphQL APIs that will be used as the foundation for your merged API. In the
   **Select source APIs** page, enter in the following information:
   1. In the **APIs from your AWS account** table, choose **Add Source APIs**. In the list of GraphQL APIs, each entry will contain the
      following data:
      1. **Name**: The GraphQL API’s **API name** field.
      2. **API ID**: The GraphQL API’s unique ID value.
      3. **Primary auth mode**: The default authorization
         mode for the GraphQL API. For more information about authorization modes in
         AWS AppSync, see [Authorization and authentication](security-authz.md "security-authz.md").
      4. **Additonal auth mode**: The secondary
         authorization modes that were configured in the GraphQL API.
      5. Choose the APIs that you will use in the merged API by selecting the checkbox next to the API’s
         **Name** field. Afterwards, choose **Add Source
         APIs**. The selected GraphQL APIs will appear in the **APIs from your
         AWS accounts** table.

   2. In the **APIs from other AWS accounts** table, choose **Add Source APIs**. The GraphQL APIs in this list come from other accounts that are
      sharing their resources to yours through AWS Resource Access Manager (AWS RAM). The process for selecting GraphQL APIs in this
      table is the same as the process in the previous section. For more information about sharing resources
      through AWS RAM, see [What is
      AWS Resource Access Manager?](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

   Choose **Next** after you're done. 3. Add your primary auth mode. See [Authorization and authentication](security-authz.md "security-authz.md") for more
   information. Choose **Next**. 4. Review your inputs, then choose **Create API**.
