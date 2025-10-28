# Edit or delete a data source

connection

You can use the Athena console to update the description, host, port, database, and other
properties for an existing connection. You can also delete the data sources from Athena
console.

## Edit a data source connection

###### To edit a data source connection

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 3. In the navigation pane, choose **Data sources and catalogs**. 4. On the **Data sources and catalogs** page, choose the data source connection
that you want to edit. 5. For **AWS Glue connection details**, choose
**Edit**. 6. Choose **Next**. 7. On the **Edit <connection-name>** page, update the information
as required. Available properties depend on the connection type.

###### Note

When you update connection properties for secrets, spill location, or AWS KMS
key ID, make sure the Lambda execution role still has access to the updated
resources. For more information, see [Viewing and
updating permissions in the execution role](../../../lambda/latest/dg/permissions-executionrole-update.md "../../../lambda/latest/dg/permissions-executionrole-update.md") in the
AWS Lambda Developer Guide.

    * **Description** – Edit the description for your
     connection.
    * **Host** – Edit the host name for your
     database.
    * **Port** – Edit the port number for your
     database.
    * **Database** – Edit the name of your
     database.
    * **JDBC parameters** – Edit any additional JDBC
     parameters required for your connection.
    * **Secret** – Choose or create a secret from
     AWS Secrets Manager. Use AWS secrets to avoid hardcoding sensitive information in
     your JDBC connection string. For more information, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") For information about creating a secret in
     Secrets Manager, see [Create an
     AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the
     *AWS Secrets Manager User Guide*.


    To use AWS Secrets Manager with Athena federated queries, you must configure an Amazon VPC
     private endpoint for Secrets Manager. For more information, see [Create a Secrets Manager VPC private endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md#vpc-endpoint-create "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md#vpc-endpoint-create") in the *AWS Secrets Manager User Guide*.
    * **Spill location in Amazon S3** – Choose or create an
     Amazon S3 bucket location in your account to store data that exceeds Lambda
     function response size limits.


    ###### Note

    Spilled data is not reused in subsequent executions and can be safely
     deleted after 12 hours. Athena does not delete this data for you. To
     manage these objects, consider adding an object lifecycle policy that
     deletes old data from your Amazon S3 spill bucket. For more information, see
     [Managing
     your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the *Amazon S3 User Guide*.
    * **Encryption for query results in S3** – Choose
     one of the following:




    	+ (Default) **Use a randomly generated key**
    	 – Data that is spilled to Amazon S3 is encrypted using the AES-GCM
    	 authenticated encryption mode and a randomly generated key.
    	+ **Use an AWS KMS key** – Choose or create a
    	 stronger, AWS KMS generated encryption key. For more information, see
    	 [Creating
    	 keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.
    	+ **Turn off** – Do not encrypt spill
    	 data.
    * **Networking settings** – Some connections require
     a virtual private cloud (VPC). Choose or create a VPC that has the data
     store that you want to access, a subnet, and one or more security groups.
     For more information, see [Create a VPC for a data source connector or
     AWS Glue connection](athena-connectors-vpc-creation.md "athena-connectors-vpc-creation.md").


    ###### Note



    	+ After you update connection properties for resources such as
    	 secrets, spill location, or AWS KMS key ID, make sure that the
    	 Lambda execution role continues to have access to the updated
    	 resources.
    	+ After you update the network settings for your connection,
    	 make sure you update the Lambda function with the same settings
    	 to make your connection compatible with the data source.

For information about additional connection properties, see [AWS Glue
connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md") in the _AWS Glue User Guide_ or
[Available data source connectors](connectors-available.md "connectors-available.md") in
the _Amazon Athena User Guide_. 8. Choose **Save**.

The **AWS Glue connection details** section of the page for your data source
shows the updated information for your connector.

## Delete a data source

When you delete a data source, it only deletes the Athena data source and does not
delete resources like the Glue connections, IAM execution role, and Lambda
function.

###### To delete a data source

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Data sources and catalogs**.
3. On the **Data sources and catalogs** page, choose the data
   source that you want to delete.
4. Choose **Delete**.
5. On the **Delete data source** page, type _confirm_ to confirm deletion and the choose
   **Delete**. It may take some time before the data source
   deletion completes. You get a success alert once the data source is
   deleted.
