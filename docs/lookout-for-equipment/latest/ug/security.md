On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Security in Amazon Lookout for Equipment

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from
data centers and network architectures that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the
cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the AWS
  Cloud. AWS also provides you with services that you can use securely. Third-party
  auditors regularly test and verify the effectiveness of our security as part of the
  [AWS Compliance
  Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance
  programs that apply to Amazon Lookout for Equipment, see [AWS
  Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility
  is determined by the AWS service that you use. You are also responsible for other
  factors including the sensitivity of your data, your company’s requirements, and
  applicable laws and regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using Lookout for Equipment. The following topics show you how to configure Lookout for Equipment to meet
  your security and compliance objectives. You also learn how to use other Amazon Web Services services that
  help you to monitor and secure your Lookout for Equipment resources.

###### Topics

- [Data protection in Amazon Lookout for Equipment](data-protection.md "data-protection.md")
- [Identity and access management for Amazon Lookout for Equipment](security-iam.md "security-iam.md")
- [Amazon Lookout for Equipment and interface VPC endpoints
  (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md")
- [Compliance validation for Amazon Lookout for Equipment](SERVICENAME-compliance.md "SERVICENAME-compliance.md")
- [Resilience in Amazon Lookout for Equipment](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure security in
  Amazon Lookout for Equipment](#infrastructure-security "#infrastructure-security")

## Infrastructure security in

Amazon Lookout for Equipment

As a managed service, Amazon Lookout for Equipment is protected by the AWS global network security
procedures that are described in the [Amazon
Web Services: Overview of Security Processes whitepaper](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf").

You use published AWS API calls to access Amazon Lookout for Equipment through the network. Clients
must support Transport Layer Security (TLS) 1.2 or later. Clients must also support cipher
suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic
Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support
these modes.

Requests must be signed by using an access key ID and a secret access key that is
associated with an IAM principal. If you don't have an access key and a secret access key,
you can use the AWS Security Token Service to generate temporary security credentials to sign requests.
