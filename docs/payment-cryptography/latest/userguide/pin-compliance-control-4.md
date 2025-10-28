# Control Objective 4: Key-loading to HSMs and POI PIN-acceptance devices is handled in a secure manner.

_Requirement 12:_ You are responsible for loading keys from components or shares. Management of HSM main
keys was assessed as part of the service’s PIN assessment. AWS Payment Cryptography does not load keys from individual shares or
components. See the [Cryptographic details](cryptographic-details.md "cryptographic-details.md") section.

_Requirements 13 and 14:_ You will need to describe key protection for transfers prior to import to and
after export from the service.

_Requirement 15:_ AWS Payment Cryptography provides key check values for all keys in the service and
integrity assurance for public keys. Your application is responsible for using these checks to validate keys after import to or
export from the service. You should document the procedures to ensure that a validation mechanism in place.

Requirement 15-2 requires that public keys are loaded in a manner that protects their integrity and authenticity.
[ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md"), together with
[GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md"), provides
for validation of provided signing certificates.
If provided certificates are self-signed, than authentication must be provided by a separate mechanism, for example secure
file exchange.

_Requirement 16:_ Documentation of your procedures must specify how keys are loaded to the service.
Procedures for key import using the API should include use of roles with key import permissions and approvals for running scripts
or other code that loads keys. AWS CloudTrail logs contain all
[ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md") events. You should include the
logging mechanisms in the
documentation. The service provides key check values for all keys to validate correct key loading.
