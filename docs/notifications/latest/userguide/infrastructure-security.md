

# Infrastructure security in AWS User Notifications
<a name="infrastructure-security"></a>

As a managed service, AWS global network security procedures protect User Notifications as described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf) whitepaper.

You use AWS published API calls to access User Notifications through the network. Clients must support Transport Layer Security (TLS) 1.2. Clients must also support cipher suites with perfect forward secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems, including Java 7 and later, support these modes.

Requests must be signed using an access key ID and a secret access key that is associated with an IAM principal. You can also use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary security credentials to sign requests.