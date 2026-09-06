

# Places quotas and usage
<a name="places-quota-usage"></a>

Amazon Location Service places quotas on API usage to manage service capacity and prevent over utilization. These quotas can be adjusted through the AWS service quotas console or by contacting support. This section covers the service quotas for Place APIs and API usage limits, including how to request increases and other related information.

## Service Quota
<a name="service-quota"></a>

Amazon Location Service sets default quotas for APIs to help manage service capacity, which can be viewed in the AWS Service Quotas management console. You can request an increase in Amazon Location Service quotas through the self-service console (links are shown in the following table), for up to 2x the default limit for each API. For quota limits exceeding 2x the default limit, request in the [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) and it will submit a support ticket. Alternatively, you can connect with your premium support team. There are no direct charges for quota increase requests, but higher usage levels may lead to increased service costs based on the additional resources consumed. For more details, see [Manage quotas with Service Quotas](manage-quotas.md).


**Service Quota Limits**  

| API Name | Default | Adjustable Max limit | More than Adjustable Max limit | 
| --- | --- | --- | --- | 
| [Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html) | 100 | 200 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 

## Other Usage Limits
<a name="other-usage-limits"></a>

### Feature Availability
<a name="feature-availability"></a>

Autocomplete is not available in Japan.


**API usage Limits**  

| API Name | Limit | Value | 
| --- | --- | --- | 
| [Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html) | Response payload size after compression | 6MB | 
| [ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html) | Response payload size after compression | 6MB | 
| [Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html) | Response payload size after compression | 6MB | 
| [GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html) | Response payload size after compression | 6MB | 
| [SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html) | Response payload size after compression | 6MB | 
| [SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html) | Response payload size after compression | 6MB | 
| [Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html) | Response payload size after compression | 6MB | 

## Next Steps
<a name="next-steps"></a>

For additional information, see:
+ [Attribution](https://docs.aws.amazon.com/location/latest/developerguide/data-attribution.html): Ensure proper data attribution when using Amazon Location Service data.
+ [SLA](https://aws.amazon.com/location/sla/): Review the Amazon Location Service Service Level Agreement to understand availability guarantees.
+ [Service Terms](https://aws.amazon.com/service-terms/): Familiarize yourself with the legal terms governing the use of Amazon Location Service.