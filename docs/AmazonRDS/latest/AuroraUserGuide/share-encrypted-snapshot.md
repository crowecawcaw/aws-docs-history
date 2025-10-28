# Sharing encrypted snapshots

You can share DB cluster snapshots that have been encrypted "at rest" using the AES-256 encryption algorithm, as described in
[Encrypting Amazon Aurora
resources](Overview.md "Overview.md").

The following restrictions apply to sharing encrypted snapshots:

- You can't share encrypted snapshots as public.
- You can't share a snapshot that has been encrypted using the default KMS key of the AWS account that shared the
  snapshot.

For more information about AWS KMS key management for Amazon RDS, see [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").
To work around the default KMS key issue, perform the following tasks:

1. [Create a customer managed key and give access to it](#share-encrypted-snapshot.cmk "#share-encrypted-snapshot.cmk").
2. [Copy and share the snapshot from the source account](#share-encrypted-snapshot.share "#share-encrypted-snapshot.share").
3. [Copy the shared snapshot in the target account](#share-encrypted-snapshot.target "#share-encrypted-snapshot.target").

## Create a customer managed key and give access to it

First you create a custom KMS key in the same AWS Region as the encrypted DB cluster snapshot. While creating the
customer managed key, you give access to it for another AWS account.

###### To create a customer managed key and give access to it

1. Sign in to the AWS Management Console from the source AWS account.
2. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
3. To change the AWS Region, use the Region selector in the upper-right corner of the page.
4. In the navigation pane, choose **Customer managed keys**.
5. Choose **Create key**.
6. On the **Configure key** page:
   1. For **Key type**, select **Symmetric**.
   2. For **Key usage**, select **Encrypt and decrypt**.
   3. Expand **Advanced options**.
   4. For **Key material origin**, select **KMS**.
   5. For **Regionality**, select **Single-Region key**.
   6. Choose **Next**.

7. On the **Add labels** page:
   1. For **Alias**. enter a display name for your KMS key, for example
      `share-snapshot`.
   2. (Optional) Enter a description for your KMS key.
   3. (Optional) Add tags to your KMS key.
   4. Choose **Next**.

8. On the **Define key administrative permissions** page, choose **Next.**
9. On the **Define key usage permissions** page:
   1. For **Other AWS accounts**, choose **Add another
      AWS account**.
   2. Enter the ID of the AWS account to which you want to give access.

   You can give access to multiple AWS accounts. 3. Choose **Next**.

10. Review your KMS key, then choose **Finish**.

## Copy and share the snapshot from the source account

Next you copy the source DB cluster snapshot to a new snapshot using the customer managed key. Then you share it with the target
AWS account.

###### To copy and share the snapshot

1. Sign in to the AWS Management Console from the source AWS account.
2. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/")
3. In the navigation pane, choose **Snapshots**.
4. Select the DB cluster snapshot you want to copy.
5. For **Actions**, choose **Copy snapshot**.
6. On the **Copy snapshot** page:
   1. For **Destination Region**, choose the AWS Region where you created the customer managed key in
      the previous procedure.
   2. Enter the name of the DB cluster snapshot copy in **New DB Snapshot Identifier**.
   3. For **AWS KMS key**, choose the customer managed key that you created.

   ![Choose the customer managed key.](images/copy-encrypted-snapshot.png) 4. Choose **Copy snapshot**.

7. When the snapshot copy is available, select it.
8. For **Actions**, choose **Share snapshot**.
9. On the **Snapshot permissions** page:
   1. Enter the **AWS account ID** with which you're sharing the snapshot copy, then choose
      **Add**.
   2. Choose **Save**.The snapshot is shared.

## Copy the shared snapshot in the target account

Now you can copy the shared snapshot in the target AWS account.

###### To copy the shared snapshot

1. Sign in to the AWS Management Console from the target AWS account.
2. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/")
3. In the navigation pane, choose **Snapshots**.
4. Choose the **Shared with me** tab.
5. Select the shared snapshot.
6. For **Actions**, choose **Copy snapshot**.
7. Choose your settings for copying the snapshot as in the previous procedure, but use an AWS KMS key that belongs
   to the target account.

Choose **Copy snapshot**.
