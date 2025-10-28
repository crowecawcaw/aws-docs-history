# Configuring available ServiceNow tables to

sync as AWS Config custom resources

In this Connector for ServiceNow release, you can now sync a set of ServiceNow
tables in the CMDB to AWS Config as custom resources.

The ServiceNow tables and AWS Config custom resource mapping are as
follows:

| ServiceNow CMDB table                 | AWS custom resource              |
| ------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cmdb_ci_apache_web_server`           | Apache Web Server                |
| `cmdb_ci_app_server`                  | Application Server               |
| `cmdb_ci_app_server_java`             | Java Server                      |
| `cmdb_ci_app_server_tomcat`           | Tomcat Server                    |
| `cmdb_ci_app_server_tomcat_war`       | Tomcat Web Application           |
| `cmdb_ci_app_server_websphere`        | IBM Websphere Application        |
| `cmdb_ci_app_server_ws_ear`           | Websphere Enterprise Archive     |
| `cmdb_ci_appl`                        | Application                      |
| `cmdb_ci_appl_dot_net`                | A .Net Application               |
| `cmdb_ci_appl_now_app_comp`           | ServiceNow Application Component |
| `cmdb_ci_appl_sap`                    | SAP Application                  |
| `cmdb_ci_appl_sap_hana_db`            | SAP Hana Database                |
| `cmdb_ci_appl_sap_system`             | SAP System                       |
| `cmdb_ci_appl_sharepoint`             | Microsoft Sharepoint Application |
| `cmdb_ci_application_cluster`         | Application Cluster              |
| `cmdb_ci_application_server_resource` | Application Server Resource      |
| `cmdb_ci_application_software`        | Application Software             |
| `cmdb_ci_db_mssql_database`           | MySql Database                   |
| `cmdb_ci_db_mysql_instance`           | MySql Instance                   |
| `cmdb_ci_kubernetes_cluster`          | Kubernetes Cluster               | ###### To configure ServiceNow tables as AWS Config custom resources ###### Note When you configure ServiceNow tables as AWS Config custom resources you might encounter an increase in your billing statement for the creation of additional resources. 1. In the navigator, enter `AWS Service Management`. 2. Choose **Setup**, then **Tables Sync to AWS Config**. 3. Choose **New**. 4. Choose an in scope ServiceNow table. 5. Choose an account and Region for the new resource type. You can select any supported Region, in addition to preconfigured Regions for the account. 6. Click **Submit**. 7. Repeat steps above to include additional ServiceNow tables available to sync as AWS Config custom resources. The amount of time to create new AWS Config resources depends on the number of ServiceNow tables you selected. You can see resources in the **Schema version** field upon successful completion. The period synchronization of resources automatically includes the new AWS Config custom resource type. As details in the ServiceNow table update, this information syncs to AWS Config custom resource. |
