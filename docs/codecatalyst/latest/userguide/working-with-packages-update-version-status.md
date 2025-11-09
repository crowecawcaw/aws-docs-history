Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Updating a package version's

status

Every package version in CodeCatalyst has a status that describes the current state and
availability of the package version. You can change the package version status in the CodeCatalyst
console. For more information about the possible status values of package versions and their
meanings, see [Package version status](#package-version-status "#package-version-status").

###### To update a package version's status

1. In the navigation pane, choose **Packages**.
2. On the **Package repositories** page, choose the repository that contains the
   package version that you want to update the status of.
3. Search and choose the package from the table.
4. On the **Package details** page, choose **Versions** and
   then choose the version that you want to view.
5. On the **Package version details** page, choose **Actions**
   and then choose **Unlist**, **Archive**, or
   **Dispose**. For information about each package version status, see [Package version status](#package-version-status "#package-version-status").
6. Enter the confirmation text into the text field, and then choose **Unlist**,
   **Archive**, or **Dispose**, depending on which status you
   are updating to.

## Package version status

The following are possible values for package version status. You can change the package version status in the console.
For more information, see [Updating a package version's
status](working-with-packages-update-version-status.md "working-with-packages-update-version-status.md").

- **Published**: The package version is successfully published and
  can be requested by a package manager. The package version will be included in package version
  lists returned to package managers; for example, in the output of `npm view
<package-name> versions`. All assets of the package version are available from
  the repository.
- **Unfinished**: The last attempt to publish did not complete.
  Currently only Maven package versions can have a status of **Unfinished**. This can occur when the client uploads one or more assets for a
  package version but does not publish a `maven-metadata.xml` file for the package
  that includes that version.
- **Unlisted**: The package version assets are available for
  download from the repository, but the package version is not included in the list of versions
  returned to package managers. For example, for an npm package, the output of `npm view
<package-name> versions` does not include the package version. This means that
  the npm dependency resolution logic does not select the package version because the version
  does not appear in the list of available versions. However, if the **Unlisted** package version is already referenced in an `npm
package-lock.json` file, it can still be downloaded and installed; for example, when
  running `npm ci`.
- **Archived**: The package version assets cannot be downloaded.
  The package version will not be included in the list of versions returned to package managers.
  Because the assets are not available, consumption of the package version by clients is
  blocked. If your application build depends on a version that is updated to **Archived**, the build will fail, unless the package version has been
  locally cached. You can't use a package manager or build tool to republish an **Archived** package version because it is still present in the
  repository. However, you can change the package version status back to **Unlisted** or **Published** in the console.
- **Disposed**: The package version doesn't appear in listings, and
  the assets cannot be downloaded from the repository. The key difference between **Disposed** and **Archived** is that with a
  status of **Disposed**, the assets of the package version are
  permanently deleted by CodeCatalyst. For this reason, you cannot move a package version from
  **Disposed** to **Archived**,
  **Unlisted**, or **Published**. The
  package version cannot be used because the assets have been deleted. When a package version
  has been marked as **Disposed**, you are not billed for storage
  of the package assets.

In addition to the statuses in the preceding list, a package version can also be deleted.
After it is deleted, a package version is not in the repository and you can freely republish
that package version by using a package manager or build tool.

## Package name, package version, and asset name normalization

CodeCatalyst normalizes package names, package versions, and asset names before storing them, which means the
names or versions in CodeCatalyst may be different than the name or version provided when the package was published. For more information
about how names and versions are normalized in CodeCatalyst for each package type, see the following documentation.

- [Python package name normalization](python-name-normalization.md "python-name-normalization.md")
- [NuGet package name, version, and asset name normalization](nuget-name-normalization.md "nuget-name-normalization.md")

CodeCatalyst does not perform normalization on other package formats.
