

# Update CloudFormation stacks using change sets
<a name="using-cfn-updating-stacks-changesets"></a>

When you need to update a stack, understanding how your changes will affect running resources before you implement them can help you update stacks with confidence. Change sets allow you to preview how proposed changes to a stack might impact your running resources, including the impact on resource properties and attributes. Whether your changes will delete or replace any critical resources, CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set. You can create and manage change sets using the CloudFormation console, AWS CLI, or CloudFormation API.

**Topics**
+ [Create a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-create.md)
+ [View a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md)
+ [Using drift-aware change sets](drift-aware-change-sets.md)
+ [Execute a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-execute.md)
+ [Delete a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-delete.md)
+ [Example change sets for CloudFormation stacks](using-cfn-updating-stacks-changesets-samples.md)
+ [Change sets for nested stacks](change-sets-for-nested-stacks.md)

**Important**  
Change sets don't guarantee that CloudFormation will successfully update a stack. However, pre-deployment validation checks for common failure causes during change set creation, including property syntax errors, resource name conflicts, service quota limits, and other constraints. Failures that occur because of runtime conditions (such as custom resource logic or service-specific constraints) might still occur during execution.

**Note**  
You can use express mode with change sets to complete stack operations faster. Specify the `--deployment-config '{"mode": "EXPRESS"}'` parameter when creating a change set. When the change set is executed, CloudFormation applies express mode, completing resource operations as soon as configuration is applied. For more information, see [Express mode](cloudformation-express-mode.md).

**Change set overview**  
The following diagram summarizes how you use change sets to update a stack:

![Diagram showing four steps to update a stack using CloudFormation change sets.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/update-stack-changesets-diagram.png)


1. Create a change set by submitting changes for the stack that you want to update. You can submit a modified stack template or modified input parameter values. CloudFormation compares your stack with the changes that you submitted to generate the change set; it doesn't make changes to your stack at this point.

1. View the change set to see which stack settings and resources will change. For example, you can see which resources CloudFormation will add, modify, or delete. Additionally, you can see a before-and-after comparison of the resource properties and attributes, such as tags, that CloudFormation will modify.

1. Optional: If you want to consider other changes before you decide which changes to make, create additional change sets. Creating multiple change sets helps you understand and evaluate how different changes will affect your resources and properties. You can create as many change sets as you need.

1. Execute the change set that contains the changes that you want to apply to your stack. CloudFormation updates your stack with those changes.
**Note**  
After you execute a change, CloudFormation removes all change sets that are associated with the stack because they aren't applicable to the updated stack.

You can also delete change sets to prevent executing a change set that shouldn't be applied.