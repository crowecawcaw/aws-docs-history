Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Allowing project access for machine resources

Machine resources are specific resources in CodeCatalystthat are granted permissions for projects or spaces in CodeCatalyst.

###### Note

The term machine resource does not refer to cloud infrastructure such as an EC2 instance, but it is instead meant to refer to a blueprint or workflow resource with permissions for a space or project.

An example of working with machine resources in projects includes enabling a blueprint resource to access a project on your behalf.

A machine resource represents your identity from your authorized resource when accessing
CodeCatalyst through SSO. Machine resources are used to grant permissions to resources in your
project, such as **blueprints** and **workflows**. You can view the machine resources in your project, and you can choose
to enable or disable machine resources for your project. For example, you might want to disable
a machine resource to manage access and then re-enable it later.

These operations are available for machine resources in cases where a machine resource needs
to be revoked or disabled. For example, if you suspect credentials might have been compromised,
you can disable the machine resource. Generally, these operations will not need to be
used.

You must have the **Space administrator** role or the
**Project administrator** role to view this page and to manage machine
resources at the project level.

Machine resources are also managed at the space level in CodeCatalyst. To learn more about teams in spaces/projects, see [Allowing space access for machine resources](managing-machine-resources.md "managing-machine-resources.md") .

###### Topics

- [Viewing project access for machine resources](projects-machine-resources-view.md "projects-machine-resources-view.md")
- [Disabling project access for machine resources](projects-machine-resources-disable.md "projects-machine-resources-disable.md")
- [Enabling project access for machine resources](projects-machine-resources-enable.md "projects-machine-resources-enable.md")
