

# Create Amazon Keyspaces resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Amazon Keyspaces is integrated with AWS CloudFormation, a service that helps you model and set up your AWS keyspaces and tables so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes the keyspaces and tables that you want, and CloudFormation takes care of provisioning and configuring those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Amazon Keyspaces resources consistently and repeatedly. Just describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## Amazon Keyspaces and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Amazon Keyspaces, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

Amazon Keyspaces supports creating keyspaces and tables in CloudFormation. For the tables you create using CloudFormation templates, you can specify the schema, read/write mode, provisioned throughput settings, and other supported features. For more information, including examples of JSON and YAML templates for keyspaces and tables, see [Amazon Keyspaces (for Apache Cassandra) resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cassandra.html) in the *AWS CloudFormation Template Reference*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation command line interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)