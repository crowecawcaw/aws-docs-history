

# Trackers quota and usage
<a name="trackers-quotas"></a>

This topic provides a summary of rate limits and quotas for Amazon Location Service trackers.

**Note**  
If you require a higher quota, you can use the Service Quotas console to [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) for adjustable quotas. When requesting a quota increase, select the Region you require the quota increase in, since most quotas are specific to the AWS Region. You can request up to twice the default limit for each API.  
For requests that exceed twice the default limit, your request will submit a support ticket. You can also connect to your premium support team. There are no direct charges for quota increase requests, but higher usage levels may lead to increased service costs based on the additional resources consumed. See [Manage quotas with Service Quotas](manage-quotas.md) for more information.

Service Quotas are maximum number of resources you can have per AWS account and AWS Region. Amazon Location Service denies additional requests that exceed the service quota. 

## Resources
<a name="tracker-quota-resources"></a>


| API name | Default | Max adjustable limit | 
| --- | --- | --- | 
| Tracker resources per account | 500 | 1000<br />If you need more than this, [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact the support team. | 
| Tracker consumers per tracker | 5 | Max adjustable limit is not applicable.<br />Contact the support team. | 

## CRUD API
<a name="tracker-quota-crud"></a>

**Note**  
If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact the support team.


| API name | Default | Max adjustable limit | 
| --- | --- | --- | 
| [AssociateTrackerConsumer](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_AssociateTrackerConsumer.html) | 10 | 20 | 
| [CreateTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_CreateTracker.html) | 10 | 20 | 
| [DeleteTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DeleteTracker.html) | 10 | 20 | 
| [DescribeTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DescribeTracker.html) | 10 | 20 | 
| [DisassociateTrackerConsumer](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DisassociateTrackerConsumer.html) | 10 | 20 | 
| [ListTrackerConsumers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackerConsumers.html) | 10 | 20 | 
| [ListTrackers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackers.html) | 10 | 20 | 
| [UpdateTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_UpdateTracker.html) | 10 | 20 | 

## Data API
<a name="tracker-quota-data"></a>

**Note**  
If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact the support team.


| API name | Default | Max adjustable limit | 
| --- | --- | --- | 
| [BatchGetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchGetDevicePosition.html) | 50 | 100 | 
| [BatchUpdateDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchUpdateDevicePosition.html) | 50 | 100 | 
| [GetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePosition.html) | 50 | 100 | 
| [GetDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePositionHistory.html) | 50 | 100 | 
| [BatchDeleteDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistory.html) | 50 | 100 | 
| [ListDevicePositions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListDevicePositions.html) | 50 | 100 | 

## Other usage limits
<a name="tracker-quota-other"></a>

