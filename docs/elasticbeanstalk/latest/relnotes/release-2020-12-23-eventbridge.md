# Release: Elastic Beanstalk introduces Amazon EventBridge console integration on December 23, 2020

Following the release of AWS Elastic Beanstalk integration with the Amazon EventBridge service in November-2020,
the EventBridge console has now made it easier for Elastic Beanstalk customers to define rules and event patterns.
You can now use pre-defined event patterns for Elastic Beanstalk in the EventBridge console.

**Release date:** December 23, 2020

## Changes

Amazon EventBridge integration with Elastic Beanstalk makes it possible to detect specific events and initiate target actions by using several key features from other AWS
services. To accomplish this, you create an EventBridge rule based on Elastic Beanstalk events. Before this release, you only could create a rule by entering and saving a
custom event pattern for Elastic Beanstalk.

This release introduces pre-defined event patterns for Elastic Beanstalk in the EventBridge console. With this feature, the EventBridge console builds an Elastic Beanstalk event pattern as
you select Elastic Beanstalk event fields and values. The EventBridge console displays the event pattern as you build it, providing a built-in method to create rules that
respond to Elastic Beanstalk events.

For more information, see [Using Elastic Beanstalk with Amazon EventBridge](../dg/AWSHowTo.md "../dg/AWSHowTo.md") in
the _AWS Elastic Beanstalk Developer Guide_.
