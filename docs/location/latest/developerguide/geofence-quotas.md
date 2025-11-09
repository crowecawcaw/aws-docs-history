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

| API name                                                                                                                                                    | Default | Max adjustable limit |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [CreateGeofenceCollection](../../previous/APIReference/API_CreateGeofenceCollection.md "../../previous/APIReference/API_CreateGeofenceCollection.md")       | 10      | 20                   |
| [DeleteGeofenceCollection](../../previous/APIReference/API_DeleteGeofenceCollection.md "../../previous/APIReference/API_DeleteGeofenceCollection.md")       | 10      | 20                   |
| [DescribeGeofenceCollection](../../previous/APIReference/API_DescribeGeofenceCollection.md "../../previous/APIReference/API_DescribeGeofenceCollection.md") | 10      | 20                   |
| [ListGeofenceCollections](../../previous/APIReference/API_ListGeofenceCollections.md "../../previous/APIReference/API_ListGeofenceCollections.md")          | 10      | 20                   |
| [UpdateGeofenceCollection](../../previous/APIReference/API_UpdateGeofenceCollection.md "../../previous/APIReference/API_UpdateGeofenceCollection.md")       | 10      | 20                   |

## Data API

###### Note

If you need a higher limit for any of these APIs, [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/geo/quotas") or contact the support team.

| API name                                                                                                                                        | Default | Max adjustable limit |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| [BatchEvaluateGeofences](../../previous/APIReference/API_BatchEvaluateGeofences.md "../../previous/APIReference/API_BatchEvaluateGeofences.md") | 50      | 100                  |
| [PutGeofence](../../previous/APIReference/API_PutGeofence.md "../../previous/APIReference/API_PutGeofence.md")                                  | 50      | 100                  |
| [BatchPutGeofence](../../previous/APIReference/API_BatchPutGeofence.md "../../previous/APIReference/API_BatchPutGeofence.md")                   | 50      | 100                  |
| [ListGeofences](../../previous/APIReference/API_ListGeofences.md "../../previous/APIReference/API_ListGeofences.md")                            | 50      | 100                  |
| [GetGeofence](../../previous/APIReference/API_GetGeofence.md "../../previous/APIReference/API_GetGeofence.md")                                  | 50      | 100                  |
| [BatchDeleteGeofence](../../previous/APIReference/API_BatchDeleteGeofence.md "../../previous/APIReference/API_BatchDeleteGeofence.md")          | 50      | 100                  |

## Other usage limits
