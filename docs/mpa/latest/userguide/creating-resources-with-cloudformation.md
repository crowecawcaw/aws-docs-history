

# Creating Multi-party approval resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Multi-party approval is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as `AWS::MPA::ApprovalTeam` and `AWS::MPA::IdentitySource`), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Multi-party approval resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

**Team activation requirements for CloudFormation deployments**

If you create an approval team using AWS CloudFormation, the team will initially be created in a *pending activation* state. For more information see, [Team health](team-health.md). To activate the team, every invited approver must accept the team invitation within 24 hours.

If at least one approver declines the team invitation or the 24-hour time window to respond expires, the team activation fails. This failure triggers a rollback of the CloudFormation template, which deletes the team.

## Multi-party approval and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Multi-party approval and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

Multi-party approval supports creating `AWS::MPA::ApprovalTeam` and `AWS::MPA::IdentitySource` in CloudFormation. For more information, including examples of JSON and YAML templates for `AWS::MPA::ApprovalTeam` and `AWS::MPA::IdentitySource`, see the [MPA](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MPA.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)