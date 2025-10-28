# Use the AWS Data Sources plugin to find

AWS data

AWS provides an application plugin to make it easier to discover and use AWS
resources as data sources in your Amazon Managed Grafana workspace. The _AWS Data
Sources_ plugin is installed by default in a new workspace.

The AWS Data Sources plugin requires permissions to access your resources
for discovery. For more information, see [Required permissions](#aws-ds-plugin-permissions "#aws-ds-plugin-permissions").

## Open the AWS Data Sources plugin

###### To open the AWS Data Sources plugin

1. Sign into your Amazon Managed Grafana workspace.
2. From the **menu** in the top left, choose
   **Apps**, then **AWS Data
   Sources**.

The AWS Data Sources plugin interface appears listing AWS services
that you can search for resources.

## Discover resources

###### To discover resources from your AWS account

1. Open the AWS Data Sources plugin.
2. From the list of AWS services, select the one that you want to find
   resources to use as a data source. For example, select
   **Amazon Managed Service for Prometheus**. This will take you to the
   **Data sources** tab, with the
   **Service** selected for you.
3. Choose the AWS Region where you want to find resources. For example,
   select `US East (N. Virginia)`.

###### Note

To find resources, the plugin must have the appropriate [permissions](#aws-ds-plugin-permissions "#aws-ds-plugin-permissions") to access that
service in that region. 4. Some services can have multiple resources in a region. If there are
multiple resources in the region, the AWS Data Sources plugin provides
a list to choose from.

From the list of resources (in this case, Amazon Managed Service for Prometheus), select the resource
that you want to use as a data source. For example, selecting a Amazon Managed Service for Prometheus
workspace will setup that resource as a data source The data source is ready
to use in your dashboards or monitoring with Amazon Managed Grafana. 5. The resources in that service and Region that you have provisioned appear
at the bottom of the page.

(Optional) You can choose **Go to settings** to view and
edit the settings for that data source.

###### Note

The AWS Data Sources plugin depends on the individual data source plugins
being installed in your workspace. For example, if you want to use the
AWS X-Ray functionality, you must have the X-Ray data source plugin
installed from the [plugin catalog](grafana-plugins.md#manage-plugins "grafana-plugins.md#manage-plugins").

## Versions and updating the plugin

The AWS Data Sources plugin is regularly updated. The version installed with a
new workspace is not typically the latest version. Newer versions can have more
functionality than the one installed in your workspace. For example, a newer
version might support additional AWS services as data sources.

To see the changes in each version of the AWS Data Sources plugin, you can
view the [Changelog](https://grafana.com/grafana/plugins/aws-datasource-provisioner-app/?tab=changelog "https://grafana.com/grafana/plugins/aws-datasource-provisioner-app/?tab=changelog").

To update to a newer version of the plugin, follow the standard instructions for
[Update a plugin](grafana-plugins.md#update-plugin "grafana-plugins.md#update-plugin").

###### Note

If you update to a newer version of the AWS Data Sources plugin, you
need to provide additional [permissions](#aws-ds-plugin-permissions "#aws-ds-plugin-permissions") for new data sources that are not managed by Amazon Managed Grafana.

## Required permissions

The AWS Data Sources plugin requires permission to access your AWS
resources. The easiest way to do that is to allow Amazon Managed Grafana to manage the
permissions for you. To learn how to set up service-managed permissions for data
sources, see [Manage permissions for data sources
and notification channels](AMG-datasource-and-notification.md "AMG-datasource-and-notification.md"). Amazon Managed Grafana can manage the
permissions for the AWS resources that are included in the AWS Data Sources
plugin by default.

If you update the AWS Data Sources plugin to a newer version than is included
by default in your workspace, it could add support for AWS resources whose
permissions are not managed by Amazon Managed Grafana automatically. In these cases, you must
add the permissions yourself. For example, AWS IoT TwinMaker was added to a recent
version of the plugin, (version 1.9.0), and permissions for these are not
managed by Amazon Managed Grafana.

To learn more about the permissions for any specific data source, see the
details for that data source provided in the [Connect to data sources](AMG-data-sources.md "AMG-data-sources.md") section. For example, the [Connect to an AWS IoT TwinMaker data source](AMG-iot-twinmaker.md "AMG-iot-twinmaker.md") section includes
details about giving Amazon Managed Grafana permissions to access AWS IoT TwinMaker.
