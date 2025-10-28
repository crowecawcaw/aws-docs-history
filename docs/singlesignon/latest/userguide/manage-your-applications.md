# Configure access to applications

With AWS IAM Identity Center, you can control who can have single sign-on access to your applications.
Users get seamless access to these applications after they use their directory credentials
to sign in.

IAM Identity Center securely communicates with these applications through a trusted relationship between
IAM Identity Center and the application's service provider. This trust can be created in different ways,
depending on the application type.

IAM Identity Center supports two application types: [AWS managed
applications](awsapps.md "awsapps.md") and [customer managed
applications](customermanagedapps.md "customermanagedapps.md"). AWS managed applications are configured directly from within the
relevant application consoles or through the application APIs. Customer managed applications
must be added to the IAM Identity Center console and configured with the appropriate metadata for both
IAM Identity Center and the service provider.

After you configure applications to work with IAM Identity Center, you can manage which users or groups
access the applications. By default, no users are assigned to applications.

You can also grant your employees access to the AWS Management Console for a specific AWS account in
your organization. For more information, see [Configure access to AWS accounts](manage-your-accounts.md "manage-your-accounts.md").

###### Topics

- [AWS managed applications](awsapps.md "awsapps.md")
- [Customer managed applications](customermanagedapps.md "customermanagedapps.md")
- [Trusted identity propagation
  overview](trustedidentitypropagation-overview.md "trustedidentitypropagation-overview.md")
- [Setting up your own OAuth 2.0
  application](trustedidentitypropagation-using-customermanagedapps-setup.md "trustedidentitypropagation-using-customermanagedapps-setup.md")
- [Rotate IAM Identity Center certificates](managecerts.md "managecerts.md")
- [Understand application properties in the IAM Identity Center
  console](appproperties.md "appproperties.md")
- [Assign user access to applications in the IAM Identity Center
  console](assignuserstoapp.md "assignuserstoapp.md")
- [Remove user access to SAML 2.0
  applications](removeaccessfromapp.md "removeaccessfromapp.md")
- [Map attributes in your application to IAM Identity Center
  attributes](mapawsssoattributestoapp.md "mapawsssoattributestoapp.md")
