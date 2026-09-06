

# Admin-managed Google Drive knowledge base setup
<a name="google-drive-kb-admin-managed"></a>

With admin-managed setup, a Google Workspace administrator creates a service account and delegates domain-wide access. Individual users don't need to authorize through sign-in.

Admin-managed setup includes built-in document-level access control list (ACL) support. Amazon Quick automatically syncs ACLs from Google Drive and verifies each user's permissions at query time.

For more information about ACL best practices, see [Best practices for managing ACLs in knowledge bases](acl-best-practices-kb.md).

## Prerequisites
<a name="google-drive-kb-admin-managed-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ Administrator access to your organization's Google Workspace.
+ An Amazon Quick enterprise user account. Administrator access is not required.
+ A Google Workspace account with an email domain that matches the email domain that is used for your Amazon Quick identity.
+ For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Setup overview
<a name="google-drive-kb-admin-managed-overview"></a>

The setup involves the following phases:

1. **Configure Google Workspace** – Create a Google Cloud service account with read-only API access and domain-wide delegation. Then create a dedicated admin user for the service account to impersonate. For more information, see [Configure Google Workspace](google-drive-kb-google-config.md).

1. **Create the knowledge base in Amazon Quick** – Create a Google Drive knowledge base by using the service account credentials from Phase 1. For more information, see [Creating a knowledge base in Amazon Quick](google-drive-kb-connection.md).

Document-level access control is automatically enabled for all admin-managed knowledge bases. For more information about how access controls work, see [Document-level access controls](google-drive-kb-acl.md).

## Known limitations
<a name="google-drive-kb-admin-managed-limitations"></a>
+ File comments synchronization is not supported.

For more information about general ACL limitations and best practices, see [Best practices for managing ACLs in knowledge bases](acl-best-practices-kb.md).