**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Internetwork traffic

privacy

_Internetwork traffic privacy_ refers to securing
connections and traffic between Amazon Pinpoint and your on-premises clients and applications, and
between Amazon Pinpoint and other AWS resources in the same AWS Region. The following features and
practices can help you ensure internetwork traffic privacy for Amazon Pinpoint.

## Traffic between

Amazon Pinpoint and on-premises clients and applications

To establish a private connection between Amazon Pinpoint and clients and applications on your
on-premises network, you can use AWS Direct Connect. This enables you to link your network to an
AWS Direct Connect location by using a standard, fiber-optic Ethernet cable. One end of the
cable is connected to your router. The other end is connected to an AWS Direct Connect router. For
more information, see [What is
AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") in the _AWS Direct Connect User Guide_.

To help secure access to Amazon Pinpoint through published APIs, we recommend that you comply
with Amazon Pinpoint requirements for API calls. Amazon Pinpoint requires clients to use Transport Layer
Security (TLS) 1.2 or later. Clients must also support cipher suites with perfect
forward secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve
Diffie-Hellman Ephemeral (ECDHE). Most modern systems such as Java 7 and later support
these modes.

In addition, requests must be signed using an access key ID and a secret access key
that's associated with an AWS Identity and Access Management (IAM) principal for your AWS account.
Alternatively, you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

## Traffic between

Amazon Pinpoint and other AWS resources

To secure communications between Amazon Pinpoint and other AWS resources in the same AWS
Region, Amazon Pinpoint uses HTTPS and TLS 1.2 by default.
