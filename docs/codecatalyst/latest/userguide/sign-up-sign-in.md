Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Accepting an invitation and creating an AWS Builder ID

You can sign up for Amazon CodeCatalyst as part of accepting an invitation to a project or a
space. As part of accepting the invitation, you'll be prompted to create an AWS Builder ID.
You'll use your AWS Builder ID to access resources in CodeCatalyst.

###### Tip

If you need additional help, see [Problems signing up](ipa-troubleshooting.md#id-troubleshooting-sign-up "ipa-troubleshooting.md#id-troubleshooting-sign-up").

Here is one possible flow for a user starting out with CodeCatalyst with an invitation to a project
or a space.

Saanvi Sarkar is a developer who has received an invitation to join a CodeCatalyst project
as a project administrator. Saanvi accepts the invitation, which opens the sign-in page for
CodeCatalyst. She chooses to sign up and provides an email address and password to create her
AWS Builder ID. Saanvi will be able to use her AWS Builder ID to sign in to CodeCatalyst and other
applications. Later, she can edit her profile to change her login email address or password.
When asked to choose an alias, Saanvi specifies `SaanviSarkar` as the CodeCatalyst alias
that will display in CodeCatalyst and that other project members will use to @mention Saanvi.
After she has signed up, Saanvi will also be able to use her sign-in credentials for other
applications that use AWS Builder ID credentials.

Upon completing sign up, Saanvi automatically joins the CodeCatalyst project and space
specified in the invitation. The invitation also provides predetermined permissions for her
roles in the project and space. In the project settings, Saanvi's alias shows in the
members list with her assigned project role. To work with source repositories in CodeCatalyst,
Saanvi takes a moment to create a personal access token (PAT). The PAT will be used in
CodeCatalyst for authentication when making source changes or actions that need an authentication
token.

When Saanvi works on a project, her alias will be listed in the work activity log for
the project. Issues and comments by Saanvi will show her alias, where other project members
are able to @mention her in replies. To @mention another project member, Saanvi looks up
their alias on their CodeCatalyst profile.

When she has a moment, Saanvi configures her AWS Builder ID to sign in to CodeCatalyst with
multi-factor authentication (MFA). With MFA configured, Saanvi can sign in to CodeCatalyst using
a combination of her CodeCatalyst password and a passcode or token from an approved third-party
authentication app.

## Accepting an invitation and creating an AWS Builder ID

When you're invited to a project or space in Amazon CodeCatalyst, you'll receive an email from notify@codecatalyst.aws asking you to accept
the invitation. If you already have a AWS Builder ID and are signed in to CodeCatalyst, choosing **Accept invitation**
will automatically open the project or space in a browser tab. If you're not signed in to the console but have a AWS Builder ID,
you'll be taken to the sign-in page. For more information, see [Signing in with an AWS Builder ID](id-how-to-sign-in.md "id-how-to-sign-in.md").

If you don't have a AWS Builder ID, choosing **Accept invitation** will take you to the sign-in page, where you should choose
the option to create your AWS Builder ID.

###### To accept an invitation and create a AWS Builder ID

1. In the invitation email, choose **Accept invitation**.
2. On the sign in page, choose **Not signed up? Create your AWS Builder ID**.

###### Tip

Your AWS Builder ID is an identity you create to sign in. It is not the same as an
AWS account. 3. On the **Create your AWS Builder ID** page, in **Email
address**, enter the email address you want to use for your AWS Builder ID.

In **Your name**, provide the first and last name you want displayed in
applications where you use your AWS Builder ID. Spaces are allowed. This will be your AWS Builder ID
profile name, such as **Mary Major**. You can change
the name later.

Choose **Next**.

A verification code will be sent to the email you specified. Enter this code in
**Verification code**, and then choose **Verify**. If you
don't receive your code after 5 minutes and cannot find it in your spam or junk folders, then
choose **Resend code**. 4. Once your code is verified, enter a password that meets the requirements in
**Password** and **Confirm password**. 5. Choose **Create AWS Builder ID**. 6. On the **Create your alias** page, enter an alias you want to use for
your unique user identifier in CodeCatalyst. Choose a shortened version of your name with no spaces,
such as **MaryMajor**. Other CodeCatalyst users will use this
to @mention you in comments and pull requests. Your CodeCatalyst profile will contain both your full
name from your AWS Builder ID and your CodeCatalyst alias. You cannot change your CodeCatalyst alias.

Your full name and your alias will display in different areas in CodeCatalyst. For example, your
profile name displays for your listed activity in the activity feed, but project members will
use your alias to @mention you.

Choose **Create alias**. You'll be taken to the project or space you
were invited to.
