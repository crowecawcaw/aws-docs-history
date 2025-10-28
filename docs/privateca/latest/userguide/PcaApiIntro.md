# Use AWS Private CA with the AWS SDK for Java

You can use the AWS Private Certificate Authority API to programmatically interact with the service by sending
HTTP requests. The service returns HTTP responses. For more information see [AWS Private Certificate Authority API Reference](../APIReference.md "../APIReference.md").

In addition to the HTTP API, you can use the AWS SDKs and command line tools to interact
with AWS Private CA. This is recommended over the HTTP API. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/"). The following topics show you
how to use the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/") to program the
AWS Private CA API.

The [GetCertificateAuthorityCsr](JavaApi-GetCertificateAuthorityCsr.md "JavaApi-GetCertificateAuthorityCsr.md"),
[GetCertificate](JavaApi-GetCertificate.md "JavaApi-GetCertificate.md"), and [DescribeCertificateAuthorityAuditReport](JavaApi-DescribeCertificateAuthorityAuditReport.md "JavaApi-DescribeCertificateAuthorityAuditReport.md") operations support waiters. You can use
waiters to control the progression of your code based on the presence or state of certain
resources. For more information, see the following topics, as well as [Waiters in the
AWS SDK for Java](https://aws.amazon.com/blogs/developer/waiters-in-the-aws-sdk-for-java/ "https://aws.amazon.com/blogs/developer/waiters-in-the-aws-sdk-for-java/") in the [AWS
Developer Blog](https://aws.amazon.com/blogs/developer/ "https://aws.amazon.com/blogs/developer/").
