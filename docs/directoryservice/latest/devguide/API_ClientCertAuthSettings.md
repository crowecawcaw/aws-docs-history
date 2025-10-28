# ClientCertAuthSettings

Contains information about the client certificate authentication settings for the
`RegisterCertificate` and `DescribeCertificate` operations.

## Contents

**OCSPUrl**

Specifies the URL of the default OCSP server used to check for revocation status. A
secondary value to any OCSP address found in the AIA extension of the user certificate.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^(https?|ftp|file|ldaps?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;()]*[-a-zA-Z0-9+&@#/%=~_|()]`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ClientCertAuthSettings.md "../../../goto/SdkForCpp/ds-2015-04-16/ClientCertAuthSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ClientCertAuthSettings.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ClientCertAuthSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ClientCertAuthSettings.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ClientCertAuthSettings.md")
