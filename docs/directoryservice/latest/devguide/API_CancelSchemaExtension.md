# CancelSchemaExtension

Cancels an in-progress schema extension to a Microsoft AD directory. Once a schema
extension has started replicating to all domain controllers, the task can no longer be
canceled. A schema extension can be canceled during any of the following states;
`Initializing`, `CreatingSnapshot`, and
`UpdatingSchema`.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "SchemaExtensionId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_CancelSchemaExtension_RequestSyntax "#API_CancelSchemaExtension_RequestSyntax")**

The identifier of the directory whose schema extension will be canceled.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[SchemaExtensionId](#API_CancelSchemaExtension_RequestSyntax "#API_CancelSchemaExtension_RequestSyntax")**

The identifier of the schema extension that will be canceled.

Type: String

Pattern: `^e-[0-9a-f]{10}$`

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

This example illustrates one usage of CancelSchemaExtension.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 68
X-Amz-Target: DirectoryService_20150416.CancelSchemaExtension
X-Amz-Date: 20161212T231630Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=14da7b7426d03c907c02a3e29f96158b8c1cd2be2e0f323a86b338a1614848f1

 {
   "DirectoryId": "d-926example",
   "SchemaExtensionId": "e-926731d2a0"
 }
```

### Example Response

This example illustrates one usage of CancelSchemaExtension.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 04eada50-c0c1-11e6-887b-29887bf36843
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Dec 2016 23:16:32 GMT

 {
 }
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/cli2/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/DotNetSDKV4/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForCpp/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForGoV2/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForKotlin/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/boto3/ds-2015-04-16/CancelSchemaExtension.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CancelSchemaExtension.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CancelSchemaExtension.md")
