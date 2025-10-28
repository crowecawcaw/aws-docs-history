# Deleting a Lake Formation connection with IAM Identity Center

If you would like to delete an existing IAM Identity Center integration, you can do it using Lake Formation
console, AWS CLI, or [DeleteLakeFormationIdentityCenterConfiguration](../APIReference/API_DeleteLakeFormationIdentityCenterConfiguration.md "../APIReference/API_DeleteLakeFormationIdentityCenterConfiguration.md") operation.

AWS Management Console

###### To delete an existing IAM Identity Center connection with Lake Formation

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left navigation pane, select **IAM Identity Center integration**.
3. Select **Delete** on the **IAM Identity Center integration** page.
4. On the **Confirm integration** screen, confirm the action, and select **Delete**.

AWS CLI
You can delete IAM Identity Center integration
by running the following AWS CLI command.

```
 aws lakeformation delete-lake-formation-identity-center-configuration \
     --catalog-id `<123456789012>`
```
