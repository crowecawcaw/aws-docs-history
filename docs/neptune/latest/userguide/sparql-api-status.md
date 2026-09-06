

# SPARQL query status API
<a name="sparql-api-status"></a>

To get the status of SPARQL queries, use HTTP `GET` or `POST` to make a request to the `https://{{your-neptune-endpoint}}:{{port}}/sparql/status` endpoint. 

## SPARQL query status request parameters
<a name="sparql-api-status-get-request"></a>

**queryId (optional)**  
The ID of a running SPARQL query. Only displays the status of the specified query.

## SPARQL query status response syntax
<a name="sparql-api-status-get-response-syntax"></a>

```
{
    "acceptedQueryCount": {{integer}},
    "runningQueryCount": {{integer}},
    "queries": [
      {
        "queryId":"{{guid}}",
        "queryEvalStats":
          {
            "subqueries": {{integer}},
            "elapsed": {{integer}},
            "cancelled": {{boolean}}
          },
        "queryString": "{{string}}"
      }
    ]
}
```

## SPARQL query status response values
<a name="sparql-api-status-get-response-values"></a>

**acceptedQueryCount**  
The number of queries accepted since the last restart of the Neptune engine.

**runningQueryCount**  
The number of currently running SPARQL queries.

**queries**  
A list of the current SPARQL queries.

**queryId**  
A GUID id for the query. Neptune automatically assigns this ID value to each query, or you can also assign your own ID (see [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md)). 

**queryEvalStats**  
Statistics for this query.

**subqueries**  
Number of subqueries in this query.

**elapsed**  
The number of milliseconds the query has been running so far.

**cancelled**  
True indicates that the query was cancelled.

**queryString**  
The submitted query.

## SPARQL query status example
<a name="sparql-api-status-get-example"></a>

The following is an example of the status command using `curl` and HTTP `GET`.

```
curl https://{{your-neptune-endpoint}}:{{port}}/sparql/status
```

This output shows a single running query.

```
{
    "acceptedQueryCount":9,
    "runningQueryCount":1,
    "queries": [
        {
            "queryId":"fb34cd3e-f37c-4d12-9cf2-03bb741bf54f",
            "queryEvalStats":
                {
                    "subqueries": 0,
                    "elapsed": 29256,
                    "cancelled": false
                },
            "queryString": "SELECT ?s ?p ?o WHERE {?s ?p ?o}"
        }
    ]
}
```