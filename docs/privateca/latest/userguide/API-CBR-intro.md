# Use AWS Private CA to implement Matter certificates

You can use the AWS Private Certificate Authority API to create certificates that conform to the [Matter connectivity
standard](https://github.com/project-chip/connectedhomeip "https://github.com/project-chip/connectedhomeip"). Matter specifies certificate configurations that improve the security
and consistency of internet of things (IoT) devices across multiple engineering platforms.
For more information about Matter, see [buildwithmatter.com](https://buildwithmatter.com "https://buildwithmatter.com").

Matter 1.2, released in October 2023, supports DAC revocation using Certificate Revocation
Lists (CRLs). To help you conform to the current Matter standard, when you enable CRL
revocation for CAs that issue Matter certificates, in the `CrlConfiguration`
object, in the `CrlDistributionPointExtensionConfiguration` structure, set
`OmitExtension` to `true`.

Typically, CAs embed the CRL Distribution Point (CDP) in the certificates they issue so
that the relying parties performing certificate chain validation can fetch the CRL and check
the certificate status. In Matter, the CDP URI is not written to certificates. Instead,
users fetch CDPs from the Matter Distributed Compliance Ledger (DCL), the trusted Matter
data store. You must upload the CDP URI to the Matter DCL so that it can be discovered when
validating DACs. For more information about determining the CDP URI, see [Determining the CRL Distribution Point (CDP) URI](crl-planning.md#crl-url "crl-planning.md#crl-url") . For more information about Matter, see the
[Matter standard home
page](https://csa-iot.org/all-solutions/matter/ "https://csa-iot.org/all-solutions/matter/").

###### Topics

- [Activate a Product
  Attestation Authority (PAA)](JavaApiCBC-ProductAttestationAuthorityActivation.md "JavaApiCBC-ProductAttestationAuthorityActivation.md")
- [Activate an
  Product Attestation Intermediate (PAI)](JavaApiCBC-ProductAttestationIntermediateActivation.md "JavaApiCBC-ProductAttestationIntermediateActivation.md")
- [Create a Device Attestation
  Certificate (DAC)](JavaApiCBC-DeviceAttestationCertificate.md "JavaApiCBC-DeviceAttestationCertificate.md")
- [Activate a Root CA for Node Operational Certificates (NOC).](JavaApiCBC-ActivateRootCA.md "JavaApiCBC-ActivateRootCA.md")
- [Activate a
  Subordinate CA for Node Operational Certificates (NOC)](JavaApiCBC-IntermediateCAActivation.md "JavaApiCBC-IntermediateCAActivation.md")
- [Create a Node Operational
  Certificate (NOC)](JavaApiCBC-NodeOperatingCertificate.md "JavaApiCBC-NodeOperatingCertificate.md")
