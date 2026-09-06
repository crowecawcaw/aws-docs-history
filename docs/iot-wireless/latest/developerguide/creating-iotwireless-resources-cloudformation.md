

# Creating AWS IoT Wireless resources with AWS CloudFormation
<a name="creating-iotwireless-resources-cloudformation"></a>

AWS IoT Wireless is integrated with AWS CloudFormation, a service that helps you model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation takes care of provisioning and configuring those resources for you.

When you use CloudFormation, you can reuse your template to set up your AWS IoT Wireless resources consistently and repeatedly. Just describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions.

## AWS IoT Wireless and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for AWS IoT Wireless and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

AWS IoT Wireless supports creating your wireless resources in CloudFormation. For more information, including examples of JSON and YAML templates for your AWS IoT Wireless resources, see [AWS IoT Wireless resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTWireless.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)