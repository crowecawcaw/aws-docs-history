# Inject a Custom ID Into a Neptune Gremlin or SPARQL Query

By default, Neptune assigns a unique `queryId` value to every query.
You can use this ID to get information about a running query (see [Gremlin query status API](gremlin-api-status.md "gremlin-api-status.md") or [SPARQL query status API](sparql-api-status.md "sparql-api-status.md")), or cancel it (see [Gremlin query cancellation](gremlin-api-status-cancel.md "gremlin-api-status-cancel.md") or [SPARQL query cancellation](sparql-api-status-cancel.md "sparql-api-status-cancel.md")).

Neptune also lets you specify your own `queryId` value for a Gremlin
or SPARQL query, either in the HTTP header, or for a SPARQL query by using the
`queryId` query hint. Assigning your own `queryID` makes it easy
to keep track of a query so as to get status or cancel it.

###### Note

This feature is available starting with [Release 1.0.1.0.200463.0 (2019-10-15)](engine-releases-1.0.1.0.200463.md "engine-releases-1.0.1.0.200463.md").

## Injecting a Custom `queryId` Value Using the HTTP Header

For both Gremlin and SPARQL, the HTTP header can be used to inject your own
`queryId` value into a query.

**Gremlin Example**

```
curl -XPOST https://`your-neptune-endpoint`:`port` \
    -d "{\"gremlin\": \
        \"g.V().limit(1).count()\" , \
        \"queryId\":\"4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47\"  }"
```

**SPARQL Example**

```
curl https://`your-neptune-endpoint`:`port`/sparql \
    -d "query=SELECT * WHERE { ?s ?p ?o } " \
       --data-urlencode \
       "queryId=4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47"
```

## Injecting a Custom `queryId` Value Using a SPARQL Query Hint

Here is an example of how you would use the SPARQL `queryId` query hint
to inject a custom `queryId` value into a SPARQL query:

```
curl https://`your-neptune-endpoint`:`port`/sparql \
    -d "query=PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#> \
       SELECT * WHERE { hint:Query hint:queryId \"4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47\" \
       {?s ?p ?o}}"
```

## Using the `queryId` Value to Check Query Status

**Gremlin Example**

```
curl https://`your-neptune-endpoint`:`port`/gremlin/status \
    -d "queryId=4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47"
```

**SPARQL Example**

```
curl https://`your-neptune-endpoint`:`port`/sparql/status \
    -d "queryId=4d5c4fae-aa30-41cf-9e1f-91e6b7dd6f47"
```
