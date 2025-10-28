# Setting up public or private access in Amazon RDS

When you create an Amazon RDS DB instance, one of the most important decisions you make is
determining how others can access it. Depending on your use case, users and applications can
access your database either from the internet (public access) or from a restricted private
network within your AWS environment. Choosing the right access configuration is essential to
balance security and connectivity.

###### Note

By default, the **Easy create** option sets your database
to private access, meaning it's only accessible from within your VPC. This configuration
enhances security by restricting internet exposure. However, if you need a simpler
connection process for testing or development purposes, consider changing to public access.
Public access allows connections from the internet.

This section helps you understand the key differences between public and private access,
and the benefits and risks associated with each. By the end of this section, you'll be able to
choose and set up the appropriate access type for your workload.

###### Topics

- [Public access](#security-public "#security-public")
- [Private access](#security-private "#security-private")
- [Next steps](#security-public-private-next-steps "#security-public-private-next-steps")

## Public access

A publicly accessible DB instance has a public IP address, which allows users to reach
it directly from the internet. Use this configuration for applications that need remote
access but require strict access control. For example, you might allow access only from a
corporate IP range or specific developer machines.

You can use this setup for the following use cases:

- **External applications**: You need to connect a
  database to applications hosted outside of AWS.
- **Testing and development**: You're developing or
  testing from your local machine and need direct access.

**Risks**: Publicly accessible databases are vulnerable to
potential threats from the internet.

**Considerations**: If you enable public access, you must
apply strict access controls. For example, you can use the following strategies:

- Configure inbound rules in the security group to allow only trusted IP
  addresses.
- Ensure strong authentication and encryption are in place to prevent unauthorized
  access.

## Private access

A private DB instance is accessible only within your VPC. It doesn't have a public IP
address, and you can't reach it from the internet. You can use private access for scenarios
like internal microservices connecting to the database within the same VPC.

This configuration is best for the following use cases:

- **Internal applications**: Databases used by
  applications within the same VPC or a connected on-premises network.
- **High-security requirements**: Workloads that require
  stringent access control, such as financial or healthcare applications.

**Benefits**: Private access minimizes exposure to external
threats because RDS isolates the database from the public internet.

**Considerations**: For private databases, you need to
establish connectivity through private resources. For example, you can use the following
strategies:

- Set up an AWS VPN or AWS Direct Connect for on-premises access.
- Use a bastion host or VPN for administrative tasks from outside the VPC.

The decision between public and private access must align with your application
architecture and security requirements. Public access can simplify connectivity during early
development or testing, but private access is better for production workloads or sensitive
data.

If you use the **Easy create** option when you create a DB instance, it
uses private access by default. To change the access type, modify the DB instance.
In the **Connectivity** section, expand
**Additional configuration** and change the **Public
access** setting.

![Public access options for RDS cluster: Yes with public IP, No for VPC-only access.](images/public-access.png)

For more information, see [Settings for DB
instances](../UserGuide/USER_ModifyInstance.md "../UserGuide/USER_ModifyInstance.md") in the _Amazon RDS User Guide_.

## Next steps

Now that you decided on public or private access for your DB instance, the next step is
to define who can connect to your DB instance.

**Next step:** [Determining who can connect to your Amazon RDS DB
instance](security-groups.md "security-groups.md")
