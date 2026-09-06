

# Setting up IAM permissions for users
<a name="setting-up-for-production"></a>

This section describes the permissions that you must assign to users and other AWS identities so that they can work with AWS Elemental MediaLive and other AWS services that your workflows use. After you have identified the required permissions, you will be able to design and create the relevant policies, and attach those policies to groups of users or to roles. 

This section assumes that you have already performed these tasks:
+ You have performed the initial setup described in [Preliminary steps for setting up to use MediaLive](setting-up.md) in order to sign up for MediaLive and to create an administrator. 
+ You have read the recommendations in [Identity and Access Management for AWS Elemental MediaLive](security-iam.md) about how to create administrators, users, and other AWS identities.

**Topics**
+ [Reference: summary of user access](setup-users-step-1-summary.md)
+ [MediaLive](requirements-for-medialive.md)
+ [MediaLive Anywhere](requirements-for-emla.md)
+ [CloudFormation](requirements-for-CFN.md)
+ [CloudFront](requirements-for-CFront.md)
+ [CloudTrail](requirements-for-cloudtrail.md)
+ [CloudWatch—channel health](requirements-for-monitor-channel-health.md)
+ [CloudWatch and Amazon SNS—email notification](requirements-for-email-notification.md)
+ [CloudWatch Logs—channel logging](requirements-for-console-logging.md)
+ [EC2 —VPC inputs](requirements-for-vpc-input.md)
+ [EC2 —delivery via VPC](requirements-vpc-delivery.md)
+ [Elemental Inference](requirements-for-inference.md)
+ [Link](requirements-for-link.md)
+ [MediaConnect](requirements-for-media-connect.md)
+ [MediaPackage](requirements-for-mediapackage.md)
+ [Resource Groups—tagging](requirements-for-tagging.md)
+ [Amazon S3](requirements-for-s3.md)
+ [Secrets Manager secrets](requirements-for-secrets.md)
+ [Systems Manager parameter store](requirements-for-EC2.md)