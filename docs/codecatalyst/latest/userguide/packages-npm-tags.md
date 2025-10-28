Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# npm tag handling

npm registries support _tags_, which are string aliases for package
versions. You can use tags to provide an alias instead of using version numbers. For
example, you have a project with multiple streams of development and you use a different
tag for each stream (for example, `stable`, `beta`, `dev`,
`canary`). For more information, see [dist-tag](https://docs.npmjs.com/cli/dist-tag "https://docs.npmjs.com/cli/dist-tag") on _npm
Docs_.

By default, npm uses the `latest` tag to identify the current version of a
package. `npm install `pkg`` (without
 `@`version`` or
`@`tag`` specifier) installs the latest tag.
Typically, projects only use the latest tag for stable release versions. Other tags are
used for unstable or prerelease versions.

## Editing tags with the npm

client

The three `npm dist-tag` commands (`add`, `rm`,
and `ls`) function the same way in CodeCatalyst package repositories as they
function in the [default npm
registry](https://registry.npmjs.com/ "https://registry.npmjs.com/").

## npm tags and upstream repositories

When `npm` requests the tags for a package and versions of that package are
also present in an upstream repository, CodeCatalyst merges the tags before returning them to the
client. For example, a repository named `R` has an upstream repository named `U`.
The following table shows the tags for a package named `web-helper` that's present in both
repositories.

| Repository | Package name | Package tags                       |
| ---------- | ------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R          | `web-helper` | _latest_ (alias for version 1.0.0) |
| U          | `web-helper` | _alpha_ (alias for version 1.0.1)  | In this case, when the npm client fetches the tags for the `web-helper` package from repository `R`, it receives both the _latest_ and _alpha_ tags. The versions the tags point to won't change. When the same tag is present on the same package in both the upstream and local repository, CodeCatalyst uses the tag that was _last updated_. For example, suppose that the tags on _webhelper_ have been modified to look like the following. |
| Repository | Package name | Package tags                       | Last updated                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---        | ---          | ---                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R          | `web-helper` | _latest_ (alias for version 1.0.0) | January 1, 2023                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| U          | `web-helper` | _latest_ (alias for version 1.0.1) | June 1, 2023                                                                                                                                                                                                                                                                                                                                                                                                                                      | In this case, when the npm client fetches the tags for package _web-helper_ from repository `R`, the _latest_ tag will alias the version _1.0.1_ because it was updated last. This makes it easy to consume new package versions in an upstream repository that are not yet present in a local repository by running `npm update`. |
