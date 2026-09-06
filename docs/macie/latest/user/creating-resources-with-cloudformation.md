

# Creating Macie resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Amazon Macie integrates with [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), which is a service that helps you model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as custom data identifiers), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Macie resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and AWS Regions. 

## Macie and AWS CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Amazon Macie and related services, you must understand CloudFormation templates. The templates describe the resources that you want to provision in your CloudFormation stacks. They are text files in JSON or YAML format. If you're unfamiliar with JSON or YAML, AWS Infrastructure Composer or CloudFormation Designer can help you get started. For more information, see [Working with CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*.

You can create CloudFormation templates for the following types of Macie resources:
+ Allow lists
+ Custom data identifiers
+ Filter rules and suppression rules for findings, also referred to as *findings filters*

For more information, including examples of JSON and YAML templates for these types of resources, see the [Amazon Macie resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_Macie.html) in the *AWS CloudFormation User Guide*.

## Additional learning resources for AWS CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about AWS CloudFormation, refer to the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)