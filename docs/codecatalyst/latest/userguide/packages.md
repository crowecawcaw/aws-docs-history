Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Publish and share software packages in CodeCatalyst

Amazon CodeCatalyst contains a fully managed package repository service that makes it easy for your development team to securely store and share software packages used for
application development. These packages are stored in package repositories, which are created and organized within projects in CodeCatalyst.

A single package repository can store packages of
every supported package type. CodeCatalyst supports the following package formats:

- npm
- Maven
- NuGet
- Python
  Packages in a package repository can be discovered and
  shared between members of the project that contains the repository.

To publish packages to, and consume packages from a repository, configure a package manager to use the repository endpoint (URL).
You can then use the package manager to publish packages to the repository. You can use package managers such as Maven, Gradle, npm,
yarn, nuget, dotnet, pip, and twine.

You can also configure CodeCatalyst workflows to use CodeCatalyst package repositories. For more
information about using packages in workflows, see [Connecting package repositories to workflows](workflows-packages.md "workflows-packages.md").

You can make packages in one package repository available to another repository in the same project by
adding it as an upstream repository. All package versions available to the upstream repository are also available to the downstream
repository. For more information, see [Configuring and using upstream repositories](packages-upstream-repositories.md "packages-upstream-repositories.md").

You can make open-source packages available to your CodeCatalyst repository by creating a special type of repository called a **gateway**.
Upstreaming to a gateway repository allows you to consume packages from popular public repositories such as npmjs.com and pypi.org, and automatically
cache them in your CodeCatalyst repository. For more information, see [Connecting to public external repositories](packages-connect-external.md "packages-connect-external.md").

###### Topics

- [Packages concepts](packages-concepts.md "packages-concepts.md")
- [Configuring and using package repositories](packages-repositories.md "packages-repositories.md")
- [Configuring and using upstream repositories](packages-upstream-repositories.md "packages-upstream-repositories.md")
- [Connecting to public external repositories](packages-connect-external.md "packages-connect-external.md")
- [Publishing and modifying packages](working-with-packages.md "working-with-packages.md")
- [Using npm](packages-npm.md "packages-npm.md")
- [Using Maven](packages-maven.md "packages-maven.md")
- [Using NuGet](packages-nuget.md "packages-nuget.md")
- [Using Python](packages-python.md "packages-python.md")
- [Quotas for packages](packages-quotas.md "packages-quotas.md")
