# Internal API operations

If you monitor API operations, you might see calls to the following internal-only operations:

- `GetDashboardUrl`
- `ListReportsV2`

## Internal API operation: GetDashboardUrl

This operation appears in system logs when invoked by the AMS console. It has no other use case. It is not available for your direct use.

Returns the embedded dashboard URL for the corresponding report. This operation accepts
a `dashboardName` returned by `ListReports`.

**Request syntax**

```
HTTP/1.1 200
Content-type: application/json
{
    "dashboardName": "string"
}
```

**Request elements**

**`dashboardName`**: The name of the Quick Suite
dashboard that the URL is being requested for. The dashboard name is returned in
ListReportsV2.

Type: String

**Response syntax**

```
HTTP/1.1 200
Content-type: application/json
{
  "url": "string"
}
```

**Response elements**

If the action is successful, the service sends back an HTTP 200 response. The following data is returned in JSON format by the service.

**`url`**: Returns the Quick Suite URL for the requested `dashboardName`.

Type: String

**Errors**

For information about the errors that are common to all actions, see
[Common errors](../../../apigateway/latest/api/CommonErrors.md "../../../apigateway/latest/api/CommonErrors.md").

**`BadRequestException`**:

The submitted request is not valid. For example, if the input is incomplete or
incorrect. See the accompanying error message for details.

HTTP Status Code: 400

**`NotFoundException`**:

The requested resource is not found. Make sure that the request URI is correct.

HTTP Status Code: 404

**`TooManyRequestsException`**:

The request has reached its throttling limit. Retry after the specified time
period.

HTTP Status Code: 429

**`UnauthorizedException`**:

The request is denied because the caller has insufficient permissions.

HTTP Status Code: 401

## Internal API operation: ListReportsV2

This API appears in system logs when invoked by the AMS console. It has no other use case. It is not available for your direct use.

Returns a list of operational reports that are available for a specified account.

**Request syntax**

The request doesn't have a request body.

**Response syntax**

```
HTTP/1.1 200
Content-type: application/json
{
  "reportsList": [
    {
        "dashboard": "string",
        "lastUpdatedTime": "string",
    }
  ],
  "reportsType": "string"
}
```

**Response elements**

If the action is successful, the service sends back an HTTP 200 response. The following data is returned in JSON format by the service.

**`reportsList`**: The list of available operational reports.

Type: Array of Dashboard objects

**`reportsType`**: Indicates whether a report is aggregated across multiple accounts or not.

Type: String

**Errors**

For information about the errors that are common to all actions, see
[Common errors](../../../apigateway/latest/api/CommonErrors.md "../../../apigateway/latest/api/CommonErrors.md").

**`BadRequestException`**:

The submitted request is not valid. For example, the input is incomplete or incorrect.
See the accompanying error message for details.

HTTP Status Code: 400

**`NotFoundException`**:

The requested resource is not found. Make sure that the request URI is correct.

HTTP Status Code: 404

**`TooManyRequestsException`**:

The request has reached its throttling limit. Retry after the specified time
period.

HTTP Status Code: 429

**`UnauthorizedException`**:

The request is denied because the caller has insufficient permissions.

HTTP Status Code: 401
