# Create resources with AWS CloudFormation

Amazon Location Service is integrated with CloudFormation, a service that helps you to
model and set up your AWS resources so that you can spend less time creating and managing
your resources and infrastructure. You create a template that describes all the AWS
resources that you want (such as Amazon Location resources), and CloudFormation
provisions and configures those resources for you.

When you use CloudFormation, you can reuse your template to set up your Amazon Location resources consistently and repeatedly. Describe your resources once, and then
provision the same resources over and over in multiple AWS accounts and Regions.

## Related CloudFormation templates

To provision and configure resources for Amazon Location and related services, you
must understand [CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These
templates describe the resources that you want to provision in your CloudFormation
stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer
to help you get started with CloudFormation templates. For more information, see
[What is CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _CloudFormation
User Guide_.

Amazon Location supports creating the following resource types in CloudFormation:

- [AWS::Location::Tracker](../../../AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.md")
- [AWS::Location::TrackerConsumer](../../../AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.md")
- [AWS::Location::GeofenceCollection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.md")

For more information, including examples of JSON and YAML templates for Amazon Location resources, see the [Amazon Location Service resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Location.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Location.md") in the _CloudFormation User Guide_.

## Learn more about CloudFormation

To learn more about CloudFormation, see the following resources:

- [CloudFormation](https://aws.amazon.com/cloudformation "https://aws.amazon.com/cloudformation")
- [CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [CloudFormation API Reference](../../../AWSCloudFormation/latest/APIReference/Welcome.md "../../../AWSCloudFormation/latest/APIReference/Welcome.md")
- [CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
