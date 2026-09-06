

# Create AWS Control Tower resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

AWS Control Tower is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, such as `AWS::ControlTower::EnabledControl` for controls. CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your AWS Control Tower resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## AWS Control Tower and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for AWS Control Tower and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use AWS Infrastructure Composer to help you get started with CloudFormation templates. For more information, see [What is AWS Infrastructure Composer?](https://docs.aws.amazon.com/infrastructure-composer/latest/dg/what-is-composer.html) in the *AWS Infrastructure Composer User Guide*.

AWS Control Tower supports creating `AWS::ControlTower::EnabledControl` (control resources), `AWS::ControlTower::LandingZone` (landing zones), and `AWS::ControlTower::EnabledBaseline` (baselines) in CloudFormation. For more information, including examples of JSON and YAML templates for these resource types, see [AWS Control Tower](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ControlTower.html) in the *AWS CloudFormation User Guide*.

**Note**  
The limit for `EnableControl`and `DisableControl` updates in AWS Control Tower is 100 concurrent operations.

To view some AWS Control Tower examples for the CLI and the console, see [Enable controls with CloudFormation](https://docs.aws.amazon.com/controltower/latest/userguide/enable-controls.html).

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)