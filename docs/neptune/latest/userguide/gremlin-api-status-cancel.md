# Gremlin query cancellation

To get the status of Gremlin queries, use HTTP `GET` or `POST` to
make a request to the `https://`your-neptune-endpoint`:`port`/gremlin/status` endpoint.

## Gremlin query cancellation request parameters

- **cancelQuery**   –  
  Required for cancellation. This parameter has no corresponding value.
- **queryId**   –  
  The ID of the running Gremlin query to cancel.

## Gremlin query cancellation example

The following is an example of the `curl` command to cancel a query.

```
curl https://`your-neptune-endpoint`:`port`/gremlin/status \
  --data-urlencode "cancelQuery" \
  --data-urlencode "queryId=fb34cd3e-f37c-4d12-9cf2-03bb741bf54f"
```

Successful cancellation returns HTTP `200` OK.
