Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting Amazon CodeCatalyst

The following information can help you troubleshoot common issues in CodeCatalyst. You can also
use the Amazon CodeCatalyst health report to determine if there are service issues that might be
impacting your experience.

###### Topics

- [Troubleshooting general access issues](#troubleshooting-general "#troubleshooting-general")
- [Troubleshooting support issues](#troubleshoot-support "#troubleshoot-support")
- [Some or all of Amazon CodeCatalyst isn't available](#service-unavailable "#service-unavailable")
- [I can't create a project in CodeCatalyst](#troubleshoot-create-project "#troubleshoot-create-project")
- [I can’t access my BID space as a
  new user or can’t be added as a new SSO user due to truncated user name](#troubleshoot-username-truncated "#troubleshoot-username-truncated")
- [Adding an SSO user to my federated space as a
  new user has created a duplicate user](#troubleshoot-username-duplicated-SSO "#troubleshoot-username-duplicated-SSO")
- [I want to submit feedback in
  CodeCatalyst](#troubleshoot-create-feedback "#troubleshoot-create-feedback")
- [Troubleshooting problems with source repositories](troubleshooting-source.md "troubleshooting-source.md")
- [Troubleshooting projects and blueprints](projects-troubleshooting.md "projects-troubleshooting.md")
- [Troubleshooting problems with Dev Environments](devenvironments-troubleshooting.md "devenvironments-troubleshooting.md")
- [Troubleshooting problems with workflows](troubleshooting-workflows.md "troubleshooting-workflows.md")
- [Troubleshooting problems with issues](troubleshooting-issues.md "troubleshooting-issues.md")
- [Troubleshooting problems with search in
  CodeCatalyst](troubleshooting-search.md "troubleshooting-search.md")
- [Troubleshooting problems with extensions](troubleshooting-extensions.md "troubleshooting-extensions.md")
- [Troubleshooting problems with accounts
  associated with your space](troubleshooting-connections.md "troubleshooting-connections.md")
- [Troubleshooting problems between Amazon CodeCatalyst and the AWS SDKs or the AWS CLI](troubleshooting-cli-sdk.md "troubleshooting-cli-sdk.md")

## Troubleshooting general access issues

### I forgot my password

**Problem:** I forgot the password I use for my
AWS Builder ID and Amazon CodeCatalyst.

**Possible fixes:** The easiest way to fix this
problem is to reset your password.

1. Open [Amazon CodeCatalyst](https://codecatalyst.aws/ "https://codecatalyst.aws/") and enter your
   **Email address**. Then, choose
   **Continue**.
2. Choose **Forgot password?**
3. We'll send you an email with a link for you to change your password. If
   you don't see the email in your inbox, check your spam folder.

### Some or all of Amazon CodeCatalyst isn't

available

**Problem:** I navigated to or followed a link to the
CodeCatalyst console, but I see an error.

**Possible fixes:** The most common reasons for this
problem are that you either followed a link to a project or a space you haven't
been invited to, or there is a general availability issue with the service. Check
the [Health report](health-dashboard.md "health-dashboard.md") to see if there are any
known issues with the service. If not, contact the person who invited you to the
project or space and ask for another invitation. If you haven't been invited to
any projects or spaces, you can sign up and [create your own space and
projects](sign-up-create-resources.md "sign-up-create-resources.md").

### I can't create a project in

CodeCatalyst

**Problem:** I want to create a project, but the
**Create project** button shows as unavailable, or I receive an
error message.

**Possible fixes:**The most common reasons for this
problem are that you are signed in to the console with an AWS Builder ID that doesn't
have the **Space administrator** role. You must have this role to
create projects in a space.

If you do have this role and the button does not appear as available, there might
be a transitory issue with the service. Refresh your browser and try again.

## Troubleshooting support issues

### I get an error when I access

Support for Amazon CodeCatalyst

**Problem:** When I choose the Support for Amazon CodeCatalyst option,
I receive the following error message:

**`Unable to assume role`**

`To access support cases, you must add the role AWSRoleForCodeCatalystSupport
 to the AWS account that is the billing account for the
 space.`

**Possible fixes:** Add the required role to the
AWS account that is the billing account for the space. The account designated as
the billing account for the space uses the `AWSRoleForCodeCatalystSupport` role and
`AmazonCodeCatalystSupportAccess` managed policy. For more information, see [Creating the AWSRoleForCodeCatalystSupport role for your
account and space](ipa-iam-roles.md#ipa-iam-roles-support-create "ipa-iam-roles.md#ipa-iam-roles-support-create").

###### Note

An AWS Builder ID can only get support for the alias they are authenticated with
and only for resources based on permissions in CodeCatalyst.
Account and
Billing support is available for all users in the space.
However, builders can only get support for resources and information they have
permissions for in CodeCatalyst.

### I cannot create technical

support cases for my space

**Problem:** I cannot create technical support cases
for my space.

**Fixes:** A Business Support or Enterprise Support
plan needs to be added to the space billing account in order for users in the
space to create technical support cases. Ask your space administrator to add an
Support plan to your space billing account or visit https://repost.aws/ to ask the AWS
community.

### My account for support

cases is no longer connected to my space in CodeCatalyst

**Problem:** My account for support cases is no
longer connected to my space in CodeCatalyst.

**Fixes:** If a user with the
**Space administrator** role switches the space billing
account, this will disconnect the Support plan and all associated cases from the
space. The Support cases associated with the old space billing account will
no longer be visible in Support for Amazon CodeCatalyst. The root user for that billing account can view
and resolve old cases from the AWS Management Console and can set up IAM permissions for Support
for other users to view and resolve old cases. You will not be able to continue to
get technical support for CodeCatalyst from the old space billing account through the
AWS Management Console, but you can receive technical support for other services until your Support
plan is canceled.

For more information, see [Updating, resolving, and reopening your case](../../../awssupport/latest/user/monitoring-your-case.md "../../../awssupport/latest/user/monitoring-your-case.md") in the _Support User Guide_.

### I can't open a support case

for another AWS service inSupport for Amazon CodeCatalyst

**Problem:** I can’t open a support case for another
AWS service in Support for CodeCatalyst.

**Possible fixes:** You can only open CodeCatalyst support
cases from Support for CodeCatalyst. If you need support for services or resources deployed
from CodeCatalyst to another AWS, Amazon, or other third-party service, you will need to
create a case through the AWS Management Console or the third-party service support channel. For
more information, see [Creating
support cases and case management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") in the _Support
User Guide_.

## Some or all of Amazon CodeCatalyst isn't available

**Problem:** I navigated to or followed a link to the
CodeCatalyst console, but I see an error.

**Possible fixes:** The most common reasons for this
problem are that you either followed a link to a project or a space you haven't
been invited to, or there is a general availability issue with the service. Check the
[Health report](health-dashboard.md "health-dashboard.md") to see if there are any known
issues with the service. If not, contact the person who invited you to the project or
space and ask for another invitation. If you haven't been invited to any projects
or spaces, you can sign up and [create your
own space and projects](sign-up-create-resources.md "sign-up-create-resources.md").

## I can't create a project in CodeCatalyst

**Problem:** I want to create a project, but the
**Create project** button shows as unavailable, or I receive an
error message.

**Possible fixes:** The most common reasons for this
problem are that you are signed in to the console with an AWS Builder ID that doesn't have
the **Space administrator** role. You must have this role to create
projects in a space.

If you do have this role and the button does not appear as available, there might be a
transitory issue with the service. Refresh your browser and try again.

## I can’t access my BID space as a

new user or can’t be added as a new SSO user due to truncated user name

**Problem:** CodeCatalyst truncates user names after 100
characters, which can cause some user names to appear identical. As a new user accessing
a CodeCatalyst space, I experience this problem depending on the type of space, as
follows:

- I have an AWS Builder ID that I want to use to sign in to CodeCatalyst. When I attempt
  to sign in to the space, I get a message that my user name is not valid.
- I am a federated identity administrator for a CodeCatalyst space that supports
  identity federation. When adding a new user to SSO users and groups in IAM Identity Center, I
  get a message that the user is not valid.

**Possible fixes:** The first user to sign in to CodeCatalyst
or be added to the space as an SSO user with a given truncated username will
succeed. Any users that sign up with a AWS Builder ID or are added in IAM Identity Center after that will
not be able to sign in because the name will appear to be a duplicate. Depending on the
type of space, do one of the following:

- To be able to sign in to the AWS Builder ID space, sign up with a different
  user name.
- To be able to add the new user in IAM Identity Center, add the user with a different user
  name.

###### Note

Even though the user name appears to be truncated, CodeCatalyst maps to identity in a
way that is not affected by user names with truncated names. However, if a user name
is created that is the same as a truncated user name, that user name will not be
available if another user associated (with the same space or IAM Identity Center application)
has already joined CodeCatalyst with that truncated user name.

## Adding an SSO user to my federated space as a

new user has created a duplicate user

**Problem:** CodeCatalyst SSO users added to a CodeCatalyst
space and then removed might experience an issue where the user name attempts
reuse. This might result in an error similar to the following, where the user is not
allowed to be duplicated even though it was re-created.

**`Unable to assume role`**

`To access support cases, you must add the role AWSRoleForCodeCatalystSupport to
 the AWS account that is the billing account for the space.`

**Possible fixes:** If an existing IDC user is deleted
and then a new user is recreate with the same username, then the new user is not able to
log in due to the username conflicting with the old user. After a user name is added to
a space as an SSO user, the name cannot be used again. Any users that sign up with
a AWS Builder ID or are added in IAM Identity Center after that will not be able to sign in because the
name will appear to be a duplicate.

Depending on the type of space, do one of the following:

- To be able to sign in to the AWS Builder ID space, sign up with a different
  user name.
- To be able to add the new user in IAM Identity Center, add the user with a different user
  name.

## I want to submit feedback in

CodeCatalyst

**Problem:** I found a bug in CodeCatalyst and I want to submit
feedback.

**Possible fixes:** You can submit feedback directly in
CodeCatalyst.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **Give feedback**.
3. Choose the type of feedback from the drop-down menu and enter your
   feedback.
