# Step 3: Create an AWS DMS Source Endpoint

After you configured the AWS Database Migration Service (AWS DMS) replication instance and the source Amazon RDS for SQL Server instance, ensure connectivity between these two instances. To ensure that the replication instance can access the server and the port for the database, make changes to the relevant security groups and network access control lists. For more information about your network configuration, see [Setting up a network for a replication instance](../userguide/CHAP_ReplicationInstance.VPC.md "../userguide/CHAP_ReplicationInstance.VPC.md").

After you completed the network configurations, you can create a source endpoint.

To create a source endpoint, do the following:

1. Open the AWS DMS console at https://console.aws.amazon.com/dms/v2/.
2. Choose **Endpoints**.
3. Choose **Create endpoint**.
4. On the **Create endpoint** page, enter the following information.

| For This Parameter                 | Do This                                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Endpoint type**                  | Choose **Source endpoint**, turn on **Select RDS DB instance**, and choose `datalake-source-db` RDS instance. |
| **Endpoint identifier**            | Enter **datalake-source-db**.                                                                                 |
| **Source engine**                  | Choose **Microsoft SQL Server**.                                                                              |
| **Access to endpoint database**    | Choose **Provide access information manually**.                                                               |
| **Server name**                    | Enter the database server name on Amazon RDS.                                                                 |
| **Port**                           | Enter **1433**.                                                                                               |
| **Secure Socket Layer (SSL) mode** | Choose **none**.                                                                                              |
| **User name**                      | Enter **dms\_user**.                                                                                          |
| **Password**                       | Enter the password that you created for the `dms_user` user.                                                  |
| **Database name**                  | Enter **AdventureWorks**.                                                                                     |

5. Choose **Create endpoint**.

###### Note

To migrate a Microsoft SQL Server Always On database, you need to use different configurations. For more information, see [Migrating a SQL Server Always On Database to Amazon Web Services](chap-manageddatabases.sqlserveralwayson.md "chap-manageddatabases.sqlserveralwayson.md").
