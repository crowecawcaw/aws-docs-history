

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Security considerations
<a name="considerations-security"></a>

## Data encryption
<a name="data-encryption"></a>
+ Messages remain encrypted from sender to Nitro Enclave
+ Only your Customer KMS keys can decrypt the data retention bot's private keys
+ Decrypted content is immediately re-encrypted with your KMS key before leaving the enclave

## Nitro enclave attestation
<a name="nitro-enclave"></a>

AWS nitro enclaves provide cryptographic attestation:
+ Each enclave version has a unique attestation
+ AWS KMS records values from the enclave's attestation document, including its Platform Configuration Registers (PCR0, PCR1, and PCR2), in CloudTrail during decryption events, so you can inspect them.

## Customer KMS key management
<a name="kms-management"></a>

You maintain full control over your KMS keys:
+ **Key rotation**: Enable automatic key rotation in KMS settings
+ **Access revocation**: Disable the KMS key to immediately stop all decryption
+ **Audit trail**: CloudTrail logs all KMS key usage
+ **Key policies**: Customize key policies to restrict access

## Data sovereignty
<a name="data-sovereignty"></a>

All decrypted data remains in your AWS account:
+ S3 bucket is in your account and region
+ You control bucket policies and access
+ Data never leaves your AWS account boundary
+ You can enable S3 versioning, lifecycle policies, and replication

## IAM roles and permissions
<a name="permissions-iam"></a>

The CloudFormation template creates minimal IAM permissions:
+ Wickr service role can only write to your specific S3 bucket
+ Decryption Lambda can only read from your S3 bucket and use your KMS key
+ All actions logged in CloudTrail