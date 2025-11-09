# Considerations

When using AWS Private Certificate Authority with Kubernetes, keep the following considerations in mind.

## Cross-account use of cert-manager

Administrators with cross-account access to a CA can use the `cert-manager`
add on for Kubernetes to provision certificates for a cluster using the shared CA. For
more information, refer to [Security best practices for Cross-account access
to private CAs](pca-resource-sharing.md "pca-resource-sharing.md").

You can use only certain AWS Private CA certificate templates in cross-account
scenarios.

The following table lists AWS Private CA templates that you can use with cert-manager to
provision a Kubernetes cluster.

| Templates supported for Kubernetes                                                                                                                                                            | Support for cross-account use |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [BlankEndEntityCertificate_CSRPassthrough/V1 definition](template-definitions.md#BlankEndEntityCertificate_CSRPassthrough "template-definitions.md#BlankEndEntityCertificate_CSRPassthrough") | No                            |
| [CodeSigningCertificate/V1<br>definition](template-definitions.md#CodeSigningCertificate-V1 "template-definitions.md#CodeSigningCertificate-V1")                                              | No                            |
| [EndEntityCertificate/V1<br>definition](template-definitions.md#EndEntityCertificate-V1 "template-definitions.md#EndEntityCertificate-V1")                                                    | Yes                           |
| [EndEntityClientAuthCertificate/V1 definition](template-definitions.md#EndEntityClientAuthCertificate-V1 "template-definitions.md#EndEntityClientAuthCertificate-V1")                         | Yes                           |
| [EndEntityServerAuthCertificate/V1 definition](template-definitions.md#EndEntityServerAuthCertificate-V1 "template-definitions.md#EndEntityServerAuthCertificate-V1")                         | Yes                           |
| [OCSPSigningCertificate/V1<br>definition](template-definitions.md#OCSPSigningCertificate-V1 "template-definitions.md#OCSPSigningCertificate-V1")                                              | No                            |
