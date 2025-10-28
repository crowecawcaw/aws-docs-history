# Gremlin query status API

To get the status of Gremlin queries, use HTTP `GET` or `POST` to
make a request to the `https://`your-neptune-endpoint`:`port`/gremlin/status` endpoint.

## Gremlin query status request parameters

- **queryId** (_optional_)   –  
  The ID of a running Gremlin query. Only displays the status of the specified query.
- **includeWaiting** (_optional_)   –  
  Returns the status of all waiting queries.

Normally, only running queries are included in the response, but when the
`includeWaiting` parameter is specified, the status of all waiting queries is
also returned.

## Gremlin query status response

syntax

```
{
  "acceptedQueryCount": integer,
  "runningQueryCount": integer,
  "queries": [
    {
      "queryId":"guid",
      "queryEvalStats":
        {
          "waited": integer,
          "elapsed": integer,
          "cancelled": boolean
        },
      "queryString": "string"
    }
  ]
}
```

## Gremlin query status response values

- **acceptedQueryCount**   –  
  The number of queries that have been accepted but not yet completed,
  including queries in the queue.
- **runningQueryCount**   –  
  The number of currently running Gremlin queries.
- **queries**   –  
  A list of the current Gremlin queries.
- **queryId**   –  
  A GUID id for the query. Neptune automatically assigns this ID
  value to each query, or you can also assign your own ID (see
  [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md "features-query-id.md")).
- **queryEvalStats**   –  
  Statistics for this query.
- **subqueries**   –  
  The number of subqueries in this query.
- **elapsed**   –  
  The number of milliseconds the query has been running so far.
- **cancelled**   –  
  True indicates that the query was cancelled.
- **queryString**   –  
  The submitted query. This is truncated to 1024 characters if it
  is longer than that.
- **waited**   –  
  Indicates how long the query waited, in milliseconds.

## Gremlin query status example

The following is an example of the status command using `curl` and HTTP
`GET`.

```
curl https://`your-neptune-endpoint`:`port`/gremlin/status
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
          "waited": 0,
          "elapsed": 23,
          "cancelled": false
        },
      "queryString": "g.V().out().count()"
    }
  ]
}
```
