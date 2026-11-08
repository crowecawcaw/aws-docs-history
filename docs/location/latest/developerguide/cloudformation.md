

# Create resources with AWS CloudFormation
<a name="cloudformation"></a>

Amazon Location Service is integrated with CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as Amazon Location resources), and CloudFormation provisions and configures those resources for you. 

When you use CloudFormation, you can reuse your template to set up your Amazon Location resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

## Related CloudFormation templates
<a name="cloudformation_templates"></a>

To provision and configure resources for Amazon Location and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use Infrastructure Composer to help you get started with CloudFormation templates. For more information, see [Infrastructure Composer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/infrastructure-composer-for-cloudformation.html) in the *CloudFormation User Guide*. 

Amazon Location supports creating the following resource types in CloudFormation: 
+ [AWS::Location::APIKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-apikey.html) 
+ [AWS::Location::GeofenceCollection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-geofencecollection.html) 
+ [AWS::Location::Map](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-map.html) 
+ [AWS::Location::PlaceIndex](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-placeindex.html) 
+ [AWS::Location::RouteCalculator](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-routecalculator.html) 
+ [AWS::Location::Tracker](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-tracker.html) 
+ [AWS::Location::TrackerConsumer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-trackerconsumer.html) 

For more information, including examples of JSON and YAML templates for Amazon Location resources, see the [Amazon Location Service resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_Location.html) in the *CloudFormation Template Reference*. 

## Required permissions
<a name="cloudformation_required-permissions"></a>

CloudFormation uses an IAM identity to create and update your Amazon Location resources. This identity is one of the following:
+ The service role you specify for the stack.
+ The CloudFormation execution role, if you deploy with the AWS CDK.
+ Your own IAM identity, if you don't specify a service role.

Starting February 26, 2027, this identity needs permission to use the `geo:TagResource` action to create Amazon Location resources that support tags, and to replace them during a stack update. Of the resource types listed above, only `AWS::Location::TrackerConsumer` doesn't support tags, and it isn't affected.

The permission is required even if your template doesn't specify tags. CloudFormation adds the `aws:cloudformation:stack-name`, `aws:cloudformation:stack-id`, and `aws:cloudformation:logical-id` tags to each resource it creates. For more information about the tags that CloudFormation adds, see the [*CloudFormation Template Reference*](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html). To learn how to manage the required permissions, see [Grant permission to tag resources](manage-resources.md#manage-resources_grant-permission).

### Step 1: Add the permission
<a name="cloudformation_add-permission"></a>

Add the following statement to the policy of the identity that CloudFormation uses:

```
{
    "Effect": "Allow",
    "Action": "geo:TagResource",
    "Resource": "arn:aws:geo:{{region}}:{{account-id}}:*"
}
```

You don't need to add the statement if the identity already allows `geo:TagResource`, for example through `geo:*` or the `AdministratorAccess` managed policy.

If you deploy with the AWS CDK, the CloudFormation execution role uses the `AdministratorAccess` policy by default, which already allows this action. You need to add the statement only if you use managed policies. For more information, see [Customize AWS CDK bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-customizing.html) in the *AWS CDK Developer Guide*.

### Step 2: Check for the error
<a name="cloudformation_check-error"></a>

If the identity doesn't have permission to use `geo:TagResource`, the resource fails to create and the stack event shows the following message.

```
Resource handler returned message: "Access denied for operation 'AWS::Location::PlaceIndex'." (RequestToken: {{request-token}}, HandlerErrorCode: AccessDenied)
```

### Existing resources and stack updates
<a name="cloudformation_existing-resources"></a>

Existing resources keep working.
+ Stack updates that replace a resource require `geo:TagResource`, including for stacks created before February 26, 2027. For example, changing `IndexName` for `AWS::Location::PlaceIndex` replaces the resource. If the permission is missing, CloudFormation rolls back the update.
+ Stack updates that don't replace a resource, and stack deletes, don't require the new permission. Resources created before February 26, 2027 don't receive the CloudFormation tags from these updates.

## Learn more about CloudFormation
<a name="cloudformation_learn"></a>

To learn more about CloudFormation, see the following resources: 
+ [CloudFormation](https://aws.amazon.com/cloudformation) 
+ [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) 
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html) 
+ [CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html) 