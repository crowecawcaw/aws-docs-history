# Preventive controls that assist with digital

sovereignty

These preventive controls are designed to assist you with your digital sovereignty
governance posture.

This group of controls helps you comply with digital sovereignty regulatory requirements because
they prevent actions, enforce configurations, and detect resource changes that affect data
residency, granular access restriction, encryption, and resilience capabilities.

- These controls are configurable. For more information about configurable controls, see [Controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
- These are optional controls with Preventive guidance, implemented with AWS service
  control policies (SCPs). They are not deployed on any OU by default. You can enable them
  through the AWS Control Tower console, or through the AWS Control Tower [APIs](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
  In the AWS Control Tower console, you can view these controls together under the
  **Groups** tab on the **Categories** page.

###### Topics

- [[CT.APPSYNC.PV.1] Require an AWS AppSync GraphQL API to be configured with private visibility](ct-appsync-pv-1.md "ct-appsync-pv-1.md")
- [[CT.EC2.PV.1] Require an Amazon EBS snapshot to be created from an encrypted EC2 volume](ct-ec2-pv-1.md "ct-ec2-pv-1.md")
- [[CT.EC2.PV.2] Require that an attached Amazon EBS volume is configured to encrypt data at rest](ct-ec2-pv-2.md "ct-ec2-pv-2.md")
- [[CT.EC2.PV.3] Require that an Amazon EBS snapshot cannot be publicly restorable](ct-ec2-pv-3.md "ct-ec2-pv-3.md")
- [[CT.EC2.PV.4] Require that Amazon EBS direct APIs are not called](ct-ec2-pv-4.md "ct-ec2-pv-4.md")
- [[CT.EC2.PV.5] Disallow the use of Amazon EC2 VM import and export](ct-ec2-pv-5.md "ct-ec2-pv-5.md")
- [[CT.EC2.PV.6] Disallow the use of deprecated Amazon EC2 RequestSpotFleet and RequestSpotInstances API actions](ct-ec2-pv-6.md "ct-ec2-pv-6.md")
- [[CT.KMS.PV.1] Require an AWS KMS key policy to have a statement that limits creation of AWS KMS grants to AWS services](ct-kms-pv-1.md "ct-kms-pv-1.md")
- [[CT.KMS.PV.2] Require that an AWS KMS asymmetric key with RSA key material used for encryption does not have a key length of 2048 bits](ct-kms-pv-2.md "ct-kms-pv-2.md")
- [[CT.KMS.PV.3] Require that an AWS KMS key is configured with the bypass policy lockout safety check enabled](ct-kms-pv-3.md "ct-kms-pv-3.md")
- [[CT.KMS.PV.4] Require that an AWS KMS customer-managed key (CMK) is configured with key material originating from AWS CloudHSM](ct-kms-pv-4.md "ct-kms-pv-4.md")
- [[CT.KMS.PV.5] Require that an AWS KMS customer-managed key (CMK) is configured with imported key material](ct-kms-pv-5.md "ct-kms-pv-5.md")
- [[CT.KMS.PV.6] Require that an AWS KMS customer-managed key (CMK) is configured with key material originating from an external key store (XKS)](ct-kms-pv-6.md "ct-kms-pv-6.md")
- [[CT.LAMBDA.PV.1] Require an AWS Lambda function URL to use AWS IAM-based authentication](ct-lambda-pv-1.md "ct-lambda-pv-1.md")
- [[CT.LAMBDA.PV.2] Require an AWS Lambda function or AWS Lambda function URL to be configured for access only to principals within your AWS account](ct-lambda-pv-2.md "ct-lambda-pv-2.md")
