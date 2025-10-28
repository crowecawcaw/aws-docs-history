# Use AWS Secrets Manager for data protection for C2C workflows

AWS Secrets Manager is a secret storage service that you can use to protect database credentials, API keys, and other secret information. Then in your code,
you can replace hardcoded credentials with an API call to Secrets Manager. This helps ensure that the secret can't be compromised by someone examining your code,
because the secret isn't there. For an overview, see the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

Secrets Manager encrypts secrets using AWS Key Management Service keys. For more information, see [Secret encryption and decryption in AWS Key Management Service](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

Managed integrations for AWS IoT Device Management integrates with AWS Secrets Manager so that you can store your data in Secrets Manager and use the secret ID in your configurations.

## How managed integrations uses secrets

Open Authorization (OAuth) is an open standard for delegated access authorization, enabling users to grant websites or applications
access to their information on other websites without sharing their passwords. It's a secure way for third-party applications to access user
data on behalf of the user, providing a more secure alternative to sharing passwords.

In OAuth, a client ID and client secret are credentials that identify and authenticate a client application when it requests an access token.

Managed integrations for AWS IoT Device Management uses OAuth to communicate with customers that use the C2C workflows. Customers need to provide the client ID and client secret to communicate.
Managed integrations customers will store a client ID and client secret in their AWS accounts, and managed integrations reads the client ID and client secret in our customer account.

## How to create a secret

To create a secret, follow the steps in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager User Guide.

You must create your secret with a customer-managed AWS KMS key for managed integrations to read the secret value. For more information, see
[Permissions for the AWS KMS key](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz") in the AWS Secrets Manager User Guide.

You must also use the IAM policies in the following section.

## Grant access for managed integrations for AWS IoT Device Management to retrieve the secret

To allow managed integrations to retrieve the secret value from Secrets Manager, include the following permissions in the resource policy for the secret when you create it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [ {
 "Effect" : "Allow",
 "Principal" : {
 "Service" : "iotmanagedintegrations.amazonaws.com"
 },
 "Action" : [ "secretsmanager:GetSecretValue" ],
 "Resource" : "*" ,
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:iotmanagedintegrations:`AWS Region`:`account-id`:account-association:`account-association-id`"

 }
 }
 } ]
}`

```

Add the following statement to the policy for your customer-managed AWS KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Principal": {
 "Service": [
 "iotmanagedintegrations.amazonaws.com"
 ]
 },
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/*"
 ]
 }

 ]
}`

```
