# Geofences quotas and usage

This topic provides a summary of rate limits and quotas for Amazon Location Service
Geofences.

###### Note

If you require a higher quota, you can use the Service Quotas console to [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") for adjustable quotas. When requesting a
quota increase, select the Region you require the quota increase in, since most
quotas are specific to the AWS Region. You can request up to twice the default
limit for each API.

For requests that exceed twice the default limit, your request will submit a
support ticket. You can also connect to your premium support team. There are no
direct charges for quota increase requests, but higher usage levels may lead to
increased service costs based on the additional resources consumed. See [Manage quotas with Service Quotas](manage-quotas.md "manage-quotas.md") for more information.

Service Quotas are maximum number of resources you can have per AWS account and AWS
Region. Amazon Location Service denies additional requests that exceed the service quota.

## Resources

| API name                         | Default | Max adjustable limit                                                                                                                                                                                                                                                               |
| -------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Collection resources per account | 1500    | 3000<br>If you need more than this, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support<br>team. |
| Geofences per collection         | 50000   | Contact the support team.                                                                                                                                                                                                                                                          |

## CRUD API

###### Note

If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support team.

| API name                                                                                                                                                                  | Default | Max adjustable limit |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [CreateGeofenceCollection](../APIReference/API_WaypointGeofencing_CreateGeofenceCollection.md "../APIReference/API_WaypointGeofencing_CreateGeofenceCollection.md")       | 10      | 20                   |
| [DeleteGeofenceCollection](../APIReference/API_WaypointGeofencing_DeleteGeofenceCollection.md "../APIReference/API_WaypointGeofencing_DeleteGeofenceCollection.md")       | 10      | 20                   |
| [DescribeGeofenceCollection](../APIReference/API_WaypointGeofencing_DescribeGeofenceCollection.md "../APIReference/API_WaypointGeofencing_DescribeGeofenceCollection.md") | 10      | 20                   |
| [ListGeofenceCollections](../APIReference/API_WaypointGeofencing_ListGeofenceCollections.md "../APIReference/API_WaypointGeofencing_ListGeofenceCollections.md")          | 10      | 20                   |
| [UpdateGeofenceCollection](../APIReference/API_WaypointGeofencing_UpdateGeofenceCollection.md "../APIReference/API_WaypointGeofencing_UpdateGeofenceCollection.md")       | 10      | 20                   |

## Data API

###### Note

If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support team.

| API name                                                                                                                                                      | Default | Max adjustable limit |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [BatchEvaluateGeofences](../APIReference/API_WaypointGeofencing_BatchEvaluateGeofences.md "../APIReference/API_WaypointGeofencing_BatchEvaluateGeofences.md") | 50      | 100                  |
| [PutGeofence](../APIReference/API_WaypointGeofencing_PutGeofence.md "../APIReference/API_WaypointGeofencing_PutGeofence.md")                                  | 50      | 100                  |
| [BatchPutGeofence](../APIReference/API_WaypointGeofencing_BatchPutGeofence.md "../APIReference/API_WaypointGeofencing_BatchPutGeofence.md")                   | 50      | 100                  |
| [ListGeofences](../APIReference/API_WaypointGeofencing_ListGeofences.md "../APIReference/API_WaypointGeofencing_ListGeofences.md")                            | 50      | 100                  |
| [GetGeofence](../APIReference/API_WaypointGeofencing_GetGeofence.md "../APIReference/API_WaypointGeofencing_GetGeofence.md")                                  | 50      | 100                  |
| [BatchDeleteGeofence](../APIReference/API_WaypointGeofencing_BatchDeleteGeofence.md "../APIReference/API_WaypointGeofencing_BatchDeleteGeofence.md")          | 50      | 100                  |

## Other usage limits
