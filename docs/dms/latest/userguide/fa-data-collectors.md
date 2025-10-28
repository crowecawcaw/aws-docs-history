# Discovering databases for migration using data collectors in AWS DMS

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet Advisor
end of support](dms_fleet.md "dms_fleet.md").

To discover your source data infrastructure, you can use either
[AWS Application Discovery Service Agentless Collector](../../../application-discovery/latest/userguide/agentless-collector.md "../../../application-discovery/latest/userguide/agentless-collector.md") or AWS DMS data collectors.
The ADS Agentless Collector is an on-premises application that collects information about your on-premises environment
through agentless methods, including server profile information (for example, OS, number of CPUs, amount of RAM), database metadata,
and utilization metrics. You install the Agentless Collector as a virtual machine (VM)
in your VMware vCenter Server environment using an Open Virtualization Archive (OVA) file.
An AWS DMS _data collector_ is a Windows application that you install in your local environment.
This application connects to your data environment and collects metadata and performance metrics from your on-premises database and analytic servers.
Once database metadata and performance metrics have been collected through
either the ADS Agentless Collector or a DMS data collector, DMS Fleet Advisor
builds an inventory of servers, databases, and schemas that you can migrate to the AWS Cloud.

The DMS data collector is a Windows application which uses .NET libraries, connectors, and data
providers to connect to your source databases for database discovery and data
collection.

The DMS data collector runs on Windows. However, your DMS data collector can collect data from all supported
database vendors regardless of the OS server where they run.

The DMS data collector uses a protected RTPS protocol with TLS encryption to establish a secure
connection with DMS Fleet Advisor. Therefore, your data is encrypted during transit by
default.

AWS DMS has the maximum number of data collectors that you can create for your AWS account.
See the following section for information about AWS DMS service quotas [Quotas for AWS Database Migration Service](CHAP_Limits.md "CHAP_Limits.md").

###### Topics

- [Permissions for a DMS data collector](#fa-data-collectors-permissions "#fa-data-collectors-permissions")
- [Creating a data collector for AWS DMS Fleet Advisor](fa-data-collectors-create.md "fa-data-collectors-create.md")
- [Installing and configuring a data
  collector in AWS DMS](fa-data-collectors-install.md "fa-data-collectors-install.md")
- [Discovering OS and database servers to
  monitor in AWS DMS](fa-discovery.md "fa-discovery.md")
- [Managing monitored objects in AWS DMS](fa-managing-objects.md "fa-managing-objects.md")
- [Using SSL with AWS DMS Fleet Advisor](fa-using-ssl.md "fa-using-ssl.md")
- [Collecting data for AWS DMS Fleet Advisor](fa-collecting.md "fa-collecting.md")
- [Troubleshooting for DMS data collector](fa-collectors-troubleshooting.md "fa-collectors-troubleshooting.md")

## Permissions for a DMS data collector

The database users that you create for the DMS data collector should have read permissions. However,
in some cases, the database user requires the `EXECUTE` permission. For more information,
see [Creating database users for AWS DMS Fleet Advisor](fa-database-users.md "fa-database-users.md").

The DMS data collector requires additional permissions to run the discovery scripts.

- For OS discovery, the DMS data collector needs credentials for the domain server to run requests using
  the LDAP protocol.
- For database discovery in Linux, the DMS data collector needs credentials with `sudo SSH`
  grants. Also, you should configure your Linux servers to allow running remote SSH scripts.
- For database discovery in Windows, the DMS data collector needs credentials with grants
  to run Windows Management Instrumentation (WMI) and WMI Query Language (WQL) queries and read the registry. Also, you should configure
  your Windows servers to allow running remote WMI, WQL, and PowerShell
  scripts.
