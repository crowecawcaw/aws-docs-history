# Readiness check components

The following diagram illustrates a sample recovery group that is configured to
support the readiness check feature. Resources in this example are grouped into cells (by
AWS Region) and nested cells (by Availability Zones) in a recovery group. There is an
overall readiness status for the recovery group (application), as well as individual
readiness statuses for each cell (Region) and nested cell (Availability Zone).

![A sample recovery group for ARC. It has two cells, by Region, and within each Region, there are 2 nested cells, by Availability Zone. The first Region cell has all ready statuses and the second Region cell has a not ready status because one of its zone cells is not ready. The recovery group is overall not ready.](images/GS_ReacoveryReadinessDiagram.png)
The following are components of the readiness check feature in ARC.

**Cell**

A cell defines your application's replicas or independent units of
failover. It groups all the AWS resources that are necessary for your
application to run independently within the replica. For example, you might have
one set of resources in a primary cell and another set in
a standby cell. You determine the boundary of what a cell includes,
but cells typically represent an Availability Zone or a Region. You can have
multiple cells (nested cells) within a cell, such as AZs within a
Region. Each nested cell represents an isolated unit of failover.

**Recovery group**

Cells are collected into a recovery group. A recovery group represents an application or group of applications that you want to check failover
readiness for. It consists of two or more cells, or replicas, that match each other in terms of functionality. For example, if you have a web
application that is replicated across us-east-1a and us-east-1b, where us-east-1b is your failover environment, you can represent this application
in ARC as a recovery group with two cells: one in us-east-1a and one in us-east-1b. A recovery group can also include a global resource, such
as a Route 53 health check.

**Resources and resource identifiers**

When you create components for readiness checks in ARC, you specify
a resource, such as an Amazon DynamoDB table, a Network Load Balancer, or a DNS target resource, by
using a resource identifier. A resource identifier is either
the Amazon Resource Name (ARN) for the resource or, for a DNS target resource,
the identifier that ARC generates when it creates the resource.

**DNS target resource**

A DNS target resource is the combination of your application's domain name and other
DNS information, such as the AWS resource that the domain points to. Including an AWS
resource is optional but if you provide it, it must be a Route 53 resource record or a Network Load Balancer.
When you provide the AWS resource, you can get more detailed architectural recommendations
that can help you improve your application's recovery resiliency.
You can create resource sets in ARC for DNS target resources, and then create a readiness
check for the resource set so that you can get architecture recommendations for your application.
The readiness check also monitors the DNS routing policy for your application, based on the readiness
rules for DNS target resources.

**Resource set**

A resource set is a set of resources, including AWS resources or DNS target resources, that span multiple cells. For example, you might have a
load balancer in us-east-1a and another one in us-east-1b. To monitor the recovery readiness of the load balancers, you can create a resource set
that includes both load balancers, and then create a readiness check for the resource set. ARC will continually check the readiness of the
resources in the set. You can also add a readiness scope to associate resources in a resource set with the recovery group that you create for your
application.

**Readiness rule**

Readiness rules are audits that ARC performs against a set of
resources in a resource set. ARC has a set of readiness rules for
each type of resource that it supports readiness checks for. Each
rule includes an ID and a description that explains what ARC inspects
the resources for.

**Readiness check**

A readiness check monitors a resource set in your application, such as a set of Amazon Aurora instances, that ARC is auditing recovery readiness
for. Readiness checks can include auditing, for example, capacity configurations, AWS quotas, or routing policies. For example, if you want to
audit readiness for your Amazon EC2 Auto Scaling groups across two Availability Zones, you can create a readiness check for a resource set with two resource
ARNs, one for each Auto Scaling group. Then, to make sure that each group is scaled equally, ARC continually monitors the instance types and the
counts in the two groups.

**Readiness scope**

A readiness scope identifies the grouping of resources
that a specific readiness check encompasses. The scope of a
readiness check can be a recovery group (that is, global to
the whole application) or a cell (that is, a Region or Availability Zone).
For a resource that is a global resource for ARC, set the readiness scope at
to recovery group or global resource level. For example, a Route 53 health
check is a global resource in ARC because it isn't specific to a
Region or Availability Zone.
