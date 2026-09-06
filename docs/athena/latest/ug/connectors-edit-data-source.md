

# Edit or delete a data source connection
<a name="connectors-edit-data-source"></a>

You can use the Athena console to update the description, host, port, database, and other properties for an existing connection. You can also delete the data sources from Athena console.

## Edit a data source connection
<a name="connectors-edit-data-source-editsteps"></a>

**To edit a data source connection**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. If the console navigation pane is not visible, choose the expansion menu on the left.  
![Choose the expansion menu.](http://docs.aws.amazon.com/athena/latest/ug/images/nav-pane-expansion.png)

1. In the navigation pane, choose **Data sources and catalogs**.

1. On the **Data sources and catalogs** page, choose the data source connection that you want to edit.

1. For **AWS Glue connection details**, choose **Edit**.

1. Choose **Next**.

1. On the **Edit <connection-name>** page, update the information as required. Available properties depend on the connection type.
**Note**  
When you update connection properties for secrets, spill location, or AWS KMS key ID, make sure the Lambda execution role still has access to the updated resources. For more information, see [Viewing and updating permissions in the execution role](https://docs.aws.amazon.com/lambda/latest/dg/permissions-executionrole-update.html) in the AWS Lambda Developer Guide.
   + **Description** – Edit the description for your connection.
   + **Host** – Edit the host name for your database.
   + **Port** – Edit the port number for your database.
   + **Database** – Edit the name of your database.
   + **JDBC parameters** – Edit any additional JDBC parameters required for your connection. 
   + **Secret** – Choose or create a secret from AWS Secrets Manager. Use AWS secrets to avoid hardcoding sensitive information in your JDBC connection string. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) For information about creating a secret in Secrets Manager, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

     To use AWS Secrets Manager with Athena federated queries, you must configure an Amazon VPC private endpoint for Secrets Manager. For more information, see [Create a Secrets Manager VPC private endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html#vpc-endpoint-create) in the *AWS Secrets Manager User Guide*.
   + **Spill location in Amazon S3** – Choose or create an Amazon S3 bucket location in your account to store data that exceeds Lambda function response size limits.
**Note**  
Spilled data is not reused in subsequent executions and can be safely deleted after 12 hours. Athena does not delete this data for you. To manage these objects, consider adding an object lifecycle policy that deletes old data from your Amazon S3 spill bucket. For more information, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.
   + **Encryption for query results in S3** – Choose one of the following:
     + (Default) **Use a randomly generated key** – Data that is spilled to Amazon S3 is encrypted using the AES-GCM authenticated encryption mode and a randomly generated key.
     + **Use an AWS KMS key** – Choose or create a stronger, AWS KMS generated encryption key. For more information, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
     + **Turn off** – Do not encrypt spill data.
   + **Networking settings** – Some connections require a virtual private cloud (VPC). Choose or create a VPC that has the data store that you want to access, a subnet, and one or more security groups. For more information, see [Create a VPC for a data source connector or AWS Glue connection](athena-connectors-vpc-creation.md).
**Note**  
After you update connection properties for resources such as secrets, spill location, or AWS KMS key ID, make sure that the Lambda execution role continues to have access to the updated resources.
After you update the network settings for your connection, make sure you update the Lambda function with the same settings to make your connection compatible with the data source.

   For information about additional connection properties, see [AWS Glue connection properties](https://docs.aws.amazon.com/glue/latest/dg/connection-properties.html) in the *AWS Glue User Guide* or [Available data source connectors](connectors-available.md) in the *Amazon Athena User Guide*.

1. Choose **Save**.

The **AWS Glue connection details** section of the page for your data source shows the updated information for your connector.

## Delete a data source
<a name="connectors-edit-data-source-delete"></a>

When you delete a data source, it only deletes the Athena data source and does not delete resources like the Glue connections, IAM execution role, and Lambda function.

**To delete a data source**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. In the navigation pane, choose **Data sources and catalogs**.

1. On the **Data sources and catalogs** page, choose the data source that you want to delete.

1. Choose **Delete**.

1. On the **Delete data source** page, type *confirm* to confirm deletion and the choose **Delete**. It may take some time before the data source deletion completes. You get a success alert once the data source is deleted.