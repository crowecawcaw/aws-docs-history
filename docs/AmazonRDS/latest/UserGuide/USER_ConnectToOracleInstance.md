

# Connecting to your Oracle DB instance
<a name="USER_ConnectToOracleInstance"></a>

After Amazon RDS provisions your Oracle DB instance, you can use any standard SQL client application to log in to your DB instance. Because RDS is a managed service, you can't log in as SYS or SYSTEM. For more information, see [RDS for Oracle users and privileges](Oracle.Concepts.Privileges.md).

In this topic, you learn how to use Oracle SQL Developer or SQL\*Plus to connect to an RDS for Oracle DB instance. For an example that walks you through the process of creating and connecting to a sample DB instance, see [Creating and connecting to an Oracle DB instance](CHAP_GettingStarted.CreatingConnecting.Oracle.md). 

**Topics**
+ [Finding the endpoint of your RDS for Oracle DB instance](USER_Endpoint.md)
+ [Connecting to your DB instance using Oracle SQL developer](USER_ConnectToOracleInstance.SQLDeveloper.md)
+ [Connecting to your DB instance using SQL\*Plus](USER_ConnectToOracleInstance.SQLPlus.md)
+ [Considerations for security groups](USER_ConnectToOracleInstance.Security.md)
+ [Considerations for process architecture](USER_ConnectToOracleInstance.SharedServer.md)
+ [Troubleshooting connections to your Oracle DB instance](USER_ConnectToOracleInstance.Troubleshooting.md)
+ [Modifying connection properties using sqlnet.ora parameters](USER_ModifyInstance.Oracle.sqlnet.md)