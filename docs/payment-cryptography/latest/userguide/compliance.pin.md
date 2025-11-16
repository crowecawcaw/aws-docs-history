# Common Topics

Migrating applications from connecting to HSM to a managed service such as AWS Payment Cryptography brings up
common issues and concepts for customers and their assessors.
This section provides information to clarify how the secure use of the service addresses these situations.

###### Topics

- [Shared Responsibility](#compliance.pin.commontopics.sharedresponsibility "#compliance.pin.commontopics.sharedresponsibility")
- [Minimum HSM configuration](#compliance.pin.commontopics.hsmconfig "#compliance.pin.commontopics.hsmconfig")
- [Key exchange between customer and APC](#compliance.pin.commontopics.keyconfig "#compliance.pin.commontopics.keyconfig")

## Shared Responsibility

Customers that have assumed complete security and compliance responsibility for applications will restructure their compliance to take advantage of AWS Payment Cryptography's
key management, security controls and managed HSM capabilities ("the service"). This will shift some requirements completely to AWS, as attested by AWS Payment Cryptography's third party assessments. Some
requirements will be shared between the customer's application and the service. An application is responsible for:

- Providing accurate information to the service
- Using security controls according to the service's recommendations and PCI PIN security requirements
- Implementing required security controls using the tools provided by the service

Customers and their assessors will use shared responsibility and implementation guides published with compliance attestations
on AWS Artifact to implement controls and control monitoring then plan for and complete assessments.

## Minimum HSM configuration

The PCI Data Security Standard, the foundational standard for other PCI standards,
requires all systems to be configured with minimum functionality needed for its function.
PCI PIN, P2PE, and other solution standards apply this requirement to HSMs in the solution. HSMs must only enable functions needed for the solution.

AWS services should be treated as systems and configured for minimum required functionality.
[Payment Card Industry Data Security Standard (PCI DSS) v4.0 on AWS](https://aws.amazon.com/blogs/security/pci-dss-v4-0-on-aws-compliance-guide-now-available/ "https://aws.amazon.com/blogs/security/pci-dss-v4-0-on-aws-compliance-guide-now-available/") recommends using
IAM to configure minimum functionality for each AWS service used by the solution.
This also applies to AWS Payment Cryptography. IAM policies enable fine-grained permissions to restrict
cryptographic functions only to the application components that rely on them.

## Key exchange between customer and APC

PIN PIN Security requirements 8-4 and 15-2 require public keys for exchange and loading of keys are
authenticated and integrity protected. For remote key loading of POI, functionally described in
ANSI/ASC X9 TR-34 and governed by PCI PIN Annex A, public keys are most often conveyed in
certificates signed by an Annex A2-compliant certificate authority. For exchanges between organization, public keys use other mechanisms for authenticity and integrity.

All interactions between customer and AWS are via AWS APIs, which mutually authenticate each
API call and assure the integrity of calls and responses using TLS. Authentication of the customer
application is managed by AWS Identity and Access Management with mechanisms such as
Security Tokens and SigV4. AWS API endpoints are authenticated by the customer using TLS
server authentication, which is built into AWS SDKs. Then TLS assures the confidentiality
and integrity of all data passed between the customer and each AWS API.

APC APIs GetParametersForImport and ImportKey implement a key transfer from the customer to the service.
While the Certificate Authority(CA) provided by GetParametersForImport is not Annex A2-compliant,
it is secure and unique to the account. While this CA cannot be relied on
for compliance with requirements 8-4 and 15-2, it does provide integrity verification of imported key. You can also use your own CA by leveraging the GetCertificateSigningRequest API.

The mechanisms that provide public key authentication and integrity assurance are:

- Authentication provided by AWS API authentication
- Integrity of the key is provided by the MAC feature of the certificate provided by GetParametersForImport,
  even if the identity information in the certificate is not trusted.
  Integrity of the key is also assured by MAC used by TLS protecting the session between the customer and AWS

Certificates and key blocks provided by APC are compliant with Annex A1, which specifies requirements for certificates and key protection by asymmetric methods.
