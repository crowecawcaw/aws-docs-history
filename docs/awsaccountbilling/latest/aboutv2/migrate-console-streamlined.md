# Using recommended actions to bulk migrate legacy policies

You can migrate all of your legacy policies by using the fine-grained actions mapped by AWS. For AWS Organizations, this applies to all legacy policies across all accounts. Once you complete your migration process, the fine-grained actions are effective. You have the option to test the bulk migration process using test accounts before committing your entire organization. For more information, see the following section.

###### To migrate all of your policies using fine-grained actions mapped by AWS

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the search bar at the top of the page, enter `Bulk Policy Migrator`.
3. On the **Manage new IAM actions** page, choose **Confirm and migrate**.
4. Remain on the **Migration in progress** page until the migration is complete. See the status bar for progress.
5. Once the **Migration in progress** section updates to **Migration successful**, you are redirected to the **Manage new IAM actions** page.

## Testing your bulk migration

You can test the bulk migration from legacy policies to AWS recommended fine-grained actions using test accounts before committing to migrating your entire organization. Once you complete your migration process on your test accounts, the fine-grained actions are applied to your test accounts.

###### To use your test accounts for bulk migration

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the search bar at the top of the page, enter `Bulk Policy Migrator`.
3. On the **Manage new IAM actions** page, choose **Customize**.
4. Once the accounts and policies load in the **Migrate accounts** table, select one or more test accounts from the list of AWS accounts.
5. (Optional) To change the mapping between your legacy policy and AWS recommended fine-grained actions, choose **View default mapping**. Change the mapping, and choose **Save**.
6. Choose **Confirm and migrate**.
7. Remain on the console page until migration is complete.
