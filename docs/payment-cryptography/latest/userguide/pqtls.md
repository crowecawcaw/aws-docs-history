# Using hybrid post-quantum TLS

AWS Payment Cryptography and many other services supports a hybrid post-quantum key exchange option for the Transport Layer
Security (TLS) network encryption protocol. You can use this TLS option when you connect to
API endpoints or when using the AWS SDKs. These optional hybrid post-quantum key exchange features are at least as
secure as the TLS encryption we use today and are likely to provide additional long-term
security benefits.

The data that you send to enabled services is protected in transit by the encryption
provided by a Transport Layer Security (TLS) connection. The classic cipher suites based on RSA and ECC that AWS Payment Cryptography
supports for TLS sessions make brute force attacks on the key exchange mechanisms infeasible
with current technology. However, if large scale or cryptographically relevant quantum computers (CRQC)
becomes practical in the
future, the existing TLS key exchange mechanisms will be susceptible to
these attacks. It is possible that adversaries may begin harvesting encrypted data now
with the hope that they can decrypt it in the future (harvest now, decrypt later).
If you’re developing applications that rely on the long-term confidentiality of
the data passed over a TLS connection, you should consider a plan to migrate to post-quantum
cryptography before large-scale quantum computers become available for use. AWS is working to
prepare for this future, and we want you to be well-prepared, too.

![An adversary who has previously recorded a TLS session. Years later, when the adversary has a CRQC, the adversary can first recover the session key by breaking the classical key exchange using the CRQC. The adversary can then decrypt the data using the discovered session key. The previously transmitted data, if still valuable, is now compromised.](images/pqtls-risk2.png)
To protect data encrypted today against potential future attacks, AWS is participating
with the cryptographic community in the development of quantum-resistant or _post-quantum_ algorithms. AWS has implemented _hybrid_ post-quantum key exchange cipher suites that combine classic and
post-quantum elements to ensure that your TLS connection is at least as strong as it would be
with classic cipher suites.

These hybrid cipher suites are available for use on your production workloads when using recent versions of the AWS SDKs.
For more information about how to enable/disable this behavior, please see [Enabling hybrid post-quantum TLS](pqtls-details.md "pqtls-details.md")

![A TLS session that is secured both using classical key agreement and post-quantum key agreement. An adversary today cannot break the classical part of the key agreement. If the adversary records the data and tries to decrypt it in the future with a CRQC, the post-quantum key agreement keeps the session key safe. Thus, today’s transmitted data remains safe against discovery even in the future. This is why hybrid post-quantum TLS is important today.](images/pqtls-mitigation.png)

## About hybrid post-quantum key exchange in TLS

The algorithms that AWS uses are a _hybrid_ that combines [Elliptic Curve
Diffie-Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman "https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman") (ECDH), a classic key exchange algorithm used today in TLS, with
[Module-Lattice-Based
Key-Encapsulation Mechanism](https://csrc.nist.gov/pubs/fips/203/final "https://csrc.nist.gov/pubs/fips/203/final") (ML-KEM), a public-key encryption and
key-establishment algorithm that the National Institute for Standards and Technology (NIST)
[has designated as its first
standard](https://csrc.nist.gov/pubs/fips/203/final "https://csrc.nist.gov/pubs/fips/203/final") post-quantum key-agreement algorithm. This hybrid uses each of the
algorithms independently to generate a key. Then it combines the two keys cryptographically.

## Learn more about PQC

For information about the post-quantum cryptography project at the National Institute
for Standards and Technology (NIST), see [Post-Quantum
Cryptography](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography "https://csrc.nist.gov/Projects/Post-Quantum-Cryptography").

For information about NIST post-quantum cryptography standardization, see [Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization "https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization").
