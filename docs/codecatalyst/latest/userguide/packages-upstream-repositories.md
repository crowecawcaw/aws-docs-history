Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring and using upstream repositories

You can connect both gateway repositories, and other CodeCatalyst package repositories, as upstreams to your package repositories.
This enables a package manager client to access the packages that are contained in more than one package repository by
using a single package repository endpoint. The following are the main benefits of using upstream
repositories:

- You only have to configure your package manager with a single repository endpoint to pull from multiple sources.
- Packages consumed from an upstream repository are stored in your downstream repository, which ensures your packages are available
  even if the upstream repository experiences unexpected outages or packages in the upstream repository are deleted.
  You can add upstream repositories when you create a package repository. You can also add
  or remove upstream repositories from existing package repositories in the CodeCatalyst console.

When you add a gateway repository as an upstream repository,
the package repository is connected to the gateway repository's corresponding
public package repository. For a list of supported public package repositories, see
[Supported external package repositories and their gateway repositories](packages-connect-external.md#packages-upstream-repositories-supported-external "packages-connect-external.md#packages-upstream-repositories-supported-external").

You can link multiple repositories together as upstream repositories. For example, suppose that your team creates a
repository named `project-repo` and is already using another repository named `team-repo` that has
the **npm-public-registry-gateway** added as an upstream repository, which is connected
to the public npm repository, `npmjs.com`. You can add `team-repo` as an upstream repository to `project-repo`.
In this case, you only have to configure your package manager to use `project-repo` to pull packages from
`project-repo`, `team-repo`, `npm-public-registry-gateway`, and `npmjs.com`.

###### Topics

- [Adding an upstream repository](packages-upstream-repositories-add.md "packages-upstream-repositories-add.md")
- [Editing the search order of
  upstream repositories](packages-upstream-repositories-search-order.md "packages-upstream-repositories-search-order.md")
- [Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md")
- [Removing an upstream
  repository](packages-upstream-repositories-remove.md "packages-upstream-repositories-remove.md")
