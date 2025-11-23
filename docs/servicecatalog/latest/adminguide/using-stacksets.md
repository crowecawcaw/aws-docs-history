# Using CloudFormation StackSets

###### Note

AutoTags are not currently supported with CloudFormation StackSets.

You can use CloudFormation StackSets to launch AWS Service Catalog products across multiple AWS Regions and accounts.
You can specify the order in which products deploy sequentially within AWS Regions.
Across accounts, products are deployed in parallel. When launching, users can specify failure tolerance and the maximum number of accounts in which to deploy in parallel.
For more information, see [Working with CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md").

## Stack sets vs. stack instances

A _stack set_ lets you create stacks in AWS accounts across AWS
Regions by using a single CloudFormation template.

A _stack instance_ refers to a stack in a target account within an
AWS Region and is associated with only one stack set.

For more information, see [StackSets
Concepts](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md").

## Stack set constraints

In AWS Service Catalog, you can use stack set constraints to configure product deployment options.

AWS Service Catalog supports stack set constraints on products in two AWS GovCloud (US) Regions: AWS GovCloud (US-West) and AWS GovCloud (US-East).

For more information, see [AWS Service Catalog Stack Set Constraints.](constraints-stackset.md "constraints-stackset.md")
