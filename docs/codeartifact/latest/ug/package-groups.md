# Working with package groups in CodeArtifact

_Package groups_ can be used to apply configuration to multiple packages that match a defined pattern using
package format, package namespace, and package name. You can use package groups to more conveniently
configure package origin controls for multiple packages. Package origin controls are used to block or allow ingestion or publishing
of new package versions, which protects users from malicious actions known as dependency substitution attacks.

Every domain in CodeArtifact automatically contains a root package group. This root package group, `/*`, contains all packages,
and allows package versions to enter repositories in the domain from all origin types by default. The root package group can be
modified, but cannot be deleted.

The Package Group Configuration feature operates in an eventually consistent manner when creating a new package group or
deleting an existing package group. This means that upon creating or deleting a package group, the origin controls will be applied
to the expected associated packages, but with some delay due to the eventual consistent behavior. The time to reach eventual consistency
depends on the number of package groups in the domain as well as the number of packages in the domain. There may be a brief period where
the origin controls are not immediately reflected on the associated packages after a package group creation or deletion.

Additionally, updates to package group origin controls are effective almost immediately. Unlike the creation or deletion of package groups,
changes to the origin controls of an existing package group are reflected on the associated packages without the same delay.

These topics contain information about package groups in AWS CodeArtifact.

###### Topics

- [Create a package group](create-package-group.md "create-package-group.md")
- [View or edit a package group](view-edit-package-group.md "view-edit-package-group.md")
- [Delete a package group](delete-package-group.md "delete-package-group.md")
- [Package group origin controls](package-group-origin-controls.md "package-group-origin-controls.md")
- [Package group definition syntax and matching behavior](package-group-definition-syntax-matching-behavior.md "package-group-definition-syntax-matching-behavior.md")
- [Tag a package group](package-group-tags.md "package-group-tags.md")
