# CloudFormation registry concepts

This topic explains key concepts to help you understand and begin using the CloudFormation
registry.

## Extension types

The CloudFormation registry offers the following extension types:

Hooks

Hooks are validation checks that inspect your stacks or specific
resources before CloudFormation creates, updates, or deletes them. Hooks can
also be invoked during create change set operations. They provide a
mechanism for enforcing organizational standards and best practices by
validating resource configurations against specific requirements. If a
Hook detects any configurations that don't comply with its logic, it can
either issue a warning or fail the provisioning process to prevent
non-compliant resources from being deployed. For more information, see
the [CloudFormation Hooks User Guide](../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md").

For documentation on how to configure Hooks using the CloudFormation
console, see the following sections of the _CloudFormation Hooks User
Guide_:

- [AWS Control Tower proactive controls as Hooks](../../../cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks.md")
- [Guard Hooks](../../../cloudformation-cli/latest/hooks-userguide/guard-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/guard-hooks.md")
- [Lambda Hooks](../../../cloudformation-cli/latest/hooks-userguide/lambda-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/lambda-hooks.md")

Modules

Modules are reusable resource configurations that can be included
across multiple CloudFormation stack templates. They simplify the the
creation and maintenance of CloudFormation templates by encapsulating
complex or frequently used resource configurations into reusable
components. This promotes consistency and standardization across your
organization's infrastructure deployments.

Resource types

Resource types allow you to model and automate third-party resources
or custom resources that aren't natively supported by CloudFormation. By
developing resource types, you can extend CloudFormation's capabilities to
provision and manage resources from various third-party services.

## Public extensions

_Public extensions_ are CloudFormation extensions that are publicly
published in the registry for use by all AWS accounts. These include:

- AWS extensions – Extensions
  published by AWS are always public, and activated by default, so you don't
  have to take any action before using them in your account. AWS controls
  the versioning of these extensions, so you are always using the latest
  available version.
- Third-party extensions – These
  extensions are made available for general use by publishers other than
  AWS. To use a third-party public extension, you must first activate it in
  your account and Region.

## Activated extensions

The CloudFormation registry in your specific AWS account includes three types of
activated extensions:

- AWS extensions – All AWS public
  extensions are automatically activated.
- Activated third-party – These are
  local copies of third-party public extensions that you have explicitly
  activated for your account and Region. When you activate a third-party
  public extension, CloudFormation creates a local copy in your account's
  registry. For more information, see [Use third-party public extensions from the CloudFormation
  registry](registry-public.md "registry-public.md").
- Privately registered – These are
  private extensions that aren't listed in the public CloudFormation registry.
  These may be extensions you've created yourself or ones shared with you by
  your organization or other third parties. To use such a private extension in
  your account, you must first register it. Registering the extension uploads
  a copy to the CloudFormation registry in your account and activates it. For more
  information, see [Use third-party private extensions that have been
  shared with you](registry-private.md "registry-private.md").

Using privately registered extensions and activated public extensions from
third-party publishers in your account is like using them in a sandbox environment.
Extensions are managed with version control, so their provisioning behavior is tied
to a specific version. As a result, these extensions function in the same way as
public extensions, adhering to the same version-specific rules.

###### Note

Privately registered extensions and activated third-party public extensions
may implement event handlers that run during create, read, update, list, and
delete operations. Using these extensions in your CloudFormation stacks may incur
charges to your account, in addition to any charges for the resources created.
For more information, see [CloudFormation pricing](https://aws.amazon.com/cloudformation/pricing/ "https://aws.amazon.com/cloudformation/pricing/").
