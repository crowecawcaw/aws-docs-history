# Migrating from VTL to JavaScript in AWS AppSync

AWS AppSync allows you to write your business logic for your resolvers and functions using VTL or
JavaScript. With both languages, you write logic that instructs the AWS AppSync service on how to interact
with your data sources. With VTL, you write mapping templates that must evaluate to a valid JSON-encoded
string. With JavaScript, you write request and response handlers that return objects. You don't return a
JSON-encoded string.

For example, take the following VTL mapping template to get an Amazon DynamoDB item:

```
{
    "operation": "GetItem",
    "key": {
        "id": $util.dynamodb.toDynamoDBJson($ctx.args.id),
    }
}
```

The utility `$util.dynamodb.toDynamoDBJson` returns a JSON-encoded string. If
`$ctx.args.id` is set to `<id>`, the template evaluates to a valid JSON-encoded
string:

```
{
    "operation": "GetItem",
    "key": {
        "id": {"S": "<id>"},
    }
}
```

When working with JavaScript, you do not need to print out raw JSON-encoded strings within your code, and
using a utility like `toDynamoDBJson` is not needed. An equivalent example of the mapping template
above is:

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  return {
    operation: 'GetItem',
    key: {id: util.dynamodb.toDynamoDB(ctx.args.id)}
  };
}
```

An alternative is to use `util.dynamodb.toMapValues`, which is the recommended approach to handle
an object of values:

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  return {
    operation: 'GetItem',
    key: util.dynamodb.toMapValues({ id: ctx.args.id }),
  };
}
```

This evaluates to:

```
{
  "operation": "GetItem",
  "key": {
    "id": {
      "S": "<id>"
    }
  }
}
```

###### Note

We recommend using the DynamoDB module with DynamoDB data sources:

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	ddb.get({ key: { id: ctx.args.id } })
}
```

As another example, take the following mapping template to put an item in an Amazon DynamoDB data source:

```
{
    "operation" : "PutItem",
    "key" : {
        "id": $util.dynamodb.toDynamoDBJson($util.autoId()),
    },
    "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args)
}
```

When evaluated, this mapping template string must produce a valid JSON-encoded string. When using
JavaScript, your code returns the request object directly:

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { id = util.autoId(), ...values } = ctx.args;
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({ id }),
    attributeValues: util.dynamodb.toMapValues(values),
  };
}
```

which evaluates to:

```
{
  "operation": "PutItem",
  "key": {
    "id": { "S": "2bff3f05-ff8c-4ed8-92b4-767e29fc4e63" }
  },
  "attributeValues": {
    "firstname": { "S": "Shaggy" },
    "age": { "N": 4 }
  }
}
```

###### Note

We recommend using the DynamoDB module with DynamoDB data sources:

```
import { util } from '@aws-appsync/utils'
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	const { id = util.autoId(), ...item } = ctx.args
	return ddb.put({ key: { id }, item })
}
```
