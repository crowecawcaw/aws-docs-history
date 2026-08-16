# Onboard users to your farm

Onboarding gives a new group of users access to a farm: members of your own
team, an outside vendor or contractor, or another team at your organization. Every
setup differs in the details, but the common steps are the same. The answers to
three questions decide how the checklist applies:

- **Who manages their identity?** You create
  users in the Deadline Cloud console, or they already exist in your organization's
  identity provider.
- **What should they see?** The whole farm, one
  queue on a shared farm, or a separate farm of their own.
- **Who sets up their workstations?** Each
  user sets up their own workstation, or you prepare the workstations in
  advance.
  Work through the following steps for each group that you onboard:

1. **Decide where their work goes** –
   Add a queue to a shared farm for a team inside your organization, or create
   a separate farm when the work must stay isolated, such as for a vendor or
   client. For how to choose, see [Organize your farms, queues, and fleets](organize-farms-queues-fleets.md "organize-farms-queues-fleets.md"). Associate each new queue
   with the fleets that will run its work. See [Associate a queue and fleet](associate-a-queue-and-fleet.md "associate-a-queue-and-fleet.md").
2. **Create their sign-ins** – Monitor
   users come from AWS IAM Identity Center (IAM Identity Center). If your identity source is the IAM Identity Center directory,
   create the users from the Deadline Cloud console. If you use an external identity
   provider such as Okta or Microsoft Entra ID,
   create the users there instead. See [Create and manage users with IAM Identity Center directory](manage-monitor-users_users.md "manage-monitor-users_users.md") and [Manage users with an external identity provider](manage-users-external-idp.md "manage-users-external-idp.md").

###### Note

Monitor sign-ins cover the monitor and the integrated submitters. To
onboard a pipeline developer or a tool that calls the Deadline Cloud API or CLI,
provide AWS credentials instead. See [Getting started with Deadline Cloud resources](../developerguide/getting-started.md "../developerguide/getting-started.md") in the
_Deadline Cloud Developer Guide_. 3. **Grant access** – Assign each user
or group an access level on the farms, queues, and fleets that they'll use.
Grants can be as open or as scoped as your organization works: many
organizations grant everyone broad access across a shared farm, while
others limit each group to its own queue. See [How permissions work in Deadline Cloud](permissions-overview.md "permissions-overview.md"). 4. **Set up their workstations** – Send
each user who submits from a digital content creation (DCC) application a
link to [Set up your workstation](submitter.md "submitter.md"). On that
page, they install the submitter and the monitor desktop application, sign
in with the monitor URL, and connect their DCC. If you use shared storage,
create storage profiles so that file paths map correctly between
workstations and workers. See [Storage profiles in Deadline Cloud](storage-profile.md "storage-profile.md"). For guidance on securing
workstations, see [Security best practices - workstations](security-best-practices.md#workstations "security-best-practices.md#workstations"). 5. **Verify the access** – Have one user
sign in and submit a test job. Confirm that the job completes and that the
user sees the farms and queues that you intend. 6. **Plan the offboarding** – Decide up
front how access ends. When you remove a user or group from IAM Identity Center, they can
no longer sign in to the monitor or access farm resources. See [Create and manage users with IAM Identity Center directory](manage-monitor-users_users.md "manage-monitor-users_users.md").

## Onboard your own artists

You and your artists follow the checklist as written. Create a group
for each department, show, or project, grant the group contributor access on
its queue, and send each artist the link to [Set up your workstation](submitter.md "submitter.md") so they can set up their own workstation. The
same steps apply to any group at your organization that submits work from
workstations. If your organization manages workstations centrally, an
administrator can install the submitter and the monitor on each workstation in
advance. The monitor installer supports a silent install on Windows. Each
user still signs in with their own account.

## Onboard a vendor or contractor

For people outside your organization, isolation and lifecycle matter most.
Create a separate farm for each vendor so that their users can't see the rest
of your organization's work. See [A farm for each vendor or client](organize-farms-queues-fleets.md#organize-vendor-farms "organize-farms-queues-fleets.md#organize-vendor-farms"). For the security details of the
farm boundary, see [Isolate workloads with farms, fleets, and queues](farm-structure.md "farm-structure.md"). To keep unassigned users from
signing in to the monitor at all, enable the require assignments setting. See
[Restricting which users can access the monitor](restrict-user-management-visibility.md "restrict-user-management-visibility.md").

If your identity source is an external identity provider, vendor sign-ins
are guest accounts in that provider, so coordinate account creation and removal
with the team that manages it. Move files with job attachments instead of
granting vendors access to your shared storage. See [Job attachments in Deadline Cloud](storage-job-attachments.md "storage-job-attachments.md"). To cap what a vendor's work can
spend, set a budget on their queue. See [Control costs with a budget](using-budget-manager.md "using-budget-manager.md"). Agree on an end date for the
engagement, and remove the vendor's users and groups when it passes.

## Onboard an internal team

A team inside your organization usually doesn't need the vendor isolation
steps. You can add a queue for the team to your shared farm and grant an
existing group from your identity source contributor access on that queue and
viewer access elsewhere. See [One shared farm, one queue per team](organize-farms-queues-fleets.md#organize-shared-farm "organize-farms-queues-fleets.md#organize-shared-farm"). If you track spending by team, set
a budget on the team's queue.

## Onboard other kinds of users

Some users don't need the full checklist:

- To onboard someone who manages the farm for you, such as a technical
  director, grant them manager or owner access so that they can grant
  permissions and create budgets. See [How permissions work in Deadline Cloud](permissions-overview.md "permissions-overview.md").
- To onboard someone who watches and manages work without submitting
  it, such as a coordinator or supervisor, create a sign-in, grant viewer
  or manager access, and share the monitor URL. The web monitor requires
  no installation. See [Share the Deadline Cloud monitor URL](share-monitor-url.md "share-monitor-url.md").
- To onboard a pipeline developer who builds job bundles, submitters,
  and integrations, provide AWS credentials and the CLI. See [Getting started with Deadline Cloud resources](../developerguide/getting-started.md "../developerguide/getting-started.md") in the
  _Deadline Cloud Developer Guide_.
- If you're building rendering into a product for your own end users,
  see [Deadline Cloud Architecture Guidance](../developerguide/architecture-guidance.md "../developerguide/architecture-guidance.md") in the _Deadline Cloud
  Developer Guide_.
