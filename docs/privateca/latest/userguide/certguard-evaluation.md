

# How condition key values are evaluated

The following details affect how you write conditions. For general information about condition operators, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the *IAM User Guide*.

Absent keys  
A key that doesn't apply to the certificate is absent. Negated operators such as `StringNotEquals` and `StringNotLike` return `true` for an absent key. For example, consider a `Deny` statement that uses only `"StringNotEquals": {"acm-pca:x509Key/curve": [...]}`. RSA and ML-DSA keys have no curve, so that statement also denies every RSA and ML-DSA request.  
To limit a `Deny` statement to certificates that have the key, add a second condition that scopes the statement. For example, add `"StringEquals": {"acm-pca:x509Key/algorithm": ["EC", "SM2"]}`, or add `"Null": {"{{key}}": "false"}`.  
In an `Allow` statement, use the `...IfExists` form of the operator to allow certificates that don't have the key. Don't use `...IfExists` to narrow a `Deny` statement. An `...IfExists` condition is `true` when the key is absent, so the statement still denies the request.

Multivalued keys  
Keys of type `ArrayOfString` and `ArrayOfIPAddress` can hold several values. Use the `ForAnyValue` or `ForAllValues` set operators with them. If the certificate has no values for the key, a `ForAnyValue` condition is `false` and a `ForAllValues` condition is `true`. For more information, see [Single-valued and multivalued context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.html) in the *IAM User Guide*.  
`acm-pca:x509Ext/ExtendedKeyUsage` contains both the name and the OID of each named purpose. A `ForAllValues:StringEquals` condition that lists only `serverAuth` doesn't match a certificate whose values are `serverAuth` and `1.3.6.1.5.5.7.3.1`. List both forms, or use `ForAnyValue` to test for a specific purpose.

Hostnames in SAN entries  
DNS names are case-insensitive, and a trailing dot doesn't change the name. So that a policy can't be bypassed with a different spelling of the same name, AWS Private CA converts hostnames before evaluation:  
+ `acm-pca:x509SAN/DNS` – Lowercased, with any trailing dot removed. `WWW.Example.COM.` is evaluated as `www.example.com`.
+ `acm-pca:x509SAN/RFC822` – AWS Private CA lowercases the domain part and removes any trailing dot. It doesn't change the local part, because the local part can be case-sensitive. `Jane.Doe@Example.COM` is evaluated as `Jane.Doe@example.com`.
+ `acm-pca:x509SAN/URI` – The host is lowercased. The scheme, path, query, and fragment are unchanged.
Write the hostname parts of your conditions in lowercase, without a trailing dot. Leading and trailing whitespace is also removed from DNS, email, and URI entries. These conversions apply only to policy evaluation. The issued certificate contains the values as they were requested.

Subject attributes  
A subject can contain the same attribute more than once, so the subject keys are multivalued. Use them with `ForAnyValue` or `ForAllValues`, as with the SAN keys.  
Common names aren't converted. This applies to both `acm-pca:x509Subject/CN` and `acm-pca:x509SAN/Name/CN`, so a request can vary the letter case of a common name. To match a common name regardless of case, use `ForAnyValue:StringEqualsIgnoreCase` or `ForAnyValue:StringNotEqualsIgnoreCase`. IAM has no case-insensitive form of `StringLike`, so a wildcard pattern on either common name key is case-sensitive and can be bypassed with a different letter case. When you need a wildcard match on a hostname, use `acm-pca:x509SAN/DNS`, which is lowercased.

Characters outside Latin-1  
IAM policies support only Latin-1 characters in condition values. You can't write a condition that matches a value containing other Unicode characters, such as a common name or an email local part in a non-Latin script.  
The condition keys hold internationalized domain names (IDNs) in their ASCII form (an A-label that starts with `xn--`). Write your conditions against the A-label; for example, match `xn--bcher-kva.example`, not `bücher.example`. If you supply a DNS name, email address, or URI that contains Unicode characters through API passthrough, AWS Private CA converts it to the A-label. AWS Private CA rejects a request whose CSR or custom extension encodes one of these entries with Unicode characters. AWS Private CA never issues a certificate with a U-label in these entries, so you don't need to check for the U-label.

Validity period  
Unless the request specifies `ValidityNotBefore`, AWS Private CA sets `notBefore` to 60 minutes before the issuance time, and calculates `notAfter` from the issuance time. The duration keys therefore include the extra hour. For example, a request for a validity of 90 days produces `durationDays` of `90` and `durationHours` of `2161`. Allow for this when you set hour-based limits, or when you compare `notBefore` with a fixed date. For more information, see [Choose validity periods](ca-lifecycle.md#ca-validity-period).  
Date conditions accept only fixed timestamps in ISO 8601 format, such as `2027-01-01T00:00:00Z`. You can't compare one condition key with another, or with a time relative to the request.

Curves and curve encoding  
`acm-pca:x509Key/curve` describes which curve a key uses, not how the curve is encoded. A condition that allows only `prime256v1` also allows P-256 keys that spell out the curve as explicit parameters. Some libraries, such as the JDK SunEC provider, can't use those keys. If the clients and servers that validate your certificates require named curves, also check `acm-pca:x509Key/namedCurve`.

Combining conditions  
All conditions in a statement must match for the statement to apply. IAM can't compare two condition keys with each other, so you can't require, for example, that the common name equals one of the DNS names. Instead, restrict each key to the same set of allowed values.