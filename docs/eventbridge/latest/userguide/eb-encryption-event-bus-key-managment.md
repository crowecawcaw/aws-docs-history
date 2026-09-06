

# Maintaining AWS KMS encryption key access in EventBridge
<a name="eb-encryption-event-bus-key-managment"></a>

To ensure EventBridge always retains access to the necessary customer managed key:
+ Do not delete a customer managed key until you are sure all resources encrypted with it have been processed.

  When you perform any of the following operations, retain the previous key material to ensure EventBridge can continue to use it for previously-encrypted resources:
  + [Automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotating-keys-enable-disable)
  + [Manual key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-manually)
  + [Updating a key alias](https://docs.aws.amazon.com/kms/latest/developerguide/alias-manage.html#alias-update)

  In general, If you are considering deleting a AWS KMS key, disable it first and set a [CloudWatch alarm](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html) or similar mechanism to be certain that you'll never need to use the key to decrypt encrypted data.
+ Do not delete the key policy that provides EventBridge the permissions to use the key.

Other considerations include:
+ Specify customer managed keys for rule targets, as appropriate.

  When EventBridge sends an event to a rule target, the event is sent using Transport layer Security (TLS). However, what encryption is applied to the event as it is stored on the target depends on the encryption you have configured on the target itself.