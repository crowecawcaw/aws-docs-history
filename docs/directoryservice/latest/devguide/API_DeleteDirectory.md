# DeleteDirectory

Deletes an AWS Directory Service directory.

Before you call `DeleteDirectory`, ensure that all of the required permissions
have been explicitly granted through a policy. For details about what permissions are required
to run the `DeleteDirectory` operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](../admin-guide/UsingWithDS_IAM_ResourcePermissions.md "../admin-guide/UsingWithDS_IAM_ResourcePermissions.md").

## Request Syntax

```
{
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DeleteDirectory_RequestSyntax "#API_DeleteDirectory_RequestSyntax")**

The identifier of the directory to delete.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "DirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DirectoryId](#API_DeleteDirectory_ResponseSyntax "#API_DeleteDirectory_ResponseSyntax")**

The directory identifier.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

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

This example illustrates one usage of DeleteDirectory.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: DirectoryService_20150416.DeleteDirectory
X-Amz-Date: 20161214T002424Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=b542aa77381528e27afcf08b229252606fa79723695fb2d19b81b51d66d7f92d

 {
   "DirectoryId": "d-926example"
 }
```

### Example Response

This example illustrates one usage of DeleteDirectory.

```
HTTP/1.1 200 OK
x-amzn-RequestId: abcbeb82-c193-11e6-bf9e-272b6602bf9f
Content-Type: application/x-amz-json-1.1
Content-Length: 30
Date: Wed, 14 Dec 2016 00:24:26 GMT

{
   "DirectoryId":"d-926example"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DeleteDirectory.md "../../../goto/cli2/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DeleteDirectory.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DeleteDirectory.md "../../../goto/boto3/ds-2015-04-16/DeleteDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteDirectory.md")
