# Supported commands for generic packages

You can use the AWS CLI or SDK to work with generic packages. The following CodeArtifact commands
work with generic packages:

- [copy-package-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/copy-package-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/copy-package-versions.html") (see [Copy packages between repositories](copy-package.md "copy-package.md"))
- [delete-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package.html") (see [Deleting a package (AWS CLI)](delete-package.md#delete-package-CLI "delete-package.md#delete-package-CLI"))
- [delete-package-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package-versions.html") (see [Deleting a package version (AWS CLI)](delete-package.md#delete-package-version-CLI "delete-package.md#delete-package-version-CLI"))
- [describe-package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-package.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-package.html")
- [describe-package-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-package-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-package-version.html") (see [View and update package version details and
  dependencies](describe-package-version.md "describe-package-version.md"))
- [dispose-package-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/dispose-package-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/dispose-package-versions.html") (see [Disposing of package versions](update-package-version-status.md#dispose-package-versions "update-package-version-status.md#dispose-package-versions"))
- [get-package-version-asset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-package-version-asset.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-package-version-asset.html") (see [Download package version assets](download-assets.md "download-assets.md"))
- [list-package-version-assets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-version-assets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-version-assets.html") (see [List package version assets](list-assets.md "list-assets.md"))
- [list-package-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-versions.html") (see [List package versions](list-packages-versions.md "list-packages-versions.md"))
- [list-packages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-packages.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-packages.html") (see [List package names](list-packages.md "list-packages.md"))
- [publish-package-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/publish-package-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/publish-package-version.html") (see [Publishing a generic package](publishing-using-generic-packages.md#publishing-generic-packages "publishing-using-generic-packages.md#publishing-generic-packages"))
- [put-package-origin-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-package-origin-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-package-origin-configuration.html") (see [Editing package origin controls](package-origin-controls.md "package-origin-controls.md"))

###### Note

You can use the `publish` origin control setting to allow or block publishing of a
generic package name in a repository. However, the `upstream` setting
does not apply to generic packages because they cannot be fetched from an upstream
repository.

- [update-package-versions-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-package-versions-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-package-versions-status.html") (see [Updating package version status](update-package-version-status.md#updating-pv-status "update-package-version-status.md#updating-pv-status"))
