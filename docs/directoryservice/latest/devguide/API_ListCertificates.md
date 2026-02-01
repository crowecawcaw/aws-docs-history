# ListCertificates

For the specified directory, lists all the certificates registered for a secure LDAP or
client certificate authentication.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Limit": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_ListCertificates_RequestSyntax "#API_ListCertificates_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Limit](#API_ListCertificates_RequestSyntax "#API_ListCertificates_RequestSyntax")**

The number of items that should show up on one page

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 50.

Required: No

**[NextToken](#API_ListCertificates_RequestSyntax "#API_ListCertificates_RequestSyntax")**

A token for requesting another page of certificates if the `NextToken` response
element indicates that more certificates are available. Use the value of the returned
`NextToken` element in your request until the token comes back as
`null`. Pass `null` if this is the first call.

Type: String

Required: No

## Response Syntax

```
{
   "CertificatesInfo": [
      {
         "CertificateId": "***string***",
         "CommonName": "***string***",
         "ExpiryDateTime": ***number***,
         "State": "***string***",
         "Type": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CertificatesInfo](#API_ListCertificates_ResponseSyntax "#API_ListCertificates_ResponseSyntax")**

A list of certificates with basic details including certificate ID, certificate common
name, certificate state.

Type: Array of [CertificateInfo](API_CertificateInfo.md "API_CertificateInfo.md") objects

**[NextToken](#API_ListCertificates_ResponseSyntax "#API_ListCertificates_ResponseSyntax")**

Indicates whether another page of certificates is available when the number of available
certificates exceeds the page limit.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ListCertificates.md "../../../goto/cli2/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/ListCertificates.md "../../../goto/DotNetSDKV4/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForCpp/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForGoV2/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForKotlin/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ListCertificates.md "../../../goto/boto3/ds-2015-04-16/ListCertificates.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ListCertificates.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ListCertificates.md")
