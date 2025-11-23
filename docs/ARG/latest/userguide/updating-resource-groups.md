# Updating groups in AWS Resource Groups

To update a tag-based resource group in Resource Groups, you can edit the query and tags that are
the basis of your group. You can add and remove resources from your group only by applying
changes to the query or tags. You cannot select specific resources to add to or remove from
your group. The best way to add or remove a specific resource from a group is to edit the
resource's tags. Then verify that your resource group tag query either includes or omits the
tag, depending on whether you want the resource in your group.

To update an CloudFormation stack-based resource group, you can choose a different stack. You can
also add or remove resource types from the stack that you want to be part of the group. To
change the resources that are available in the stack, update the CloudFormation template used to
create the stack, and then update the stack in CloudFormation. For more information about how to
update an CloudFormation stack, see [CloudFormation stacks updates](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.md") in the
_CloudFormation User Guide._

In the AWS CLI, you update groups in two commands.

- `update-group`, which you run to update a group's description.
- `update-group-query`, which you run to update the resource query and
  tags that determine the group's member resources.
  In the console, you cannot change an CloudFormation stack-based group to a tag-based query group,
  or vice versa. However, you can do this by using the Resource Groups API, including in the
  AWS CLI.
