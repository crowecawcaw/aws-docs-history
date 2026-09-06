

# Release: Elastic Beanstalk increases timeout period for updates on February 7, 2025
<a name="release-2025-02-07-release-notes"></a>

AWS Elastic Beanstalk increases wait condition timeout, allowing more time for managed updates to complete successfully.

**Release date:** February 7, 2025

## Changes
<a name="release-2025-02-07-release-notes.changes"></a>

Elastic Beanstalk has released a change that allows your managed platform updates more time to complete successfully. We have doubled the timeout period before a wait condition timeout causes an unsuccessful status for a managed platform update, including immutable updates. This allows more time for the new EC2 instances launched as part of the update to complete their bootstrapping process.

The Elastic Beanstalk service coordinates resource creation with CloudFormation, and it sends the CloudFormation service a signal when your EC2 instance and application successfully start up. Managed platform updates that may have required more time than originally provided by the previous setting for the [CloudFormation wait condition ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html) timeout will now have more time to complete successfully.

For more information about platform updates see [ Managed platform updates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html) in the *AWS Elastic Beanstalk Developer Guide*.