# Keys

The following list defines the keys referenced in this document.

**HBK**
HSM backing key: HSM backing keys are 256-bit root keys, from which specific use keys are derived.

**DK**
Domain key: A domain key is a 256-bit AES-GCM key. It is shared among all the members of a domain and is used to protect HSM backing keys material and HSM-service host session keys.

**DKEK**
Domain key encryption key: A domain key encryption Key is an AES-256-GCM key generated on a host and used for encrypting the current set of domain keys synchronizing domain state across the HSM hosts.

**(dHAK,QHAK)**
HSM agreement key pair: Every initiated HSM has a locally generated Elliptic Curve Diffie-Hellman agreement key pair on the curve secp384r1 (NIST-P384).

**(dE, QE)**
Ephemeral agreement key pair: HSM and service hosts generate ephemeral agreement keys. These are Elliptic Curve Diffie-Hellman keys on the curve secp384r1 (NIST-P384). These are generated in two use cases: to establish a host-to-host encryption key to transport domain key encryption keys in domain tokens and to establish HSM-service host session keys to protect sensitive communications.

**(dHSK,QHSK)**
HSM signature key pair: Every initiated HSM has a locally generated Elliptic Curve Digital Signature key pair on the curve secp384r1 (NIST-P384).

**(dOS,QOS)**
Operator signature key pair: Both the service host operators and AWS KMS operators have an identity signing key used to authenticate itself to other domain participants.

**K**
Data encryption key: A 256-bit AES-GCM key derived from an HBK using the NIST SP800-108 KDF in counter mode using HMAC with SHA256.

**SK**
Session key: A session key is created as a result of an authenticated Elliptic Curve Diffie-Hellman key exchanged between a service host operator and an HSM. The purpose of the exchange is to secure communication between the service host and the members of the domain.
