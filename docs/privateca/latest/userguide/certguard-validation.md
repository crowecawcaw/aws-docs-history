

# Certificate request validation

To evaluate condition keys, AWS Private CA must be able to read every attribute that the keys describe. If it can't, it rejects the request with a `MalformedCSRException` instead of evaluating your policies without the key. AWS Private CA rejects requests whose certificate would contain any of the following:
+ An EC or SM2 subject public key with no curve parameters, or with `implicitCurve` parameters. AWS Private CA can't determine the curve or the key size of these keys. Generate the CSR with a named curve instead.
+ An EC or SM2 subject public key with malformed explicit curve parameters, or with a curve OID that AWS Private CA doesn't recognize.
+ An extended key usage extension with three or more bytes of extra data after its encoded value.
+ A SAN entry that's empty, that contains only whitespace, or that contains a control character.
+ A SAN IP address that isn't 4 or 16 bytes long.
+ A key usage, basic constraints, or SAN extension, or a validity date, that can't be parsed.

These checks apply to all `IssueCertificate` requests, whether or not your policies use X.509 certificate condition keys. To resolve a rejected request, see [MalformedCSRException with X.509 certificate condition keys](troubleshoot-certguard-malformed-csr.md).