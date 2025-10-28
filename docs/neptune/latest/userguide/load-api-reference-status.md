# Neptune Loader Get-Status API

Gets the status of a `loader` job.

To get load status, you must send an HTTP `GET` request to the
`https://`your-neptune-endpoint`:`port`/loader` endpoint. To get the status for a particular load request,
you must include the `loadId` as a URL parameter, or append the `loadId`
to the URL path.

Neptune only keeps track of the most recent 1,024 bulk load jobs, and only stores
the last 10,000 error details per job.

See [Neptune Loader Error and Feed Messages](loader-message.md "loader-message.md")
for a list of the error and feed messages returned by the loader in case
of errors.

###### Contents

- [Neptune Loader Get-Status requests](load-api-reference-status-requests.md "load-api-reference-status-requests.md")
  - [Loader Get-Status request syntax](load-api-reference-status-requests.md#load-api-reference-status-request-syntax "load-api-reference-status-requests.md#load-api-reference-status-request-syntax")
  - [Neptune Loader Get-Status request parameters](load-api-reference-status-requests.md#load-api-reference-status-parameters "load-api-reference-status-requests.md#load-api-reference-status-parameters")

- [Neptune Loader Get-Status Responses](load-api-reference-status-response.md "load-api-reference-status-response.md")
  - [Neptune Loader Get-Status Response JSON layout](load-api-reference-status-response.md#load-api-reference-status-response-layout "load-api-reference-status-response.md#load-api-reference-status-response-layout")
  - [Neptune Loader Get-Status
    overallStatus and failedFeeds response objects](load-api-reference-status-response.md#load-api-reference-status-response-objects "load-api-reference-status-response.md#load-api-reference-status-response-objects")
  - [Neptune Loader Get-Status errors response object](load-api-reference-status-response.md#load-api-reference-status-errors "load-api-reference-status-response.md#load-api-reference-status-errors")
  - [Neptune Loader Get-Status errorLogs response object](load-api-reference-status-response.md#load-api-reference-error-logs "load-api-reference-status-response.md#load-api-reference-error-logs")

- [Neptune Loader Get-Status Examples](load-api-reference-status-examples.md "load-api-reference-status-examples.md")
  - [Example request for load status](load-api-reference-status-examples.md#load-api-reference-status-examples-status-request "load-api-reference-status-examples.md#load-api-reference-status-examples-status-request")
  - [Example request for loadIds](load-api-reference-status-examples.md#load-api-reference-status-examples-loadId-request "load-api-reference-status-examples.md#load-api-reference-status-examples-loadId-request")
  - [Example request for detailed status](load-api-reference-status-examples.md#load-api-reference-status-examples-details-request "load-api-reference-status-examples.md#load-api-reference-status-examples-details-request")

- [Neptune Loader Get-Status errorLogs examples](load-api-reference-error-logs-examples.md "load-api-reference-error-logs-examples.md")
  - [Example detailed status response when errors occurred](load-api-reference-error-logs-examples.md#load-api-reference-status-examples-details-request-errors "load-api-reference-error-logs-examples.md#load-api-reference-status-examples-details-request-errors")
  - [Example of a
    Data prefetch task interrupted error](load-api-reference-error-logs-examples.md#load-api-reference-status-examples-task-interrupted "load-api-reference-error-logs-examples.md#load-api-reference-status-examples-task-interrupted")
