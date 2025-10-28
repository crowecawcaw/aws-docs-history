# Amazon EFS API

The Amazon EFS API is a network protocol based on [HTTP (RFC 2616)](https://www.ietf.org/rfc/rfc2616.txt "https://www.ietf.org/rfc/rfc2616.txt"). For each API call, you
make an HTTP request to the region-specific Amazon EFS API endpoint for the AWS Region where you want
to manage file systems. The API uses JSON (RFC 4627) documents for HTTP request/response
bodies.

The Amazon EFS API is an RPC model. In this model, there is a fixed set of operations and the
syntax for each operation is known to clients without any prior interaction. In the following
section, you can find a description of each API operation using an abstract RPC notation. Each
has an operation name that doesn't appear on the wire. For each operation, the topic specifies
the mapping to HTTP request elements.

The specific Amazon EFS operation to which a given request maps is determined by a combination of
the request's method (GET, PUT, POST, or DELETE) and which of the various patterns its
Request-URI matches. If the operation is PUT or POST, Amazon EFS extracts call arguments from the
Request-URI path segment, query parameters, and the JSON object in the request body.

###### Note

Although operation names, such as `CreateFileSystem`, don't appear on the
wire, these names are meaningful in AWS Identity and Access Management (IAM) policies. For more information, see
[Identity and access management for Amazon EFS](security-iam.md "security-iam.md").

The operation name is also used to name commands in command-line tools and elements of the
AWS SDK APIs. For example, there is a AWS CLI command named `create-file-system` that
maps to the `CreateFileSystem` operation.

The operation name also appears in AWS CloudTrail logs for Amazon EFS API calls.

## API endpoints

An endpoint is a URL that serves as an entry point for an AWS web service. Amazon EFS
supports the following endpoint types:

- IPv4 endpoints
- Dual-stack (both IPv4 and IPv6) endpoints
- [FIPS endpoints](../../../general/latest/gr/rande.md#FIPS-endpoints "../../../general/latest/gr/rande.md#FIPS-endpoints")

When you make a request, you can specify the endpoint to use. If you do not specify an
endpoint, the IPv4 endpoint is used by default. To use a different endpoint type, you must
specify it in your request. For examples of how to do this, see [Specifying endpoints](#endpoints-specifying "#endpoints-specifying"). For a table of
available endpoints, see [Amazon EFS endpoints and quotas](../../../general/latest/gr/elasticfilesystem.md "../../../general/latest/gr/elasticfilesystem.md").

### IPv4 endpoints

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all
Regions. The format of the IPv4 endpoint depends on the Region.

- For IPv4 endpoints in the AWS commercial Regions, the format is
  `elasticfilesystem.`region`.amazonaws.com`.

For example, if you specify
`elasticfilesystem.us-west-2.amazonaws.com` as the endpoint, we
direct your request to the US West (Oregon) Region (us-west-2) endpoint.

- For IPv4 endpoints in the China Regions, the format is
  `elasticfilesystem.`region`.amazonaws.com.cn`.

For example, the Amazon EFS API endpoint for the China (Beijing) Region is
`elasticfilesystem.cn-north-1.amazonaws.com.cn`.

### Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a
dual-stack endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address, depending on
the protocol used by your network and client. The format of the dual-stack endpoint depends
on the Region.

- For dual-stack endpoints in the AWS commercial Regions, the format
  is `efs.`aws-region`.api.aws`.

For example, the dual-stack endpoint for the US West (Oregon) Region (us-west-2) is
`efs.eu-west-2.api.aws`.

- For dual-stack endpoints in the China Regions, the format is
  `efs.`region`.api.amazonwebservices.com.cn`.

For example, the dual-stack endpoint for the China (Beijing) Region is
`efs.cn-north-1.api.amazonwebservices.com.cn`.

### Specifying endpoints

The following examples show how to specify an endpoint for the US West (N. California)
Region (us-west-1) using the AWS CLI for Amazon EFS.

IPv4

```
aws efs get-rest-apis --region us-west-1 --endpoint-url https://``elasticfilesystem.us-west-1.amazonaws.com``
```

Dual-stack

```
aws efs get-rest-apis --region us-west-1 --endpoint-url https://`efs.us-west-1.api.aws`
```

## API version

The version of the API being used for a call is identified by the first path segment of
the request URI, and its form is an ISO 8601 date. For example, see [CreateFileSystem](API_CreateFileSystem.md "API_CreateFileSystem.md").

The documentation describes API version 2015-02-01.

## Related topics

The following sections provide descriptions of the API operations, how to create a
signature for request authentication, and how to grant permissions for these API operations
using the IAM policies.

- [Identity and access management for Amazon EFS](security-iam.md "security-iam.md")
- [Actions](API_Operations.md "API_Operations.md")
- [Data Types](API_Types.md "API_Types.md")

## Working with the query API request rate for Amazon EFS

Amazon EFS API requests are throttled for each AWS account on a per-region basis to help
service performance. All Amazon EFS API calls together, whether they originate from an application,
the AWS CLI, or the Amazon EFS console, must not exceed the maximum allowed API request rate. The
maximum API request rate can vary across AWS Regions. API requests made are attributed to
the underlying AWS account.

If an API request exceeds the API request rate for its category, the request returns the
`ThrottlingException` error code. To prevent this error, ensure that your
application doesn't retry API requests at a high rate. You can do this by using care when
polling and by using exponential backoff retries.

### Polling

Your application might need to call an API operation repeatedly to check for an update
in status. Before you start polling, give the request time to potentially complete. When you
begin polling, use an appropriate sleep interval between successive requests. For best
results, use an increasing sleep interval.

### Retries or batch processing

Your application might need to retry an API request after it fails, or to process
multiple resources (for example, all of your Amazon EFS file systems). To lower the rate of API
requests, use an appropriate sleep interval between successive requests. For best results,
use an increasing or variable sleep interval.

### Calculating the sleep interval

When you have to poll or retry an API request, we recommend using an exponential backoff
algorithm to calculate the sleep interval between API calls. The idea behind exponential
backoff is to use progressively longer waits between retries for consecutive error
responses. For more information, and implementation examples of this algorithm, see [Retry behavior](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md")
in the _Amazon Web Services General Reference._
