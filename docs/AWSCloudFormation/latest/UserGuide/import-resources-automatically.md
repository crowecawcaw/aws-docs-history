# Import AWS resources into a CloudFormation stack

automatically

You can now import _named resources_ automatically when creating or
updating CloudFormation stacks. A _named resource_ is one with a custom name. For
more information, see [Name type](../TemplateReference/aws-properties-name.md "../TemplateReference/aws-properties-name.md") in the
_CloudFormation Template Reference_.

When you initiate auto-import, CloudFormation checks for existing resources that match your
template and imports them during deployment. For nested stacks, create the change set from the
root stack.

After the import is complete and before performing subsequent stack operations, we
recommend running drift detection on imported resources. Drift detection ensures that the
template configuration matches the actual configuration. For more information, see [Detect drift on an entire CloudFormation stack](detect-drift-stack.md "detect-drift-stack.md").

To import a resource, they need to meet the following requirements:

- The resource must have a static custom name defined in your template. Dynamic names (using !Ref or other functions) are
  not currently supported.
- The resource must have a `DeletionPolicy` of `Retain` or
  `RetainExceptOnCreate`.
- The resource must not already belong to another CloudFormation stack.
- The resource type must support CloudFormation import operations. For more information, see
  [Resource type
  support](resource-import-supported-resources.md "resource-import-supported-resources.md").
- The primary ID for the resource type must be in the template. Primary IDs with read only properties aren't supported. To find out what the
  primary ID is for a type, look for the `primaryIdentifier` property in the resource schema. For more information on the property, see [primaryIdentifier](../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-primaryidentifier "../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-primaryidentifier").

###### Example auto-import

The following example uses a change set, `CreateChangeSet` to create a stack called `my-stack` based on a template file, `template.yaml`, and imports matching resources automatically.

```
aws cloudformation create-change-set \
  --stack-name `my-stack` \
  --change-set-name `CreateChangeSet` \
  --change-set-type CREATE \
  --template-body `file://template.yaml` \
  --import-existing-resources
```

## Troubleshooting

If auto-import fails, do the following to troubleshoot:

- Verify the resource name in your template matches the name of the resource exactly
- Verify that the resource isn't already managed by another stack
- Make sure the resource type supports import operations
- Verify your template includes all the required properties for the resource type
