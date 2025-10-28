# Create and use user-generated

KMS keys

This section describes how to create and use your own KMS keys, instead of using the
master key administered by Amazon Kinesis.

## Create user-generated KMS keys

For instructions on creating your own keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_. After you create keys for your account,
the Kinesis Data Streams service returns these keys in the **KMS master key**
list.

## Use user-generated KMS keys

After the correct permissions are applied to your consumers, producers, and
administrators, you can use custom KMS keys in your own AWS account or another
AWS account. All KMS master keys in your account appear in the **KMS
Master Key** list within the AWS Management Console.

To use custom KMS master keys located in another account, you need permissions to
use those keys. You must also specify the ARN of the KMS master key in the ARN input
box in the AWS Management Console.
