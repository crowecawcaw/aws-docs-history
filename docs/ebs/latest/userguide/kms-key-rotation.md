# Rotate AWS KMS keys used for Amazon EBS encryption

Cryptographic best practices discourage extensive reuse of encryption keys.

To create new cryptographic material for use with Amazon EBS encryption, you can either
create a new customer managed key, and then change your applications to use that new KMS key.
Or, you can enable automatic key rotation for an existing customer managed key.

When you enable automatic key rotation for a customer managed key, AWS KMS generates new cryptographic
material for the KMS key every year. AWS KMS saves all previous versions of the cryptographic
material so that you can continue to decrypt and use volumes and snapshots previously encrypted
with that KMS key material. AWS KMS does not delete any rotated key material until you delete
the KMS key.

When you use a rotated customer managed key to encrypt a new volume or snapshot, AWS KMS uses the
current (new) key material. When you use a rotated customer managed key to decrypt a volume or snapshot,
AWS KMS uses the version of the cryptographic material that was used to encrypt it. If a volume
or snapshot is encrypted with a previous version of the cryptographic material, AWS KMS continues
to use that previous version to decrypt it. AWS KMS does not re-encrypt previously encrypted
volumes or snapshots to use the new cryptographic material after a key rotation. They remain
encrypted with the cryptographic material with which they were originally encrypted. You can
safely use a rotated customer managed key in applications and AWS services without code changes.

###### Note

- Automatic key rotation is supported only for symmetric customer managed keys with key
  material that AWS KMS creates.
- AWS KMS automatically rotates AWS managed keys every year. You can't enable or
  disable key rotation for AWS managed keys.
  For more information, see [Rotating KMS key](../../../kms/latest/developerguide/rotate-keys.md#rotate-keys-how-it-works "../../../kms/latest/developerguide/rotate-keys.md#rotate-keys-how-it-works") in the _AWS Key Management Service Developer Guide_.
