# Provision accounts in the Service Catalog console, with Account Factory

The following procedure describes how to create and provision accounts as a user in
IAM Identity Center through AWS Service Catalog. This procedure also is referred to as _advanced account provisioning_, or _manual account
provisioning_. Optionally, you may be able to provision AWS Control Tower accounts
programmatically, with the AWS CLI, with Service Catalog APIs, or with AWS Control Tower Account Factory for Terraform
(AFT). You may be able to provision customized accounts in the console if you've
previously set up custom blueprints. For more information about customization, see [Customize accounts with Account Factory
Customization (AFC)](af-customization-page.md "af-customization-page.md").

###### To provision accounts individually in Account Factory, as a user

1. Sign in from your user portal URL.
2. From **Your applications**, choose **AWS
   Account**.
3. From the list of accounts, choose the account ID for your management account.
   This ID may also have a label, for example, **(Management)**.
4. From **AWSServiceCatalogEndUserAccess**, choose
   **Management console**. This opens the AWS Management Console for this
   user in this account.
5. Ensure that you've selected the correct AWS Region for provisioning
   accounts, which should be your AWS Control Tower Region.
6. Search for and choose **Service Catalog** to open the Service Catalog
   console.
7. In the navigation pane, choose **Products**.
8. Select **AWS Control Tower Account Factory**, then choose the
   **Launch product** button. This selection starts the wizard
   to provision a new account.
9. Fill in the information, and keep the following in mind:
   - The **SSOUserEmail** can be a new email address, or
     the email address associated with an existing IAM Identity Center user. Whichever you
     choose, this user will have administrative access to the account you're
     provisioning.
   - The **AccountEmail** must be an email address that
     isn't already associated with an AWS account. If you used a new email
     address in **SSOUserEmail**, you can use that email
     address here.

10. Don't define **TagOptions** and don't enable
    **Notifications**, otherwise the account can fail to be
    provisioned. When you're finished, choose **Launch
    product**.
11. Review your account settings, and then choose **Launch**.
    Don't create a resource plan, otherwise the account will fail to be
    provisioned.
12. Your account is now being provisioned. It can take a few minutes to complete.
    You can refresh the page to update the displayed status information.

###### Note

Up to five accounts can be provisioned at a time.
