# Resend the verification email with AWS Organizations

If you don't verify your email address within 24 hours, you can resend the
verification request. After you have verified your email address, you can invite other AWS accounts to your organization.
If you don't receive the verification email, check that your email address is correct
and, if necessary, modify it.

- To find out what email address is associated with your management account, see
  [Viewing details of an organization from the
  management account](orgs_view_org.md "orgs_view_org.md").
- To change the email address that is associated with your management account,
  see [Managing an
  AWS account](../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md "../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md") in the _AWS Billing User Guide_.

AWS Management Console

###### To resend the verification request

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page and then choose **Send
   verification request**. The option is only present if
   the management account is not verified.
3. Verify your email address within 24 hours.

After verifying your email address, you can invite other
AWS accounts to your organization. For more information, see [Managing account invitations with AWS Organizations](orgs_manage_accounts_invites.md "orgs_manage_accounts_invites.md").
