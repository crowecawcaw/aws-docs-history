

# Setting up MediaLive as a trusted entity
<a name="device-iam-for-medialive"></a>

An IAM administrator must consider the special permissions that MediaLive requires if your organization will use a Link device as the source for a MediaConnect flow. 

You must set up MediaLive as a *trusted entity*. In a trusted entity relationship, a role identifies MediaLive as a trusted entity. One or more policies are attached to the role. Each policy contains statements about allowed operations and resources. The chain between the trusted entity, role, and policies makes this statement:

"MediaLive is allowed to assume this role in order to perform the operations on the resources that are specified in the policies."

**Important**  
You might be familiar with the trusted entity role that MediaLive needs [to work with channels at runtime](setting-up-trusted-entity.md). We recommend that you create a separate trusted entity role for MediaLive to use with Link devices. The permissions for channels are very complicated. The permissions for devices are very simple. Keep them separate.

**Permissions that MediaLive requires**

For you to use a Link device, MediaLive must have permissions on operations and resources in MediaConnect and in Secrets Manager:
+ For MediaConnect: MediaLive must be able to read details about a flow. This allows MediaLive to retrieve flow configuration information (such as the ingest endpoint) so that the device knows where to send content. This permission is read-only and does not allow MediaLive to modify or delete the flow.
+ For Secrets Manager: The device always encrypts the content it sends to MediaConnect. It encrypts using an encryption key that MediaLive provides. MediaLive in turn obtains the encryption key from a secret that the MediaConnect user has stored in Secrets Manager. Therefore, MediaLive needs permission to read the encryption key that is stored in a secret. This permission is limited to reading the specific secrets that you identify in the policy. It does not grant MediaLive access to other secrets in your account.

This table specifies the required operations and resources.


| Permissions | Service name in IAM | Actions | Resources | 
| --- | --- | --- | --- | 
| View the details of a flow | mediaconnect | `DescribeFlow`<br />  | All resources | 
| Obtain the encryption key from the secret. See the explanation after this table. | secretsmanager | `GetSecretValue` | The ARN of each secret that holds an encryption key that MediaLive needs to access | 

**Topics**
+ [Step 1: Create the IAM policy](#device-iam-medialive-policy)
+ [Step 2: Set up the trusted entity role](#device-iam-medialive-role)

## Step 1: Create the IAM policy
<a name="device-iam-medialive-policy"></a>

In this step, you create a policy that makes the statement "Let a principal have access to the specified Secrets Manager actions on the specified resource". Note that the policy doesn't specify a principal. You specify the principal in the next step, when you set up the trusted entity role.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. Choose **Create Policy**, then choose the **JSON** tab.

1. In the **Policy editor**, clear the sample content and paste the following:

1. In the **Resource** section for **secretsmanager**, replace the Region, account, and secret name with real values.

1. Add more lines in the **Resources** section or `secretsmanager`, one for each secret. Make sure you include a comma at the end of all lines except the last line. For example:

   ```
         "Resource": [
           "arn:aws:secretsmanager:us-west-2:111122223333:secret:emx_special_skating-KM19jL",
           "arn:aws:secretsmanager:us-west-2:111122223333:secret:aes-":secret:emx_weekly_live_poetry-3ASA30",
           "arn:aws:secretsmanager:us-west-2:111122223333:secret:aes-":secret:emx_tuesday_night_curling-AMcb01"
         ]
   ```

1. Give the policy a name that makes it clear that this policy is for Link and a flow. For example, `medialiveForLinkFlowAccess`. 

1. Choose **Create policy**.

## Step 2: Set up the trusted entity role
<a name="device-iam-medialive-role"></a>

In this step, you create a role that consists of a trust policy ("let MediaLive call the `AssumeRole` action") and a policy (the policy that you just created). In this way, MediaLive has permission to assume the role. When it assumes the role, it acquires the permissions specified in the policy. 

1. On the IAM console, in the navigation pane, choose **Roles**, then **Create Role**. The **Create role** wizard appears. This wizard walks you through the steps of setting up a trusted entity, and adding permissions (by adding a policy).

1. On the **Select trusted entity** page, choose the **Custom trust policy** card. The **Custom trust policy **section appears, with a sample policy.

1. Erase the sample, copy the following text, and paste the text in the **Custom trust policy **section. The **Custom trust policy **section now looks like this:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
   	{
               "Effect": "Allow",
               "Principal": {
                   "Service": "medialive.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. Choose **Next**. 

1. On the **Add Permissions** page, find the policy that you created (for example, `medialiveForLinkFlowAccess`), and select the checkbox. Then choose **Next**.

1. On the review page, enter a name for the role. For example, `medialiveRoleForLinkFlowAccess`. 

1. Choose **Create role**.