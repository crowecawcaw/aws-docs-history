

# Managing stacks across accounts and Regions with StackSets
<a name="what-is-cfnstacksets"></a>

CloudFormation StackSets extends the capability of stacks by allowing you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation. Using an administrator account, you define and manage a CloudFormation template, and use the template as the basis for provisioning stacks into selected target accounts across specified AWS Regions.

![A StackSet is a collection of resources in a template, that's deployed across multiple accounts and regions.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/stack_set_conceptual_sv.png)


This section helps you get started using StackSets, and answers common questions about how to work with and troubleshoot StackSet creation, updates, and deletion.

**Topics**
+ [StackSets concepts](stacksets-concepts.md)
+ [Prerequisites for using CloudFormation StackSets](stacksets-prereqs.md)
+ [Get started with StackSets using a sample template](stacksets-getting-started.md)
+ [Create CloudFormation StackSets with self-managed permissions](stacksets-getting-started-create-self-managed.md)
+ [Create CloudFormation StackSets with service-managed permissions](stacksets-orgs-associate-stackset-with-org.md)
+ [Enable or disable automatic deployments for StackSets in AWS Organizations](stacksets-orgs-manage-auto-deployment.md)
+ [Update CloudFormation StackSets](stacksets-update.md)
+ [Add stacks to CloudFormation StackSets](stackinstances-create.md)
+ [Override parameter values on stacks within your CloudFormation StackSet](stackinstances-override.md)
+ [Delete stacks from CloudFormation StackSets](stackinstances-delete.md)
+ [Delete CloudFormation StackSets](stacksets-delete.md)
+ [Prevent failed StackSets deployments using target account gates](stacksets-account-gating.md)
+ [Choose the Concurrency Mode for CloudFormation StackSets](concurrency-mode.md)
+ [Performing drift detection on CloudFormation StackSets](stacksets-drift.md)
+ [Import stacks into CloudFormation StackSets](stacksets-import.md)
+ [Best practices for using CloudFormation StackSets](stacksets-bestpractices.md)
+ [CloudFormation StackSets sample templates](stacksets-sampletemplates.md)
+ [Troubleshooting CloudFormation StackSets](stacksets-troubleshooting.md)