# DeregisterCertificate

Deletes from the system the certificate that was registered for secure LDAP or client
certificate authentication.

## Request Syntax

```
{
   "CertificateId": "`string`",
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[CertificateId](#API_DeregisterCertificate_RequestSyntax "#API_DeregisterCertificate_RequestSyntax")**

The identifier of the certificate.

Type: String

Pattern: `^c-[0-9a-f]{10}$`

Required: Yes

**[DirectoryId](#API_DeregisterCertificate_RequestSyntax "#API_DeregisterCertificate_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**CertificateDoesNotExistException**

The certificate is not present in the system for describe or deregister activities.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**CertificateInUseException**

The certificate is being used for the LDAP security connection and cannot be removed
without disabling LDAP security.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DeregisterCertificate.md "../../../goto/cli2/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DeregisterCertificate.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForCpp/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForGoV2/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForKotlin/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DeregisterCertificate.md "../../../goto/boto3/ds-2015-04-16/DeregisterCertificate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DeregisterCertificate.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DeregisterCertificate.md")
