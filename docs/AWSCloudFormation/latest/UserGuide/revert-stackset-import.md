# Revert stack imports into AWS CloudFormation StackSets

If you have unwanted changes in your stack instance, you can revert the stack instance
 import.

When you revert a stack instance import, CloudFormation deletes the stack instance from the
 StackSet but retains the stack's resources.

To revert a stack import operation, complete the following procedure.

1. Specify a `DeletionPolicy` attribute of `Retain` for each resource
 that you want to keep after the stack instance is deleted. For more information, see [Reverting an import operation](resource-import-revert.md "resource-import-revert.md").
2. Delete stack instances from your StackSet. For more information, see [Delete stacks from AWS CloudFormation StackSets](stackinstances-delete.md "stackinstances-delete.md") .
3. Delete your StackSet. For more information, see [Delete AWS CloudFormation StackSets](stacksets-delete.md "stacksets-delete.md").
