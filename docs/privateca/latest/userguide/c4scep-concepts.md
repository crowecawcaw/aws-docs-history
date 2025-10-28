# Connector for SCEP concepts

Connector for SCEP is an add-on feature for AWS Private Certificate Authority.

The following are the key concepts for Connector for SCEP:

**Certificate Signing Request (CSR)**

The required information provided to a CA in order to have a digital certificate issued. This information contains a public key as well as an identity.

**Challenge password**

The SCEP protocol uses challenge passwords to authenticate a request before issuing a certificate from a CA. Connector for SCEP handles SCEP challenge passwords based on the connector type. For more information, see [Configure your MDM system for
Connector for SCEP](using-connector-for-scep-with-mdm.md "using-connector-for-scep-with-mdm.md").

**Certificate revocation**

Certificate revocation is the process of revoking an issued certificate before its expiration date. You can revoke the private CA certificate associated to a connector by calling [RevokeCertificate](../APIReference/API_RevokeCertificate.md "../APIReference/API_RevokeCertificate.md") in the API, AWS SDK, AWS Command Line Interface, or AWS CloudFormation.

**Connector for SCEP**

A connector for SCEP links AWS Private CA to your SCEP-enabled devices.

**Mobile Device Management**

Mobile Device Management (MDM) allows IT administrators to control, secure, and enforce policies on smartphones, tablets, and other endpoints or devices. Many MDM systems provide built-in integrations for SCEP-based certificate enrollment.

**SCEP**

SCEP is a standardized protocol ([RFC 8894](https://datatracker.ietf.org/doc/html/rfc8894 "https://datatracker.ietf.org/doc/html/rfc8894")) to automatically distribute certificates. The protocol provides an endpoint for devices to request certificates from a CA. SCEP uses challenge passwords to authorize certificate issuance to devices. SCEP is commonly applied for mobile device management (MDM) systems and networking equipment. MDM solutions allow IT administrators to control, secure and enforce policies on smartphones, tablets and other entities like Apple workstations. Most MDM solutions support SCEP, such as Microsoft Intune, Apple MDM, and Jamf Pro. Most networking equipment, such as routers, load balancers, Wi-Fi hubs, VPN devices and firewalls, use SCEP for automated certificate enrollment.

**SCEP profile**

A SCEP profile contains configuration parameters that are used to define the certificate profile. This includes certificate validity period, key size, SCEP configuration name, the challenge password, number of failed attempt retries and retry interval, and other information relevant to the issuance of certificates. MDM systems and certificate management platforms typically send the SCEP profile to the client that will request a certificate for authentication.
