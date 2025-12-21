# Use AWS data source configuration

to add Amazon Athena as a data source

## Prerequisites

- The [AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") is installed and configured in your
  environment.
- You have access to Athena from your account.

To use AWS data source configuration, first go to the Amazon Managed Grafana console to
enable service-managed IAM roles that grant the workspace the IAM policies
necessary to read the Athena resources in your account or in your entire
organizational units. Then you use the Amazon Managed Grafana workspace console to add Athena
as a data source.

# To use AWS data source configuration to add Athena as a data

source

1. Ensure that your user role is admin or editor.
2. Select the workspace that you want to work on from the Amazon Managed Grafana
   console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
3. If you didn't choose to use service-managed permissions for this
   workspace when you created it, then change from using
   customer-managed permissions to use service-managed permissions to
   ensure that the proper IAM roles and policies are enabled for using
   the AWS data source configuration option in the Grafana workspace
   console. To do so, choose the edit icon by **IAM
   role** and then choose **Service
   managed**, **Save changes**. For more
   information, see [Amazon Managed Grafana permissions and policies for AWS data
   sources](AMG-manage-permissions.md "AMG-manage-permissions.md").
4. Choose the **Data sources** tab. Then select the
   check box for **Amazon Athena**, and choose
   **Actions**, **Enable service-managed
   policy**.
5. Choose the **Data sources** tab again, and then
   choose **Configure in Grafana** in the
   **Amazon Athena** row.
6. Sign into the Grafana workspace console using IAM Identity Center if necessary.
   The user should have Athena access policy attached to the user/role
   in order to have access to Athena data source. See [AWS managed policy:
   AmazonGrafanaAthenaAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaAthenaAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaAthenaAccess") for more info.
7. In the left navigation bar in the Grafana workspace console,
   choose the lower AWS icon (there are two) and then choose
   **Athena** from **Data sources**
   menu.
8. Select the default Region that you want the Athena data source to
   query from, and then select the accounts that you want, and then
   choose **Add data source**.
9. Follow the steps to configure **Athena Details**
   in [Athena Details
   settings](#Athena-settings "#Athena-settings")

## **Athena Details**

settings

###### Configure **Athena Details** settings

1. In **Connection Details** menu, select the
   authentication provider (recommended: **Workspace IAM
   Role**).
2. Select your targeted Athena data source where you have your
   Athena account with. If you do not select any data source, there is
   a default data source in the drop-down.

To create a new Athena account, follow the instructions at [Getting started with Athena](../../../athena/latest/ug/getting-started.md "../../../athena/latest/ug/getting-started.md") 3. Select your targeted Athena database in the data source selected
above. 4. Select the Workgroup. **Primary** is by default. 5. If your workgroup doesn't have an output location configured
already, specify an S3 bucket and folder to use for query results.
For example,
`s3://grafana-athena-plugin-test-data/query-result-output/` 6. Select **Save & Test**.
