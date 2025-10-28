# Infrastructure security in Amazon GameLift Servers

If you're using Amazon GameLift Servers FleetIQ as a standalone feature with Amazon EC2, see [Security in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md") in the
_Amazon EC2 User Guide_.

As a managed service, Amazon GameLift Servers is protected by the AWS global
network security procedures that are described in the [Amazon Web Services: Overview of security processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access Amazon GameLift Servers through the network. Clients must
support Transport Layer Security (TLS) 1.2 or later. We recommend TLS 1.3 or later. Clients
must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key
that is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

The Amazon GameLift Servers service places all fleets into Amazon virtual private clouds (VPCs) so that
each fleet exists in a logically isolated area in the AWS Cloud. You can use Amazon GameLift Servers
policies to control access from specific VPC endpoints or specific VPCs. Effectively, this
isolates network access to a given Amazon GameLift Servers resource from only the specific VPC within the
AWS network. When you create a fleet, you specify a range of port numbers and IP
addresses. These ranges limit how inbound traffic can access hosted game servers on a fleet
VPC. Use standard security best practices when choosing fleet access settings.
