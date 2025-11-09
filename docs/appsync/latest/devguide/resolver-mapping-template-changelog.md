# AWS AppSync resolver mapping template

changelog

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

Resolver and function mapping templates are versioned. The mapping template version, such
as `2018-05-29`) dictates the following:

- The expected shape of the data source request configuration provided by the request
  template
- The execution behavior of the request mapping template and the response mapping
  template
  Versions are represented using the YYYY-MM-DD format, a later date corresponds to a more
  recent version. This page lists the differences between the mapping template versions
  currently supported in AWS AppSync.

###### Topics

- [Datasource Operation Availability Per Version Matrix](#aws-appsync-resolver-mapping-template-operation-availability-per-version "#aws-appsync-resolver-mapping-template-operation-availability-per-version")
- [Changing the
  Version on a Unit Resolver Mapping Template](#changing-the-version-on-a-unit-resolver-mapping-template "#changing-the-version-on-a-unit-resolver-mapping-template")
- [Changing the Version on a
  Function](#changing-the-version-on-a-function "#changing-the-version-on-a-function")
- [2018-05-29](#aws-appsync-resolver-mapping-template-version-2018-05-29 "#aws-appsync-resolver-mapping-template-version-2018-05-29")
- [2017-02-28](#aws-appsync-resolver-mapping-template-version-2017-02-28 "#aws-appsync-resolver-mapping-template-version-2017-02-28")

## Datasource Operation Availability Per Version Matrix

| Operation/Version Supported | 2017-02-28 | 2018-05-29 |
| --------------------------- | ---------- | ---------- |
| AWS Lambda Invoke           | Yes        | Yes        |
| AWS Lambda BatchInvoke      | Yes        | Yes        |
| None Datasource             | Yes        | Yes        |
| Amazon OpenSearch GET       | Yes        | Yes        |
| Amazon OpenSearch POST      | Yes        | Yes        |
| Amazon OpenSearch PUT       | Yes        | Yes        |
| Amazon OpenSearch DELETE    | Yes        | Yes        |
| Amazon OpenSearch GET       | Yes        | Yes        |
| DynamoDB GetItem            | Yes        | Yes        |
| DynamoDB Scan               | Yes        | Yes        |
| DynamoDB Query              | Yes        | Yes        |
| DynamoDB DeleteItem         | Yes        | Yes        |
| DynamoDB PutItem            | Yes        | Yes        |
| DynamoDB BatchGetItem       | No         | Yes        |
| DynamoDB BatchPutItem       | No         | Yes        |
| DynamoDB BatchDeleteItem    | No         | Yes        |
| HTTP                        | No         | Yes        |
| Amazon RDS                  | No         | Yes        |

**Note**: Only **2018-05-29**
version is currently supported in functions.

## Changing the

Version on a Unit Resolver Mapping Template

For Unit resolvers, the version is specified as part of the body of the request mapping
template. To update the version, simply update the `version` field to the new
version.

For example, to update the version on the AWS Lambda template:

```
{
    "version": "2017-02-28",
    "operation": "Invoke",
    "payload": {
        "field": "getPost",
        "arguments": $utils.toJson($context.arguments)
    }
}
```

You need to update the version field from `2017-02-28` to
`2018-05-29` as follows:

```
{
    "version": "2018-05-29", ## Note the version
    "operation": "Invoke",
    "payload": {
        "field": "getPost",
        "arguments": $utils.toJson($context.arguments)
    }
}
```

## Changing the Version on a

Function

For functions, the version is specified as the `functionVersion` field on the
function object. To update the version, simply update the `functionVersion`.
_Note:_ Currently, only `2018-05-29` is supported for
function.

The following is an example of a CLI command to update an existing function
version:

```
aws appsync update-function \
--api-id REPLACE_WITH_API_ID \
--function-id REPLACE_WITH_FUNCTION_ID \
--data-source-name "PostTable" \
--function-version "2018-05-29" \
--request-mapping-template "{...}" \
--response-mapping-template "\$util.toJson(\$ctx.result)"
```

**Note:** It is recommended to omit the version field from the
function request mapping template as it will not be honored. If you do specify a version
inside a function request mapping template, the version value will be overridden by the
value of the `functionVersion` field.

## 2018-05-29

### Behavior Change

- If the datasource invocation result is `null`, the response mapping
  template is executed.
- If the datasource invocation yields an error, it is now up to you to handle the
  error, the response mapping template evaluated result will **always** be placed inside the GraphQL response `data`
  block.

### Reasoning

- A `null` invocation result has meaning, and in some application use
  cases we might want to handle `null` results in a custom way. For
  example, an application might check if a record exists in an Amazon DynamoDB table
  to perform some authorization check. In this case, a `null` invocation
  result would mean the user might not be authorized. Executing the response mapping
  template now provides the ability to raise an unauthorized error. This behavior
  provides greater control to the API designer.

Given the following response mapping template:

```
$util.toJson($ctx.result)
```

Previously with `2017-02-28`, if `$ctx.result` came back null,
the response mapping template was not executed. With `2018-05-29`, we can now
handle this scenario. For example, we can choose to raise an authorization error as
follows:

```
# throw an unauthorized error if the result is null
#if ( $util.isNull($ctx.result) )
    $util.unauthorized()
#end
$util.toJson($ctx.result)
```

**Note:** Errors coming back from a data source are
sometimes not fatal or even expected, that is why the response mapping template should
be given the flexibility to handle the invocation error and decide whether to ignore it,
re-raise it, or throw a different error.

Given the following response mapping template:

```
$util.toJson($ctx.result)
```

Previously, with `2017-02-28`, in case of an invocation error, the
response mapping template was evaluated and the result was placed automatically in the
`errors` block of the GraphQL response. With `2018-05-29`, we
can now choose what to do with the error, re-raise it, raise a different error, or
append the error while return data.

### Re-raise an Invocation Error

In the following response template, we raise the same error that came back from the
data source.

```
#if ( $ctx.error )
    $util.error($ctx.error.message, $ctx.error.type)
#end
$util.toJson($ctx.result)
```

In case of an invocation error (for example, `$ctx.error` is present) the
response looks like the following:

```
{
    "data": {
        "getPost": null
    },
    "errors": [
        {
            "path": [
                "getPost"
            ],
            "errorType": "DynamoDB:ConditionalCheckFailedException",
            "message": "Conditional check failed exception...",
            "locations": [
                {
                    "line": 5,
                    "column": 5
                }
            ]
        }
    ]
}
```

### Raise a Different Error

In the following response template, we raise our own custom error after processing
the error that came back from the data source.

```
#if ( $ctx.error )
    #if ( $ctx.error.type.equals("ConditionalCheckFailedException") )
        ## we choose here to change the type and message of the error for ConditionalCheckFailedExceptions
        $util.error("Error while updating the post, try again. Error: $ctx.error.message", "UpdateError")
    #else
        $util.error($ctx.error.message, $ctx.error.type)
    #end
#end
$util.toJson($ctx.result)
```

In case of an invocation error (for example, `$ctx.error` is present) the
response looks like the following:

```
{
    "data": {
        "getPost": null
    },
    "errors": [
        {
            "path": [
                "getPost"
            ],
            "errorType": "UpdateError",
            "message": "Error while updating the post, try again. Error: Conditional check failed exception...",
            "locations": [
                {
                    "line": 5,
                    "column": 5
                }
            ]
        }
    ]
}
```

### Append an Error to Return Data

In the following response template, we append the same error that came back from the
data source while returning data back inside the response. This is also known as a
partial response.

```
#if ( $ctx.error )
    $util.appendError($ctx.error.message, $ctx.error.type)
    #set($defaultPost = {id: "1", title: 'default post'})
    $util.toJson($defaultPost)
#else
    $util.toJson($ctx.result)
#end
```

In case of an invocation error (for example, `$ctx.error` is present) the
response looks like the following:

```
{
    "data": {
        "getPost": {
            "id": "1",
            "title: "A post"
        }
    },
    "errors": [
        {
            "path": [
                "getPost"
            ],
            "errorType": "ConditionalCheckFailedException",
            "message": "Conditional check failed exception...",
            "locations": [
                {
                    "line": 5,
                    "column": 5
                }
            ]
        }
    ]
}
```

#### Migrating from _2017-02-28_ to _2018-05-29_

Migrating from **2017-02-28** to **2018-05-29** is straightforward. Change the version field on
the resolver request mapping template or on the function version object. However,
note that **2018-05-29** execution behaves differently
from **2017-02-28**, changes are outlined [here](#aws-appsync-resolver-mapping-template-version-2018-05-29 "#aws-appsync-resolver-mapping-template-version-2018-05-29").

#### Preserving the same execution behavior from _2017-02-28_ to _2018-05-29_

In some cases, it is possible to retain the same execution behavior as the
**2017-02-28** version while executing a **2018-05-29** versioned template.

### Example: DynamoDB PutItem

Given the following **2017-02-28** DynamoDB PutItem
request template:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key": {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "attributeValues" : {
        "baz" : ... typed value
    },
    "condition" : {
       ...
    }
}
```

And the following response template:

```
$util.toJson($ctx.result)
```

Migrating to **2018-05-29** changes these templates as
follows:

```
{
    "version" : "2018-05-29", ## Note the new 2018-05-29 version
    "operation" : "PutItem",
    "key": {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "attributeValues" : {
        "baz" : ... typed value
    },
    "condition" : {
       ...
    }
}
```

And changes the response template as follows:

```
## If there is a datasource invocation error, we choose to raise the same error
## the field data will be set to null.
#if($ctx.error)
  $util.error($ctx.error.message, $ctx.error.type, $ctx.result)
#end

## If the data source invocation is null, we return null.
#if($util.isNull($ctx.result))
  #return
#end

$util.toJson($ctx.result)
```

Now that it is your responsibility to handle errors, we chose to raise the same error
using `$util.error()` that was returned from DynamoDB. You can adapt this
snippet to convert your mapping template to **2018-05-29**,
note that if your response template is different you will have to take account of the
execution behavior changes.

### Example: DynamoDB GetItem

Given the following **2017-02-28** DynamoDB GetItem
request template:

```
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "consistentRead" : true
}
```

And the following response template:

```
## map table attribute postId to field Post.id
$util.qr($ctx.result.put("id", $ctx.result.get("postId")))

$util.toJson($ctx.result)
```

Migrating to **2018-05-29** changes these templates as
follows:

```
{
    "version" : "2018-05-29", ## Note the new 2018-05-29 version
    "operation" : "GetItem",
    "key" : {
        "foo" : ... typed value,
        "bar" : ... typed value
    },
    "consistentRead" : true
}
```

And changes the response template as follows:

```
## If there is a datasource invocation error, we choose to raise the same error
#if($ctx.error)
  $util.error($ctx.error.message, $ctx.error.type)
#end

## If the data source invocation is null, we return null.
#if($util.isNull($ctx.result))
  #return
#end

## map table attribute postId to field Post.id
$util.qr($ctx.result.put("id", $ctx.result.get("postId")))

$util.toJson($ctx.result)
```

In the **2017-02-28** version, if the datasource
invocation was `null`, meaning there is no item in the DynamoDB table that
matches our key, the response mapping template would not execute. It might be fine for
most of the cases, but if you expected the `$ctx.result` to not be
`null`, you now have to handle that scenario.

## 2017-02-28

### Characteristics

- If the datasource invocation result is `null`, the response mapping
  template is **not** executed.
- If the datasource invocation yields an error, the response mapping template is
  executed and the evaluated result is placed inside the GraphQL response
  `errors.data` block.
