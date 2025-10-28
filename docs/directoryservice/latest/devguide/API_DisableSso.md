# DisableSso

Disables single-sign on for a directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Password": "`string`",
   "UserName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DisableSso_RequestSyntax "#API_DisableSso_RequestSyntax")**

The identifier of the directory for which to disable single-sign on.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Password](#API_DisableSso_RequestSyntax "#API_DisableSso_RequestSyntax")**

The password of an alternate account to use to disable single-sign on. This is only used
for AD Connector directories. For more information, see the _UserName_
parameter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: No

**[UserName](#API_DisableSso_RequestSyntax "#API_DisableSso_RequestSyntax")**

The username of an alternate account to use to disable single-sign on. This is only used
for AD Connector directories. This account must have privileges to remove a service
principal name.

If the AD Connector service account does not have privileges to remove a service
principal name, you can specify an alternate account with the _UserName_
and _Password_ parameters. These credentials are only used to disable
single sign-on and are not stored by the service. The AD Connector service account is not
changed.

Type: String

Length Constraints: Minimum length of 1.

Pattern: `[a-zA-Z0-9._-]+`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AuthenticationFailedException**

An authentication error occurred.

**Message**

The textual message for the exception.

**RequestId**

The identifier of the request that caused the exception.

HTTP Status Code: 400

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

**InsufficientPermissionsException**

The account does not have sufficient permission to perform the operation.

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

This example illustrates one usage of DisableSso.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 80
X-Amz-Target: DirectoryService_20150416.DisableSso
X-Amz-Date: 20161214T221722Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=b68ee7e88af7fc741471e9098dbc1636979ae461f0b9cd2f187124abbf762455

 {
   "UserName": "Admin",
   "DirectoryId": "d-926example",
   "Password": "Str0ngP@ssw0rd"
 }
```

### Example Response

This example illustrates one usage of DisableSso.

```
HTTP/1.1 200 OK
x-amzn-RequestId: fcd40ac9-c247-11e6-a7ca-f9a52a6a0390
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 22:17:12 GMT

{

}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DisableSso.md "../../../goto/cli2/ds-2015-04-16/DisableSso.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DisableSso.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DisableSso.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DisableSso.md "../../../goto/SdkForCpp/ds-2015-04-16/DisableSso.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DisableSso.md "../../../goto/SdkForGoV2/ds-2015-04-16/DisableSso.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DisableSso.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DisableSso.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DisableSso.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DisableSso.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DisableSso.md "../../../goto/SdkForKotlin/ds-2015-04-16/DisableSso.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DisableSso.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DisableSso.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DisableSso.md "../../../goto/boto3/ds-2015-04-16/DisableSso.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DisableSso.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DisableSso.md")
