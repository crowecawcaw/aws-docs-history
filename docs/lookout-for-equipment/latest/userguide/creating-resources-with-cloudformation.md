

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Creating Amazon Lookout for Equipment resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Amazon Lookout for Equipment is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your Lookout for Equipment resources and infrastructure. You create a template that describes all the AWS resources that you want (such as Amazon S3 buckets), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Lookout for Equipment resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## Lookout for Equipment and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Lookout for Equipment and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

Lookout for Equipment supports creating Amazon S3 buckets in CloudFormation. For more information, including examples of JSON and YAML templates for Amazon S3 buckets, see the [Lookout For Equipment resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutEquipment.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)