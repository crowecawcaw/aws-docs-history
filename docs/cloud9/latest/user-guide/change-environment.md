AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Changing environment settings in AWS Cloud9

You can change the preferences or settings for an AWS Cloud9 development environment.

- [Change Environment Preferences](#change-environment-single "#change-environment-single")
- [Change Environment Settings with the Console](#change-environment-description "#change-environment-description")
- [Change Environment Settings with Code](#change-environment-description-code "#change-environment-description-code")

## Change environment preferences

1. Open the environment that you want to change settings for. To open an environment, see [Opening an Environment](open-environment.md "open-environment.md").
2. In the AWS Cloud9 IDE, on the menu bar, choose **AWS Cloud9**, **Preferences**.
3. In the **Preferences** window, choose **Project Settings**.
4. Change any of the available project settings as you want. These include settings such as **Code Editor (Ace)** and **Find in Files**.

###### Note

For more information, see [Project Setting Changes You Can Make](settings-project-change.md "settings-project-change.md").

### Adjusting the timeout of an environment in the AWS Cloud9 IDE

The following steps outline how to update the timeout period for an Amazon EC2 environment in the AWS Cloud9 IDE. This will be the amount of time before the environment stops.

1. Open the environment that you want to configure.
2. In the **AWS Cloud9 IDE**, on the menu bar, choose **AWS Cloud9** **Preferences**.
3. In the **Preferences** window scroll to the **Amazon EC2 instance** section.
4. Select the timeout value from the list available and update.

## Change environment settings with the

console

1. Sign in to the AWS Cloud9 console as follows:
   - If you're the only individual using your AWS account or you're an
     IAM user in a single AWS account, go to [https://console.aws.amazon.com/cloud9/](https://console.aws.amazon.com/cloud9/ "https://console.aws.amazon.com/cloud9/").
   - If your organization uses AWS IAM Identity Center, see your AWS account administrator
     for sign-in instructions.

2. In the top navigation bar, choose the AWS Region where the environment is
   located.

![AWS Region selector in the AWS Cloud9 console](/images/cloud9/latest/user-guide/images/consolas_region_new_UX.png) 3. In the list of environments, for the environment whose settings you want to change, do one of the following.

    * Choose the title of the card for the environment. Then choose **View
     details** on the next page.
    * Select the card for the environment, and then choose the **View
     details** button.

4. Make your changes, and then choose **Save changes**.

You can use the AWS Cloud9 console to change the following settings.

    * For EC2 environments, **Name** and **Description**.
    * For SSH environments: **Name**, **Description**, **User**, **Host**, **Port**,
    **Environment path**, **Node.js binary path**, and **SSH jump host**.

To change other settings, do the following.

    * For EC2 environments, do the following.




    	+ You cannot change **Type**, **Security groups**, **VPC**, **Subnet**, **Environment path**, or **Environment ARN**.
    	+ For **Permissions** or **Number of members**, see [Change the Access Role of an Environment

    	 Member](share-environment-change-access.md "share-environment-change-access.md"),
    	[Remove Your User](share-environment-change-access.md "share-environment-change-access.md"), [Invite an IAM user](share-environment.md#share-environment-invite-user "share-environment.md#share-environment-invite-user"), and
    	[Remove Another Environment

    	 Member](share-environment-delete-member.md "share-environment-delete-member.md").
    	+ For **EC2 instance type**, **Memory**, or **vCPU**, see [Moving or Resizing an Environment](move-environment.md "move-environment.md").
    * For SSH environments, do the following.




    	+ You cannot change **Type** or **Environment ARN**.
    	+ For **Permissions** or **Number of members**, see [Change the Access Role of an Environment

    	 Member](share-environment-change-access.md "share-environment-change-access.md"),
    	[Remove Your User](share-environment-change-access.md "share-environment-change-access.md"), [Invite an IAM User](share-environment.md#share-environment-invite-user "share-environment.md#share-environment-invite-user"), and
    	[Remove Another Environment

    	 Member](share-environment-delete-member.md "share-environment-delete-member.md").

If your environment isn't displayed in the console, try doing one or more of the following
actions to have it be displayed.

- In the dropdown menu bar on the **Environments** page, choose one or
  more of the following.
  - Choose **My environments** to display all environments that your
    AWS entity owns within the selected AWS Region and AWS account.
  - Choose **Shared with me** to display all environments your
    AWS entity was invited to within the selected AWS Region and
    AWS account.
  - Choose **All account environments** to display all environments
    within the selected AWS Region and AWS account that your AWS entity has
    permissions to display.

- If you think you are a member of an environment, but the environment isn't displayed in the
  **Shared with you** list, check with the environment owner.
- In the top navigation bar, choose a different AWS Region.

## Change environment settings with code

To use code to change the settings of an environment in AWS Cloud9, call the AWS Cloud9 update environment operation, as follows.

|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS CLI                          | [update-environment](../../../cli/latest/reference/cloud9/update-environment.md "../../../cli/latest/reference/cloud9/update-environment.md")                                                                                                                                                                                                                                                                                                                                                                                                        |
| AWS SDK for C++                  | [UpdateEnvironmentRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_request.html "https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_request.html"),<br>[UpdateEnvironmentResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_result.html "https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_result.html")                                         |
| AWS SDK for Go                   | [UpdateEnvironment](../../../sdk-for-go/api/service/cloud9.md#Cloud9.UpdateEnvironment "../../../sdk-for-go/api/service/cloud9.md#Cloud9.UpdateEnvironment"),<br>[UpdateEnvironmentRequest](../../../sdk-for-go/api/service/cloud9.md#Cloud9.UpdateEnvironmentRequest "../../../sdk-for-go/api/service/cloud9.md#Cloud9.UpdateEnvironmentRequest"),<br>[UpdateEnvironmentWithContext](../../../sdk-for-go/api/service/cloud9.md#Cloud9.UpdateEnvironmentWithContext "../../../sdk-for-go/api/service/cloud9.md#Cloud9.UpdateEnvironmentWithContext") |
| AWS SDK for Java                 | [UpdateEnvironmentRequest](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentRequest.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentRequest.md"),<br>[UpdateEnvironmentResult](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentResult.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentResult.md")                                                                             |
| AWS SDK for JavaScript           | [updateEnvironment](../../../AWSJavaScriptSDK/latest/AWS/Cloud9.md#updateEnvironment-property "../../../AWSJavaScriptSDK/latest/AWS/Cloud9.md#updateEnvironment-property")                                                                                                                                                                                                                                                                                                                                                                           |
| AWS SDK for .NET                 | [UpdateEnvironmentRequest](../../../sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentRequest.md "../../../sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentRequest.md"),<br>[UpdateEnvironmentResponse](../../../sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentResponse.md "../../../sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentResponse.md")                                                                                                                                                                                   |
| AWS SDK for PHP                  | [updateEnvironment](../../../aws-sdk-php/v3/api/api-cloud9-2017-09-23.md#updateenvironment "../../../aws-sdk-php/v3/api/api-cloud9-2017-09-23.md#updateenvironment")                                                                                                                                                                                                                                                                                                                                                                                 |
| AWS SDK for Python (Boto)        | [update_environment](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.update_environment "https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.update_environment")                                                                                                                                                                                                                                                                                                                |
| AWS SDK for Ruby                 | [update_environment](../../../sdk-for-ruby/v3/api/Aws/Cloud9/Client.md#update_environment-instance_method "../../../sdk-for-ruby/v3/api/Aws/Cloud9/Client.md#update_environment-instance_method")                                                                                                                                                                                                                                                                                                                                                    |
| AWS Tools for Windows PowerShell | [Update-C9Environment](../../../powershell/latest/reference/items/Update-C9Environment.md "../../../powershell/latest/reference/items/Update-C9Environment.md")                                                                                                                                                                                                                                                                                                                                                                                      |
| AWS Cloud9 API                   | [UpdateEnvironment](../APIReference/API_UpdateEnvironment.md "../APIReference/API_UpdateEnvironment.md")                                                                                                                                                                                                                                                                                                                                                                                                                                             |
