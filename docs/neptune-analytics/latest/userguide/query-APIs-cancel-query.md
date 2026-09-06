

# CancelQuery
<a name="query-APIs-cancel-query"></a>

CancelQuery cancels a specific query request.

## CancelQuery inputs
<a name="query-APIs-cancel-query-inputs"></a>
+ graph-identifier (required)

  Type: `String`

  The identifier representing a graph.
+ region (required)

  Type: `String`

  The region where the graph is present.
+ query-id (required)

  Type: `String`

  The id of the query request for which you want to cancel.

## CancelQuery outputs
<a name="query-APIs-cancel-query-outputs"></a>

CancelQuery does not have any output.

## CancelQuery examples
<a name="query-APIs-cancel-query-examples"></a>

------
#### [ AWS CLI ]

```
aws neptune-graph cancel-query \
    --graph-identifier <graph-id> \
    --region <region> \
    --query-id <query-id>
```

------
#### [ AWSCURL ]

```
awscurl -X DELETE "https://<graph-id>.<endpoint>/queries/<query-id>"  --region us-east-1 --service neptune-graph
```

------