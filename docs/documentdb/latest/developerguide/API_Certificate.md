# Certificate

A certificate authority (CA) certificate for an AWS account.

## Contents

###### Note

In the following list, the required parameters are described first.

**CertificateArn**

The Amazon Resource Name (ARN) for the certificate.

Example: `arn:aws:rds:us-east-1::cert:rds-ca-2019`

Type: String

Required: No

**CertificateIdentifier**

The unique key that identifies a certificate.

Example: `rds-ca-2019`

Type: String

Required: No

**CertificateType**

The type of the certificate.

Example: `CA`

Type: String

Required: No

**Thumbprint**

The thumbprint of the certificate.

Type: String

Required: No

**ValidFrom**

The starting date-time from which the certificate is valid.

Example: `2019-07-31T17:57:09Z`

Type: Timestamp

Required: No

**ValidTill**

The date-time after which the certificate is no longer valid.

Example: `2024-07-31T17:57:09Z`

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/Certificate.md "../../../goto/SdkForCpp/docdb-2014-10-31/Certificate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/Certificate.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/Certificate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/Certificate.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/Certificate.md")
