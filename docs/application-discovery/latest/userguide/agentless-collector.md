AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Application Discovery Service Agentless Collector

Application Discovery Service Agentless Collector (Agentless Collector) is an on-premises
application that collects information through agentless methods about your on-premises
environment, including server profile information (for example, OS, number of CPUs, amount
of RAM), database metadata, utilization metrics, and data about network traffic among
on-premises servers. You install the Agentless Collector as a virtual machine (VM)
in your VMware vCenter Server environment using an Open Virtualization Archive (OVA) file.

Agentless Collector has a modular architecture, which allows for the use of
multiple agentless collection methods. Agentless Collector provides modules for
data collection from VMware VMs and from database and analytics servers. It also provides a
module for collecting data about network traffic among your on-premises servers.

Agentless Collector supports data collection for AWS Application Discovery Service (Application Discovery Service) by
collecting usage and configuration data about your on-premises servers and databases, as
well as data about network traffic among your on-premises servers.

Application Discovery Service is integrated with AWS Migration Hub, a service that simplifies your migration tracking
as it aggregates your migration status information into a single console. You can view the
discovered servers, obtain Amazon EC2 recommendations, visualize network connections, group
servers into applications, and then track the migration status of each application from the
Migration Hub console in your home Region.

The Agentless Collector database and analytics data collection module is
integrated with AWS Database Migration Service (AWS DMS). This integration helps plan your migration to the
AWS Cloud. You can use the database and analytics data collection module to discover
database and analytics servers in your environment and build an inventory of servers that
you want to migrate to the AWS Cloud. This data collection module collects database
metadata and actual utilization metrics of CPU, memory, and disk capacity. After you collect
these metrics, you can use the AWS DMS console to generate target recommendations for your
source databases.
