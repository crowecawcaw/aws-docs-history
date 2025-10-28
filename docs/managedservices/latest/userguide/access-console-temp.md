# Temporary AMS console access

If you haven't yet set up an identity provider (for instance, SAML) to authenticate to AMS, you can get temporary access to the AMS console. Contact your CSDM to have a
Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy change request (ct-3dpd8mdd9jn1r) submitted on your behalf with
these values:

- UserName: A name for the IAM user entity that you're creating
- AccessType: "Console access"
- UserPermissions: "Temporary AMS console access for `USERNAME` (the person that you want to have temporary access)"
- Email notifications: Your email address, so you can approve the request when AMS requests
  you to

###### Note

This RFC for temporary AMS Console access requires a security review and acceptance by both your internal security team and AMS Global Security.

After this request has been completed, and you're able to log in, you're required to approve the RFC that was created, to track the approval and allow the AMS team to
close out the work. To approve the RFC, find it in the RFC's list page (there will be a Pending Approval flag next to it), select it to open the RFC details page for that RFC,
and then choose **Approve**. Note that you won't be able to use AMS until the RFC is approved.

When the RFC successfully completes, AMS operations provides you with the new IAM user and a password. Then follow these steps:

1. Go to the AWS Management console and log in with provided credentials. You'll be asked to create a new password. You must also, upon login,
   set up multi-factor authentication (MFA); to learn more about doing that, see
   [Using Multi-Factor Authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md").
2. In the AWS Management console, change to the provided IAM role
   (`customer_`CustomerCode`_readonly_user_role`).
3. Open the AMS **Managed Services** Console.

###### Note

Temporary access defaults to sixty days; however, you can request a thirty-day extension by contacting your CSDM.
