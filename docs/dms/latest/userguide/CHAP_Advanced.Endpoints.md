# Security group configuration

for AWS DMS

Security group in AWS DMS must allow inbound and outbound connections for your
replication instances on the appropriate database port. If you are using Amazon RDS, you
must configure the security group between DMS and RDS for your instances.

You must perform the following steps:

###### Configure the RDS instance security group

1. Navigate to the [Amazon
   VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane on the left under **Security**,
   select **Security Groups**.
3. Select the RDS Security Group associated with your RDS instance.
4. Edit the inbound rules:
   1. Click **Actions** and select **Edit
      inbound rules**.
   2. Click **Add Rule** to create a new rule.
   3. Configure the rule as follows:
      - **Type**: Select your
        database type (Example: MySQL/Aurora for port 3306,
        PostgreSQL for port 5432).
      - **Protocol**: This
        auto-populates based on your database type.
      - **Port Range**: this
        auto-populates based on your database type.
      - **Source**: Choose
        **Custom**, and paste the security
        group ID associated with your DMS instance. This allows
        traffic from any resource within that security group. You
        can also specify the IP range (CIDR block) of your DMS
        instance.

   4. Click **Save rules**.

###### Configure the DMS replication instance security group

1. Navigate to the [Amazon
   VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane on the left under **Security**,
   select **Security Groups**.
3. In the **Security Group** list find and select the
   security group associated with your DMS replication instance.
4. Edit the outbound rules:
   1. Click **Actions** and select **Edit
      outbound rules**.
   2. Click **Add Rule** to create a new rule.
   3. Configure the rule as follows:
      - Type: Select your database type (Example: MySQL/Aurora,
        PostgreSQL).
      - Protocol: This auto-populates based on your database
        type.
      - Port Range: this auto-populates based on your database
        type.
      - Source: Choose **Custom**, and paste the
        security group ID associated with your RDS instance. This
        allows traffic from any resource within that security group.
        You can also specify the IP range (CIDR block) of your RDS
        instance.

   4. Click **Save rules**.

## Additional

Considerations

You must consider the following additional configuration information:

- **Use Security Group References**:
  Referencing security groups in the source or destional instances allows
  for dynamic management and is more secure than using IP addresses as it
  automatically included all resources within the group.
- **Database Ports**: Ensure you are using
  the correct port for your database.
- **Security Best Practices**: Only open
  the necessary ports to minimize security risks. you must also regular
  review of your security group rules to ensure they meed your security
  standards and requirements.
