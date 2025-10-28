# Making requests to S3 Tables over IPv6

Amazon S3 supports the ability to access S3 buckets using the Internet Protocol version 6 (IPv6), in addition to the IPv4 protocol, using dual-stack endpoints. Dual-stack endpoints resolve to either an IPv6 endpoint or IPv4 endpoint depending on what your network supports.

The following are some things you should know before trying to access S3 Tables over IPv6:

- The client and the network accessing the table bucket must be enabled to use IPv6.
- Your tables client and your S3 client must both have dual-stack enabled.
- If you use IP address filtering IAM policies they must be updated to handle IPv6 addresses. For more information about managing access permissions with IAM, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").
- When using IPv6, server access log files output IP addresses in an IPv6 format. You need to update existing tools, scripts, and software that you use to parse Amazon S3 log files so that they can parse the IPv6 formatted `Remote IP` addresses. For more information, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md").

## Getting started making S3 Tables requests over IPv6

When you make a request to a dual-stack endpoint, the table bucket URL resolves to an IPv6 or an IPv4 address depending on what your network supports. If your network prefers IPv4 requests will automatically use IPv4. If your network prefers IPv6, requests will use IPv6. No configuration change is required other than updating your client or application to enable the dual-stack endpoint.

When using the REST API, you directly access an Amazon S3 endpoint by using the endpoint name (URI). You can access S3 Tables and table buckets through a dual-stack endpoint using the following naming convention:

`s3tables.<region>.api.aws`

For a complete list of endpoints for S3 Tables, see [Amazon Simple Storage Service endpoints and quotas](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md").

When using the AWS CLI, AWS SDKs, and Iceberg clients, you can use a parameter or flag to change to a dual-stack endpoint. You can also specify the dual-stack endpoint directly as an override of the Amazon S3 endpoint in the config file.

You can enable dual-stack endpoint resolution in SDKs or clients by setting the dual-stack flag using the following command:

```
S3TablesClient client = S3TablesClient.builder()
    .region(Region.US_EAST_1)
    .dualstackEnabled(true)
    .build();
```

To use the dual-stack endpoint in the AWS CLI, see [Using dual-stack endpoints from the AWS CLI](../API/dual-stack-endpoints.md#dual-stack-endpoints-cli "../API/dual-stack-endpoints.md#dual-stack-endpoints-cli").

For information on using the dual-stack endpoints for AWS PrivateLink, see, [Using the dual-stack endpoints to access tables and table buckets](s3-tables-VPC.md#s3-tables-dual-stack-endpoints "s3-tables-VPC.md#s3-tables-dual-stack-endpoints").
