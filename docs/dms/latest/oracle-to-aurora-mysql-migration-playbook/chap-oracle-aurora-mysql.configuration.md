# Oracle instance parameters and Aurora MySQL parameter groups

With AWS DMS, you can configure database settings to optimize performance, security, and resource utilization during and after migrating databases to Amazon Aurora. Oracle instance parameters and Aurora MySQL parameter groups define settings that govern database behavior, such as memory allocation, query optimization, and security policies.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                              |
| ------------------------------ | ---------------------------------- | ------------------------- | -------------------------------------------- |
| One star feature compatibility | N/A                                | N/A                       | Use cluster and database cluster parameters. |

## Oracle usage

You can configure Oracle instance and database-level parameters using the `ALTER SYSTEM` command. You can configure certain parameters dynamically and take immediate effect while other parameters require an instance restart.

- All Oracle instance and database-level parameters are stored in a binary file known as the Server Parameter file (`SPFILE`).
- The binary `SPFILE` can be exported to a text file using the following command:

```
CREATE PFILE = 'my_init.ora'
FROM SPFILE = 's_params.ora';
```

When you modify parameters, you can choose the persistence of the changed values with one of the three following options:

- Make the change applicable only after a restart by specifying `scope=spfile`.
- Make the change dynamically, but not persistent , after a restart by specifying `scope=memory`.
- Make the change both dynamically and persistent by specifying `scope=both`.

### Examples

Use the `ALTER SYSTEM SET` command to configure a value for an Oracle parameter.

```
ALTER SYSTEM SET QUERY_REWRITE_ENABLED = TRUE SCOPE=BOTH;
```

For more information, see [Initialization Parameters](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/initialization-parameters-2.html#GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/initialization-parameters-2.html#GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61") and [Changing Parameter Values in a Parameter File](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html") in the _Oracle documentation_.

## MySQL usage

When you run MySQL databases as Amazon Aurora clusters, you can use parameter groups to change the cluster-level and database-level parameters.

Most of the MySQL parameters are configurable in an Amazon Aurora MySQL cluster, but some are disabled and cannot be modified. Since Amazon Aurora clusters restrict access to the underlying operating system, modification to MySQL parameters must be made using Parameter Groups.

Amazon Aurora is a cluster of database instances and, as a direct result, some of the MySQL parameters apply to the entire cluster while other parameters apply only to a particular database instance.

| Aurora MySQL parameter class                                                                                                                  | Controlled through                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster-level parameters**<br>Single cluster parameter group for each Amazon Aurora cluster                                                 | Managed using cluster parameter groups.<br>Consider the following example:<br>`<br>aurora_load_from_s3_role,<br>default_password_lifetime,<br>default_storage_engine<br>` |
| **Database instance-level parameters**<br>Every instance in an Amazon Aurora cluster can be associated with a unique database parameter group | Managed using database parameter groups.<br>Consider the following example:<br>`<br>autocommit,<br>connect_timeout,<br>innodb_change_buffer_max_size<br>`                 |

### Examples

**Create and configure a new parameter group**

Follow these steps to create and configure an Amazon Aurora database and cluster parameter groups:

1. Sign in to the AWS Management Console, choose **RDS**, and then choose **Databases**.
2. Choose **Parameter groups**, and choose **Create parameter group**.

###### Note

You can’t edit the default parameter group. Create a custom parameter group to apply changes to your Amazon Aurora cluster and its database instances. 3. For **Parameter group family**, choose **aurora-mysql5.7**. 4. For **Type**, choose **DB parameter group**. 5. Choose **Create**.

**Modify an existing parameter group**

1. Sign in to the AWS Management Console, choose **RDS**, and then choose **Databases**.
2. Choose **Parameter groups**, and choose the name of the parameter to edit.
3. For **Parameter group actions**, choose **Edit**.
4. Change parameter values and choose **Save changes**.

For more information, see [Server System Variables](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html "https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html") in the _MySQL documentation_.
