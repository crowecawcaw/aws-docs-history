

# Committing a data model to DynamoDB
<a name="workbench.Modeler.Commit"></a>

 When you are satisfied with your data model, you can commit the model to Amazon DynamoDB. 

**Note**  
This action creates server-side resources in AWS for the tables and global secondary indexes represented in the data model.
NoSQL Workbench creates tables and indexes with on-demand capacity by default.

**To commit the data model to DynamoDB**

1. Open NoSQL Workbench, and on the main screen, choose the name of the model that you want to commit.

1. In the top bar, choose **Commit**.

1. Choose an existing connection, or create a new connection by choosing **Add new connection**.
   + To add a new connection, specify the following information:
     + **Account Alias**
     + **AWS Region**
     + **Access key ID**
     + **Secret access key**

     For more information about how to obtain the access keys, see [Getting an AWS access key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.DynamoWebService.html#SettingUp.DynamoWebService.GetCredentials).
   + You can optionally specify the following:
     + [**Session token**](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)
     + [**IAM role ARN**](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns)

1. If you prefer to use [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html):

   1. Choose the **Local connection** tab.

   1. Choose **Add new connection**.

   1. Specify the **Connection name** and **Port**.
**Note**  
 To use DynamoDB local, turn it on by using the **DynamoDB local** toggle at the bottom left of the NoSQL Workbench screen. 

1. Choose **Commit**.