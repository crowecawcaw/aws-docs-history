# Neptune Loader Cancel Job

Cancels a load job.

To cancel a job, you must send an HTTP `DELETE` request to the
`https://`your-neptune-endpoint`:`port`/loader` endpoint.
The `loadId` can be appended to the `/loader` URL path, or included as
a variable in the URL.

## Cancel Job request syntax

```
DELETE https://`your-neptune-endpoint`:`port`/loader?loadId=`loadId`
```

```
DELETE https://`your-neptune-endpoint`:`port`/loader/`loadId`
```

## Cancel Job Request Parameters

###### loadId

The ID of the load job.

## Cancel Job Response Syntax

```
no response body
```

###### 200 OK

Successfully deleted load job returns a `200` code.

## Cancel Job Errors

When an error occurs, a JSON object is returned in the `BODY` of the
response. The `message` object contains a description of the error.

###### Error Categories

- **`Error 400`**   –   An invalid
  `loadId` returns an HTTP `400` bad request error.
  The message describes the error.
- **`Error 500`**   –   A valid request that
  cannot be processed returns an HTTP `500` internal server
  error. The message describes the error.

## Cancel Job Error Messages

The following are possible error messages from the cancel API with a description
of the error.

- `The load with id = `load_id` does not exist or not
active` (HTTP 404)   –   The load was not found. Check the
  value of `id` parameter.
- `Load cancellation is not permitted on a read replica instance.`
  (HTTP 405)   –   Loading is a write operation. Retry load on the
  read/write cluster endpoint.

## Cancel Job Examples

###### Example Request

The following is a request sent via HTTP `DELETE` using the
`curl` command.

```
curl -X DELETE 'https://`your-neptune-endpoint`:`port`/loader/`0a237328-afd5-4574-a0bc-c29ce5f54802`'
```
