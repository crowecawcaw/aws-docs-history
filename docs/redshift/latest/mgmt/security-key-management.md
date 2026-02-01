Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Key management

You can configure your environment to protect data with keys:

- Amazon Redshift automatically integrates with AWS Key Management Service (AWS KMS) for key
  management. AWS KMS uses envelope encryption. For more information, see
  [Envelope Encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping").
- When encryption keys are managed in AWS KMS, Amazon Redshift uses a four-tier, key-based architecture for encryption. The architecture consists of
  randomly generated AES-256 data encryption keys, a database key, a cluster key, and a
  root key. For more information, see
  [How Amazon Redshift Uses AWS KMS](../../../kms/latest/developerguide/services-redshift.md "../../../kms/latest/developerguide/services-redshift.md").
- You can create your own customer managed key in AWS KMS. For more information, see
  [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
- You can also import your own key material for new AWS KMS keys. For more information, see
  [Importing Key Material in AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide/importing-keys.md "../../../kms/latest/developerguide/importing-keys.md").
- Amazon Redshift supports management of encryption keys in external hardware security modules (HSMs).
  The HSM can be on-premises or can be AWS CloudHSM. When you use an HSM, you
  must use client and server certificates to configure a trusted connection
  between Amazon Redshift and your HSM. Amazon Redshift supports only AWS CloudHSM Classic for
  key management. For more information, see [Encryption using hardware security
  modules](working-with-db-encryption.md#working-with-HSM "working-with-db-encryption.md#working-with-HSM"). For information about AWS CloudHSM, see
  [What is AWS CloudHSM?](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md")
- You can rotate encryption keys for encrypted clusters.. For more information, see
  [Encryption key rotation](working-with-db-encryption.md#working-with-key-rotation "working-with-db-encryption.md#working-with-key-rotation").
