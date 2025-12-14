# Infrastructure security

and compliance validation

The following sections provide information about these key security
concepts for AWS IoT Wireless.

###### Topics

- [Compliance validation for AWS IoT Wireless](#compliance-validation "#compliance-validation")
- [Resilience in AWS IoT Wireless](#disaster-recovery-resiliency "#disaster-recovery-resiliency")
- [Infrastructure security in AWS IoT Wireless](#infrastructure-security "#infrastructure-security")

## Compliance validation for AWS IoT Wireless

Third-party auditors assess the security and compliance of AWS IoT Wireless as part of
multiple AWS compliance programs. These include SOC, PCI, FedRAMP, HIPAA, and
others.

For a list of AWS services in scope of specific compliance programs, see [AWS Services
in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/"). For general information, see
[AWS Compliance
Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more information,
see [Downloading Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using AWS IoT Wireless is determined by the sensitivity of
your data, your company's compliance objectives, and applicable laws and regulations.
AWS provides the following resources to help with compliance:

- [Security and Compliance Quick Start Guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance "https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance") – These deployment guides discuss architectural
  considerations and provide steps for deploying security- and compliance-focused baseline environments on
  AWS.
- [HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/ "https://aws.amazon.com/compliance/hipaa-eligible-services-reference/") –
  Lists HIPAA eligible services. Not all AWS services are HIPAA eligible.
- [AWS Compliance
  Resources](https://aws.amazon.com/compliance/resources/ "https://aws.amazon.com/compliance/resources/") – This collection of workbooks and guides might apply to
  your industry and location.
- [Evaluating
  Resources with Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") in the _AWS Config Developer Guide_ – AWS Config;
  assesses how well your resource configurations comply with internal practices, industry guidelines,
  and regulations.
- [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") – This AWS service provides a comprehensive view of
  your security state within AWS that helps you check your compliance with security
  industry standards and best practices.

## Resilience in AWS IoT Wireless

The AWS global infrastructure is built around AWS Regions and Availability Zones. Regions
provide multiple physically separated and isolated Availability Zones, which are connected through
low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can
design and operate applications and databases that automatically fail over between zones without
interruption. Availability Zones are more highly available, fault tolerant, and scalable than
traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

## Infrastructure security in AWS IoT Wireless

As a managed service, AWS IoT Wireless is protected by the AWS global network security
procedures that are described in the [Amazon Web Services:
Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access AWS IoT Wireless through the network. Clients must
support Transport Layer Security (TLS) 1.0 or later. We recommend TLS 1.2 or later. Clients
must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed using an access key ID and a secret access key that
is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.
