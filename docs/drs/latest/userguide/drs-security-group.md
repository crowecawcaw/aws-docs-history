# Elastic Disaster Recovery security groups

A security group acts as a virtual firewall, which controls the inbound and
outbound traffic of the staging area. We recommend that you have AWS Elastic Disaster Recovery
automatically attach and monitor the default Elastic Disaster Recovery security group. This group
opens inbound TCP Port 1500 for receiving the transferred replicated data. When
you use the default DRS; security group Elastic Disaster Recovery constantly monitors whether the
rules within this security group are enforced, in order to maintain
uninterrupted data replication. If these rules are altered, Elastic Disaster Recovery automatically
fixes the issue. Choose:

- Recommended - Select **Always use AWS Elastic Disaster Recovery security group**
  to allow data to flow from your source servers to the replication
  servers, and so that the replication servers can communicate their state
  to the AWS Elastic Disaster Recovery servers.
- Not recommended - Deselect **Always use AWS Elastic Disaster Recovery security
  group** option. Then, select
  the drop-down menu to choose from the list of available security groups.
  The list of available security groups changes according to the **Staging area subnet** that you selected.
  - To search for a specific security group, use the search box.
  - If you add security groups via the AWS Console, they appear on the
    Security group drop-down list in the AWS Elastic Disaster Recovery Console. Learn more about
    AWS security groups in [this VPC article](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md").
  - Any security group that you select is added to the default AWS Elastic Disaster Recovery
    group, because the default security group is essential for the operation
    of AWS Elastic Disaster Recovery.
