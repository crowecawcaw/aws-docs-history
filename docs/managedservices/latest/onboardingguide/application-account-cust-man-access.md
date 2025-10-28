# Accessing your Customer Managed account

After you provision a Customer Managed account (CMA) in multi-account landing zone, (MALZ) an Admin role, `CustomerDefaultAdminRole`,
is in the account for you to assume, through SAML federation, to configure the account.

To access the CMA:

1. Log into the IAM console for the management account with the **CustomerDefaultAssumeRole**
   role.
2. In the IAM console, on the navigation bar, choose your username.
3. Choose **Switch Role**. If this is the first time choosing
   this option, a page appears with more information. After reading it, choose **Switch Role**.
   If you clear your browser cookies, this page can appear again.
4. On the **Switch Role** page, type the Customer Managed account ID
   and the name of the role to assume: **CustomerDefaultAdminRole**.
   Now that you have access, you can create new IAM Roles to continue to access your environment. If you would like
   to leverage SAML Federation for your CMA Account, see
   [Enabling SAML 2.0 federated users to access the AWS Management Console](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md").
