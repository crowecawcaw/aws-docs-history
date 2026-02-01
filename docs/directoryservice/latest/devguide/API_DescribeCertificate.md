# DescribeCertificate

Displays information about the certificate registered for secure LDAP or client
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

**[CertificateId](#API_DescribeCertificate_RequestSyntax "#API_DescribeCertificate_RequestSyntax")**

The identifier of the certificate.

Type: String

Pattern: `^c-[0-9a-f]{10}$`

Required: Yes

**[DirectoryId](#API_DescribeCertificate_RequestSyntax "#API_DescribeCertificate_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "Certificate": {
      "CertificateId": "***string***",
      "ClientCertAuthSettings": {
         "OCSPUrl": "***string***"
      },
      "CommonName": "***string***",
      "ExpiryDateTime": ***number***,
      "RegisteredDateTime": ***number***,
      "State": "***string***",
      "StateReason": "***string***",
      "Type": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Certificate](#API_DescribeCertificate_ResponseSyntax "#API_DescribeCertificate_ResponseSyntax")**

Information about the certificate, including registered date time, certificate state, the
reason for the state, expiration date time, and certificate common name.

Type: [Certificate](API_Certificate.md "API_Certificate.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**CertificateDoesNotExistException**

The certificate is not present in the system for describe or deregister activities.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeCertificate.md "../../../goto/cli2/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeCertificate.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeCertificate.md "../../../goto/boto3/ds-2015-04-16/DescribeCertificate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeCertificate.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeCertificate.md")
