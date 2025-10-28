# Best Practice 11.2 – Define an

approach to maintain availability

Maintain availability by having a resilient architecture that can sustain the failure
of a single technical component or AWS service. Implement mechanisms, which could include
redundant capacity, load balancing, and software clusters.

**Suggestion 11.2.1 – Avoid failures due to exhausted resources or
service deterioration**

Investigate over-provisioning of resources, proactive monitoring of growth, and
throttling usage by setting limits.

The operational excellence pillar covers the different ways in which you can
understand the state of your SAP application and ensure that the appropriate actions are
taken, see [Operational Excellence]: [1 - Design SAP
workload to allow understanding and reaction to its state](design-principle-1.md "design-principle-1.md").

The performance pillar can assist with guidance on right-sizing and scaling capacity
[Performance]: [16 - Understand ongoing performance and
optimization options](design-principle-16.md "design-principle-16.md").

**Suggestion 11.2.2 – Have a strategy for scheduled
maintenance**

If your business has a requirement to minimize scheduled outages, you should develop
a strategy for maintenance at all levels – SAP application, database, operating system,
and AWS. Consider the following:

- Use of replication and cluster solutions to alternate the primary and secondary
  node.
- Excess capacity and mechanisms to scale up and down to facilitate rolling
  outages.
- Use of a live patching approach for the operating system, if possible.
  - [SUSE Linux Enterprise
    Live Patching](https://www.suse.com/products/live-patching/ "https://www.suse.com/products/live-patching/")
  - [Red Hat Reducing downtime for SAP HANA Whitepaper](https://www.redhat.com/cms/managed-files/pa-sap-hana-reducing-downtime-overview-f22788pr-202004-en.pdf "https://www.redhat.com/cms/managed-files/pa-sap-hana-reducing-downtime-overview-f22788pr-202004-en.pdf")

- AWS Documentation: [AWS Systems Manager Patch Manager Patch Groups](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md")
- SAP Note: [1913302

* HANA: Suspend DB connections for short maintenance tasks](https://launchpad.support.sap.com/#/notes/1913302 "https://launchpad.support.sap.com/#/notes/1913302") [Requires SAP
  Portal Access]

- SAP Note: [2077934

* Rolling kernel switch in HA environments](https://launchpad.support.sap.com/#/notes/2077934 "https://launchpad.support.sap.com/#/notes/2077934") [Requires SAP Portal Access]

- SAP Note: [953653 -
  Rolling Kernel Switch](https://launchpad.support.sap.com/#/notes/953653 "https://launchpad.support.sap.com/#/notes/953653") [Requires SAP Portal Access]
- SAP Note: [2254173

* Linux: Rolling Kernel Switch in Pacemaker-based NetWeaver HA environments](https://launchpad.support.sap.com/#/notes/2254173 "https://launchpad.support.sap.com/#/notes/2254173")
  [Requires SAP Portal Access]
  You should also evaluate the elastic capabilities of AWS services to reduce the
  overall downtime of scheduled maintenance by temporarily increasing performance. For
  example, scaling up the size of the Amazon EC2 instance running your database to provide more CPU
  and storage throughput for upgrade activities, or switching your EBS volumes type from
  `gp2` to `io2` to improve storage throughput during a database
  reorganization.

**Suggestion 11.2.3 – Protect SAP single points of failure with
software clusters or other mechanisms**

You can use a high availability (HA) clustering solution for autonomous failover of
SAP single points of failure (SAP Central Services and database) across Availability
Zones.

There are multiple SAP-certified clustering solutions [listed on
the SAP website](https://wiki.scn.sap.com/wiki/display/SI/Certified+HA-Interface+Partners "https://wiki.scn.sap.com/wiki/display/SI/Certified+HA-Interface+Partners"). SAP clustering solutions are supported by the cluster software
vendors themselves, not by SAP. SAP only certifies the solution. Any custom-built solution
is not certified and will need to be supported by the solution builder.

If you choose not to use a clustering solution for your single points of failure,
consider scripting or runbooks to minimize the errors associated with restoring
services.

**Suggestion 11.2.4 – Consider redundant capacity or automatic scaling
for components that support it**

Evaluate static, dynamic, or scheduled capacity changes to match your usage. Examine
the minimum capacity requirements and how they would be impacted by failures and
maintenance. Overprovision where appropriate to allow time to recover from failure.

If you need to maintain 100% capacity in the event of an AZ failure, then you should
consider deploying the application tier across three AZs, each with 50% of the total
required capacity.

In addition to deploying the SAP Application Server Layer across multiple AZs, you
could consider scaling solutions such as the one described in the following SAP on AWS
Blog post that leverages the capabilities of [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling "https://aws.amazon.com/ec2/autoscaling").

- SAP on AWS Blog: [Using AWS to enable SAP Application Auto Scaling](https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/ "https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/")
- AWS Documentation: [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/")
- SAP Note: [1656099

* SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") [Requires SAP
  Portal Access]

**Suggestion 11.2.5 – Ensure the availability of capacity for all
identified failure scenarios**

The following are examples of failure scenarios that could be used to guide your
analysis. Granularity and coverage of the scenarios, classification, and impact will vary
depending on your requirements and architecture.

| Failure scenario examples                                                                                    | Comparative Risk of Occurrence |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Planned / Controlled Maintenance                                                                             | Planned                        |
| Resource exhausted or compromised (High CPU utilization / File system full / Out of memory / Storage issues) | Medium                         |
| Distributed stateless component failure (for example, web dispatchers)                                       | Medium                         |
| Distributed stateful component failure (for example, application servers)                                    | Medium                         |
| Single point of failure (Database / SAP Central Services)                                                    | Medium                         |
| AZ / Network failure                                                                                         | Low                            |
| Core service failure (DNS / Amazon EFS / API calls)                                                          | Low / Medium                   |
| Corruption / Accidental deletion / Malicious activities / Faulty code deployment                             | Low                            |
| Region failure                                                                                               | Very Low                       | Further guidance on capacity reservations is available in [Reliability]: [Suggestion 10.2.5 - Investigate strategies for ensuring capacity](best-practice-10-2.md "best-practice-10-2.md") and in the AWS whitepaper: [Architecture Guidance for Availability and Reliability of SAP on AWS](../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md "../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md"). You can review what Reserved Instances you have available within your AWS account using the [Reserved Instances](../../../AWSEC2/latest/UserGuide/ri-market-concepts-buying.md#view-reserved-instances "../../../AWSEC2/latest/UserGuide/ri-market-concepts-buying.md#view-reserved-instances") section of the Amazon EC2 console. You can review what On-Demand Capacity Reservations you have available using the [Capacity Reservations](../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md#capacity-reservations-view "../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md#capacity-reservations-view") section of the Amazon EC2 console. **Suggestion 11.2.6 – Use AWS services that have inherent availability where applicable** Several AWS services have inherent availability as part of their design and run across multiple Availability Zones for high availability. Some of the relevant services used in an SAP context include: <br>• AWS Service: [Amazon EFS](../../../efs/latest/ug/how-it-works.md "../../../efs/latest/ug/how-it-works.md") <br>• AWS Service: [Elastic Load Balancing](../../../elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.md "../../../elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.md") <br>• AWS Service: [Route 53](https://aws.amazon.com/route53/faqs/ "https://aws.amazon.com/route53/faqs/") <br>• AWS Service: [AWS Transit Gateway](../../../vpc/latest/tgw/how-transit-gateways-work.md "../../../vpc/latest/tgw/how-transit-gateways-work.md") <br>• AWS Service: [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") <br>• AWS Service: [Amazon FSx](../../../fsx/index.md "../../../fsx/index.md") In addition, components that use stateless services, such as bastian hosts or SAProuter, can use Auto Scaling Groups to achieve high availability. **Suggestion 11.2.7 -– Follow AWS best practices to ensure network connectivity** Evaluate one or more of the following AWS best practices to ensure the resilience of network connectivity to the AWS Region in use: <br>• AWS Documentation: [AWS Direct Connect Resiliency Toolkit](../../../directconnect/latest/UserGuide/resilency_toolkit.md "../../../directconnect/latest/UserGuide/resilency_toolkit.md") <br>• AWS Documentation: [AWS VPN CloudHub](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-vpn-cloudhub.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-vpn-cloudhub.md") <br>• AWS Documentation: [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/ "https://aws.amazon.com/cloud-wan/") If your cluster solution relies on an overlay IP consider the following to enable access from outside of the VPC: <br>• AWS Documentation: [SAP on AWS High Availability with Overlay IP Address Routing](../../../sap/latest/sap-hana/sap-ha-overlay-ip.md "../../../sap/latest/sap-hana/sap-ha-overlay-ip.md") |
