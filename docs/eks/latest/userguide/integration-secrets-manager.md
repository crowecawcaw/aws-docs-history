**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage application secrets with AWS Secrets Manager

[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/") helps you manage, access, and rotate credentials, API keys, and other secrets throughout their lifecycle.
With Secrets Manager, you can secure and manage secrets used to access resources in AWS, on third-party services, and on-premises.
For more information, see the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

When using the EKS Capability for Argo CD, Secrets Manager provides a secure way to store and retrieve Git repository credentials without hardcoding sensitive data in your Argo CD configuration and resources.
This integration is particularly useful for managing private repository access tokens and SSH keys used by Argo CD to sync applications from Git repositories.

## Use AWS Secrets Manager with Argo CD

When using the EKS Capability for Argo CD, you can store Git repository credentials in Secrets Manager and configure Argo CD to retrieve them.
This approach is more secure than storing credentials directly in Argo CD configuration or using long-lived personal access tokens.

**Prerequisites**

- An Amazon EKS cluster with the Argo CD capability enabled
- Git repository credentials stored in AWS Secrets Manager
- IAM permissions configured for Argo CD to access Secrets Manager

**To configure Argo CD to use Secrets Manager for repository credentials**

1. Store your Git credentials in Secrets Manager. For example, to store a GitHub personal access token:

```
aws secretsmanager create-secret \
  --name argocd/github-token \
  --secret-string '{"username":"git","password":"ghp_xxxxxxxxxxxx"}'
```

2. Ensure the Argo CD capability role has permissions to retrieve the secret:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "arn:aws:secretsmanager:region:account-id:secret:argocd/github-token*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:region:account-id:key/*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:region:account-id:secret:argocd/*",
          "kms:ViaService": "secretsmanager.*.amazonaws.com"
        }
      }
    }
  ]
}
```

###### Note

The KMS decrypt permission is required because Secrets Manager encrypts all secrets using AWS KMS.
The condition restricts decryption to only secrets with the `argocd/` prefix.
If you use the default AWS managed key for Secrets Manager, this permission is sufficient.
For customer managed KMS keys, update the `Resource` field with your specific key ARN. 3. Configure Argo CD to use the credentials from Secrets Manager. For information about syncing secrets from Secrets Manager into Kubernetes secrets that Argo CD can reference, see [Secret Management](https://argo-cd.readthedocs.io/en/stable/operator-manual/secret-management/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/secret-management/") in the Argo CD documentation. 4. Create an Argo CD repository configuration that references the secret ARN:

```
apiVersion: v1
kind: Secret
metadata:
  name: private-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/org/repo
  secretArn: arn:aws:secretsmanager:region:account-id:secret:argocd/github-token
```

For more information about configuring repository access with Argo CD, see [Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md").
