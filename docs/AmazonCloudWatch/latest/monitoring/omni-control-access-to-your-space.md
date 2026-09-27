

# Control access to your space
<a name="omni-control-access-to-your-space"></a>

Omni separates setting up access from managing it. You enable Omni, create your domain and space, and grant the first Space Admins in the Amazon CloudWatch console — the setup that [Set up Omni](omni-set-up-omni.md) covers. The identity that creates the space becomes its first Space Admin automatically: setup adds a system managed Space Admin grant for the IAM role or user that ran the setup flow. That grant cannot be removed while it is the last Space Admin grant. Space Admins are the one part of access you can keep managing in the CloudWatch console: it has a page for adding and removing them at any time after setup. Everything else is in the Omni web UI (the other permission levels, data scopes, and access profiles), where a Space Admin adds members and each member's grants decide what they can do and see. This page explains the model; the pages under it carry the procedures and the reference.

The following diagram shows where each piece is created. The **Omni Space Access role** in it is the IAM role the space assumes to reach your AWS resources; the next section explains how it works alongside permission levels.

![Access control in CloudWatch Omni: setup in the CloudWatch console creates the domain and space, adds Space Admins, and creates the Omni Space Access role, and Space Admins can be added or removed there at any time afterwards; all other member management happens in the Omni web UI, where grants carry permission levels, data scopes, and access profiles, and identities arrive from IAM Identity Center or IAM at the domain. Every action passes two checks: the member's permission level and the Omni Space Access role.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-access-control-overview.png)


**Grants and permission levels**

When you add a member to a space or edit their access, you create a **grant** that carries a **permission level**. A grant belongs to a **principal**: a user, a group, an IAM user or role, an access profile, or an alert. This guide calls them all principals, and calls the people among them members.

Each grant carries one permission level:
+ **Viewer**: Read-only access to the whole space, including queries and the Omni agent.
+ **Editor**: Create, modify, and delete resources, run queries, and manage datasets, in addition to everything a Viewer can do.
+ **Space Admin**: Full access, including managing members and their permissions.
+ **Custom**: Exactly the actions you list, optionally limited to specific resources. See [Custom grant actions](omni-custom-grant-actions.md).

A member can hold grants directly and through groups, and the grants combine: their effective access is the union of what all the grants allow. For the tiered levels the highest one wins, and a Custom grant adds exactly the actions it lists. There are no explicit denies; a grant only ever adds access.

A grant applies everywhere the member works (the Omni web UI, the IDE extension, and the API), and one permission level governs every kind of resource: threads, dashboards, alerts, integrations, and agents. You manage grants in the Omni web UI. For the procedure, see [Manage space members and permissions](omni-manage-space-members-and-permissions.md).

**Two layers decide every action**

Two conditions must hold for an action to succeed in a space:
+ The **member's permission level** decides whether that person is allowed to request the operation.
+ The **Omni Space Access role** decides whether the space itself is permitted to carry out the operation against your AWS resources. This is the IAM role you configure for the space when you set it up. The space assumes this role to read your telemetry and, for evaluations, to invoke models on your behalf.

A member can perform an operation only when their permission level allows it and the Space Access role grants the underlying AWS permission it depends on. Raising a member to Space Admin does not add permissions that the Space Access role does not have.

Use permission levels to decide what each person on your team can do, and keep the Space Access role scoped to the AWS permissions the space needs. For how to configure the role during setup, see [Set up Omni](omni-set-up-omni.md).

**Who can sign in and be added**

Identities come from your domain, not from the space. Sign-in is configured through AWS IAM Identity Center at the domain, so members use the identities you already manage, including an external provider such as Okta or Microsoft Entra ID connected through IAM Identity Center. A domain without an identity provider uses IAM instead: members sign in with an IAM user or IAM role, for example through a deep link from the CloudWatch console.

Grants attach to those identities. The users and groups you can add as members are the ones your domain's identity provider supplies, and the IAM users and roles of the space's account. To configure the identity provider, see [Set up Omni](omni-set-up-omni.md).

**Limit what members can see**

By default, every member can read all of the space's telemetry. A **data scope** on a grant narrows that: it filters log and trace rows at read time, wherever the member reads — queries, dashboards, traces, and the Omni agent's answers.

A data scope is a read-time filter on those rows, not a containment boundary for the space. It does not filter metrics, and it does not extend to dataset creation and export, to AI-assisted summaries, or to prompt playground runs, so a member who is scoped out of a field in queries can still reach that content by building a dataset over the underlying traces. Scope the dataset, export, and AI-feature actions as well. See [Limit what members can see](omni-limit-what-members-can-see.md) and [Security best practices for CloudWatch Omni](omni-security-best-practices-for-cloudwatch-omni.md).

**Resources that act on their own**

Some resources act when no one is signed in: an alert evaluates its query on a schedule. An **access profile** gives such a resource an identity of its own, with its own grants. See [Access profiles](omni-access-profiles.md).

**Where to go next**


| To do this | See | 
| --- | --- | 
| Add members and manage their grants | [Manage space members and permissions](omni-manage-space-members-and-permissions.md) | 
| Narrow which telemetry rows a member sees | [Limit what members can see](omni-limit-what-members-can-see.md) | 
| Look up the actions a Custom grant can carry | [Custom grant actions](omni-custom-grant-actions.md) | 
| Give an alert or other resource its own identity | [Access profiles](omni-access-profiles.md) | 
| Review the security model end to end | [Security in CloudWatch Omni](omni-security-in-cloudwatch-omni.md) | 