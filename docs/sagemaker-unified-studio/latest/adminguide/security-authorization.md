# Authorization in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio’s interface consists of a management console within AWS and an off-console web
application.

The Amazon SageMaker Unified Studio management console can be used by AWS administrators for
top-level-resource APIs, including creating and managing domains, AWS account associations
for these domains, and data sources for which you want to delegate access management to
Amazon SageMaker Unified Studio. You can use the Amazon SageMaker Unified Studio management console to manage all of the IAM roles and
configuration needed to delegate access management control to the Amazon SageMaker Unified Studio service for
their explicitly configured AWS accounts. The Amazon SageMaker Unified Studio is a first-party AWS Identity
Center application for SSO users. If enabled, the console can also be used by authorized IAM
principals to federate into the Amazon SageMaker Unified Studio instead of using an SSO identity.

Amazon SageMaker Unified Studio is designed to be used principally by AWS IAM Identity Center-authenticated
users or third party Identity Providers who support SAML to manage access to data and
perform data publishing, discovery, subscription, and analytics tasks.

## Authorization in the Amazon SageMaker Unified Studio

console

The Amazon SageMaker Unified Studio console authorization model uses IAM authorization. The console is used
by administrators primarily for setup. Amazon SageMaker Unified Studio uses the concept of a domain
administrator AWS account, and member AWS accounts, and the console is used from all
of these accounts to build the trust relationships while respecting AWS Organization
boundaries.

## Authorization in Amazon SageMaker Unified Studio

The Amazon SageMaker Unified Studio authorization model is a hierarchical ACL with static role archetypes
(profiles) that include administrators and viewers. For example, users can have a
profile of administrator or user. At the level of a domain, they may have a domain user
owner designation. At the level of a project, a user can be an owner or contributor.
These profiles can be configured as one of two types: users and groups.

Within this authorization model, Amazon SageMaker Unified Studio allows users to manage user and group
permissions. Users manage project membership, request membership to projects, and
approve memberships. Users publish data, define data subscription approvers, subscribe
to data, and approve subscriptions.

Users perform data analytics in specific projects when their Amazon SageMaker Unified Studio client requests
IAM session credentials that Amazon SageMaker Unified Studio generates based on the user's effective profile
in the specific project context. This session is scoped both to the user's permissions
and also the specific project's resources. Users then use the projects tools (i.e.
Amazon Athena or Amazon Redshift) to query the relevant data, and all of the underlying
IAM work is completely abstracted away.

Note that only IAM users and SSO users can access the Amazon SageMaker Unified Studio UI. IAM roles cannot
access the Amazon SageMaker Unified Studio UI. But but IAM roles can interact with the Amazon SageMaker Unified Studio through APIs
(searching assets, creating and managing projects, etc.)

## Amazon SageMaker Unified Studio profiles and roles

Once a user is authenticated, the authenticated context maps to a user profile ID.
This user profile can have multiple, different associations (project owner, domain owner
etc.) which is used for authorizing users. Each association (for example, project owner,
domain administrator, etc.) has permissions for certain activities based on the context.
For example, a user that has a domain owner association can create additional domains
andcan assign other domain owners to the domain. A project owner can add or remove
project members for their project, they can create publishing agreements with a domain,
and publish assets to a domain.
