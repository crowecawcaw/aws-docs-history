# Step 5: Create Your Aurora MySQL Target Endpoint

Next, you can provide information for the target Amazon Aurora MySQL database by specifying the target endpoint settings.

To specify a target database endpoint, do the following:

1. In the AWS DMS console, choose **Endpoints** on the navigation pane.
2. Choose **Create endpoint**. The **Create endpoint** appears, as shown following.
3. Specify your connection information for the target Aurora MySQL database. The following table describes the target settings.

| For This Parameter                 | Do This                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Endpoint type**                  | Choose **Target endpoint**.                                                                                                                                                                   |
| **Endpoint identifier**            | Enter an identifier for your Aurora MySQL endpoint. The identifier for your endpoint must be unique within an AWS Region.                                                                     |
| **Target engine**                  | Choose **Amazon Aurora MySQL**.                                                                                                                                                               |
| **Access to endpoint database**    | Choose **Provide access information manually**.                                                                                                                                               |
| **Server name**                    | Enter the writer endpoint for your Aurora MySQL instance. The writer endpoint is the primary instance.                                                                                        |
| **Port**                           | Enter the port assigned to the instance.                                                                                                                                                      |
| **Secure Socket Layer (SSL) mode** | Choose an SSL mode if you want to enable connection encryption for this endpoint. Depending on the mode you select, you might need to provide certificate and server certificate information. |
| **User name**                      | Enter the user name for the user you are using for the migration. We recommend that you create a user specific to your migration.                                                             |
| **Password**                       | Provide the password for the user name preceding.                                                                                                                                             |

4. Define additional specific settings for your endpoints using wizard or editor in **Endpoint settings**.
5. Choose the encryption key to use to encrypt replication storage and connection information in **KMS key**. If you choose **(Default) aws/dms**, the default AWS Key Management Service (AWS KMS) key associated with your user and region is used.
6. Add tags to organize your DMS resources in **Tags**. You can use tags to manage your IAM roles and policies, and track your DMS costs.
   Prior to saving your endpoint, you have an opportunity to test it in **Test endpoint connection (optional)**. To do so you’ll need to choose a VPC and replication instance from which to perform the test.
