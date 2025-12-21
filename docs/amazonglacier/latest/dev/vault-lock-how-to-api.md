**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Locking a Vault by Using the Amazon Glacier API

To lock your vault with the Amazon Glacier API, you first call [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md") with a Vault
Lock policy that specifies the controls that you want to deploy. The `Initiate Vault
 Lock` operation attaches the policy to your vault, transitions the Vault Lock to
the in-progress state, and returns a unique lock ID. After the Vault Lock enters the
in-progress state, you have 24 hours to complete the lock by calling [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md") with the lock ID
that was returned from the `Initiate Vault Lock` call.

###### Important

- We recommend that you first create a vault, complete a Vault Lock policy, and
  then upload your archives to the vault so that the policy will be applied to
  them.
- After the Vault Lock policy is locked, it cannot be changed or deleted.
  If you don't complete the Vault Lock process within 24 hours after entering the
  in-progress state, your vault automatically exits the in-progress state, and the Vault Lock
  policy is removed. You can call `Initiate Vault Lock` again to install a new
  Vault Lock policy and transition into the in-progress state.

The in-progress state provides the opportunity to test your Vault Lock policy before you
lock it. Your Vault Lock policy takes full effect during the in-progress state just as if
the vault has been locked, except that you can remove the policy by calling [Abort Vault Lock (DELETE lock-policy)](api-AbortVaultLock.md "api-AbortVaultLock.md"). To fine-tune your
policy, you can repeat the `Abort Vault Lock`/`Initiate Vault Lock`
combination as many times as necessary to validate your Vault Lock policy changes.

After you validate the Vault Lock policy, you can call [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md") with the most
recent lock ID to complete the vault locking process. Your vault transitions to a locked
state, where the Vault Lock policy is unchangeable and can no longer be removed by calling
`Abort Vault Lock`.

## Related Sections

- [Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md")
- [Abort Vault Lock (DELETE lock-policy)](api-AbortVaultLock.md "api-AbortVaultLock.md")
- [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md")
- [Get Vault Lock (GET lock-policy)](api-GetVaultLock.md "api-GetVaultLock.md")
- [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md")
