Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Publishing packages to a CodeCatalyst package repository

You can publish versions of any supported package type to a CodeCatalyst package repository by
using package manager tools. The steps to publish a package version are as follows:

###### To publish a package version to a CodeCatalyst package repository

1. If you haven't, [create a package repository](packages-repositories-create.md "packages-repositories-create.md").
2. Connect your package manager to your package repository. For instructions on how to connect the npm package manager to a CodeCatalyst package repository,
   see [Configuring and using npm](packages-npm-use.md "packages-npm-use.md").
3. Use your connected package manager to publish your package versions.

###### Contents

- [Publishing and upstream
  repositories](package-publishing.md#package-publishing-upstreams "package-publishing.md#package-publishing-upstreams")
- [Private packages and public repositories](package-publishing.md#package-publishing-upstreams-direct "package-publishing.md#package-publishing-upstreams-direct")
- [Overwriting package assets](package-publishing.md#package-publishing-overwrite-assets "package-publishing.md#package-publishing-overwrite-assets")

## Publishing and upstream

repositories

In CodeCatalyst, you cannot publish package versions that are present in reachable upstream
repositories or public repositories. For example, suppose that you want to publish an npm
package, `lodash@1.0`, to a package repository, `myrepo`, and
`myrepo` is connected to npmjs.com through a gateway repository configured as an
upstream repository. If `lodash@1.0` is present in the upstream repository or in
npmjs.com, CodeCatalyst rejects any attempt to publish to it in `myrepo` by issuing a 409
conflict error. This helps prevent you from accidentally publishing a package with the same name
and version as a package in an upstream repository, which can result in unexpected behavior.

You can still publish different versions of a package name that exist in an upstream
repository. For example, if `lodash@1.0` is present in an upstream repository, but
`lodash@1.1` is not, you can publish `lodash@1.1` to the downstream
repository.

## Private packages and public repositories

CodeCatalyst does not publish packages stored in CodeCatalyst repositories to public repositories,
such as npmjs.com or Maven Central. CodeCatalyst imports packages
from public repositories into a CodeCatalyst repository, but it doesn't move packages in the opposite
direction. Packages that you publish to CodeCatalyst repositories remain private and are only
available to the CodeCatalyst project in which the repository belongs.

## Overwriting package assets

You can't republish a package asset that already exists with different content. For
example, suppose that you already published a Maven package with a JAR asset
`mypackage-1.0.jar`. You can only publish that asset again if the checksum of the
old and new assets are identical. To republish the same asset with new content, delete the
package version first. Trying to republish the same asset name with different content will
result in an HTTP 409 conflict error.

For package formats that support multiple assets (Python and Maven), you can add new assets
with different names to an existing package version at any time, assuming you have the required
permissions. Because npm and NuGet only support a single asset per package version, to modify a
published package version you must first delete it.

If you try to republish an asset that already exists (for example,
`mypackage-1.0.jar`), and the content of the published asset and the new asset are
identical, the operation will succeed because the operation is idempotent.
