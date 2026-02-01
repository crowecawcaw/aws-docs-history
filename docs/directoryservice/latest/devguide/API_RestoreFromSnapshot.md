# RestoreFromSnapshot

Restores a directory using an existing directory snapshot.

When you restore a directory from a snapshot, any changes made to the directory after the snapshot date are overwritten.

This action returns as soon as the restore operation is initiated. You can monitor the
progress of the restore operation by calling the [DescribeDirectories](API_DescribeDirectories.md "API_DescribeDirectories.md") operation with
the directory identifier. When the **DirectoryDescription.Stage** value changes to
`Active`, the restore operation is complete.

## Request Syntax

```
{
   "SnapshotId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[SnapshotId](#API_RestoreFromSnapshot_RequestSyntax "#API_RestoreFromSnapshot_RequestSyntax")**

The identifier of the snapshot to restore from.

Type: String

Pattern: `^s-[0-9a-f]{10}$`

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

This example illustrates one usage of RestoreFromSnapshot.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 30
X-Amz-Target: DirectoryService_20150416.RestoreFromSnapshot
X-Amz-Date: 20161214T235310Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=5c6be5a543a9df855e15ed75c131318330c4acf9b791515e8b3524e2430c180f

 {
   "SnapshotId": "s-9267f6da4e"
 }
```

### Example Response

This example illustrates one usage of RestoreFromSnapshot.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 78ebab96-c258-11e6-a4dc-e5519684970a
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 23:53:12 GMT

{

}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/cli2/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/DotNetSDKV4/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForCpp/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForGoV2/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForKotlin/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForPHPV3/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/boto3/ds-2015-04-16/RestoreFromSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RestoreFromSnapshot.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RestoreFromSnapshot.md")
