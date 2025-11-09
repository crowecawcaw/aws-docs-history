Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Standardizing projects with custom blueprints in CodeCatalyst

You can standardize the development and best practices for your CodeCatalyst space's projects with
custom blueprints. Custom blueprints can be used to define various aspects of a CodeCatalyst project, such
as workflow definitions and application code. After a custom blueprint is used to create a new
project or applied to existing projects, any changes to the blueprint are available to those projects
as pull request updates. As a blueprint author, you can view details about which projects are using
your blueprints throughout your space, so you can see how standards are being applied across
projects. Lifecycle mangement of a blueprint allows you to centrally manage the software development
lifecycle of every project, giving you ability to make sure the projects in your space continue to
follow best practices with the latest changes or fixes. For more information, see
[Working with lifecycle management as a blueprint author](lifecycle-management-dev.md "lifecycle-management-dev.md").

Custom blueprints provide the ability to update blueprint versions against the prior project
through resynthesis. Resynthesis is the process of rerunning blueprint synthesis with updated
versions or the ability to incorporate fixes and changes into existing projects. For more information,
see [Custom blueprints concepts](custom-bp-concepts.md "custom-bp-concepts.md").

You may already have standardization and best practices in place. Instead of creating and developing
a custom blueprint from scratch, you can choose to convert an existing source repository with source code
into a custom blueprint. For more information, see [Converting source repositories to custom blueprints](convert-bp.md "convert-bp.md").

To view the blueprints SDK and sample blueprints, see the
[open-source GitHub repository](https://github.com/aws/codecatalyst-blueprints "https://github.com/aws/codecatalyst-blueprints").

###### Topics

- [Custom blueprints concepts](custom-bp-concepts.md "custom-bp-concepts.md")
- [Getting started with custom blueprints](getting-started-bp.md "getting-started-bp.md")
- [Tutorial: Creating and updating a React application](blueprint-getting-started-tutorial.md "blueprint-getting-started-tutorial.md")
- [Converting source repositories to custom blueprints](convert-bp.md "convert-bp.md")
- [Working with lifecycle management as a blueprint author](lifecycle-management-dev.md "lifecycle-management-dev.md")
- [Developing a custom blueprint to meet project requirements](develop-bp.md "develop-bp.md")
- [Publishing a custom blueprint to a space](publish-bp.md "publish-bp.md")
- [Setting publishing permissions for a custom blueprint](manage-permissions-bp.md "manage-permissions-bp.md")
- [Adding a custom blueprint to a space blueprints catalog](add-bp.md "add-bp.md")
- [Changing catalog versions for a custom blueprint](mange-version-bp.md "mange-version-bp.md")
- [Viewing details, versions, and projects of a custom blueprint](view-bp.md "view-bp.md")
- [Removing a custom blueprint from a space blueprints catalog](remove-bp.md "remove-bp.md")
- [Deleting a published custom blueprint or version](delete-bp.md "delete-bp.md")
- [Handling dependencies, mismatches, and tooling](dependencies-tooling-bp.md "dependencies-tooling-bp.md")
- [Contribute](contribute-bp.md "contribute-bp.md")
