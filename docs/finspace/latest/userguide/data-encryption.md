After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Data encryption in Amazon FinSpace

######

Amazon FinSpace uses the following data encryption features

- [Encryption at rest](#encryption-at-rest "#encryption-at-rest")
- [Encryption in transit](#encryption-in-transit "#encryption-in-transit")

## Encryption at rest

To encrypt data at rest, Amazon FinSpace uses a customer-owned key from the AWS Key Management Service
(AWS KMS). When you [create a FinSpace
environment](using-kdb-environment.md#create-kdb-environment "using-kdb-environment.md#create-kdb-environment"), you can specify the KMS key that you want to use to encrypt
all of the service data and metadata in your environment.

## Encryption in transit

Amazon FinSpace uses TLS 1.2 to encrypt data in transit.
