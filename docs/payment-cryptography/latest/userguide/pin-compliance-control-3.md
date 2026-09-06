

# Control Objective 3: Keys are conveyed or transmitted in a secure manner.
<a name="pin-compliance-control-3"></a>

*Requirement 8:* Key conveyance with AWS Payment Cryptography was assessed as part of our PCI PIN assessment. You will need to document key protection mechanisms for transfers prior to import to and after export from AWS Payment Cryptography. The service provides key check values for all keys to validate correct conveyance.

Requirement 8-4 requires that public keys are conveyed in a manner that protects their integrity and authenticity. Conveyance between your application and AWS is controlled by the application’s authentication to AWS, using AWS Identity and Access Management methods, AWS’ API end point authentication to the application via TLS server certificates. Additionally, public keys exported from or imported to AWS Payment Cryptography have certificates signed by ephemeral, customer-specific CAs (See [GetPublicKeyCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate), [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport), and [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport)). These CAs cannot be used as the sole method of authentication, because they are not compliant with PCI PIN Security Annex A2. However, the certificates still provide integrity assurance for public keys with IAM providing authentication.

When exchanging public keys with your business partners using asymmetric methods, you must provide for authentication of the business via the communications channel, using a secure file exchange website, for example.

*Requirement 9:* The service does not use or directly support clear text key components.

*Requirement 10:* The service enforces relative key strength of protecting keys for conveyance. You are responsible for key conveyance prior to import to and after export from AWS Payment Cryptography and using API and TR-31 parameters that are accurate for key import, export, and generation. You should have documented procedures to describe the key conveyance mechanisms and the list of cryptographic keys used for the conveyance. 

*Requirement 11:* Documentation of your procedures must specify how keys are conveyed. Procedures for key conveyance using the AWS Payment Cryptography API should include use of roles with key import and export permissions and approvals for running scripts or other code that creates keys. AWS CloudTrail logs contain all [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey) and [ExportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey) events.