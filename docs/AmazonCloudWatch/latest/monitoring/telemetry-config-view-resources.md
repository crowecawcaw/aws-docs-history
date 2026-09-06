

# Discovering resource telemetry
<a name="telemetry-config-view-resources"></a>

The telemetry configuration experience displays AWS resources in two places: as an overview on the **Ingestion – Data sources** and in detail on the **Discovered resources** page.

**Topics**
+ [Viewing data sources](#telemetry-config-view-data-sources)
+ [Viewing discovered resources](#telemetry-config-view-discovered)
+ [Filtering and preferences](#telemetry-config-filter-resource-view)

## Viewing data sources
<a name="telemetry-config-view-data-sources"></a>

The **Ingestion – Data sources** shows the AWS resources that you can send to CloudWatch. For specific resource types, it shows the percentage of resources with telemetry configured and the total number of resources detected. You can filter the display of resources in the **Data source** tab by account ID or by the tags applied to your resources.

**To view resources on the **Ingestion** page**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Ingestion**.

1. The **Ingestion** page shows the total number of each resource that was discovered by CloudWatch, the number of resources providing telemetry, and the percentage of discovered resources that are providing telemetry.

1. To see recent changes to resources, choose **Refresh**.

## Viewing discovered resources
<a name="telemetry-config-view-discovered"></a>

The **Discovered resources** page shows details about each AWS resource that has been discovered by telemetry configuration, including the resource ID, the type of telemetry each resource is providing, and the time when information about the resource was last refreshed.

For each AWS resource tracked by CloudWatch, the **Discovered resources** page shows the status of its telemetry by providing the following information:
+ For telemetry types that CloudWatch detects that the resource is sending to CloudWatch, the **Discovered resources** page shows **On**.
+ For telemetry types that CloudWatch detects the resource is not providing, the **Discovered resources** page shows **Off**.
+ For telemetry types that are not supported for a resource, the **Discovered resources** page shows **NS**, that is, not supported.

**To view resources on the **Discovered resources** page**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Ingestion**.

1. Do one of the following to view all resource types discovered by telemetry configuration or to view one resource type:

   1. To view all resources that have been discovered by CloudWatch, click **View data sources**. The **Discovered resources** page appears and shows all resources discovered.

   1. To view one resource type, click the name of the AWS resource type in the **Ingestion > Data sources**. The **Discovered resources** page appears. The **Discovered resources** page shows that a filter has been applied for that data source and now displays all discovered resources for that resource type.

1. On the **Discovered resources** page, to view information about the resource or to change its telemetry settings, click the resource ID. The console page for the AWS resource will open, navigate to the configuration setting and turn on or off the configuration.
**Note**  
You can only view a resource on its console page if the resource belongs to your account. To determine if the resource belongs to your account, check the **AWS account** column. If the **AWS account** column does not appear, change your **Discovered resources** page preferences. For more information, see [Changing preferences for the Discovered resources page](#telemetry-config-resource-view-prefs).

### Viewing resources across Regions
<a name="telemetry-config-view-multi-region"></a>

When multi-Region support is active, the **Discovered resources** page includes a **Region** column. You can filter resources by Region to focus on specific Regions.

CloudWatch uses a AWS Config aggregator to collect resource data across Regions. Because of this, there may be a short delay before resources from spoke Regions appear in the home Region view.

## Filtering and preferences
<a name="telemetry-config-filter-resource-view"></a>

You can use one or more filters on the **Ingestion > Data Sources** page and the **Discovered resources** page to change your view of the resources. Your filter settings persist across both pages.

**To filter resources on the **Data Sources** page**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Ingestion**, and then choose **Data sources**.

1. You can filter the discovered resources that are displayed on the page by specifying an account ID or tag value.

   1. Choose **Find resource**.

   1. Choose **Account ID** or **Tag value**, and then choose additional options for the filter. Statistics about telemetry coverage for each resource change based on your filter options.

1. To remove a filter, in the filter text box, choose **X**.

**To filter resources on the **Discovered Data sources** page**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Ingestion**.

1. To view all resource types discovered by telemetry configuration or to view one resource type, do one of the following:

   1. To view all resources discovered by CloudWatch, choose **View data sources**. The **Discovered resources** page appears and shows all resources discovered.

   1. To view one resource type, at the bottom of the page, choose a type of AWS resource. The **Discovered resources** page appears. The **Discovered resources** page filters all discovered resources for that resource type.

1. You can filter the resources displayed in the page based on any of the columns in the page. You can change the columns in the page by changing your preferences for the **Discovered resources** page. For more information, see the preferences procedure below.

   1. Choose **Find resource**. Filters for each column in the page appear. Choose one, then choose additional options to define the filter. Resources appear in the page that match the filter settings.

   1. To further filter the resources displayed in the page, choose **Find resources** again, choose another filter, and choose additional options. Resources appear in the page that match all of the filter settings.

1. To remove one of the filters, in the filter text box, choose **X**.

1. To remove all of the filters and see all resource types discovered, choose **Clear filters**.

### Changing preferences for the Discovered resources page
<a name="telemetry-config-resource-view-prefs"></a>

You can change your preferences for the **Discovered resources** page to control how many resources appear per page and which detailed metrics appear in the page. Only detailed metrics in view can be used to filter the resources displayed in the discovered resources page. For more information, see [Filtering and preferences](#telemetry-config-filter-resource-view).

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Ingestion** and **Data sources tab**.

1. Choose **Discovered resources**. The **Discovered resources** page appears.

1. Choose the gear icon.

1. In the **Preferences** dialog box, choose the number of resources per page and the visible content to show as columns.

1. Choose **Confirm**.