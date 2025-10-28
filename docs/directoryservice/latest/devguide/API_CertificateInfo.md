# CertificateInfo

Contains general information about a certificate.

## Contents

**CertificateId**

The identifier of the certificate.

Type: String

Pattern: `^c-[0-9a-f]{10}$`

Required: No

**CommonName**

The common name for the certificate.

Type: String

Required: No

**ExpiryDateTime**

The date and time when the certificate will expire.

Type: Timestamp

Required: No

**State**

The state of the certificate.

Type: String

Valid Values: `Registering | Registered | RegisterFailed | Deregistering | Deregistered | DeregisterFailed`

Required: No

**Type**

The function that the registered certificate performs. Valid values include
`ClientLDAPS` or `ClientCertAuth`. The default value is
`ClientLDAPS`.

Type: String

Valid Values: `ClientCertAuth | ClientLDAPS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CertificateInfo.md "../../../goto/SdkForCpp/ds-2015-04-16/CertificateInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CertificateInfo.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CertificateInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CertificateInfo.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CertificateInfo.md")
