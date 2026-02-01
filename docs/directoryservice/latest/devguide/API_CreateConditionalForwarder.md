# CreateConditionalForwarder

Creates a conditional forwarder associated with your AWS directory. Conditional
forwarders are required in order to set up a trust relationship with another domain. The
conditional forwarder points to the trusted domain.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "DnsIpAddrs": [ "`string`" ],
   "DnsIpv6Addrs": [ "`string`" ],
   "RemoteDomainName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_CreateConditionalForwarder_RequestSyntax "#API_CreateConditionalForwarder_RequestSyntax")**

The directory ID of the AWS directory for which you are creating the conditional
forwarder.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[DnsIpAddrs](#API_CreateConditionalForwarder_RequestSyntax "#API_CreateConditionalForwarder_RequestSyntax")**

The IP addresses of the remote DNS server associated with RemoteDomainName.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**[DnsIpv6Addrs](#API_CreateConditionalForwarder_RequestSyntax "#API_CreateConditionalForwarder_RequestSyntax")**

The IPv6 addresses of the remote DNS server associated with RemoteDomainName.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**[RemoteDomainName](#API_CreateConditionalForwarder_RequestSyntax "#API_CreateConditionalForwarder_RequestSyntax")**

The fully qualified domain name (FQDN) of the remote domain with which you will set up
a trust relationship.

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryUnavailableException**

The specified directory is unavailable.

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

This example illustrates one usage of CreateConditionalForwarder.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 105
X-Amz-Target: DirectoryService_20150416.CreateConditionalForwarder
X-Amz-Date: 20161213T215543Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=717e381f0258731fe0197c68d1f5d2a0e96825119c15a6e0dcfa2d07063c6af6

 {
   "DirectoryId":"d-926example",
   "RemoteDomainName":"sales.example.com",
   "DnsIpAddrs":[
      "172.30.21.228"
   ]
 }
```

### Example Response

This example illustrates one usage of CreateConditionalForwarder.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 68e74443-c180-11e6-91f4-6dbff6648f8a
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Tue, 13 Dec 2016 22:06:34 GMT

 {

 }
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/cli2/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/DotNetSDKV4/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/boto3/ds-2015-04-16/CreateConditionalForwarder.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateConditionalForwarder.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateConditionalForwarder.md")
