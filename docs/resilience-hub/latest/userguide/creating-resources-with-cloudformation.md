

# AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

AWS Resilience Hub is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as AWS::ResilienceHub:::ResiliencyPolicy and AWS::ResilienceHub:::App), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your AWS Resilience Hub resources consistently and repeatedly. Describe your resources one time, and then provision the same resources repeatedly in multiple AWS accounts and Regions. 

## AWS Resilience Hub and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for AWS Resilience Hub and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

AWS Resilience Hub supports creating AWS::ResilienceHub:::ResiliencyPolicy and AWS::ResilienceHub:::App in CloudFormation. For more information, including examples of JSON and YAML templates for AWS::ResilienceHub:::ResiliencyPolicy and AWS::ResilienceHub:::App, see the [AWS Resilience Hub resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResilienceHub.html) in the *AWS CloudFormation User Guide*.

You can use CloudFormation stacks to define AWS Resilience Hub applications. A stack lets you manage related resources as a single unit. A stack can contain all the resources that you need to run a web application, such as a web server or networking rules. 

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

For more information about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)