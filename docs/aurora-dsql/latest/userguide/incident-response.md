# Incident response in Amazon Aurora DSQL

Security is the highest priority at AWS. As part of the AWS Cloud shared responsibility model, AWS manages a data center, network,
and software architecture that meets the requirements of the most security-sensitive organizations. AWS is responsible for any incident
response with respect to the Amazon Aurora DSQL service itself. Also, as an AWS customer, you share a responsibility for maintaining
security in the cloud. This means that you control the security you choose to implement from the AWS tools and features
you have access to. In addition, you’re responsible for incident response on your side of the shared responsibility model.

By establishing a security baseline that meets the objectives for your applications running in the cloud, you're able
to detect deviations that you can respond to. To help you understand the impact that incident response and your choices have on
your corporate goals, we encourage you to review the following resources:

- [AWS Security Incident Response Guide](../../../whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.md "../../../whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.md")
- [AWS Best Practices for Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/")
- [Security Perspective of the AWS Cloud Adoption Framework (CAF) whitepaper](../../../whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.md "../../../whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.md")
  [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") is a managed threat detection service continuously monitoring
  malicious or unauthorized behavior to help customers protect AWS accounts and workloads and identify suspicious activity
  potentially before it escalates into an incident. It monitors activity such as unusual API calls or potentially
  unauthorized deployments indicating possible account or resource compromise or reconnaissance by bad actors. For example,
  Amazon GuardDuty is able to detect suspicious activity in Amazon Aurora DSQL APIs, such as a user logging in from a new location and creating a new cluster.
