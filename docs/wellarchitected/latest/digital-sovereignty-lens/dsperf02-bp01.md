# DSPERF02-BP01 Implement confidential computing technologies for

data protection during processing

Confidential computing technology extends traditional security
models for highly regulated industries. It protects sensitive data
not just at rest and in transit, but also during processing by using
hardware-enforced isolated runtime environments. This enhanced
protection addresses critical security gaps by blocking unauthorized
access, including from privileged users and cloud providers.

**Desired outcome:** Protect
sensitive data during processing through hardware-enforced
isolation. Maintain cryptographic isolation of sensitive data while
enabling secure computation.

**Common anti-patterns:**

- Running highly-confidential workloads on regular EC2 instances
  without considering hardware-enforced isolation and encryption,
  and secure enclaves.
- Underestimating CPU and memory requirements and granting
  excessive IAM permissions to applications handling sensitive
  data.
- Failing to properly validate enclave attestation documents and
  overlooking proper key management practices.
- Not properly segregating confidential data flows and allowing
  unrestricted network access without proper controls.

**Benefits of establishing this best
practice:**

- Block unauthorized access to sensitive data, including from
  privileged users and cloud operators, through cryptographic
  isolation.
- Meet stringent data protection requirements with verifiable
  evidence of data isolation and protection.
- Process data collaboratively across organizational boundaries
  while maintaining complete confidentiality.
- Minimize potential breach points through hardware-enforced
  isolation and limited system access.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Identify sensitive workloads requiring confidential computing
protection. Implement AWS Nitro Enclaves with proper isolation,
and design architectures that separate confidential processing
from general application logic and maintain comprehensive security
controls.

Key steps include:

- Assess workloads for confidential computing suitability and
  regulatory compliance requirements
- Design and implement enclave architecture with proper resource
  allocation, network isolation, and attestation verification
- Configure end-to-end encryption using AWS KMS or CloudHSM with
  secure communication protocols
- Establish comprehensive monitoring, logging, and incident
  response procedures while maintaining confidentiality
- Implement strict IAM policies and access controls for enclave
  interactions using least privilege principles

## Implementation steps

1. Catalog sensitive data workflows and identify workloads
   requiring data-in-use protection, then select appropriate
   [Amazon EC2](../../../ec2/latest/devguide/ec2-api-intro.md "../../../ec2/latest/devguide/ec2-api-intro.md") instance types supporting
   [AWS Nitro Enclaves](../../../enclaves/latest/user/enclaves-user.md "../../../enclaves/latest/user/enclaves-user.md") with
   [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") network segmentation to properly isolate
   confidential processing from general application logic and
   adhere to regulatory requirements.
2. Configure
   [AWS KMS](../../../kms.md "../../../kms.md") keys with enclave-specific policies and
   [AWS CloudHSM](../../../cloudhsm.md "../../../cloudhsm.md") for additional key protection, combined with
   [AWS Certificate Manager](../../../acm.md "../../../acm.md") for encryption and secure
   communication channels to establish end-to-end encryption that
   protects data while it's being processed within the enclave
   environment.
3. Build
   [AWS Nitro Enclaves](../../../enclaves/latest/user/enclaves-user.md "../../../enclaves/latest/user/enclaves-user.md") images using the
   **Nitro Enclaves SDK** with
   proper attestation mechanisms, then deploy comprehensive
   monitoring through
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"),
   [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), and
   [AWS Systems Manager](../../../systems-manager.md "../../../systems-manager.md") to track and maintain enclave
   operations while preserving confidentiality of the processed
   data.
4. Implement strict
   [AWS IAM](../../../iam.md "../../../iam.md") roles and policies with
   [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") for role-based access control using least
   privilege principles, then validate security posture using
   [AWS Security Hub](../../../securityhub.md "../../../securityhub.md"),
   [AWS Audit Manager](../../../audit-manager.md "../../../audit-manager.md")
   [AWS Inspector](../../../inspector.md "../../../inspector.md") to control enclave interactions and meet
   regulatory requirements.

## Resources

**Related best practices:**

- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")
- [SEC08-BP02
  Enforce encryption at rest](../security-pillar/sec_protect_data_rest_encrypt.md "../security-pillar/sec_protect_data_rest_encrypt.md")
- [SEC05-BP02
  Control traffic at all layers](../security-pillar/sec_network_protection_layered.md "../security-pillar/sec_network_protection_layered.md")
- [PERF02-BP01
  Select the best compute options for your workload](../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md "../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md")

**Related documents:**

- [AWS Nitro Enclaves Documentation](../../../enclaves/latest/user/nitro-enclave.md "../../../enclaves/latest/user/nitro-enclave.md")
- [AWS Confidential Computing](https://aws.amazon.com/confidential-computing/ "https://aws.amazon.com/confidential-computing/")
- [AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md")
- [AWS Security Blog - Confidential Computing](https://aws.amazon.com/blogs/security/tag/confidential-computing/ "https://aws.amazon.com/blogs/security/tag/confidential-computing/")
- [AWS Nitro Enclaves – Isolated EC2 Environments to Process
  Confidential Data](https://aws.amazon.com/blogs/aws/aws-nitro-enclaves-isolated-ec2-environments-to-process-confidential-data/ "https://aws.amazon.com/blogs/aws/aws-nitro-enclaves-isolated-ec2-environments-to-process-confidential-data/")

**Related videos:**

- [AWS Nitro Enclaves Overview](https://www.youtube.com/watch?v=tRL7Y0mJqU4 "https://www.youtube.com/watch?v=tRL7Y0mJqU4")
- [Protecting
  Sensitive Data with AWS Confidential Computing: Nitro System
  and Enclaves](https://aws.amazon.com/awstv/watch/e80ad59b24d/ "https://aws.amazon.com/awstv/watch/e80ad59b24d/")
- [AWS re:Invent 2024 - Dive deep into the AWS Nitro System
  (CMP301)](https://www.youtube.com/watch?v=YKZbNcOU77c "https://www.youtube.com/watch?v=YKZbNcOU77c")
- [AWS Nitro Enclaves - Getting Started Video](https://www.youtube.com/watch?v=t-XmYt2z5S8 "https://www.youtube.com/watch?v=t-XmYt2z5S8")

**Related services:**

- [AWS Nitro Enclaves](../../../enclaves/latest/user/nitro-enclave.md "../../../enclaves/latest/user/nitro-enclave.md")
- [AWS KMS](../../../kms.md "../../../kms.md")
- [AWS CloudHSM](../../../cloudhsm.md "../../../cloudhsm.md")
- [Amazon EC2](../../../ec2.md "../../../ec2.md")
