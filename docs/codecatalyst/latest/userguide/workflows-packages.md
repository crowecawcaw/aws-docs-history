Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Connecting package repositories to workflows

A _package_ is a bundle that includes both software and the metadata that is
required to install the software and resolve any dependencies. CodeCatalyst supports the npm package format.

A package consists of:

- A name (for example, `webpack` is the name of a
  popular npm package)
- An optional [namespace](packages-concepts.md#packages-concepts-package-namespaces "packages-concepts.md#packages-concepts-package-namespaces")
  (for example, `@types` in `@types/node`)
- A set of [versions](packages-concepts.md#packages-concepts-package-versions "packages-concepts.md#packages-concepts-package-versions")
  (for example, `1.0.0`, `1.0.1`, `1.0.2`)
- Package-level metadata (for example, npm dist tags)
  In CodeCatalyst, you can publish packages to and consume packages from CodeCatalyst package
  repositories in your workflows. You can configure a build or test action with a CodeCatalyst
  package repository to automatically configure an action's npm client to push and pull
  packages from the specified repository.

For more information about packages, see [Publish and share software packages in CodeCatalyst](packages.md "packages.md").

###### Note

Currently, build and test actions support CodeCatalyst package repositories.

###### Topics

- [Tutorial: Pull from a package repository](packages-tutorial.md "packages-tutorial.md")
- [Specifying CodeCatalyst package
  repositories in workflows](workflows-package-specify-action.md "workflows-package-specify-action.md")
- [Using authorization tokens in workflow
  actions](workflows-package-export-token.md "workflows-package-export-token.md")
- [Examples: Package repositories in
  workflows](workflows-working-packages-ex.md "workflows-working-packages-ex.md")
