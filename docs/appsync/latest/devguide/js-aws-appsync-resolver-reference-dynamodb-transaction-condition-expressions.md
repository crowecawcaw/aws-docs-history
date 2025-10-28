# Transaction condition expressions

Transaction condition expressions are available in requests of all four types of
operations in `TransactWriteItems`, namely, `PutItem`,
`DeleteItem`, `UpdateItem`, and
`ConditionCheck`.

For `PutItem`, `DeleteItem`, and `UpdateItem`, the
transaction condition expression is optional. For `ConditionCheck`, the
transaction condition expression is required.

## Example 1

The following transactional `DeleteItem` function request handler does not
have a condition expression. As a result, it deletes the item in DynamoDB.

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { postId } = ctx.args;
  return {
    operation: 'TransactWriteItems',
    transactItems: [
      {
        table: 'posts',
        operation: 'DeleteItem',
        key: util.dynamodb.toMapValues({ postId }),
      }
    ],
  };
}

```

## Example 2

The following transactional `DeleteItem` function request handler does
have a transaction condition expression that allows the operation succeed only if the
author of that post equals a certain name.

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { postId, authorName} = ctx.args;
  return {
    operation: 'TransactWriteItems',
    transactItems: [
      {
        table: 'posts',
        operation: 'DeleteItem',
        key: util.dynamodb.toMapValues({ postId }),
        condition: util.transform.toDynamoDBConditionExpression({
          authorName: { eq: authorName },
        }),
      }
    ],
  };
}
```

If the condition check fails, it will cause `TransactionCanceledException`
and the error detail will be returned in `ctx.result.cancellationReasons`.
Note that by default, the old item in DynamoDB that made condition check fail will be
returned in `ctx.result.cancellationReasons`.

## Specifying a condition

The `PutItem`, `UpdateItem`, and `DeleteItem`
request objects all allow an optional `condition` section to be specified. If
omitted, no condition check is made. If specified, the condition must be true for the
operation to succeed. The `ConditionCheck` must have a `condition`
section to be specified. The condition must be true for the whole transaction to
succeed.

A `condition` section has the following structure:

```
type TransactConditionCheckExpression = {
  expression: string;
  expressionNames?: { [key: string]: string };
  expressionValues?: { [key: string]: string };
  returnValuesOnConditionCheckFailure: boolean;
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

**`returnValuesOnConditionCheckFailure`**

Specify whether to retrieve the item in DynamoDB back when a condition check
fails. The retrieved item will be in
`ctx.result.cancellationReasons[<index>].item`, where
`<index>` is the index of the request item that failed the
condition check. This value defaults to true.
