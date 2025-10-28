# SPARQL query cancellation

To get the status of SPARQL queries, use HTTP `GET` or `POST` to
make a request to the `https://`your-neptune-endpoint`:`port`/sparql/status` endpoint.

## SPARQL query cancellation request

parameters

###### cancelQuery

(Required) Tells the status command to cancel a query. This parameter does not
take a value.

###### queryId

(Required) The ID of the running SPARQL query to cancel.

###### silent

(Optional) If `silent=true` then the running query is cancelled and
the HTTP response code is 200. If `silent` is not present or
`silent=false`, the query is cancelled with an HTTP 500 status code.

## SPARQL query cancellation examples

###### Example 1: Cancellation with `silent=false`

The following is an example of the status command using `curl` to cancel a
query with the `silent` parameter set to `false`:

```
curl https://`your-neptune-endpoint`:`port`/sparql/status \
  -d "cancelQuery" \
  -d "queryId=4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47" \
  -d "silent=false"
```

Unless the query has already started streaming results, the cancelled query
would then return an HTTP 500 code with a response like this:

```
{
  "code": "CancelledByUserException",
  "requestId": "4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47",
  "detailedMessage": "Operation terminated (cancelled by user)"
}
```

If the query already returned an HTTP 200 code (OK) and has started streaming
results before being cancelled, the timeout exception information is sent to the
regular output stream.

###### Example 2: Cancellation with `silent=true`

The following is an example of the same status command as above except
with the `silent` parameter now set to `true`:

```
curl https://`your-neptune-endpoint`:`port`/sparql/status \
  -d "cancelQuery" \
  -d "queryId=4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47" \
  -d "silent=true"
```

This command would return the same response as when `silent=false`, but
the cancelled query would now return an HTTP 200 code with a response like this:

```
{
  "head" : {
    "vars" : [ "s", "p", "o" ]
  },
  "results" : {
    "bindings" : [ ]
  }
}
```
