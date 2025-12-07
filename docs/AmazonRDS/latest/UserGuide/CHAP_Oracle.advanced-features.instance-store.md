# Configuring a temporary tablespace group on an instance store and

Amazon EBS

You can configure a temporary tablespace group to include temporary tablespaces on both an instance store and Amazon EBS. This technique is
useful when you want more temporary storage than is allowed by the maximum setting of `rds.instance_store_temp_size`.

When you configure a temporary tablespace group on both an instance store and Amazon EBS, the two tablespaces have significantly different
performance characteristics. Oracle Database chooses the tablespace to serve queries based on an internal algorithm. Therefore, similar
queries can vary in performance.

Typically, you create a temporary tablespace in the instance store as follows:

1. Create a temporary tablespace in the instance store.
2. Set the new tablespace as the database default temporary tablespace.
   If the tablespace size in the instance store is insufficient, you can create additional temporary storage as follows:

3. Assign the temporary tablespace in the instance store to a temporary tablespace group.
4. Create a new temporary tablespace in Amazon EBS if one doesn't exist.
5. Assign the temporary tablespace in Amazon EBS to the same tablespace group that includes the instance store tablespace.
6. Set the tablespace group as the default temporary tablespace.
   The following example assumes that the size of the temporary tablespace in the instance store doesn't meet your application
   requirements. The example creates the temporary tablespace `temp_in_inst_store` in the instance store, assigns it to tablespace
   group `temp_group`, adds the existing Amazon EBS tablespace named `temp_in_ebs` to this group, and sets this group as the
   default temporary tablespace.

```
SQL> EXEC rdsadmin.rdsadmin_util.create_inst_store_tmp_tblspace('`temp_in_inst_store`');

PL/SQL procedure successfully completed.

SQL> ALTER TABLESPACE `temp_in_inst_store` TABLESPACE GROUP `temp_group`;

Tablespace altered.

SQL> ALTER TABLESPACE `temp_in_ebs` TABLESPACE GROUP `temp_group`;

Tablespace altered.

SQL> EXEC rdsadmin.rdsadmin_util.alter_default_temp_tablespace('`temp_group`');

PL/SQL procedure successfully completed.

SQL> SELECT * FROM DBA_TABLESPACE_GROUPS;

GROUP_NAME                     TABLESPACE_NAME
------------------------------ ------------------------------
TEMP_GROUP                     TEMP_IN_EBS
TEMP_GROUP                     TEMP_IN_INST_STORE

SQL> SELECT PROPERTY_VALUE FROM DATABASE_PROPERTIES WHERE PROPERTY_NAME='DEFAULT_TEMP_TABLESPACE';

PROPERTY_VALUE
--------------
TEMP_GROUP
```
