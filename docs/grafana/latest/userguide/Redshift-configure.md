

# Use AWS data source configuration to add Amazon Redshift as a data source
<a name="Redshift-configure"></a>

# To use AWS data source configuration to add Amazon Redshift as a data source


1.  Ensure that your user role is admin or editor.

1.  Select the workspace that you want to work on from the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/).

1. If you didn't choose to use service-managed permissions for this workspace when you created it, then change from using customer-managed permissions to use service-managed permissions to ensure that the proper IAM roles and policies are enabled for using the AWS data source configuration option in the Grafana workspace console. To do so, choose the edit icon by **IAM role** and then choose **Service managed**, **Save changes**. For more information, see [Amazon Managed Grafana permissions and policies for AWS data sources](AMG-manage-permissions.md). 

1. Choose the **Data sources** tab. Then select the check box for **Amazon Redshift**, and choose **Actions**, **Enable service-managed policy**.

1. Choose the **Data sources** tab again, and then choose **Configure in Grafana** in the **Amazon Redshift** row.

1. Sign into the Grafana workspace console using IAM Identity Center if necessary.

1. In the left navigation bar in the Grafana workspace console, choose the lower AWS icon (there are two) and then choose **Redshift**.

1. Select the default region that you want the Amazon Redshift data source to query from, and then select the accounts that you want, and then choose **Add data source**.

1.  Follow the steps to configure **Connection Details** in [**Connection details** settings](Redshift-config.md#Redshift-connection-details).