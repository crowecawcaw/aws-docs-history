# Record resource types in AWS Config

You can specify that AWS Config automatically track your private resource types and record
changes to those resources as _configuration items_. This enables you
to view configuration history for these private resource types, in addition to write
AWS Config Rules rules to verify configuration best practices. AWS Config is required for the Hook
extension.

To have AWS Config automatically track your private resource types:

- Manage the resources through CloudFormation. This includes performing all resource
  create, updated, and delete operations through CloudFormation.

###### Note

If you use an IAM role to perform your stack operations, that IAM role
must have permission to call the following AWS Config actions:

    + [PutResourceConfig](../../../config/latest/APIReference/API_PutResourceConfig.md "../../../config/latest/APIReference/API_PutResourceConfig.md")
    + [DeleteResourceConfig](../../../config/latest/APIReference/API_DeleteResourceConfig.md "../../../config/latest/APIReference/API_DeleteResourceConfig.md")

- Configure AWS Config to record all resource types. For more information, see [Recording Configurations for Third-Party Resources using the AWS CLI](../../../config/latest/developerguide/customresources.md "../../../config/latest/developerguide/customresources.md")
  in the _AWS Config Developer Guide_.

###### Note

AWS Config doesn't support recording of private resources containing properties
defined as both required _and_ write-only.

By design, resource properties defined as write-only aren't returned in
the schema used to create AWS Config configuration item. Because of this,
including a property that's defined as both write-only and required will
cause the configuration item creation to fail, as a required property will
not be present. To view the schema that will be used to create the
configuration item, you can review the `schema` property of the
[DescribeType](../APIReference/API_DescribeType.md "../APIReference/API_DescribeType.md") action.
For more information about configuration items, see [Configuration
items](../../../config/latest/developerguide/config-concepts.md#config-items "../../../config/latest/developerguide/config-concepts.md#config-items") in the _AWS Config Developer Guide_.

## Preventing sensitive properties

being recorded in a configuration item

Your resource type may contain properties that you consider sensitive information,
such as passwords, secrets, or other sensitive data, that you don't want recorded as
part of the configuration item. To prevent a property from being recorded in the
configuration item, you can include that property in the
`writeOnlyproperties` list in your resource type schema. Resource
properties listed as `writeOnlyproperties` can be specified by the user,
but won't be returned by a `read` or `list` request.

For more information, see [writeOnlyProperties](../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-writeonlyproperties "../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-writeonlyproperties") in the _CloudFormation CLI
User Guide_.
