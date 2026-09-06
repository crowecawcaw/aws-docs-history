

# Geofences quotas and usage
<a name="geofence-quotas"></a>

This topic provides a summary of rate limits and quotas for Amazon Location Service Geofences.

**Note**  
If you require a higher quota, you can use the Service Quotas console to [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) for adjustable quotas. When requesting a quota increase, select the Region you require the quota increase in, since most quotas are specific to the AWS Region. You can request up to twice the default limit for each API.  
For requests that exceed twice the default limit, your request will submit a support ticket. You can also connect to your premium support team. There are no direct charges for quota increase requests, but higher usage levels may lead to increased service costs based on the additional resources consumed. See [Manage quotas with Service Quotas](manage-quotas.md) for more information.

Service Quotas are maximum number of resources you can have per AWS account and AWS Region. Amazon Location Service denies additional requests that exceed the service quota. 

## Resources
<a name="geofence-quota-resources"></a>


| API name | Default | Max adjustable limit | 
| --- | --- | --- | 
| Collection resources per account | 1500 | 3000<br />If you need more than this, [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact the support team. | 
| Geofences per collection | 50000 | Contact the support team. | 

## CRUD API
<a name="geofence-quota-crud"></a>

**Note**  
If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact the support team.


| API name | Default | Max adjustable limit | 
| --- | --- | --- | 
| [CreateGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_CreateGeofenceCollection.html) | 10 | 20 | 
| [DeleteGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DeleteGeofenceCollection.html) | 10 | 20 | 
| [DescribeGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DescribeGeofenceCollection.html) | 10 | 20 | 
| [ListGeofenceCollections](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceCollections.html) | 10 | 20 | 
| [UpdateGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_UpdateGeofenceCollection.html) | 10 | 20 | 

## Data API
<a name="geofence-quota-data"></a>

**Note**  
If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact the support team.


| API name | Default | Max adjustable limit | 
| --- | --- | --- | 
| [BatchEvaluateGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchEvaluateGeofences.html) | 50 | 100 | 
| [PutGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_PutGeofence.html) | 50 | 100 | 
| [BatchPutGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofence.html) | 50 | 100 | 
| [ListGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofences.html) | 50 | 100 | 
| [GetGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GetGeofence.html) | 50 | 100 | 
| [BatchDeleteGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchDeleteGeofence.html) | 50 | 100 | 

## Other usage limits
<a name="geofence-quota-other"></a>

