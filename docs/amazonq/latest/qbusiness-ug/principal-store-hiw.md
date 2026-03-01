# How the User Store works

Each document in any data source has access control list (ACL) information
inherently attached to it as metadata. ACLs contain information about which
users and groups have access to a document.

Connectors support crawl ACL and identity information where applicable based
on the data source. To index documents without ACLs (as public documents) ensure
the documents you want to index from your data source are public documents in
the enterprise data source the connectors index the content from.

An Amazon Q Business connector updates any changes in ACLs each time
that your data source content is crawled. To capture ACL changes to make sure
that the right end users have access to the right content, re-sync your data
source regularly.

###### Note

As of Dec 17, 2024, Amazon Q Business will recognize all email
addresses as case-insensitive and recognize subaddresses as equivalent to
the original email address. For example, JohnDoe@example.com,
johndoe@example.com, and johndoe+work@example.com will be considered the
same email address. For assistance with applications or to report a concern,
contact Support, sign into the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") .

###### Note

Amazon Q Business supports crawling ACLs for document security by
default. As a general rule, turning off ACLs and identity crawling once they
have been enabled are no longer supported. In preparation for [connecting Amazon Q Business applications to
IAM Identity Center](migrate-application.md "migrate-application.md"), enable ACL indexing and identity crawling for secure
querying and re-sync your connector. Once you turn ACL and identity crawling
on you won't be able to turn them off. Certain connectors provide you with
the ability to manage ACLs by enabling or disabling them during data source
creation. To create a data source with ACLs disabled, you need specific
IAM permissions. For more information, see [Setting up](setting-up.md "setting-up.md").

Each data source also contains information about the users and groups which
have access to it. Amazon Q Business crawls information about users and
groups attached to each data source and automatically extracts and maps user and
group information internally. Amazon Q Business then stores this crawled
identity information in the user store and uses it to match and map user and
group IDs with their document access details.

If you delete a group in the User Store and then re-create it later with the
same name but with different group members, document ACLs which contain this
group may be impacted. We recommend that this type of change (deleting or
re-creating a group with the same name but with different group members) be done
in the data source instead of the Amazon Q Business User Store.

Using a reassigned email address requires deleting the original user’s UUID
from the User Store. This is because Amazon Q Business verifies that the
new user's IAM Identity Center attributes match those in the User Store. If the previous email
address user UUID is not deleted, and the previous user’s attributes are found,
API calls will be denied.

###### Important

Inadvertent mistakes when you update the User Store’s user, group, group
membership, and mapping information can result in unintentional and
unacceptable changes in the accessibility of documents to users.

Treat the ability to update the User Store to create users, update users,
delete users, create groups, update groups, delete groups (i.e, create
update delete operations), and update the mappings, as a privileged
operation.

Ensure that access to the User Store APIs is provided only to admin who
fully understand how to use these APIs and the implications of these changes
on your document security. We recommend establishing a documented approval
process be followed for making such changes.

The following overview describes how principal mapping works by using either
the console or the Amazon Q Business API.

###### Topics

- [Using the console](#principal-store-hiw-console "#principal-store-hiw-console")
- [Using the API](#principal-store-hiw-api "#principal-store-hiw-api")

## Using the console

Each document in any data source has access control list (ACL) information
inherently attached to it as metadata. ACLs contain information about which
users and groups have access to a document. To ensure document security,
Amazon Q Business crawls ACL information by default. Then, the
connector automatically extracts and maps document access information
internally.

When you crawl this ACL information, Amazon Q Business stores it in
its internal user store to assess which user IDs have access to a
document.

Each data source also contains information about the users and groups
which have access to it. During data source connector configuration, Amazon Q Business crawls information about users and groups attached to
each data source. Then, the connector automatically extracts and maps user
and group information internally.

Amazon Q Business stores this crawled identity information in the
user store and uses it to match and map user and group ids with their
document access details. You can only use the **Identity
crawler** feature if you also crawl ACLs using the
**Authorization** feature.

If you use the console, you must re-sync your data to your index to
capture any changes in the ACL and user and group membership within your
data source.

For more information regarding setting up user mapping for specific
connectors, consult the detailed ACL crawling documentation section for that
connector. For example, if you need to set up user mapping for Salesforce
Online, see [How Amazon Q Business connector crawls Salesforce ACLs](salesforce-user-management.md "salesforce-user-management.md").

## Using the API

When you configure your Amazon Q Business application, you use the
following API operations to create your principal mapping
solution:

**User management**

- [CreateUser](../api-reference/API_CreateUser.md "../api-reference/API_CreateUser.md") –
  Creates a universally unique identifier (UUID) that's mapped to a
  list of local user IDs within a data source.
- [DeleteUser](../api-reference/API_DeleteUser.md "../api-reference/API_DeleteUser.md") —
  Deletes a UUID that's mapped to a user.
- [UpdateUser](../api-reference/API_UpdateUser.md "../api-reference/API_UpdateUser.md") –
  Updates local user IDs within a data source that are mapped to a
  UUID.
- [GetUser](../api-reference/API_GetUser.md "../api-reference/API_GetUser.md") –
  Lists information associated with a user ID.

**Group management**

- [PutGroup](../api-reference/API_PutGroup.md "../api-reference/API_PutGroup.md") –
  Creates, or updates, a mapping of users to groups, or groups to
  subgroups. You can use this API operation to:
  - Map a group from groups in the data source to groups in
    your IdP.
  - Map a list of users and sub groups (for example,
    `Interns`) to a group (for example,
    `Interns 2023`).

- [DeleteGroup](../api-reference/API_DeleteGroup.md "../api-reference/API_DeleteGroup.md") –
  Deletes a group or a subgroup.
- [GetGroup](../api-reference/API_GetGroup.md "../api-reference/API_GetGroup.md") –
  Lists information about a group.
