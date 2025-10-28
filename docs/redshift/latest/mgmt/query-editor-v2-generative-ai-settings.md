Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Updating generative SQL settings as an administrator

A user with the right IAM permissions can view and change **Generative SQL settings** for other users in the same AWS account.
This administrator must have permission `sqlworkbench:UpdateAccountQSqlSettings` in their IAM policy,
in addition to other permissions specified in the AWS managed policy for query editor v2.
For more information about managed policies, see
[Permissions
required to use the query editor v2](redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor-v2 "redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor-v2") .

###### For an administrator to turn on generative SQL chat for all users in the account

1. Choose the ![Settings](images/qev2-cog.png)
   **Settings** icon to show a menu of the different settings screens.
2. Then choose the
   ![Generative SQL settings](images/qev2-amazon-q.png)
   Generative SQL settings icon to show the **Q generative SQL settings** page.
3. Select **Q generative SQL settings** to turn on the generative SQL capability for users in the account.

After you turn on Amazon Q generative SQL, you can view the number of prompts left in your allocation.
The query editor v2 administrator can enable users in the account to use Amazon Q Developer Pro tier.
To use the Pro tier, set up your users with IAM Identity Center and subscribe each user to Amazon Q Developer Pro tier.
For information about setting up IAM Identity Center with Amazon Redshift, see
[Connect Redshift with AWS IAM Identity Center
for a single sign-on experience](redshift-iam-access-control-idp-connect.md "redshift-iam-access-control-idp-connect.md").
For information about Amazon Q Developer pricing, see
[Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").

When using Amazon Q Developer Free tier, the total number of prompts of all users of an AWS account is limited to 1,000 in a month.
When using Amazon Q Developer Pro tier, the total number of prompts that any individual user can submit is limited to 1,000 in a month.
You can view the number of prompts available on the **Settings** page.
For information about Amazon Q Developer pricing, see
[Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").
