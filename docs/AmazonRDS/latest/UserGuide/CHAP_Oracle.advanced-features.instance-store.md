# Configuring an RDS for Oracle instance store

By default, 100% of instance store space is allocated to the temporary tablespace. To configure the instance store to allocate space to
the flash cache and temporary tablespace, set the following parameters in the parameter group for your instance:

**db_flash_cache_size={DBInstanceStore\*{0,2,4,6,8,10}/10}**

This parameter specifies the amount of storage space allocated for the flash cache. This parameter is valid only for Oracle
Database Enterprise Edition. The default value is `{DBInstanceStore*0/10}`. If you set a nonzero value for
`db_flash_cache_size`, your RDS for Oracle instance enables the flash cache after you restart the instance.

**rds.instance_store_temp_size={DBInstanceStore\*{0,2,4,6,8,10}/10}**

This parameter specifies the amount of storage space allocated for the temporary tablespace. The default value is
`{DBInstanceStore*10/10}`. This parameter is modifiable for Oracle Database Enterprise Edition and read-only
for Standard Edition 2. If you set a nonzero value for `rds.instance_store_temp_size`, Amazon RDS allocates space in the
instance store for the temporary tablespace.

You can set the `db_flash_cache_size` and `rds.instance_store_temp_size` parameters for DB instances
that don't use an instance store. In this case, both settings evaluate to `0`, which turns off the feature. In this
case, you can use the same parameter group for different instance sizes and for instances that don't use an instance store. If
you modify these parameters, make sure to reboot the associated instances so that the changes can take effect.

###### Important

If you allocate space for a temporary tablespace, Amazon RDS doesn't create the temporary tablespace automatically. To learn
how to create the temporary tablespace on the instance store, see [Creating a temporary tablespace on the instance store](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.creating-tts-instance-store "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.creating-tts-instance-store").

The combined value of the preceding parameters must not exceed 10/10, or 100%. The following table illustrates valid and invalid
parameter settings.

| db_flash_cache_size setting                  | rds.instance_store_temp_size setting                  | Explanation                                                                                                                                                                                                     |
| -------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| db_flash_cache_size={DBInstanceStore\*0/10}  | rds.instance_store_temp_size={DBInstanceStore\*10/10} | This is a valid configuration for all editions of Oracle Database. Amazon RDS allocates 100% of instance store space to<br>the temporary tablespace. This is the default.                                       |
| db_flash_cache_size={DBInstanceStore\*10/10} | rds.instance_store_temp_size={DBInstanceStore\*0/10}  | This is a valid configuration for Oracle Database Enterprise Edition only. Amazon RDS allocates 100% of instance store<br>space to the flash cache.                                                             |
| db_flash_cache_size={DBInstanceStore\*2/10}  | rds.instance_store_temp_size={DBInstanceStore\*8/10}  | This is a valid configuration for Oracle Database Enterprise Edition only. Amazon RDS allocates 20% of instance store<br>space to the flash cache, and 80% of instance store space to the temporary tablespace. |
| db_flash_cache_size={DBInstanceStore\*6/10}  | rds.instance_store_temp_size={DBInstanceStore\*4/10}  | This is a valid configuration for Oracle Database Enterprise Edition only. Amazon RDS allocates 60% of instance store<br>space to the flash cache, and 40% of instance store space to the temporary tablespace. |
| db_flash_cache_size={DBInstanceStore\*2/10}  | rds.instance_store_temp_size={DBInstanceStore\*4/10}  | This is a valid configuration for Oracle Database Enterprise Edition only. Amazon RDS allocates 20% of instance store space<br>to the flash cache, and 40% of instance store space to the temporary tablespace. |
| db_flash_cache_size={DBInstanceStore\*8/10}  | rds.instance_store_temp_size={DBInstanceStore\*8/10}  | This is an invalid configuration because the combined percentage of instance store space exceeds 100%. In such<br>cases, Amazon RDS fails the attempt.                                                          |

## Considerations when changing the DB instance type

If you change your DB instance type, it can affect the configuration of the flash cache or the temporary tablespace on the instance
store. Consider the following modifications and their effects:

**You scale up or scale down the DB instance that supports the instance
store.**

The following values increase or decrease proportionally to the new size of the instance store:

- The new size of the flash cache.
- The space allocated to the temporary tablespaces that reside in the instance store.

For example, the setting `db_flash_cache_size={DBInstanceStore*6/10}` on a db.m5d.4xlarge instance provides
around 340 GB of flash cache space. If you scale up the instance type to db.m5d.8xlarge, the flash cache space increases to
around 680 GB.

**You modify a DB instance that doesn't use an instance store to an instance
that does use an instance store.**

If `db_flash_cache_size` is set to a value larger than `0`, the flash cache is configured. If
`rds.instance_store_temp_size` is set to a value larger than `0`, the instance store space is
allocated for use by a temporary tablespace. RDS for Oracle doesn't move tempfiles to the instance store automatically. For
information about using the allocated space, see [Creating a temporary tablespace on the instance store](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.creating-tts-instance-store "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.creating-tts-instance-store") or [Adding a tempfile to the instance store on a read replica](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.adding-tempfile-replica "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.adding-tempfile-replica").

**You modify a DB instance that uses an instance store to an instance that
doesn't use an instance store.**

In this case, RDS for Oracle removes the flash cache. RDS re-creates the tempfile that is currently located on the instance store
on an Amazon EBS volume. The maximum size of the new tempfile is the former size of the `rds.instance_store_temp_size`
parameter.
