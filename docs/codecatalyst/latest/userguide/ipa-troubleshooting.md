Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting

This section can help you troubleshoot some common issues you might encounter while
accessing your Amazon CodeCatalyst profile.

## Problems signing up

You might encounter some issues while signing up. We've got some solutions.

### My email address is already in use

If the email that you entered is already in use and you recognize it as your own,
then you may already have a profile with us. Sign in with this existing identity. If
you do not own the existing email, then sign up with a different, unused one.

### I can't complete email verification

If you have not received your verification email

1. Check your spam, junk, and deleted items folder.

###### Note

This verification email comes from either the address
`no-reply@signin.aws` or
`no-reply@login.awsapps.com`. We recommend that you
configure your mail system so that it accepts emails from these sender
email addresses and does not handle them as junk or spam. 2. Wait 5 minutes and refresh your inbox. Check your spam, junk, and deleted
items folder again. 3. If you still don't see your verification email, choose **Resend
code**. If you exited that page already, then restart your
workflow for signing up with [Amazon CodeCatalyst](https://codecatalyst.aws/ "https://codecatalyst.aws/").

### My password doesn't meet minimum

requirements

For your security, your password must include 8-20 characters, both uppercase and
lowercase letters, and numbers.

## Problems signing in

### I forgot my password

Follow the steps in [I forgot my password](troubleshooting.md#id-forgot-password "troubleshooting.md#id-forgot-password").

### My password isn’t working

You must follow these requirements whenever you set or change your
password:

- Passwords are case-sensitive.
- Passwords must be between 8 and 64 characters in length with both
  uppercase and lowercase letters, numbers, and at least one non-alphanumeric
  character.
- You can't reuse the last three passwords
  .

### I can't enable MFA

To enable MFA, add one or more MFA devices to your profile by following the steps
in [Configure your AWS Builder ID to sign in with multi-factor authentication (MFA)](mfa.md "mfa.md").

### I can't add an MFA device

If you find that you can't add another MFA device, it may have reached the limit
of MFA devices that you can register. You may need to remove an existing MFA device
before adding a new one.

### I can't remove an MFA device

If you intend to disable MFA, then proceed with removing your MFA device by
following the steps in [Deleting an MFA device](mfa.md#id-delete-mfa "mfa.md#id-delete-mfa"). However, if you want to keep MFA enabled, you should add another MFA device
before attempting to delete an existing MFA device. For more information about
adding another MFA device, see [How to register a device for use with multi-factor authentication](mfa.md#id-how-to-register "mfa.md#id-how-to-register").

## Problems signing out

### I can't find where to sign out

In the top right corner of the page, choose **Sign out**.

### Sign out doesn't sign me out

completely

The system is designed to sign out immediately, but full sign out may take up to
an hour.

## I get a role does not exist

error for a failed workflow

**Issue:** After creating a project from the web
application or serverless blueprint, the workflow fails with the following error:

**`CLIENT_ERROR: Role does not exist`**

**Possible solution:** After you configure an IAM role
with the permissions to run your workflow, and you have added the IAM role to your
workflow YAML, the workflow still fails because the IAM role might need to be added to
your account connection. Add the IAM role to the account connection for your
space as detailed in [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

## I get a role error for a

failed workflow

**Issue:** After creating a project from the web
application or serverless blueprint, the workflow fails with the following error:

**`CLIENT_ERROR: Role not set up properly or does not exist`**

**Possible solution:** The space where the project
was created might need to set up an AWS account connection or might need
to complete an account connection request. If your space already has an active
AWS account connection, create and add an IAM role with permissions
to run workflow actions. Add the IAM role to your account connection as detailed in
[Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

**Possible solution:** If the project was created without
specifying a connection, then the account connection needs to be associated with the
deployment environment. If your space already has an active AWS account connection and IAM role added, you must add the account
connection with the IAM role to your deployment environment as detailed in [Adding the account connection and
IAM roles to your deploy environment](ipa-connect-account-addroles-env.md "ipa-connect-account-addroles-env.md").

## I need to update the IAM role in

a project workflow

If the AWS account connection is set up completely, and the IAM role
is created and added to the account connection, you can update the IAM role in your
project workflow.

1. Choose the **CI/CD** option and choose your workflow. Choose
   the YAML button.
2. Choose **Edit**.
3. In the `ActionRoleArn:` field, replace the IAM role ARN with the
   updated IAM role ARN. Choose **Validate**.
4. Choose **Commit**.

The workflow starts automatically if on the mainline branch. Otherwise, to
rerun the workflow, choose **Run**.

## I have a review request for

my GitHub account after creating a personal connection

After you create a personal connection to GitHub, the CodeCatalyst app is installed for your
GitHub account as a GitHub app. If there are certain resources in CodeCatalyst that require
updated read or write permissions, you might need to access your GitHub account to
update the permissions on the installed app.

1. Sign in to GitHub and navigate to your account settings for installed apps.
   Choose your profile icon, choose **Settings**, and then choose
   **Applications**.
2. On the **Installed GitHub Apps** tab, in the list of
   installed applications, view the app installed for CodeCatalyst. A **Review request** link will display if there are
   permissions to review.
3. Choose the link, and then confirm your credentials when prompted. Enter your
   credentials and choose **Verify**.
4. Accept the new permissions, indicate the repositories where you want to apply
   the permissions, and then choose **Save**.

## How do I fill out a support form?

You can go to [Amazon CodeCatalyst](https://codecatalyst.aws/ "https://codecatalyst.aws/") or fill out a
[Support
Feedback form](https://support.aws.amazon.com/#/contacts/aws-account-support/ "https://support.aws.amazon.com/#/contacts/aws-account-support/"). In the **Request information** section,
under **How can we help you**, include that you are an Amazon CodeCatalyst
customer. Provide as much detail as possible so that we can most efficiently address
your issue.
