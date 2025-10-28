# Updating role permissions in Security Lake

If you don't have the required role permissions or resources—new AWS Lambda
function and Amazon Simple Queue Service (Amazon SQS) queue—to ingest data from a new version of the
data source, you must update your `AmazonSecurityLakeMetaStoreManagerV2` role
permissions and create a new set of resources to process data from your sources.

Choose your preferred method, and follow the instructions to update your role
permissions and create new resources to process data from a new version of an AWS log
source in a specified Region. This is a one-time action, as the permissions and
resources are automatically applied to future data source releases.

Console

###### To update role permissions (console)

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").

Sign in with the credentials of the delegated Security Lake
administrator. 2. In the navigation pane, under **Settings**,
choose **General**. 3. Choose **Update role permissions**. 4. In the **Service access** section, do one of the
following:

    * **Create and use a new service
     role**— You can use the
     **AmazonSecurityLakeMetaStoreManagerV2**
     role created by Security Lake.
    * **Use an existing service role**—
     You can choose an existing service role from the
     **Service role name** list.

5. Choose **Apply**.

API
**To update role permissions (API)**

To update permissions programmatically, use the [UpdateDataLake](../APIReference/API_UpdateDataLake.md "../APIReference/API_UpdateDataLake.md") operation of the Security Lake API. To
update permissions using the AWS CLI, run the [update-data-lake](../../../cli/latest/reference/securitylake/update-data-lake.md "../../../cli/latest/reference/securitylake/update-data-lake.md") command.

To update your role permissions, you must attach the [AmazonSecurityLakeMetastoreManager](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakeMetastoreManager "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakeMetastoreManager") policy to
the role.

## Deleting the

AmazonSecurityLakeMetaStoreManager role

###### Important

After you update your role permissions to
`AmazonSecurityLakeMetaStoreManagerV2`, confirm that the data
lake works correctly before you remove the old
`AmazonSecurityLakeMetaStoreManager` role. It is recommended to
wait at-least 4 hours before removing the role.

If you decide to remove the role, you must first delete the
`AmazonSecurityLakeMetaStoreManager` role from AWS Lake Formation.

Follow these steps to remove the `AmazonSecurityLakeMetaStoreManager`
role from the Lake Formation console.

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the Lake Formation console, from the navigation pane, choose
   **Administrative roles and tasks**.
3. Remove `AmazonSecurityLakeMetaStoreManager` from each
   Region.
