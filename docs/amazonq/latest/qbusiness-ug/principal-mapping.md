# Principal mapping

Amazon Q Business uses _principal
mapping_ to map users and groups with permissions to access an
Amazon Q Business application environment to their user ids and group membership
information within the data sources that are connected to the
application.

Although user and group mapping is a synchronous, simultaneous process, the
following sections explain them separately for conceptual clarity.

###### Topics

- [User mapping](#user-mapping "#user-mapping")
- [Group mapping](#group-mapping "#group-mapping")

## User mapping

Each Amazon Q Business application environment can have multiple data sources
connected to it. Each data source can have specific users and groups
configured within it. Additionally, a user can be associated with multiple
groups within a data source, or be attached to multiple groups across
multiple data sources. A user attached to multiple data sources can also
have different user IDs within these data sources.

A unique end user who signs in to an Amazon Q Business application environment
must see only chat responses generated from documents that they have access
to. To achieve that objective, Amazon Q Business maps their user IDs
and group IDs within each data source to their identity provider (IdP) login
credentials. Then, Amazon Q Business creates a universally unique
identifier (UUID) to assign to each user. Using the UUID that it creates,
Amazon Q Business stores a comprehensive mapping of the user’s
group membership in an application. During chat, Amazon Q Business
checks this UUID that's stored in its user store and retrieves user access
information to generate chat responses.

The User Store feature also supports the following user management
scenarios:

- **An end user leaves your
  organization.**

When an end user leaves your organization, you can choose to
delete the user from your user store.

- **An end user leaves your organization, and
  their email gets reassigned.**

Because the User Store assigns each user a UUID for secure and
accurate chat responses, using an email reassigned from a previous
UUID to a new one doesn't impact the content that a user sees. Any
new user within your application environment that is using a
reassigned email ID will be assigned a new UUID to be used for
response generation.

- **An end user with multiple login IDs needs
  chat content generated from documents they access using both
  these login IDs.**

With User Store, you can store user aliases attached to end user
UUIDs. For example, a username Saanvi Sarkar uses two login IDs to
sign in to Amazon Q Business—`saanvi_sarkar`
and `saanvi_s`. You can store both IDs under the same
UUID to ensure their chat responses are generated from content that
they access using both login IDs.

## Group mapping

Each Amazon Q Business application environment can have multiple data sources
attached to it. Each data source in an Amazon Q Business application environment
can have multiple groups attached to it. Multiple groups can repeat across
multiple data sources. Additionally, each group across data sources can also
contain multiple subgroups. Each Amazon Q Business application environment also
has an associated identity provider (IdP) that can contain group information
for the users accessing the application.

A unique end user signing in to an Amazon Q Business application environment
must see only chat responses generated from documents within groups that
they have access to. To achieve that objective, Amazon Q Business does
the following:

- Automatically crawls local groups and their associated
  relationships from data sources during the connector configuration
  process.
- Provides you with API operations to map your end users group and
  subgroup membership details within each data source to their IdP
  group membership.

###### Note

As of Dec 17, 2024, Amazon Q Business will recognize all email
addresses as case-insensitive and recognize subaddresses as equivalent
to the original email address. For example, JohnDoe@example.com,
johndoe@example.com, and johndoe+work@example.com will be considered the
same email address. For assistance with applications or to report a
concern, contact Support, sign into the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") .

Then, Amazon Q Business creates a unique user identifier (UUID) to
assign to each user. Under the UUID, Amazon Q Business stores a
comprehensive mapping of the user’s group membership in an application.
During chat, Amazon Q Business checks this UUID that's stored in its
user store and quickly retrieves group access information to generate chat
responses.

The User Store feature supports the following group management
scenarios:

- **Your users mapped to all groups that they
  have access to within an Amazon Q Business
  application.**

Amazon Q Business crawls all groups that a user has access
to in a data source and stores this information under a user's
UUID.

- **Create a subgroup of users within your
  application.**

For example, for a group called `company_employees`,
you might want to create a subgroup `summer_interns` and
specify group level access for the subgroup. You might also want to
group your interns into further subgroups like
`product_interns` and
`engineering_interns`.

- **Map your data source groups to your IdP
  groups.**

A unique end user signing in to an Amazon Q Business
application must see only chat responses generated from documents
within groups they have access to. To support that objective, you
can use Amazon Q to map your end users group membership
details within each data source to their IdP group
membership.

###### Note

Amazon Q Business doesn't interact or crawl this
information from your IdP automatically. To ingest the
relationship between data source groups and IdP groups, use the
Amazon Q Business API.
