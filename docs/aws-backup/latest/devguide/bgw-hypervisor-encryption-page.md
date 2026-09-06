

# Virtual machine hypervisor credential encryption
<a name="bgw-hypervisor-encryption-page"></a>

Virtual machines [ managed by a hypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-hypervisors.html) use [AWS Backup Gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-gateways.html) to connect on-premises systems to AWS Backup. It is important that hypervisors have the same robust and reliable security. This security can be achieved by encrypting the hypervisor, either by AWS owned keys or by customer managed keys.

## AWS owned and customer managed keys
<a name="bgw-encryption-keys"></a>

AWS Backup provides encryption for hypervisor credentials to protect sensitive customer login information using **AWS owned encryption** keys. You have the option of using **customer managed keys **instead.

By default, the keys used to encrypt credentials in your hypervisor are **AWS owned keys**. AWS Backup uses these keys to automatically encrypt hypervisor credentials. You can neither view, manage, or use AWS owned keys, nor can you audit their use. However, you don't have to take any action or change any programs to protect the keys that encrypt your data. For more information, see AWS owned keys in the [* AWS KMS Developer Guide*](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt).

Alternatively, credentials can be encrypted using *Customer managed keys*. AWS Backup supports the use of symmetric customer-managed keys that you create, own, and manage to perform your encryption. Because you have full control of this encryption, you can perform tasks such as:
+ Establishing and maintaining key policies
+ Establishing and maintaining IAM policies and grants
+ Enabling and disabling key policies
+ Rotating key cryptographic material
+ Adding tags
+ Creating key aliases
+ Scheduling keys for deletion

When you use a customer managed key, AWS Backup validates whether your role has permission to decrypt using this key (prior to a backup or restore job being run). You must add the `kms:Decrypt` action to the role used to start a backup or restore job.

Because the `kms:Decrypt` action cannot be added to the default backup role, you must use a role other than the default backup role to use customer managed keys.

For more information, see [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.

## Grant required when using customer managed keys
<a name="encryption-grant"></a>

AWS KMS requires a [ grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) to use your customer managed key. When you import a [ hypervisor configuration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ImportHypervisorConfiguration.html) encrypted with a customer managed key, AWS Backup creates a grant on your behalf by sending a [`CreateGrant`](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) request to AWS KMS. AWS Backup uses grants to access a KMS key in a customer account. 

You can revoke access to the grant, or remove AWS Backup's access to the customer managed key at any time. If you do, all your gateways associated with your hypervisor can no longer access the hypervisor's username and password encrypted by the customer managed key, which will affect your backup and restore jobs. Specifically, backup and restore jobs you perform on the virtual machines in this hypervisor will fail.

Backup gateway uses the `RetireGrant` operation to remove a grant when you delete a hypervisor.

## Monitoring encryption keys
<a name="monitoring-encryption-keys"></a>

When you use an AWS KMS customer managed key with your AWS Backup resources, you can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) or [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to track requests that AWS Backup sends to AWS KMS.

Look for AWS CloudTrail events with the following `"eventName"` fields to for monitor AWS KMS operations called by AWS Backup to access data encrypted by your customer managed key:
+ `"eventName": "CreateGrant"`
+ `"eventName": "Decrypt"`
+ `"eventName": "Encrypt"`
+ `"eventName": "DescribeKey"`