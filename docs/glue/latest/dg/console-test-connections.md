# Testing an AWS Glue connection

As a best practice, before you use an AWS Glue connection in an ETL
job, use the AWS Glue console to test the connection. AWS Glue uses the parameters in your
connection to confirm that it can access your data store and reports any errors. For
information about AWS Glue connections, see [Connecting to data](glue-connections.md "glue-connections.md").

###### To test an AWS Glue connection

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, under **Data Catalog**, choose
   **Connections**. You can also choose **Data connections**
   above **Data Catalog** in the navigation pane.
3. In **Connections**, select the check box next to the desired connection, and then choose
   **Actions**. In the drop-down menu, choose **Test connection**.
4. In the **Test connection** dialog box, select a role or choose
   **Create IAM role** to go to the AWS Identity and Access Management (IAM) console to
   create a new role. The role must have permissions on the data store.
5. Choose **Confirm**.

The test begins and can take several minutes to complete. If the test fails,
choose **Troubleshoot** to view the steps to resolve the issue. 6. Choose **Logs** to view the logs in CloudWatch. You must have the required IAM
permissions to view the logs. For more information, see
[AWS Managed (Predefined) Policies for CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.md#managed-policies-cwl "../../../AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.md#managed-policies-cwl")  
 in the _Amazon CloudWatch Logs User Guide_.
