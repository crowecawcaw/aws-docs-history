# ShareDirectory

Shares a specified directory (`DirectoryId`) in your AWS account (directory
owner) with another AWS account (directory consumer). With this operation you can use your
directory from any AWS account and from any Amazon VPC within an AWS Region.

When you share your AWS Managed Microsoft AD directory, AWS Directory Service creates a shared directory in the
directory consumer account. This shared directory contains the metadata to provide access to
the directory within the directory owner account. The shared directory is visible in all VPCs
in the directory consumer account.

The `ShareMethod` parameter determines whether the specified directory can be
shared between AWS accounts inside the same AWS organization (`ORGANIZATIONS`).
It also determines whether you can share the directory with any other AWS account either
inside or outside of the organization (`HANDSHAKE`).

The `ShareNotes` parameter is only used when `HANDSHAKE` is called,
which sends a directory sharing request to the directory consumer.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "ShareMethod": "`string`",
   "ShareNotes": "`string`",
   "ShareTarget": {
      "Id": "`string`",
      "Type": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_ShareDirectory_RequestSyntax "#API_ShareDirectory_RequestSyntax")**

Identifier of the AWS Managed Microsoft AD directory that you want to share with other
AWS accounts.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[ShareMethod](#API_ShareDirectory_RequestSyntax "#API_ShareDirectory_RequestSyntax")**

The method used when sharing a directory to determine whether the directory should be
shared within your AWS organization (`ORGANIZATIONS`) or with any AWS account
by sending a directory sharing request (`HANDSHAKE`).

Type: String

Valid Values: `ORGANIZATIONS | HANDSHAKE`

Required: Yes

**[ShareNotes](#API_ShareDirectory_RequestSyntax "#API_ShareDirectory_RequestSyntax")**

A directory share request that is sent by the directory owner to the directory consumer.
The request includes a typed message to help the directory consumer administrator determine
whether to approve or reject the share invitation.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[ShareTarget](#API_ShareDirectory_RequestSyntax "#API_ShareDirectory_RequestSyntax")**

Identifier for the directory consumer account with whom the directory is to be
shared.

Type: [ShareTarget](API_ShareTarget.md "API_ShareTarget.md") object

Required: Yes

## Response Syntax

```
{
   "SharedDirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SharedDirectoryId](#API_ShareDirectory_ResponseSyntax "#API_ShareDirectory_ResponseSyntax")**

Identifier of the directory that is stored in the directory consumer account that is
shared from the specified directory (`DirectoryId`).

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryAlreadySharedException**

The specified directory has already been shared with this AWS account.

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

**InvalidTargetException**

The specified shared target is not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**OrganizationsException**

Exception encountered while trying to access your AWS organization.

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

**ShareLimitExceededException**

The maximum number of AWS accounts that you can share with this directory has been
reached.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ShareDirectory.md "../../../goto/cli2/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/ShareDirectory.md "../../../goto/DotNetSDKV3/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ShareDirectory.md "../../../goto/boto3/ds-2015-04-16/ShareDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ShareDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ShareDirectory.md")
