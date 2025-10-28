# Elements of an AWS API request

signature

###### Important

Unless you are using the AWS SDKs or CLI, you must write code to calculate
signatures that provide authentication information in your requests. Signature
calculation in AWS Signature Version 4 can be a complex undertaking, and we recommend
that you use the AWS SDKs or CLI whenever possible.

Each HTTP/HTTPS request that uses Signature Version 4 signing must contain these elements.

###### Elements

- [Endpoint specification](#endpoint-specification "#endpoint-specification")
- [Action](#action "#action")
- [Action parameters](#parameters "#parameters")
- [Date](#date "#date")
- [Authentication information](#authentication "#authentication")

## Endpoint specification

Specifies the DNS name of the endpoint to which you send the request. This name
usually contains the service code and the Region. For example, the endpoint for
Amazon DynamoDB in the `us-east-1` Region is
`dynamodb.us-east-1.amazonaws.com`.

For HTTP/1.1 requests, you must include the `Host` header. For HTTP/2
requests, you can include the `:authority` header or the `Host`
header. Use only the `:authority` header for compliance with the HTTP/2
specification. Not all services support HTTP/2 requests.

For the endpoints supported by each service, see [Service
endpoints and quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md") in the _AWS General Reference_.

## Action

Specifies an API action for the service. For example, the DynamoDB
`CreateTable` action or the Amazon EC2 `DescribeInstances`
action.

For the actions supported by each service, see the [Service Authorization Reference](../../../service-authorization/latest/reference/reference.md "../../../service-authorization/latest/reference/reference.md").

## Action parameters

Specifies the parameters for the action specified in the request. Each AWS API
action has a set of required and optional parameters. The API version is usually a
required parameter.

For the parameters supported by an API action, see the API Reference for the
service.

## Date

Specifies the date and time of the request. Including the date and time in a request
helps prevent third parties from intercepting your request and resubmitting it later.
The date that you specify in the credential scope must match the date of your
request.

The time stamp must be in UTC and use the following ISO 8601 format:
*YYYYMMDD*T*HHMMSS*Z. For example,
`20220830T123600Z`. Do not include milliseconds in the time stamp.

You can use a `date` or an `x-amz-date` header, or include
`x-amz-date` as a query parameter. If we can't find an
`x-amz-date` header, then we look for a `date` header.

## Authentication information

Each request that you send must include the following information. AWS uses this
information to ensure the validity and authenticity of the request.

- Algorithm – The algorithm that you're using as part of the signing
  process.
  - SigV4 – Use `AWS4-HMAC-SHA256` to specify Signature Version 4
    with the `HMAC-SHA256` hash algorithm.
  - SigV4a – Use `AWS4-ECDSA-P256-SHA256` to specify the
    `ECDSA-P256-SHA-256` hash algorithm.

- Credential – A string that is formed by concatenating your access key ID
  and your credential scope components.
  - SigV4 – Credential scope includes your access key ID, the date
    in _YYYYMMDD_ format, the Region code, the service
    code, and the `aws4_request` termination string, separated by
    slashes (/). The Region code, service code, and termination string must
    use lowercase characters.

  ```
  `AKIAIOSFODNN7EXAMPLE`/`YYYYMMDD`/`region`/`service`/aws4_request
  ```

  - SigV4a – Credential scope includes the date in YYYYMMDD format,
    the service name, and the `aws4_request` termination string,
    separated by slashes (/). Note that credential scope does not include
    the region as the region is covered in a separate header
    `X-Amz-Region-Set`.

  ```
  `AKIAIOSFODNN7EXAMPLE`/`YYYYMMDD`/`service`/aws4_request
  ```

- Signed headers – The HTTP headers to include in the signature, separated
  by semicolons (;). For example, `host;x-amz-date`.

For SigV4a, you must include a region set header that specifies the set of
regions the request will be valid in. The header `X-Amz-Region-Set`
is specified as a list of comma separated values. The following example shows a
region header that allows a request to be made in both us-east-1 and us-west-1
regions.

```
X-Amz-Region-Set=us-east-1,us-west-1
```

You can use wildcards (\*) in regions to specify multiple regions. In the
following example, the header allows a request to be made in both us-west-1 and
us-west-2.

```
X-Amz-Region-Set=us-west-*
```

- Signature – A hexadecimal-encoded string that represents the calculated
  signature. You must calculate the signature using the algorithm that you
  specified in the `Algorithm` parameter.

For more information, see [Authentication methods](reference_sigv-authentication-methods.md "reference_sigv-authentication-methods.md")
