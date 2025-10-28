Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Setting up a billing account

To set up billing, you must add an authorized AWS account to your CodeCatalyst space
and configure it for billing. Before you can set up a billing account, you must work
with your AWS administrator to complete the prerequisites in the following
procedure.

Where necessary, these steps link you to the procedures in this guide for adding the
AWS account you want to use for billing to your space by creating a
connection.

You must have the **Space administrator** role in CodeCatalyst and have
administrator permissions for your account in AWS to manage billing.

## Step 1: Add the billing account

to your space

To choose a new account for billing, you must have completed the steps to add it
to your space. Complete the steps as detailed in [Administering connected accounts](managing-accounts.md "managing-accounts.md").

You must have the **Space administrator** role in CodeCatalyst and have
administrator permissions for your account in AWS to manage billing.

## Step 2: Choose the billing

account in CodeCatalyst

Next, specify the connected account as a billing account.

The account ID is now authorized for billing. This is the account that you will
add to your space, and it is available in the list of options. Only
AWS accounts that have been added to your space will show in the list.

You must have the **Space administrator** role to manage billing and
accounts for your space.

###### To designate an added AWS account to a CodeCatalyst space for

billing

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space. Choose **Settings**,
   and then choose **Billing**.

The **Billing details** page displays. 3. Choose **Add an AWS account**.

If the space already has a designated billing account that you want
to change, choose the **Edit** button next to the
**AWS account name** field.

The **Change AWS billing account** page
displays. 4. From the **Choose from AWS accounts already associated with your
space** dropdown menu, choose the name of another added
account for your space that you want to designate as the billing
account for your CodeCatalyst space. The account name must be for an account
that has been added to your space with a connection and is listed in
the **AWS accounts list for your space**. 5. Choose **Change billing account**.
