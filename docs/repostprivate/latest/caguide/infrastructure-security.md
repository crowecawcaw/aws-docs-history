End of support notice: On June 30, 2027, AWS
will end support for AWS re:Post Private. After June 30, 2027, you will
no longer be able to access the re:Post Private console or re:Post Private resources.
For more information, see [AWS re:Post Private end of support](../userguide/repost-private-end-of-support.md "../userguide/repost-private-end-of-support.md").

# Infrastructure Security in AWS re:Post Private

As a managed service, AWS re:Post Private is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access re:Post Private through the network. Clients must
support Transport Layer Security (TLS) 1.0 or later. We recommend TLS 1.2 or later. Clients
must also support cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed by using
an access key ID and a secret access key that is associated with an AWS Identity and Access Management principal. Or you
can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.
