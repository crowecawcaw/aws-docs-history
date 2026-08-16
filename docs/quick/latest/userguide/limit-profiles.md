# Limit profiles

|                                                                             |
| --------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick administrators |

With Limits Management, you can monitor resource consumption. You can cap
per-user usage before account-level service limits are reached. You can govern two resource
types: _index storage_ and _agent hours_.

The mechanism is straightforward: you create reusable _limit profiles_
that define per-user caps, then assign those profiles to individual users, roles, or the
entire account as a default. Quick enforces the most specific assignment that
applies to each user.

## Understanding index storage and agent hours

Limit profiles govern two resource types: index storage and agent hours. Understanding
how each is measured helps you set effective per-user caps.

### Index storage

Index capacity is measured by the original (raw) file size of documents at their
source location before any processing by Quick. Supported source locations
include Amazon S3, SharePoint, and Confluence. For full details on how index capacity is
allocated, pooled, and purchased, see
[Index capacity](manage-unstructured-data-capacity.md "manage-unstructured-data-capacity.md").

Index storage allocation is based on user count and subscription tier and is pooled
at the payer-account level. Because the pool is shared, a single heavy user can consume
capacity that would otherwise be available to other users. With limit profiles, you can
cap individual consumption so that no single user exhausts the shared pool.

### Agent hours

Agent hours measure the time consumed by AI-powered features in
Quick. The following activities are metered:

- Quick Research – Time from research request submission until the report completes.
- Quick Flows – Runtime while workflows are actively executing, excluding idle and waiting time.
- Quick Automate – Runtime of deployed automations.
- Desktop app – Time spent actively using the AI assistant.
- Custom apps – Runtime of AI-powered custom applications.
- Artifact generation – Time spent generating documents, presentations, and images.

## Viewing usage

Index capacity consumption is visible three ways: by user, by knowledge base, and
by space. The **Per-user Capacity Overview** table provides an
at-a-glance summary.

The **Per-user Capacity Overview** table provides an at-a-glance
summary with the following columns.

User
The user's display name.

Role
The user's assigned role (Author or Reader).

Storage usage
Current index storage that the user consumed.

Agent-hours usage
Agent hours that the user consumed in the current billing cycle.

Usage distribution
A breakdown of consumption across knowledge bases and spaces.

### User detail side panel

Select a user row to open a side panel that shows the following details:

- Linked limit profiles for each resource type
- Storage consumption compared to the user's effective limit
- Agent-hours consumption for the current billing cycle
- Usage distribution across knowledge bases and spaces

For additional analytics on agent-hours consumption trends, see
[Usage metrics](qs-usage-metrics.md "qs-usage-metrics.md").

## Managing limit profiles

### Create a limit profile

Each limit profile requires a name and at least one limit. You can configure
the following fields:

- **Name** (required) – A descriptive name for the profile.
- **Description** (optional) – Additional context about the profile's purpose.
- **Storage limit** (optional) – The maximum index storage in GB that the user can consume.
- **Agent hours per month** (optional) – The maximum agent hours the user can consume per billing cycle.

You must set at least one of the two limits (storage or agent hours) when
creating a profile.

### Assign a limit profile

You can assign a limit profile to:

- An individual user
- A role (Author or Reader)
- The account default (applies to all users who do not have a more specific assignment)

### Resolution hierarchy

When multiple assignments apply to a user, the most specific assignment
determines the effective limit, in the following priority order:

1. **User-level** – A limit profile assigned directly to a user takes highest priority.
2. **Role-level** – A limit profile assigned to the user's role (Author or Reader) applies if no user-level assignment exists.
3. **Account-level** – The account default profile applies if neither a user-level nor role-level assignment exists.
4. **System default** – The built-in subscription entitlement applies when no admin-configured profile is in effect.

Group-level assignment (assigning a profile to an identity-provider group) is
planned for a future release. When available, group-level assignment will slot
between user-level and role-level in the resolution hierarchy.

## How limits are enforced

As long as a user stays below their effective limit, they can work without
interruption.

When a user reaches 100% of a limit:

- **Index storage** – New file uploads and knowledge base ingestion are blocked for that user.
- **Agent hours** – New agent invocations are blocked until the next billing cycle begins.

Existing content is always preserved. Tightening a limit never deletes files or
knowledge bases.

Enforcement is global across all AWS Regions. Usage in any Region counts toward
the same per-user limit.

## End-user visibility

Your users can view their own consumption in the **My usage**
widget (available in **My stuff**). The widget shows:

- Agent hours used compared to their monthly limit. This value resets at the start of each billing cycle.
- Index storage capacity consumed compared to their effective limit.

For programmatic management of limit profiles, see the Amazon Quick API Reference.
