# Considerations for RDS Custom for Oracle OS upgrades

When you plan an OS upgrade, consider the following:

- You can't provide your own AMI for use in an RDS Custom for Oracle CEV. You can specify either the
  default AMI, which uses Oracle Linux 8, or an AMI that has been previously used by an
  RDS Custom for Oracle CEV.

###### Note

RDS Custom for Oracle releases a new default AMI when common vulnerabilities and exposures are
discovered. No fixed schedule is available or guaranteed. RDS Custom for Oracle tends to publish a
new default AMI every 30 days.

- When you upgrade the OS in your primary DB instance, you must upgrade its associated
  read replicas manually.
- Reserve sufficient Amazon EC2 compute capacity for your instance type in your AZ before
  you begin patching the OS.

When you create a Capacity Reservation, you specify the AZ, number of instances,
and instance attributes (including instance type). For example, if your DB instance uses
the underlying EC2 instance type r5.large, we recommend that you reserve EC2
capacity for r5.large in your AZ. During OS patching, RDS Custom creates one new host of
type db.r5.large, which can become stuck if the AZ lacks EC2 capacity for this
instance type. If you reserve EC2 capacity, you lower the risk of blocked patching
caused by capacity constraints. For more information, see [On-Demand Capacity
Reservations](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") in the _Amazon EC2 User Guide_.

- Back up your DB instance before you upgrade its OS. The upgrade removes your root volume
  data and any existing OS customizations.
- In the shared responsibility model, you're responsible for keeping your OS up to
  date. RDS Custom for Oracle doesn't mandate which patches you apply to your OS. If your
  RDS Custom for Oracle is functional, you can use the AMI associated with this CEV
  indefinitely.
