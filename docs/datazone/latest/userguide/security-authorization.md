# Authorization in Amazon DataZone

Amazon DataZone’s interface consists of a management console within AWS and an off-console
web application (data portal).

The Amazon DataZone management console can be used by AWS administrators for
top-level-resource APIs, including creating and managing domains, AWS account
associations for these domains, and data sources for which you want to delegate access
management to Amazon DataZone. You can use the Amazon DataZone management console to manage all of the
IAM roles and configuration needed to delegate access management control to the Amazon DataZone
service for their explicitly configured AWS accounts. The Amazon DataZone data portal is a
first-party AWS Identity Center application for SSO users. If enabled, the console can
also be used by authorized IAM principals to federate into the data portal instead of using
an SSO identity.

Amazon DataZone's data portal is designed to be used principally by AWS IAM Identity
Center-authenticated users to manage access to data and perform data publishing, discovery,
subscription, and analytics tasks.

## Authorization in the Amazon DataZone

console

The Amazon DataZone console authorization model uses IAM authorization. The console is used
by administrators primarily for setup. Amazon DataZone uses the concept of a domain
administrator AWS account, and member AWS accounts, and the console is used from all
of these accounts to build the trust relationships while respecting AWS Organization
boundaries.

## Authorization in the Amazon DataZone

portal

The Amazon DataZone data portal authorization model is a hierarchical ACL with static role
archetypes (profiles) that include administrators and viewers. For
example, users can have a profile of administrator or user. At the level of a domain,
they may have a domain user designation of data owner. At the level of a
project, a user can be an owner or contributor. These profiles can be
configured as one of two types: users and groups. These profiles are then associated
with domains and projects, and the state for these permissions is stored in an
association table.

Within this authorization model, Amazon DataZone allows users to manage user and group
permissions. Users manage project membership, request membership to projects, and
approve memberships. Users publish data, subscribe
to data, and approve subscriptions.

Users perform data analytics in specific projects when their data portal client
requests IAM session credentials that Amazon DataZone generates based on the user's effective
profile in the specific project context. This session is scoped both to the user's
permissions and also the specific project's resources. Users then drop into Athena or
Redshift to query the relevant data, and all of the underlying IAM work is completely
abstracted away.

## Amazon DataZone profiles and roles

Once a user is authenticated, the authenticated context maps to a user profile ID.
This user profile can have multiple, different associations (project owner, domain
administrator, etc.) which is used for authorizing users. Each association (for example,
project owner, domain administrator, etc.) has permissions for certain activities based
on the context. For example, a user that has a domain admin association can create
additional domains, can assign other domain administrators to the
domain, and can create project templates within their domain. A project owner can add or
remove project members for their project, and publish assets to a domain.
