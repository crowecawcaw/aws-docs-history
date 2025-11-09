# Connect to an Amazon Timestream data source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

With Amazon Managed Grafana, you can add Amazon Timestream as a data source by using the AWS data
source configuration option in the Grafana workspace console. This feature
simplifies adding Timestream as a data source by discovering your existing Timestream
accounts and manages the configuration of the authentication credentials that are
required to access Timestream. You can use this method to set up authentication and add
Timestream as a data source, or you can manually set up the data source and the
necessary authentication credentials using the same method that you would on a
self-managed Grafana server.

## Timestream settings

| Name                     | Description                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Name                     | The data source name. This is how you see the data source in<br>panels and queries.                          |
| Auth Provider            | Specify the provider to get credentials.                                                                     |
| Default Region           | Used in query editor to set region (can be changed on per<br>query basis).                                   |
| Credentials profile name | Specify the name of the profile to use (if you use<br>`~/.aws/credentials` file), keep blank for<br>default. |
| Assume Role Arn          | Specify the ARN of the role to assume.                                                                       |
| Endpoint (optional)      | If you must specify an alternate service endpoint.                                                           |

### Authentication

This section covers the different types of authentication that you can
use for the Amazon Timestream data source.

#### Example AWS

credentials

You can't use the credentials file method of authentication in
Amazon Managed Grafana.
