# Updating IAM Identity Center

integration

After creating the connection, you can add third-party applications for the IAM Identity Center
integration to integrate with Lake Formation, and get access to Amazon S3 data on behalf of the users.
You can also remove existing applications from the IAM Identity Center integration. You can add or
remove applications using Lake Formation console, AWS CLI, and using [UpdateLakeFormationIdentityCenterConfiguration](../APIReference/API_UpdateLakeFormationIdentityCenterConfiguration.md "../APIReference/API_UpdateLakeFormationIdentityCenterConfiguration.md") operation.

###### Note

After creating IAM Identity Center integration, you can't update the instance `ARN`.

AWS Management Console

###### To update an existing IAM Identity Center connection with Lake Formation

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left navigation pane, select **IAM Identity Center integration**.
3. Select **Add** on the **IAM Identity Center integration** page.
4. Enter one or more valid AWS account IDs, organization IDs, and/or organizational
   unit IDs to allow external accounts to access the Data Catalog resources.
5. On the **Add applications** screen, enter the application IDs of the third-party applications that you want to integrate with Lake Formation.
6. Select **Add**.

AWS CLI
You can add or remove third-party applications for the IAM Identity Center integration
by running the following AWS CLI command. When you set external filtering
status to `ENABLED`, it enables the IAM Identity Center to provide identity
management for third-party applications to access data managed by Lake Formation. You
can also enable or disable the IAM Identity Center integration by setting the application
status.

```
aws lakeformation update-lake-formation-identity-center-configuration \
 --external-filtering '{"AuthorizedTargets": ["`<app arn1>`", "`<app arn2>`"], "Status": "ENABLED"}'\
 --share-recipients '[{"DataLakePrincipalIdentifier": "`<444455556666>`"}
                     {"DataLakePrincipalIdentifier": "`<777788889999>`"}]' \
 --application-status ENABLED
```
