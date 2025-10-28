# Key management

Amazon Q Business encrypts the contents of your index using the following types of
keys:

- An AWS-owned AWS KMS. This is the default.
- A customer-managed KMS key. You can create the key when you are creating an
  Amazon Q application environment, retriever, index, web experience, data source, or plugins, or
  you can create the key using the AWS KMS console. Select a symmetric encryption
  customer-managed KMS key.

###### Important

Amazon Q does not support asymmetric KMS keys. For more information, see [Using Symmetric and Asymmetric
Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the _AWS Key Management Service Developer
Guide_.
