

# Security and permissions
<a name="mes-security"></a>

Managed external secrets does not require you to share admin-level privileges of your third party application accounts with AWS. Instead, the rotation process uses credentials and metadata you provide to make authorized API calls to the third party application for credential updates and validation.

Managed external secrets maintain the same security standards as other Secrets Manager secret types. Secret values are encrypted at rest using your KMS keys and in transit using TLS. Access to secrets is controlled through IAM policies and resource-based policies. When using a Customer Managed Key to encrypt your secret, you will need to update the IAM policy of the rotation role and CMK trust policy to provide the required permissions to ensure successful rotation.

For rotation to function properly, you must provide Secrets Manager with specific permissions to manage the secret lifecycle. These permissions can be scoped to individual secrets and follow the principle of least privilege. The rotation role you provide is validated during setup and used exclusively for rotation operations.

You can restrict the IP ingress to your external resource by only allowing the Secrets Manager managed external secrets [AWS-managed prefix list](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html) in the region where your secret exists. The prefix list is named `com.amazonaws.{{region}}.secretsmanager-managed-external-secrets`, where {{region}} is the AWS Region of your secret. Using the managed prefix list ensures your ingress rules automatically stay current as the underlying IP ranges change.

If you prefer to reference the prefix list programmatically, you can use the [GetManagedPrefixListEntries](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetManagedPrefixListEntries.html) API to list the IPs that need to be allowlisted. You should periodically refresh your ingress rules with this prefix list to keep them current.

 AWS Secrets Manager also offers single touch solutions to create the IAM policy with the permissions necessary to manage the secret when creating the secret through the Secrets Manager console. The permissions for this role are scoped down for each integration partner in each region.

**Example Permissions Policy:**

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowRotationAccess",
      "Action": [
        "secretsmanager:DescribeSecret",
        "secretsmanager:GetSecretValue",
        "secretsmanager:PutSecretValue",
        "secretsmanager:UpdateSecretVersionStage"
      ],
      "Resource": "*",
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "secretsmanager:resource/Type": "{{SalesforceClientSecret}}"
        }
      }
    },
    {
      "Sid": "AllowPasswordGenerationAccess",
      "Action": [
        "secretsmanager:GetRandomPassword"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
```

Note: The list of secret types that are available for secretsmanager:resource/Type can be found in [Integration Partners](mes-partners.md).

**Example Trust Policy:**

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "SecretsManagerPrincipalAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "secretsmanager.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{111122223333}}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:secretsmanager:us-east-1:{{111122223333}}:secret:*"
        }
      }
    }
  ]
}
```