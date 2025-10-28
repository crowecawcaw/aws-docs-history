# Infrastructure Security in AWS End User Messaging SMS

As a managed service, AWS End User Messaging SMS is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access AWS End User Messaging SMS through the network. Clients must
support Transport Layer Security (TLS) 1.0 or later. We recommend TLS 1.2. Clients
must also support cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed by using
an access key ID and a secret access key that is associated with an IAM principal. Or you
can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.
