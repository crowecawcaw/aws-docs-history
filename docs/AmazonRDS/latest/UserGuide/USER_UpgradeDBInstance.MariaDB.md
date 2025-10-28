# Major version upgrades for RDS for MariaDB

Major version upgrades can contain database changes that are not backward-compatible
with existing applications. As a result, Amazon RDS doesn't apply major version upgrades
automatically. You must manually modify your DB instance. We recommend that you
thoroughly test any upgrade before applying it to your production instances.

###### Note

In MariaDB 11.8, the default value for `require_secure_transport` is now `1`, requiring secure SSL/TLS connections. Set to `0` if non-secure connections are needed.

Amazon RDS supports the following in-place upgrades for major versions of the MariaDB database engine:

- Any MariaDB version to MariaDB 11.8
- Any MariaDB version to MariaDB 11.4
- Any MariaDB version to MariaDB 10.11
- Any MariaDB version to MariaDB 10.6
- MariaDB 10.4 to MariaDB 10.5
  If you are using a custom parameter group, and you perform a major version upgrade,
  you must specify either a default parameter group for the new DB engine version or
  create your own custom parameter group for the new DB engine version. Associating the
  new parameter group with the DB instance requires a customer-initiated database reboot
  after the upgrade completes. The instance's parameter group status will show
  `pending-reboot` if the instance needs to be rebooted to apply the
  parameter group changes. An instance's parameter group status can be viewed in the
  AWS Management Console or by running a "describe" call such as
  `describe-db-instances`.
