# Connecting to live datasets

To connect to your Amazon DynamoDB tables with NoSQL Workbench, you must first connect to
your AWS account.

###### To add a connection to your database

1.  In NoSQL Workbench, in the navigation pane on the left side, choose the
    **Operation builder** icon.
2.  Choose **Add connection**.
3.  Specify the following information:

        * **Connection name**
        * **AWS Region**
        * **Access key ID**
        * **Secret access key**

    For more information about how to obtain the access keys, see [Getting an AWS access key](SettingUp.md#SettingUp.DynamoWebService.GetCredentials "SettingUp.md#SettingUp.DynamoWebService.GetCredentials").

You can optionally, specify the following:

    * [**Session token**](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md")
    * [**IAM role ARN**](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns")

4. Choose **Connect**.

If you don't want to sign up for a free tier account, and prefer to use
[DynamoDB
local (downloadable version)](DynamoDBLocal.md "DynamoDBLocal.md"):

    1. Choose the **Local** tab on the connection
     screen.
    2. Specify the following information:




    	* **Connection name**
    	* **Port**
    3. Choose the **connect** button.###### Note

To connect to DynamoDB local, either manually launch DynamoDB local using your
terminal (see [deploying
DynamoDB local on your computer](DynamoDBLocal.md "DynamoDBLocal.md")) or launch DynamoDB local directly using
the DDB local toggle in the NoSQL Workbench navigation menu. Ensure the
connection port is the same as your DynamoDB local port. 5. On the created connection, choose **Open**.
After connecting to your DynamoDB database, the list of available tables appears in the
left pane. Choose one of the tables to return a sample of the data stored in the
table.

You can now run queries against the selected table.

To run queries on a table, see the next section on building operations see [Building complex operations](workbench.querybuilder.md "workbench.querybuilder.md").
