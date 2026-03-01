# Determining who can connect to your Amazon RDS DB instance

Security groups act as virtual firewalls for your Amazon RDS DB instance, controlling inbound
and outbound traffic. It's important to properly configure security groups to ensure that only
trusted connections can access your database.

###### Topics

- [Purpose of security groups and default behavior](#security-groups-purpose "#security-groups-purpose")
- [Configuring inbound and outbound rules](#security-groups-rules "#security-groups-rules")
- [Next steps](#security-groups-next-steps "#security-groups-next-steps")

## Purpose of security groups and default behavior

Security groups in RDS determine which IP addresses and ports can connect to your DB
instance. By default, each DB instance has the following behavior:

- Blocks all inbound traffic.
- Allows outbound traffic to all destinations.

To connect to your DB instance, you must explicitly define inbound rules that specify
allowed IP addresses, protocols, and port numbers. This setup prevents unauthorized access
and grants flexibility for trusted connections.

## Configuring inbound and outbound rules

Follow these steps to configure inbound and outbound rules for your security
group.

###### To configure inbound and outbound rules

1. Navigate to the **Amazon EC2 console** and choose **Security
   Groups** under the **Network & Security** menu.
2. Select or create a security group for your DB instance.
3. Configure inbound rules:
   - Add a rule to allow access on the database port (for example, port 3306 for
     MySQL) from a specific IP address or IP range.
   - For the **Source**, choose **My IP** for
     personal access, or specify a CIDR block for broader access.

   For example, you might allow inbound traffic from an application hosted on an
   EC2 instance within the same VPC by specifying the EC2 instance security group as
   the source.

   ![Inbound rules configuration with Custom TCP type, port 3306, and source IP address.](images/security-group.png)

4. (Optional) Adjust outbound rules. Typically, you don't need to make any changes
   because the DB instance allows all outbound traffic by default.
5. Save your changes and associate the security group with your DB instance in the RDS
   console. Modify the DB instance and choose the new security group in the
   **Connectivity** section.

For more information, see [Controlling access with
security groups](../UserGuide/Overview.md "../UserGuide/Overview.md") in the _Amazon RDS User Guide_.

## Next steps

After you explicitly define at least one inbound rule that allows an IP address to
access your DB instance, the next step is to decide on a database authentication option.

###### Note

The **Easy create** option for database creation uses password
authentication by default, which is the simplest option. If you want to explore advanced
authentication options, proceed to the next step. Otherwise, you can skip directly to
connecting to your DB instance.

**Next step:** [Database authentication options for Amazon RDS](database-auth.md "database-auth.md") or [Connecting to your Amazon RDS DB instance](connecting.md "connecting.md")
