# Encrypt Amazon ECS Service Connect traffic

Amazon ECS Service Connect supports automatic traffic encryption with Transport Layer
Security (TLS) certificates for Amazon ECS services. When you point your Amazon ECS services
toward an [AWS Private Certificate Authority (AWS Private CA)](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md"), Amazon ECS automatically provisions TLS certificates to
encrypt traffic between your Amazon ECS Service Connect services. Amazon ECS generates, rotates,
and distributes TLS certificates used for traffic encryption.

Automatic traffic encryption with Service Connect uses industry-leading encryption
capabilities to secure your inter-service communication that helps you meet your
security requirements. It supports AWS Private Certificate Authority TLS certificates with `256-bit
 ECDSA` and `2048-bit RSA` encryption. You also have full control
over private certificates and signing keys to help you meet compliance requirements. By
default, TLS 1.3 is supported, but TLS 1.0 - 1.2 are not supported. Service Connect
supports TLS 1.3 with the following ciphers:

- `TLS_AES_128_GCM_SHA256`
- `TLS_AES_256_GCM_SHA384`
- `TLS_CHACHA20_POLY1305_SHA256`

###### Note

In order to use TLS 1.3, you must enable it on the listener on the target.

Only inbound and outbound traffic passing though the Amazon ECS agent is
encrypted.

## Service Connect and Application Load Balancer

health checks

You can use Service Connect with Application Load Balancer health checks and TLS 1.3 encryption.

### Application Load Balancer configuration

Configure the Application Load Balancer with the following settings:

- Configure a TLS listener with a TLS 1.3 security policy (such as
  `ELBSecurityPolicy-TLS13-1-2-2021-06`). For more information, see [Security policies for your Application Load Balancer](../../../elasticloadbalancing/latest/application/describe-ssl-policies.md "../../../elasticloadbalancing/latest/application/describe-ssl-policies.md").
- Create a target group with the following settings:
  - Set the protocol to HTTPS
  - Attach the target group to the TLS listener
  - Configure the health check port to match your Service Connect
    service's container port

### Service Connect

configuration

Configure a service with the following settings:

- Configure the service to use `awsvpc` network mode, as
  `bridge` network mode is not supported.
- Enable Service Connect for the service.
- Set up the load balancer configuration with the following
  settings:
  - Specify the target group you configured for your Application Load Balancer
  - Set the container port to match the Service Connect TLS
    service's container port

- Avoid setting `ingressPortOverride` for the service. For
  more information, see [ServiceConnectService](../APIReference/API_ServiceConnectService.md "../APIReference/API_ServiceConnectService.md") in the _Amazon Elastic Container Service API Reference_.

### Considerations

Consider the following when using Application Load Balancer, TLS and Service Connect:

- Use `awsvpc` network mode instead of `bridge`
  network mode for HTTPS health checks when using Service Connect with
  TLS encryption. HTTP health checks will continue to work with
  `bridge` mode.
- Configure the target group health check port to match the
  Service Connect service's container port, not the default HTTPS port
  (443).

## AWS Private Certificate Authority certificates and

Service Connect

You need to have the infrastructure IAM role. For more information about this
role, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").

###### AWS Private Certificate Authority modes for Service Connect

AWS Private Certificate Authority can run in two modes: general purpose and short-lived.

- General purpose ‐ Certificates that can be configured with any
  expiration date.
- Short-lived ‐ Certificates with a maximum validity of seven
  days.

While Amazon ECS supports both modes, we recommend using short-lived certificates. By
default, certificates rotate every five days, and running in short-lived mode offers
significant cost savings over general purpose.

Service Connect doesn't support certificate revocation and instead leverages
short-lived certificates with frequent certificate rotation. You have the authority
to modify the rotation frequency, disable, or delete the secrets using [managed
rotation](../../../secretsmanager/latest/userguide/rotate-secrets_managed.md "../../../secretsmanager/latest/userguide/rotate-secrets_managed.md") in [Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"), but doing so can
come with the following possible consequences.

- Shorter Rotation Frequency ‐ A shorter rotation frequency incurs
  higher costs due to AWS Private CA, AWS KMS and Secrets Manager, and Amazon EC2 Auto Scaling experiencing an
  increased workload for rotation.
- Longer Rotation Frequency ‐ Your applications’ communications fail if
  the rotation frequency exceeds **seven**
  days.
- Deletion of Secret ‐ Deleting the secret results in rotation failure
  and impacts customer application communications.

In the event of your secret rotation failing, a `RotationFailed` event
is published in [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"). You can also set up a [CloudWatch
Alarm](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") for `RotationFailed`.

###### Important

Don't add replica Regions to secrets. Doing so prevents Amazon ECS
from deleting the secret, because Amazon ECS doesn't have permission to remove
Regions from replication. If you already added the replication,
run the following command.

```
aws secretsmanager remove-regions-from-replication \
 --secret-id `SecretId` \
 --remove-replica-regions `region-name`
```

###### Subordinate Certificate Authorities

You can bring any AWS Private CA, root or subordinate, to Service Connect TLS to issue
end-entity certificates for the services. The provided issuer is treated as the
signer and root of trust everywhere. You can issue end-entity certificates for
different parts of your application from different subordinate CAs. When using
the AWS CLI, provide the Amazon Resource Name (ARN) of the CA to establish the trust chain.

###### On-premises Certificate Authorities

To use your on-premises CA, you create and configure a subordinate CA in
AWS Private Certificate Authority. This ensures all TLS certificates issued for your Amazon ECS workloads
share the trust chain with the workloads you run on premises and are able to
securely connect.

###### Important

Add the **required** tag `AmazonECSManaged :
 true` in your AWS Private CA.

###### Infrastructure as code

When using Service Connect TLS with Infrastructure as Code (IaC) tools, it's
important to configure your dependencies correctly to avoid issues, such as
services stuck in draining. Your AWS KMS key, if provided, IAM role, and AWS Private CA
dependencies should be deleted after your Amazon ECS service.

If the namespace used for Service Connect is a shared namespace, you can choose
to use a shared AWS Private CA resource. For more information, see [Attach a
policy for cross-account access](../../../privateca/latest/userguide/pca-ram.md "../../../privateca/latest/userguide/pca-ram.md") in the _AWS Private Certificate Authority User
Guide_.

## Service Connect and Secrets Manager

###### When using Amazon ECS Service Connect with TLS encryption, the service interacts

with Secrets Manager in the following ways:

Service Connect utilizes the infrastructure role provided to create secrets
within Secrets Manager. These secrets are used to store the associated private keys for
your TLS certificates for encrypting traffic between your Service Connect
services.

###### Warning

The automatic creation and management of these secrets by Service Connect
streamlines the process of implementing TLS encryption for your services.
However, it's important to be aware of potential security implications. Other
IAM roles that have read access to Secrets Manager may be able to access these
automatically created secrets. This could expose sensitive cryptographic
material to unauthorized parties, if access controls are not properly
configured.

To mitigate this risk, follow these best practices:

- Carefully manage and restrict access to Secrets Manager, especially for secrets
  created by Service Connect.
- Regularly audit IAM roles and their permissions to ensure the
  principle of least privilege is maintained.

When granting read access to Secrets Manager, consider excluding the TLS private keys
created by Service Connect. You can do this by using a condition in your IAM
policies to exclude secrets with ARNs that match the pattern:

```
"arn:aws:secretsmanager:::secret:ecs-sc!"
```

An example IAM policy that denies the `GetSecretValue` action to all secrets with the `ecs-sc!`
prefix:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:*:*:secret:ecs-sc!*"
 }
 ]
}`

```

###### Note

This is a general example and may need to be adjusted based on your specific
use case and AWS account configuration. Always test your IAM policies
thoroughly to ensure they provide the intended access while maintaining
security.

By understanding how Service Connect interacts with Secrets Manager, you can better manage
the security of your Amazon ECS services while leveraging the benefits of automatic TLS
encryption.

## Service Connect and AWS Key Management Service

You can use [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") to encrypt and
decrypt your Service Connect resources. AWS KMS is a service managed by AWS where
you can make and manage cryptographic keys that protect your data.

When using AWS KMS with Service Connect, you can either choose to use an AWS
owned key that AWS manages for you, or you can choose an existing AWS KMS key. You
can also [create a
new AWS KMS key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") to use.

###### Providing your own encryption key

You can provide your own key materials, or you can use an external key store
through AWS Key Management Service Import your own key into AWS KMS, and then specify the Amazon Resource Name (ARN)
of that key in Amazon ECS Service Connect.

The following is an example AWS KMS policy. Replace the `user
 input` values with your own.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`id`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`role-name`"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyPair"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about key policies, see [Creating a key
policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") in the _AWS Key Management Service Developer
Guide_.

###### Note

Service Connect supports only symmetric encryption AWS KMS keys. You can't use
any other type of AWS KMS key to encrypt your Service Connect resources. For help
determining whether a AWS KMS key is a symmetric encryption key, see [Identify asymmetric KMS keys](../../../kms/latest/developerguide/identify-key-types.md#identify-asymm-keys "../../../kms/latest/developerguide/identify-key-types.md#identify-asymm-keys").

For more information on AWS Key Management Service symmetric encryption keys, see [Symmetric
encryption AWS KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") in the _AWS Key Management Service Developer
Guide_.
