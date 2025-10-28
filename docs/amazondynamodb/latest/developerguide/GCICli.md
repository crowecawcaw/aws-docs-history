# Working with Global Secondary Indexes in DynamoDB using AWS CLI

You can use the AWS CLI to create an Amazon DynamoDB table with one or more global secondary
indexes, describe the indexes on the table, and perform queries using the indexes.

###### Topics

- [Create a table with a Global Secondary Index](#GCICli.CreateTableWithIndex "#GCICli.CreateTableWithIndex")
- [Add a Global Secondary Index to an existing table](#GCICli.CreateIndexAfterTable "#GCICli.CreateIndexAfterTable")
- [Describe a table with a Global Secondary Index](#GCICli.DescribeTableWithIndex "#GCICli.DescribeTableWithIndex")
- [Query a Global Secondary Index](#GCICli.QueryAnIndex "#GCICli.QueryAnIndex")

## Create a table with a Global Secondary Index

Global secondary indexes may be created at the same time you create a table. To do
this, use the `create-table` parameter and provide your specifications for
one or more global secondary indexes. The following example creates a table named
`GameScores` with a global secondary index called `GameTitleIndex`. The base
table has a partition key of `UserId` and a sort key of
`GameTitle`, allowing you to find an individual user's best score for a
specific game efficiently, whereas the GSI has a partition key of `GameTitle`
and a sort key of `TopScore`, allowing you to quickly find the overall
highest score for a particular game.

```
aws dynamodb create-table \
    --table-name GameScores \
    --attribute-definitions AttributeName=UserId,AttributeType=S \
                            AttributeName=GameTitle,AttributeType=S \
                            AttributeName=TopScore,AttributeType=N  \
    --key-schema AttributeName=UserId,KeyType=HASH \
                 AttributeName=GameTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=5 \
    --global-secondary-indexes \
        "[
            {
                \"IndexName\": \"GameTitleIndex\",
                \"KeySchema\": [{\"AttributeName\":\"GameTitle\",\"KeyType\":\"HASH\"},
                                {\"AttributeName\":\"TopScore\",\"KeyType\":\"RANGE\"}],
                \"Projection\":{
                    \"ProjectionType\":\"INCLUDE\",
                    \"NonKeyAttributes\":[\"UserId\"]
                },
                \"ProvisionedThroughput\": {
                    \"ReadCapacityUnits\": 10,
                    \"WriteCapacityUnits\": 5
                }
            }
        ]"
```

You must wait until DynamoDB creates the table and sets the table status to
`ACTIVE`. After that, you can begin putting data items into the table.
You can use [describe-table](../../../cli/latest/reference/dynamodb/describe-table.md "../../../cli/latest/reference/dynamodb/describe-table.md") to
determine the status of the table creation.

## Add a Global Secondary Index to an existing table

Global secondary indexes may also be added or modified after table creation. To do
this, use the `update-table` parameter and provide your specifications for
one or more global secondary indexes. The following example uses the same schema as the
previous example, but assumes that the table has already been created and we're adding
the GSI later.

```
aws dynamodb update-table \
    --table-name GameScores \
    --attribute-definitions AttributeName=TopScore,AttributeType=N  \
    --global-secondary-index-updates \
        "[
            {
                \"Create\": {
                    \"IndexName\": \"GameTitleIndex\",
                    \"KeySchema\": [{\"AttributeName\":\"GameTitle\",\"KeyType\":\"HASH\"},
                                    {\"AttributeName\":\"TopScore\",\"KeyType\":\"RANGE\"}],
                    \"Projection\":{
                        \"ProjectionType\":\"INCLUDE\",
                        \"NonKeyAttributes\":[\"UserId\"]
                    }
                }
            }
        ]"
```

## Describe a table with a Global Secondary Index

To get information about Global Secondary Indexes on a table, use the
`describe-table` parameter. For each index, you can access its name, key
schema, and projected attributes.

```
aws dynamodb describe-table --table-name GameScores
```

## Query a Global Secondary Index

You can use the `query` operation on a global secondary index in much the same way that you
`query` a table. You must specify the index name, the query criteria for
the index sort key, and the attributes that you want to return. In this example, the
index is `GameTitleIndex` and the index sort key is
`GameTitle`.

The only attributes returned are those that have been projected into the index. You
could modify this query to select non-key attributes too, but this would require table
fetch activity that is relatively expensive. For more information about table fetches,
see [Attribute projections](GSI.md#GSI.Projections "GSI.md#GSI.Projections").

```
aws dynamodb query --table-name GameScores\
    --index-name GameTitleIndex \
    --key-condition-expression "GameTitle = :v_game" \
    --expression-attribute-values '{":v_game":{"S":"Alien Adventure"} }'
```
