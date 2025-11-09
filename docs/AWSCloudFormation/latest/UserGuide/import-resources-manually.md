# Import AWS resources into a CloudFormation stack

manually

With resource import, you can import existing AWS resources into a new or existing
CloudFormation stack. During an import operation, you create a change set that imports your existing
resources into a stack or creates a new stack from your existing resources. You provide the
following during import.

- A template that describes the entire stack, including both the original stack resources and
  the resources you're importing. Each resource to import must have a [DeletionPolicy
  attribute](../TemplateReference/aws-attribute-deletionpolicy.md "../TemplateReference/aws-attribute-deletionpolicy.md").
- Identifiers for the resources you're importing that CloudFormation can use to map the logical
  IDs in the template with the existing resources.

###### Note

CloudFormation only supports one level of nesting using resource import. This means that you
can't import a stack into a child stack or import a stack that has children.

###### Topics

- [Resource
  identifiers](#resource-import-identifiers-unique-ids "#resource-import-identifiers-unique-ids")
- [Validation](#resource-import-validation "#resource-import-validation")
- [Status codes](#resource-import-status-codes "#resource-import-status-codes")
- [Considerations](#resource-import-considerations "#resource-import-considerations")
- [Additional
  resources](#resource-import-additional-resources "#resource-import-additional-resources")
- [Creating a stack from existing
  resources](resource-import-new-stack.md "resource-import-new-stack.md")
- [Importing existing resources into a
  stack](resource-import-existing-stack.md "resource-import-existing-stack.md")
- [Moving resources between stacks](refactor-stacks.md "refactor-stacks.md")
- [Nesting an existing
  stack](resource-import-nested-stacks.md "resource-import-nested-stacks.md")

## Resource identifiers

You provide two values to identify each resource you're importing.

- An identifier property. This is a resource property that can be used to identify each
  resource type. For example, an `AWS::S3::Bucket` resource can be identified using
  its `BucketName`.

The resource property that you use to identify the resource you're importing varies with
the resource type. You can find the resource property in the CloudFormation console. After you
create a template that includes the resource to import, you can initiate the import process,
where you'll find the identifier properties for the resources you're importing. For some
resource types, there might be multiple ways to identify them, and you can select which
property to use in the drop-down lists.

Alternatively, you can get the identifier properties for the resources you're importing by
calling the [get-template-summary](../../../cli/latest/reference/cloudformation/get-template-summary.md "../../../cli/latest/reference/cloudformation/get-template-summary.md") CLI command and specifying the S3 URL of the stack template as
the value for the `--template-url` option.

- An identifier value. This is the resource's actual property value. For example, the actual
  value for the `BucketName` property might be `MyS3Bucket`.

You can get the value of the identifier property from the service console for the
resource.

## Resource import validation

During an import operation, CloudFormation performs the following validations.

- The resource to import exists.
- The properties and configuration values for each resource to import adhere to the resource
  type schema, which defines its accepted properties, required properties, and supported property
  values.
- The required properties are specified in the template. Required properties for each
  resource type are described in the [AWS resource and property types reference](../TemplateReference/aws-template-resource-type-ref.md "../TemplateReference/aws-template-resource-type-ref.md").
- The resource to import doesn't belong to another stack in the same Region.

CloudFormation doesn't check that the template configuration matches the actual configuration of
resource properties.

###### Important

Verify that resources and their properties defined in the template match the intended
configuration of the resource import to avoid unexpected changes.

## Resource import status codes

This table describes the various status types used with the resource import feature.

| Import operation status       | Description                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| `IMPORT_IN_PROGRESS`          | The import operation is in progress.                                                  |
| `IMPORT_COMPLETE`             | The import operation completed for all resources in the stack.                        |
| `IMPORT_ROLLBACK_IN_PROGRESS` | The rollback import operation is rolling back the previous template<br>configuration. |
| `IMPORT_ROLLBACK_FAILED`      | The import rollback operation failed.                                                 |
| `IMPORT_ROLLBACK_COMPLETE`    | The import rolled back to the previous template configuration.                        |

## Considerations during an import

operation

- After the import is complete and before performing subsequent stack operations, we
  recommend running drift detection on imported resources. Drift detection ensures that the
  template configuration matches the actual configuration. For more information, see [Detect drift on an entire CloudFormation stack](detect-drift-stack.md "detect-drift-stack.md").
- Import operations don't allow new resource creations, resource deletions, or changes to
  property configurations.
- Each resource to import must have a `DeletionPolicy` attribute for the import
  operation to succeed. The `DeletionPolicy` can be set to any possible value. Only
  the resources you're importing need a `DeletionPolicy`. Resources that are already
  part of the stack don't need a `DeletionPolicy`.
- You can't import the same resource into multiple stacks.
- You can use the `cloudformation:ImportResourceTypes` IAM policy condition to
  control which resource types users can work with during an import operation. For more
  information, see [Policy condition keys for CloudFormation](control-access-with-iam.md#using-iam-conditions "control-access-with-iam.md#using-iam-conditions").
- The CloudFormation stack limits apply when importing resources. For more information on
  limits, see [Understand CloudFormation quotas](cloudformation-limits.md "cloudformation-limits.md").

## Additional resources

To resolve stack drift with a resource import, see [Resolve drift with an import
operation](resource-import-resolve-drift.md "resource-import-resolve-drift.md").
