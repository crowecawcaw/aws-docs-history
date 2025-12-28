# Updating the VPC for a DB instance

You can use the AWS Management Console to move your DB instance to a different VPC.

For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). In the
**Connectivity** section of the modify page, shown following, enter
the new DB subnet group for **DB subnet group**. The new subnet group
must be a subnet group in a new VPC.

![Modify the DB instance subnet group.](images/EC2-VPC.png)
You can't change the VPC for a DB instance if the following conditions apply:

- The DB instance is in multiple Availability Zones. You can convert the DB
  instance to a single Availability Zone, move it to a new VPC, and then convert
  it back to a Multi-AZ DB instance. For more information, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").
- The DB instance has one or more read replicas. You can remove the read
  replicas, move the DB instance to a new VPC, and then add the read replicas
  again. For more information, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").
- The DB instance is a read replica. You can promote the read replica, and then
  move the standalone DB instance to a new VPC. For more information, see [Promoting a read replica to be a standalone
  DB instance](USER_ReadRepl.md "USER_ReadRepl.md").
- The subnet group in the target VPC doesn't have subnets in the DB instance's
  the Availability Zone. You can add subnets in the DB instance's Availability
  Zone to the DB subnet group, and then move the DB instance to the new VPC. For
  more information, see [Working with DB subnet groups](USER_VPC.md#USER_VPC.Subnets "USER_VPC.md#USER_VPC.Subnets").
