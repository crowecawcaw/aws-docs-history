Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with IAM credentials for

Amazon Redshift

When you sign in to the Amazon Redshift console for the first time and first try out
Amazon Redshift Serverless, we recommend that you sign
in as a user with an attached IAM role that has the policies required. After you get
started creating an Amazon Redshift Serverless instance, Amazon Redshift records the IAM role name
that you used to sign in. You can use the same credentials to sign in to
the Amazon Redshift console and the Amazon Redshift Serverless console.

While creating the Amazon Redshift Serverless instance, you can create a database. Use the
query editor v2 to connect to the database with the temporary credentials option.

To add a new admin user name and password that persist for the database, choose
**Customize admin user credentials** and enter a new admin user
name and admin user password.

To get started using Amazon Redshift Serverless and create a workgroup and namespace in the
console for the first time, use an IAM role with a permissions
policy attached. Make sure that this role has either the administrator
permission `arn:aws:iam::aws:policy/AdministratorAccess` or the full Amazon Redshift
permission `arn:aws:iam::aws:policy/AmazonRedshiftFullAccess` attached to the
IAM policy.

The following scenarios outline how your IAM credentials are used by
Amazon Redshift Serverless when you get started on the Amazon Redshift Serverless console:

- If you choose **Use default settings** –
  Amazon Redshift Serverless translates your current IAM identity to a database
  superuser. You can use the same IAM identity with the Amazon Redshift Serverless
  console to perform superuser actions in your database in
  Amazon Redshift Serverless.
- If you choose **Customize settings** without specifying the
  **Admin user name** and password Amazon Redshift Serverless, your
  current IAM credentials are used as your default admin user credentials.
- If you choose **Customize settings** and specify
  **Admin user name** and password Amazon Redshift Serverless –
  Amazon Redshift Serverless translates your current IAM identity to a database
  superuser. Amazon Redshift Serverless also creates another long-term login username and
  password pair also as a superuser. You can either use your current IAM
  identity or the created username and password pair to login in to your database
  as a superuser.
