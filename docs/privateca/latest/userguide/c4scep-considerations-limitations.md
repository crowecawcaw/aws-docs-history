# Understand Connector for SCEP considerations and limitations

Keep in mind the following considerations and limitations when using Connector for SCEP.

## Considerations

**CA operating modes**

You can only use Connector for SCEP with private CAs that use a general-purpose operating mode. Connector for SCEP defaults to issuing certificates with a validity period of one year. A private CA using a short-lived certificate mode doesn't support issuing certificates with a validity period greater than seven days. For information about operating modes, see [Understand AWS Private CA CA modes](short-lived-certificates.md "short-lived-certificates.md").

**Challenge passwords**

- Distribute your challenge passwords very carefully and share only with highly trusted individuals and clients. A single challenge password can be used to issue any certificate, with any subject and SANs, which poses a security risk.
- If using a general-purpose connector, we recommend that you manually rotate your challenge passwords frequently.

**Conformance to RFC 8894**

Connector for SCEP deviates from the [RFC 8894](https://www.rfc-editor.org/rfc/rfc8894.html "https://www.rfc-editor.org/rfc/rfc8894.html") protocol by providing HTTPS endpoints instead of HTTP endpoints.

**CSRs**

- If a certificate signing request (CSR) that is sent to Connector for SCEP doesn't include the Extended
  Key Usage (EKU) extension, we'll set the EKU value to `clientAuthentication`.
  For information, see [4.2.1.12. Extended Key Usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12:~:text=MAX)%0A%0A4.2.1.12.-,Extended%20Key%20Usage,-This%20extension%20indicates "https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12:~:text=MAX)%0A%0A4.2.1.12.-,Extended%20Key%20Usage,-This%20extension%20indicates") in RFC 5280.
- We support `ValidityPeriod` and `ValidityPeriodUnits` custom attributes in CSRs. If your CSR doesn't include a `ValidityPeriod`, we issue a certificate that has a one year validity period. Keep in mind that you might not be able to set these attributes in your MDM system. But if you can set them, we support them. For information about these attributes, see [szENROLLMENT_NAME_VALUE_PAIR](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/92f07a54-2889-45e3-afd0-94b60daa80ec "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/92f07a54-2889-45e3-afd0-94b60daa80ec").

###### Endpoint sharing

Distribute a connector's endpoints to trusted parties only. Treat the endpoints as secret because anyone who can find your unique fully-qualified domain name and path can retrieve your CA certificate.

## Limitations

The following limitations apply to Connector for SCEP.

###### Dynamic challenge passwords

You can only create static challenge passwords with general-purpose connectors. To use dynamic passwords with a general-purpose connector, you must build your own rotation mechanism that employs the connector's static passwords. Connector for SCEP for Microsoft Intune connector types offer support for dynamic passwords, which you manage using Microsoft Intune.

###### HTTP

Connector for SCEP supports HTTPS only, and creates redirects for HTTP calls. If your system
is reliant on HTTP, make sure that it can accommodate the HTTP redirects that
Connector for SCEP provides.

###### Shared private CAs

You can only use Connector for SCEP with private CAs of which you are the owner.
