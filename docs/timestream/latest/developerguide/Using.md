For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using the API

In addition to the [SDKs](getting-started-sdks.md "getting-started-sdks.md"), Amazon Timestream for LiveAnalytics provides
direct REST API access via the _endpoint discovery pattern_. The
endpoint discovery pattern is described below, along with its use cases.

## The endpoint discovery pattern

Because Timestream Live Analytics's SDKs are designed to transparently work with the service's
architecture, including the management and mapping of the service endpoints, it is
recommended that you use the SDKs for most applications. However, there are a few
instances where use of the Timestream for LiveAnalytics REST API endpoint discovery pattern is necessary:

- You are using [VPC endpoints (AWS PrivateLink)
  with Timestream for LiveAnalytics](VPCEndpoints.md "VPCEndpoints.md")
- Your application uses a programming language that does not yet have SDK
  support
- You require better control over the client-side implementation

This section includes information on how the endpoint discovery pattern works, how
to implement the endpoint discovery pattern, and usage notes. Select a topic below
to learn more.

###### Topics

- [How the endpoint
  discovery pattern works](Using-API.endpoint-discovery.md "Using-API.endpoint-discovery.md")
- [Implementing the endpoint discovery pattern](Using-API.endpoint-discovery.describe-endpoints.md "Using-API.endpoint-discovery.describe-endpoints.md")
