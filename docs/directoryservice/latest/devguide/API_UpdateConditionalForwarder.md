# UpdateConditionalForwarder

Updates a conditional forwarder that has been set up for your AWS
directory.

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

**[DirectoryId](#API_UpdateConditionalForwarder_RequestSyntax "#API_UpdateConditionalForwarder_RequestSyntax")**

The directory ID of the AWS directory for which to update the conditional
forwarder.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[DnsIpAddrs](#API_UpdateConditionalForwarder_RequestSyntax "#API_UpdateConditionalForwarder_RequestSyntax")**

The updated IP addresses of the remote DNS server associated with the conditional
forwarder.

Type: Array of strings

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**[DnsIpv6Addrs](#API_UpdateConditionalForwarder_RequestSyntax "#API_UpdateConditionalForwarder_RequestSyntax")**

The updated IPv6 addresses of the remote DNS server associated with the conditional
forwarder.

Type: Array of strings

Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`

Required: No

**[RemoteDomainName](#API_UpdateConditionalForwarder_RequestSyntax "#API_UpdateConditionalForwarder_RequestSyntax")**

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

This example illustrates one usage of UpdateConditionalForwarder.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: DirectoryService_20150416.UpdateConditionalForwarder
X-Amz-Date: 20161215T183823Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161215/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=84648cead858ef1efd7db75ce248aa3e22a78139b109eec6122dc3c495b71085

 {
   "DirectoryId":"d-926example",
   "RemoteDomainName":"sales.example.com",
   "DnsIpAddrs": ["172.168.101.11"]
 }
```

### Example Response

This example illustrates one usage of UpdateConditionalForwarder.

```
HTTP/1.1 200 OK
x-amzn-RequestId: aa015a05-c2f5-11e6-b3d3-bf8f15b8b2ee
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Thu, 15 Dec 2016 18:38:27 GMT

 {

 }
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/cli2/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/boto3/ds-2015-04-16/UpdateConditionalForwarder.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateConditionalForwarder.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateConditionalForwarder.md")
