

# Using CloudFormation StackSets
<a name="using-stacksets"></a>

**Note**  
AutoTags are not currently supported with CloudFormation StackSets. 

You can use CloudFormation StackSets to launch AWS Service Catalog products across multiple AWS Regions and accounts. You can specify the order in which products deploy sequentially within AWS Regions. Across accounts, products are deployed in parallel. When launching, users can specify failure tolerance and the maximum number of accounts in which to deploy in parallel. For more information, see [Working with CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

## Stack sets vs. stack instances
<a name="stacksets-vs-stack-instances"></a>

A *stack set* lets you create stacks in AWS accounts across AWS Regions by using a single CloudFormation template.

A *stack instance* refers to a stack in a target account within an AWS Region and is associated with only one stack set.

For more information, see [StackSets Concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html).

## Stack set constraints
<a name="stackset-constraints"></a>

In AWS Service Catalog, you can use stack set constraints to configure product deployment options.

 AWS Service Catalog supports stack set constraints on products in two AWS GovCloud (US) Regions: AWS GovCloud (US-West) and AWS GovCloud (US-East).

For more information, see [AWS Service Catalog Stack Set Constraints.](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-stackset.html) 