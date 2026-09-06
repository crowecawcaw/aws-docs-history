

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Changing allowed tiers for a billing account
<a name="managing-billing-turn-on-tier"></a>

When you set up a billing account, the allowed CodeCatalyst tiers that you want to allow your space to use defaults to the free and paid tiers. You can turn the paid tiers on or off from your space's **Settings**. 

You must have the **Space administrator** role in CodeCatalyst and have administrator permissions for your account in AWS to manage billing.

1. In the AWS Management Console, make sure you are signed in with the same account that you want to manage. You will be automatically directed to a page in the AWS Management Console from the CodeCatalyst console.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose **Billing**.

   The **Billing details** page displays.

1. Choose **Manage billing in AWS**. This opens the Amazon CodeCatalyst Spaces in the AWS Management Console. If you are prompted to sign in, sign in to AWS, and then choose the button again to load the page.

1. Choose **Spaces**. The list of each space with a connection to the account you are signed in with, if any, displays.

1. Choose the account link for your CodeCatalyst space. The connection page is shown.

1. Under **Billing details**, choose **Edit**. The **Update allowed billing tiers** page displays.

1. To keep the default, leave the selection on **PAID (STANDARD, ENTERPRISE)**. To turn off paid tiers, deselect the **PAID (STANDARD, ENTERPRISE)** field.

1. Choose **Update**.