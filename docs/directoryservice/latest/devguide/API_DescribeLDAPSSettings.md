# DescribeLDAPSSettings

Describes the status of LDAP security for the specified directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Limit": `number`,
   "NextToken": "`string`",
   "Type": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DescribeLDAPSSettings_RequestSyntax "#API_DescribeLDAPSSettings_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Limit](#API_DescribeLDAPSSettings_RequestSyntax "#API_DescribeLDAPSSettings_RequestSyntax")**

Specifies the number of items that should be displayed on one page.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 50.

Required: No

**[NextToken](#API_DescribeLDAPSSettings_RequestSyntax "#API_DescribeLDAPSSettings_RequestSyntax")**

The type of next token used for pagination.

Type: String

Required: No

**[Type](#API_DescribeLDAPSSettings_RequestSyntax "#API_DescribeLDAPSSettings_RequestSyntax")**

The type of LDAP security to enable. Currently only the value `Client` is
supported.

Type: String

Valid Values: `Client`

Required: No

## Response Syntax

```
{
   "LDAPSSettingsInfo": [
      {
         "LastUpdatedDateTime": ***number***,
         "LDAPSStatus": "***string***",
         "LDAPSStatusReason": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LDAPSSettingsInfo](#API_DescribeLDAPSSettings_ResponseSyntax "#API_DescribeLDAPSSettings_ResponseSyntax")**

Information about LDAP security for the specified directory, including status of
enablement, state last updated date time, and the reason for the state.

Type: Array of [LDAPSSettingInfo](API_LDAPSSettingInfo.md "API_LDAPSSettingInfo.md") objects

**[NextToken](#API_DescribeLDAPSSettings_ResponseSyntax "#API_DescribeLDAPSSettings_ResponseSyntax")**

The next token used to retrieve the LDAPS settings if the number of setting types exceeds
page limit and there is another page.

Type: String

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

**InvalidNextTokenException**

The `NextToken` value is not valid.

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

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/cli2/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/boto3/ds-2015-04-16/DescribeLDAPSSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeLDAPSSettings.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeLDAPSSettings.md")
