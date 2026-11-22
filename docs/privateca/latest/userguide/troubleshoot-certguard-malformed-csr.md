

# MalformedCSRException with X.509 certificate condition keys

AWS Private CA returns a `MalformedCSRException` when it can't read an attribute that an X.509 certificate condition key describes. For example, it can't determine the curve of an EC key that has implicit parameters. AWS Private CA rejects these requests whether or not your policies use the keys.

1. Compare your CSR, template, and API passthrough values with the validation checks. For more information about these checks, see [Certificate request validation](certguard-validation.md).

1. Fix the value that fails the check, and then try the request again. If the value comes from the CSR, generate a new CSR. For example, use a named curve for EC and SM2 keys, and remove empty SAN entries. If the value comes from API passthrough, correct the API passthrough values.