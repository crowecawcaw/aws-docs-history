# Neptune Loader Reference

This section describes the `Loader` APIs for Amazon Neptune
that are available from the HTTP endpoint of a Neptune DB instance.

###### Note

See [Neptune Loader Error and Feed Messages](loader-message.md "loader-message.md")
for a list of the error and feed messages returned by the loader in case
of errors.

###### Contents

- [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md")
  - [Neptune Loader Request Syntax](load-api-reference-load.md#load-api-reference-load-syntax "load-api-reference-load.md#load-api-reference-load-syntax")
  - [Neptune Loader Request Parameters](load-api-reference-load.md#load-api-reference-load-parameters "load-api-reference-load.md#load-api-reference-load-parameters")
    - [Special considerations for loading openCypher data](load-api-reference-load.md#load-api-reference-load-parameters-opencypher "load-api-reference-load.md#load-api-reference-load-parameters-opencypher")

  - [Neptune Loader Response Syntax](load-api-reference-load.md#load-api-reference-load-return "load-api-reference-load.md#load-api-reference-load-return")
  - [Neptune Loader Errors](load-api-reference-load-errors.md "load-api-reference-load-errors.md")
  - [Neptune Loader Examples](load-api-reference-load-examples.md "load-api-reference-load-examples.md")

- [Neptune Loader Get-Status API](load-api-reference-status.md "load-api-reference-status.md")
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

- [Neptune Loader Cancel Job](load-api-reference-cancel.md "load-api-reference-cancel.md")
  - [Cancel Job request syntax](load-api-reference-cancel.md#load-api-reference-cancel-syntax "load-api-reference-cancel.md#load-api-reference-cancel-syntax")
  - [Cancel Job Request Parameters](load-api-reference-cancel.md#load-api-reference-cancel-parameters "load-api-reference-cancel.md#load-api-reference-cancel-parameters")
  - [Cancel Job Response Syntax](load-api-reference-cancel.md#load-api-reference-cancel-parameters-response "load-api-reference-cancel.md#load-api-reference-cancel-parameters-response")
  - [Cancel Job Errors](load-api-reference-cancel.md#load-api-reference-cancel-parameters-errors "load-api-reference-cancel.md#load-api-reference-cancel-parameters-errors")
  - [Cancel Job Error Messages](load-api-reference-cancel.md#load-api-reference-cancel-parameters-errors-messages "load-api-reference-cancel.md#load-api-reference-cancel-parameters-errors-messages")
  - [Cancel Job Examples](load-api-reference-cancel.md#load-api-reference-cancel-examples "load-api-reference-cancel.md#load-api-reference-cancel-examples")
