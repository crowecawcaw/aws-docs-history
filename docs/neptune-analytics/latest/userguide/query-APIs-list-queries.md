# ListQueries

ListQueries API fetches the list of running/waiting/cancelling queries on the graph.

## ListQueries syntax

```
aws neptune-graph list-queries \
    --graph-identifier <graph-id> \
    --region <region> \
    --max-results <result_count>
    --state [all | running | waiting | cancelling]
```

## ListQueries inputs

- graph-identifier (required)

Type: `String`

Identifier representing your graph.

- region (required)

Type: `String`

Region where the graph is present.

- max-results (required)

Type: `Integer`

The maximum number of results to be fetched by the API.

- state (optional)

Type: `String`

Supported values: all | running | waiting | cancelling

If `state` parameter is not specified, the API fetches all types.

## ListQueries outputs

```
# Sample Response
{
    "queries": [
        {
            "id": "130ab841-8b4b-46c3-afbe-af00274c7fd9",
            "queryString": "MATCH p=(n)-[*]-(m) RETURN p;",
            "waited": 0,
            "elapsed": 1686,
            "state": "RUNNING"
        }
    ]
}
```

The output contains a list of query objects, each containing:

- id: `String` - representing the unique identifier of the query.
- queryString: `String` - The actual query text. The queryString may be truncated if the actual query string
  is too long.
- waited: `Integer` - The time in milliseconds for which the query has waited in the waiting queue before
  being picked up by a worker thread.
- elapsed: `Integer` - The time in milliseconds representing the running time of the query.
- state: Current state of the query (running | waiting | cancelling).

The default list order is queries that are `running`, followed by `waiting` and
`cancelling`.

## ListQueries Examples

AWS CLI

```
aws neptune-graph list-queries \
    --graph-identifier <graph-id> \
    --region us-east-1 \
    --max-results 200
    --state waiting
```

AWSCURL

```
awscurl -X GET "https://<graph-id>.<endpoint>/queries?state=WAITING&maxResults=200" \
   -H "Content-Type: application/x-www-form-urlencoded" \
   --region us-east-1 \
   --service neptune-graph
```
