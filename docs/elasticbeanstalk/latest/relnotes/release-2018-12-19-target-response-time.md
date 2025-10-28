# Release: AWS Elastic Beanstalk adds TargetResponseTime Auto Scaling trigger metric on December 19, 2018

Elastic Beanstalk added the option to trigger Auto Scaling events based on response time for environments with Application Load Balancers.

**Release date:** December 19, 2018

## Changes

Today's release adds `TargetResponseTime` as a metric to trigger Auto Scaling activity for Elastic Beanstalk environments.

Previously, Elastic Beanstalk required custom `.ebextensions` to configure scaling based on response time for environments with Application Load
Balancers. With today's release, you can configure scaling activity directly with the
`TargetResponseTime` option in the
[`aws:autoscaling:trigger`](../dg/command-options-general.md#command-options-general-autoscalingtrigger "../dg/command-options-general.md#command-options-general-autoscalingtrigger") namespace. For details, see [Auto Scaling Triggers](../dg/environments-cfg-autoscaling-triggers.md "../dg/environments-cfg-autoscaling-triggers.md") in the _AWS Elastic Beanstalk Developer
Guide_.
