# Welcome


 AWS CloudFormation allows you to create and manage AWS infrastructure deployments predictably and
 repeatedly. You can use CloudFormation to leverage AWS products, such as Amazon Elastic Compute Cloud, Amazon Elastic Block Store,
 Amazon Simple Notification Service, Elastic Load Balancing, and Amazon EC2 Auto Scaling to build highly reliable, highly scalable, cost-effective
 applications without creating or configuring the underlying AWS infrastructure.

With CloudFormation, you declare all your resources and dependencies in a template file. The
 template defines a collection of resources as a single unit called a stack. CloudFormation creates
 and deletes all member resources of the stack together and manages all dependencies between the
 resources for you.

For more information about CloudFormation, see the [AWS CloudFormation product page](http://aws.amazon.com/cloudformation/ "http://aws.amazon.com/cloudformation/").

CloudFormation makes use of other AWS products. If you need additional technical information
 about a specific AWS product, you can find the product's technical documentation at [docs.aws.amazon.com](https://docs.aws.amazon.com/ "https://docs.aws.amazon.com/").




**Stack actions**


When you use CloudFormation, you manage related resources as a single unit called a
 stack. You create, update, and delete a collection of resources by creating, updating, and
 deleting stacks. All the resources in a stack are defined by the stack's template.



[CancelUpdateStack](API_CancelUpdateStack.md "API_CancelUpdateStack.md") | [ContinueUpdateRollback](API_ContinueUpdateRollback.md "API_ContinueUpdateRollback.md") | [CreateStack](API_CreateStack.md "API_CreateStack.md") | [DeleteStack](API_DeleteStack.md "API_DeleteStack.md") | [DescribeStacks](API_DescribeStacks.md "API_DescribeStacks.md") |
 [ListStacks](API_ListStacks.md "API_ListStacks.md") | [UpdateStack](API_UpdateStack.md "API_UpdateStack.md")



Stack events: [DescribeStackEvents](API_DescribeStackEvents.md "API_DescribeStackEvents.md")



Stack resources: [DescribeStackResource](API_DescribeStackResource.md "API_DescribeStackResource.md") | [DescribeStackResources](API_DescribeStackResources.md "API_DescribeStackResources.md") | [ListStackResources](API_ListStackResources.md "API_ListStackResources.md")



Stack drift: [DescribeStackDriftDetectionStatus](API_DescribeStackDriftDetectionStatus.md "API_DescribeStackDriftDetectionStatus.md") | [DescribeStackResourceDrifts](API_DescribeStackResourceDrifts.md "API_DescribeStackResourceDrifts.md") | [DetectStackDrift](API_DetectStackDrift.md "API_DetectStackDrift.md") | [DetectStackResourceDrift](API_DetectStackResourceDrift.md "API_DetectStackResourceDrift.md")



Stack operations: [ListExports](API_ListExports.md "API_ListExports.md") | [ListImports](API_ListImports.md "API_ListImports.md") | [UpdateTerminationProtection](API_UpdateTerminationProtection.md "API_UpdateTerminationProtection.md")



Stack policies: [GetStackPolicy](API_GetStackPolicy.md "API_GetStackPolicy.md") | [SetStackPolicy](API_SetStackPolicy.md "API_SetStackPolicy.md")



Templates: [EstimateTemplateCost](API_EstimateTemplateCost.md "API_EstimateTemplateCost.md") | [GetTemplate](API_GetTemplate.md "API_GetTemplate.md") | [GetTemplateSummary](API_GetTemplateSummary.md "API_GetTemplateSummary.md") | [ValidateTemplate](API_ValidateTemplate.md "API_ValidateTemplate.md")







**Change set actions**


If you need to make changes to the running resources in a stack, you update the
 stack. Before making changes to your resources, you can generate a change set, which is
 summary of your proposed changes. Change sets allow you to see how your changes might impact
 your running resources, especially for critical resources, before implementing them.



[CreateChangeSet](API_CreateChangeSet.md "API_CreateChangeSet.md") | [DeleteChangeSet](API_DeleteChangeSet.md "API_DeleteChangeSet.md") | [DescribeChangeSet](API_DescribeChangeSet.md "API_DescribeChangeSet.md") | [ExecuteChangeSet](API_ExecuteChangeSet.md "API_ExecuteChangeSet.md") | [ListChangeSets](API_ListChangeSets.md "API_ListChangeSets.md")







**StackSets actions**


CloudFormation StackSets lets you create a collection, or *stack
 set*, of stacks that can automatically and safely provision a common set of AWS
 resources across multiple AWS accounts and multiple AWS Regions from a single CloudFormation
 template. When you create a StackSet, CloudFormation provisions a stack in each of the specified
 accounts and AWS Regions by using the supplied CloudFormation template and parameters. Stack
 sets let you manage a common set of AWS resources in a selection of accounts and
 AWS Regions in a single operation.



[CreateStackSet](API_CreateStackSet.md "API_CreateStackSet.md") | [DeleteStackSet](API_DeleteStackSet.md "API_DeleteStackSet.md") | [DescribeStackSet](API_DescribeStackSet.md "API_DescribeStackSet.md") | [ListStackSets](API_ListStackSets.md "API_ListStackSets.md") | [UpdateStackSet](API_UpdateStackSet.md "API_UpdateStackSet.md")



Stack instances: [CreateStackInstances](API_CreateStackInstances.md "API_CreateStackInstances.md") | [DeleteStackInstances](API_DeleteStackInstances.md "API_DeleteStackInstances.md") | [DescribeStackInstance](API_DescribeStackInstance.md "API_DescribeStackInstance.md") | [ListStackInstances](API_ListStackInstances.md "API_ListStackInstances.md")



StackSet operations: [DescribeStackSetOperation](API_DescribeStackSetOperation.md "API_DescribeStackSetOperation.md") | [ListStackSetOperations](API_ListStackSetOperations.md "API_ListStackSetOperations.md") | [ListStackSetOperationResults](API_ListStackSetOperationResults.md "API_ListStackSetOperationResults.md") | [StopStackSetOperation](API_StopStackSetOperation.md "API_StopStackSetOperation.md")







**Extension management actions**


The AWS CloudFormation registry enables you to manage the extensions, both private and
 public, that are available for use in your account.



[ActivateType](API_ActivateType.md "API_ActivateType.md") | [DeactivateType](API_DeactivateType.md "API_DeactivateType.md") | [DescribeType](API_DescribeType.md "API_DescribeType.md") | [ListTypes](API_ListTypes.md "API_ListTypes.md")



Registration: [DescribeTypeRegistration](API_DescribeTypeRegistration.md "API_DescribeTypeRegistration.md") | [DeregisterType](API_DeregisterType.md "API_DeregisterType.md") | [ListTypeRegistrations](API_ListTypeRegistrations.md "API_ListTypeRegistrations.md") | [RegisterType](API_RegisterType.md "API_RegisterType.md")



Configuration: [BatchDescribeTypeConfigurations](API_BatchDescribeTypeConfigurations.md "API_BatchDescribeTypeConfigurations.md") | [SetTypeConfiguration](API_SetTypeConfiguration.md "API_SetTypeConfiguration.md")



Versioning: [ListTypeVersions](API_ListTypeVersions.md "API_ListTypeVersions.md") | [SetTypeDefaultVersion](API_SetTypeDefaultVersion.md "API_SetTypeDefaultVersion.md")







**Extension publication actions**


Use the CloudFormation operation to develop and publish your own public third-party
 extensions.


For more information, see [Publishing extensions to
 make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.



[PublishType](API_PublishType.md "API_PublishType.md") | [TestType](API_TestType.md "API_TestType.md")



Publishers: [DescribePublisher](API_DescribePublisher.md "API_DescribePublisher.md") | [RegisterPublisher](API_RegisterPublisher.md "API_RegisterPublisher.md")




This document was last published on October 14, 2025.
