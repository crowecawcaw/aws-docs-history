

# Creating AWS Clean Rooms resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

AWS Clean Rooms is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources. As a result of this integration, you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you. Examples of resources include collaborations, configured tables, configured table associations, and memberships.

When you use CloudFormation, you can reuse your template to set up your AWS Clean Rooms resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and AWS Regions. 

## AWS Clean Rooms and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for AWS Clean Rooms and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

AWS Clean Rooms supports creating collaborations, configured tables, configured table associations, and memberships in CloudFormation. For more information, including examples of JSON and YAML templates for collaborations, configured tables, configured table associations, and memberships, see the [AWS Clean Rooms](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.html) and [AWS Clean Rooms ML](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.html) resource type references in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)