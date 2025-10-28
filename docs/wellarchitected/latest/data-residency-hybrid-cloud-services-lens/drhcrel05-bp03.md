# DRHCREL05-BP03 Maintain high availability during on-premises maintenance activities

AWS Outposts hardware failures require proactive management
through EC2 retirement notifications and automated failover
mechanisms.

**Desired outcome:** Achieve high
availability during scheduled maintenance in compliance with
residency regulations throughout the maintenance process.

**Benefits of establishing this best
practice:** Maintaining high availability during
on-premises maintenance activities minimizes service disruptions
and provides high availability while adhering to data residency
requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Hardware on AWS Outposts can eventually fail and will need to be
replaced. If AWS detects an irreparable
[issue
with hardware](../../../outposts/latest/userguide/outpost-maintenance.md#outpost-hardware-maintenance-events "../../../outposts/latest/userguide/outpost-maintenance.md#outpost-hardware-maintenance-events") hosting Amazon EC2 instances running on
your Outpost, AWS notifies the owner of the Outpost and the
owner of the instances that the affected instances are scheduled
for retirement. As a design precaution, customers should
architect for resiliency, just as they do in Regions (for
example, by subscribing to
[instance
retirement](../../../AWSEC2/latest/UserGuide/instance-retirement.md "../../../AWSEC2/latest/UserGuide/instance-retirement.md") notifications).

The Outposts owner and EC2 instance owner (these can be
different AWS accounts, as
[resources
on the Outposts can be shared](../../../outposts/latest/userguide/sharing-outposts.md "../../../outposts/latest/userguide/sharing-outposts.md")) can work together to
resolve the issue. The instance owner could stop and start an
affected instance to migrate it to available capacity. Instance
owners can stop and start the affected instances at a convenient
time.

Otherwise, AWS stops and starts the affected instances on the
instance retirement date. If there is no additional capacity on
the Outpost, the instance remains in the stopped state. The
Outpost owner can try to free up used capacity or request
additional capacity for the Outpost so that the migration can
complete.

If AWS detects an irreparable issue with hardware hosting EC2
instances running on your Outpost, AWS sends an
instance-retirement notice for the affected instance. For more
information, see
[Outposts
rack maintenance](../../../outposts/latest/userguide/outpost-maintenance.md "../../../outposts/latest/userguide/outpost-maintenance.md"). When the AWS installation team arrives
on site, they replace the unhealthy hosts, switches, or rack
elements and bring the new capacity online.

AWS Health events such as instance-retirement are surfaced using
[AWS EventBridge and](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") the
[AWS Health API](../../../health/latest/ug/health-api.md "../../../health/latest/ug/health-api.md"). We recommend updating the correct contact
information, especially the operations contact as described
[in
our accounts documentation so that the correct individuals
receive these events.](../../../accounts/latest/reference/manage-acct-update-contact.md "../../../accounts/latest/reference/manage-acct-update-contact.md")
