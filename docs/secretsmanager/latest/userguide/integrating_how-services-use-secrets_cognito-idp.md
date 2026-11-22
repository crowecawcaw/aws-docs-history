

# How Amazon Cognito uses AWS Secrets Manager

With Amazon Cognito, you can add authentication, authorization, and user management to your web and mobile apps. Amazon Cognito integrates with Secrets Manager to manage client secrets for your user pool app clients, enhancing security and simplifying credential management.

When you turn on managed secrets for an app client, Amazon Cognito stores its client secret in a [managed secret](service-linked-secrets.md) with the prefix `cognito-idp`. It creates, rotates, and deletes the secret. By default, it rotates the secret every 7 days with [managed rotation](rotate-secrets_managed.md), so you don't need a Lambda rotation function. Your app reads the current client secret from Secrets Manager. If your user pool has replicas in other AWS Regions, Amazon Cognito also replicates the secret to those Regions. Standard Secrets Manager charges apply. For pricing, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing). For more information about managed app client secrets, see [Managing app client secrets with AWS Secrets Manager](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html#user-pool-settings-client-apps-asm-managed-secrets) in the *Amazon Cognito Developer Guide*.

**Important**  
To stop storing an app client secret in Secrets Manager, turn off managed secrets for the app client in Amazon Cognito. Don't delete the secret in Secrets Manager. If you delete it, your apps can't read the client secret.