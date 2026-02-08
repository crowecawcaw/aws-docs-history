# MSFTCOST06-BP02 Use AD Connector

AD Connector is a directory gateway with which you can redirect
directory requests to your on-premises Microsoft Active Directory
without caching any information in the cloud. AD Connector comes in
two sizes, small and large. A small AD Connector is designed for
smaller organizations and is intended to handle a low number of
operations per second. A large AD Connector is designed for larger
organizations and is intended to handle a moderate to high number of
operations per second. You can spread application loads across
multiple AD Connectors to scale to your performance needs. There are
no enforced user or connection limits.

**Desired outcome:** By implementing
AD Connector, the organization may achieve seamless integration
between on-premises Microsoft Active Directory and AWS Cloud
services without data replication or cloud caching. The solution
will be appropriately sized (small or large) based on operational
requirements, with the flexibility to add multiple AD Connectors for
increased performance as needed, ensuring cost-effective directory
services management while maintaining security and scalability.

**Common anti-patterns:**

- Replicating the entire on-premises Active Directory to AWS using
  AWS Managed Microsoft AD or EC2 instances running AD Domain
  Controllers, when only authentication and authorization services
  are required, leading to increased attack surface, higher costs,
  and unnecessary data duplication.
- Implementing AWS Managed Microsoft AD when only directory
  authentication is needed, resulting in higher operational costs
  and unnecessary complexity when AD Connector could provide the
  same functionality through simple proxying of authentication
  requests to the existing on-premises Active Directory.

**Benefits of establishing this best
practice:**

- AD Connector eliminates the need for complex directory
  synchronization solutions or maintaining separate directory
  infrastructures in the cloud, reducing both capital and
  operational expenses associated with directory services
  management.
- By not storing or caching any directory information in the
  cloud, AD Connector minimizes the risk of data breaches and
  maintains a smaller attack surface, while still allowing AWS
  resources to leverage existing on-premises Active Directory for
  authentication and authorization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement AD Connector effectively, start by assessing your
organization's directory service needs and sizing requirements.
Choose between small and large AD Connector options based on your
expected operation volume. Ensure your on-premises Active
Directory is properly configured and accessible from your AWS VPC
through a secure connection, such as AWS Direct Connect or a VPN.
Set up the AD Connector in your VPC, configure the necessary
security groups, and test the connection thoroughly. For high
availability, consider deploying AD Connectors in multiple
Availability Zones. Finally, integrate your AWS resources and
applications with AD Connector for seamless authentication and
authorization using your existing Active Directory credentials.

### Implementation steps

1. Establish network connectivity between AWS and on-premises
   environment through either AWS Direct Connect or AWS Site-to-Site VPN, ensuring proper routing and security group
   configurations are in place.
2. Deploy AD Connector in your VPC, selecting the appropriate
   size (small or large) based on your organization's
   authentication operation volume and configuring it with your
   on-premises Active Directory service account credentials.
3. Test AD Connector functionality by verifying authentication
   flows and ensuring proper communication between AWS
   resources and your on-premises Active Directory.
4. Enable and configure AWS services and applications to use AD
   Connector for authentication, including AWS Management Console access and AWS Enterprise Applications that support
   SAML 2.0.

## Resources

**Related documents:**

- [AD
  Connector](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-connector.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-connector.md")
