

# Filters
<a name="js-aws-appsync-resolver-reference-dynamodb-filter"></a>

When querying objects in DynamoDB using the `Query` and `Scan` operations, you can optionally specify a `filter` that evaluates the results and returns only the desired values.

The filter property of a `Query` or `Scan` request has the following structure:

```
type DynamoDBExpression = {
  expression: string;
  expressionNames?: { [key: string]: string};
  expressionValues?: { [key: string]: any};
};
```

The fields are defined as follows:

** `expression` **  
The query expression. For more information about how to write filter expressions, see the [DynamoDB QueryFilter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html) and [DynamoDB ScanFilter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ScanFilter.html) documentation. This field must be specified.

** `expressionNames` **  
The substitutions for expression attribute *name* placeholders, in the form of key-value pairs. The key corresponds to a name placeholder used in the `expression`. The value must be a string that corresponds to the attribute name of the item in DynamoDB. This field is optional, and should only be populated with substitutions for expression attribute name placeholders used in the `expression`.

** `expressionValues` **  
The substitutions for expression attribute *value* placeholders, in the form of key-value pairs. The key corresponds to a value placeholder used in the `expression`, and the value must be a typed value. For more information about how to specify a “typed value”, see [Type system (request mapping)](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html#js-aws-appsync-resolver-reference-dynamodb-typed-values-request). This must be specified. This field is optional, and should only be populated with substitutions for expression attribute value placeholders used in the `expression`.

## Example
<a name="js-id18"></a>

The following example is a filter section for a request, where entries retrieved from DynamoDB are only returned if the title starts with the `title` argument. 

Here we use the `util.transform.toDynamoDBFilterExpression` to automatically create a filter from an object:

```
const filter = util.transform.toDynamoDBFilterExpression({
  title: { beginsWith: 'far away' },
});

const request = {};
request.filter = JSON.parse(filter);
```

This generates the following filter:

```
{
  "filter": {
    "expression": "(begins_with(#title,:title_beginsWith))",
    "expressionNames": { "#title": "title" },
    "expressionValues": {
      ":title_beginsWith": { "S": "far away" }
    }
  }
}
```