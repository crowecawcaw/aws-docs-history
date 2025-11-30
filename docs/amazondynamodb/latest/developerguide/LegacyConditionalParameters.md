# AttributesToGet (legacy)

###### Note

We recommend that you use the new expression parameters instead of these legacy parameters whenever possible.
For more information, see [Using expressions in DynamoDB](Expressions.md "Expressions.md").
For specific information on the new parameter replacing this one,
[Use ProjectionExpression instead](#ProjectionExpression.instead "#ProjectionExpression.instead").

The legacy conditional parameter `AttributesToGet` is an array of one or more attributes to retrieve from DynamoDB. If no
attribute names are provided, then all attributes will be returned. If any of the
requested attributes are not found, they will not appear in the result.

`AttributesToGet` allows you to retrieve attributes of type List or Map;
however, it cannot retrieve individual elements within a List or a Map.

Note that `AttributesToGet` has no effect on provisioned
throughput consumption. DynamoDB determines capacity units consumed based on item size,
not on the amount of data that is returned to an application.

## Use _ProjectionExpression_ instead – Example

Suppose you wanted to retrieve an item from the _Music_ table,
but that you only wanted to return some of the attributes. You could use a
`GetItem` request with an `AttributesToGet` parameter, as
in this AWS CLI example:

```
aws dynamodb get-item \
    --table-name Music \
    --attributes-to-get '["Artist", "Genre"]' \
    --key '{
        "Artist": {"S":"No One You Know"},
        "SongTitle": {"S":"Call Me Today"}
    }'

```

You can use a `ProjectionExpression` instead:

```
aws dynamodb get-item \
    --table-name Music \
    --projection-expression "Artist, Genre" \
    --key '{
        "Artist": {"S":"No One You Know"},
        "SongTitle": {"S":"Call Me Today"}
    }'

```
