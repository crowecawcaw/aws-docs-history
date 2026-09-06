

# Adding an IAM policy for a console user
<a name="setting-up-iam-policy-for-databrew-console-access"></a>

Setting up permissions for a user for the AWS Management Console is optional, but if you require console access, take this step first.

To set up permissions to reach DataBrew on the console, choose one of the following:
+ Use the policy that's managed by AWS: `AwsGlueDataBrewFullAccessPolicy`. If you choose this option, skip to the next policy, [Adding permissions for data resources for an IAM role](setting-up-iam-policy-for-data-resources-role.md). 
+ Create the policy described in this section, `AwsGlueDataBrewCustomUserPolicy`. This option enables you to customize the policy with additional custom security requirements.

The following policy grants the permissions needed to run the DataBrew console. You provide those permissions by using IAM.<a name="AwsGlueDataBrewCustomUserPolicy-console-steps"></a>

**To define the AwsGlueDataBrewCustomUserPolicy IAM policy for DataBrew (console)**

1. Download the JSON for the [`AwsGlueDataBrewCustomUserPolicy`](samples/AwsGlueDataBrewCustomUserPolicy.json.zip) IAM policy. 

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). 

1. In the navigation pane, choose **Policies**.

1. For each policy, choose **Create Policy**.

1. On the **Create Policy** screen, navigate to the **JSON** tab. 

1. Copy the policy JSON statement that you downloaded. Paste it over the sample statement in the editor.

1. Verify that the policy is customized to your account, security requirements, and required AWS resources. If you need to make changes, you can make them in the editor.

1. Choose **Review policy**.<a name="AwsGlueDataBrewCustomUserPolicy-cli-steps"></a>

**To define the AwsGlueDataBrewCustomUserPolicy IAM policy for DataBrew (AWS CLI)**

1. Download the JSON for the [`AwsGlueDataBrewCustomUserPolicy`](samples/AwsGlueDataBrewCustomUserPolicy.json.zip) IAM policy. 

1. Customize the policy as described in the first step of the previous procedure.

1. Run the following command to create the policy.

   ```
   aws iam create-policy --policy-name AwsGlueDataBrewCustomUserPolicy --policy-document file://iam-policy-AwsGlueDataBrewCustomUserPolicy.json
   ```