# Configuring Mailchimp

Before you can use AWS Glue to transfer from Mailchimp, you must meet the following
requirements:

## Minimum requirements

- You have an Mailchimp account with email and password. For more
  information about creating an account, see [Creating a Mailchimp
  account](mailchimp-create-account.md "mailchimp-create-account.md").
- You must have AWS Account created with the service access to AWS Glue.
- Ensure you have created one of the following resources. These resources
  provide credentials that AWS Glue uses to securely access your data when making
  authenticated calls to your account:
  - A Developer App that supports OAuth 2.0 authentication. For more information about creating a Developer App, see [Creating a Mailchimp
    account](mailchimp-create-account.md "mailchimp-create-account.md").

If you meet these requirements, you’re ready to connect AWS Glue to your Mailchimp
account. For typical connections, you don't need do anything else in Mailchimp.
