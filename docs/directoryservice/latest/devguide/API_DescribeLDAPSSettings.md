

# DescribeLDAPSSettings
<a name="API_DescribeLDAPSSettings"></a>

Describes the status of LDAP security for the specified directory.

## Request Syntax
<a name="API_DescribeLDAPSSettings_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLDAPSSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeLDAPSSettings_RequestSyntax) **   <a name="DirectoryService-DescribeLDAPSSettings-request-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Limit](#API_DescribeLDAPSSettings_RequestSyntax) **   <a name="DirectoryService-DescribeLDAPSSettings-request-Limit"></a>
Specifies the number of items that should be displayed on one page.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** [NextToken](#API_DescribeLDAPSSettings_RequestSyntax) **   <a name="DirectoryService-DescribeLDAPSSettings-request-NextToken"></a>
The type of next token used for pagination.  
Type: String  
Required: No

 ** [Type](#API_DescribeLDAPSSettings_RequestSyntax) **   <a name="DirectoryService-DescribeLDAPSSettings-request-Type"></a>
The type of LDAP security to enable. Currently only the value `Client` is supported.  
Type: String  
Valid Values: `Client`   
Required: No

## Response Syntax
<a name="API_DescribeLDAPSSettings_ResponseSyntax"></a>

```
{
   "LDAPSSettingsInfo": [ 
      { 
         "LastUpdatedDateTime": number,
         "LDAPSStatus": "string",
         "LDAPSStatusReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLDAPSSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LDAPSSettingsInfo](#API_DescribeLDAPSSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeLDAPSSettings-response-LDAPSSettingsInfo"></a>
Information about LDAP security for the specified directory, including status of enablement, state last updated date time, and the reason for the state.  
Type: Array of [LDAPSSettingInfo](API_LDAPSSettingInfo.md) objects

 ** [NextToken](#API_DescribeLDAPSSettings_ResponseSyntax) **   <a name="DirectoryService-DescribeLDAPSSettings-response-NextToken"></a>
The next token used to retrieve the LDAPS settings if the number of setting types exceeds page limit and there is another page.  
Type: String

## Errors
<a name="API_DescribeLDAPSSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryDoesNotExistException **   
The specified directory does not exist in the system.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The `NextToken` value is not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidParameterException **   
One or more parameters are not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLDAPSSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeLDAPSSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeLDAPSSettings) 