Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Working with lifecycle management as a blueprint author

Lifecycle management allows you to keep a large number of projects synchronized from a single common source of
best-practices. This scales the propagation of fixes and the maintenance of any number of projects across their entire
software development lifecycle. Lifecycle management streamlines internal campaigns, security fixes, audits, runtime
upgrades, changes in best practices, and other maintenance practices because those standards are defined in one place
and automatically kept up to date centrally when new standards are published.

When a new version of your blueprint is published, all projects containing that blueprint are prompted to update to
the latest version. As a blueprint author, you can also see the version of a particular blueprint that each project contains
for compliance purposes. When there are conflicts in an existing source repository, lifecycle management creates pull requests.
For all other resources, such as Dev Environment, all lifecycle management updates strictly create new resources. Users are
free to merge or not merge those pull requests. When the pending pull requests are merged, the version of the blueprint,
including options, used in your project are then updated. To learn about working with lifecycle management as a blueprint user,
see [Using lifecycle management on existing projects](lifecycle-management-user.md#using-lm-existing-projects "lifecycle-management-user.md#using-lm-existing-projects") and
[Using lifecycle management on multiple blueprints in a project](lifecycle-management-user.md#using-lm-multiple-bp "lifecycle-management-user.md#using-lm-multiple-bp").

###### Topics

- [Testing lifecycle management for bundle outputs and merge conflicts](test-lm.md "test-lm.md")
- [Using merge strategies to generate bundles and specifying files](merge-strategies-lm.md "merge-strategies-lm.md")
- [Accessing context objects for project details](context-objects-lm.md "context-objects-lm.md")
