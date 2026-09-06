

# Encrypting data in transit
<a name="encryption-in-transit"></a>



AWS provides Transport Layer Security (TLS) encryption for data in motion. You can configure encryption settings for crawlers, ETL jobs, and development endpoints using [security configurations](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html) in AWS Glue. You can turn on AWS Glue Data Catalog encryption via the settings for the Data Catalog.

As of September 4, 2018, AWS KMS (*bring your own key* and *server-side encryption*) for AWS Glue ETL and the AWS Glue Data Catalog is supported.

## Spark Connect encryption in transit
<a name="encryption-in-transit-spark-connect"></a>

When you use Spark Connect with AWS Glue interactive sessions, all communication between your client application and the Spark Connect endpoint is encrypted using TLS 1.3. The Spark Connect data path uses gRPC over HTTP/2, and all traffic is encrypted end-to-end across the following hops:
+ **Client to endpoint** – Your Spark Connect client (pyspark or spark-connect-go) connects to the session endpoint over TLS-encrypted gRPC (HTTP/2). The endpoint terminates TLS using an Application Load Balancer with a TLS 1.3 security policy.
+ **Proxy to compute** – Internal traffic between the reverse proxy and the Spark Connect server running on the session worker is encrypted using TLS via a transit gateway connection.

Spark Connect sessions use short-lived bearer tokens for request authentication. These tokens are encrypted using AES-256-GCM with AWS KMS data keys and have a 5-minute time-to-live. Tokens are returned by the `GetSessionEndpoint` API and must be included in each gRPC request to the Spark Connect endpoint.

Customer data (Spark queries, DataFrames, and results) flows in-transit only through the proxy chain and is not persisted by the proxy infrastructure. At-rest storage of session data on worker volumes uses default Amazon EBS encryption.