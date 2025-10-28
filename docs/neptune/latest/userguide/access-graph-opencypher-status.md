# Neptune openCypher status servlet and status endpoint

The openCypher status endpoint provides access to information about queries that
are currently running on the server or waiting to run. It also lets you cancel those
queries. The endpoint is:

```
https://`(the server)`:`(the port number)`/openCypher/status
```

You can use the HTTP `GET` and `POST` methods to get current
status from the server, or to cancel a query. You can also use the `DELETE`
method to cancel a running or waiting query.

## Parameters for status requests

###### Status query parameters

- **`includeWaiting`** (`true` or `false`)   –  
  When set to `true` and other parameters are not present, causes
  status information for waiting queries to be returned as well as for running
  queries.
- **`cancelQuery`**   –  
  Used only with `GET` and `POST` methods, to indicate
  that this is a cancelation request. The `DELETE` method does not need this
  parameter.

The value of the `cancelQuery` parameter is not used, but when
`cancelQuery` is present, the `queryId` parameter is
required, to identify which query to cancel.

- **`queryId`**   –  
  Contains the ID of a specific query.

When used with the `GET` or `POST` method and the
`cancelQuery` parameter is not present, `queryId`
causes status information to be returned for the specific query it identifies.
If the `cancelQuery` parameter is present, then the specific query
that `queryId` identifies is canceled.

When used with the `DELETE` method, `queryId` always
indicates a specific query to be canceled.

- **`silent`**   –  
  Only used when canceling a query. If set to `true`, causes the cancelation
  to happen silently.

## Status request response fields

###### Status response fields if the ID of a specific query is not provided

- **acceptedQueryCount**   –  
  The number of queries that have been accepted but not yet completed, including
  queries in the queue.
- **runningQueryCount**   –  
  The number of currently running openCypher queries.
- **queries**   –  
  A list of the current openCypher queries.

###### Status response fields for a specific query

- **queryId**   –  
  A GUID id for the query. Neptune automatically assigns this ID
  value to each query, or you can also assign your own ID (see
  [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md "features-query-id.md")).
- **queryString**   –  
  The submitted query. This is truncated to 1024 characters if it
  is longer than that.
- **queryEvalStats**   –  
  Statistics for this query:
  - **waited**   –  
    Indicates how long the query waited, in milliseconds.
  - **elapsed**   –  
    The number of milliseconds the query has been running so far.
  - **cancelled**   –  
    `True` indicates that the query was cancelled, or `False`
    that it has not been cancelled.

## Examples of status requests and responses

- **Request for the status of all queries, including
  those waiting:**

```
curl https://`server`:`port`/openCypher/status \
  --data-urlencode "includeWaiting=true"
```

_Response:_

```
{
  "acceptedQueryCount" : 0,
  "runningQueryCount" : 0,
  "queries" : [ ]
}
```

- **Request for the status of running queries,
  **not** including those waiting:**:

```
curl https://`server`:`port`/openCypher/status
```

_Response:_

```
{
  "acceptedQueryCount" : 0,
  "runningQueryCount" : 0,
  "queries" : [ ]
}
```

- **Request for the status of a single query:**

```
curl https://`server`:`port`/openCypher/status \
 --data-urlencode "queryId=eadc6eea-698b-4a2f-8554-5270ab17ebee"
```

_Response:_

```
{
  "queryId" : "eadc6eea-698b-4a2f-8554-5270ab17ebee",
  "queryString" : "MATCH (n1)-[:knows]->(n2), (n2)-[:knows]->(n3), (n3)-[:knows]->(n4), (n4)-[:knows]->(n5), (n5)-[:knows]->(n6), (n6)-[:knows]->(n7), (n7)-[:knows]->(n8), (n8)-[:knows]->(n9), (n9)-[:knows]->(n10) RETURN COUNT(n1);",
  "queryEvalStats" : {
    "waited" : 0,
    "elapsed" : 23463,
    "cancelled" : false
  }
}
```

- **Requests to cancel a query**

1. Using `POST`:

```
curl -X POST https://`server`:`port`/openCypher/status \
  --data-urlencode "cancelQuery" \
  --data-urlencode "queryId=f43ce17b-db01-4d37-a074-c76d1c26d7a9"
```

_Response:_

```
{
  "status" : "200 OK",
  "payload" : true
}
```

2. Using `GET`:

```
curl -X GET https://`server`:`port`/openCypher/status \
  --data-urlencode "cancelQuery" \
  --data-urlencode "queryId=588af350-cfde-4222-bee6-b9cedc87180d"
```

_Response:_

```
{
  "status" : "200 OK",
  "payload" : true
}
```

3. Using `DELETE`:

```
curl -X DELETE \
  -s "https://`server`:`port`/openCypher/status?queryId=b9a516d1-d25c-4301-bb80-10b2743ecf0e"
```

_Response:_

```
{
  "status" : "200 OK",
  "payload" : true
}
```
