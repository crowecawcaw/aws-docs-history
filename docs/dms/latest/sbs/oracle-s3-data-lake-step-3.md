# Step 3: Create an AWS DMS Source Endpoint

In this step, we configure a source endpoint. AWS DMS uses this endpoint to connect to the source database to read data as well as changes to the data via transaction logs. You can use Extra Connection Attributes for the source endpoint to configure how AWS DMS captures changes to the data.

After you configure the AWS Database Migration Service (AWS DMS) replication instance and the source RDS for Oracle instance, ensure connectivity between these two instances. To ensure that the replication instance can access the server and the port for the database, make changes to the relevant security groups and network access control lists. For more information about your network configuration, see [Setting up a network for a replication instance](../userguide/CHAP_ReplicationInstance.md "../userguide/CHAP_ReplicationInstance.md").

AWS DMS can stream the changes to the data from `REDO` logs using either Logminer or Binary reader protocols. You can choose this protocol when you create your source endpoint. For detailed comparison on which mode to pickup for CDC replication, see [Using Oracle LogMiner or Binary Reader for CDC](../userguide/CHAP_Source.md#CHAP_Source.Oracle.CDC "../userguide/CHAP_Source.md#CHAP_Source.Oracle.CDC").

Logminer option is easier to set up. However, since our source Oracle database workload involves ETL jobs that result in high volume of transactions, we choose Binary Reader since it offers better performance for ongoing replication.

After you completed the network configurations, you can create a source endpoint.

**To create a source endpoint**

1. Sign in to the AWS Management Console, and open the [AWS DMS console](https://console.aws.amazon.com/dms/v2 "https://console.aws.amazon.com/dms/v2").
2. Choose **Endpoints**, then choose **Create endpoint**.
3. On the **Create endpoint** page, enter the following information.

| Parameter                                              | Action                                                                                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Endpoint type**                                      | Choose **Source endpoint**, turn on **Select RDS DB instance**, and choose an RDS for Oracle instance that you created for this walkthrough.                 |
| **Endpoint identifier**                                | Enter `datalake-source-db`.                                                                                                                                  |
| **Source engine**                                      | Choose **Oracle**.                                                                                                                                           |
| **Access to endpoint database**                        | Choose **Provide access information manually**. Alternatively, you can choose to provide a secret from AWS Secrets Manager that includes connection details. |
| **Server name**                                        | Enter the database server name on Amazon RDS.                                                                                                                |
| **Port**                                               | Enter `1521`.                                                                                                                                                |
| **Secure Socket Layer (SSL) mode**                     | Choose **none**.                                                                                                                                             |
| **User name**                                          | Enter the name of the user that you created for your RDS for Oracle database.                                                                                |
| **Password**                                           | Enter the password that you created for your Oracle DB user.                                                                                                 |
| **SID/Service name**                                   | Enter `SH`.                                                                                                                                                  |
| **Endpoint settings<br>• Extra connection attributes** | Enter `useLogminerReader=N;useBfile=Y;`.                                                                                                                     |

4. Choose **Create endpoint**.
