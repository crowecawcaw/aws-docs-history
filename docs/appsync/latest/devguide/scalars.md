# Scalar types in GraphQL

A GraphQL object type has a name and fields, and those fields can have sub-fields. Ultimately, an object type's
fields must resolve to _scalar_ types, which represent the leaves of the query. For more
information about object types and scalars, see [Schemas and
types](https://graphql.org/learn/schema/ "https://graphql.org/learn/schema/") on the GraphQL website.

In addition to the default set of GraphQL scalars, AWS AppSync also lets you use the **service-defined** scalars that start with the _AWS_ prefix.
AWS AppSync doesn't support the creation of **user-defined** (custom) scalars. You must use
either the default or _AWS_ scalars.

You cannot use _AWS_ as a prefix for custom object types.

The following section is a reference for schema typing.

## Default scalars

GraphQL defines the following default scalars:

`ID`

A unique identifier for an object. This scalar is serialized like a `String` but isn't
meant to be human-readable.

`String`

A UTF-8 character sequence.

`Int`

An integer value between -(231) and
231-1.

`Float`

An IEEE 754 floating point value.

`Boolean`

A
Boolean
value, either `true` or `false`.

## AWS AppSync scalars

AWS AppSync defines the following scalars:

`AWSDate`

An extended [ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates "https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates")
string in the format `YYYY-MM-DD`.

`AWSTime`

An extended [ISO 8601 time](https://en.wikipedia.org/wiki/ISO_8601#Times "https://en.wikipedia.org/wiki/ISO_8601#Times") string
in the format `hh:mm:ss.sss`.

`AWSDateTime`

An extended [ISO 8601 date and
time](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations "https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations") string in the format `YYYY-MM-DDThh:mm:ss.sssZ`.

###### Note

The `AWSDate`, `AWSTime`, and `AWSDateTime` scalars can optionally
include a [time zone
offset](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators "https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators"). For example, the values `1970-01-01Z`, `1970-01-01-07:00`, and
`1970-01-01+05:30` are all valid for `AWSDate`. The time zone offset must be
either `Z` (UTC) or an offset in hours and minutes (and, optionally, seconds). For example,
`±hh:mm:ss`. The seconds field in the time zone offset is considered valid even though it's
not part of the ISO 8601 standard.

`AWSTimestamp`

An integer value representing the number of seconds before or after
`1970-01-01-T00:00Z`.

`AWSEmail`

An email address in the format `local-part@domain-part` as defined by [RFC 822](https://tools.ietf.org/html/rfc822 "https://tools.ietf.org/html/rfc822").

`AWSJSON`

A JSON string. Any valid JSON construct is automatically parsed and loaded in the resolver code as
maps, lists, or scalar values rather than as the literal input strings. Unquoted strings or otherwise
invalid JSON result in a GraphQL validation error.

`AWSPhone`

A phone number. This value is stored as a string. Phone numbers can contain either spaces or hyphens
to separate digit groups. Phone numbers without a country code are assumed to be US/North American
numbers adhering to the [North
American Numbering Plan (NANP)](https://en.wikipedia.org/wiki/North_American_Numbering_Plan "https://en.wikipedia.org/wiki/North_American_Numbering_Plan").

`AWSURL`

A URL as defined by [RFC 1738](https://tools.ietf.org/html/rfc1738 "https://tools.ietf.org/html/rfc1738"). For example,
`https://www.amazon.com/dp/B000NZW3KC/` or `mailto:example@example.com`. URLs
must contain a schema (`http`, `mailto`) and can't contain two forward slashes
(`//`) in the path part.

`AWSIPAddress`

A valid IPv4 or IPv6 address. IPv4 addresses are expected in quad-dotted notation
(`123.12.34.56`). IPv6 addresses are expected in non-bracketed, colon-separated format
(`1a2b:3c4b::1234:4567`). You can include an optional CIDR suffix
(`123.45.67.89/16`) to indicate subnet mask.

## Schema usage example

The following example GraphQL schema uses all of the custom scalars as an "object" and shows the resolver
request and response templates for basic put, get, and list operations. Finally, the example shows how you can use
this when running queries and mutations.

```
type Mutation {
    putObject(
        email: AWSEmail,
        json: AWSJSON,
        date: AWSDate,
        time: AWSTime,
        datetime: AWSDateTime,
        timestamp: AWSTimestamp,
        url: AWSURL,
        phoneno: AWSPhone,
        ip: AWSIPAddress
    ): Object
}

type Object {
    id: ID!
    email: AWSEmail
    json: AWSJSON
    date: AWSDate
    time: AWSTime
    datetime: AWSDateTime
    timestamp: AWSTimestamp
    url: AWSURL
    phoneno: AWSPhone
    ip: AWSIPAddress
}

type Query {
    getObject(id: ID!): Object
    listObjects: [Object]
}

schema {
    query: Query
    mutation: Mutation
}
```

Here's what a request template for `putObject` might look like. A `putObject` uses a
`PutItem` operation to create or update an item in your Amazon DynamoDB table. Note that this code snippet
doesn't have a configured Amazon DynamoDB table as a data source. This is being used as an example only:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key" : {
        "id": $util.dynamodb.toDynamoDBJson($util.autoId()),
    },
    "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args)
}
```

The response template for `putObject` returns the results:

```
$util.toJson($ctx.result)
```

Here's what a request template for `getObject` might look like. A `getObject` uses a
`GetItem` operation to return a set of attributes for the item given the primary key. Note that this
code snippet doesn't have a configured Amazon DynamoDB table as a data source. This is being used as an example
only:

```
{
    "version": "2017-02-28",
    "operation": "GetItem",
    "key": {
        "id": $util.dynamodb.toDynamoDBJson($ctx.args.id),
    }
}
```

The response template for `getObject` returns the results:

```
$util.toJson($ctx.result)
```

Here's what a request template for `listObjects` might look like. A `listObjects` uses a
`Scan` operation to return one or more items and attributes. Note that this code snippet doesn't have
a configured Amazon DynamoDB table as a data source. This is being used as an example only:

```
{
    "version" : "2017-02-28",
    "operation" : "Scan",
}
```

The response template for `listObjects` returns the results:

```
$util.toJson($ctx.result.items)
```

The following are some examples of using this schema with GraphQL queries:

```
mutation CreateObject {
    putObject(email: "example@example.com"
        json: "{\"a\":1, \"b\":3, \"string\": 234}"
        date: "1970-01-01Z"
        time: "12:00:34."
        datetime: "1930-01-01T16:00:00-07:00"
        timestamp: -123123
        url:"https://amazon.com"
        phoneno: "+1 555 764 4377"
        ip: "127.0.0.1/8"
    ) {
        id
        email
        json
        date
        time
        datetime
        url
        timestamp
        phoneno
        ip
    }
}

query getObject {
    getObject(id:"0d97daf0-48e6-4ffc-8d48-0537e8a843d2"){
        email
        url
        timestamp
        phoneno
        ip
    }
}

query listObjects {
    listObjects {
        json
        date
        time
        datetime
    }
}
```
