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

| API name                                                                                                                                                       | Default | Max adjustable limit |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [AssociateTrackerConsumer](../../previous/APIReference/API_AssociateTrackerConsumer.md "../../previous/APIReference/API_AssociateTrackerConsumer.md")          | 10      | 20                   |
| [CreateTracker](../../previous/APIReference/API_CreateTracker.md "../../previous/APIReference/API_CreateTracker.md")                                           | 10      | 20                   |
| [DeleteTracker](../../previous/APIReference/API_DeleteTracker.md "../../previous/APIReference/API_DeleteTracker.md")                                           | 10      | 20                   |
| [DescribeTracker](../../previous/APIReference/API_DescribeTracker.md "../../previous/APIReference/API_DescribeTracker.md")                                     | 10      | 20                   |
| [DisassociateTrackerConsumer](../../previous/APIReference/API_DisassociateTrackerConsumer.md "../../previous/APIReference/API_DisassociateTrackerConsumer.md") | 10      | 20                   |
| [ListTrackerConsumers](../../previous/APIReference/API_ListTrackerConsumers.md "../../previous/APIReference/API_ListTrackerConsumers.md")                      | 10      | 20                   |
| [ListTrackers](../../previous/APIReference/API_ListTrackers.md "../../previous/APIReference/API_ListTrackers.md")                                              | 10      | 20                   |
| [UpdateTracker](../../previous/APIReference/API_UpdateTracker.md "../../previous/APIReference/API_UpdateTracker.md")                                           | 10      | 20                   |

## Data API

###### Note

If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support team.

| API name                                                                                                                                                                      | Default | Max adjustable limit |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [BatchGetDevicePosition](../../previous/APIReference/API_BatchGetDevicePosition.md "../../previous/APIReference/API_BatchGetDevicePosition.md")                               | 50      | 100                  |
| [BatchUpdateDevicePosition](../../previous/APIReference/API_BatchUpdateDevicePosition.md "../../previous/APIReference/API_BatchUpdateDevicePosition.md")                      | 50      | 100                  |
| [GetDevicePosition](../../previous/APIReference/API_GetDevicePosition.md "../../previous/APIReference/API_GetDevicePosition.md")                                              | 50      | 100                  |
| [GetDevicePositionHistory](../../previous/APIReference/API_GetDevicePositionHistory.md "../../previous/APIReference/API_GetDevicePositionHistory.md")                         | 50      | 100                  |
| [BatchDeleteDevicePositionHistory](../../previous/APIReference/API_BatchDeleteDevicePositionHistory.md "../../previous/APIReference/API_BatchDeleteDevicePositionHistory.md") | 50      | 100                  |
| [ListDevicePositions](../../previous/APIReference/API_ListDevicePositions.md "../../previous/APIReference/API_ListDevicePositions.md")                                        | 50      | 100                  |

## Other usage limits
