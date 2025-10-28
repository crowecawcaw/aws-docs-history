AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Tags

A tag is a label or attribute that you or AWS attaches to an AWS resource. Each tag
consists of a _key_ and a paired _value_. You can use tags
to control access to your AWS Cloud9 resources, as described in [Control Access Using AWS Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")_. Tags can also help you manage billing information, as
described in [User-Defined Cost Allocation
Tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md").

When you [create an AWS Cloud9 EC2 development environment](create-environment-main.md "create-environment-main.md"), AWS Cloud9
includes certain system tags that it needs to manage the environment. System tags start with
"**aws:**". During that creation process, you can also add your
own resource tags.

After the environment is created, you can view the tags that are attached to the environment, add
new resource tags to the environment, or modify or remove the tags that you added earlier. You
can attach up to 50 user-defined tags to an AWS Cloud9 environment.

View or update tags using one or more of the following methods.

- In the [AWS Cloud9 console](https://console.aws.amazon.com/cloud9/ "https://console.aws.amazon.com/cloud9/"), select the
  environment you're interested in, and then choose **View Details**.

![View the details of an environment.](images/view-details.png)

- Use the following AWS Cloud9 CLI commands: [`list-tags-for-resource`](../../../cli/latest/reference/cloud9/list-tags-for-resource.md "../../../cli/latest/reference/cloud9/list-tags-for-resource.md"), [`tag-resource`](../../../cli/latest/reference/cloud9/tag-resource.md "../../../cli/latest/reference/cloud9/tag-resource.md"), and [`untag-resource`](../../../cli/latest/reference/cloud9/untag-resource.md "../../../cli/latest/reference/cloud9/untag-resource.md").
- Use the following AWS Cloud9 API actions: [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md"), [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md"), and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md").

###### Warning

Tags that you create or update for AWS Cloud9 by using the preceding methods are not
automatically propagated to underlying resources. For information about how to do this, see
the next section, [Propagating tag updates to underlying resources](#tags-propagate "#tags-propagate").

## Propagating tag updates to underlying resources

When you use AWS Cloud9 CLI commands or API actions to add, modify, or remove the tags that are
attached to an AWS Cloud9 environment, those changes aren't automatically propagated to underlying
resources such as the AWS CloudFormation stack, the Amazon EC2 instance, and Amazon EC2 security groups. You must
manually propagate those changes.

To make it easier to use the following procedures, you can obtain the environment ID for
the environment you're interested in. If you want to do this, follow these steps:

1. In the [AWS Cloud9 console](https://console.aws.amazon.com/cloud9/ "https://console.aws.amazon.com/cloud9/"), select the
   environment that you're interested in, and then choose **View
   Details**.
2. Look for the **Environment ARN** property and record the environment
   ID, which is the part of the environment ARN after "**environment:**".

You need to propagate tag updates to one or more of the following locations, depending on
what you'll use the tags for.

### Propagating tag updates to the AWS CloudFormation stack

###### Note

When you update tags to the AWS CloudFormation stack, those updates are automatically
propagated to the Amazon EC2 instance and Amazon EC2 security groups that are associated with the
stack.

1. Navigate to the [AWS CloudFormation
   console.](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation")
2. Find and choose the stack that corresponds to the AWS Cloud9 environment that you're
   interested in. If you recorded the environment ID, you can use it to filter for the
   environment.
3. On the **Stack info** tab, in the **Tags**
   section, review the list of tags.
4. If you need to update the tags, choose **Update** near the top of
   the page, and follow the instructions. For more information, see [Updating Stacks
   Directly](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md") in the _[AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md")_.

You can also update tags using the [`describe-stacks`](../../../cli/latest/reference/cloudformation/describe-stacks.md "../../../cli/latest/reference/cloudformation/describe-stacks.md") and [`update-stack`](../../../cli/latest/reference/cloudformation/update-stack.md "../../../cli/latest/reference/cloudformation/update-stack.md") CLI
commands.

### Propagating tag updates to the Amazon EC2 instance

1. Navigate to the [Amazon EC2
   Instances](https://console.aws.amazon.com/ec2/home#Instances "https://console.aws.amazon.com/ec2/home#Instances") console.
2. Find and select the Amazon EC2 instance that corresponds to the AWS Cloud9 environment you're
   interested in. If you recorded the environment ID earlier, you can use it to filter for
   the environment.
3. On the **Tags** tab, view and update tags as necessary.

You can also update tags using the [describe-tags](../../../cli/latest/reference/ec2/describe-tags.md "../../../cli/latest/reference/ec2/describe-tags.md"), [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md"), and [delete-tags](../../../cli/latest/reference/ec2/delete-tags.md "../../../cli/latest/reference/ec2/delete-tags.md")
CLI commands.

### Propagating tag updates to Amazon EC2 security groups

1. Navigate to the [Amazon EC2
   Security Groups](https://console.aws.amazon.com/ec2/home#SecurityGroups "https://console.aws.amazon.com/ec2/home#SecurityGroups") console.
2. Find and select the security group that corresponds to the AWS Cloud9 environment that
   you're interested in. If you recorded the environment ID earlier, you can use it to
   filter for the environment.
3. Open the **Tags** tab to view and update tags as necessary.

You can also update tags using the [describe-tags](../../../cli/latest/reference/ec2/describe-tags.md "../../../cli/latest/reference/ec2/describe-tags.md"), [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md"), and [delete-tags](../../../cli/latest/reference/ec2/delete-tags.md "../../../cli/latest/reference/ec2/delete-tags.md")
CLI commands.
