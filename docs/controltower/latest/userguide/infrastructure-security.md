# Infrastructure Security in AWS Control Tower

AWS Control Tower is protected by the AWS global network security procedures that are described in
the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls for access to AWS services and resources within your
landing zone through the network. We require Transport Layer Security (TLS) 1.2 and recommend Transport
Layer Security (TLS) 1.3 or later. Clients must also support cipher suites with perfect forward
secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman
(ECDHE). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that
is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security credentials to sign requests.

You can set up security groups to provide additional network infrastructure security for your
AWS Control Tower landing zone workloads. For more information, see [Walkthrough: Set Up Security Groups in AWS Control Tower
With AWS Firewall Manager](firewall-setup-walkthrough.md "firewall-setup-walkthrough.md").
