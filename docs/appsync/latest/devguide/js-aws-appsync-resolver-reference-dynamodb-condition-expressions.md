# Condition expressions

When you mutate objects in DynamoDB by using the `PutItem`,
`UpdateItem`, and `DeleteItem` DynamoDB operations, you can
optionally specify a condition expression that controls whether the request should succeed
or not, based on the state of the object already in DynamoDB before the operation is
performed.

The AWS AppSync DynamoDB function allows a condition expression to be specified in
`PutItem`, `UpdateItem`, and `DeleteItem` request
objects, and also a strategy to follow if the condition fails and the object was not
updated.

## Example 1

The following `PutItem` request object doesn’t have a condition
expression. As a result, it puts an item in DynamoDB even if an item with the same key
already exists, thereby overwriting the existing item.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { foo, bar, ...values} = ctx.args
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({foo, bar}),
    attributeValues: util.dynamodb.toMapValues(values),
  };
}
```

## Example 2

The following `PutItem` object does have a condition expression that
allows the operation succeed only if an item with the same key does
_not_ exist in DynamoDB.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { foo, bar, ...values} = ctx.args
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({foo, bar}),
    attributeValues: util.dynamodb.toMapValues(values),
    condition: { expression: "attribute_not_exists(id)" }
  };
}
```

By default, if the condition check fails, the AWS AppSync DynamoDB function provides an error
for the mutation.

However, the AWS AppSync DynamoDB function offers some additional features to help developers
handle some common edge cases:

- If AWS AppSync DynamoDB functions can determine that the current value in DynamoDB matches
  the desired result, it treats the operation as if it succeeded anyway.
- Instead of returning an error, you can configure the function to invoke a
  custom Lambda function to decide how the AWS AppSync DynamoDB function should handle the
  failure.

These are described in greater detail in the [Handling
a condition check failure](#condition-check "#condition-check") section.

For more information about DynamoDB conditions expressions, see the [DynamoDB ConditionExpressions documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md") .

## Specifying a condition

The `PutItem`, `UpdateItem`, and `DeleteItem`
request objects all allow an optional `condition` section to be specified. If
omitted, no condition check is made. If specified, the condition must be true for the
operation to succeed.

A `condition` section has the following structure:

```
type ConditionCheckExpression = {
  expression: string;
  expressionNames?: { [key: string]: string};
  expressionValues?: { [key: string]: any};
  equalsIgnore?: string[];
  consistentRead?: boolean;
  conditionalCheckFailedHandler?: {
    strategy: 'Custom' | 'Reject';
    lambdaArn?: string;
  };
};
```

The following fields specify the condition:

**`expression`**

The update expression itself. For more information about how to write
condition expressions, see the [DynamoDB ConditionExpressions documentation](../../../amazondynamodb/latest/developerguide/Expressions.md "../../../amazondynamodb/latest/developerguide/Expressions.md") . This field must be
specified.

**`expressionNames`**

The substitutions for expression attribute name placeholders, in the form of
key-value pairs. The key corresponds to a name placeholder used in the
_expression_, and the value must
be a string corresponding to the attribute name of the item in DynamoDB. This
field is optional, and should only be populated with substitutions for
expression attribute name placeholders used in the _expression_.

**`expressionValues`**

The substitutions for expression attribute value placeholders, in the form
of key-value pairs. The key corresponds to a value placeholder used in the
expression, and the value must be a typed value. For more information about how
to specify a “typed value”, see [Type system (request mapping)](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-typed-values-request"). This must be specified. This field
is optional, and should only be populated with substitutions for expression
attribute value placeholders used in the expression.

The remaining fields tell the AWS AppSync DynamoDB function how to handle a condition check
failure:

**`equalsIgnore`**

When a condition check fails when using the `PutItem` operation,
the AWS AppSync DynamoDB function compares the item currently in DynamoDB against the item
it tried to write. If they are the same, it treats the operation as it if
succeeded anyway. You can use the `equalsIgnore` field to specify a
list of attributes that AWS AppSync should ignore when performing that
comparison. For example, if the only difference was a `version`
attribute, it treats the operation as if it succeeded. This field is
optional.

**`consistentRead`**

When a condition check fails, AWS AppSync gets the current value of the item
from DynamoDB using a strongly consistent read. You can use this field to tell the
AWS AppSync DynamoDB function to use an eventually consistent read instead. This field
is optional, and defaults to `true`.

**`conditionalCheckFailedHandler`**

This section allows you to specify how the AWS AppSync DynamoDB function treats a
condition check failure after it has compared the current value in DynamoDB
against the expected result. This section is optional. If omitted, it defaults
to a strategy of `Reject`.

**`strategy`**

The strategy the AWS AppSync DynamoDB function takes after it has compared
the current value in DynamoDB against the expected result. This field is
required and has the following possible values:

**`Reject`**

The mutation fails, and an error is added to the GraphQL
response.

**`Custom`**

The AWS AppSync DynamoDB function invokes a custom Lambda function
to decide how to handle the condition check failure. When the
`strategy` is set to `Custom`, the
`lambdaArn` field must contain the ARN of the
Lambda function to invoke.

**`lambdaArn`**

The ARN of the Lambda function to invoke that determines how the
AWS AppSync DynamoDB function should handle the condition check failure. This
field must only be specified when `strategy` is set to
`Custom`. For more information about how to use this
feature, see [Handling a condition
check failure](#condition-check "#condition-check").

## Handling a condition check failure

When a condition check fails, the AWS AppSync DynamoDB function can pass on the error for the
mutation and the current value of the object by using the `util.appendError`
utility. However, the AWS AppSync DynamoDB function offers some additional features to help
developers handle some common edge cases:

- If AWS AppSync DynamoDB functions can determine that the current value in DynamoDB matches
  the desired result, it treats the operation as if it succeeded anyway.
- Instead of returning an error, you can configure the function to invoke a
  custom Lambda function to decide how the AWS AppSync DynamoDB function should handle the
  failure.

The flowchart for this process is:

![Flowchart showing process for transforming requests with mutation attempts and value checks.](images/DynamoDB-condition-check-failure-handling.png)

### Checking for the desired

result

When the condition check fails, the AWS AppSync DynamoDB function performs a
`GetItem` DynamoDB request to get the current value of the item from
DynamoDB. By default, it uses a strongly consistent read, however this can be configured
using the `consistentRead` field in the `condition` block and
compare it against the expected result:

- For the `PutItem` operation, the AWS AppSync DynamoDB function compares
  the current value against the one it attempted to write, excluding any
  attributes listed in `equalsIgnore` from the comparison. If the
  items are the same, it treats the operation as successful and returns the item
  that was retrieved from DynamoDB. Otherwise, it follows the configured
  strategy.

For example, if the `PutItem` request object looked like the
following:

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { id, name, version} = ctx.args
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({foo, bar}),
    attributeValues: util.dynamodb.toMapValues({ name, version: version+1 }),
    condition: {
      expression: "version = :expectedVersion",
      expressionValues: util.dynamodb.toMapValues({':expectedVersion': version}),
      equalsIgnore: ['version']
    }
  };
}
```

And the item currently in DynamoDB looked like the following:

```
{
   "id" : { "S" : "1" },
   "name" : { "S" : "Steve" },
   "version" : { "N" : 8 }
}
```

The AWS AppSync DynamoDB function would compare the item it tried to write against
the current value, see that the only difference was the `version`
field, but because it’s configured to ignore the `version` field, it
treats the operation as successful and returns the item that was retrieved from
DynamoDB.

- For the `DeleteItem` operation, the AWS AppSync DynamoDB function checks
  to verify that an item was returned from DynamoDB. If no item was returned, it
  treats the operation as successful. Otherwise, it follows the configured
  strategy.
- For the `UpdateItem` operation, the AWS AppSync DynamoDB function does
  not have enough information to determine if the item currently in DynamoDB matches
  the expected result, and therefore follows the configured strategy.

If the current state of the object in DynamoDB is different from the expected result,
the AWS AppSync DynamoDB function follows the configured strategy, to either reject the
mutation or invoke a Lambda function to determine what to do next.

### Following the “reject”

strategy

When following the `Reject` strategy, the AWS AppSync DynamoDB function returns
an error for the mutation.

For example, given the following mutation request:

```
mutation {
    updatePerson(id: 1, name: "Steve", expectedVersion: 1) {
        Name
        theVersion
    }
}
```

If the item returned from DynamoDB looks like the following:

```
{
   "id" : { "S" : "1" },
   "name" : { "S" : "Steve" },
   "version" : { "N" : 8 }
}
```

And the function response handler looks like the following:

```
import { util } from '@aws-appsync/utils';
export function response(ctx) {
  const { version, ...values } = ctx.result;
  const result = { ...values, theVersion: version };
  if (ctx.error) {
    if (error) {
      return util.appendError(error.message, error.type, result, null);
    }
  }
  return result
}
```

The GraphQL response looks like the following:

```
{
  "data": null,
  "errors": [
    {
      "message": "The conditional request failed (Service: AmazonDynamoDBv2; Status Code: 400; Error Code: ConditionalCheckFailedException; Request ID: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ)"
      "errorType": "DynamoDB:ConditionalCheckFailedException",
      ...
    }
  ]
}
```

Also, if any fields in the returned object are filled by other resolvers and the
mutation had succeeded, they won’t be resolved when the object is returned in the
`error` section.

### Following the “custom”

strategy

When following the `Custom` strategy, the AWS AppSync DynamoDB function invokes
a Lambda function to decide what to do next. The Lambda function chooses one of the
following options:

- `reject` the mutation. This tells the AWS AppSync DynamoDB function to
  behave as if the configured strategy was `Reject`, returning an
  error for the mutation and the current value of the object in DynamoDB as
  described in the previous section.
- `discard` the mutation. This tells the AWS AppSync DynamoDB function to
  silently ignore the condition check failure and returns the value in
  DynamoDB.
- `retry` the mutation. This tells the AWS AppSync DynamoDB function to retry
  the mutation with a new request object.

**The Lambda invocation request**

The AWS AppSync DynamoDB function invokes the Lambda function specified in the
`lambdaArn`. It uses the same `service-role-arn` configured
on the data source. The payload of the invocation has the following structure:

```
{
    "arguments": { ... },
    "requestMapping": {... },
    "currentValue": { ... },
    "resolver": { ... },
    "identity": { ... }
}
```

The fields are defined as follows:

**`arguments`**

The arguments from the GraphQL mutation. This is the same as the
arguments available to the request object in
`context.arguments`.

**`requestMapping`**

The request object for this operation.

**`currentValue`**

The current value of the object in DynamoDB.

**`resolver`**

Information about the AWS AppSync resolver or function.

**`identity`**

Information about the caller. This is the same as the identity
information available to the request object in
`context.identity`.

A full example of the payload:

```
{
    "arguments": {
        "id": "1",
        "name": "Steve",
        "expectedVersion": 1
    },
    "requestMapping": {
        "version" : "2017-02-28",
        "operation" : "PutItem",
        "key" : {
           "id" : { "S" : "1" }
        },
        "attributeValues" : {
           "name" : { "S" : "Steve" },
           "version" : { "N" : 2 }
        },
        "condition" : {
           "expression" : "version = :expectedVersion",
           "expressionValues" : {
               ":expectedVersion" : { "N" : 1 }
           },
           "equalsIgnore": [ "version" ]
        }
    },
    "currentValue": {
        "id" : { "S" : "1" },
        "name" : { "S" : "Steve" },
        "version" : { "N" : 8 }
    },
    "resolver": {
        "tableName": "People",
        "awsRegion": "us-west-2",
        "parentType": "Mutation",
        "field": "updatePerson",
        "outputType": "Person"
    },
    "identity": {
        "accountId": "123456789012",
        "sourceIp": "x.x.x.x",
        "user": "AIDAAAAAAAAAAAAAAAAAA",
        "userArn": "arn:aws:iam::123456789012:user/appsync"
    }
}
```

**The Lambda Invocation Response**

The Lambda function can inspect the invocation payload and apply any business
logic to decide how the AWS AppSync DynamoDB function should handle the failure. There are
three options for handling the condition check failure:

- `reject` the mutation. The response payload for this option must
  have this structure:

```
{
    "action": "reject"
}
```

This tells the AWS AppSync DynamoDB function to behave as if the configured strategy
was `Reject`, returning an error for the mutation and the current
value of the object in DynamoDB, as described in the section above.

- `discard` the mutation. The response payload for this option must
  have this structure:

```
{
    "action": "discard"
}
```

This tells the AWS AppSync DynamoDB function to silently ignore the condition check
failure and returns the value in DynamoDB.

- `retry` the mutation. The response payload for this option must have
  this structure:

```
{
    "action": "retry",
    "retryMapping": { ... }
}
```

This tells the AWS AppSync DynamoDB function to retry the mutation with a new
request object. The structure of the `retryMapping` section depends
on the DynamoDB operation, and is a subset of the full request object for that
operation.

For `PutItem`, the `retryMapping` section has the
following structure. For a description of the `attributeValues`
field, see [PutItem](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-putitem "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-putitem").

```
{
    "attributeValues": { ... },
    "condition": {
        "equalsIgnore" = [ ... ],
        "consistentRead" = true
    }
}
```

For `UpdateItem`, the `retryMapping` section has the
following structure. For a description of the `update` section, see
[UpdateItem](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem").

```
{
    "update" : {
        "expression" : "someExpression"
        "expressionNames" : {
            "#foo" : "foo"
        },
        "expressionValues" : {
            ":bar" : ... typed value
        }
    },
    "condition": {
        "consistentRead" = true
    }
}
```

For `DeleteItem`, the `retryMapping` section has the
following structure.

```
{
    "condition": {
        "consistentRead" = true
    }
}
```

There is no way to specify a different operation or key to work on. The
AWS AppSync DynamoDB function only allows retries of the same operation on the same
object. Also, the `condition` section doesn’t allow a
`conditionalCheckFailedHandler` to be specified. If the retry
fails, the AWS AppSync DynamoDB function follows the `Reject`
strategy.

Here is an example Lambda function to deal with a failed `PutItem`
request. The business logic looks at who made the call. If it was made by
`jeffTheAdmin`, it retries the request, updating the
`version` and `expectedVersion` from the item currently in
DynamoDB. Otherwise, it rejects the mutation.

```
exports.handler = (event, context, callback) => {
    console.log("Event: "+ JSON.stringify(event));

    // Business logic goes here.

    var response;
    if ( event.identity.user == "jeffTheAdmin" ) {
        response = {
            "action" : "retry",
            "retryMapping" : {
                "attributeValues" : event.requestMapping.attributeValues,
                "condition" : {
                    "expression" : event.requestMapping.condition.expression,
                    "expressionValues" : event.requestMapping.condition.expressionValues
                }
            }
        }
        response.retryMapping.attributeValues.version = { "N" : event.currentValue.version.N + 1 }
        response.retryMapping.condition.expressionValues[':expectedVersion'] = event.currentValue.version

    } else {
        response = { "action" : "reject" }
    }

    console.log("Response: "+ JSON.stringify(response))
    callback(null, response)
};
```
