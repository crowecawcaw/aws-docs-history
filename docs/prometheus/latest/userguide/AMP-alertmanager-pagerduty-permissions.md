

# Configure AWS Secrets Manager and permissions
<a name="AMP-alertmanager-pagerduty-permissions"></a>

Before you can send alerts to PagerDuty, you must securely store your PagerDuty integration key and configure the necessary permissions. This process involves creating a secret in AWS Secrets Manager, encrypting it with a customer-managed AWS Key Management Service (AWS KMS) key, and granting Amazon Managed Service for Prometheus the required permissions to access both the secret and its encryption key. The following procedures guide you through each step of this configuration process. 

**To create a secret in Secrets Manager for PagerDuty**  
To use PagerDuty as an alert receiver, you must store your PagerDuty integration key in Secrets Manager. Follow these steps:

1. Open the [Secrets Manager console](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. For **Secret type**, choose **Other type of secret**.

1. For **Key/value pairs**, enter your PagerDuty integration key as the secret value. This is either the routing key or service key from your PagerDuty integration.

1. Choose **Next**.

1. Enter a name and description for your secret, then choose **Next**.

1. Configure rotation settings if desired, then choose **Next**.

1. Review your settings and choose **Store**.

1. After creating the secret, note its ARN. You'll need this when configuring the alert manager.

**To encrypt your secret with a customer-managed AWS KMS key**

You must grant Amazon Managed Service for Prometheus permission to access your secret and its encryption key:

1. **Secret resource policy**: Open your secret in the [Secrets Manager console](https://console.aws.amazon.com/secretsmanager/).

   1. Choose **Resource permissions**.

   1. Choose **Edit permissions**.

   1. Add the following policy statement. In the statement, replace the {{highlighted values}} with your specific values.

      ```
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "aps.amazonaws.com"
        },
        "Action": "secretsmanager:GetSecretValue",
        "Resource": "*",
        "Condition": {
          "ArnEquals": {
            "aws:SourceArn": "arn:aws:aps:{{aws-region}}:{{123456789012}}:workspace/{{WORKSPACE_ID}}"
          },
          "StringEquals": {
            "aws:SourceAccount": "{{123456789012}}"
          }
        }
      }
      ```

   1. Choose **Save**.

1. **KMS key policy**: Open your AWS KMS key in the [AWS KMS console](https://console.aws.amazon.com/kms).

   1. Choose **Key policy**.

   1. Choose **Edit**.

   1. Add the following policy statement. In the statement, replace the {{highlighted values}} with your specific values.

      ```
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "aps.amazonaws.com"
        },
        "Action": "kms:Decrypt",
        "Resource": "*",
        "Condition": {
          "ArnEquals": {
            "aws:SourceArn": "arn:aws:aps:{{aws-region}}:{{123456789012}}:workspace/{{WORKSPACE_ID}}"
          },
          "StringEquals": {
            "aws:SourceAccount": "{{123456789012}}"
          }
        }
      }
      ```

   1. Choose **Save**.

**Next steps** – Continue to the next topic, [Configure alert manager to send alerts to PagerDuty](AMP-alertmanager-pagerduty-configure-alertmanager.md).