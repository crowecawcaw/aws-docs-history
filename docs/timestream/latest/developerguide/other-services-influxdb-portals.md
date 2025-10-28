For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# InfluxDB portals

Amazon Timestream for InfluxDB, based on InfluxDB 2.7 Open Source, utilizes long-lived access tokens for
authentication. Organizations with stringent security requirements can enhance their
token management through custom implementation of rotation and expiration mechanisms.
For environments requiring advanced security protocols, especially those with public
internet-exposed API endpoints, implementing additional token management strategies
becomes essential. You can address these security considerations through Ockam’s
InfluxDB portals, which provide comprehensive token management capabilities for InfluxDB
deployments.

InfluxDB portals allow you to establish a private connection, with enhanced
authentication and authorization controls, between any InfluxDB client and Amazon Timestream for InfluxDB
API endpoints by creating an InfluxDB portal powered by [Ockam](https://www.ockam.io/ "https://www.ockam.io/"). Portals enable you to:

- Privately access Amazon Timestream for InfluxDB API operations over mutually authenticated and
  encrypted connections without the need for a VPN or AWS Direct Connect connection.
- Automatically distribute and rotate short-lived least privilege API tokens to
  InfluxDB clients. The built-in lease manager significantly reduces the risk
  associated with using the default InfluxDB approach of long-lived access tokens
  by dynamically assigning each client a unique access token with a short
  time-to-live (TTL).
- Have cryptographic guarantees of data privacy, data integrity, and authenticity
  thanks to the mutually authenticated end-to-end encryption.

Amazon Timestream for InfluxDB endpoints do not need public IP addresses. All clients automatically get
unique short-lived API tokens. Traffic between your InfluxDB and clients is encrypted
using unique encryption keys per client.

For more information on using InfluxDB Portals for secure connectivity and enhanced
authentication, see Ockam’s guide to [Secure token
management for Amazon Timestream for InfluxDB](https://www.ockam.io/blog/amazon-influxdb-token-management "https://www.ockam.io/blog/amazon-influxdb-token-management").
