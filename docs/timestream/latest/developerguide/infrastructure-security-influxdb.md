For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Infrastructure security in Amazon Timestream for InfluxDB

As a managed service, Amazon Timestream for InfluxDB is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published control plane API calls to access Timestream for InfluxDB through the network. For more information, see [Control planes and data planes](../../../whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.md"). Clients must
support Transport Layer Security (TLS) 1.2 or later. We recommend TLS 1.2 or 1.3. Clients
must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed by using
an access key ID and a secret access key that is associated with an IAM principal. Or you
can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

Timestream for InfluxDB is architected so that your traffic is isolated to the specific AWS Region that your Timestream for InfluxDB instance resides in.

## Security groups

Security groups control the access that traffic has in and out of a DB instance. By default, network access is turned off to a DB instance. You can specify rules in a security group that allow access from an IP address range, port, or security group. After ingress rules are configured, the same rules apply to all DB instances that are associated with that security group.

For more information, see [Controlling access to a DB instance in a VPC](timestream-for-influxdb-controlling-access.md "timestream-for-influxdb-controlling-access.md").
