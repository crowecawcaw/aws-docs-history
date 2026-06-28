# Making API requests

Query requests for the Amazon Verified Permissions are HTTP or HTTPS requests that use the
`POST` method.

## Verified Permissions endpoints

An _endpoint_ is a URL that serves as an entry point
for a web service. You can select an appropriate AWS Region endpoint when you make
your requests to reduce latency. For information about the endpoints used by Verified Permissions,
see [Amazon Verified Permissions](../../../general/latest/gr/verified-permissions.md "../../../general/latest/gr/verified-permissions.md") in the _Amazon Web Services General Reference_.

## Request parameters

Amazon Verified Permissions uses a JSON-based protocol. You pass request parameters as JSON in the
body of your HTTP request. Lists are represented as JSON arrays. For more information,
see [Common Parameters](../apireference/CommonParameters.md "../apireference/CommonParameters.md") in the
_Amazon Verified Permissions API Reference_.

## Request identifiers

In every response, AWS returns a request ID via the
`x-amzn-RequestId` HTTP response header. This string is a unique
identifier that AWS assigns to provide tracking information. Although the request ID
is included in every response, it isn't listed on the individual API documentation
pages to improve readability and reduce redundancy.

## Query API authentication

You send query requests over HTTPS. You must include a signature in every query
request. For more information about creating and including a signature, see [Signing AWS API Requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md")
in the _Amazon Web Services General Reference_.

## Available libraries

AWS provides libraries, sample code, tutorials, and other resources for software
developers who prefer to build applications using language-specific APIs instead of the
command-line tools and Query API. These libraries provide basic functions (not included
in the APIs), such as request authentication, request retries, and error handling so
that it's easier to get started. Verified Permissions libraries and resources are available for the
following languages and platforms:

- [AWS SDK for Go](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/verifiedpermissions "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/verifiedpermissions")
- [AWS SDK for Java 2.x](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/verifiedpermissions/package-summary.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/verifiedpermissions/package-summary.html")
- [AWS SDK for Java 1.x](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/verifiedpermissions/package-summary.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/verifiedpermissions/package-summary.md")
- [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/latest/AWS/VerifiedPermissions.md "../../../AWSJavaScriptSDK/latest/AWS/VerifiedPermissions.md")
- [AWS SDK for .NET](../../../sdkfornet/v3/apidocs/items/VerifiedPermissions/NVerifiedPermissions.md "../../../sdkfornet/v3/apidocs/items/VerifiedPermissions/NVerifiedPermissions.md")
- [AWS SDK for PHP](../../../aws-sdk-php/v3/api/api-verifiedpermissions-2022-07-28.md "../../../aws-sdk-php/v3/api/api-verifiedpermissions-2022-07-28.md")
- [AWS SDK for Python (Boto)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html")
- [AWS SDK for Ruby](https://github.com/aws/aws-sdk-ruby/tree/version-3/apis/verifiedpermissions/2021-12-01 "https://github.com/aws/aws-sdk-ruby/tree/version-3/apis/verifiedpermissions/2021-12-01")

For more information about libraries and sample code in all languages, see [Sample Code & Libraries](../../../code-library.md "../../../code-library.md").

## Making API requests using the `POST` method

If you don't use one of the AWS SDKs, you can make Verified Permissions requests over HTTPS
using the `POST` request method. The `POST` method requires that
you specify the operation in the header of the request and provide the data for the
operation in JSON format in the body of the request.

| Header name        | Header value                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Host`             | The Amazon Verified Permissions endpoint. For example:<br>`verifiedpermissions.us-east-1.amazonaws.com`                                                                                                                                                                                                                                                                                                     |
| `X-Amz-Date`       | You must provide the timestamp in either the HTTP Date header or<br>the AWS *x-amz-date<br>• header. Some HTTP client<br>libraries don't let you set the Date header. When an<br>*x-amz-date<br>• header is present, the system<br>ignores any Date header during the request authentication.<br>The *x-amz-date<br>• header must be specified in<br>ISO 8601 basic format. For example: `20130315T092054Z` |
| `Authorization`    | The set of authorization parameters that AWS uses to ensure the<br>validity and authenticity of the request. For more information about<br>constructing this header, see [Signature Version 4<br>Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the<br>_Amazon Web Services General Reference_.                                 |
| `X-Amz-Target`     | Specifies the Verified Permissions operation that you want to perform.<br>`VerifiedPermissions.`API_Name``<br>For example, to call the `CreatePolicy` operation, use<br>the following target value.<br>`VerifiedPermissions.CreatePolicy`                                                                                                                                                                   |
| `Content-Type`     | Specifies the input format. Use the following value.<br>`application/x-amz-json-1.0`                                                                                                                                                                                                                                                                                                                        |
| `Accept`           | Specifies the response format. Use the following value.<br>`application/x-amz-json-1.0`                                                                                                                                                                                                                                                                                                                     |
| `Content-Length`   | Size of the payload in bytes.                                                                                                                                                                                                                                                                                                                                                                               |
| `Content-Encoding` | Specifies the encoding format of the input and output. Use the<br>following value.<br>`amz-1.0`                                                                                                                                                                                                                                                                                                             |

The following is an example header for an HTTP request to return a list of all
policies in the specified policy store in the AWS account where the
`Principal` references a `User` named `alice`. In
this example, the `Authorization` line is word-wrapped here for easier
reading. Don't word wrap it in your actual request.

```
POST / HTTP/1.1
Host: verifiedpermissions.us-east-1.amazonaws.com
X-Amz-Date: 20230101T200059Z
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.0
X-Amz-Target: VerifiedPermissions.ListPolicies
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "PolicyStoreId": "PSExAmPLE222222222",
    "Filter": {
        "Principal": {
            "Id": {
                "EntityType": "User",
                "EntityId": "alice"
            }
        }
    }
}
```
