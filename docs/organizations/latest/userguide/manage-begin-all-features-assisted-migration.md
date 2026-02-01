# Assisted migration process to enable all features with Organizations

If you are an Enterprise customer, it can be difficult to complete the standard migration process due to the large number of accounts you might manage.
For example, you might have difficulty obtaining approval to migrate all invited accounts in large organizations.

Assisted migration helps with this process by enabling customers with an Enterprise Support plan to request that AWS migrate their organization to all
features on your behalf. This process requires that you sign an agreement affirming that you own all accounts. Then, all member accounts in the organization will be notified by email of the migration, and the email notifications will trigger a a 14-day waiting period. This waiting period provides accounts time to leave the organization before the migration to all features takes effect.

AWS Management Console

###### To migrate to all features with assisted migration

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page choose **Enable all feature** and then select **Assisted migration**.
3. Read the terms and conditions of the agreement, choose **Accept** and choose **Begin process to enable all features** to start the migration.

###### Note

**Beginning the assisted migration process overrides the standard migration process**

If you are currently enabling all features using the standard migration process, it will be canceled, and the assisted migration process will kick-off.

**The assisted migration process is one-way and cannot be rolled back**

After you have begun the assisted migration process, it cannot be rolled back. You will need to wait 90 days until the process expires if you want to go through the standard process instead.

If you use assisted migration, you do not need to worry about accessing your invited account as the root user to accept the migration to all features.

You can reach out to your Technical Account Manager (TAM) for exact details, progress, and timelines for the assisted migration.
