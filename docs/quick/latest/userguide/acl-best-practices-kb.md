# Best practices for managing ACLs in knowledge bases

With document-level access control lists (ACLs), Amazon Quick enforces source-document
permissions for an ACL-aware knowledge base. Each authorized user retrieves only the indexed
documents they have permission to access. Use ACLs when different users need access to
different documents in the same knowledge base.

You're responsible for keeping source identities, groups, and document permissions
accurate. Quick enforces the synchronized document permissions on every retrieval. For
supported integrations, it also verifies document access against the source in real time when
returning results. If Quick can't evaluate document permissions for a query, it returns
no documents rather than unfiltered results.

Quick synchronizes identity and document-permission changes on the knowledge base
refresh schedule, which is every 24 hours by default. Configure a different schedule when
your access-change requirements demand it.

###### Sharing and document access are separate controls

Sharing a knowledge base and granting document access are separate controls.
Knowledge-base sharing determines who can use the knowledge base. For ACL-aware knowledge
bases, source-document ACLs further limit which indexed documents each authorized user
can retrieve. Review both controls before granting access.

For more information about configuring ACLs for a specific data source, see
[Amazon S3](s3-integration.md "s3-integration.md"),
[Google Drive](google-drive-kb-acl.md "google-drive-kb-acl.md"), or
[Microsoft SharePoint](sharepoint-kb-acl.md "sharepoint-kb-acl.md"). For
[Atlassian Confluence Cloud](confluence-kb-acl.md "confluence-kb-acl.md") and
[Microsoft OneDrive](onedrive-kb-acl.md "onedrive-kb-acl.md"), configure
document-level ACLs in the console where available.

To verify document-level access controls and troubleshoot permission issues, see
[Check document access (ACL verification)](sync-reports-observability.md#sync-reports-acl-verification "sync-reports-observability.md#sync-reports-acl-verification").

###### Note

Quick treats all email addresses as case-insensitive.
`JohnDoe@example.com`, `johndoe@example.com`, and
`JOHNDOE@example.com` are all considered the same user.

## Plan ACL-aware knowledge bases before creation

Before you create an ACL-aware knowledge base, complete the following steps:

1. Confirm that your integration supports document-level ACLs.
2. Confirm the identity attribute that Quick uses to resolve users and
   groups.

Quick resolves ACLs within the namespace of the knowledge base creator. For
details, see [Limitations](#acl-limitations "#acl-limitations"). 3. Remove shared or recycled identities from source ACLs before you assign them to
another person. 4. Select a refresh schedule that meets your access-change requirements. For
Amazon S3, permission changes take effect at the next sync, so plan the schedule
accordingly. 5. Test document access with representative users before you share the knowledge
base broadly. To check document access, see
[Check document access (ACL verification)](sync-reports-observability.md#sync-reports-acl-verification "sync-reports-observability.md#sync-reports-acl-verification"). 6. Confirm that the knowledge base isn't required for Quick Research. 7. Assign at least one additional owner to an admin-managed knowledge base so that
it remains manageable when its original creator leaves.

## Important user management scenarios

**Understanding email binding**

Email addresses are bound to Quick users dynamically when users initiate chat
interactions. This binding follows a first-come-first-serve approach. The first
user to chat with a given email address establishes the binding for that identity
within the namespace.

**When an employee leaves your organization**

When an employee leaves, clean up their access promptly:

1. Update the ACL configuration files to remove references to their email
   address. For example, in Amazon S3, update the global ACL file or metadata
   files.
2. Refresh the knowledge bases to apply the changes.

This prevents potential security issues if the email is later reassigned to
someone else.

Updating knowledge base ACLs is separate from removing the user from Quick. For
the full model of how user removal affects a user's assets and data, see
[User lifecycle and data handling in Amazon Quick](user-lifecycle-data-handling.md "user-lifecycle-data-handling.md").

**Share admin-managed knowledge bases with co-owners**

Admin-managed knowledge bases (service credentials) are often used across
teams and organizations. If the original creator leaves the company and no
co-owners exist, the knowledge base becomes unmanageable — no one can edit
settings, trigger syncs, or update permissions. To avoid this, share
admin-managed knowledge bases with at least one additional owner. For more
information, see [Sharing knowledge bases and data sources](sharing-kb-datasources.md "sharing-kb-datasources.md").

**When an email address is reassigned to a new employee**

- ACL-aware knowledge base access is automatically locked for the
  reassigned email address to protect data security.
- Contact Quick support to clean up the previous user's access before
  the new employee can access documents associated with that email.

## Limitations

When configuring document-level ACLs for your knowledge bases, be aware of these
limitations:

- **Document-level ACL configuration is permanent**
  – You cannot turn on ACLs for a knowledge base created without ACL support. You
  also cannot turn them off after you turn them on. To change ACL configuration, create a new
  knowledge base with your desired setting from the start.
- **Shared email addresses within a namespace** –
  If multiple Quick users share the same email address within a namespace, the
  system denies access to everyone using that shared email. This safeguard prevents
  accidentally granting document access to the wrong person.
- **ACL resolution scope** – Quick resolves all
  ACLs within the namespace of the knowledge base creator. This applies whether you
  specify ACLs by email address or group name. Quick looks up identities in the
  creator's organizational context to ensure consistent identity resolution.
- **Email address recycling timing** – If your
  organization reassigns an email address from one employee to another, there's an
  important timing consideration. If the previous employee never used Quick for
  chat or AI interactions, and the email is reassigned before the next ACL refresh,
  the new employee may temporarily access documents intended for the previous
  employee.

To avoid this, complete the following steps in order:

    1. Update your ACLs (if applicable, such as in Amazon S3) to remove the
     old user and add the new user.
    2. Manually refresh your knowledge base, or wait for the automatic daily
     refresh.
    3. Assign the email address to the new employee.

This ensures access permissions are properly synchronized before the new user
begins using Quick.

###### Research compatibility

Knowledge bases with document-level ACLs enabled aren't currently compatible with
Quick Research. If you need to use documents from an ACL-enabled knowledge base
for research, create a separate knowledge base without ACLs for those
documents.
