# Network Access Control List (NACL)

configuration for AWS DMS

When using Amazon RDS as a replication source, you should update the Network Access
Control Lists (NACLs) for your DMS and RDS instance. Ensure that the NACLs are
associated with the subnets where these instances reside. This allows inbound and
outbound traffic on the specific database port.

To update the Network Access Control Lists, you must perform the following
steps:

###### Note

If your DMS and RDS instances are in the same subnet, you only need to update
that subnet's NACL.

###### Identify the relevant NACLs

1. Navigate to the [Amazon
   VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane on the left under **Security**,
   select **Network ACLs**.
3. Select the relevant NACLs associated with the subnets where your DMS and
   RDS instances reside.

###### Update the NACLs for the DMS instance subnet

1. Identify the NACL associated with your DMS instance's subnet. To do so,
   you can browse through the subnets in the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"),
   find the DMS subnet, and note the associated NACL ID.
2. Edit the inbound rules:
   1. Click the **Inbound Rules** tab for the selected
      NACL.
   2. Select **Edit inbound rules**.
   3. Add a new rule:
      - **Rule #**: Choose a unique
        number (Example: 100).
      - **Type**: Select
        **Custom TCP Rule**.
      - **Protocol**: TCP
      - **Port Range**: Enter your
        database port (Example: 3306 for MySQL).
      - **Source**: Enter the CIDR
        block of the RDS subnet (Example: 10.1.0.0/16).
      - **Allow/Deny**: Select
        **Allow**.

3. Edit the outbound rules:
   1. Click the **Outbound Rules** tab for the selected
      NACL.
   2. Click **Edit outbound rules**.
   3. Add a new rule:
      - **Rule #**: Use the same
        number as used in the inbound rules.
      - **Type**: All traffic.
      - **Destination**:
        0.0.0.0/0
      - **Allow/Deny**: Select
        **Allow**.

4. Click **Save changes**.
5. Perform the same steps to update the NACLs associated with the RDS
   instance's subnet.

## Verify the NACL rules

You must ensure the following criteria for regarding the NACL rules.:

- **Order of rules**: NACLs processes rules
  in the ascending order based on th erule number. Ensure that all the
  rules set as "**Allow**" have lower rule
  numbers than all the rules set as "**Deny**" as that might block traffic.
- **Stateless nature**: NACLs are
  stateless. You must explicity allow both inbound and outbound
  traffic.
- **CIDR blocks**: You must ensure that the
  CIDR blocks you use accurately represent the subnets of your DMS and RDS
  instances.
