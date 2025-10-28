# Release: Elastic Beanstalk introduces change history for environments on January 7, 2021

AWS Elastic Beanstalk added the ability to view a history of configuration changes made to your Elastic Beanstalk environments.
This information includes the configuration parameter that was changed and its new value, the date and time the
change occurred, and the user that made the change.

**Release date:** January 7, 2021

## Changes

Activity that occurs in your Elastic Beanstalk environments is recorded as an AWS CloudTrail event. You can view general information about configuration changes to your
environments on the Events page in the Elastic Beanstalk console. However, in some situations you might want to see more specific information related to these
changes, such as which user made the configuration change or what value a configuration parameter was set to. Until now, you would've needed to
navigate to CloudTrail and search for this information there.

With this release, you can access this more detailed change history information related to your Elastic Beanstalk environments directly through the Elastic Beanstalk console.
The Change History panel displays a list of detailed configuration changes for all of your Elastic Beanstalk environments, including information about who made the
changes, what the configuration values were set to and when the changes were made. You can filter this information using the Change History panel's
search bar.

For more information, see [Change history](../dg/using-features.md "../dg/using-features.md") in the
_AWS Elastic Beanstalk Developer Guide_.
