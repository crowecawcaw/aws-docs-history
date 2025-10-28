# Release: Elastic Beanstalk added support for tagging launch templates on October 18, 2023

AWS Elastic Beanstalk added support for tagging launch templates.

**Release date:** October 18, 2023

## Changes

Elastic Beanstalk now provides the option to enable the propagation of environment tags to launch templates. This option provides continued support for tag-based
access control (TBAC) with launch templates.

You can enable this feature with the `LaunchTemplateTagPropagationEnabled` option in the [aws:autoscaling:launchconfiguration](../dg/command-options-general.md#command-options-general-autoscalinglaunchconfiguration "../dg/command-options-general.md#command-options-general-autoscalinglaunchconfiguration") namespace. For more information, see [Tag propagation to launch
templates](../dg/applications-tagging-resources.md#applications-tagging-resources.launch-templates "../dg/applications-tagging-resources.md#applications-tagging-resources.launch-templates") in the _AWS Elastic Beanstalk Developer Guide_.
