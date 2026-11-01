

# Post-quantum keys in AWS KMS
<a name="pqkeys"></a>

Most of the public-key cryptography in use today, such as RSA and elliptic curve cryptography (ECC), relies on mathematical problems that are computationally infeasible for classical computers to solve. A sufficiently large, fault-tolerant quantum computer could use [Shor's algorithm](https://en.wikipedia.org/wiki/Shor's_algorithm) to solve these problems efficiently. This would let an adversary recover private keys. It would also defeat the confidentiality and authenticity that these algorithms provide. Although no such quantum computer exists today, an adversary could record protected data and attack it later once quantum computers become available. This strategy is known as *harvest now, decrypt later*. The risk is particularly relevant to data that must remain secure for many years.

Post-quantum cryptography, also called quantum-resistant cryptography, uses algorithms that are designed to remain secure against attacks from both classical and quantum computers. The U.S. National Institute of Standards and Technology (NIST) began a public standardization effort for these algorithms in 2016. In August 2024, NIST published its first post-quantum cryptography standards. These include [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) and [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) for the Module-Lattice Digital Signature Algorithm (ML-DSA). To help you protect the long-term confidentiality and integrity of your data, AWS KMS supports both of these post-quantum key types:
+ **[ML-DSA keys in AWS KMS](#mldsa)**: choose these keys when you need post-quantum digital signatures.
+ **[ML-KEM keys in AWS KMS](#mlkem)**: choose these keys when you need post-quantum key establishment.

Post-quantum KMS keys protect the data and signatures that you use them for. To also protect the confidentiality of the requests and responses that you exchange with AWS KMS itself, use post-quantum TLS. For more information, see [Using hybrid post-quantum TLS with AWS KMS](pqtls.md).

## ML-DSA keys in AWS KMS
<a name="mldsa"></a>

AWS Key Management Service (AWS KMS) supports Module-Lattice Digital Signature Algorithm (ML-DSA) for post-quantum cryptographic signatures. This implementation follows the [FIPS 204 standard](https://csrc.nist.gov/pubs/fips/204/final) on the NIST website to help protect against future quantum computing threats. AWS KMS creates and protects all ML-DSA keys and signature operations in FIPS 140-3 Security Level 3 validated hardware security modules. To help balance security with performance, ML-DSA in AWS KMS offers three distinct security levels through different key specifications, ML\_DSA\_44, ML\_DSA\_65, and ML\_DSA\_87.

AWS KMS supports asymmetric key signatures for messages up to 4 KB using the `RAW` message type. For larger messages, you must externally compute the 64-byte message representation μ used in ML-DSA signing as defined in NIST FIPS 204 section 6.2. Use the `EXTERNAL_MU` message type in the AWS KMS [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) operation to specify this pre-processed 64-byte message. The signatures produced by the externally computed μ are the same as the `RAW` ones when using the same message and private key. Note that this signing is different from the "pre-hash" ML-DSA or HashML-DSA from section 5.4 of NIST FIPS 204.

For more information about using ML-DSA and the EXTERNAL\_MU message type, see [ML-DSA key specs](symm-asymm-choose-key-spec.md#key-spec-mldsa).

For an example of using ML-DSA and the EXTERNAL\_MU message type, see [Offline verification with ML-DSA key pairs](offline-operations.md#mldsa-offline-verification).

## ML-KEM keys in AWS KMS
<a name="mlkem"></a>

AWS Key Management Service (AWS KMS) supports the Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) for post-quantum key establishment. This implementation follows the [FIPS 203 standard](https://csrc.nist.gov/pubs/fips/203/final) on the NIST website to help protect against future quantum computing threats. AWS KMS creates and protects all ML-KEM keys in FIPS 140-3 Security Level 3 validated hardware security modules. To help balance security with performance, ML-KEM in AWS KMS offers three distinct security levels through different key specifications, ML\_KEM\_512, ML\_KEM\_768, and ML\_KEM\_1024.

**Note**  
ML-KEM keys are not available in the China Regions.

The following workflow shows how two parties, Alice and Bob, establish a shared secret over an insecure channel using ML-KEM.

1. **Alice** calls [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) to create an asymmetric KMS key with a `KeyUsage` value of `ENCAPSULATE_DECAPSULATE` and an [ML-KEM](symm-asymm-choose-key-spec.md#key-spec-mlkem) key spec (`ML_KEM_512`, `ML_KEM_768`, or `ML_KEM_1024`).

1. Alice **sends her public key** to Bob over an insecure channel. Alternatively, Alice can authorize Bob to call [GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) to download her public key.
**Note**  
AWS KMS strongly recommends verifying that the public key you receive came from the expected party before using it to encapsulate a shared secret.

1. **Bob** calls [Encapsulate](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encapsulate.html) with Alice's public key. AWS KMS generates a random 32-byte shared secret and its encapsulated (ciphertext) form. Bob keeps the shared secret and sends only the encapsulated form to Alice. Because encapsulation requires only the public key, Bob can also encapsulate the shared secret outside of AWS KMS with his own cryptographic library.

1. **Alice** calls [Decapsulate](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decapsulate.html) with her KMS key and the encapsulated shared secret she received from Bob. AWS KMS uses the private key to recover the same 32-byte shared secret that Bob generated. The private key never leaves AWS KMS unencrypted. Alice and Bob now share a secret they can use to derive symmetric keys for encrypting data or for generating and verifying HMACs.

Unlike a key agreement mechanism such as [Elliptic Curve Diffie-Hellman (ECDH)](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html), which derives a shared secret from a key contributed by each party, a key encapsulation mechanism generates the shared secret using only the recipient's public key. The shared secret that ML-KEM returns is cryptographically random and can be used directly as key material. It can also be processed using a key derivation function to produce multiple distinct keys and nonces.

**Note**  
Post-Quantum Hybrid Public Key Encryption (PQ-HPKE), as described in the [PQ-HPKE draft](https://datatracker.ietf.org/doc/draft-ietf-hpke-pq/) on the IETF website, combines three steps into one operation. It encapsulates the shared secret, uses a key derivation function (KDF) to derive an AES key and base initialization, and encrypts plaintext with AES-GCM. A direct Encrypt API for ML-KEM keys would bundle these steps and simplify the user experience. AWS KMS is closely tracking the standardization of this draft at the IETF as a PQ-safe replacement for RSA-based encryption.

For more information about the ML-KEM key specs, see [ML-KEM key specs](symm-asymm-choose-key-spec.md#key-spec-mlkem).