**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Amazon Glacier Vault Lock

The following topics describe how to lock a vault in Amazon Glacier and how to use Vault Lock
policies.

###### Topics

- [Vault Locking Overview](#vault-lock-overview "#vault-lock-overview")
- [Locking a Vault by Using the Amazon Glacier API](vault-lock-how-to-api.md "vault-lock-how-to-api.md")
- [Locking a Vault using the AWS Command Line Interface](vault-lock-how-to-cli.md "vault-lock-how-to-cli.md")
- [Locking a Vault by Using the Amazon Glacier Console](vault-lock-walkthrough.md "vault-lock-walkthrough.md")

## Vault Locking Overview

Amazon Glacier Vault Lock helps you to easily deploy and enforce compliance controls for
individual Amazon Glacier vaults with a Vault Lock policy. You can specify controls such as
"write once read many" (WORM) in a Vault Lock policy and lock the policy from future edits.

###### Important

After a Vault Lock policy is locked, the policy can no longer be changed or
deleted.

Amazon Glacier enforces the controls set in the Vault Lock policy to help achieve your
compliance objectives. For example, you can use Vault Lock policies to enforce data
retention. You can deploy a variety of compliance controls in a Vault Lock policy by using
the AWS Identity and Access Management (IAM) policy language. For more information about Vault Lock policies, see
[Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md").

A Vault Lock policy is different from a vault access policy. Both policies govern access
controls to your vault. However, a Vault Lock policy can be locked to prevent future
changes, which provides strong enforcement for your compliance controls. You can use the
Vault Lock policy to deploy regulatory and compliance controls, which typically require
tight controls on data access.

###### Important

We recommend that you first create a vault, complete a Vault Lock policy, and then
upload your archives to the vault so that the policy will be applied to them.

In contrast, you use a vault access policy to implement access controls that are not
compliance related, temporary, and subject to frequent modification. You can use Vault lock
and vault access policies together. For example, you can implement time-based
data-retention rules in the Vault Lock policy (deny deletes), and grant read access to
designated third parties or your business partners (allow reads) in your vault access
policy.

Locking a vault takes two steps:

1. Initiate the lock by attaching a Vault Lock policy to your vault, which sets the
   lock to an in-progress state and returns a lock ID. While the policy is in the
   in-progress state, you have 24 hours to validate your Vault Lock policy before the
   lock ID expires. To prevent your vault from exiting the in-progress state, you must
   complete the Vault Lock process within these 24 hours. Otherwise, your Vault Lock
   policy will be deleted.
2. Use the lock ID to complete the lock process. If the Vault Lock policy doesn't
   work as expected, you can stop the Vault Lock process and restart from the beginning.
   For information about how to use the Amazon Glacier API to lock a vault, see [Locking a Vault by Using the Amazon Glacier API](vault-lock-how-to-api.md "vault-lock-how-to-api.md").
