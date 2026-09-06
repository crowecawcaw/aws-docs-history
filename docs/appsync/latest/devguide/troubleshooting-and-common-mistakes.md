

# Troubleshooting and common mistakes in AWS AppSync
<a name="troubleshooting-and-common-mistakes"></a>

This section discusses some common errors and how to troubleshoot them.

## Incorrect DynamoDB key mapping
<a name="incorrect-dynamodb-key-mapping"></a>

If your GraphQL operation returns the following error message, it may be because your request mapping template structure doesn’t match the Amazon DynamoDB key structure:

```
The provided key element does not match the schema (Service: AmazonDynamoDBv2; Status Code: 400; Error Code
```

For example, if your DynamoDB table has a hash key called `"id"` and your template says `"PostID"`, as in the following example, this results in the preceding error, because `"id"` doesn’t match `"PostID"`.

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
<a name="missing-resolver"></a>

If you execute a GraphQL operation, such as a query, and get a null response, this may be because you don’t have a resolver configured.

For example, if you import a schema that defines a `getCustomer(userId: ID!):` field, and you haven’t configured a resolver for this field, then when you execute a query such as `getCustomer(userId:"ID123"){...}`, you’ll get a response such as the following:

```
{
    "data": {
    "getCustomer": null
    }
}
```

If a resolver that you previously configured is missing after you changed your schema, see [Resolver removed when you remove its schema field](#resolver-removed-when-schema-field-removed).

## Mapping template errors
<a name="mapping-template-errors"></a>

If your mapping template isn’t properly configured, you’ll receive a GraphQL response whose `errorType` is `MappingTemplate`. The `message` field should indicate where the problem is in your mapping template.

For example, if you don’t have an `operation` field in your request mapping template, or if the `operation` field name is incorrect, you’ll get a response like the following:

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
<a name="incorrect-return-types"></a>

The return type from your data source must match the defined type of an object in your schema, otherwise you may see a GraphQL error like:

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

Which expects a LIST of `[Posts]` objects. For example if you had a Lambda function in Node.JS with something like the following:

```
const result = { data: data.Items.map(item => { return item ; }) };
callback(err, result);
```

This would throw an error as `result` is an object. You would need to either change the callback to `result.data` or alter your schema to not return a LIST.

## Processing invalid requests
<a name="invalid-requests"></a>

When AWS AppSync is unable to process and send a request (due to improper data such as invalid syntax) to the field resolver, the response payload will return the field data with values set to `null` and any relevant errors.

## Resolver removed when you remove its schema field
<a name="resolver-removed-when-schema-field-removed"></a>

A resolver is attached to a specific field on a type in your schema. If you update your schema to remove a field, or to remove a type, that has a resolver attached to it, AWS AppSync also removes the attached resolver. This keeps your schema and its resolvers consistent.

If you later restore the field (for example, by rolling back a change), the resolver is not restored with it. Requests to the field then return `null` because no resolver is configured for it. For more information, see [Missing resolver](#missing-resolver).

### Interaction with AWS CloudFormation and the AWS CDK
<a name="resolver-removal-and-cloudformation"></a>

When you manage your API with CloudFormation or the AWS CDK, your schema and each resolver are defined as separate resources (for example, `AWS::AppSync::GraphQLSchema` and `AWS::AppSync::Resolver`). When a schema update removes a field, AWS AppSync removes the attached resolver, but this removal is not reflected in your CloudFormation stack. CloudFormation continues to track the resolver as though it still exists. As a result:
+ Rolling back the stack does not recreate the removed resolver.
+ Redeploying an unchanged template does not recreate it, because CloudFormation detects no change to the resolver resource.
+ If the schema again references the field but the resolver is missing, requests to that field return `null`, and a stack operation can fail or stop (for example, with the status `UPDATE_ROLLBACK_FAILED`).

### Recover a removed resolver
<a name="recover-a-removed-resolver"></a>

1. Make sure your schema declares the field that the resolver is attached to.

1. Recreate the resolver. Because CloudFormation doesn't act on a resolver resource whose definition hasn't changed, make a change that causes it to recreate the resource. For example, change the resolver's logical ID, or remove and then re-add the resolver resource in separate deployments. Alternatively, recreate the resolver directly by using the AWS AppSync console, the `CreateResolver` API operation, or the AWS CLI, and then reconcile your template or AWS CDK app.

1. If a stack operation is stopped (for example, with the status `UPDATE_ROLLBACK_FAILED`), recreate the missing resolver so that the operation can complete, and then deploy a known-good template.

### Remove or rename fields safely
<a name="remove-schema-fields-safely"></a>
+ To rename a field, first add the new field and attach its resolver, deploy the change, and then remove the old field.
+ Don't remove a schema field whose resolver you want to keep.
+ When you intentionally remove a field, also remove its resolver resource from your template or AWS CDK app in the same change, so that your CloudFormation state stays consistent.
+ Test schema changes in a development or test environment before you deploy them to production.