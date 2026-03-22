# DB instance class support for RDS Custom for SQL Server

Check if the DB instance class is supported in your Region by using the
[describe-orderable-db-instance-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-orderable-db-instance-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-orderable-db-instance-options.html") command.

RDS Custom for SQL Server supports the DB instance classes shown in the following table:

| SQL Server edition | RDS Custom support                                                                                                                                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enterprise Edition | db.r5.xlarge–db.r5.24xlarge<br>db.r5b.xlarge–db.r5b.24xlarge<br>db.m5.xlarge–db.m5.24xlarge<br>db.r6i.xlarge–db.r6i.32xlarge<br>db.m6i.xlarge–db.m6i.32xlarge<br>db.x2iedn.xlarge–db.x2iedn.32xlarge |
| Standard Edition   | db.r5.large–db.r5.24xlarge<br>db.r5b.large–db.r5b.8xlarge<br>db.m5.large–db.m5.24xlarge<br>db.r6i.large–db.r6i.8xlarge<br>db.m6i.large–db.m6i.8xlarge<br>db.x2iedn.xlarge–db.x2iedn.8xlarge          |
| Developer Edition  | db.r5.xlarge–db.r5.24xlarge<br>db.r5b.xlarge–db.r5b.24xlarge<br>db.m5.xlarge–db.m5.24xlarge<br>db.r6i.xlarge–db.r6i.32xlarge<br>db.m6i.xlarge–db.m6i.32xlarge<br>db.x2iedn.xlarge–db.x2iedn.32xlarge |
| Web Edition        | db.r5.large–db.r5.4xlarge<br>db.m5.large–db.m5.4xlarge<br>db.r6i.large–db.r6i.4xlarge<br>db.m6i.large–db.m6i.4xlarge<br>db.r5b.large–db.r5b.4xlarge                                                  |

The following recommendations apply to db.x2iedn class types:

- At creation, local storage is a raw and unallocated device. Before using a DB instance with this
  instance class, you must mount and format the local storage. Afterward,
  configure `tempdb` on it to ensure optimal performance. For more
  information, see
  [Optimize tempdb performance in Amazon RDS Custom for SQL Server using local instance
  storage](https://aws.amazon.com/blogs/database/optimize-tempdb-performance-in-amazon-rds-custom-for-sql-server-using-local-instance-storage/ "https://aws.amazon.com/blogs/database/optimize-tempdb-performance-in-amazon-rds-custom-for-sql-server-using-local-instance-storage/").
- Local storage reverts to its raw and unallocated state when you run DB instance operations such
  as scale compute, instance replacement, snapshot restore, or point-in-time
  recovery (PITR). In these situations, you must remount, reformat, and
  reconfigure the drive and `tempdb` to restore functionality.
- For Multi-AZ instances, we recommend that you perform the configuration on a standby
  DB instance. This way, if a failover occurs, the system continues to operate without
  issues because the configuration is already in place on the standby
  instance.
