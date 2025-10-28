# Viewing AWS resource telemetry in

CloudWatch

Telemetry configuration displays AWS resources in two places: As an overview, on the
**Telemetry config** page and in detail, on the **Discovered
data sources** page.

- **Telemetry config** – This page shows the percentage of resources
  with telemetry that are configured for each resource type and the number of resources detected
  as providing metrics, as well as the total number of resources in your account or organization.
  You can filter the display of resources in the **Telemetry config** page by
  account ID or by the tags applied to your resources.
- **Discovered data sources** – This page shows details about each
  resource that has been discovered by telemetry configuration, including the resource ID, the
  type of telemetry each resource is providing, and the time when information about the resource
  was last refreshed by telemetry configuration. You can filter the display of resource on the
  **Discovered data sources** page by any of the information provided about the
  resource.

For each AWS resource tracked by telemetry configuration, the **Discovered
resources** page shows the status of its telemetry by providing the following
information:

    + For telemetry types that CloudWatch detects that the resource is providing, the
     **Discovered data sources** page shows **On**.
    + For telemetry types that CloudWatch detects the resource is not providing, the
     **Discovered data sources** page shows **Off**.
    + For telemetry types that are not supported for a resource, the **Discovered
     resources** page shows **NS**, that is, not supported.

###### To view resources on the **Telemetry config** page

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. The **Telemetry config** page shows the total number of each resource
   that was discovered by telemetry config, the number of resources providing telemetry, and the
   percentage of discovered resources that are providing telemetry.
4. To see recent changes to resources, choose **Refresh**.

###### To view resources on the **Discovered data sources** page

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Do one of the following to view all resource types discovered by telemetry configuration
   or to view one resource type:
   1. To view all resources that have been discovered by telemetry configuration, choose
      **View data sources**. The **Discovered data sources** page
      appears and shows all resources discovered by telemetry configuration.
   2. To view one resource type, at the bottom of the page, choose a type of AWS resource.
      The **Discovered data source** page appears. The **Discovered
      data sources** page shows that a filter has been applied for that data source and now diplays all discovered resources for that resource type.

4. On the **Discovered data sources** page, do one or more of the
   following:
   - To view information about the resource or to change its telemetry settings, choose a
     resource ID. The console page for the resource appears.

   ###### Note

   You can only view a resource on its console page if the resource belongs to your
   account. To determine if the resource belongs to your account, check the
   **AWS account** column. If the **AWS account** column
   does not appear, change your the **Discovered data sources** page preferences.
   For more information, see [Changing preferences for the Discovered
   data sources page](#telemetry-config-resource-view-prefs "#telemetry-config-resource-view-prefs").
   - To view other pages of resources, choose a page number, or navigate by using
     **<** or **>** to view next or previous
     pages.
   - To see the latest information about resources in the page, choose
     **Refresh**.

###### Topics

- [Filtering discovered resources](#telemetry-config-filter-resource-view "#telemetry-config-filter-resource-view")
- [Changing preferences for the Discovered
  data sources page](#telemetry-config-resource-view-prefs "#telemetry-config-resource-view-prefs")

## Filtering discovered resources

You can use one or more filters on the **Telemetry config** page or the
**Discovered data sources** page to change your view of the resources. Your
filter settings persist across both pages.

###### To filter resources on the **Telemetry config** page

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**, and then choose
   **Telemetry config**.
3. You can filter the discovered resources that are displayed on the page by specifying an
   account ID or tag value.
   1. Choose **Find resource**.
   2. Choose **Account ID** or **Tag value**, and then
      choose additional options for the filter. Statistics about telemetry coverage for each
      resource change based on your filter options.

4. To remove a filter, in the filter text box, choose **X**.

###### To filter resources on the **Discovered data sources** page

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. To view all resource types discovered by telemetry configuration or to view one resource
   type, do one of the following:
   1. To view all resources discovered by telemetry configuration, choose **View
      resources**. The **Discovered data sources** page appears and shows
      all resources discovered by telemetry configuration.
   2. To view one resource type, at the bottom of the page, choose a type of AWS resource.
      The **Discovered data sources** page appears. The **Discovered
      resources** page filters all discovered resources for that resource type.

4. You can filter the resources displayed in the page based on any of the columns in the
   page. You can change the columns in the page by changing your preferences for the
   **Discovered data sources** page. For more information, see [Changing preferences for the Discovered
   data sources page](#telemetry-config-resource-view-prefs "#telemetry-config-resource-view-prefs").
   1. Choose **Find resource**. Filters for each column in the page appear.
      Choose one, then choose additional options to define the filter. Resources appear in the
      page that match the filter settings.
   2. To further filter the resources displayed in the page, choose **Find
      resources** again, choose another filter, and choose additional options. Resources
      appear in the page that match all of the filter settings.

5. To remove one of the filters, in the filter text box, choose
   **X**.
6. To remove all of the filters and see all resource types discovered by telemetry
   configuration, choose **Clear filters**.

## Changing preferences for the Discovered

data sources page

You can change your preferences for the **Discovered data sources** page to
control how many resources appear per page and which detailed metrics appear in the page. Only
detailed metrics in view can be used to filter the resources displayed in the discovered
resources page. For more information, see [Filtering discovered resources](#telemetry-config-filter-resource-view "#telemetry-config-filter-resource-view").

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose **View data sources**. The **Discovered data sources**
   page appears.
4. Choose the gear icon.
5. In the **Preferences** dialog box, choose the number of resources per
   page and the visible content to show as columns.
6. Choose **Confirm**.
