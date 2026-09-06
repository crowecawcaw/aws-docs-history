

# Making API requests
<a name="making-api-requests"></a>

Query requests for the Amazon Verified Permissions are HTTP or HTTPS requests that use the `POST` method.

## Verified Permissions endpoints
<a name="avp-endpoints"></a>

An *endpoint* is a URL that serves as an entry point for a web service. You can select an appropriate AWS Region endpoint when you make your requests to reduce latency. For information about the endpoints used by Verified Permissions, see [Amazon Verified Permissions](https://docs.aws.amazon.com/general/latest/gr/verified-permissions.html) in the *Amazon Web Services General Reference*.

## Request parameters
<a name="request-parameters"></a>

Amazon Verified Permissions uses a JSON-based protocol. You pass request parameters as JSON in the body of your HTTP request. Lists are represented as JSON arrays. For more information, see [Common Parameters](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/CommonParameters.html) in the *Amazon Verified Permissions API Reference*.

## Request identifiers
<a name="request-identifiers"></a>

In every response, AWS returns a request ID via the `x-amzn-RequestId` HTTP response header. This string is a unique identifier that AWS assigns to provide tracking information. Although the request ID is included in every response, it isn't listed on the individual API documentation pages to improve readability and reduce redundancy.

## Query API authentication
<a name="query-authentication"></a>

You send query requests over HTTPS. You must include a signature in every query request. For more information about creating and including a signature, see [Signing AWS API Requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html) in the *Amazon Web Services General Reference*.

## Available libraries
<a name="using-libraries"></a>

AWS provides libraries, sample code, tutorials, and other resources for software developers who prefer to build applications using language-specific APIs instead of the command-line tools and Query API. These libraries provide basic functions (not included in the APIs), such as request authentication, request retries, and error handling so that it's easier to get started. Verified Permissions libraries and resources are available for the following languages and platforms:
+  [AWS SDK for Go](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/verifiedpermissions) 
+  [AWS SDK for Java 2.x](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/verifiedpermissions/package-summary.html) 
+  [AWS SDK for Java 1.x](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/verifiedpermissions/package-summary.html) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/VerifiedPermissions.html) 
+  [AWS SDK for .NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/VerifiedPermissions/NVerifiedPermissions.html) 
+  [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-verifiedpermissions-2022-07-28.html) 
+  [AWS SDK for Python (Boto)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html) 
+  [AWS SDK for Ruby](https://github.com/aws/aws-sdk-ruby/tree/version-3/apis/verifiedpermissions/2021-12-01) 

For more information about libraries and sample code in all languages, see [Sample Code & Libraries](https://docs.aws.amazon.com/code-library).

## Making API requests using the `POST` method
<a name="avp-API-requests-using-post-method"></a>

If you don't use one of the AWS SDKs, you can make Verified Permissions requests over HTTPS using the `POST` request method. The `POST` method requires that you specify the operation in the header of the request and provide the data for the operation in JSON format in the body of the request.


| Header name | Header value | 
| --- | --- | 
| Host | The Amazon Verified Permissions endpoint. For example: `verifiedpermissions.us-east-1.amazonaws.com`  | 
| X-Amz-Date | You must provide the timestamp in either the HTTP Date header or the AWS *x-amz-date* header. Some HTTP client libraries don't let you set the Date header. When an *x-amz-date* header is present, the system ignores any Date header during the request authentication.<br />The *x-amz-date* header must be specified in ISO 8601 basic format. For example: `20130315T092054Z`  | 
| Authorization | The set of authorization parameters that AWS uses to ensure the validity and authenticity of the request. For more information about constructing this header, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon Web Services General Reference*. | 
| X-Amz-Target | Specifies the Verified Permissions operation that you want to perform. <br />`VerifiedPermissions.{{API_Name}}`<br />For example, to call the `CreatePolicy` operation, use the following target value.<br />`VerifiedPermissions.CreatePolicy` | 
| Content-Type | Specifies the input format. Use the following value.<br />`application/x-amz-json-1.0` | 
| Accept | Specifies the response format. Use the following value.<br />`application/x-amz-json-1.0` | 
| Content-Length | Size of the payload in bytes. | 
| Content-Encoding | Specifies the encoding format of the input and output. Use the following value.<br />`amz-1.0` | 

The following is an example header for an HTTP request to return a list of all policies in the specified policy store in the AWS account where the `Principal` references a `User` named `alice`. In this example, the `Authorization` line is word-wrapped here for easier reading. Don't word wrap it in your actual request.

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