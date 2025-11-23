# Best Practice 10.2 – Select an

architecture suitable for your availability and capacity requirements

There are standard architectural patterns for SAP availability to suit the
requirements of most customers deploying SAP on AWS. Use the following suggestions to
determine what patterns best meet your availability and capacity requirements. Evaluate
the risk and impact of each failure scenario against your business requirements.

Additional information on availability in SAP can be found in the whitepaper [Architecture Guidance for Availability and Reliability of SAP on AWS](../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md "../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md").

**Suggestion 10.2.1 – Identify all components and AWS services that
are required for your SAP system**

Identify all the required technical components of your SAP system, starting with the
core (database, application servers, central services, global file systems) and extending
to optional components (for example, Web Dispatchers, SAProuter, Cloud Connector).
Determine the required AWS services to support these components and review the
shared responsibility model for resiliency.

- AWS Documentation: [Shared Responsibility Model for Resiliency](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.md")

**Suggestion 10.2.2 – Use SLAs, durability, availability, and
historical data as a guide to the likelihood of failure**

Likelihood of failure is subjective. Published service level agreements (SLAs) and
past performance can only be used to guide the risk of potential future failure. However,
the assumed frequency of various scenarios remains a useful data point. Something which is
statistically likely to happen once a year might have a greater impact on design decisions
than a failure that is yet to occur.

The following information can be used to better understand the services:

- [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/") provides alerts and remediation guidance when AWS is experiencing
  events that might impact you
- [AWS Post-Event
  Summaries](https://aws.amazon.com/premiumsupport/technology/pes/ "https://aws.amazon.com/premiumsupport/technology/pes/") are provided for all major service events which impact AWS
  service availability
- [Amazon Compute Service Level
  Agreement](https://aws.amazon.com/compute/sla/ "https://aws.amazon.com/compute/sla/") lists service level agreements (SLAs) for compute services
- AWS Documentation: [Amazon EBS Durability and Availability](../../../whitepapers/latest/aws-storage-services-overview/durability-and-availability-3.md "../../../whitepapers/latest/aws-storage-services-overview/durability-and-availability-3.md")
- AWS Documentation: [Amazon EFS
  Data Protection and availability](https://aws.amazon.com/efs/faq/#Data_protection_and_availability "https://aws.amazon.com/efs/faq/#Data_protection_and_availability")
- AWS Documentation: [Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/?nc=sn&loc=4&dn=2 "https://aws.amazon.com/directconnect/resiliency-recommendation/?nc=sn&loc=4&dn=2")
  The likelihood of failure of other supporting services should also be evaluated
  including, but not limited to, domain name services, load balancers, and serverless
  functions.

More information can be found in the [Architecture Guidance for Availability and Reliability of SAP on AWS
whitepaper](../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md "../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md").

**Suggestion 10.2.3 – Assess options for clustering, resilience, and
load balancing**

An SAP system can be distributed across multiple hosts, with differing mechanisms for
ensuring availability. For example, a clustering solution can be used to protect single
points of failure (for example, the SAP database and SAP Central Services). The SAP
application tier can be scaled horizontally and load balancing can be used to make the web
dispatcher highly available.

- AWS Documentation: [SAP NetWeaver Deployment and Operations Guide for Windows - High Availability
  System Deployment](../../../sap/latest/sap-netweaver/net-win-high-availability-system-deployment.md "../../../sap/latest/sap-netweaver/net-win-high-availability-system-deployment.md")
- AWS Documentation: [SAP
  on AWS – IBM Db2 HADR with Pacemaker](../../../sap/latest/sap-AnyDB/sap-ibm-pacemaker.md "../../../sap/latest/sap-AnyDB/sap-ibm-pacemaker.md")
- AWS Documentation: [SQL Server Deployment for High Availability](../../../sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.md "../../../sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.md")
- SAP Documentation: [High Availability Partners](https://wiki.scn.sap.com/wiki/display/SI/High+Availability+Partner+Information "https://wiki.scn.sap.com/wiki/display/SI/High+Availability+Partner+Information")

**Suggestion 10.2.4 - Determine the availability of EC2 instance
families within Availability Zones**

Some Amazon EC2 instance families (for example, `X` and `U`)
are not available across all AZs. Check with your AWS account team or Support to confirm
that the EC2 instance families you want to use are available in the intended Availability
Zones. Note that the logical AZ identifiers might be different across different accounts.
See the AWS documentation for more information.

- AWS Documentation: [AZ
  IDs for your AWS resources](../../../ram/latest/userguide/working-with-az-ids.md "../../../ram/latest/userguide/working-with-az-ids.md")

**Suggestion 10.2.5 – Investigate strategies for ensuring
capacity**

The best way to help ensure capacity is to have a similarly sized instance available
in case of failure. Other strategies include cloud native options (for example, On-Demand
Instances, EC2 instance recovery) or re-allocating shared capacity.

We recommend that you make a capacity commitment in at least two AZs for Amazon EC2
instances that support SAP single points of failure so that the capacity is available at the
time you need it.

Amazon EC2 capacity can be reserved using [Zonal Reserved Instances](../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md "../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md") or [On-Demand Capacity Reservations](../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md"). Both Zonal Reserved Instances and On-Demand
Capacity Reservations can be shared between AWS accounts within the same AWS
organization, which allows for the approach of using sacrificial capacity from another
environment in the event of significant failure (for example, a complete AZ failure).

Further guidance on capacity reservations is available in:

- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md "../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md")

**Suggestion 10.2.6 – Design your VPC across multiple Availability
Zones**

Design your VPC and subnets to ensure that instances can be provisioned in multiple
Availability Zones, even if your initial design only relies on one or two AZs. This builds
resilience into your design and helps ensure that connectivity and access to services can
be confirmed in advance.
