For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# How VPC endpoints work with Timestream

When you create a VPC endpoint to access either the Timestream Write or Timestream Query SDK,
all requests are routed to endpoints within the Amazon network and do not access the public internet.
More specifically,
your requests are routed to the write and query endpoints of the cell that your account has been mapped to for a given region.
To learn more about Timestream's cellular architecture and cell-specific endpoints, you can refer to
[Cellular architecture](architecture.md#cells "architecture.md#cells").
For example,
suppose that your account has been mapped to `cell1` in `us-west-2`,
and you've set up VPC interface endpoints for writes (`ingest-cell1.timestream.us-west-2.amazonaws.com`)
and queries (`query-cell1.timestream.us-west-2.amazonaws.com`).
In this case, any write requests sent using these endpoints will stay entirely within the Amazon network and will not access the public internet.

## Considerations for Timestream VPC endpoints

Consider the following when creating a VPC endpoint for Timestream:

- Before you set up an interface VPC endpoint for Timestream for LiveAnalytics, ensure that you
  review [Interface
  endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.
- Timestream for LiveAnalytics supports making calls to
  [all of its API actions](API_Reference.md "API_Reference.md") from your VPC.
- VPC endpoint policies are supported for Timestream for LiveAnalytics. By default, full access to
  Timestream for LiveAnalytics is allowed through the endpoint. For more information, see [Controlling access to services with
  VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.
- Because of Timestream's architecture,
  access to both Write and Query actions requires the creation of two VPC interface endpoints, one for each SDK.
  Additionally, you must specify a cell endpoint (you will only be able to create an endpoint for the Timestream cell that you are mapped to).
  Detailed information can be found in the [create an interface VPC endpoint for
  Timestream for LiveAnalytics](VPCEndpoints.md "VPCEndpoints.md") section of this guide.

Now that you understand how Timestream for LiveAnalytics works with VPC endpoints, [create an interface VPC endpoint for
Timestream for LiveAnalytics](VPCEndpoints.md "VPCEndpoints.md").
