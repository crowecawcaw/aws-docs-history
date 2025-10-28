# Control Objective 3: Keys are conveyed or transmitted in a secure manner.

_Requirement 8:_ Key conveyance with AWS Payment Cryptography was assessed as part of our PCI PIN assessment.
You will need to document key protection mechanisms for transfers prior to import to and after export from AWS Payment Cryptography. The service provides
key check values for all keys to validate correct conveyance.

Requirement 8-4 requires that public keys are conveyed in a manner that protects their integrity and authenticity. Conveyance
between your application and AWS is controlled by the application’s authentication to AWS, using AWS Identity and Access Management methods, AWS’ API end point
authentication to the application via TLS server certificates. Additionally, public keys exported from or imported to AWS Payment Cryptography have
certificates signed by ephemeral, customer-specific CAs (See
[GetPublicKeyCertificate](../APIReference/API_GetPublicKeyCertificate.md "../APIReference/API_GetPublicKeyCertificate.md"),
[GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md"), and
[GetParametersForExport](../APIReference/API_GetParametersForExport.md "../APIReference/API_GetParametersForExport.md")).
These CAs cannot be used as the sole method of authentication, because they are not compliant with PCI PIN Security Annex A2. However,
the certificates still provide integrity assurance for public keys with IAM providing authentication.

When exchanging public keys with your business partners using asymmetric methods, you must provide for authentication of the
business via the communications channel, using a secure file exchange website, for example.

_Requirement 9:_ The service does not use or directly support clear text key components.

_Requirement 10:_ The service enforces relative key strength of protecting keys for conveyance. You are
responsible for key conveyance prior to import to and after export from AWS Payment Cryptography and using API and TR-31 parameters
that are accurate for key import, export, and generation. You should have documented procedures to describe the key conveyance mechanisms
and the list of cryptographic keys used for the conveyance.

_Requirement 11:_ Documentation of your procedures must specify how keys are conveyed. Procedures for key
conveyance using the AWS Payment Cryptography API should include use of roles with key import and export permissions and approvals
for running scripts or other code that creates keys. AWS CloudTrail logs contain all
[ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md") and
[ExportKey](../APIReference/API_ExportKey.md "../APIReference/API_ExportKey.md") events.
