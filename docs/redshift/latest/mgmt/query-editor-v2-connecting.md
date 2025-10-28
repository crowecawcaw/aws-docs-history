Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to an Amazon Redshift database

To connect to a database, choose the cluster or workgroup name in the tree-view panel.
If prompted, enter the connection parameters.

When you connect to a cluster or workgroup and its databases, you usually provide a
**Database** name. You also
provide parameters required for one of the following authentication methods:

**IAM Identity Center**

With this method, connect to your Amazon Redshift data warehouse with your single
sign-on credentials from your identity provider (IdP). Your cluster or
workgroup must be enabled for IAM Identity Center in the Amazon Redshift console. For
help setting up connections to IAM Identity Center, see [Connect Redshift with AWS IAM Identity Center
for a single sign-on experience](redshift-iam-access-control-idp-connect.md "redshift-iam-access-control-idp-connect.md").

**Federated user**

With this method, the principal tags of your IAM role or
user must provide the connection details. You configure these
tags in AWS Identity and Access Management or your identity provider (IdP). The query editor v2 relies on the
following tags.

- `RedshiftDbUser` – This tag defines the database
  user that is used by query editor v2. This tag is required.
- `RedshiftDbGroups` – This tag defines the
  database groups that are joined when connecting to query editor v2. This tag
  is optional and its value must be a colon-separated list such as
  `group1:group2:group3`. Empty values are ignored,
  that is, `group1::::group2` is interpreted as
  `group1:group2`.

These tags are forwarded to the
`redshift:GetClusterCredentials`

API to get credentials for your cluster. For more information, see [Setting up principal tags to
connect a cluster or workgroup from query editor v2](query-editor-v2-getting-started.md#query-editor-v2-principal-tags-iam "query-editor-v2-getting-started.md#query-editor-v2-principal-tags-iam").

**Temporary credentials using a database user name**

This option is only available when connecting to a cluster. With this
method, query editor v2, provide a **User name** for the database.
The query editor v2 generates a temporary password to connect to the database as your
database user name. A user using this method to connect must be allowed
IAM permission to `redshift:GetClusterCredentials`. To prevent
users from using this method, modify their IAM user or role to deny this
permission.

**Temporary credentials using your IAM identity**

This option is only available when connecting to a cluster. With this
method, query editor v2 maps a user name to your IAM identity and generates a
temporary password to connect to the database as your IAM identity. A user
using this method to connect must be allowed IAM permission to
`redshift:GetClusterCredentialsWithIAM`. To prevent users
from using this method, modify their IAM user or role to deny this
permission.

**Database user name and password**

With this method, also provide a **User name** and
**Password** for the database that you are connecting
to. The query editor v2 creates a secret on your behalf stored in AWS Secrets Manager. This
secret contains credentials to connect to your database.

**AWS Secrets Manager**

With this method, instead of a database name, you provide a
**Secret** stored in Secrets Manager that contains your database
and sign-in credentials.

For information about creating a secret, see [Creating a secret for
database connection credentials](redshift-secrets-manager-integration-create.md "redshift-secrets-manager-integration-create.md").

When you select a cluster or workgroup with query editor v2, depending on the context, you can
create, edit, and delete connections using the context (right-click) menu.
You can
view attributes such as the **Connection ARN** of the connection by
choosing **Connection details**. You can also edit tags attached to the
connection.
