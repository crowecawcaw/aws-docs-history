# Security best practices

The topics in this section explain the best practices to follow to best maintain security in your
Amazon Managed Grafana deployment.

## Use short-lived API keys

To use Grafana APIs in an Amazon Managed Grafana workspace, you must first create an API key to use for authorization.
When you create the key, you specify the **Time to live** for the key, which defines
how long the key is valid, up to a maximum of 30 days. We strongly recommend that you set
the key's time to live for a shorter time, such as a few hours or less. This creates much
less risk than having API keys that are valid for a long time.

We also recommend that you treat API keys as passwords, in terms of securing them. For example,
do not store them in plain text.

## Migrating from self-managed Grafana

This section is relevant for you if you are migrating an existing self-managed Grafana or Grafana Enterprise
deployment to Amazon Managed Grafana. This applies to both on-premises Grafana and to a Grafana deployment on AWS, in your own account.

If you are running Grafana on-premises or in your own AWS account, you have likely defined users and
teams and potentially organization roles to manage access. In Amazon Managed Grafana, users and groups are
managed outside of Amazon Managed Grafana, using IAM Identity Center or directly from your identity provider (IdP) via SAML 2.0 integration.
With Amazon Managed Grafana, you can assign certain permissions
as necessary for carrying out a task— for example viewing dashboards. For more information about user management
in Amazon Managed Grafana, see [Manage workspaces, users, and policies in
Amazon Managed Grafana](AMG-manage-workspaces-users.md "AMG-manage-workspaces-users.md").

Additionally, when you run on-premises Grafana you’re using long-lived keys or secret credentials
to access data sources. We strongly recommend that when you migrate to Amazon Managed Grafana, you replace these
IAM users with IAM roles. For an example, see [Manually add CloudWatch as a data
source](adding--CloudWatch-manual.md "adding--CloudWatch-manual.md").
