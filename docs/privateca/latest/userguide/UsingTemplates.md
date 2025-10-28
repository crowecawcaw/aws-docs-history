# Use AWS Private CA certificate templates

AWS Private CA uses configuration templates to issue both CA certificates and end-entity
certificates. When you issue a CA certificate from the PCA console, the appropriate root or
subordinate CA certificate template is applied automatically.

If you use the CLI or API to issue a certificate, you can supply a template ARN as a
parameter to the `IssueCertificate` action. If you provide no ARN, then the
`EndEntityCertificate/V1` template is applied by default. For more
information, see the [IssueCertificate](../APIReference/API_IssueCertificate.md "../APIReference/API_IssueCertificate.md") API and [issue-certificate](../../../cli/latest/reference/acm-pca/issue-certificate.md "../../../cli/latest/reference/acm-pca/issue-certificate.md") command documentation.

###### Note

AWS Certificate Manager (ACM) users with cross-account shared access to a private CA can issue
managed certificates that are signed by the CA. Cross-account issuers are constrained
by a resource-based policy and have access only to the
following end-entity certificate templates:

- [EndEntityCertificate/V1](template-definitions.md#EndEntityCertificate-V1 "template-definitions.md#EndEntityCertificate-V1")
- [EndEntityClientAuthCertificate/V1](template-definitions.md#EndEntityClientAuthCertificate-V1 "template-definitions.md#EndEntityClientAuthCertificate-V1")
- [EndEntityServerAuthCertificate/V1](template-definitions.md#EndEntityServerAuthCertificate-V1 "template-definitions.md#EndEntityServerAuthCertificate-V1")
- [BlankEndEntityCertificate_APIPassthrough/V1](template-definitions.md#BlankEndEntityCertificate_APIPassthrough "template-definitions.md#BlankEndEntityCertificate_APIPassthrough")
- [BlankEndEntityCertificate_APICSRPassthrough/V1](template-definitions.md#BlankEndEntityCertificate_APICSRPassthrough "template-definitions.md#BlankEndEntityCertificate_APICSRPassthrough")
- [SubordinateCACertificate_PathLen0/V1](template-definitions.md#SubordinateCACertificate_PathLen0-V1 "template-definitions.md#SubordinateCACertificate_PathLen0-V1")
  For more information, see [Resource-based policies](pca-rbp.md "pca-rbp.md").

###### Topics

- [AWS Private CA template varieties](template-varieties.md "template-varieties.md")
- [AWS Private CA template order of operations](template-order-of-operations.md "template-order-of-operations.md")
- [AWS Private CA template definitions](template-definitions.md "template-definitions.md")
