

# Creating X-Ray resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

AWS X-Ray is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your X-Ray resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## X-Ray and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for X-Ray and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

X-Ray supports creating [`AWS::XRay::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html), [`AWS::XRay::SamplingRule`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html), and [`AWS::XRay::ResourcePolicy`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html) resources in CloudFormation. For more information, including examples of JSON and YAML templates, see the [X-Ray resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_XRay.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)