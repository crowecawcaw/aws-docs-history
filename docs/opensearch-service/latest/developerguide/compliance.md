# Compliance validation for Amazon OpenSearch Service

Third-party auditors assess the security and compliance of Amazon OpenSearch Service as part of multiple
AWS compliance programs. These programs include SOC, PCI, and HIPAA.

If you have compliance requirements, consider using any version of OpenSearch or
Elasticsearch 6.0 or later. Earlier versions of Elasticsearch don't offer a combination of
[encryption of data at rest](encryption-at-rest.md "encryption-at-rest.md") and [node-to-node encryption](ntn.md "ntn.md") and are unlikely to meet your needs. You
might also consider using any version of OpenSearch or Elasticsearch 6.7 or later if [fine-grained access control](fgac.md "fgac.md") is important to your use case.
Regardless, choosing a particular OpenSearch or Elasticsearch version when you create a
domain does not guarantee compliance.

To learn whether an AWS service is within the scope of specific compliance programs, see
[AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/") and choose the compliance program that you are
interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more
information, see [Downloading Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using AWS services is determined by the sensitivity
of your data, your company's compliance objectives, and applicable laws and
regulations. For more information about your compliance responsibility when using AWS services, see
[AWS Security Documentation](../../../security.md "../../../security.md").
