AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Remove your user from a shared
 Environment

This step shows how you can remove your user from a shared environment.

###### Note

If you're the environment owner, you can't remove your user from an environment.

Removing your user from an environment doesn't remove your user from IAM.


1. With the shared environment open, in the **Collaborate** window, expand
 **Environment Members**, if the list of members isn't
 visible.
2. Do one of the following actions:




	* Next to **You**, choose the trash can icon.
	* Open the context (right-click) menu for **You**, and then
	 choose **Leave environment**.
3. When prompted, choose **Leave**.
To use code to remove your user from a shared environment, call the AWS Cloud9 delete environment
 membership operation, as follows.



|  |  |
| --- | --- |
| AWS CLI | [delete-environment-membership](https://docs.aws.amazon.com/cli/latest/reference/cloud9/delete-environment-membership.html "https://docs.aws.amazon.com/cli/latest/reference/cloud9/delete-environment-membership.html") |
| AWS SDK for C++ | [DeleteEnvironmentMembershipRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_request.html "https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_request.html"), [DeleteEnvironmentMembershipResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_result.html "https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_result.html") |
| AWS SDK for Go | [DeleteEnvironmentMembership](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembership "https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembership"), [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipRequest "https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipRequest"), [DeleteEnvironmentMembershipWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipWithContext "https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipWithContext") |
| AWS SDK for Java | [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipRequest.html "https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipRequest.html"), [DeleteEnvironmentMembershipResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipResult.html "https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipResult.html") |
| AWS SDK for JavaScript | [deleteEnvironmentMembership](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#deleteEnvironmentMembership-property "https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#deleteEnvironmentMembership-property") |
| AWS SDK for .NET | [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipRequest.html "https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipRequest.html"), [DeleteEnvironmentMembershipResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipResponse.html "https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipResponse.html") |
| AWS SDK for PHP | [deleteEnvironmentMembership](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#deleteenvironmentmembership "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#deleteenvironmentmembership") |
| AWS SDK for Python (Boto) | [delete\_environment\_membership](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership "https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership") |
| AWS SDK for Ruby | [delete\_environment\_membership](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#delete_environment_membership-instance_method "https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#delete_environment_membership-instance_method") |
| AWS Tools for Windows PowerShell | [Remove-C9EnvironmentMembership](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-C9EnvironmentMembership.html "https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-C9EnvironmentMembership.html") |
| AWS Cloud9 API | [DeleteEnvironmentMembership](../APIReference/API_DeleteEnvironmentMembership.md "../APIReference/API_DeleteEnvironmentMembership.md") |
