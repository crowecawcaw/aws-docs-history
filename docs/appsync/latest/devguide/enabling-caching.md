# Configuring server-side

caching and API payload compression in AWS AppSync

AWS AppSync's server-side data caching capabilities make data available in a high speed,
in-memory cache, improving performance and decreasing latency. This reduces the need to
directly access data sources. Caching is available for both unit and pipeline
resolvers.

AWS AppSync also allows you to compress API responses so that payload content loads and
downloads faster. This potentially reduces the strain on your applications while also
potentially reducing your data transfer charges. Compression behavior is configurable and can
be set at your own discretion.

Refer to this section for help defining the desired behavior of server-side caching and
compression in your AWS AppSync API.

## Instance types

AWS AppSync hosts Amazon ElastiCache (Redis OSS) instances in the same AWS account and AWS Region as your
AWS AppSync API.

The following ElastiCache (Redis OSS) instance types are available:

**small**

1 vCPU, 1.5 GiB RAM, low to moderate network performance

**medium**

2 vCPU, 3 GiB RAM, low to moderate network performance

**large**

2 vCPU, 12.3 GiB RAM, up to 10 Gigabit network performance

**xlarge**

4 vCPU, 25.05 GiB RAM, up to 10 Gigabit network performance

**2xlarge**

8 vCPU, 50.47 GiB RAM, up to 10 Gigabit network performance

**4xlarge**

16 vCPU, 101.38 GiB RAM, up to 10 Gigabit network performance

**8xlarge**

32 vCPU, 203.26 GiB RAM, 10 Gigabit network performance (not available in all
Regions)

**12xlarge**

48 vCPU, 317.77 GiB RAM, 10 Gigabit network performance

###### Note

Historically, you specified a specific instance type (such as
`t2.medium`). As of July 2020, these legacy instance types continue to be
available, but their use is deprecated and discouraged. We recommend that you use the
generic instance types described here.

## Caching behavior

The following are the behaviors related to caching:

**None**

No server-side caching.

**Full request caching**

Full request caching is a mechanism that caches resolver execution results
individually. With this setting, AWS AppSync caches the execution of all resolvers
invoked during a request, with each resolver cached separately. The data for each
resolver is retrieved from its data source and populates the cache until the time
to live (TTL) expires. For subsequent API requests, results for each specific
resolver are returned from the cache. This means that data sources aren't
contacted directly unless the TTL has expired. AWS AppSync uses the contents of the
`context.arguments` and `context.identity` maps as
caching keys for each resolver.

**Per-resolver caching**

With this setting, each resolver must be explicitly opted in for it to cache
responses. You can specify a TTL and caching keys on the resolver. Caching keys
that you can specify are the top-level maps `context.arguments`,
`context.source`, and `context.identity`, and/or string
fields from these maps. The TTL value is mandatory, but the caching keys are
optional. If you don't specify any caching keys, the defaults are the contents of
the `context.arguments`, `context.source`, and
`context.identity` maps.

For example, you could use the following combinations:

- _context.arguments_ and _context.source_
- _context.arguments_ and _context.identity.sub_
- _context.arguments.id_ or _context.arguments.InputType.id_
- _context.source.id_ and _context.identity.sub_
- _context.identity.claims.username_

When you specify only a TTL and no caching keys, the behavior of the resolver
is the same as full request caching.

**Operation level caching**

Operation level caching stores entire GraphQL query operation responses as a
whole. When enabled, successful query responses are cached until their TTL
expires, with a maximum cacheable response size of 15 MB. For subsequent query
requests with the same cache key, responses will be served directly from the cache
without executing any resolvers while the TTL has not expired.

The cache key for operation level caching is generated using a combination of
the following:

- Certain attributes from the request's JSON payload:
  - The `query` string
  - The `operationName` string
  - The `variables` map

- The `context.identity` map (excluding
  `context.identity.sourceIp` for IAM and Amazon Cognito
  requests)
- The `context.request.headers` map (excluding certain reserved
  headers that are listed in the next section)

The authorization type used by the request will also affect the cache key. For
IAM-authorized requests, the cache key will additionally include the list of
allowed and denied resources. For Lambda-authorized requests, the cache key will
additionally include the list of denied fields.

The cache key will consider all request headers found in
`context.request.headers`, except the following reserved headers,
which are typically unique to specific requests:

- authorization
- cloudfront-forwarded-proto
- cloudfront-is-desktop-viewer
- cloudfront-is-mobile-viewer
- cloudfront-is-smarttv-viewer
- cloudfront-is-tablet-viewer
- cloudfront-viewer-asn
- cloudfront-viewer-country
- content-length
- host
- priority
- sec-ch-ua
- sec-ch-ua-mobile
- sec-ch-ua-platform
- via
- x-amz-cf-id
- x-amz-date
- x-amz-security-token
- x-amzn-appsync-is-vpce-request
- x-amzn-remote-ip
- x-amzn-requestid
- x-amzn-trace-id
- x-forwarded-for

**Cache time to live**

This setting defines the amount of time to store cached entries in memory. The
maximum TTL is 3,600 seconds (1 hour), after which entries are automatically
deleted.

## Cache encryption

When you use AWS AppSync's server-side data caching feature, encryption at rest and in transit is always enabled for new caches, and can't be disabled.

To enable encryption on an existing API cache, delete the cache and then recreate it.

To invalidate cache entries,
you
can make a flush cache API call using either the AWS AppSync console or the AWS Command Line Interface
(AWS CLI).

For more information, see the [ApiCache](../APIReference/API_ApiCache.md "../APIReference/API_ApiCache.md") data type in the
AWS AppSync API Reference.

## Cache eviction

When you set up AWS AppSync's server-side caching, you can configure a maximum TTL. This
value defines the amount of time that cached entries are stored in memory. In situations
where you must remove specific entries from your cache, you can use AWS AppSync's
`evictFromApiCache` extensions utility in your resolver's request or
response. (For example, when your data in your data sources have changed, and your cache
entry is now stale.) To evict an item from the cache, you must know its key. For this
reason, if you must evict items dynamically, we recommend using per-resolver caching and
explicitly defining a key to use to add entries to your cache.

## Evicting a cache entry

To evict an item from the cache, use the `evictFromApiCache` extensions
utility. Specify the type name and field name, then provide an object of key-value items to
build the key of the entry that you want to evict. In the object, each key represents a
valid entry from the `context` object that is used in the cached resolver's
`cachingKey` list. Each value is the actual value used to construct the value
of the key. You must put the items in the object in the same order as the caching keys in
the cached resolver's `cachingKey` list.

For example, see the following schema:

```
type Note {
  id: ID!
  title: String
  content: String!
}

type Query {
  getNote(id: ID!): Note
}

type Mutation {
  updateNote(id: ID!, content: String!): Note
}
```

In this example, you can enable per-resolver caching, then enable it for the
`getNote` query. Then, you can configure the caching key to consist of
`[context.arguments.id]`.

When you try to get a `Note`, to build the cache key, AWS AppSync performs a
lookup in its server-side cache using the `id` argument of the
`getNote` query.

When you update a `Note`, you must evict the entry for the specific note to
make sure that the next request fetches it from the backend data source. To do this, you
must create a request handler.

The following example shows one way to handle the eviction using this method:

```
import { util, Context } from '@aws-appsync/utils';
import { update } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	extensions.evictFromApiCache('Query', 'getNote', { 'ctx.args.id': ctx.args.id });
	return update({ key: { id: ctx.args.id }, update: { context: ctx.args.content } });
}

export const response = (ctx) => ctx.result;
```

Alternatively, you can also handle the eviction in the response handler.

When the `updateNote` mutation is processed, AWS AppSync tries to evict the
entry. If an entry is successfully cleared, the response contains an
`apiCacheEntriesDeleted` value in the `extensions` object that
shows how many entries were deleted:

```
"extensions": {  "apiCacheEntriesDeleted": 1}
```

## Evicting a cache entry based on identity

You can create caching keys based on multiple values from the `context`
object.

For example, take the following schema that uses Amazon Cognito user pools as the
default auth mode and is backed by an Amazon DynamoDB data source:

```
type Note {
  id: ID! # a slug; e.g.: "my-first-note-on-graphql"
  title: String
  content: String!
}

type Query {
  getNote(id: ID!): Note
}

type Mutation {
  updateNote(id: ID!, content: String!): Note
}
```

The `Note` object types are saved in a DynamoDB table. The table has a composite
key that uses the Amazon Cognito user name as the primary key and the `id` (a slug) of
the `Note` as the partition key. This is a multi-tenant system that allows
multiple users to host and update their private `Note` objects, which are never
shared.

Since this is a read-heavy system, the `getNote` query is cached using
per-resolver caching, with the caching key composed of `[context.identity.username,
 context.arguments.id]`. When a `Note` is updated, you can evict the
entry for that specific `Note`. You must add the components in the object in the
same order that they are specified in your resolver's `cachingKeys` list.

The following example shows this:

```
import { util, Context } from '@aws-appsync/utils';
import { update } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	extensions.evictFromApiCache('Query', 'getNote', {
		'ctx.identity.username': ctx.identity.username,
		'ctx.args.id': ctx.args.id,
	});
	return update({ key: { id: ctx.args.id }, update: { context: ctx.args.content } });
}

export const response = (ctx) => ctx.result;
```

A backend system can also update the `Note` and evict the entry. For example,
take this mutation:

```
type Mutation {
  updateNoteFromBackend(id: ID!, content: String!, username: ID!): Note @aws_iam
}
```

You can evict the entry, but add the components of the caching key to the
`cachingKeys` object.

In the following example, the eviction occurs in the response of the resolver:

```
import { util, Context } from '@aws-appsync/utils';
import { update } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
    return update({ key: { id: ctx.args.id }, update: { context: ctx.args.content } });
}

export function response(ctx) {
    extensions.evictFromApiCache('Query', 'getNote', {
        'ctx.identity.username': ctx.args.username,
        'ctx.args.id': ctx.args.id,
    });
    return ctx.result;
}
```

In cases where your backend data has been updated outside of AWS AppSync, you can evict an
item from the cache by calling a mutation that uses a `NONE` data source.

## Compressing API responses

AWS AppSync allows clients to request compressed payloads. If requested, API responses are
compressed and returned in response to requests that indicate that compressed content is
preferred. Compressed API responses load faster, content is downloaded faster, and your
data transfer charges may be reduced as well.

###### Note

Compression is available on all new APIs created after June 1st, 2020.

AWS AppSync [compresses](../../../AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.md#compressed-content-cloudfront-notes "../../../AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.md#compressed-content-cloudfront-notes") objects on a best-effort basis. In rare cases, AWS AppSync may skip
compression based on a variety of factors, including current capacity.

AWS AppSync can compress GraphQL query payload sizes between 1,000 to 10,000,000 bytes. To
enable compression, a client must send the `Accept-Encoding` header with the
value `gzip`. Compression can be verified by checking the
`Content-Encoding` header's value in the response (`gzip`).

The query explorer in the AWS AppSync console automatically sets the header value in the
request by default. If you execute a query that has a large enough response, compression
can be confirmed using your browser developer tools.
