# Neptune Loader Get-Status requests

## Loader Get-Status request syntax

```
GET https://`your-neptune-endpoint`:`port`/loader?loadId=`loadId`
```

```
GET https://`your-neptune-endpoint`:`port`/loader/`loadId`
```

```
GET https://`your-neptune-endpoint`:`port`/loader
```

## Neptune Loader Get-Status request parameters

- **`loadId`**   –   The ID of the load job.
  If you do not specify a `loadId`, a list of load IDs is returned.
- **`details`**   –   Include details beyond
  overall status.

_Allowed values_: `TRUE`, `FALSE`.

_Default value_: `FALSE`.

- **`errors`**   –   Include the list of errors.

_Allowed values_: `TRUE`, `FALSE`.

_Default value_: `FALSE`.

The list of errors is paged. The `page` and `errorsPerPage`
parameters allow you to page through all the errors.

- **`page`**   –   The error page number.
  Only valid with the `errors` parameter set to `TRUE`.

_Allowed values_: Positive integers.

_Default value_: 1.

- **`errorsPerPage`**   –   The number of errors
  per each page. Only valid with the `errors` parameter set to
  `TRUE`.

_Allowed values_: Positive integers.

_Default value_: 10.

- **`limit`**   –   The number of load ids
  to list. Only valid when requesting a list of load IDs by sending a
  `GET` request with no `loadId` specified.

_Allowed values_: Positive integers from 1 through 100.

_Default value_: 100.

- **`includeQueuedLoads`**   –   An optional
  parameter that can be used to exclude the load IDs of queued load requests when a list of load IDs
  is requested.

###### Note

This parameter is available starting in [Neptune engine release 1.0.3.0](engine-releases-1.0.3.md "engine-releases-1.0.3.md").

By default, the load IDs of all load jobs with status `LOAD_IN_QUEUE` are
included in such a list. They appear before the load IDs of other jobs, sorted by the time they
were added to the queue from most recent to earliest.

_Allowed values_: `TRUE`, `FALSE`.

_Default value_: `TRUE`.
