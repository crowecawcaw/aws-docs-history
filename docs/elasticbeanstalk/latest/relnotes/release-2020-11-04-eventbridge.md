# Release: Elastic Beanstalk introduces Amazon EventBridge integration on November 04, 2020

AWS Elastic Beanstalk added integration with the Amazon EventBridge service.
You can use EventBridge to detect and react to changes in the status
of your Elastic Beanstalk resources.

**Release date:** November 04, 2020

## Changes

Activity that occurs in your Elastic Beanstalk environments is recorded as an AWS CloudTrail event. You can view general information about configuration changes to your
environments on the Events page in the Elastic Beanstalk console.

However, in some situations, you might want to have the ability
to detect specific events and initiate target actions using other AWS services. For example, you may want to send an email notification by signaling an
Amazon SNS topic when a production environment's health transitions to a _Warning_ status. Or, if the environment's health status
transitions to _Degraded_ or _Severe_, you might want to use a Lambda function to pass a notification to a Slack
channel. With this release, you can use Amazon EventBridge to set up event-driven rules that monitor your Elastic Beanstalk resources and initiate target actions that use other
AWS services.

For more information, see [Using Elastic Beanstalk with Amazon EventBridge](../dg/AWSHowTo.md "../dg/AWSHowTo.md") in
the _AWS Elastic Beanstalk Developer Guide_.
