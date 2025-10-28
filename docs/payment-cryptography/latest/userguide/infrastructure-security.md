# Infrastructure security in AWS Payment Cryptography

As a managed service, AWS Payment Cryptography is protected by the AWS global network security
procedures that are described in the [Amazon Web Services:
Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access AWS Payment Cryptography through the network. Clients must
support Transport Layer Security (TLS) 1.2 or later. Clients
must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed using an access key ID and a secret access key that
is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

## Isolation of physical hosts

The security of the physical infrastructure that AWS Payment Cryptography uses is subject to the controls described in the Physical and Environmental Security section of Amazon Web Services: Overview of Security Processes. You can find more detail in compliance reports and third-party audit findings listed in the previous section.

AWS Payment Cryptography is supported by dedicated commercial-off-the-shelf PCI PTS HSM-listed hardware security modules (HSMs). The key material for AWS Payment Cryptography keys is stored only in volatile memory on the HSMs, and only while the Payment Cryptography key is in use. HSMs are in access controlled racks within Amazon data centers that enforce dual control for any physical access. For detailed information about the operation of AWS Payment Cryptography HSMs, see AWS Payment Cryptography Cryptographic Details.
