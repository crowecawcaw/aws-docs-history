AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Infrastructure security in Amazon Q Developer in chat applications

As a managed service, Amazon Q Developer in chat applications is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access Amazon Q Developer through the network. Clients must
support Transport Layer Security (TLS) 1.2 or later. We recommend TLS 1.3. Clients
must also support cipher suites with perfect forward secrecy
(PFS),
such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE).
Most modern
systems,
such as Java 7 and
later,
support these modes.

Additionally, requests must be signed by using
an access key ID and a secret access key that is associated with an IAM principal. Or you
can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.
