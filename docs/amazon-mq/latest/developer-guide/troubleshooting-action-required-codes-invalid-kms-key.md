# RabbitMQ on Amazon MQ: Invalid AWS Key Management Service Key

RabbitMQ on Amazon MQ will raise an INVALID_KMS_KEY critical action required code when a broker created
with a customer managed AWS KMS key(CMK) detects that the AWS Key Management Service (KMS) key is disabled.
A RabbitMQ broker with a CMK periodically verifies that the KMS key is enabled and the broker has
all necessary grants. If RabbitMQ cannot verify that the key is enabled,
the broker is quarantined and RabbitMQ will return INVALID_KMS_KEY.

Without an active KMS key, the broker does not have basic permissions for customer managed KMS keys.
The broker cannot perform cryptographic operations using your key until you re-enable your key
and the broker restarts. A RabbitMQ broker with a disabled KMS key is quarantined to prevent deterioration.
After RabbitMQ determines the KMS key is active again, your broker is removed from quarantine.
Amazon MQ does not restart a broker with a disabled KMS key and returns an exception for `RebootBroker`
API operations as long as the broker continues to have an invalid KMS key.

## Diagnosing and addressing INVALID_KMS_KEY

To diagnose and address the INVALID_KMS_KEY action required code,
you must use the AWS Command Line Interface (CLI) and the AWS Key Management Service console.

###### To re-enable your KMS key

1. Call the `DescribeBroker` method to retrieve the `kmsKeyId`
   for your CMK broker.
2. Sign in to the AWS Key Management Service console.
3. On the **Customer managed keys** page, locate the KMS Key ID of the problematic broker and verify the status is
   **Enabled**.
4. If your KMS key has been disabled, re-enable the key by choosing **Key Actions**,
   then choose **Enable**.
   After your key has been re-enabled, you must wait for RabbitMQ to remove the broker
   from quarantine.

To verify that the necessary grants are still associated with the broker's KMS key,
call the `ListGrant`ListGrant method to verify that `mq_rabbit_grant` and `mq_grant` are present.
If the KMS grant or key has been deleted, you must delete the broker and create a new one with all necessary grants.
For steps on deleting a broker, see [Deleting a broker](amazon-mq-deleting-broker.md "amazon-mq-deleting-broker.md").

To prevent the INVALID_KMS_KEY critical action required code, do not manually delete or disable a KMS key or CMK grant.
If you wish to delete the key, delete the broker first.
