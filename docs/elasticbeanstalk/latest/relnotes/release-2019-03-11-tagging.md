

# Release: AWS Elastic Beanstalk extends support for tagging to all resources on March 11, 2019
<a name="release-2019-03-11-tagging"></a>

Elastic Beanstalk extended support for tagging, and tag-based access control, to all Elastic Beanstalk resources.

**Release date:** March 11, 2019

## Changes
<a name="release-2019-03-11-tagging.changes"></a>

Prior to this release, Elastic Beanstalk supported tagging environments. You were also able to use AWS Identity and Access Management (IAM) policies to control access to environments based on their tags. Starting with today's release, we're extending support for tagging, and tag-based access control, to all Elastic Beanstalk resources: environments, applications, application versions, saved configurations, and custom platform versions.

**Note**  
At this time, you can manage tags for the four added resources using the API or the AWS CLI.

For more information about tagging Elastic Beanstalk resources, see [Tagging AWS Elastic Beanstalk Application Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html) in the *AWS Elastic Beanstalk Developer Guide*. For more information about tag-based access control, see [Controlling Access to Elastic Beanstalk Resources Using Tags](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.access-tags.html) in the guide.