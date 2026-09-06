

# Reference architecture
<a name="reference-architecture-4"></a>

![Diagram showing QuickSight dashboard end-to-end design](http://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/images/quicksight-dashboard-design.png)




 **Data sources:** Supports connection with traditional Data Warehouse or databases and also have the capacity to connect to non-traditional sources such as SaaS applications. Supported datasources in QuickSight include Amazon S3, Amazon Redshift, Amazon Aurora, Oracle, MySQL, Microsoft SQL Server, Snowﬂake, Teradata, Jira, and ServiceNow. Check [here](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html) for the complete list of data sources supported in QuickSight. These data sources could be secured behind a private subnet and QuickSight can connect in a secure mechanism using strategies such as VPC endpoints, and secure firewalls. 

 **Visualization Tool:** Quick. 

 **Consumers:** Visual dashboard consumers accessing a QuickSight console or embedded QuickSight analytics dashboard. 