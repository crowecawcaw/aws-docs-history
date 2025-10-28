# EnableClientAuthentication

Enables alternative client authentication methods for the specified directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Type": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_EnableClientAuthentication_RequestSyntax "#API_EnableClientAuthentication_RequestSyntax")**

The identifier of the specified directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Type](#API_EnableClientAuthentication_RequestSyntax "#API_EnableClientAuthentication_RequestSyntax")**

The type of client authentication to enable. Currently only the value
`SmartCard` is supported. Smart card authentication in AD Connector requires
that you enable Kerberos Constrained Delegation for the Service User to the LDAP service in
your self-managed AD.

Type: String

Valid Values: `SmartCard | SmartCardOrPassword`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidClientAuthStatusException**

Client authentication is already enabled.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**NoAvailableCertificateException**

Client authentication setup could not be completed because at least one valid certificate
must be registered in the system.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/cli2/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/DotNetSDKV3/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForCpp/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForGoV2/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForJavaV2/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForKotlin/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForPHPV3/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/boto3/ds-2015-04-16/EnableClientAuthentication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/EnableClientAuthentication.md "../../../goto/SdkForRubyV3/ds-2015-04-16/EnableClientAuthentication.md")
