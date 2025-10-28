# Permissions for AWS KMS–encrypted Amazon SNS

topics

The Amazon SNS topic you specify might be encrypted by AWS Key Management Service. To allow DevOps Guru to work
with encrypted topics, you must first create a AWS KMS key and then add the following
statement to the policy of the KMS key. For more information, see [Encrypting
messages published to Amazon SNS with AWS KMS](https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/ "https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/"), [Key identifiers (KeyId)](../../../kms/latest/developerguide/concepts.md#key-id "../../../kms/latest/developerguide/concepts.md#key-id")
in the _AWS KMS User Guide_, and [Data encryption](../../../sns/latest/dg/sns-data-encryption.md "../../../sns/latest/dg/sns-data-encryption.md") in the
_Amazon Simple Notification Service Developer Guide_.

###### Note

DevOps Guru currently supports encrypted topics for use within a single account.
Using an encrypted topic across multiple accounts is not supported at this time.
