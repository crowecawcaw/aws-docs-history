# CreateTrust

AWS Directory Service for Microsoft Active Directory allows you to configure trust relationships. For
example, you can establish a trust between your AWS Managed Microsoft AD directory, and your existing
self-managed Microsoft Active Directory. This would allow you to provide users and groups
access to resources in either domain, with a single set of credentials.

This action initiates the creation of the AWS side of a trust relationship between an
AWS Managed Microsoft AD directory and an external domain. You can create either a forest trust or an
external trust.

## Request Syntax

```
{
   "ConditionalForwarderIpAddrs": [ "`string`" ],
   "ConditionalForwarderIpv6Addrs": [ "`string`" ],
   "DirectoryId": "`string`",
   "RemoteDomainName": "`string`",
   "SelectiveAuth": "`string`",
   "TrustDirection": "`string`",
   "TrustPassword": "`string`",
   "TrustType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ConditionalForwarderIpAddrs](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The IP addresses of the remote DNS server associated with RemoteDomainName.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**[ConditionalForwarderIpv6Addrs](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The IPv6 addresses of the remote DNS server associated with RemoteDomainName.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**[DirectoryId](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The Directory ID of the AWS Managed Microsoft AD directory for which to establish the trust
relationship.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[RemoteDomainName](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The Fully Qualified Domain Name (FQDN) of the external domain for which to create the
trust relationship.

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`

Required: Yes

**[SelectiveAuth](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

Optional parameter to enable selective authentication for the trust.

Type: String

Valid Values: `Enabled | Disabled`

Required: No

**[TrustDirection](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The direction of the trust relationship.

Type: String

Valid Values: `One-Way: Outgoing | One-Way: Incoming | Two-Way`

Required: Yes

**[TrustPassword](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The trust password. The trust password must be the same password that was used when creating the trust
relationship on the external domain.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^(\p{LD}|\p{Punct}| )+$`

Required: Yes

**[TrustType](#API_CreateTrust_RequestSyntax "#API_CreateTrust_RequestSyntax")**

The trust relationship type. `Forest` is the default.

Type: String

Valid Values: `Forest | External`

Required: No

## Response Syntax

```
{
   "TrustId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[TrustId](#API_CreateTrust_ResponseSyntax "#API_CreateTrust_ResponseSyntax")**

A unique identifier for the trust relationship that was created.

Type: String

Pattern: `^t-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityAlreadyExistsException**

The specified entity already exists.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of CreateTrust.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 222
X-Amz-Target: DirectoryService_20150416.CreateTrust
X-Amz-Date: 20161213T235223Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=1f0cff7825d20bab2a0dab1e0b8bedbed72f0c22175c7d9ed0e63598ae99cae5

 {
   "TrustPassword":"Str0ngP@ssw0rd",
   "DirectoryId":"d-926example",
   "RemoteDomainName":"europe.example.com",
   "ConditionalForwarderIpAddrs":[
      "172.30.21.228"
   ],
   "TrustType":"Forest",
   "TrustDirection":"One-Way: Outgoing"
 }
```

### Example Response

This example illustrates one usage of CreateTrust.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 3343bc79-c18f-11e6-ba7f-e33ae22bc363
Content-Type: application/x-amz-json-1.1
Content-Length: 26
Date: Tue, 13 Dec 2016 23:52:26 GMT

{
   "TrustId":"t-9267353743"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateTrust.md "../../../goto/cli2/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/CreateTrust.md "../../../goto/DotNetSDKV3/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateTrust.md "../../../goto/boto3/ds-2015-04-16/CreateTrust.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateTrust.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateTrust.md")
