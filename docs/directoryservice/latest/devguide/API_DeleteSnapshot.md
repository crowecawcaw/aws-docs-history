# DeleteSnapshot

Deletes a directory snapshot.

## Request Syntax

```
{
   "SnapshotId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[SnapshotId](#API_DeleteSnapshot_RequestSyntax "#API_DeleteSnapshot_RequestSyntax")**

The identifier of the directory snapshot to be deleted.

Type: String

Pattern: `^s-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "SnapshotId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SnapshotId](#API_DeleteSnapshot_ResponseSyntax "#API_DeleteSnapshot_ResponseSyntax")**

The identifier of the directory snapshot that was deleted.

Type: String

Pattern: `^s-[0-9a-f]{10}$`

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

This example illustrates one usage of DeleteSnapshot.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 30
X-Amz-Target: DirectoryService_20150416.DeleteSnapshot
X-Amz-Date: 20161214T012131Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=685c5716e7e11b8d5b2ed5f413d6ff47fe179a1f215b83aa89d00d3b28827c1c

 {
   "SnapshotId": "s-9267f8d3f0"
 }
```

### Example Response

This example illustrates one usage of DeleteSnapshot.

```
HTTP/1.1 200 OK
x-amzn-RequestId: a68a1e79-c19b-11e6-870b-c3330207df37
Content-Type: application/x-amz-json-1.1
Content-Length: 29
Date: Wed, 14 Dec 2016 01:21:34 GMT

{
   "SnapshotId":"s-9267f8d3f0"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DeleteSnapshot.md "../../../goto/cli2/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DeleteSnapshot.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForCpp/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForGoV2/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForKotlin/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DeleteSnapshot.md "../../../goto/boto3/ds-2015-04-16/DeleteSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteSnapshot.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteSnapshot.md")
