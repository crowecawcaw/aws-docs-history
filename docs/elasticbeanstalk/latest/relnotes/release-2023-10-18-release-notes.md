

# Release: Elastic Beanstalk added support for tagging launch templates on October 18, 2023
<a name="release-2023-10-18-release-notes"></a>

AWS Elastic Beanstalk added support for tagging launch templates.

**Release date:** October 18, 2023

## Changes
<a name="release-2023-10-18-release-notes.changes"></a>

Elastic Beanstalk now provides the option to enable the propagation of environment tags to launch templates. This option provides continued support for tag-based access control (TBAC) with launch templates.

You can enable this feature with the `LaunchTemplateTagPropagationEnabled` option in the [aws:autoscaling:launchconfiguration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalinglaunchconfiguration) namespace. For more information, see [Tag propagation to launch templates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html#applications-tagging-resources.launch-templates) in the *AWS Elastic Beanstalk Developer Guide*.