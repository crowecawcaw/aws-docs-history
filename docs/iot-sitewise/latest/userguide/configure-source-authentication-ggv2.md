

# Configure data source authentication for SiteWise Edge
<a name="configure-source-authentication-ggv2"></a>

If your OPC UA server requires authentication credentials to connect, you can use AWS Secrets Manager to create and deploy a secret to your SiteWise Edge gateway. AWS Secrets Manager encrypts secrets on the device to keep your user name and password secure until you need to use them. For more information about the AWS IoT Greengrass secret manager component, see [Secret manager](https://docs.aws.amazon.com/greengrass/v2/developerguide/secret-manager-component.html) in the *AWS IoT Greengrass Version 2 Developer Guide*.

For information about managing access to Secrets Manager secrets, see:
+ [ Who has permissions to your AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html).
+ [ Determining if a request is allowed or denied within an account](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow).

## Step 1: Create source authentication secrets
<a name="create-secrets-ggv2"></a>

You can use AWS Secrets Manager to create an authentication secret for your data source. In the secret, define **username** and **password** key-value pairs that contain authentication details for your data source.

**To create a secret (console)**

1. Navigate to the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. Under **Secret type**, choose **Other type of secrets**.

1. Under **Key/value pairs**, do the following:

   1. In the first input box, enter **username** and in the second input box enter the username.

   1. Choose **Add row**.

   1. In the first input box, enter **password** and in the second input box enter the password.

1. For **Encryption key**, select **aws/secretsmanager**, and then choose **Next**.

1. On the **Store a new secret** page, enter a **Secret name**. 

1. (Optional) Enter a **Description** that helps you identify this secret, and then choose **Next**.

1. (Optional) On the **Store a new secret** page, turn on **Automatic rotation**. For more information, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*.

1. Specify a rotation schedule.

1. Choose a Lambda function that can rotate this secret, and then choose **Next**.

1. Review your secret configurations, and then choose **Store**.

To authorize your SiteWise Edge gateway to interact with AWS Secrets Manager, the IAM role for your SiteWise Edge gateway must allow the `secretsmanager:GetSecretValue` action. You can use the **Greengrass core device** to search for the IAM policy. For more information about updating an IAM policy, see [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) in the *AWS Identity and Access Management User Guide*.

**Example policy**  
Replace {{secret-arn}} with the Amazon Resource Name (ARN) of the secret that you created in the previous step. For more information about how to get the ARN of a secret, see [Find secrets in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html) in the *AWS Secrets Manager User Guide*.    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement":[
  {
     "Action":[
        "secretsmanager:GetSecretValue"
     ],
     "Effect":"Allow",
     "Resource":[
        "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret/*"
     ]
  }
]
}
```

## Step 2: Deploy secrets to your SiteWise Edge gateway device
<a name="deploy-secrets-ggv2"></a>

You can use the AWS IoT SiteWise console to deploy secrets to your SiteWise Edge gateway.

**To deploy a secret (console)**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Gateways**.

1. From the **Gateways** list, choose the target SiteWise Edge gateway.

1. In the **Gateway configuration** section, choose the **Greengrass core device** link to open the AWS IoT Greengrass core associated with the SiteWise Edge gateway.

1. In the navigation pane, choose **Deployments**.

1. Choose the target deployment, and then choose **Revise**.

1. On the **Specify target** page, choose **Next**.

1. On the **Select components** page, in the **Public components** section, turn off **Show only selected components**.

1. Search for and choose the **aws.greengrass.SecretManager** component, and then choose **Next**.

1. From the **Selected components** list, choose the **aws.greengrass.SecretManager** component, and then choose **Configure component**.

1. In the **Configuration to merge** field, add the following JSON object.
**Note**  
Replace {{secret-arn}} with the ARN of the secret that you created in the previous step. For more information about how to get the ARN of a secret, see [Find secrets in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html) in the *AWS Secrets Manager User Guide*.

   ```
   {
   "cloudSecrets":[
     {
        "arn":"{{secret-arn}}"
     }
   ]
   }
   ```

1. Choose **Confirm**.

1. Choose **Next**.

1. On the **Configure advanced settings** page, choose **Next**.

1. Review your deployment configurations, and then choose **Deploy**.

## Step 3: Add authentication configurations
<a name="add-authentication-configurations"></a>

You can use the AWS IoT SiteWise console to add authentication configurations to your SiteWise Edge gateway.

**To add authentication configurations (console)**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. From the **Gateways** list, choose the target SiteWise Edge gateway.

1. From the **Data sources** list, choose the target data source, and then choose **Edit**.

1. On the **Add a data source** page, choose **Advanced configuration**.

1. For **Authentication configuration**, choose the secret that you deployed in the previous step.

1. Choose **Save**.