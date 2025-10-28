# Configure the AWS access portal

As an administrator, you can customize the AWS access portal to meet your organization's needs and ensure users can easily access their authorized resources.

## What you can configure

**AWS access portal activation**: Set up initial user access to the AWS access portal, including user credential activation and first-time sign-in processes.

**Custom AWS access portal URL (optional)**: Personalize your
organization's AWS access portal URL from the default format
(`d-xxxxxxxxxx.awsapps.com/start`) to a more recognizable subdomain
(`your-company.awsapps.com/start`).

###### Before you begin

Ensure you have administrative access to IAM Identity Center, verify that IAM Identity Center is set up as either an [organization instance](organization-instances-identity-center.md "organization-instances-identity-center.md") or
[account instance](account-instances-identity-center.md "account-instances-identity-center.md"), and plan your custom subdomain name (this is a one-time configuration that cannot be changed later).

Once configured, users can access the AWS access portal using the custom URL and follow
the activation process you've established for your organization.

###### Topics

- [Activating the AWS access portal for first-time IAM Identity Center
  users](howtoactivateaccount.md "howtoactivateaccount.md")
- [Customizing the AWS access portal URL](howtochangeURL.md "howtochangeURL.md")
- [Confirm users can sign in to the AWS access portal](howtosigninprocedure.md "howtosigninprocedure.md")
