# Step 5: Create an AWS SCT Project

After you configure AWS SCT, create a new migration project.

1. In AWS SCT, choose **File**, then choose **New Project**.
2. For **Project name**, enter a descriptive name of your project, and then choose **OK**.
3. Choose **Add source** to add a source BigQuery data warehouse to your project, then choose **BigQuery**, and choose **Next**.
4. For **Connection name**, enter a name for your source data warehouse. AWS SCT displays this name in the tree in the left panel.
5. For **Key path**, choose **Browse** and then choose the BigQuery service account key file that you created in step 1.
6. Choose **Connect** to close the dialog box and to connect to your BigQuery data warehouse.
7. Choose **Add target** to add a target Amazon Redshift database to your project, then choose **Amazon Redshift**, and choose **Next**.
8. If you store your database credentials in AWS Secrets Manager, choose your secret and then choose **Populate**. For more information, see [Using Secrets Manager](../../../SchemaConversionTool/latest/userguide/CHAP_UserInterface.md#CHAP_UserInterface.SecretsManager "../../../SchemaConversionTool/latest/userguide/CHAP_UserInterface.md#CHAP_UserInterface.SecretsManager").

If you don’t use Secrets Manager, enter your database credentials manually.

    * For **Connection name**, enter a name for your target data warehouse. AWS SCT displays this name in the tree in the right panel.
    * For **Server name**, enter the server name of the Amazon Redshift cluster that you created in step 2. You can copy the server name as **JDBC URL** in the **General information** for your Amazon Redshift cluster. Remove `jdbc:redshift://` from the URL that you copied.
    * For **Server port**, enter 5439.
    * For **User name**, enter the name of the user that you created in step 2.
    * For **Password**, enter the password for the user that you created in step 2.

9. Turn off **Use AWS Glue** and choose **Connect**.
10. In the tree in the left panel, choose your BigQuery dataset. In the tree in the right panel, choose your target Amazon Redshift database. Choose **Create mapping**. You can add multiple mapping rules a single AWS SCT project. For more information about mapping rules, see [Creating mapping rules](../../../SchemaConversionTool/latest/userguide/CHAP_Mapping.md "../../../SchemaConversionTool/latest/userguide/CHAP_Mapping.md").
11. Choose **Main view**.
