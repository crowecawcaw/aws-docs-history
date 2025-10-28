# EUCPERF05-BP02 Understand integrated storage capabilities (AppStream)

For persistent, per-user storage, AppStream 2.0 offers built-in connectors to Amazon S3 home
folders, Google Drive for Google Workspace, and OneDrive for Business. For more information
on these connectors, see [Enable and Administer
Persistent Storage for Your AppStream 2.0 Users](../../../appstream2/latest/developerguide/persistent-storage.md "../../../appstream2/latest/developerguide/persistent-storage.md").

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Use Amazon S3 home folders when you need a simple, fully-managed solution for persisting
user files between sessions and users don't need to access their files from outside their
AppStream 2.0 sessions. Use Google Drive for Google Workspaces or OneDrive for Business
when you use Windows fleets and your users have a license for one of the services.

If the integrated storage features of Amazon AppStream 2.0 do not offer the
capabilities you require, consider Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, or Amazon EC2 hosted file
sharing. You can use these fully or partly-managed solutions to store user data or user
profiles, such as FSLogix, close to your AWS EUC control plane.
