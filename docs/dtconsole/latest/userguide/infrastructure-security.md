# Infrastructure security in AWS CodeStar Notifications and AWS CodeConnections

As features in a managed service, AWS CodeStar Notifications and AWS CodeConnections are protected by the AWS global
network security procedures that are described in the [Amazon Web Services:
Overview of security processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access AWS CodeStar Notifications and AWS CodeConnections through the network. Clients must
support Transport Layer Security (TLS) 1.0 or later. Clients must also support cipher suites
with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve
Ephemeral Diffie-Hellman (ECDHE). Most modern systems support these modes.

Requests must be signed by using an access key ID and a secret access key that is
associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary
security credentials to sign requests.

## Traffic between AWS CodeConnections

resources across Regions

If you use the connections feature to enable connection of your resources, you agree and
instruct us to store and process information associated with such connection resources in
AWS Regions outside the AWS Regions where you are using the underlying service, solely
in connection with, and for the sole purpose of, providing connection to such resources in
Regions other than the one where the resource was created.

For more information, see [Global resources in
AWS CodeConnections](welcome-connections-how-it-works-global.md "welcome-connections-how-it-works-global.md").

###### Note

If you use the connections feature to enable connection for your resources in Regions
that do not require first being enabled, we will store and process information as
detailed in the preceding topics.

For connections established in Regions that must first be enabled, such as the
Europe (Milan) Region, we will only store and process information for that
connection in that Region.
