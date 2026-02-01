# RegisterCertificate

Registers a certificate for a secure LDAP or client certificate authentication.

## Request Syntax

```
{
   "CertificateData": "`string`",
   "ClientCertAuthSettings": {
      "OCSPUrl": "`string`"
   },
   "DirectoryId": "`string`",
   "Type": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[CertificateData](#API_RegisterCertificate_RequestSyntax "#API_RegisterCertificate_RequestSyntax")**

The certificate PEM string that needs to be registered.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 8192.

Required: Yes

**[ClientCertAuthSettings](#API_RegisterCertificate_RequestSyntax "#API_RegisterCertificate_RequestSyntax")**

A `ClientCertAuthSettings` object that contains client certificate
authentication settings.

Type: [ClientCertAuthSettings](API_ClientCertAuthSettings.md "API_ClientCertAuthSettings.md") object

Required: No

**[DirectoryId](#API_RegisterCertificate_RequestSyntax "#API_RegisterCertificate_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Type](#API_RegisterCertificate_RequestSyntax "#API_RegisterCertificate_RequestSyntax")**

The function that the registered certificate performs. Valid values include
`ClientLDAPS` or `ClientCertAuth`. The default value is
`ClientLDAPS`.

Type: String

Valid Values: `ClientCertAuth | ClientLDAPS`

Required: No

## Response Syntax

```
{
   "CertificateId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CertificateId](#API_RegisterCertificate_ResponseSyntax "#API_RegisterCertificate_ResponseSyntax")**

The identifier of the certificate.

Type: String

Pattern: `^c-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**CertificateAlreadyExistsException**

The certificate has already been registered into the system.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**CertificateLimitExceededException**

The certificate could not be added because the certificate limit has been reached.

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

**DirectoryUnavailableException**

The specified directory is unavailable.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidCertificateException**

The certificate PEM that was provided has incorrect encoding.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/RegisterCertificate.md "../../../goto/cli2/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/RegisterCertificate.md "../../../goto/DotNetSDKV4/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForCpp/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForGoV2/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForKotlin/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForPHPV3/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/RegisterCertificate.md "../../../goto/boto3/ds-2015-04-16/RegisterCertificate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RegisterCertificate.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RegisterCertificate.md")
