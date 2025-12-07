# Trackers quota and usage

This topic provides a summary of rate limits and quotas for Amazon Location Service trackers.

###### Note

If you require a higher quota, you can use the Service Quotas console to [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") for adjustable quotas. When requesting a
quota increase, select the Region you require the quota increase in, since most
quotas are specific to the AWS Region. You can request up to twice the default
limit for each API.

For requests that exceed twice the default limit, your request will submit a
support ticket. You can also connect to your premium support team. There are no
direct charges for quota increase requests, but higher usage levels may lead to
increased service costs based on the additional resources consumed. See [Manage quotas with Service Quotas](manage-quotas.md "manage-quotas.md") for more information.

Service Quotas are maximum number of resources you can have per AWS account and AWS Region.
Amazon Location Service denies additional requests that exceed the service quota.

## Resources

| API name                      | Default | Max adjustable limit                                                                                                                                                                                                                                                               |
| ----------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tracker resources per account | 500     | 1000<br>If you need more than this, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support<br>team. |
| Tracker consumers per tracker | 5       | Max adjustable limit is not applicable.<br>Contact the support team.                                                                                                                                                                                                               |

## CRUD API

###### Note

If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support team.

| API name                                                                                                                                                                 | Default | Max adjustable limit |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------- |
| [AssociateTrackerConsumer](../APIReference/API_WaypointTracking_AssociateTrackerConsumer.md "../APIReference/API_WaypointTracking_AssociateTrackerConsumer.md")          | 10      | 20                   |
| [CreateTracker](../APIReference/API_WaypointTracking_CreateTracker.md "../APIReference/API_WaypointTracking_CreateTracker.md")                                           | 10      | 20                   |
| [DeleteTracker](../APIReference/API_WaypointTracking_DeleteTracker.md "../APIReference/API_WaypointTracking_DeleteTracker.md")                                           | 10      | 20                   |
| [DescribeTracker](../APIReference/API_WaypointTracking_DescribeTracker.md "../APIReference/API_WaypointTracking_DescribeTracker.md")                                     | 10      | 20                   |
| [DisassociateTrackerConsumer](../APIReference/API_WaypointTracking_DisassociateTrackerConsumer.md "../APIReference/API_WaypointTracking_DisassociateTrackerConsumer.md") | 10      | 20                   |
| [ListTrackerConsumers](../APIReference/API_WaypointTracking_ListTrackerConsumers.md "../APIReference/API_WaypointTracking_ListTrackerConsumers.md")                      | 10      | 20                   |
| [ListTrackers](../APIReference/API_WaypointTracking_ListTrackers.md "../APIReference/API_WaypointTracking_ListTrackers.md")                                              | 10      | 20                   |
| [UpdateTracker](../APIReference/API_WaypointTracking_UpdateTracker.md "../APIReference/API_WaypointTracking_UpdateTracker.md")                                           | 10      | 20                   |

## Data API

###### Note

If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support team.

| API name                                                                                                                                                                                | Default | Max adjustable limit |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [BatchGetDevicePosition](../APIReference/API_WaypointTracking_BatchGetDevicePosition.md "../APIReference/API_WaypointTracking_BatchGetDevicePosition.md")                               | 50      | 100                  |
| [BatchUpdateDevicePosition](../APIReference/API_WaypointTracking_BatchUpdateDevicePosition.md "../APIReference/API_WaypointTracking_BatchUpdateDevicePosition.md")                      | 50      | 100                  |
| [GetDevicePosition](../APIReference/API_WaypointTracking_GetDevicePosition.md "../APIReference/API_WaypointTracking_GetDevicePosition.md")                                              | 50      | 100                  |
| [GetDevicePositionHistory](../APIReference/API_WaypointTracking_GetDevicePositionHistory.md "../APIReference/API_WaypointTracking_GetDevicePositionHistory.md")                         | 50      | 100                  |
| [BatchDeleteDevicePositionHistory](../APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistory.md "../APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistory.md") | 50      | 100                  |
| [ListDevicePositions](../APIReference/API_WaypointTracking_ListDevicePositions.md "../APIReference/API_WaypointTracking_ListDevicePositions.md")                                        | 50      | 100                  |

## Other usage limits
