For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# How the endpoint

discovery pattern works

Timestream is built using a [cellular architecture](architecture.md#cells "architecture.md#cells")
to ensure better scaling and traffic isolation properties. Because each customer
account is mapped to a specific cell in a region, your application must use the
correct cell-specific endpoints that your account has been mapped to. When using the
SDKs, this mapping is transparently handled for you and you do not need to manage
the cell-specific endpoints. However, when directly accessing the REST API, you will
need to manage and map the correct endpoints yourself. This process, the
_endpoint discovery pattern_, is described below:

1. The endpoint discovery pattern starts with a call to the
   `DescribeEndpoints` action (described in the [`DescribeEndpoints`](API_Reference.md "API_Reference.md") section).
2. The endpoint should be cached and reused for the amount of time specified
   by the returned time-to-live (TTL) value (the [`CachePeriodInMinutes`](API_Endpoint.md#timestream-Type-Endpoint-CachePeriodInMinutes.html "API_Endpoint.md#timestream-Type-Endpoint-CachePeriodInMinutes.html")). Calls to the Timestream Live Analytics
   API can then be made for the duration of the TTL.
3. After the TTL expires, a new call to DescribeEndpoints should be made to
   refresh the endpoint (in other words, start over at Step 1).

###### Note

Syntax, parameters and other usage information for the
`DescribeEndpoints` action are described in the [API
Reference](API_DescribeEndpoints.md "API_DescribeEndpoints.md"). Note that the `DescribeEndpoints` action is
available via both SDKs, and is identical for each.

For implementation of the endpoint discovery pattern, see [Implementing the endpoint discovery pattern](Using-API.endpoint-discovery.describe-endpoints.md "Using-API.endpoint-discovery.describe-endpoints.md").
