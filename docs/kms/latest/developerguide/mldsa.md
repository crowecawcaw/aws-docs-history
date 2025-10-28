# ML-DSA keys in AWS KMS

AWS Key Management Service (AWS KMS) supports Module-Lattice Digital Signature Algorithm (ML-DSA) for
post-quantum cryptographic signatures. This implementation follows the [Federal Information Processing Standards
(FIPS) 204 standard](https://csrc.nist.gov/pubs/fips/204/final "https://csrc.nist.gov/pubs/fips/204/final") to help protect against future quantum computing threats.
AWS KMS creates and protects all ML-DSA keys and signature operations in FIPS 140-3 Security
Level 3 validated hardware security modules. To help balance security with performance,
ML-DSA in AWS KMS offers three distinct security levels through different key specifications,
ML_DSA_44, ML_DSA_65, and ML_DSA_87.

AWS KMS supports asymmetric key signatures for messages up to 4 KB using the
`RAW` message type. For larger messages, you must externally compute the
64-byte message representation μ used in ML-DSA signing as defined in NIST FIPS 204 section
6.2. Use the `EXTERNAL_MU` message type in the AWS KMS [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md") operation to specify this pre-processed
64-byte message. The signatures produced by the externally computed μ are the same as the
`RAW` ones when using the same message and private key. Note that this
signing is different from the "pre-hash" ML-DSA or HashML-DSA from section 5.4 of NIST FIPS 204.

For more information about using ML-DSA and the EXTERNAL_MU message type, see [ML-DSA key specs](symm-asymm-choose-key-spec.md#key-spec-mldsa "symm-asymm-choose-key-spec.md#key-spec-mldsa").

For an example of using ML-DSA and the EXTERNAL_MU message type, see [Offline verification with ML-DSA key
pairs](offline-operations.md#mldsa-offline-verification "offline-operations.md#mldsa-offline-verification").
