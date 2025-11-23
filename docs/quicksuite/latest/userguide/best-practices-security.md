# Best practices for security in

Amazon Quick Suite

Amazon Quick Suite provides a number of security features to consider as you develop and
implement your own security policies. The following best practices are general guidelines
and don’t represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

**Firewall** – To allow
users to access Amazon Quick Suite, allow access to HTTPS and WebSockets Secure (wss://) protocol.
To allow Amazon Quick Suite to reach a database that is on a non-AWS server, change that
server's firewall configuration to accept traffic from the applicable Amazon Quick Suite IP
address range.

**SSL** – Use SSL to
connect to your databases, especially if you are using public networks. Using SSL with
Amazon Quick Suite requires the use of certificates signed by a publicly-recognized certificate
authority (CA).

**Enhanced security** –
Use Amazon Quick Suite Enterprise edition to make use of its enhanced security capabilities,
including the following.

- Store data in SPICE with encryption at rest.
- Integrate Active Directory and IAM Identity Center authentication.
- Securely access data in private VPCs and on-premises.
- Limit access to data with row level security.
  **VPC** – (Enterprise
  Edition) Use a virtual private cloud (VPC) for data in AWS data sources and for data in
  on-premises servers without public connectivity. For AWS sources, VPC access for
  Amazon Quick Suite uses an elastic network interface for secure, private communication with data
  sources in a VPC. For your local data, VPC allows you to use Direct Connect to create a secure,
  private link with your on-premises resources.
