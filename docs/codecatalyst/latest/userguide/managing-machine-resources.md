Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Allowing space access for machine resources

Machine resources are specific resources in CodeCatalyst that are granted permissions for projects or spaces in CodeCatalyst.

###### Note

The term machine resource does not refer to cloud infrastructure such as an Amazon EC2 instance, but it is instead meant to refer to a blueprint or workflow resource with permissions for a space or project.

A machine resource represents your identity from your authorized resource when accessing
CodeCatalyst through SSO. Machine resources are used to grant permissions to resources in the
space, such as **blueprints** and **workflows**. You can view the machine resources in your space, and you can
choose to enable or disable machine resources for your space. For example, you might want
to disable a machine resource to manage access and then re-enable it later.

These operations are available for machine resources in cases where a machine resource needs
to be revoked or disabled. For example, if you suspect credentials might have been compromised,
you can disable the machine resource. Generally, these operations will not need to be
used.

You must have the **Space administrator** role to view this page and to manage
machine resources at the space level.

Machine resources are also managed at the project level in CodeCatalyst. To learn more about teams in projects, see Allowing space access for machine resources .

###### Topics

- [Viewing space access for machine resources](managing-machine-resources-view.md "managing-machine-resources-view.md")
- [Disabling space access for machine resources](managing-machine-resources-disable.md "managing-machine-resources-disable.md")
- [Enabling space access for machine resources](managing-machine-resources-enable.md "managing-machine-resources-enable.md")
