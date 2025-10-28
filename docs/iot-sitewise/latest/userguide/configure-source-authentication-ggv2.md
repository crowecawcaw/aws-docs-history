# Configure data source

authentication for SiteWise Edge

If your OPC UA server requires authentication credentials to connect, you can use
AWS Secrets Manager to create and deploy a secret to your SiteWise Edge gateway. AWS Secrets Manager encrypts
secrets on the device to keep your user name and password secure until you need to use
them. For more information about the AWS IoT Greengrass secret manager component, see [Secret manager](../../../greengrass/v2/developerguide/secret-manager-component.md "../../../greengrass/v2/developerguide/secret-manager-component.md") in the _AWS IoT Greengrass Version 2 Developer Guide_.

For information about managing access to Secrets Manager secrets, see:

- [Who has permissions to your AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.md "../../../secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.md").
- [Determining if a request is allowed or denied within an account](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow").

## Step 1: Create source authentication

secrets

You can use AWS Secrets Manager to create an authentication secret for your data source. In
the secret, define `username` and
`password` key-value pairs that contain authentication
details for your data source.

###### To create a secret (console)

1. Navigate to the [AWS Secrets Manager
   console](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. Under **Secret type**, choose **Other type of
   secrets**.
4. Under **Key/value pairs**, do the following:
   1. In the first input box, enter `username` and in the second input box enter the username.
   2. Choose **Add row**.
   3. In the first input box, enter `password` and in the second input box enter the password.

5. For **Encryption key**, select
   **aws/secretsmanager**, and then choose
   **Next**.
6. On the **Store a new secret** page, enter a
   **Secret name**.
7. (Optional) Enter a **Description** that helps you
   identify this secret, and then choose **Next**.
8. (Optional) On the **Store a new secret** page, turn on
   **Automatic rotation**. For more information, see
   [Rotate
   secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_.
9. Specify a rotation schedule.
10. Choose a Lambda function that can rotate this secret, and then choose
    **Next**.
11. Review your secret configurations, and then choose
    **Store**.

To authorize your SiteWise Edge gateway to interact with AWS Secrets Manager, the IAM role for
your SiteWise Edge gateway must allow the `secretsmanager:GetSecretValue`
action. You can use the **Greengrass core device** to search for the IAM policy.
For more information about updating an IAM policy, see [Editing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _AWS Identity and Access Management User
Guide_.

###### Example policy

Replace `secret-arn` with the Amazon Resource Name
(ARN) of the secret that you created in the previous step. For more information
about how to get the ARN of a secret, see [Find secrets in AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") in the _AWS Secrets Manager User
Guide_.

JSON

```
`{
"Version":"2012-10-17",
"Statement":[
 {
 "Action":[
 "secretsmanager:GetSecretValue"
 ],
 "Effect":"Allow",
 "Resource":[
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret/*"
 ]
 }
]
}`

```

## Step 2: Deploy secrets to your SiteWise Edge gateway

device

You can use the AWS IoT SiteWise console to deploy secrets to your SiteWise Edge gateway.

###### To deploy a secret (console)

1. Navigate to the [AWS IoT SiteWise
   console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Gateways**.
3. From the **Gateways** list, choose the target
   SiteWise Edge gateway.
4. In the **Gateway configuration** section, choose the
   **Greengrass core device** link to open the AWS IoT Greengrass core
   associated with the SiteWise Edge gateway.
5. In the navigation pane, choose **Deployments**.
6. Choose the target deployment, and then choose
   **Revise**.
7. On the **Specify target** page, choose
   **Next**.
8. On the **Select components** page, in the
   **Public components** section, turn off **Show
   only selected components**.
9. Search for and choose the
   **aws.greengrass.SecretManager** component, and then
   choose **Next**.
10. From the **Selected components** list, choose the
    **aws.greengrass.SecretManager** component, and then
    choose **Configure component**.
11. In the **Configuration to merge** field, add the
    following JSON object.

###### Note

Replace `secret-arn` with the ARN of the
secret that you created in the previous step. For more information about
how to get the ARN of a secret, see [Find secrets in AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") in the _AWS Secrets Manager User
Guide_.

```
{
"cloudSecrets":[
  {
     "arn":"`secret-arn`"
  }
]
}
```

12. Choose **Confirm**.
13. Choose **Next**.
14. On the **Configure advanced settings** page, choose
    **Next**.
15. Review your deployment configurations, and then choose
    **Deploy**.

## Step 3: Add authentication

configurations

You can use the AWS IoT SiteWise console to add authentication configurations to your
SiteWise Edge gateway.

###### To add authentication configurations (console)

1. Navigate to the [AWS IoT SiteWise
   console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. From the **Gateways** list, choose the target
   SiteWise Edge gateway.
3. From the **Data sources** list, choose the target data
   source, and then choose **Edit**.
4. On the **Add a data source** page, choose
   **Advanced configuration**.
5. For **Authentication configuration**, choose the secret
   that you deployed in the previous step.
6. Choose **Save**.
