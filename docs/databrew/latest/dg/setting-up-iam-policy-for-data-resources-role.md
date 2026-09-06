

# Adding permissions for data resources for an IAM role
<a name="setting-up-iam-policy-for-data-resources-role"></a>

To connect to data, AWS Glue DataBrew needs to have an IAM role that it can pass on behalf of the user. Following, you can find how to create the policy that you later attach to an IAM role. 

The `AwsGlueDataBrewDataResourcePolicy` policy grants the permissions needed to connect to data using DataBrew. For any operation that accesses data in another AWS resource, such as accessing your objects in Amazon S3, DataBrew needs permission to access the resource on your behalf. <a name="AwsGlueDataBrewDataResourcePolicy-console-steps"></a>

**To define the AwsGlueDataBrewDataResourcePolicy IAM policy for DataBrew (console)**

1. Download the JSON for [`AwsGlueDataBrewDataResourcePolicy`](samples/AwsGlueDataBrewDataResourcePolicy.json.zip). 

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). 

1. In the navigation pane, choose **Policies**.

1. For each policy, choose **Create Policy**.

1. On the **Create Policy** screen, navigate to the **JSON** tab. 

1. Copy the policy JSON statement that you downloaded. Paste it over the sample statement in the editor.

1. Verify that the policy is customized to your account, security requirements, and required AWS resources. If you need to make changes, you can make them in the editor.

1. Choose **Review policy**.<a name="AwsGlueDataBrewDataResourcePolicy-cli-steps"></a>

**To define the AwsGlueDataBrewDataResourcePolicy IAM policy for DataBrew (AWS CLI)**

1. Download the JSON for [`AwsGlueDataBrewDataResourcePolicy`](samples/AwsGlueDataBrewDataResourcePolicy.json.zip). 

1. Customize the policy as described in the first step of the previous procedure.

1. Run the following command to create the policy.

   ```
   aws iam create-policy --policy-name AwsGlueDataBrewDataResourcePolicy --policy-document file://iam-policy-AwsGlueDataBrewDataResourcePolicy.json
   ```