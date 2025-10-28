# Amazon Detective concepts and terminology

The following terms and concepts are important for understanding Amazon Detective and how it
works.

\***\*Administrator account\*\***

The AWS account that owns a behavior graph and that uses the behavior graph for
investigation.

The administrator account invites member accounts to contribute their data to the behavior
graph. For more information, see [Managing invited member accounts in Detective](accounts-invited-members.md "accounts-invited-members.md").

For the organization behavior graph, the administrator account is the Detective administrator
account that the organization management account designates. For more information, see [Designating the Detective administrator for an
organization](accounts-designate-admin.md "accounts-designate-admin.md"). The Detective administrator account can enable any
organization account as a member account in the organization behavior graph. For more
information, see [Managing organization accounts as Detective member accounts](accounts-orgs-members.md "accounts-orgs-members.md").

Administrator accounts can also view data usage for the behavior graph, and remove member
accounts from the behavior graph.

\***\*Autonomous System Organization (ASO)\*\***

The titled organization which is assigned an autonomous system. This autonomous system is a heterogenous network or a set of networks using similar routing logic and policies.

\***\*Behavior graph\*\***

A linked set of data generated from incoming source data that is associated with one or
more AWS accounts.

Each behavior graph uses the same structure of findings, entities, and
relationships.

\***\*Delegated administrator account (AWS Organizations)\*\***

In Organizations, the delegated administrator account for a service is able to manage the use of a
service for the organization.

In Detective, the Detective administrator account is also the delegated administrator account,
unless the Detective administrator account is the organization management account. The organization
management account cannot be a delegated administrator account.

In Detective, self-delegation is allowed. An organization management account can delegate
their own account to be the delegated administrator of Detective but this would be registered or
remembered only in the scope of Detective and not organizations.

\***\*Detective administrator account\*\***

The account designated by the organization management account to be the administrator
account for the organization behavior graph in a Region. For more information, see [Designating the Detective administrator for an
organization](accounts-designate-admin.md "accounts-designate-admin.md").

Detective recommends that the organization management account chooses an account other than
their account.

If the account is not the organization management account, then the Detective administrator
account is also the delegated administrator account for Detective in Organizations.

\***\*Detective source data\*\***

Processed, structured versions of information from the following types of feeds:

- Logs from AWS services, such as AWS CloudTrail logs and Amazon VPC Flow Logs
- GuardDuty findings

Detective uses the Detective source data to populate the behavior graph. Detective also stores copies
of the Detective source data to support its analytics.

\***\*Entity\*\***

An item extracted from the ingested data.

Each entity has a type, which identifies the type of object it represents. Examples of
entity types include IP addresses, Amazon EC2 instances, and AWS users.

Entities can be AWS resources that you manage, or external IP addresses that have
interacted with your resources.

For each entity, the source data is also used to populate entity properties. Property
values can be extracted directly from source records or aggregated across multiple
records.

\***\*Finding\*\***

A security issue detected by Amazon GuardDuty.

\***\*Finding group\*\***

A collection of related findings, entities, and evidence that may be related to the same
event or security issue. Detective generates finding groups based on a built-in machine learning
model.

\***\*Detective evidence\*\***

Detective identifies additional evidence related to a finding group based on data in your
behavior graph collected within the last 45 days. This evidence is presented as a finding with
the severity value of **Informational**. Evidence provides supporting
information that highlights an unusual activity or unknown behavior that is potentially
suspicious when viewed within a finding group. An example of this might be newly observed
geolocations or API calls observed within the scope time of a finding. At this time, these
findings are only viewable in Detective and not sent to Security Hub.

\***\*Finding overview\*\***

A single page that provides a summary of information about a finding.

A finding overview contains the list of involved entities for the findings. From the list,
you can pivot to the profile for an entity.

A finding overview also contains a details panel that contains the finding
attributes.

\***\*High-volume entity\*\***

An entity that has connections to or from a large number of other entities during a time
interval. For example, an EC2 instance might have connections from millions of IP addresses.
The number of connections exceeds the threshold that Detective can accommodate.

When the current scope time contains a high-volume time interval, Detective notifies the
user.

For more information, see [Viewing details for high-volume
entities](high-degree-entities.md "high-degree-entities.md") in the _Amazon Detective User Guide_.

\***\*Investigation\*\***

The process of triaging suspicious or interesting activity, determining its scope, getting
to its underlying source or cause, and then determining how to proceed.

\***\*Member account\*\***

An AWS account that an administrator account invited to contribute data to a behavior
graph. In the organization behavior graph, a member account can be an organization account that
the Detective administrator account enabled as a member account.

Member accounts that are invited can respond to the behavior graph invitation and remove
their account from the behavior graph. For more information, see [For member accounts: Managing behavior graph
invitations and memberships](member-account-graph-management.md "member-account-graph-management.md").

Organization accounts cannot change their membership in the organization behavior
graph.

All member accounts can also view usage information for their account across the behavior
graphs that they contribute data to.

They have no other access to the behavior graph.

\***\*Organization behavior graph\*\***

The behavior graph that is owned by the Detective administrator account. The organization
management account designates the Detective administrator account. For more information, see [Designating the Detective administrator for an
organization](accounts-designate-admin.md "accounts-designate-admin.md").

In the organization behavior graph, the Detective administrator account controls whether an
organization account is a member account. An organization account cannot remove itself from the
organization behavior graph.

The Detective administrator account can also invite other accounts to the organization
behavior graph.

\***\*Profile\*\***

A single page that provides a collection of data visualizations related to activity for an
entity.

For findings, profiles help analysts to determine whether the finding is of genuine
concern or a false positive.

Profiles provide information to support an investigation into a finding or for a general
hunt for suspicious activity.

\***\*Profile panel\*\***

A single visualization on a profile. Each profile panel is intended to help answer a
specific question or questions to assist an analyst in an investigation.

Profile panels can contain key-value pairs, tables, timelines, bar charts, or geolocation
charts.

\***\*Relationship\*\***

Activity that occurs between individual entities. Relationships are also extracted from
the incoming source data.

Similar to an entity, a relationship has a type, which identifies the types of entities
involved and the direction of the connection. An example of a relationship type is an IP
address connecting to an Amazon EC2 instance.

\***\*Scope time\*\***

The time window that is used to scope the data displayed on profiles.

The default scope time for a finding reflects the first and last times when the suspicious
activity was observed.

The default scope time for an entity profile is the previous 24 hours.
