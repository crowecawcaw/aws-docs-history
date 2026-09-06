

# Creating Security Hub CSPM resources with CloudFormation
<a name="creating-resources-with-cloudformation"></a>

AWS Security Hub CSPM integrates with AWS CloudFormation, which is a service that helps you model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as automation rules), and CloudFormation provisions and configures those resources for you.

When you use CloudFormation, you can reuse your template to set up your Security Hub CSPM resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## Security Hub CSPM and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Security Hub CSPM and related services, you must understand how [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) work. Templates are text files in JSON or YAML format. These templates describe the resources that you want to provision in your CloudFormation stacks.

If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

You can create CloudFormation templates for the following types of Security Hub CSPM resources:
+ Enabling Security Hub CSPM
+ Designating the delegated Security Hub CSPM administrator for an organization
+ Specify the way your organization is configured in Security Hub CSPM
+ Enabling a security standard
+ Enabling cross-Region aggregation
+ Creating a central configuration policy and associating it with accounts, organizational unit (OUs), or the root
+ Creating a custom insight
+ Creating an automation rule
+ Customizing control parameters
+ Subscribing to a third-party product integration

For more information, including examples of JSON and YAML templates for resources, see the [AWS Security Hub CSPM resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)