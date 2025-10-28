# Customizing actions to bulk migrate legacy policies

You can customize your bulk migration in various ways, instead of using the AWS recommended action for all of your accounts. You have the option to review any changes needed to your legacy policies before migrating, choose specific accounts in your Organizations to migrate at a time, and change the access range by updating the mapped fine-grained actions.

###### To review your affected policies before bulk migrating

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the search bar at the top of the page, enter `Bulk Policy Migrator`.
3. On the **Manage new IAM actions** page, choose **Customize**.
4. Once the accounts and policies load in the **Migrate accounts** table, choose the number in the **Number of affected IAM policies** column to see the affected policies. You will also see when that policy was used last to access the Billing and Cost Management consoles.
5. Choose a policy name to open it in the IAM console to view definitions and manually update the policy.

###### Notes

    * Doing this might log you out of your current account if the policy is from another member account.
    * You won't be redirected to the corresponding IAM page if your current account has a bulk migration in progress.

6. (Optional) Choose **View default mapping** to see the legacy policies to understand the fine-grained policy mapped by AWS.

###### To migrate a select group of accounts to migrate from your organization

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the search bar at the top of the page, enter `Bulk Policy Migrator`.
3. On the **Manage new IAM actions** page, choose **Customize**.
4. Once the accounts and policies load in the **Migrate accounts** table, select one or more accounts to migrate.
5. Choose **Confirm and migrate**.
6. Remain on the console page until migration is complete.

###### To change the access range by updating the mapped fine-grained actions

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the search bar at the top of the page, enter `Bulk Policy Migrator`.
3. On the **Manage new IAM actions** page, choose **Customize**.
4. Choose **View default mapping**.
5. Choose **Edit**.
6. Add or remove IAM actions for the Billing and Cost Management services you want to control access to. For more information about fine-grained actions and the access it controls, see [Mapping fine-grained IAM
   actions reference](migrate-granularaccess-iam-mapping-reference.md "migrate-granularaccess-iam-mapping-reference.md").
7. Choose **Save changes**.
   The updated mapping is used for all future migrations from the account you're logged into. This can be changed at any time.
