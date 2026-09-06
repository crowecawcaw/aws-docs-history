

# Neptune Loader Get-Status requests
<a name="load-api-reference-status-requests"></a>

## Loader Get-Status request syntax
<a name="load-api-reference-status-request-syntax"></a>

```
GET https://{{your-neptune-endpoint}}:{{port}}/loader?loadId={{loadId}}
```

```
GET https://{{your-neptune-endpoint}}:{{port}}/loader/{{loadId}}
```

```
GET https://{{your-neptune-endpoint}}:{{port}}/loader
```

## Neptune Loader Get-Status request parameters
<a name="load-api-reference-status-parameters"></a>
+ **`loadId`**   –   The ID of the load job. If you do not specify a `loadId`, a list of load IDs is returned.
+ **`details`**   –   Include details beyond overall status.

  *Allowed values*: `TRUE`, `FALSE`.

  *Default value*: `FALSE`.
+ **`errors`**   –   Include the list of errors.

  *Allowed values*: `TRUE`, `FALSE`.

  *Default value*: `FALSE`.

  The list of errors is paged. The `page` and `errorsPerPage` parameters allow you to page through all the errors.
+ **`page`**   –   The error page number. Only valid with the `errors` parameter set to `TRUE`.

  *Allowed values*: Positive integers.

  *Default value*: 1.
+ **`errorsPerPage`**   –   The number of errors per each page. Only valid with the `errors` parameter set to `TRUE`.

  *Allowed values*: Positive integers.

  *Default value*: 10.
+ **`limit`**   –   The number of load ids to list. Only valid when requesting a list of load IDs by sending a `GET` request with no `loadId` specified.

  *Allowed values*: Positive integers from 1 through 100.

  *Default value*: 100.
+ **`includeQueuedLoads`**   –   An optional parameter that can be used to exclude the load IDs of queued load requests when a list of load IDs is requested.

  By default, the load IDs of all load jobs with status `LOAD_IN_QUEUE` are included in such a list. They appear before the load IDs of other jobs, sorted by the time they were added to the queue from most recent to earliest.

  *Allowed values*: `TRUE`, `FALSE`.

  *Default value*: `TRUE`.