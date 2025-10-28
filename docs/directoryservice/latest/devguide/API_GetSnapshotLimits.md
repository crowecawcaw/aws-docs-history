# GetSnapshotLimits

Obtains the manual snapshot limits for a directory.

## Request Syntax

```
{
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_GetSnapshotLimits_RequestSyntax "#API_GetSnapshotLimits_RequestSyntax")**

Contains the identifier of the directory to obtain the limits for.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "SnapshotLimits": {
      "ManualSnapshotsCurrentCount": ***number***,
      "ManualSnapshotsLimit": ***number***,
      "ManualSnapshotsLimitReached": ***boolean***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SnapshotLimits](#API_GetSnapshotLimits_ResponseSyntax "#API_GetSnapshotLimits_ResponseSyntax")**

A [SnapshotLimits](API_SnapshotLimits.md "API_SnapshotLimits.md") object that contains the manual snapshot limits for the specified
directory.

Type: [SnapshotLimits](API_SnapshotLimits.md "API_SnapshotLimits.md") object

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

This example illustrates one usage of GetSnapshotLimits.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: DirectoryService_20150416.GetSnapshotLimits
X-Amz-Date: 20161214T224507Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=f9ba790cf905e14fa97fd1ed6a961c72d83a23f3e54ab126d8e4a30ec14d3cdb

 {
   "DirectoryId": "d-926example"
 }
```

### Example Response

This example illustrates one usage of GetSnapshotLimits.

```
HTTP/1.1 200 OK
x-amzn-RequestId: f7895979-c24e-11e6-a0ba-6bb2a89ebc49
Content-Type: application/x-amz-json-1.1
Content-Length: 113
Date: Wed, 14 Dec 2016 22:45:09 GMT

{
   "SnapshotLimits":{
      "ManualSnapshotsCurrentCount":1,
      "ManualSnapshotsLimit":5,
      "ManualSnapshotsLimitReached":false
   }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/cli2/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/DotNetSDKV3/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForCpp/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForGoV2/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForJavaV2/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForKotlin/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForPHPV3/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/boto3/ds-2015-04-16/GetSnapshotLimits.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/GetSnapshotLimits.md "../../../goto/SdkForRubyV3/ds-2015-04-16/GetSnapshotLimits.md")
