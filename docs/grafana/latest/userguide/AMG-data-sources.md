# Connect to data sources

Amazon Managed Grafana supports many different _data sources_. Data sources are
storage backends that you can query in Grafana to do things like building dashboards. Each
data source has a specific query editor that is customized for the features and capabilities
that the particular data source exposes.

The query language and capabilities of each data source are different. You can combine
data from multiple data sources onto a single dashboard.

Every AWS account that uses Amazon Managed Grafana has access to create or configure many data
sources. Some data sources require you to install the respective plugin for that data
source. If you upgrade your workspace to Amazon Managed Grafana Enterprise plugins, you may also need to
install the plugins for the Enterprise data sources. The following sections describe details
of many of the data sources available, but the Grafana community sometimes adds new data
sources that may be available in the [plugin catalog](grafana-plugins.md#plugin-catalog "grafana-plugins.md#plugin-catalog")
within your workspace.

###### Note

To help you discover AWS resources in your account and setup data sources to query
them, Amazon Managed Grafana provides the [Use the AWS Data Sources plugin to find
AWS data](aws-datasources-plugin.md "aws-datasources-plugin.md").

## Special data sources

Amazon Managed Grafana includes three special data sources:

- **Grafana** (called _TestDB_
  in earlier versions of Grafana – Use this built-in data source to
  generate random walk data, or list files. This is useful for testing
  visualizations and running experiments.
- **Mixed** – Use this to query multiple
  data sources in the same panel. When you use this data source, you can specify a
  data source for every new query that you add. The first query uses the data
  source that you specified before selecting **Mixed**.

You cannot change an existing query to use a mixed data source.

- **Dashboard** – Use this to use a result
  set from another panel in the same dashboard.

###### Important

Amazon Managed Grafana has a data source timeout limit, which might override any timeout limit
configured on data sources. The lower of the two limits supersedes the other. To learn
about the Amazon Managed Grafana data source timeout limit, see [Amazon Managed Grafana service
quotas](../../../general/latest/gr/grafana-service.md#grafana-quotas "../../../general/latest/gr/grafana-service.md#grafana-quotas") in the _AWS General Reference_.

###### Topics

- [How Amazon Managed Grafana works with AWS Organizations for AWS data
  source access](AMG-and-Organizations.md "AMG-and-Organizations.md")
- [Connect to built-in data sources](AMG-data-sources-builtin.md "AMG-data-sources-builtin.md")
- [Connect to Enterprise data sources](AMG-data-sources-enterprise.md "AMG-data-sources-enterprise.md")
