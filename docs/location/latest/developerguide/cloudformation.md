

# Create resources with AWS CloudFormation
<a name="cloudformation"></a>

Amazon Location Service is integrated with CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as Amazon Location resources), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Amazon Location resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## Related CloudFormation templates
<a name="cloudformation_templates"></a>

To provision and configure resources for Amazon Location and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use Infrastructure Composer to help you get started with CloudFormation templates. For more information, see [Infrastructure Composer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/infrastructure-composer-for-cloudformation.html) in the *CloudFormation User Guide*. 

Amazon Location supports creating the following resource types in CloudFormation: 
+ [AWS::Location::Tracker](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-tracker.html) 
+ [AWS::Location::TrackerConsumer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-trackerconsumer.html) 
+ [AWS::Location::GeofenceCollection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-geofencecollection.html) 

For more information, including examples of JSON and YAML templates for Amazon Location resources, see the [Amazon Location Service resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_Location.html) in the *CloudFormation Template Reference*. 

## Learn more about CloudFormation
<a name="cloudformation_learn"></a>

To learn more about CloudFormation, see the following resources: 
+ [CloudFormation](https://aws.amazon.com/cloudformation) 
+ [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) 
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html) 
+ [CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html) 