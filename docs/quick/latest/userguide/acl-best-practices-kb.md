# Best practices for managing ACLs in knowledge bases

When using knowledge bases with access control lists (ACLs), you're responsible for
keeping user identities and permissions accurate. This ensures the right people can access the
right documents. Quick automatically syncs identity and document-level ACL changes every
24 hours by default. Any updates to users or permissions will take up to a day to appear
in the system unless you've configured a different refresh schedule for your knowledge
bases.

For more information about configuring ACLs for a specific data source, see
[Amazon S3 integration](s3-integration.md "s3-integration.md").

###### Note

Quick treats all email addresses as case-insensitive.
`JohnDoe@example.com`, `johndoe@example.com`, and
`JOHNDOE@example.com` are all considered the same user.

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

**When an email address is reassigned to a new employee**

- ACL-aware knowledge base access is automatically locked for the
  reassigned email address to protect data security.
- Contact Quick support to clean up the previous user's access before
  the new employee can access documents associated with that email.

## Limitations

When configuring document-level ACLs for your knowledge bases, be aware of these
limitations:

- **Document-level ACL configuration is permanent**
  – You cannot enable ACLs on knowledge bases created without ACL support. You
  also cannot disable ACLs once enabled. To change ACL configuration, create a new
  knowledge base with your desired setting from the start.
- **Shared email addresses within a namespace** –
  If multiple Quick users share the same email address within a namespace, the
  system denies access to everyone using that shared email. This safeguard prevents
  accidentally granting document access to the wrong person.
- **ACL resolution scope** – All ACLs are
  resolved within the Quick namespace of the knowledge base creator. This
  applies whether ACLs are specified by email address or group name. Quick
  looks up identities in the creator's organizational context to ensure consistent
  identity resolution.
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

- **Research compatibility** – Knowledge bases with
  document-level ACLs enabled are not currently compatible with Quick Research. If
  you need to use documents from an ACL-enabled knowledge base for research
  purposes, create a separate knowledge base without ACLs for those
  documents.
