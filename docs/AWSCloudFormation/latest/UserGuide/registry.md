# Managing extensions with the CloudFormation registry

The CloudFormation registry serves as a centralized hub for managing extensions that can be
integrated into the CloudFormation templates in your AWS account. Extensions include resource
types, modules, and Hooks from AWS and third-party publishers, and your own custom
extensions. The registry makes it easier to discover and provision extensions in your
CloudFormation templates in the same manner you use AWS-provided resources.

This section describes how to use the CloudFormation registry to activate third-party
extensions in your account, including:

- Activating public extensions
- Registering and activating private extensions

###### Topics

- [Related documentation](#registry-related-documentation "#registry-related-documentation")
- [CloudFormation registry concepts](registry-concepts.md "registry-concepts.md")
- [View the available and activated extensions in the
  CloudFormation registry](registry-view.md "registry-view.md")
- [Use third-party public extensions from the CloudFormation
  registry](registry-public.md "registry-public.md")
- [Use third-party private extensions that have been
  shared with you](registry-private.md "registry-private.md")
- [Edit configuration data for extensions in
  your account](registry-set-configuration.md "registry-set-configuration.md")
- [Record resource types in AWS Config](registry-config-record.md "registry-config-record.md")

## Related documentation

If you are a developer interested in creating your own extensions, see the following
documentation:

- [Developing modules
  using the CloudFormation CLI](../../../cloudformation-cli/latest/userguide/modules.md "../../../cloudformation-cli/latest/userguide/modules.md") in the _CloudFormation Command Line
  Interface User Guide_
- [Creating
  resource types using the CloudFormation CLI](../../../cloudformation-cli/latest/userguide/resource-types.md "../../../cloudformation-cli/latest/userguide/resource-types.md") in the _CloudFormation
  Command Line Interface User Guide_
- [Developing custom Hooks using the CloudFormation CLI](../../../cloudformation-cli/latest/hooks-userguide/hooks-develop.md "../../../cloudformation-cli/latest/hooks-userguide/hooks-develop.md") in the
  _CloudFormation Hooks User Guide_

Additionally, all provisionable AWS resource types available in the CloudFormation
registry can be used with the AWS Cloud Control API, with their attributes and properties defined
in a standard JSON schema. For more information, see the [Cloud Control API User
Guide](../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md "../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md"). When using Cloud Control API to perform CRUDL (Create, Read, Update, Delete,
List) operations on AWS resources, you can only do so on AWS resources within your
own AWS account.
