# EnableLDAPS

Activates the switch for the specific directory to always use LDAP secure calls.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Type": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_EnableLDAPS_RequestSyntax "#API_EnableLDAPS_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Type](#API_EnableLDAPS_RequestSyntax "#API_EnableLDAPS_RequestSyntax")**

The type of LDAP security to enable. Currently only the value `Client` is
supported.

Type: String

Valid Values: `Client`

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

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

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

**InvalidLDAPSStatusException**

The LDAP activities could not be performed because they are limited by the LDAPS
status.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/EnableLDAPS.md "../../../goto/cli2/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/EnableLDAPS.md "../../../goto/DotNetSDKV4/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForCpp/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForGoV2/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForJavaV2/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForKotlin/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForPHPV3/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/EnableLDAPS.md "../../../goto/boto3/ds-2015-04-16/EnableLDAPS.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/EnableLDAPS.md "../../../goto/SdkForRubyV3/ds-2015-04-16/EnableLDAPS.md")
