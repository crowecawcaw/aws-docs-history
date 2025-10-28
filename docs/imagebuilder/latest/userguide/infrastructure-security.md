# Infrastructure security in Image Builder

The AWS global network provides security capabilities and controls network access
for services like EC2 Image Builder. For more information about the infrastructure security that
AWS provides for its services, see the [Infrastructure Security](../../../whitepapers/latest/introduction-aws-security/infrastructure-security.md "../../../whitepapers/latest/introduction-aws-security/infrastructure-security.md") section in the _Introduction to AWS
Security_ whitepaper.

To send requests through the AWS global network for Image Builder API actions, your client
software must comply with the following security guidelines:

- To send requests for Image Builder API actions, client software must use a
  supported version of Transport Layer Security (TLS).

###### Note

AWS is phasing out support for TLS versions 1.0 and 1.1. We
strongly recommend that you update your client software to use TLS version 1.2
or later so that you can still connect. For more information, see this
[AWS
Security Blog post](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/").

- Client software must support cipher suites with perfect forward secrecy (PFS), such
  as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE).
  Most current systems, such as Java 7 and later, support these modes.
- You must sign your API requests with an access key ID and a secret access
  key that is associated with an AWS Identity and Access Management (IAM) principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/welcome.md "../../../STS/latest/APIReference/welcome.md")
  (AWS STS) to generate temporary security credentials for your requests.
  Additionally, the EC2 instances that Image Builder uses to build and test images must have access to
  AWS Systems Manager.
