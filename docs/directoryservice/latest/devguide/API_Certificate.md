# Certificate

Information about the certificate.

## Contents

**CertificateId**

The identifier of the certificate.

Type: String

Pattern: `^c-[0-9a-f]{10}$`

Required: No

**ClientCertAuthSettings**

A `ClientCertAuthSettings` object that contains client certificate
authentication settings.

Type: [ClientCertAuthSettings](API_ClientCertAuthSettings.md "API_ClientCertAuthSettings.md") object

Required: No

**CommonName**

The common name for the certificate.

Type: String

Required: No

**ExpiryDateTime**

The date and time when the certificate will expire.

Type: Timestamp

Required: No

**RegisteredDateTime**

The date and time that the certificate was registered.

Type: Timestamp

Required: No

**State**

The state of the certificate.

Type: String

Valid Values: `Registering | Registered | RegisterFailed | Deregistering | Deregistered | DeregisterFailed`

Required: No

**StateReason**

Describes a state change for the certificate.

Type: String

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

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/Certificate.md "../../../goto/SdkForCpp/ds-2015-04-16/Certificate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/Certificate.md "../../../goto/SdkForJavaV2/ds-2015-04-16/Certificate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/Certificate.md "../../../goto/SdkForRubyV3/ds-2015-04-16/Certificate.md")
