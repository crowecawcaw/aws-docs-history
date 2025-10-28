# Use AWS data source configuration to

add Amazon Managed Service for Prometheus as a data source

To use AWS data source configuration, first you use the Amazon Managed Grafana console to
enable service-managed IAM roles that grant the workspace the IAM policies
necessary to read the Amazon Managed Service for Prometheus resources in your account or in your entire
organizational units. Then you use the Amazon Managed Grafana workspace console to add Amazon Managed Service for Prometheus
as a data source.

###### To use AWS data source configuration to add Amazon Managed Service for Prometheus as a data

source

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the upper left corner of the page, choose the menu icon and then
   choose **All workspaces**.
3. Choose the name of the workspace.
4. If you didn't choose to use service-managed permissions for this
   workspace when you created it, then change from using customer-managed
   permissions to use service-managed permissions to ensure that the proper
   IAM roles and policies are enabled for using the AWS data source
   configuration option in the Grafana workspace console. To do so, choose
   the edit icon by **IAM role** and then choose
   **Service managed**, **Save
   changes**. For more information, see [Amazon Managed Grafana permissions and policies for AWS data
   sources](AMG-manage-permissions.md "AMG-manage-permissions.md").
5. Choose the **Data sources** tab. Then select the
   check box for **Amazon Managed Service for Prometheus**, and choose
   **Actions**, **Enable service-managed
   policy**.
6. Choose the **Data sources** tab again, and then
   choose **Configure in Grafana** in the
   **Amazon Managed Service for Prometheus** row.
7. Sign into the Grafana workspace console using IAM Identity Center if
   necessary.
8. In the left navigation bar in the Grafana workspace console, choose
   the AWS icon and then choose **AWS services**,
   **Prometheus**.
9. Select the Region that you want Amazon Managed Grafana to search to discover Amazon Managed Service for Prometheus
   workspaces, and then select the accounts and Amazon Managed Service for Prometheus workspaces that you
   want to add, and then choose **Add data
   source**.
