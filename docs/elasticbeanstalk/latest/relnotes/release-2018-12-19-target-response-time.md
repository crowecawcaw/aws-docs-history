

# Release: AWS Elastic Beanstalk adds TargetResponseTime Auto Scaling trigger metric on December 19, 2018
<a name="release-2018-12-19-target-response-time"></a>

Elastic Beanstalk added the option to trigger Auto Scaling events based on response time for environments with Application Load Balancers.

**Release date:** December 19, 2018

## Changes
<a name="release-2018-12-19-target-response-time.changes"></a>

Today's release adds `TargetResponseTime` as a metric to trigger Auto Scaling activity for Elastic Beanstalk environments.

Previously, Elastic Beanstalk required custom `.ebextensions` to configure scaling based on response time for environments with Application Load Balancers. With today's release, you can configure scaling activity directly with the `TargetResponseTime` option in the [`aws:autoscaling:trigger`](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingtrigger) namespace. For details, see [Auto Scaling Triggers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-triggers.html) in the *AWS Elastic Beanstalk Developer Guide*.