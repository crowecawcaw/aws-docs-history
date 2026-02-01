# GetDirectoryLimits

Obtains directory limit information for the current Region.

## Response Syntax

```
{
   "DirectoryLimits": {
      "CloudOnlyDirectoriesCurrentCount": ***number***,
      "CloudOnlyDirectoriesLimit": ***number***,
      "CloudOnlyDirectoriesLimitReached": ***boolean***,
      "CloudOnlyMicrosoftADCurrentCount": ***number***,
      "CloudOnlyMicrosoftADLimit": ***number***,
      "CloudOnlyMicrosoftADLimitReached": ***boolean***,
      "ConnectedDirectoriesCurrentCount": ***number***,
      "ConnectedDirectoriesLimit": ***number***,
      "ConnectedDirectoriesLimitReached": ***boolean***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DirectoryLimits](#API_GetDirectoryLimits_ResponseSyntax "#API_GetDirectoryLimits_ResponseSyntax")**

A [DirectoryLimits](API_DirectoryLimits.md "API_DirectoryLimits.md") object that contains the directory limits for the
current Region.

Type: [DirectoryLimits](API_DirectoryLimits.md "API_DirectoryLimits.md") object

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

This example illustrates one usage of GetDirectoryLimits.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: DirectoryService_20150416.GetDirectoryLimits
X-Amz-Date: 20161214T223512Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=550da3fb7986c02e54cb35d644fd6601bfe823c3956e9471308682df2c1977ac

 {

 }
```

### Example Response

This example illustrates one usage of GetDirectoryLimits.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 9526b149-c24d-11e6-bc3e-5ffd5f600cd8
Content-Type: application/x-amz-json-1.1
Content-Length: 348
Date: Wed, 14 Dec 2016 22:35:14 GMT

{
   "DirectoryLimits":{
      "CloudOnlyDirectoriesCurrentCount":2,
      "CloudOnlyDirectoriesLimit":10,
      "CloudOnlyDirectoriesLimitReached":false,
      "CloudOnlyMicrosoftADCurrentCount":2,
      "CloudOnlyMicrosoftADLimit":10,
      "CloudOnlyMicrosoftADLimitReached":false,
      "ConnectedDirectoriesCurrentCount":1,
      "ConnectedDirectoriesLimit":10,
      "ConnectedDirectoriesLimitReached":false
   }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/cli2/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/DotNetSDKV4/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForCpp/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForGoV2/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForJavaV2/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForKotlin/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForPHPV3/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/boto3/ds-2015-04-16/GetDirectoryLimits.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/GetDirectoryLimits.md "../../../goto/SdkForRubyV3/ds-2015-04-16/GetDirectoryLimits.md")
