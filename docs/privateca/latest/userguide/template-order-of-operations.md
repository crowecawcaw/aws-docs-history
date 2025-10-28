# AWS Private CA template order of operations

Information contained in an issued certificate can come from four sources: the
template definition, API passthrough, CSR passthrough, and the CA configuration.

API passthrough values are only respected when you use an API passthrough or APICSR
passthrough template. CSR passthrough is only respected when you use a CSRPassthrough or
APICSR passthrough template. When these sources of information are in conflict, a
general rule usually applies: For each extension value, the template definition has
highest priority, followed by API passthrough values, followed by CSR passthrough
extensions.

**Examples**

1. The template definition for [EndEntityClientAuthCertificate_APIPassthrough](template-definitions.md#EndEntityClientAuthCertificate_APIPassthrough "template-definitions.md#EndEntityClientAuthCertificate_APIPassthrough") defines the
   ExtendedKeyUsage extension with a value of "TLS web server authentication, TLS web
   client authentication". If ExtendedKeyUsage is defined in the CSR or in the
   `IssueCertificate`
   `ApiPassthrough` parameter, the `ApiPassthrough` value for
   ExtendedKeyUsage will be ignored because the template definition takes priority,
   and the CSR value for ExtendedKeyUsage value will be ignored because the template
   is not a CSR passthrough variety.

###### Note

The template definition nonetheless copies over other values from the CSR,
such as Subject and Subject Alternative Name. These values are still taken from
the CSR even though the template is not a CSR passthrough variety, because the
template definition always takes highest priority. 2. The template definition for [EndEntityClientAuthCertificate_APICSRPassthrough](template-definitions.md#EndEntityClientAuthCertificate_APICSRPassthrough "template-definitions.md#EndEntityClientAuthCertificate_APICSRPassthrough") defines the Subject
Alternative Name (SAN) extension as being copied from the API or CSR. If the SAN
extension is defined in the CSR and provided in the
`IssueCertificate` `ApiPassthrough` parameter, the API
passthrough value will take priority because API passthrough values take priority
over CSR passthrough values.
