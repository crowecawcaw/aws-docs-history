

# Using Amazon ECS with AWS CloudFormation
<a name="ecs-with-cloudformation"></a>

Amazon ECS is integrated with AWS CloudFormation, a service that you can use to model and set up AWS resources with templates that you define. CloudFormation uses **templates** that are either a `YAML` or `JSON` formatted text file. Templates are like blueprints for the AWS resource you want to create. When you create and submit a template, CloudFormation creates a **stack**. You manage the resources you defined in your template through the stack. When you want to create, update, or delete a resource, you create, update, or delete the stack that was created from that resource. When it comes to updating your stacks, you need to create a **change set** first. Change sets show you what is impacted by the change before you make it. This keeps you from deleting databases accidently by changing your database name, for example. For more information on templates, stacks, and change sets, see [How CloudFormation works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html#cfn-concepts-stacks) in the *AWS CloudFormation User Guide*.

By using CloudFormation, you can spend less time creating and managing your resources and infrastructure. You can create a template that describes all the AWS resources that you want, such as Amazon ECS clusters, task definitions, services. Then, CloudFormation takes care of provisioning and configuring those resources for you. 

CloudFormation also allows you to reuse your template to set up your Amazon ECS resources in a consistent and repeatable manner. You describe your resources one time and then provision the same resources again across multiple AWS accounts and AWS Regions.

CloudFormation templates can be used with both the AWS Management Console or the AWS Command Line Interface to create resources.

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)

**Topics**
+ [Creating Amazon ECS resources using the CloudFormation console](ecs-cloudformation-console.md)
+ [Creating Amazon ECS resources using AWS CLI commands for CloudFormation](ecs-cloudformation-cli.md)
+ [CloudFormation example templates for Amazon ECS](working-with-templates.md)