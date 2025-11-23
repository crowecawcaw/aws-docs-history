# Working with an instance store on an Oracle read replica

Read replicas support the flash cache and temporary tablespaces on an instance store. While the flash cache works the same way as on the
primary DB instance, note the following differences for temporary tablespaces:

- You can't create a temporary tablespace on a read replica. If you create a new temporary tablespace on the primary instance,
  RDS for Oracle replicates the tablespace information without tempfiles. To add a new tempfile, use either of the following
  techniques:
  - Use the Amazon RDS procedure `rdsadmin.rdsadmin_util.add_inst_store_tempfile`. RDS for Oracle creates a tempfile in the
    instance store on your read replica, and adds it to the specified temporary tablespace.
  - Run the `ALTER TABLESPACE … ADD TEMPFILE` command. RDS for Oracle places the tempfile on Amazon EBS storage.

###### Note

The tempfile sizes and storage types can be different on the primary DB instance and the read replica.

- You can manage the default temporary tablespace setting only on the primary DB instance. RDS for Oracle replicates the setting to all
  read replicas.
- You can configure the temporary tablespace groups only on the primary DB instance. RDS for Oracle replicates the setting to all read
  replicas.
