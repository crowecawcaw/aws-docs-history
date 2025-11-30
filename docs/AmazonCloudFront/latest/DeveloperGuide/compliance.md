# Compliance validation for Amazon CloudFront

Third-party auditors assess the security and compliance of Amazon CloudFront as part of
multiple AWS compliance programs. These include SOC, PCI, HIPAA, and others.

For a list of AWS services in scope of specific compliance programs, see [AWS Services in Scope by Compliance
Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/"). For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more information, see
[Downloading
Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using CloudFront is determined by the sensitivity
of your data, your company’s compliance objectives, and applicable laws and regulations.
AWS provides the following resources to help with compliance:

- [Security and Compliance Quick Start Guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance "https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance") – These deployment
  guides discuss architectural considerations and provide steps for deploying
  security- and compliance-focused baseline environments on AWS.
- [Architecting for HIPAA Security and Compliance on AWS](../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.md "../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.md") –
  This whitepaper describes how companies can use AWS to create HIPAA-compliant
  applications.

The AWS HIPAA compliance program includes CloudFront (excluding content delivery through CloudFront
Embedded POPs) as a HIPAA eligible service. If you have an executed Business
Associate Addendum (BAA) with AWS, you can use CloudFront (excluding content delivery
through CloudFront Embedded POPs) to deliver content that contains protected health
information (PHI). For more information, see [HIPAA Compliance.](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/")

- [AWS Compliance
  Resources](https://aws.amazon.com/compliance/resources/ "https://aws.amazon.com/compliance/resources/") – This collection of workbooks and guides might apply
  to your industry and location.
- [AWS Config](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") – This AWS service assesses how well your resource
  configurations comply with internal practices, industry guidelines, and
  regulations.
- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") – This AWS service uses security controls to
  evaluate resource configurations and security standards to help you comply with
  various compliance frameworks. For more information about using Security Hub to evaluate
  CloudFront resources, see [Amazon CloudFront controls](../../../securityhub/latest/userguide/cloudfront-controls.md "../../../securityhub/latest/userguide/cloudfront-controls.md") in the _AWS Security Hub User
  Guide_.

## CloudFront compliance best practices

This section provides best practices and recommendations for compliance when you use
Amazon CloudFront to serve your content.

If you run PCI-compliant or HIPAA-compliant workloads that are based on the [AWS shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), we recommend that you log your CloudFront usage data for the
last 365 days for future auditing purposes. To log usage data, you can do the
following:

- Enable CloudFront access logs. For more information, see [Access logs (standard logs)](AccessLogs.md "AccessLogs.md").
- Capture requests that are sent to the CloudFront API. For more information, see
  [Logging Amazon CloudFront API calls using AWS CloudTrail](logging_using_cloudtrail.md "logging_using_cloudtrail.md").

In addition, see the following for details about how CloudFront is compliant with the PCI
DSS and SOC standards.

### Payment Card Industry Data Security Standard (PCI DSS)

CloudFront (excluding content delivery through CloudFront Embedded POPs) supports the processing,
storage, and transmission of credit card data by a merchant or service provider, and
has been validated as being compliant with Payment Card Industry (PCI) Data Security
Standard (DSS). For more information about PCI DSS, including how to request a copy
of the AWS PCI Compliance Package, see [PCI DSS Level 1](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/").

As a security best practice, we recommend that you don't cache credit card
information in CloudFront edge caches. For example, you can configure your origin to
include a
`Cache-Control:no-cache="``field-name``"`
header in responses that contain credit card information, such as the last four
digits of a credit card number and the card owner's contact information.

### System and Organization Controls (SOC)

CloudFront (excluding content delivery through CloudFront Embedded POPs) is compliant with System and
Organization Controls (SOC) measures, including SOC 1, SOC 2, and SOC 3. SOC reports
are independent, third-party examination reports that demonstrate how AWS achieves
key compliance controls and objectives. These audits ensure that the appropriate
safeguards and procedures are in place to protect against risks that might affect
the security, confidentiality, and availability of customer and company data. The
results of these third-party audits are available on the [AWS SOC Compliance website](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/"),
where you can view the published reports to get more information about the controls
that support AWS operations and compliance.
