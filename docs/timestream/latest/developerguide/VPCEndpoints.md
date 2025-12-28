For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Timestream for LiveAnalytics by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access Timestream for LiveAnalytics APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with Timestream for LiveAnalytics APIs. Traffic between your VPC and Timestream for LiveAnalytics
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets. For more information on Interface VPC
endpoints, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

To get started with Timestream for LiveAnalytics and VPC endpoints, we've provided information on specific considerations for Timestream for LiveAnalytics with VPC endpoints,
creating an interface VPC endpoint for Timestream for LiveAnalytics,
creating a VPC endpoint policy for Timestream for LiveAnalytics,
and using the Timestream client (for either the Write or Query SDK) with VPC endpoints..

###### Topics

- [How VPC endpoints work with Timestream](VPCEndpoints.md "VPCEndpoints.md")
- [Creating an interface VPC endpoint for
  Timestream for LiveAnalytics](VPCEndpoints.md "VPCEndpoints.md")
- [Creating a VPC endpoint policy for
  Timestream for LiveAnalytics](VPCEndpoints.md "VPCEndpoints.md")
