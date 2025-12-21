**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Compliance Validation for Amazon Glacier

The security and compliance of Amazon Glacier (Amazon Glacier) is assessed by third-party auditors as part
of multiple AWS compliance programs, including the following:

- System and Organization Controls (SOC)
- Payment Card Industry Data Security Standard (PCI DSS)
- Federal Risk and Authorization Management Program (FedRAMP)
- Health Insurance Portability and Accountability Act (HIPAA)
  AWS provides a frequently updated list of AWS services in scope of specific compliance
  programs at [AWS Services in Scope
  by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

Third-party audit reports are available for you to download using AWS Artifact. For more
information, see [Downloading Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md") in the _AWS Artifact User
Guide_.

For more information about AWS compliance programs, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

Your compliance responsibility when using Amazon Glacier is determined by the sensitivity of your
data, your organization’s compliance objectives, and applicable laws and regulations. If
your use of Amazon Glacier is subject to compliance with standards like HIPAA, PCI, or FedRAMP, AWS
provides resources to help:

- [Amazon Glacier Vault Lock](vault-lock.md "vault-lock.md") allows you to easily
  deploy and enforce compliance controls for individual Amazon Glacier vaults with a vault lock
  policy. You can specify controls such as “write once read many” (WORM) in a vault
  lock policy and lock the policy from future edits. After the policy is locked, it
  can no longer be changed. Vault lock policies can help you comply with regulatory
  frameworks such as SEC17a-4 and HIPAA.
- [Security and Compliance Quick Start Guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance "https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance") discuss architectural
  considerations and steps for deploying security- and compliance-focused baseline
  environments on AWS.
- [Architecting for HIPAA Security and Compliance](../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.md "../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.md") outlines how
  companies use AWS to help them meet HIPAA requirements.
- [The AWS Well-Architected Tool (AWS WA Tool)](../../../wellarchitected/latest/userguide/intro.md "../../../wellarchitected/latest/userguide/intro.md") is a service in the cloud that provides a consistent process for you to review and measure your architecture using AWS best practices. The AWS WA Tool provides recommendations for making your workloads more reliable, secure, efficient, and cost-effective.
- [AWS Compliance Resources](https://aws.amazon.com/compliance/resources/ "https://aws.amazon.com/compliance/resources/")
  provide several different workbooks and guides that might apply to your industry and
  location.
- [AWS Config](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") can help you assess
  how well your resource configurations comply with internal practices, industry
  guidelines, and regulations.
- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") provides
  you with a comprehensive view of your security state within AWS and helps you
  check your compliance with security industry standards and best practices.
