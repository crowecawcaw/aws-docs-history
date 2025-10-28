# DRHCREL03-BP02 Implement failover

mechanisms to maintain highly-available data access and
processing across on-premises, edge, and cloud
environments

Data residency requirements can be addressed through various
high-availability architectures, ranging from fully local
deployments using redundant Outposts to hybrid solutions
leveraging AWS Regions where regulations permit data transfer
with proper consent and controls.

**Desired outcome:** Achieve
seamless operational continuity and data availability across
hybrid infrastructures and consistently meet data residency
requirements even during system failures or disruptions.

**Benefits of establishing this best
practice:** Failover mechanisms enhance reliability,
minimize downtime, and help maintain continuous data
accessibility while complying with data residency regulations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Depending on the specific data residency requirements for your
use-case, high availability can be achieved with the right
architecture and failover strategies in place. We will use the
following five categories of data residency requirements and
apply design reliability best practices and failover
requirements to each.

**Regulations allow data storage outside
the country with user consent as data subjects or the permission
or notification of the regulators (or both).**

As data can reside outside of the country with user consent,
backup and failover strategies can be employed if data controls
are place. Where there are no Local Zones, Outposts should be
deployed with sufficient redundant power and network to meet
availability requirements. To avoid disruptions, the Outposts
should be set up in different physical locations with different
power and network sources (for example, data centers in
different cities). Amazon S3 is available on Outposts racks, and
data can be backed up and recovered from Amazon S3 on the
Outposts similarly to how this is done in the Region.

With consent, the data can be backed up in redundant AWS Region
in the nearest country. AWS Backup, Amazon EBS snapshots, and
Amazon EC2 AMIs offer options for backup of data from EC2
instances to Amazon S3 in the Region. These can also be copied
with consent across Regions if required for additional
reliability. Applications can also be served from the AWS Region
specifically only using the data that has consent and permission
to leave the country.

Regardless of whether Outposts, Local Zones, or Regions are used
to preserve data residency requirements, the failover mechanism
must meet the availability recovery time objectives. AWS offers
Amazon Route 53 and high availability services for failover,
where you can use APIs failover in response to events like
failed health checks.

Failover of on-premises local traffic across Outposts can be
done using networking techniques such as using Border Gateway
Protocol (BGP) Bidirectional Forwarding Detection (BFD) to
failover across Outposts using load balancers or DNS. Fast
failover requires monitoring to be in place to initiate the
failover. This can be done using local health checks or using
Amazon Cloudwatch.

On Outposts, you can replace failed instances with new instances
using automated mechanisms like Amazon EC2 Auto Scaling groups.
Instance auto recovery can restart instances that fail due to
server failures provided there is sufficient spare capacity
available on the remaining servers. Outposts also supports AWS
Application Load Balancer for targets local to the Outposts (for
example, Amazon EC2 instances or containers).

The transfer of data should also be done in a high availability
manner. Outposts offer local gateway (for Outposts racks) and
local network interface (for Outposts Servers), which can send
traffic to the Region over AWS Direct Connect. Direct Connect
offers SLAs, allows private connectivity into one or more AWS Regions, and can be set up with redundancy. For guidance on
setting up AWS Direct Connect resiliency, see
[AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/ "https://aws.amazon.com/directconnect/resiliency-recommendation/").

From a Local Zone, data can be transferred using the VPC if the
local zone is the in same Region as the destination service (for
example, Amazon S3, Amazon EC2, or Amazon EFS). If the traffic
needs to go across Regions or VPCs, VPC peering or AWS Transit Gateway can be used.

**Transfer of in-scope data may be allowed
to countries that adhere to the same specific set of standards
(or higher) than the originating country with permissions or
notification to the regulators.**

In this scenario, retention requirements can be met using Local
Zones and Regions for backup, restore, and failover. However,
the Regions must be carefully selected to ensure that they are
allowed by the country's requirements.

**Primary servicing copy: In a scenario
where the law mandates data residency requirements that specify
that the primary copy of the data must be maintained within the
country or jurisdiction.**

In this scenario, in-scope data can be stored or transferred
outside the borders, but the primary servicing copy must be held
within the border of your jurisdiction. Data can be backed up
outside of the country in the nearest AWS Region into Amazon S3.
If the data is large, use a dedicated virtual interface (VIF)
with Direct Connect for high performance connectivity to Amazon S3. The data must be backed up with sufficient frequency to meet
your recovery point objective (RPO). Since the primary servicing
copy must be in the country, it's not possible to failover
outside the country. As a result, failover must occur across
Local Zones or Outposts within the country.

**In-scope data must be stored and
processed in country.**

In this scenario, if there is no AWS Region or Local Zone
present in the country, then AWS Outposts must be used. Outposts
should be deployed with sufficient redundant power and network
to meet availability requirements. To avoid impact from local
events, the Outposts should be set up in different physical
locations with different power and network sources (for example,
data centers in different cities). Amazon S3 is available on
Outposts, and data can backed-up and recovered from S3 buckets.
