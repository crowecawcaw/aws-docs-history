# DRHCREL06-BP01 Use AWS Health to receive EC2 instance retirement notifications and scheduled events on Outposts that may require instance failover ahead of time

Configure AWS Health event monitoring and maintain current
operations contact information while ensuring adequate capacity to
minimize impact during maintenance activities.

**Desired outcome:** Use AWS Health
for getting AWS events signals and taking recommended actions,
providing high availability while meeting data residency
requirements.

**Benefits of establishing this best
practice:** Using AWS Health for proactive notifications
allows for timely planning and initiation of instance failovers,
minimizing potential downtime while meeting data residency
requirements during maintenance events.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Monitor AWS Health events through
[AWS EventBridge,](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
[AWS Health API](../../../health/latest/ug/health-api.md "../../../health/latest/ug/health-api.md"), or email. We recommend updating the correct
contact information, especially the operations contact as
described
[in
our accounts documentation so that the correct individuals
receive these events.](../../../accounts/latest/reference/manage-acct-update-contact.md "../../../accounts/latest/reference/manage-acct-update-contact.md") Provide sufficient capacity and
highly available design to avoid any impact during maintenance
activities.
