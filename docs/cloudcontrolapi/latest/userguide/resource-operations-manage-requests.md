# Managing resource operation

requests with AWS Cloud Control API

Because resource operations are asynchronous, resource requests such as `create-resource` and
`update-resource` return a `ProgressEvent` object that contains information about the current
state of your resource create or update request.

For example, a resource create request might initially return the following `ProgressEvent`
object.

```
{
    "ProgressEvent": {
        "EventTime": "2021-08-09T18:17:15.219Z",
        "TypeName": "AWS::Logs::LogGroup",
        "OperationStatus": "IN_PROGRESS",
        "Operation": "CREATE",
        "Identifier": "LogGroupResourceExample",
        "RequestToken": "5f40c577-3534-4b20-9599-0b0123456789"
    }
}
```

The information returned in the `ProgressEvent` object includes a request token that you can then
use to track or cancel a resource operation request.

###### Note

Resource operation requests expire after seven days.

## Listing active resource

operation requests

Use the `list-resource-requests` command to return a list of active resource operation
requests for an AWS account and AWS Region. You can filter the list by request type and status.

Resource operation requests expire after seven
days.

The following example returns active resource operation requests, but it filters out any resource create
requests that are still in progress.

```
`$` `aws cloudcontrol list-resource-requests --resource-request-status-filter \
 Operations=CREATE,OperationStatuses=IN_PROGRESS`
```

The information returned for each resource operation includes a request token that you can then use to
track or cancel a resource operation request.

```
{
    "ResourceRequestStatusSummaries": [
        {
            "EventTime": "2021-08-09T18:17:16.591Z",
            "TypeName": "AWS::Logs::LogGroup",
            "OperationStatus": "SUCCESS",
            "Operation": "CREATE",
            "Identifier": "LogGroupResourceExample",
            "RequestToken": "5f40c577-3534-4b20-9599-0b0123456789"
        }
    ]
}
```

## Tracking the progress of resource operation

requests

Use the `get-resource-request-status` command to track the progress of your resource operation
request. This command takes the request token included in the `ProgressEvent` object generated during the
initial resource operation request. (You can also retrieve the request token for a resource operation request using
the `list-resource-requests` command.) The `get-resource-request-status` command returns an
updated `ProgressEvent` object containing information on the current state of the request.

See the following example.

```
`$` `aws cloudcontrol get-resource-request-status \
 --request-token 5f40c577-3534-4b20-9599-0b0123456789`
```

## Canceling resource

operation requests

Use the `cancel-resource-request` command to cancel a resource operation request that is
currently in progress. Because you can only perform a single operation on a given resource at a time, there might be
cases where you need to cancel the current resource operation to make the resource available so that another
operation may be performed on it.

Canceling a resource request does not guarantee that Cloud Control API can immediately cancel all resource
operations. Rather, Cloud Control API will stop making further calls to the resource event handler. A single resource
operation request to Cloud Control API might actually consist of multiple calls to the underlying service that provisions the
resource. Because of this, canceling a resource operation request might leave the request partially completed,
resulting in only some of the requested changes being applied to the resource. Cloud Control API doesn't roll back the
resource to its previous state.

Only resource operations requests with a status of `PENDING` or `IN_PROGRESS` can
be canceled.

###### Note

Although calling `CancelResourceRequest` cancels operations performed by Cloud Control API, it
doesn't terminate any asynchronous operations that may have already started on downstream services.
