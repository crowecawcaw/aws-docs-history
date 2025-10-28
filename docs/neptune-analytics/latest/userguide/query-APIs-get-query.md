# GetQuery

The GetQuery API can be used to get the status of a specific query request.

## GetQuery inputs

- graph-identifier (required)

Type: `String`

The identifier representing a graph.

- region (required)

Type: `String`

The region where the graph is present.

- query-id (required)

Type: `String`

The id of the query request for which you want to get information.

## GetQuery outputs

- id: The same id used in this request.
- queryString: Non-truncated query string associated to this `query-id`.
- waited: Time in milliseconds this query request had to wait to be executed.
- elapsed: Time in milliseconds the query spent while in execution.
- state: Current state of the query - running | waiting | cancelling.

```
{
    "id" : "d6873456-40a7-44d7-be5c-46b4acfdc171",
    "queryString" : "UNWIND range(1,100000) AS i MATCH (n) RETURN i, n",
    "waited" : 1,
    "elapsed" : 8645,
    "state" : "RUNNING"
}
```

## GetQuery examples

AWS CLI

```
aws neptune-graph get-query \
    --graph-identifier <graph-id> \
    --region <region> \
    --query-id <query-id>
```

AWSCURL

```
awscurl -X GET "https://<graph-id>.<endpoint>/queries/<query-id>" \
   -H "Content-Type: application/x-www-form-urlencoded" \
   --region us-east-1 \
   --service neptune-graph
```
