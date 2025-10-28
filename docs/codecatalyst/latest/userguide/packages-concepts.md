Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Packages concepts

Here are some concepts and terms to know when managing, publishing, or consuming packages in CodeCatalyst.

## Packages

A _package_ is a bundle that includes both software and the metadata that is
required to install the software and resolve any dependencies. CodeCatalyst supports the npm package format.

A package consists of:

- A name (for example, `webpack` is the name of a
  popular npm package)
- An optional [namespace](#packages-concepts-package-namespaces "#packages-concepts-package-namespaces")
  (for example, `@types` in `@types/node`)
- A set of [versions](#packages-concepts-package-versions "#packages-concepts-package-versions")
  (for example, `1.0.0`, `1.0.1`, `1.0.2`)
- Package-level metadata (for example, npm dist tags)

## Package namespaces

Some package formats support hierarchical package names to organize packages into
logical groups and to help avoid name collisions. Packages that have the same name can
be stored in different namespaces. For example, npm supports scopes, and the
npm package `@types/node` has a scope
of `@types` and a name of `node`. There are many other package
names in the `@types` scope. In CodeCatalyst, the scope (“types”) is referred to as
the package namespace, and the name (“node”) is referred to as the package name.
For Maven packages, the package namespace corresponds to the Maven groupID. The Maven
package `org.apache.logging.log4j:log4j` has a groupID (package namespace) of
`org.apache.logging.log4j` and the artifactID (package name)
`log4j`. Some package formats such as Python don't support hierarchical
names with a concept similar to npm scope or Maven groupID. If you don't
have a way to group package names, it can be more difficult to avoid name
collisions.

## Package versions

A _package version_ identifies the specific version of a
package, such as `@types/node@12.6.9`. The version number format and
semantics vary for different package formats. For example, npm package versions must
conform to the [Semantic Versioning
specification](https://semver.org/ "https://semver.org/"). In CodeCatalyst, a package version consists of the version
identifier, package-version-level metadata, and a set of assets.

## Assets

An _asset_ is an individual file stored in CodeCatalyst that is
associated with a package version, such as an npm `.tgz` file or a Maven POM or JAR file.

## Package repositories

A CodeCatalyst _package repository_ contains a set of [packages](#packages-concepts-packages "#packages-concepts-packages"), which contain
[package versions](#packages-concepts-package-versions "#packages-concepts-package-versions"), each of which maps to a set of [assets](#packages-concepts-assets "#packages-concepts-assets").
Package repositories are polyglot, meaning a single repository can contain packages of any
supported type. Each package repository exposes endpoints for fetching and publishing
packages using tools like the NuGet CLIs (`nuget`, `dotnet`), the `npm` CLI,
the Maven CLI (`mvn`), and the Python CLIs (`pip` and `twine`).
For information about packages quotas in CodeCatalyst, including how many package
repositories can be created in each space, see [Quotas for packages](packages-quotas.md "packages-quotas.md").

You can link a package repository to another by setting it as an upstream. When a repository is set as an upstream, you can
use any package from the upstream as well as any additional upstream repositories in the chain. For more information, see [Upstream repositories](#packages-concepts-upstream-repositories "#packages-concepts-upstream-repositories").

Gateway repositories are a special type of package repository that pulls and stores packages from official external package authorities.
For more information, see [Gateway repositories](#packages-concepts-gateway-repositories "#packages-concepts-gateway-repositories").

## Upstream repositories

You can use CodeCatalyst to create an upstream relationship between two package repositories.
A package repository is an _upstream_ of another when the package
versions it contains can be accessed from the package repository endpoint of the
downstream repository. With an upstream relationship, the contents of the two package
repositories are effectively merged from the point of view of a client.

For example, if a
package manager requests a package version that does not exist in a repository, CodeCatalyst
will then search configured upstream repositories for the package version. Upstream repositories are searched
in the order they are configured, and once a package is found, CodeCatalyst will stop searching.

## Gateway repositories

A _gateway repository_ is a special type of package repository that is connected to
a supported external, official package authority. When you add a gateway repository as an
[upstream repository](#packages-concepts-upstream-repositories "#packages-concepts-upstream-repositories"), you can consume packages from the
corresponding official package authority. Your downstream repository does not communicate to the public repository, instead, everything is intermediated
by the gateway repository. Packages consumed in this manner are stored in both the gateway repository and the downstream repository
that received the original request.

Gateway repositories are predefined, but they must be created in each project to be used.
The following list contains every gateway repository that can be created in CodeCatalyst and the package authority they are connected to.

- **npm-public-registry-gateway** provides npm packages from npmjs.com.
- **maven-central-gateway** provides Maven packages from the Maven Central repository.
- **google-android-gateway** provides Maven packages from Google Android.
- **commonsware-gateway** provides Maven packages from CommonsWare.
- **gradle-plugins-gateway** provides Maven packages from Gradle Plugins.
- **nuget-gallery-gateway** provides NuGet packages from the NuGet Gallery.
- **pypi-gateway** provides Python packages from the Python Package Index.
