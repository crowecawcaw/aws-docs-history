# ResetUserPassword

Resets the password for any user in your AWS Managed Microsoft AD or Simple AD directory. Disabled
users will become enabled and can be authenticated following the API call.

You can reset the password for any user in your directory with the following
exceptions:

- For Simple AD, you cannot reset the password for any user that is a member of either
  the **Domain Admins** or **Enterprise
  Admins** group except for the administrator user.
- For AWS Managed Microsoft AD, you can only reset the password for a user that is in an OU based
  off of the NetBIOS name that you typed when you created your directory. For example, you
  cannot reset the password for a user in the **AWS
  Reserved** OU. For more information about the OU structure for an AWS Managed Microsoft AD
  directory, see [What Gets Created](../admin-guide/ms_ad_getting_started_what_gets_created.md "../admin-guide/ms_ad_getting_started_what_gets_created.md") in the _AWS Directory Service Administration
  Guide_.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "NewPassword": "`string`",
   "UserName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_ResetUserPassword_RequestSyntax "#API_ResetUserPassword_RequestSyntax")**

Identifier of the AWS Managed Microsoft AD or Simple AD directory in which the user resides.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[NewPassword](#API_ResetUserPassword_RequestSyntax "#API_ResetUserPassword_RequestSyntax")**

The new password that will be reset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 127.

Required: Yes

**[UserName](#API_ResetUserPassword_RequestSyntax "#API_ResetUserPassword_RequestSyntax")**

The user name of the user whose password will be reset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `^(?!.*\\|.*"|.*\/|.*\[|.*\]|.*:|.*;|.*\||.*=|.*,|.*\+|.*\*|.*\?|.*<|.*>|.*@).*$`

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

**InvalidPasswordException**

The new password provided by the user does not meet the password complexity
requirements defined in your directory.

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

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**UserDoesNotExistException**

The user provided a username that does not exist in your directory.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ResetUserPassword.md "../../../goto/cli2/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/ResetUserPassword.md "../../../goto/DotNetSDKV3/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForCpp/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForGoV2/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForKotlin/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ResetUserPassword.md "../../../goto/boto3/ds-2015-04-16/ResetUserPassword.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ResetUserPassword.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ResetUserPassword.md")
