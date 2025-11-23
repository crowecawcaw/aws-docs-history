# Release: Elastic Beanstalk increases timeout period for updates on February 7, 2025

AWS Elastic Beanstalk increases wait condition timeout, allowing more time for managed updates to complete successfully.

**Release date:** February 7, 2025

## Changes

Elastic Beanstalk has released a change that allows your managed platform updates more time to complete successfully. We have doubled the timeout period before a
wait condition timeout causes an unsuccessful status for a managed platform update, including immutable updates. This allows more time for the new EC2
instances launched as part of the update to complete their bootstrapping process.

The Elastic Beanstalk service coordinates resource creation with CloudFormation, and it sends the CloudFormation service a signal when your EC2 instance and application
successfully start up. Managed platform updates that may have required more time than originally provided by the previous setting for the [CloudFormation wait condition](../../../AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.md") timeout will now have more
time to complete successfully.

For more information about platform updates see [Managed platform updates](../dg/environment-platform-update-managed.md "../dg/environment-platform-update-managed.md") in the _AWS Elastic Beanstalk Developer Guide_.
