# TELCOSEC01-BP02 Encrypt data at-rest and sensitive traffic

(control plane, data plane) using secure VPNs and custom encryption keys

Due to regulatory requirements, the CSPs often need to apply
additional encryption to traffic that is not already secured by the underlying transport or
application protocols. Both control plane traffic, such as Diameter signaling, and data plane
traffic, like voice or RTP, require the use of encrypted virtual private networks (VPNs), most
commonly IPsec. It is crucial for CSPs to evaluate their regulatory landscape and establish a
framework to identify and label the traffic and data that needs to be encrypted in transit as
well as at rest, using customer-owned encryption keys.

The data in-use is protected by the
underlying CPU architecture and features like AMD SEV-SNP, Intel TME, and Graviton Memory
Encryption. However, these security measures come with additional costs and limitations, such as
restrictions on packets per second (PPS) per flow (number of IPsec tunnels), PPS per instance
(lack of equal-cost multi-path routing after reaching the largest single-slot capacity),
complexity, and vendor dependencies.

**Desired outcome:**

- Verify sensitive telco network traffic, including control plane and data plane, is
  encrypted using secure VPN protocols like IPsec.
- Implement a comprehensive data encryption strategy to protect data in transit and
  at rest using customer-managed encryption keys.
- Fulfill regulatory requirements for data protection and secure communications in the
  telco industry.
- Maintain the confidentiality and integrity of critical telco network data and signaling
  traffic, even when traversing the public cloud infrastructure.
- Provide visibility and control over the encryption keys and algorithms used to secure
  the telco workloads.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement a secure, encrypted communication framework for control and data plane traffic
comply with industry standards and regulations. Leverage built-in features for key management,
high availability, and automatic failover. Utilize a centralized key management service to
generate, manage, and rotate encryption keys for securing data in-transit and at-rest across
various systems and services. Verify comprehensive auditing and monitoring of encryption and
key management activities to maintain adherence and provide detailed reporting.

### Implementation steps

- Implement VPN-based encryption for control and data plane traffic:
  - Configure AWS managed VPN solutions, such as Site-to-Site VPN, to establish secure IPsec
    tunnels for control and data plane communications.
  - Use the built-in features of these services for automatic key management,
    tunnel failover, and high availability.
  - Verify the VPN configurations comply with industry standards and regulations
    for secure network communications.

- Encrypt data in-transit using custom keys:
  - Use AWS Key Management Service to generate and manage the encryption keys used to
    secure data in-transit.
  - Integrate KMS with other AWS services, such as Amazon S3, Amazon EBS, and Amazon RDS, to
    transparently encrypt data flowing through these services.
  - Implement a key rotation strategy to maintain the cryptographic strength of the
    encryption keys over time.

- Encrypt data at rest using custom keys:
  - Configure AWS services handling telco data, such as Amazon S3, Amazon EBS, and Amazon RDS,
    to use customer-managed encryption keys from KMS.
  - Verify that sensitive telco data, including logs, metrics, and configuration
    files, is encrypted at rest using the custom encryption keys.
  - Use KMS key policies to control access and usage of the encryption keys,
    aligned with the principle of least privilege.

- Implement key management and rotation:
  - Establish key management processes and procedures for the creation,
    distribution, and rotation of the customer-managed encryption keys.
  - Automate key rotation using AWS Lambda functions or AWS Systems Manager, verifying that
    keys are updated on a regular basis.
  - Integrate the key management processes with the overall security operations and
    incident response procedures.

- Maintain audit trails:
  - Use AWS CloudTrail to create comprehensive audit trails of key management and
    data encryption activities.
  - Configure AWS Config to continuously monitor the configuration of the encryption
    services and report on deviations from the desired state.
  - Integrate the encryption and key management data with the organization's
    security information and event management (SIEM) system for advanced analytics and
    reporting.

## Resources

**Key AWS services:**

- [Site-to-Site VPN](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/")
- [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/")
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/")
- [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
