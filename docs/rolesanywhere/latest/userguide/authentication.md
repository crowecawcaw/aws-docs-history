# The IAM Roles Anywhere authentication process

To provide credentials, AWS Identity and Access Management Roles Anywhere uses the [IAM Roles Anywhere CreateSession API](authentication-create-session.md "authentication-create-session.md"). The API authenticates requests with a signature using keys associated with the X.509 certificate, which was used for authentication. It acts like `AssumeRole` – exchanging the signature for a standard SigV4-compatible session credential.

To successfully authenticate, the following constraints must be satisfied:

- The signature attached to the request **MUST** be validated against the signing certificate (also attached to the request).
- The signing certificate **MUST** have a valid trust chain to a Certificate Authority (CA) certificate configured in the customer account.
- The target role for which credentials are issued **MUST** have an `AssumeRolePolicyDocument` that allows IAM Roles Anywhere service principal, `rolesanywhere.amazonaws.com`, to call `sts:AssumeRole`, `sts:TagSession`, and `sts:SetSourceIdentity`. For more information, see [Granting permissions to pass a role to a service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the _IAM User Guide_.
- The target role for which credentials are issued **MAY** have additional `Condition` predicates in the `AssumeRolePolicyDocument` that restrict authorization based on attributes extracted from the X.509 Certificate (for example, Subject or Issuer).
  The signature uses the same canonicalization mechanism as [AWS Signature V4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") (SigV4), with the following changes and additions:

- The private key used to sign the request **MUST** be bound to an X.509 Certificate.
- The signing certificate **MUST** be a v3 certificate.
- The signing certificate **MUST** be attached to the request via the header `X-Amz-X509`, as Base64-encoded Distinguished Encoding Rules (DER) data.
- The relevant headers – `X-Amz-X509` and `X-Amz-X509-Chain` (if applicable) **MUST** be included in the signed headers field of the `Authorization` header.
- The `X-Amz-X509-Chain` header **MUST** be encoded as comma-delimited, base64-encoded DER.
- The `X-Amx-X509-Chain` header **MUST NOT** exceed the maximum depth of 5 certificates.
- The signing certificate's serial number **MUST** be included in the Credential portion of the Scope field of the `Authorization` header.
  RSA, EC and ML-DSA keys are supported; RSA keys are used with the RSA PKCS#1 v1.5 signing algorithm. EC keys are used with the ECDSA. ML-DSA keys can be used with ML-DSA-44, ML-DSA-65 or ML-DSA-87.

###### Topics

- [IAM Roles Anywhere CreateSession API](authentication-create-session.md "authentication-create-session.md")
- [The IAM Roles Anywhere authentication signing
  process](authentication-sign-process.md "authentication-sign-process.md")
