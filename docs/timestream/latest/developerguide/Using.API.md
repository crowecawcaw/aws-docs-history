

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Using the API
<a name="Using.API"></a>

 In addition to the [SDKs](getting-started-sdks.md), Amazon Timestream for LiveAnalytics provides direct REST API access via the *endpoint discovery pattern*. The endpoint discovery pattern is described below, along with its use cases. 

## The endpoint discovery pattern
<a name="Using-API.endpoint-discovery"></a>

Because Timestream Live Analytics's SDKs are designed to transparently work with the service's architecture, including the management and mapping of the service endpoints, it is recommended that you use the SDKs for most applications. However, there are a few instances where use of the Timestream for LiveAnalytics REST API endpoint discovery pattern is necessary: 
+ You are using [VPC endpoints (AWS PrivateLink) with Timestream for LiveAnalytics](VPCEndpoints.md)
+ Your application uses a programming language that does not yet have SDK support
+ You require better control over the client-side implementation

This section includes information on how the endpoint discovery pattern works, how to implement the endpoint discovery pattern, and usage notes. Select a topic below to learn more. 

**Topics**
+ [The endpoint discovery pattern](#Using-API.endpoint-discovery)
+ [How the endpoint discovery pattern works](Using-API.endpoint-discovery.how-it-works.md)
+ [Implementing the endpoint discovery pattern](Using-API.endpoint-discovery.describe-endpoints.implementation.md)