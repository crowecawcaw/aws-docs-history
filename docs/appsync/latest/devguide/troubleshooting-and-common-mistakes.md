# Troubleshooting and common mistakes in AWS AppSync

This section discusses some common errors and how to troubleshoot them.

## Incorrect DynamoDB key mapping

If your GraphQL operation returns the following error message, it may be because your
request mapping template structure doesn’t match the Amazon DynamoDB key structure:

```
The provided key element does not match the schema (Service: AmazonDynamoDBv2; Status Code: 400; Error Code
```

For example, if your DynamoDB table has a hash key called `"id"` and your
template says `"PostID"`, as in the following example, this results in the
preceding error, because `"id"` doesn’t match `"PostID"`.

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "PostID" : $util.dynamodb.toDynamoDBJson($ctx.args.id)
    }
}
```

## Missing resolver

If you execute a GraphQL operation, such as a query, and get a null response, this may
be because you don’t have a resolver configured.

For example, if you import a schema that defines a `getCustomer(userId:
 ID!):` field, and you haven’t configured a resolver for this field, then when
you execute a query such as `getCustomer(userId:"ID123"){...}`, you’ll get a
response such as the following:

```
{
    "data": {
    "getCustomer": null
    }
}
```

## Mapping template errors

If your mapping template isn’t properly configured, you’ll receive a GraphQL response
whose `errorType` is `MappingTemplate`. The `message`
field should indicate where the problem is in your mapping template.

For example, if you don’t have an `operation` field in your request mapping
template, or if the `operation` field name is incorrect, you’ll get a
response like the following:

```
{
    "data": {
        "searchPosts": null
    },
    "errors": [
        {
        "path": [
            "searchPosts"
        ],
        "errorType": "MappingTemplate",
        "locations": [
            {
            "line": 2,
            "column": 3
            }
        ],
        "message": "Value for field '$[operation]' not found."
        }
    ]
}
```

## Incorrect return types

The return type from your data source must match the defined type of an object in your
schema, otherwise you may see a GraphQL error like:

```
"errors": [
    {
    "path": [
        "posts"
    ],
    "locations": null,
    "message": "Can't resolve value (/posts) : type mismatch error, expected type LIST, got OBJECT"
    }
]
```

For example this could occur with the following query definition:

```
type Query {
    posts: [Post]
}
```

Which expects a LIST of `[Posts]` objects. For example if you had a Lambda
function in Node.JS with something like the following:

```
const result = { data: data.Items.map(item => { return item ; }) };
callback(err, result);
```

This would throw an error as `result` is an object. You would need to
either change the callback to `result.data` or alter your schema to not
return a LIST.

## Processing invalid requests

When AWS AppSync is unable to process and send a request (due to improper data such as invalid syntax) to the
field resolver, the response payload will return the field data with values set to `null` and any
relevant errors.
