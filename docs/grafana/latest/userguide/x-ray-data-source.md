# Connect to an AWS X-Ray data source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

Add AWS X-Ray as a data source, and then build dashboards or use Explore with
X-Ray to look at traces, analytics, or insights.

With Amazon Managed Grafana, you can add X-Ray as a data source by using the AWS data
source configuration option in the Grafana workspace console. This feature
simplifies adding X-Ray as a data source by discovering your existing X-Ray
accounts and manages the configuration of the authentication credentials that are
required to access X-Ray. You can use this method to set up authentication and add
X-Ray as a data source, or you can manually set up the data source and the
necessary authentication credentials using the same method that you would on a
self-managed Grafana server.

###### Topics

- [Use AWS data source configuration to
  add X-Ray as a data source](xray-adding-AWS-config.md "xray-adding-AWS-config.md")
- [Manually adding the X-Ray data
  source](xray-add-the-data-source.md "xray-add-the-data-source.md")
- [X-Ray settings](#xray-settings "#xray-settings")
- [Using the X-Ray data source](xray-using.md "xray-using.md")

## X-Ray settings

| Name                     | Description                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                     | The data source name. This is how you see the data source in panels and queries.                                        |
| Default                  | Default data source means that it will be pre-selected for new panels.                                                  |
| Default Region           | Used in query editor to set region (can be changed on per query basis).                                                 |
| Auth Provider            | Specify the provider to get credentials.                                                                                |
| Credentials profile name | Specify the name of the profile to use (if you use `~/.aws/credentials` file), keep blank for default.                  |
| Assume Role Arn          | Specify the ARN of the role to assume.                                                                                  |
| External ID              | If you are assuming a role in another account, that has been created with an external ID, specify the external ID here. | ### Authentication This section covers the different types of authentication that you can use for X-Ray data source. #### IAM roles Currently, all access to X-Ray is done server side by the Grafana workspace backend using the official AWS SDK. If your Grafana server is running on AWS, you can use IAM roles and authentication will be handled automatically. For more information, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md"). ### IAM policies Grafana needs permissions granted via IAM to be able to read X-Ray data and EC2 tags/instances/regions. You can attach these permissions to IAM roles and use the built-in Grafana support for assuming roles. The following code example shows a minimal policy. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "xray:BatchGetTraces", "xray:GetTraceSummaries", "xray:GetTraceGraph", "xray:GetGroups", "xray:GetTimeSeriesServiceStatistics", "xray:GetInsightSummaries", "xray:GetInsight", "ec2:DescribeRegions" ], "Resource": "*" } ] }` `` #### Example AWS credentials You can't use the credentials file method in Amazon Managed Grafana. |
