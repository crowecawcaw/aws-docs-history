

# Tag propagation to launch templates
<a name="applications-tagging-resources.launch-templates"></a>

Elastic Beanstalk provides an option to enable the propagation of environment tags to launch templates. This option provides continued support for tag-based access control (TBAC) with launch templates.

**Note**  
Launch configurations are being phased out and replaced by launch templates. For more information, see [Launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html) in the *Amazon EC2 Auto Scaling User Guide*.

To prevent down-time of running EC2 instances CloudFormation doesn’t propagate tags to existing launch templates. If there's a use case that requires tags for your environment’s resources, you can enable Elastic Beanstalk to create launch templates with tags for these resources. To do so, set the `LaunchTemplateTagPropagationEnabled` option in the [aws:autoscaling:launchconfiguration](command-options-general.md#command-options-general-autoscalinglaunchconfiguration) namespace to `true`. The default value is `false`.

The following [configuration file](ebextensions.md) example enables the propagation of tags to launch templates.

```
option_settings:
  aws:autoscaling:launchconfiguration:
    LaunchTemplateTagPropagationEnabled: true
```

Elastic Beanstalk can only propagate tags to launch templates for the following resources:
+ EBS volumes
+ EC2 instances 
+ EC2 network interfaces
+ CloudFormation launch templates that define a resource

This constraint exists because CloudFormation only allows tags on template creation for specific resources. For more information see [TagSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html) in the *AWS CloudFormation User Guide*.

**Important**  
Changing this option value from `false` to `true` for an existing environment may be a breaking change for previously existing tags.
When this feature is enabled, the propagation of tags will require EC2 replacement, which can result in downtime. You can enable *rolling updates* to apply configuration changes in batches and prevent downtime during the update process. For more information, see [Configuration changes](environments-updating.md).

For more information about launch templates, see the following:
+ [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) in the *Amazon EC2 Auto Scaling User Guide*
+ [Working with templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*
+ [Elastic Beanstalk template snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elasticbeanstalk.html) in the *AWS CloudFormation User Guide*