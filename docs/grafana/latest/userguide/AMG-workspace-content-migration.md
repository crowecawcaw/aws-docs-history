# Migrate content between Amazon Managed Grafana

workspaces

There are times that you want to migrate your content (including data sources,
dashboards, folder, and alert rules) from one workspace to another. For example, you are
migrating from an on-premise Grafana instance to an Amazon Managed Grafana workspace, and you want to
migrate your existing content to the new workspace.

Amazon Managed Grafana does not directly support migrating content between workspaces, however,
AWS does provide an open-source migration utility that can handle this scenario by
providing export and import functionality within a workspace or Grafana instance. This
utility is called the **Amazon Managed Grafana Migrator**.

For more information, see [Amazon Managed Grafana
Migrator](https://github.com/aws-observability/amazon-managed-grafana-migrator "https://github.com/aws-observability/amazon-managed-grafana-migrator") on GitHub.
