AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Using the database and analytics data collection module

This section describes how to set up, configure, and use a database and analytics data
collection module. You can use this data collection module to connect to your data
environment and collect metadata and performance metrics from your on-premises databases and
analytics servers. For information about the metrics that you can collect with this module,
see [Data collected by the Agentless Collector database and analytics data collection module](agentless-collector-data-collected-database-analytics.md "agentless-collector-data-collected-database-analytics.md").

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet Advisor
end of support](../../../dms/latest/userguide/dms_fleet.md "../../../dms/latest/userguide/dms_fleet.md").

At a high level, when using the database and analytics data collection module, you take
the following steps.

1. Complete the prerequisite steps, configure your IAM user, and create the AWS DMS
   data collector.
2. Configure data forwarding to make sure that your data collection module can send
   the collected metadata and performance metrics to AWS.
3. Add your LDAP servers and use them to discover OS servers in your data
   environment. Alternatively, add your OS servers manually or use the [Using the VMware data
   collection module](agentless-collector-gs-data-collection-vcenter.md "agentless-collector-gs-data-collection-vcenter.md").
4. Configure connection credentials to your OS servers and then use them to discover
   database servers.
5. Configure connection credentials to your database and analytics servers and then
   run the data collection. For more information, see [Database and analytics data collection](agentless-collector-dashboard.md#using-collector-data-collect-database-analytics "agentless-collector-dashboard.md#using-collector-data-collect-database-analytics").
6. View collected data in the AWS DMS console and use it to generate target
   recommendations for a migration to the AWS Cloud. For more information, see [Database and analytics data collection](agentless-collector-dashboard.md#using-collector-data-collect-database-analytics "agentless-collector-dashboard.md#using-collector-data-collect-database-analytics").

###### Topics

- [Supported OS, database, and analytics servers](#agentless-collector-gs-database-analytics-collection-supported-servers "#agentless-collector-gs-database-analytics-collection-supported-servers")
- [Creating the AWS DMS data collector](agentless-collector-gs-database-analytics-collection-resources.md "agentless-collector-gs-database-analytics-collection-resources.md")
- [Configuring data forwarding](agentless-collector-gs-database-analytics-collection-prerequisites.md "agentless-collector-gs-database-analytics-collection-prerequisites.md")
- [Adding your LDAP and OS servers](agentless-collector-gs-database-analytics-collection-add-servers.md "agentless-collector-gs-database-analytics-collection-add-servers.md")
- [Discovering your database servers](agentless-collector-gs-database-analytics-collection-discovery.md "agentless-collector-gs-database-analytics-collection-discovery.md")
- [Data collected by the Agentless Collector database and analytics data collection module](agentless-collector-data-collected-database-analytics.md "agentless-collector-data-collected-database-analytics.md")

## Supported OS, database, and analytics servers

The database and analytics data collection module in the Agentless Collector supports
Microsoft Active Directory LDAP servers.

This data collection module supports the following OS servers.

- Amazon Linux 2
- CentOS Linux version 6 and higher
- Debian version 10 and higher
- Red Hat Enterprise Linux version 7 and higher
- SUSE Linux Enterprise Server version 12 and higher
- Ubuntu version 16.01 and higher
- Windows Server 2012 and higher
- Windows XP and higher

Also, the database and analytics data collection module supports the following
database servers.

- Microsoft SQL Server version 2012 and up to 2019
- MySQL version 5.6 and up to 8
- Oracle version 11g Release 2 and up to 12c, 19c, and 21c
- PostgreSQL version 9.6 and up to 13
