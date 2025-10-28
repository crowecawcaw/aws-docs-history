# Connect to an AWS IoT SiteWise data

source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

With Amazon Managed Grafana, you can add AWS IoT SiteWise as a data source by using the AWS data
source configuration option in the Grafana workspace console. This feature
simplifies adding AWS IoT SiteWise as a data source by discovering your existing AWS IoT SiteWise
accounts and manages the configuration of the authentication credentials that are
required to access AWS IoT SiteWise. You can use this method to set up authentication and add
AWS IoT SiteWise as a data source, or you can manually set up the data source and the
necessary authentication credentials using the same method that you would on a
self-managed Grafana server.

###### Topics

- [Use AWS data source
  configuration to add AWS IoT SiteWise as a data source](IoTSiteWise-adding-AWS-config.md "IoTSiteWise-adding-AWS-config.md")
- [Manually adding the AWS IoT SiteWise
  data source](iotsitewise-add-the-data-source.md "iotsitewise-add-the-data-source.md")
- [AWS IoT SiteWise settings](#iotsitewise-settings "#iotsitewise-settings")
- [Using the AWS IoT SiteWise data source](IoTSiteWise-using.md "IoTSiteWise-using.md")

## AWS IoT SiteWise settings

| Name                     | Description                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| Name                     | The data source name. This is how you see the data source in panels and queries.                       |
| Auth Provider            | Specify the provider to get credentials.                                                               |
| Default Region           | Used in query editor to set the region (can be changed on per query basis).                            |
| Credentials profile name | Specify the name of the profile to use (if you use `~/.aws/credentials` file); keep blank for default. |
| Assume Role Arn          | Specify the ARN of the role to assume.                                                                 |
| Endpoint (optional)      | If you must specify an alternate service endpoint.                                                     |
