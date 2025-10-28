# DRHCREL05-BP04 Design your environment to maintain availability and recover in case of failure in a critical sub-system like networking, server, rack, or within the application itself

You should consider the failure modes in this section when
planning your Outposts and application deployments. The following
sections review how to mitigate these failure modes to provide an
increased level of high availability for your application
environment.

**Desired outcome:** Achieve a
fault-tolerant application architecture that can withstand
failures at various levels of the infrastructure stack and
application, which provides high availability and consistent
adherence to data residency regulations, even during unexpected
system disruptions.

**Benefits of establishing this best
practice:** Implementing high availability mechanisms
across all critical sub-systems and application components
enhances overall system reliability, minimizes downtime, and
maintains compliance with data residency requirements.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

**Failure mode 1: Network**

An Outpost deployment depends on a resilient connection to its
parent Region for management and monitoring. Network disruptions
may be caused by a variety of failures, such as operator errors,
equipment failures, and service provider outages. An Outpost,
which may be comprised of one or more racks connected together
at the site, is considered disconnected when it cannot
communicate with the Region through the service link.

Redundant network paths can help mitigate the risk of disconnect
events. You should map application dependencies and network
traffic to understand the impact disconnect events will have on
workload operations. Plan sufficient network redundancy to meet
your application's availability requirements (for more detail,
see
[AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/ "https://aws.amazon.com/directconnect/resiliency-recommendation/")).

During a disconnect event, instances running on an Outpost
continue to run and are accessible from on-premises networks
through the Outpost local gateway. Local workloads and services
may be impaired or fail if they rely on services in the Region.
Mutating requests (like starting or stopping instances on the
Outpost), control plane operations, and service telemetry (for
example, CloudWatch metrics) will fail while the Outpost is
disconnected from the Region. It is best to practice to run
[game
days](../reliability-pillar/rel_testing_resiliency_game_days_resiliency.md "../reliability-pillar/rel_testing_resiliency_game_days_resiliency.md") to test service link and local gateway connection
failures.

**Failure mode 2: Instances**

EC2 instances may become impaired or fail if the server they are
running on has an issue or if the instance experiences an
operating system or application failure. How applications handle
these types of failures depends on the application architecture.
Monolithic applications typically use application or system
features for recovery, while modular service-oriented or
microservices architectures typically replace failed components
to maintain service availability.

On Outposts racks with local Amazon S3 storage, you can replace
failed instances with new instances using automated mechanisms
like EC2 Auto Scaling groups and using shared storage service
like Amazon S3, multi-AZ Amazon RDS, or Amazon EBS to maintain
stateful application data.

AWS Elastic Disaster Recovery (AWS DRS) is available on AWS Outposts racks for reliable recovery in the event of a site
failure (for more detail, see
[Architecting
for Disaster Recovery on AWS Outposts racks with AWS Elastic
Disaster Recovery](https://aws.amazon.com/blogs/compute/architecting-for-disaster-recovery-on-aws-outposts-racks-with-aws-elastic-disaster-recovery/ "https://aws.amazon.com/blogs/compute/architecting-for-disaster-recovery-on-aws-outposts-racks-with-aws-elastic-disaster-recovery/")). Use AWS Outposts static stability for
Amazon EC2 instances backed by EC2 instance store. This enables
automatic recovery for workloads running on such EC2 instances
from power failures or reboots, even when the connection to the
parent AWS Region is temporarily unavailable.

**Failure mode 3: Compute**

Compute hardware can fail or become impaired and may need to be
taken out of operation (temporarily or permanently) for a
variety of reasons, such as component failures and scheduled
maintenance operations. How services on Outposts rack handle
hardware failures and impairments varies and can depend on how
customers configure high availability options. 

You should order sufficient compute capacity to support an N+M
availability model, where N is the required capacity and M is
the spare capacity provisioned to accommodate server failures.

On-premises hardware replacements for failed components are
completed by AWS as part of the fully-managed AWS Outposts Rack
service. AWS actively monitors the health of all servers and
networking devices in an Outpost deployment. If there is a need
to perform physical maintenance, AWS schedules a time to visit
your site to replace failed components.

Provisioning spare capacity allows you to keep your workloads
running while failed servers are taken out of service and
replaced. To improve reliability across hardware components,
[placement
groups](../../../AWSEC2/latest/UserGuide/placement-groups-outpost.md "../../../AWSEC2/latest/UserGuide/placement-groups-outpost.md") with a spread strategy on an Outpost can spread
instances across hosts or racks. Outposts servers with hardware
failures can be returned, and replacements are shipped out as
part of the
[replacement
process](../../../outposts/latest/server-userguide/shipping-outposts-server.md "../../../outposts/latest/server-userguide/shipping-outposts-server.md").

**Failure mode 4: Racks or data
centers**

Rack failures may occur due to a total loss of power to racks or
due to environmental failures like loss of cooling or physical
damage to the data center from a flood or earthquake.
Deficiencies in data center power distribution architectures or
errors during standard data center power maintenance can result
in loss of power to one or more racks or even the entire data
center.

These scenarios can be mitigated by deploying infrastructure to
multiple data center floors or locations that are independent
from one another within the same campus or metro area. Taking
this approach with AWS Outposts rack requires careful
consideration for how applications are architected and
distributed to run across multiple separate logical Outposts to
maintain application availability.

**Failure mode 5: AWS Availability Zone or
Region**

Each Outpost is anchored to a specific Availability Zone within
an AWS Region. Failures within the anchor Availability Zone or
parent Region could cause the loss of Outpost management and
mutability and may disrupt network communication between the
Outpost and the Region.

Similar to network failures, Availability Zone or Region
failures may cause the Outpost to become disconnected from the
Region. The instances running on an Outpost continue to run and
are accessible from on-premises networks through the Outpost
local gateway and may be impaired or fail if they rely on
services in the Region.

To mitigate the impact of Availability Zone and Region failures,
you can deploy multiple Outposts each anchored to a different
Availability Zone or Region. You may then design your workload
to operate in a distributed multi-Outpost deployment model using
many of the similar
[mechanisms
and architectural patterns](../reliability-pillar/design-principles.md "../reliability-pillar/design-principles.md") that you use to design and
deploy on AWS today.
