

# Control certificate issuance with X.509 certificate condition keys

With X.509 certificate condition keys, you can write IAM policies that inspect the certificate that AWS Private CA is about to sign. When a caller invokes the [IssueCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) operation, AWS Private CA builds the certificate from the certificate signing request (CSR), the certificate template, any API passthrough values, and the request parameters. It then evaluates your policies against the attributes of that certificate before signing it. If a policy denies the request, AWS Private CA returns an `AccessDeniedException` and doesn't issue the certificate.

The condition keys describe the certificate that would be issued, not how its contents were supplied. For example, `acm-pca:x509Ext/ExtendedKeyUsage` has the same value whether the extended key usage came from the CSR, the template, or API passthrough. This means that a policy can't be bypassed by moving an attribute from one input to another.

X.509 certificate condition keys are available only for the `acm-pca:IssueCertificate` action. Don't use them in statements that apply to other actions, such as `acm-pca:RevokeCertificate` or `acm-pca:GetCertificate`. Those requests don't include the keys, so the conditions in those statements won't match the way you intend.

**Important**  
A new `Deny` statement can block certificate requests that you didn't intend to block, including requests that other AWS services and connectors make on your behalf. Before you apply a policy broadly, read [Before you deploy a policy](certguard-before-you-deploy.md) and test the policy in a non-production account.

**Topics**
+ [Supported policy types](certguard-policy-types.md)
+ [Condition key reference](#certguard-condition-key-reference)
+ [How condition key values are evaluated](certguard-evaluation.md)
+ [Certificate request validation](certguard-validation.md)
+ [Example policies](certguard-example-policies.md)
+ [Before you deploy a policy](certguard-before-you-deploy.md)

## Condition key reference
<a name="certguard-condition-key-reference"></a>

All X.509 certificate condition keys use the `acm-pca:` prefix and describe the To-Be-Signed (TBS) certificate. A key that doesn't apply to the certificate is absent from the request context. For example, `acm-pca:x509Key/curve` is absent for an RSA key, and `acm-pca:x509Ext/BasicConstraints/pathLen` is absent when the certificate doesn't set a path length. For how absent keys affect your policies, see [How condition key values are evaluated](certguard-evaluation.md).

The following keys describe the subject of the certificate.


| Condition key | Type | Description | 
| --- | --- | --- | 
| `acm-pca:x509Subject/empty` | Bool | true if the subject distinguished name is empty or contains only empty relative distinguished names. Always present. | 
| `acm-pca:x509Subject/CN` | ArrayOfString | Subject common names, matched as written in the certificate. For more information, see [How condition key values are evaluated](certguard-evaluation.md). | 
| `acm-pca:x509Subject/C` | ArrayOfString | Subject countries, as two-letter codes. For example, DE. | 
| `acm-pca:x509Subject/O` | ArrayOfString | Subject organizations. | 
| `acm-pca:x509Subject/OU` | ArrayOfString | Subject organizational units. | 

The following keys describe the subject alternative name (SAN) extension.


| Condition key | Type | Description | 
| --- | --- | --- | 
| `acm-pca:x509SAN/present` | Bool | true if the certificate has a subject alternative name extension. | 
| `acm-pca:x509SAN/critical` | Bool | true if the SAN extension is marked critical. | 
| `acm-pca:x509SAN/count` | Numeric | Total number of entries in the SAN extension. | 
| `acm-pca:x509SAN/DNS` | ArrayOfString | DNS name entries, in lowercase without a trailing dot. For example, www.example.com. | 
| `acm-pca:x509SAN/IP` | ArrayOfIPAddress | IP address entries. AWS Private CA evaluates IPv4-mapped IPv6 addresses as IPv4 addresses, so IPv4 ranges in your conditions also match them. | 
| `acm-pca:x509SAN/URI` | ArrayOfString | URI entries, such as SPIFFE workload identifiers. The host part is lowercase, and the rest of the URI is unchanged. | 
| `acm-pca:x509SAN/RFC822` | ArrayOfString | Email address entries. The domain part is lowercase, and the local part is unchanged. | 
| `acm-pca:x509SAN/Name/CN` | ArrayOfString | Common names from all directory name entries in the SAN extension. | 
| `acm-pca:x509SAN/OtherName/${OID}` | ArrayOfString | Values of other name entries, keyed by type ID. For example, the Microsoft user principal name is acm-pca:x509SAN/OtherName/1.3.6.1.4.1.311.20.2.3. | 

The following keys describe the subject public key and the signature algorithm.


| Condition key | Type | Description | 
| --- | --- | --- | 
| `acm-pca:x509Key/algorithm` | String | Algorithm of the subject public key from the CSR: RSA, EC, SM2, ML-DSA-44, ML-DSA-65, or ML-DSA-87. This is the key being certified, not the CA's key. | 
| `acm-pca:x509Key/size` | Numeric | Size of the subject public key, in bits:+  RSA – Modulus length. For example, `2048`. <br />+  EC and SM2 – Field size of the curve. For example, `256` for `prime256v1`. For a curve that isn't a known named curve, this is the field size given in the explicit parameters. It isn't a measure of curve strength. <br />+  ML-DSA – Length of the encoded public key: `10496` (ML-DSA-44), `15616` (ML-DSA-65), or `20736` (ML-DSA-87). To restrict ML-DSA parameter sets, use `acm-pca:x509Key/algorithm`.  | 
| `acm-pca:x509Key/curve` | String | Curve of an EC or SM2 subject key. For example, prime256v1, secp384r1, or secp521r1. Present when the key names its curve, and also when the key spells out explicit parameters that exactly match a known named curve. Absent for other keys, including explicit parameters that don't match a known curve. | 
| `acm-pca:x509Key/namedCurve` | Bool | true if an EC or SM2 subject key identifies its curve by object identifier (a named curve), as RFC 5480 requires. false if the key spells out explicit curve parameters. Absent for other key algorithms. | 
| `acm-pca:x509Signature/algorithm` | String | Algorithm the CA uses to sign the certificate, set by the SigningAlgorithm request parameter. For example, sha256WithRSAEncryption, ecdsa-with-SHA384, or ML-DSA-65. This describes the CA's signature, not the subject key. | 

The following keys describe the validity period.


| Condition key | Type | Description | 
| --- | --- | --- | 
| `acm-pca:x509Validity/notBefore` | Date | Start of the validity period, in UTC. For example, 2026-03-02T18:56:38Z. | 
| `acm-pca:x509Validity/notAfter` | Date | End of the validity period, in UTC. | 
| `acm-pca:x509Validity/durationDays` | Numeric | Time from notBefore to notAfter, in whole days, rounded down. | 
| `acm-pca:x509Validity/durationHours` | Numeric | Time from notBefore to notAfter, in whole hours, rounded down. | 

The following keys describe the key usage, extended key usage, and basic constraints extensions.


| Condition key | Type | Description | 
| --- | --- | --- | 
| `acm-pca:x509Ext/KeyUsage/present` | Bool | true if the certificate has a key usage extension. | 
| `acm-pca:x509Ext/KeyUsage` | ArrayOfString | Key usage values, using the RFC 5280 names: digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment, keyAgreement, keyCertSign, cRLSign, encipherOnly, and decipherOnly. | 
| `acm-pca:x509Ext/KeyUsage/critical` | Bool | true if the key usage extension is marked critical. | 
| `acm-pca:x509Ext/ExtendedKeyUsage/present` | Bool | true if the certificate has an extended key usage extension. | 
| `acm-pca:x509Ext/ExtendedKeyUsage` | ArrayOfString | Extended key usage purposes. Each purpose appears as its object identifier (OID). Purposes defined in RFC 5280 also appear by name: serverAuth, clientAuth, codeSigning, emailProtection, timeStamping, and OCSPSigning. For example, a TLS server certificate has the values serverAuth and 1.3.6.1.5.5.7.3.1. | 
| `acm-pca:x509Ext/ExtendedKeyUsage/count` | Numeric | Number of extended key usage purposes in the certificate. Each purpose counts once. | 
| `acm-pca:x509Ext/ExtendedKeyUsage/critical` | Bool | true if the extended key usage extension is marked critical. | 
| `acm-pca:x509Ext/BasicConstraints/present` | Bool | true if the certificate has a basic constraints extension. | 
| `acm-pca:x509Ext/BasicConstraints/CA` | Bool | true if the certificate is a CA certificate. Absent when the certificate has no basic constraints extension. | 
| `acm-pca:x509Ext/BasicConstraints/pathLen` | Numeric | Path length constraint of a CA certificate. Absent when the certificate doesn't set one. | 
| `acm-pca:x509Ext/BasicConstraints/critical` | Bool | true if the basic constraints extension is marked critical. | 