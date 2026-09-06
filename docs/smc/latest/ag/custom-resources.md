

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring available ServiceNow tables to sync as AWS Config custom resources
<a name="custom-resources"></a>

In this Connector for ServiceNow release, you can now sync a set of ServiceNow tables in the CMDB to AWS Config as custom resources.

The ServiceNow tables and AWS Config custom resource mapping are as follows:


| ServiceNow CMDB table | AWS custom resource  | 
| --- | --- | 
| cmdb\_ci\_apache\_web\_server | Apache Web Server | 
| cmdb\_ci\_app\_server | Application Server | 
| cmdb\_ci\_app\_server\_java | Java Server | 
| cmdb\_ci\_app\_server\_tomcat | Tomcat Server | 
| cmdb\_ci\_app\_server\_tomcat\_war | Tomcat Web Application | 
| cmdb\_ci\_app\_server\_websphere | IBM Websphere Application | 
| cmdb\_ci\_app\_server\_ws\_ear | Websphere Enterprise Archive | 
| cmdb\_ci\_appl | Application | 
| cmdb\_ci\_appl\_dot\_net | A .Net Application | 
| cmdb\_ci\_appl\_now\_app\_comp | ServiceNow Application Component | 
| cmdb\_ci\_appl\_sap | SAP Application | 
| cmdb\_ci\_appl\_sap\_hana\_db | SAP Hana Database | 
| cmdb\_ci\_appl\_sap\_system | SAP System | 
| cmdb\_ci\_appl\_sharepoint | Microsoft Sharepoint Application | 
| cmdb\_ci\_application\_cluster | Application Cluster | 
| cmdb\_ci\_application\_server\_resource | Application Server Resource | 
| cmdb\_ci\_application\_software | Application Software | 
| cmdb\_ci\_db\_mssql\_database | MySql Database | 
| cmdb\_ci\_db\_mysql\_instance | MySql Instance | 
| cmdb\_ci\_kubernetes\_cluster | Kubernetes Cluster | 

**To configure ServiceNow tables as AWS Config custom resources**
**Note**  
 When you configure ServiceNow tables as AWS Config custom resources you might encounter an increase in your billing statement for the creation of additional resources. 

1. In the navigator, enter **AWS Service Management**.

1. Choose **Setup**, then **Tables Sync to AWS Config**.

1. Choose **New**.

1. Choose an in scope ServiceNow table.

1. Choose an account and Region for the new resource type. You can select any supported Region, in addition to preconfigured Regions for the account. 

1. Click **Submit**.

1. Repeat steps above to include additional ServiceNow tables available to sync as AWS Config custom resources.

   The amount of time to create new AWS Config resources depends on the number of ServiceNow tables you selected. You can see resources in the **Schema version** field upon successful completion. The period synchronization of resources automatically includes the new AWS Config custom resource type. As details in the ServiceNow table update, this information syncs to AWS Config custom resource. 