# Provision accounts in the AWS Control Tower console

The following procedure describes how to create and provision accounts as a user in
IAM Identity Center through the AWS Control Tower console. This procedure also is referred to as _manual account
provisioning_. Optionally, you may be able to provision AWS Control Tower accounts
programmatically, with the AWS CLI, with Service Catalog APIs, or with AWS Control Tower Account Factory for Terraform
(AFT), or automatically enroll an existing account into a registered OU. You may be able to provision customized accounts in the console if you've
previously set up custom blueprints. For more information about customization, see [Customize accounts with Account Factory
Customization (AFC)](af-customization-page.md "af-customization-page.md").

###### To provision accounts individually in the AWS Control Tower console, as a user

1. Sign in to AWS and navigate to the AWS Control Tower console..
2. From the left navigation, choose **Organizations** to view the **Organization** page.
3. From the upper right, choose **Create resources**.
4. In the dropdown menu, choose **Create account**.
5. Fill in the information on the page, and keep the following in mind:
   - The **Account email** must be an email address that
     isn't already associated with an AWS account.
   - The display name is the name you want to see for this account.

6. Fill in the fields to define your **Access configuration**, with an IAM Identity Center email address and user name.
7. Select a registered OU from the dropdown list, to indicate the OU in which you'd like to provision the account.
8. Optionally use a pre-defined blueprint to provision your account with customized resources. You can do this task later.
9. Review your account selections, and then choose **Create account**, in the lower right.
10. Your account is now being provisioned. It can take a few minutes to complete.
    You can refresh the page to update the displayed status information.

###### Note

Up to five accounts can be provisioned at a time.
