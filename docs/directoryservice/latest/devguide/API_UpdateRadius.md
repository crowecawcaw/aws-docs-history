# UpdateRadius

Updates the Remote Authentication Dial In User Service (RADIUS) server information for
an AD Connector or Microsoft AD directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "RadiusSettings": {
      "AuthenticationProtocol": "`string`",
      "DisplayLabel": "`string`",
      "RadiusPort": `number`,
      "RadiusRetries": `number`,
      "RadiusServers": [ "`string`" ],
      "RadiusServersIpv6": [ "`string`" ],
      "RadiusTimeout": `number`,
      "SharedSecret": "`string`",
      "UseSameUsername": `boolean`
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_UpdateRadius_RequestSyntax "#API_UpdateRadius_RequestSyntax")**

The identifier of the directory for which to update the RADIUS server
information.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[RadiusSettings](#API_UpdateRadius_RequestSyntax "#API_UpdateRadius_RequestSyntax")**

A [RadiusSettings](API_RadiusSettings.md "API_RadiusSettings.md") object that contains information about the RADIUS
server.

Type: [RadiusSettings](API_RadiusSettings.md "API_RadiusSettings.md") object

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

This example illustrates one usage of UpdateRadius.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 262
X-Amz-Target: DirectoryService_20150416.UpdateRadius
X-Amz-Date: 20161215T184937Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161215/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=6cc8097b61ad0ee23e166193d317a066feeea582d252b57923a0781dc011a686

 {
   "DirectoryId":"d-926example",
   "RadiusSettings":{
      "DisplayLabel":"MyRadius",
      "UseSameUsername":true,
      "RadiusTimeout":1,
      "AuthenticationProtocol":"PAP",
      "RadiusPort":1027,
      "RadiusRetries":1,
      "SharedSecret":"12345678",
      "RadiusServers":[
         "172.168.101.113"
      ]
   }
 }
```

### Example Response

This example illustrates one usage of UpdateRadius.

```
HTTP/1.1 200 OK
x-amzn-RequestId: fcd40ac9-c247-11e6-a7ca-f9a52a6a0390
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Thu, 15 Dec 2016 18:49:39 GMT

{

}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateRadius.md "../../../goto/cli2/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateRadius.md "../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateRadius.md "../../../goto/boto3/ds-2015-04-16/UpdateRadius.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateRadius.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateRadius.md")
