# Committing a data model to DynamoDB

When you are satisfied with your data model, you can commit the model to
Amazon DynamoDB.

###### Note

- This action creates server-side resources in AWS for the tables and global secondary indexes represented in the data model.
- NoSQL Workbench creates tables and indexes with on-demand capacity by default.

###### To commit the data model to DynamoDB

1. Open NoSQL Workbench, and on the main screen, choose the name of the model that you want to commit.
2. In the top bar, choose **Commit**.
3. Choose an existing connection, or create a new connection by choosing **Add new connection**.

   - To add a new connection, specify the following information:

     - **Account Alias**
     - **AWS Region**
     - **Access key ID**
     - **Secret access key**
       For more information about how to obtain the access keys, see [Getting an AWS access key](SettingUp.DynamoWebService.md#SettingUp.DynamoWebService.GetCredentials "SettingUp.DynamoWebService.md#SettingUp.DynamoWebService.GetCredentials").

   - You can optionally specify the following:

     - [**Session token**](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md")
     - [**IAM role ARN**](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns")

4. If you prefer to use [DynamoDB local](DynamoDBLocal.md "DynamoDBLocal.md"):

   1. Choose the **Local connection** tab.
   2. Choose **Add new connection**.
   3. Specify the **Connection name** and **Port**.

###### Note

To use DynamoDB local, turn it on by using the **DynamoDB local** toggle at the bottom left of the NoSQL Workbench screen. 5. Choose **Commit**.
