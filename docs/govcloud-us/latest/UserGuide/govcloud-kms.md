# AWS Key Management Service in AWS GovCloud (US)

AWS Key Management Service (KMS) is an encryption and key management service scaled for the cloud. KMS keys and functionality are used by other AWS services, and you can use them to protect data in your own applications that use AWS.

## How AWS KMS differs for AWS GovCloud (US)

- External key store proxies in the AWS GovCloud (US) Region must support HTTP/1.1 or later
  and TLS 1.2 or later with at least one of these cipher suites: TLS_AES_256_GCM_SHA384 (TLS
  1.3), TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (TLS 1.2),
  TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (TLS 1.2). The AWS GovCloud (US) Region does not
  support the TLS_CHACHA20_POLY1305_SHA256 cipher suite. For more information, see the
  open-source [external key store
  proxy API specification](https://github.com/aws/aws-kms-xksproxy-api-spec/ "https://github.com/aws/aws-kms-xksproxy-api-spec/") that AWS KMS publishes.

## Documentation for AWS Key Management Service

[AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS KMS metadata is not permitted to contain export-controlled data. Do not enter
  export-controlled data in the following fields:
  - Alias
  - Descriptions
  - Key policy documents, including key administrators and key users
  - Resource tags: Key
  - Resource tags: Value

- The [Encryption Context](../../../kms/latest/developerguide/encrypt-context.md "../../../kms/latest/developerguide/encrypt-context.md") is
  outside the Export-Controlled Content.
- AWS KMS generated metadata will not contain export-controlled data:
  - Key ID
  - Key ARN
