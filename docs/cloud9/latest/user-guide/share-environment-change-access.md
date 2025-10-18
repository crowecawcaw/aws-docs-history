AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Change the access role of an
 environment member

This step shows how you can change the access role of an environment member. You can also
 use code to change the access role and update the AWS Cloud9 environment membership. 


1. Open the environment that you own and that contains the member whose access role you want
 to change, if the environment isn't already open. For more information, see [Opening an Environment in AWS Cloud9](open-environment.md "open-environment.md").
2. If the list of members isn't visible, expand **Environment
 Members** in the **Collaborate** window.
3. Do one of the following actions:




	* Next to the member name whose access role that you want to change, choose
	 **R** or **RW** to make this member owner
	 or read/write, respectively.
	* To change a read/write member to read-only, open the context (right-click) menu
	 for the member name, and then choose **Revoke Write
	 Access**.
	* To change a read-only member to read/write, open the context (right-click) menu
	 for the member name, and then choose **Grant Read+Write
	 Access**.
	
	
	###### Note
	
	If you make this user a read/write member, a dialog box is displayed,
	 containing information about possibly putting your AWS security
	 credentials at risk. Unless you trust that user to take actions in AWS on
	 your behalf, don't make a user a read/write member. For more information, see
	 the related note in [Invite a
	 User in the Same Account as the Environment](share-environment.md#share-environment-invite-user "share-environment.md#share-environment-invite-user").
To use code to change the access role of an environment member, call the AWS Cloud9 update environment
 membership operation, as follows.



|  |  |
| --- | --- |
| AWS CLI | [update-environment-membership](https://docs.aws.amazon.com/cli/latest/reference/cloud9/update-environment-membership.html "https://docs.aws.amazon.com/cli/latest/reference/cloud9/update-environment-membership.html") |
| AWS SDK for C++ | [UpdateEnvironmentMembershipRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_request.html "https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_request.html"), [UpdateEnvironmentMembershipResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_result.html "https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_result.html") |
| AWS SDK for Go | [UpdateEnvironmentMembership](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembership "https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembership"), [UpdateEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembershipRequest "https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembershipRequest"), [UpdateEnvironmentMembershipWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembershipWithContext "https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembershipWithContext") |
| AWS SDK for Java | [UpdateEnvironmentMembershipRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipRequest.html "https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipRequest.html"), [UpdateEnvironmentMembershipResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipResult.html "https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipResult.html") |
| AWS SDK for JavaScript | [updateEnvironmentMembership](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#updateEnvironmentMembership-property "https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#updateEnvironmentMembership-property") |
| AWS SDK for .NET | [UpdateEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentMembershipRequest.html "https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentMembershipRequest.html"), [UpdateEnvironmentMembershipResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentMembershipResponse.html "https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentMembershipResponse.html") |
| AWS SDK for PHP | [updateEnvironmentMembership](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#updateenvironmentmembership "https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#updateenvironmentmembership") |
| AWS SDK for Python (Boto) | [update\_environment\_membership](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.update_environment_membership "https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.update_environment_membership") |
| AWS SDK for Ruby | [update\_environment\_membership](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#update_environment_membership-instance_method "https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#update_environment_membership-instance_method") |
| AWS Tools for Windows PowerShell | [Update-C9EnvironmentMembership](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-C9EnvironmentMembership.html "https://docs.aws.amazon.com/powershell/latest/reference/items/Update-C9EnvironmentMembership.html") |
| AWS Cloud9 API | [UpdateEnvironmentMembership](../APIReference/API_UpdateEnvironmentMembership.md "../APIReference/API_UpdateEnvironmentMembership.md") |
