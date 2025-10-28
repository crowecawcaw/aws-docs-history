# Security

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network
architecture that are built to meet the requirements of the most security-sensitive organizations.

###### Topics

- [Shared responsibility](#shared-responsibility "#shared-responsibility")
- [Amazon EC2 security](#ec2-security "#ec2-security")
- [Enclave security](#enclaves-security "#enclaves-security")
- [Logging API calls with AWS CloudTrail](logging-enclaves-using-cloudtrail.md "logging-enclaves-using-cloudtrail.md")

## Shared responsibility

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security
of the cloud and security in the cloud:

- **Security of the cloud** – AWS is responsible for protecting
  the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services
  that you can use securely. Third-party auditors regularly test and verify the effectiveness of our
  security as part of the [AWS Compliance
  Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to Amazon EC2,
  see [AWS Services in Scope
  by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is determined
  by the AWS service that you use. You are also responsible for other factors including the
  sensitivity of your data, your company’s requirements, and applicable laws and regulations.

## Amazon EC2 security

The AWS Nitro Enclaves parent instance benefits from the standard security features and capabilities of Amazon EC2. The
following documentation helps you understand how to apply the shared responsibility model when using Amazon EC2.
It shows you how to configure Amazon EC2 to meet your security and compliance objectives. You also learn how to use
other AWS services that help you to monitor and secure your Amazon EC2 resources.

- [Infrastructure security in Amazon EC2](../../../AWSEC2/latest/UserGuide/infrastructure-security.md "../../../AWSEC2/latest/UserGuide/infrastructure-security.md")
- [Amazon EC2 and interface VPC endpoints](../../../AWSEC2/latest/UserGuide/interface-vpc-endpoints.md "../../../AWSEC2/latest/UserGuide/interface-vpc-endpoints.md")
- [Resilience in Amazon EC2](../../../AWSEC2/latest/UserGuide/disaster-recovery-resiliency.md "../../../AWSEC2/latest/UserGuide/disaster-recovery-resiliency.md")
- [Data protection in Amazon EC2](../../../AWSEC2/latest/UserGuide/data-protection.md "../../../AWSEC2/latest/UserGuide/data-protection.md")
- [Identity and access management for Amazon EC2](../../../AWSEC2/latest/UserGuide/security-iam.md "../../../AWSEC2/latest/UserGuide/security-iam.md")
- [Amazon EC2 key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md")
- [Amazon EC2 security groups for Linux instances](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md")
- [Update management in Amazon EC2](../../../AWSEC2/latest/UserGuide/update-management.md "../../../AWSEC2/latest/UserGuide/update-management.md")
- [Compliance validation for Amazon EC2](../../../AWSEC2/latest/UserGuide/compliance-validation.md "../../../AWSEC2/latest/UserGuide/compliance-validation.md")

## Enclave security

Nitro Enclaves use the same Nitro Hypervisor technology that provides CPU and memory isolation for Amazon EC2
instances in order to isolate the vCPUs and memory for an enclave from a parent instance. Enclaves provide only
secure local socket connectivity with their parent instance. They have no persistent storage, SSH access, or external
networking. Users cannot SSH into an enclave, and the data and applications inside the enclave cannot be accessed
by the processes, applications, or users (root or admin) of the parent instance.

Nitro Enclaves also supports a cryptographic attestation feature, which allows you to verify an enclave's identity and
ensure that only authorized code is running inside it. Attestation ensures that only authorized enclaves are able to
decrypt sensitive data and perform specific cryptographic operations.

Nitro Enclaves integrates with AWS Key Management Service (KMS). AWS KMS makes it easy for you to create and manage cryptographic keys
and control their use across a wide range of AWS services and in your applications. AWS KMS provides built-in attestation
support that allows you to create condition keys for AWS KMS key policies that include an enclave's
platform configuration registers. This ensures that only authorized enclaves are able to perform cryptographic
operations using a specific KMS key.
