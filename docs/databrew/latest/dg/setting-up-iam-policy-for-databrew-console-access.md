# Adding an IAM policy for a console user

Setting up permissions for a user for the AWS Management Console is optional, but if you
require console access, take this step first.

To set up permissions to reach DataBrew on the console, choose one of the
following:

- Use the policy that's managed by AWS:
  `AwsGlueDataBrewFullAccessPolicy`. If you choose this option,
  skip to the next policy, [Adding permissions for
  data resources for an IAM role](setting-up-iam-policy-for-data-resources-role.md "setting-up-iam-policy-for-data-resources-role.md").
- Create the policy described in this section,
  `AwsGlueDataBrewCustomUserPolicy`. This option enables you to
  customize the policy with additional custom security requirements.
  The
  following policy grants the permissions needed to run the DataBrew console. You provide those
  permissions by using IAM.

###### To define the AwsGlueDataBrewCustomUserPolicy IAM policy for DataBrew (console)

1. Download the JSON for the [`AwsGlueDataBrewCustomUserPolicy`](samples/AwsGlueDataBrewCustomUserPolicy.json.md "samples/AwsGlueDataBrewCustomUserPolicy.json.md") IAM policy.
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

###### To define the AwsGlueDataBrewCustomUserPolicy IAM policy for DataBrew (AWS CLI)

1. Download the JSON for the [`AwsGlueDataBrewCustomUserPolicy`](samples/AwsGlueDataBrewCustomUserPolicy.json.md "samples/AwsGlueDataBrewCustomUserPolicy.json.md") IAM policy.
2. Customize the policy as described in the first step of the previous
   procedure.
3. Run the following command to create the policy.

```
aws iam create-policy --policy-name AwsGlueDataBrewCustomUserPolicy --policy-document file://iam-policy-AwsGlueDataBrewCustomUserPolicy.json
```
