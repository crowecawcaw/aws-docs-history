# RemoveIpRoutes

Removes IP address blocks from a directory.

## Request Syntax

```
{
   "CidrIps": [ "`string`" ],
   "CidrIpv6s": [ "`string`" ],
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[CidrIps](#API_RemoveIpRoutes_RequestSyntax "#API_RemoveIpRoutes_RequestSyntax")**

IP address blocks that you want to remove.

Type: Array of strings

Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([1-9]|[1-2][0-9]|3[0-2]))$`

Required: No

**[CidrIpv6s](#API_RemoveIpRoutes_RequestSyntax "#API_RemoveIpRoutes_RequestSyntax")**

IPv6 address blocks that you want to remove.

Type: Array of strings

Pattern: `^((([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,7}:)|(([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2})|(([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3})|(([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4})|(([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5})|([0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))|(:((:[0-9a-fA-F]{1,4}){1,7}|:)))\/(12[0-8]|1[01][0-9]|[1-9]?[0-9])$`

Required: No

**[DirectoryId](#API_RemoveIpRoutes_RequestSyntax "#API_RemoveIpRoutes_RequestSyntax")**

Identifier (ID) of the directory from which you want to remove the IP addresses.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

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

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of RemoveIpRoutes.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 62
X-Amz-Target: DirectoryService_20150416.RemoveIpRoutes
X-Amz-Date: 20161214T233152Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=b3413802dda807a99b3a5783eef6fc3599eefa200820af9842cc5b24becb1802

 {
   "DirectoryId":"d-926example",
   "CidrIps": ["12.12.12.12/32"]
 }
```

### Example Response

This example illustrates one usage of RemoveIpRoutes.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 7f62aa28-c255-11e6-b3d3-bf8f15b8b2ee
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 23:31:54 GMT

{

}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/cli2/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/DotNetSDKV3/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForCpp/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForGoV2/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForKotlin/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForPHPV3/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/boto3/ds-2015-04-16/RemoveIpRoutes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RemoveIpRoutes.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RemoveIpRoutes.md")
