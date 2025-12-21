**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Locking a Vault using the AWS Command Line Interface

You can lock your vault using the AWS Command Line Interface. This will install a vault lock policy on the specified vault and return the lock
ID. You must complete the vault locking process within 24 hours else the vault lock policy
is removed from the vault.

## (Prerequisite) Setting Up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following topics in the
   _AWS Command Line Interface User Guide_:

[Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md")

[Configuring the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") 2. Verify your AWS CLI setup by entering the following commands at the command prompt. These
commands don't provide credentials explicitly, so the credentials of the default
profile are used.

    * Try using the help command.



    ```
    aws help
    ```
    * To get a list of Amazon Glacier vaults on the configured account, use the `list-vaults` command. Replace `123456789012` with your AWS account ID.



    ```
    aws glacier list-vaults --account-id `123456789012`
    ```
    * To see the current configuration data for the AWS CLI, use the `aws
     configure list` command.



    ```
    aws configure list
    ```

1. Use the `initiate-vault-lock` to install a vault lock policy and sets the lock state of the vault lock to `InProgress`.

```
aws glacier initiate-vault-lock --vault-name `examplevault` --account-id `111122223333` --policy file://lockconfig.json
```

2. The lock configuration is a JSON document as shown in the following example.
   Before using this command, replace the
   `VAULT_ARN` and `Principal` with the appropriate values for your use case.

To find the ARN of the vault you wish to lock, you can use the
`list-vaults` command.

```
{"Policy":"{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"Define-vault-lock\",\"Effect\":\"Deny\",\"Principal\":{\"AWS\":\"arn:aws:iam::`111122223333:root`\"},\"Action\":\"glacier:DeleteArchive\",\"Resource\":\"`VAULT_ARN`\",\"Condition\":{\"NumericLessThanEquals\":{\"glacier:ArchiveAgeinDays\":\"365\"}}}]}"}
```

3. After initiating the vault lock you should see the `lockId` returned.

```
{
    "lockId": "`LOCK_ID`"
}
```

To complete the vault lock You must run `complete-vault-lock` within 24 hours else the vault lock policy
is removed from the vault.

```
aws glacier complete-vault-lock --vault-name `examplevault` --account-id `111122223333` --lock-id `LOCK_ID`
```

## Related Sections

- [initiate-vault-lock](../../../cli/latest/reference/glacier/initiate-vault-lock.md "../../../cli/latest/reference/glacier/initiate-vault-lock.md") in the _AWS CLI Command Reference_
- [list-vaults](../../../cli/latest/reference/glacier/list-vaults.md "../../../cli/latest/reference/glacier/list-vaults.md") in the _AWS CLI Command Reference_
- [complete-vault-lock](../../../cli/latest/reference/glacier/complete-vault-lock.md "../../../cli/latest/reference/glacier/complete-vault-lock.md") in the _AWS CLI Command Reference_
- [Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md")
- [Abort Vault Lock (DELETE lock-policy)](api-AbortVaultLock.md "api-AbortVaultLock.md")
- [Complete Vault Lock (POST lockId)](api-CompleteVaultLock.md "api-CompleteVaultLock.md")
- [Get Vault Lock (GET lock-policy)](api-GetVaultLock.md "api-GetVaultLock.md")
- [Initiate Vault Lock (POST lock-policy)](api-InitiateVaultLock.md "api-InitiateVaultLock.md")
