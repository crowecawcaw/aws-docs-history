# Resetting your AWS access portal user password

The AWS access portal provides [IAM Identity Center](what-is.md "what-is.md") users with single sign-on
access to all their assigned AWS accounts and cloud applications through a web portal. The
AWS access portal is different from the [AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/learn-whats-new.md "../../../awsconsolehelpdocs/latest/gsg/learn-whats-new.md"), which is a
collection of service consoles for managing AWS resources.

Use this procedure to reset your IAM Identity Center user password for the AWS access portal. Learn more about
[User
types](../../../signin/latest/userguide/user-types-list.md "../../../signin/latest/userguide/user-types-list.md") in the _AWS Sign-In User Guide_.

###### Considerations

The reset your password functionality for your AWS access portal is only available for users
of Identity Center instances that are using Identity Center directory or [AWS Managed Microsoft AD](gs-ad.md "gs-ad.md") as their identity source. If your user is connected to an external
identity provider or [AD Connector](../../../directoryservice/latest/admin-guide/directory_ad_connector.md "../../../directoryservice/latest/admin-guide/directory_ad_connector.md"), user password resets must be done from the external identity
provider or connected Active Directory.

- If your identity source is an **IAM Identity Center directory**, see [Password requirements when managing identities
  in IAM Identity Center](password-requirements.md "password-requirements.md").
- If your identity source is an **AWS Managed Microsoft AD**, see [Password requirements when resetting a password in AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_password_policies.md#how_password_policies_applied "../../../directoryservice/latest/admin-guide/ms_ad_password_policies.md#how_password_policies_applied").

###### To reset your password to the AWS access portal

1. Open a web browser and go to the sign-in page for your AWS access portal.

If you do not have your AWS access portal URL, check your email. You should have been emailed
an invitation to join AWS IAM Identity Center that includes a specific sign-in URL to the AWS access portal.
Alternatively, your administrator might have directly provided you with a one-time
password and the AWS access portal URL. If you cannot locate this information, ask your
administrator to send it to you.

For more information about signing into the AWS access portal, see [Sign in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User
Guide_. 2. Enter your **Username**, and then choose
**Next**. 3. Under **Password**, choose **Forgot
password**.

Verify your **Username** and enter the characters for the provided
image to confirm that you are not a robot. Then choose **Next**. You might
need to disable ad blocker software if you cannot enter characters. 4. A message appears to confirm that a reset password email was sent. Choose **Continue**. 5. You'll receive an email from `no-reply@signin.aws` with the subject
**Password reset requested**. In your email, choose **Reset
password**. 6. On the **Reset password** page, verify your
**Username**, specify a new password for the AWS access portal, and then
choose **Set new password**. 7. You'll receive an email from `no-reply@signin.aws` with the subject line
**Password updated**.

###### Note

An administrator can reset your password by either sending an email to you with
instructions for resetting your password or generating a one-time password and sharing it
with you. If you are an administrator, see [Reset the IAM Identity Center user password for an end
user](reset-password-for-user.md "reset-password-for-user.md").
