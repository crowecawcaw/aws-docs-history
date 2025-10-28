**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Locking a Vault by Using the Amazon Glacier Console

Amazon Glacier Vault Lock helps you to easily deploy and enforce compliance controls for
individual Amazon Glacier vaults with a Vault Lock policy. For more information about Amazon Glacier
Vault Lock, see [Amazon Glacier Access Control with Vault Lock Policies](vault-lock-policy.md "vault-lock-policy.md").

###### Important

- We recommend that you first create a vault, complete a Vault Lock policy, and
  then upload your archives to the vault so that the policy will be applied to
  them.
- After the Vault Lock policy is locked, it cannot be changed or deleted.

###### To initiate a Vault Lock policy on your vault by using the Amazon Glacier console

You initiate the lock by attaching a Vault Lock policy to your vault, which sets the
lock to an in-progress state and returns a lock ID. While the policy is in the
in-progress state, you have 24 hours to validate your Vault Lock policy before the lock
ID expires.

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. Under **Select a Region**, select an AWS Region from the Region
   selector.
3. In the left navigation pane, choose **Vaults**.
4. On the **Vaults** page, choose **Create
   vault**.
5. Create a new vault.

###### Important

We recommend that you first create a vault, complete a Vault Lock policy, and then upload
your archives to the vault so that the policy will be applied to them. 6. Choose your new vault from the **Vaults** list. 7. Choose the **Vault policies** tab. 8. In the **Vault Lock policy** section, choose **Initiate
Vault Lock policy**. 9. On the **Initiate Vault Lock policy** page, specify the record retention
controls in your Vault Lock policy in text format in the standard text box.

###### Note

You can specify the record retention controls in a Vault Lock policy in text
format and initiate the Vault Lock by calling the `Initiate Vault Lock`
API operation or through the interactive UI in the Amazon Glacier console. For
information about formatting your Vault Lock policy, see [Amazon Glacier Vault Lock Policy Examples](vault-lock-policy.md#vault-lock-policy-example-deny-delete-archive-age "vault-lock-policy.md#vault-lock-policy-example-deny-delete-archive-age"). 10. Choose **Save changes**. 11. In the **Record Vault Lock ID** dialog box, copy your **Lock
ID** and save it in a safe place.

###### Important

After the Vault Lock policy has been initiated, you have 24 hours to validate the
policy and complete the lock process. To complete the lock process, you must
provide the lock ID. If it's not provided within 24 hours, the lock ID expires and
your in-progress policy is deleted. 12. After saving your lock ID in a safe place, choose **Close**. 13. Test your Vault Lock policy within the next 24 hours. If the policy is working as intended,
choose **Complete Vault Lock policy**. 14. In the **Complete Vault Lock** dialog box, select the check box to
acknowledge that completing the Vault Lock policy process is irreversible. 15. Enter your provided **Lock ID** in the text box. 16. Choose **Complete Vault Lock**.
