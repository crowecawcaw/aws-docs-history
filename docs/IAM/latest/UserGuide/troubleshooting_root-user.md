# Troubleshoot issues with the root user

Use the information here to help you troubleshoot issues related to the root user of an
AWS account.

###### Note

AWS accounts managed using AWS Organizations may have [centralized root access](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") enabled for
member accounts. These member accounts do not have root user credentials, can't sign in as
a root user, and are prevented from recovering the root user password. Contact your
administrator if you need to perform a task that requires root user credentials.

Your account might be a member of an organization in AWS Organizations. Your organizational
administrator may have a service control policy (SCP) to limit the permissions of
your account. SCPs impact all users, including the root user. For more information, see
[Service
control policies](../../../organizations/latest/userguide/orgs_manage_policies_type-auth.md "../../../organizations/latest/userguide/orgs_manage_policies_type-auth.md") in the _AWS Organizations User Guide_.

If you're a root user and you have lost or forgot the password for your
AWS account, you can reset your password. You must know the email address used to
create the AWS account, and you must have access to the email account. For more
information, see [Reset a lost or forgotten root user password](reset-root-password.md "reset-root-password.md").

When you create an AWS account, you provide an email address and password. These
are the credentials for the AWS account root user. If you aren't sure of the email address
associated with your AWS account, search for messages sent from
`@signin.aws` or `@verify.signin.aws` to any email address
for your organization that might have been used to open the AWS account.

If you know the email address but no longer have access to the email, try to
recover access to the email. Use one of the following options to regain access to
your email:

- If you own the domain for the email address, you can restore a deleted
  email address. Alternatively, you can set up a catch-all for your email
  account. A catch-all collects all messages sent to email addresses that no
  longer exist in the mail server and redirects them to another email
  address.
- If the email address on the account is part of your corporate email
  system, we recommend that you contact your IT system administrators. They
  might be able to help you regain access to the email.
  If you're still not able to sign in to your AWS account, you can find alternate
  support options at [Contact
  us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
