

# Control Objective 4: Key-loading to HSMs and POI PIN-acceptance devices is handled in a secure manner.
<a name="pin-compliance-control-4"></a>

*Requirement 12:* You are responsible for loading keys from components or shares. Management of HSM main keys was assessed as part of the service’s PIN assessment. AWS Payment Cryptography does not load keys from individual shares or components. See the [Cryptographic details](cryptographic-details.md) section.

*Requirements 13 and 14:* You will need to describe key protection for transfers prior to import to and after export from the service.

*Requirement 15:* AWS Payment Cryptography provides key check values for all keys in the service and integrity assurance for public keys. Your application is responsible for using these checks to validate keys after import to or export from the service. You should document the procedures to ensure that a validation mechanism in place.

Requirement 15-2 requires that public keys are loaded in a manner that protects their integrity and authenticity. [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey), together with [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport), provides for validation of provided signing certificates. If provided certificates are self-signed, than authentication must be provided by a separate mechanism, for example secure file exchange.

*Requirement 16:* Documentation of your procedures must specify how keys are loaded to the service. Procedures for key import using the API should include use of roles with key import permissions and approvals for running scripts or other code that loads keys. AWS CloudTrail logs contain all [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey) events. You should include the logging mechanisms in the documentation. The service provides key check values for all keys to validate correct key loading.