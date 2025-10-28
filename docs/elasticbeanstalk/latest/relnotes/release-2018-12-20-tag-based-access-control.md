# Release: AWS Elastic Beanstalk support for Tag-Based Access Control on December 20, 2018

Elastic Beanstalk added support for using tags in AWS Identity and Access Management (IAM) conditions in user policies.

**Release date:** December 20, 2018

## Changes

Conditions in IAM user policy statements are part of the syntax that you use to specify permissions to resources that Elastic Beanstalk actions need to
complete.

Starting with today's release, you can specify tags in policy conditions as a new way to control access of requests to resources. When a user makes
an API request to act on an Elastic Beanstalk environment, tags in the request and tags attached to the environment play a part in determining if the action is
allowed or denied.

For more information about tag-based access control in Elastic Beanstalk, see [Controlling Access
to Elastic Beanstalk Resources Using Tags](../dg/AWSHowTo.iam.policies.md "../dg/AWSHowTo.iam.policies.md") in the _AWS Elastic Beanstalk Developer Guide_.
