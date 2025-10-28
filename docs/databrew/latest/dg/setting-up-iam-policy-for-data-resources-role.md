# Adding permissions for

data resources for an IAM role

To connect to data, AWS Glue DataBrew needs to have an IAM role that it can pass on
behalf of the user. Following, you can find how to create the policy that you later
attach to an IAM role.

The `AwsGlueDataBrewDataResourcePolicy` policy grants the permissions
needed to connect to data using DataBrew. For any operation that accesses data in
another AWS resource, such as accessing your objects in Amazon S3, DataBrew needs permission
to access the resource on your behalf.

###### To define the AwsGlueDataBrewDataResourcePolicy IAM policy for DataBrew (console)

1. Download the JSON for [`AwsGlueDataBrewDataResourcePolicy`](samples/AwsGlueDataBrewDataResourcePolicy.json.md "samples/AwsGlueDataBrewDataResourcePolicy.json.md").
2. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
3. In the navigation pane, choose **Policies**.
4. For each policy, choose **Create Policy**.
5. On the **Create Policy** screen, navigate to the
   **JSON** tab.
6. Copy the policy JSON statement that you downloaded. Paste it over the sample
   statement in the editor.
7. Verify that the policy is customized to your account, security requirements, and
   required AWS resources. If you need to make changes, you can make them in the
   editor.
8. Choose **Review policy**.

###### To define the AwsGlueDataBrewDataResourcePolicy IAM policy for DataBrew (AWS CLI)

1. Download the JSON for [`AwsGlueDataBrewDataResourcePolicy`](samples/AwsGlueDataBrewDataResourcePolicy.json.md "samples/AwsGlueDataBrewDataResourcePolicy.json.md").
2. Customize the policy as described in the first step of the previous
   procedure.
3. Run the following command to create the policy.

```
aws iam create-policy --policy-name AwsGlueDataBrewDataResourcePolicy --policy-document file://iam-policy-AwsGlueDataBrewDataResourcePolicy.json
```
