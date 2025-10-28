# Certificate authorities in AWS Private CA

Using AWS Private Certificate Authority, you can create an entirely AWS hosted hierarchy of root and
subordinate certificate authorities (CAs) for internal use by your organization. To manage
certificate revocation, you can enable Online Certificate Status Protocol (OCSP),
certificate revocation lists (CRLs), or both. AWS Private CA stores and manages your CA
certificates, CRLs, and OCSP responses, and the private keys for your root authorities are
securely stored by AWS.

###### Note

The OCSP implementation in AWS Private CA does not support OCSP request extensions. If you
submit an OCSP batch query containing multiple certificates, the AWS OCSP responder
processes only the first certificate in the queue and drops the others. A revocation
might take up to an hour to appear in OCSP responses.

You can access AWS Private CA using the AWS Management Console, the AWS CLI, and the AWS Private CA API. The
following topics show you how to use the console and the CLI. To learn more about the API,
see the [AWS Private Certificate Authority API Reference](../APIReference.md "../APIReference.md"). For Java examples that show you how to use the API, see [Use AWS Private CA with the AWS SDK for Java](PcaApiIntro.md "PcaApiIntro.md").

After you create an active private CA and configured access to it, you can issue and retrieve certificates, as described in [Issue and manage certificates in AWS Private CA](PcaUsing.md "PcaUsing.md").

###### Topics

- [Set up to use AWS Private CA](setup-aws.md "setup-aws.md")
- [Create a private CA in AWS Private CA](create-CA.md "create-CA.md")
- [Installing the CA certificate](PCACertInstall.md "PCACertInstall.md")
- [Control access to the private CA](granting-ca-access.md "granting-ca-access.md")
- [List private CAs](list-CAs.md "list-CAs.md")
- [View a private CA](describe-CA.md "describe-CA.md")
- [Add tags for your private CA](PcaCaTagging.md "PcaCaTagging.md")
- [Understand AWS Private CA CA status](PcaUpdateStatus.md "PcaUpdateStatus.md")
- [Update a private CA in AWS Private Certificate Authority](PCAUpdateCA.md "PCAUpdateCA.md")
- [Delete your private CA](PCADeleteCA.md "PCADeleteCA.md")
- [Restore a private CA](PCARestoreCA.md "PCARestoreCA.md")
- [Use externally signed private CA certificates](PcaExternalRoot.md "PcaExternalRoot.md")
