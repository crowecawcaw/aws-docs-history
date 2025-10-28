# StartSchemaExtension

Applies a schema extension to a Microsoft AD directory.

## Request Syntax

```
{
   "CreateSnapshotBeforeSchemaExtension": `boolean`,
   "Description": "`string`",
   "DirectoryId": "`string`",
   "LdifContent": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[CreateSnapshotBeforeSchemaExtension](#API_StartSchemaExtension_RequestSyntax "#API_StartSchemaExtension_RequestSyntax")**

If true, creates a snapshot of the directory before applying the schema
extension.

Type: Boolean

Required: Yes

**[Description](#API_StartSchemaExtension_RequestSyntax "#API_StartSchemaExtension_RequestSyntax")**

A description of the schema extension.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: Yes

**[DirectoryId](#API_StartSchemaExtension_RequestSyntax "#API_StartSchemaExtension_RequestSyntax")**

The identifier of the directory for which the schema extension will be applied
to.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[LdifContent](#API_StartSchemaExtension_RequestSyntax "#API_StartSchemaExtension_RequestSyntax")**

The LDIF file represented as a string. To construct the LdifContent string, precede
each line as it would be formatted in an ldif file with \n. See the example request below for
more details. The file size can be no larger than 1MB.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 500000.

Required: Yes

## Response Syntax

```
{
   "SchemaExtensionId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SchemaExtensionId](#API_StartSchemaExtension_ResponseSyntax "#API_StartSchemaExtension_ResponseSyntax")**

The identifier of the schema extension that will be applied.

Type: String

Pattern: `^e-[0-9a-f]{10}$`

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

**SnapshotLimitExceededException**

The maximum number of manual snapshots for the directory has been reached. You can
use the [GetSnapshotLimits](API_GetSnapshotLimits.md "API_GetSnapshotLimits.md") operation to determine the snapshot limits
for a directory.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of StartSchemaExtension.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 320
X-Amz-Target: DirectoryService_20150416.StartSchemaExtension
X-Amz-Date: 20161219T190703Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161219/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=5c1200f494c1771770d7aa964e45ee36d80e724e0d9a8e62ab9822574c8cc915

 {
   "CreateSnapshotBeforeSchemaExtension":true,
   "DirectoryId":"d-926example",
   "LdifContent":"dn: CN=User,CN=Schema,CN=Configuration,DC=sales,DC=example,DC=com\nchangetype: modify\nadd: mayContain\nmayContain: drink\n-\n\nDN:\nchangetype: modify\nreplace: schemaupdatenow\nschemaupdatenow: 1\n-",
   "Description":"Adds may contain attribute to user class. To construct the LdifContent string, precede each line as it would be formatted in an ldif file with \n. For example the LdifContent string above is formatted the following way in an Ldif file:

     dn: CN=User,CN=Schema,CN=Configuration,DC=sales,DC=example,DC=com
     changetype: modify
     add: mayContain
     mayContain: drink
     -

     dn:
     changetype: modify
     replace: schemaupdatenow
     schemaupdatenow: 1
     -"
 }
```

### Example Response

This example illustrates one usage of StartSchemaExtension.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 54723d00-c61e-11e6-a96d-2b0686697d23
Content-Type: application/x-amz-json-1.1
Content-Length: 36
Date: Mon, 19 Dec 2016 19:07:04 GMT

{
  "SchemaExtensionId": "e-926731dc50"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/StartSchemaExtension.md "../../../goto/cli2/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/StartSchemaExtension.md "../../../goto/DotNetSDKV3/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForCpp/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForGoV2/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForJavaV2/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForKotlin/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForPHPV3/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/StartSchemaExtension.md "../../../goto/boto3/ds-2015-04-16/StartSchemaExtension.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/StartSchemaExtension.md "../../../goto/SdkForRubyV3/ds-2015-04-16/StartSchemaExtension.md")
