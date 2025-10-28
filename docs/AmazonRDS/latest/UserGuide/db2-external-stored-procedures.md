# External stored procedures for

Amazon RDS for Db2

You can create external routines and register them with your Amazon RDS for Db2 databases as
external stored procedures. Currently, RDS for Db2 only supports Java-based routines for
external stored procedures.

## Java-based external stored procedures

Java-based external stored procedures are external Java routines that you register
with your RDS for Db2 database as external stored procedures.

###### Topics

- [Limitations for Java-based external stored procedures](#db2-external-stored-procedures-java-limitations "#db2-external-stored-procedures-java-limitations")
- [Configuring Java-based external stored procedures](#db2-external-stored-procedures-java-configuring "#db2-external-stored-procedures-java-configuring")

### Limitations for Java-based external stored procedures

Before you develop your external routine, consider the following limitations and
restrictions.

To create your external routine, make sure to use the Java Development Kit (JDK) provided by Db2. For more information, see
[Java software support for Db2 database products](https://www.ibm.com/docs/en/db2/11.5?topic=servers-java-software-support-db2-database-products "https://www.ibm.com/docs/en/db2/11.5?topic=servers-java-software-support-db2-database-products").

Your Java program can create files only in the `/tmp` directory,
and Amazon RDS doesn't support enabling executable or Set User ID (SUID) permissions on
these files. Your Java program also can't use socket system calls or the following system
calls:

- \_sysctl
- acct
- afs_syscall
- bpf
- capset
- chown
- chroot
- create_module
- delete_module
- fanotify_init
- fanotify_mark
- finit_module
- fsconfig
- fsopen
- fspick
- get_kernel_syms
- getpmsg
- init_module
- mount
- move_mount
- nfsservctl
- open_by_handle_at
- open_tree
- pivot_root
- putpmsg
- query_module
- quotactl
- reboot
- security
- setdomainname
- setfsuid
- sethostname
- sysfs
- tuxcall
- umount2
- uselib
- ustat
- vhangup
- vserver

For additional restrictions on external routines for Db2, see
[Restrictions on external routines](https://www.ibm.com/docs/en/db2/11.5?topic=routines-restrictions-external "https://www.ibm.com/docs/en/db2/11.5?topic=routines-restrictions-external") in
the IBM Db2 documentation.

### Configuring Java-based external stored procedures

To configure an external stored procedure, create a .jar file with your external routine, install it on your RDS for Db2 database, and then register it as an external stored procedure.

###### Topics

- [Step 1: Enable external stored procedures](#db2-external-stored-procedures-java-enable "#db2-external-stored-procedures-java-enable")
- [Step 2: Install the .jar file with your external routine](#db2-external-stored-procedures-java-install-jar "#db2-external-stored-procedures-java-install-jar")
- [Step 3: Register the external stored procedure](#db2-external-stored-procedures-java-register "#db2-external-stored-procedures-java-register")
- [Step 4: Validate the external stored procedure](#db2-external-stored-procedures-java-validate "#db2-external-stored-procedures-java-validate")

#### Step 1: Enable external stored procedures

To enable external stored procedures, in a custom parameter group associated with your DB instance, set the parameter `db2_alternate_authz_behaviour` to one of the following values:

- `EXTERNAL_ROUTINE_DBADM` – Implicitly grants any user, group, or role with `DBADM` authority the `CREATE_EXTERNAL_ROUTINE` permission.
- `EXTERNAL_ROUTINE_DBAUTH` – Allows a user with `DBADM` authority to grant `CREATE_EXTERNAL_ROUTINE` permission to any user, group, or role.
  In this case, no user, group, or role is implicitly granted this permission, not even a user with `DBADM` authority.

For more information about this setting, see [GRANT (database authorities) statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-grant-database-authorities "https://www.ibm.com/docs/en/db2/11.5?topic=statements-grant-database-authorities") in the IBM Db2
documentation.

You can create and modify a custom parameter group by using the AWS Management Console, the
AWS CLI, or the Amazon RDS API.

###### To configure the db2_alternate_authz_behaviour parameter in a custom parameter group

1. If you want to use a different custom DB parameter group than
   the one your DB instance is using, create a new DB parameter
   group. If you're using the bring your own license (BYOL) model,
   make sure that the new custom parameter group includes the
   IBM IDs. For information about these IDs, see
   [IBM IDs for bring your own
   license (BYOL) for Db2](db2-licensing.md#db2-prereqs-ibm-info "db2-licensing.md#db2-prereqs-ibm-info"). For more information
   about creating a DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
2. Set the value for the
   `db2_alternate_authz_behaviour` parameter in your
   custom parameter group. For more information about modifying a
   parameter group, see [Modifying parameters in a DB parameter group
   in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### To configure the db2_alternate_authz_behaviour parameter in a custom parameter group

1. If you want to use a different custom DB parameter group than
   the one your DB instance is using, create a custom parameter
   group by running the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md")
   command. If you're using the bring your own license (BYOL)
   model, make sure that the new custom parameter group includes
   the IBM IDs. For information about these IDs, see
   [IBM IDs for bring your own
   license (BYOL) for Db2](db2-licensing.md#db2-prereqs-ibm-info "db2-licensing.md#db2-prereqs-ibm-info").

Include the following required options:

    * `--db-parameter-group-name` – A name for
     the parameter group that you are creating.
    * `--db-parameter-group-family` – The Db2
     engine edition and major version. Valid values are
     `db2-se-11.5` and `db2-ae-11.5`.
    * `--description` – A description for this
     parameter group.

For more information about creating a DB parameter group, see
[Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

The following example shows you how to create a custom
parameter group named `MY_EXT_SP_PARAM_GROUP` for the
parameter group family `db2-se-11.5`.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
--region us-east-1 \
--db-parameter-group-name MY_EXT_SP_PARAM_GROUP \
--db-parameter-group-family db2-se-11.5 \
--description "test db2 external routines"
```

For Windows:

```
aws rds create-db-parameter-group ^
--region us-east-1 ^
--db-parameter-group-name MY_EXT_SP_PARAM_GROUP ^
--db-parameter-group-family db2-se-11.5 ^
--description "test db2 external routines"
```

2. Modify the `db2_alternate_authz_behaviour`
   parameter in your custom parameter group by running the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md")
   command.

Include the following required options:

    * `--db-parameter-group-name` – The name
     of the parameter group that you created.
    * `--parameters` – An array of parameter
     names, values, and the application methods for the parameter
     update.

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

The following example shows you how to modify the parameter
group `MY_EXT_SP_PARAM_GROUP` by setting the value of
`db2_alternate_authz_behaviour` to
`EXTERNAL_ROUTINE_DBADM`.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name MY_EXT_SP_PARAM_GROUP \
    --parameters "ParameterName='db2_alternate_authz_behaviour',ParameterValue='EXTERNAL_ROUTINE_DBADM',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name MY_EXT_SP_PARAM_GROUP ^
    --parameters "ParameterName='db2_alternate_authz_behaviour',ParameterValue='EXTERNAL_ROUTINE_DBADM',ApplyMethod=immediate"
```

###### To configure the db2_alternate_authz_behaviour parameter in a custom parameter group

1. If you want to use a different custom DB parameter group than
   the one your DB instance is using, create a new DB parameter
   group by using the Amazon RDS API [CreateDBParameterGroup](../APIReference/API_CreateDBParameterGroup.md "../APIReference/API_CreateDBParameterGroup.md")
   operation. If you're using the bring your own license (BYOL)
   model, make sure that the new custom parameter group includes
   the IBM Db2 IDs. For information about these IDs, see [IBM IDs for bring your own
   license (BYOL) for Db2](db2-licensing.md#db2-prereqs-ibm-info "db2-licensing.md#db2-prereqs-ibm-info").

Include the following required parameters:

    * `DBParameterGroupName`
    * `DBParameterGroupFamily`
    * `Description`

For more information about creating a DB parameter group, see
[Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Modify the `db2_alternate_authz_behaviour`
parameter in your custom parameter group that you created by
using the RDS API [ModifyDBParameterGroup](../APIReference/API_ModifyDBParameterGroup.md "../APIReference/API_ModifyDBParameterGroup.md")
operation.

Include the following required parameters:

    * `DBParameterGroupName`
    * `Parameters`

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

#### Step 2: Install the .jar file with your external routine

After you create your Java routine, create the .jar file and then run `db2 "call sqlj.install_jar('file:`file_path`',`jar_ID`)"` to install it on your RDS for Db2 database.

The following example shows you how to create a Java routine and install it on
an RDS for Db2 database. The example includes sample code for a simple routine that
you can use to test the process. This example makes the following
assumptions:

- The Java code is compiled on a server where Db2 is installed. This is a best practice because not compiling with the IBM-provided JDK can result in unexplained errors.
- The server has the RDS for Db2 database cataloged locally.

If you'd like to try out the process with the following sample code, copy it and then save it to a file named `MYJAVASP.java`.

```
import java.sql.*;
public class MYJAVASP
{
public static void my_JAVASP (String inparam) throws SQLException, Exception
{
try
{
// Obtain the calling context's connection details.
Connection myConn = DriverManager.getConnection("jdbc:default:connection");
String myQuery = "INSERT INTO TEST.TEST_TABLE VALUES (?, CURRENT DATE)";
PreparedStatement myStmt = myConn.prepareStatement(myQuery);
myStmt.setString(1, inparam);
myStmt.executeUpdate();
}
catch (SQLException sql_ex)
{
throw sql_ex;
}
catch (Exception ex)
{
throw ex;
}
}
```

The following command compiles the Java routine.

```
~/sqllib/java/jdk64/bin/javac MYJAVASP.java
```

The following command creates the .jar file.

```
~/sqllib/java/jdk64/bin/jar cvf MYJAVASP.jar MYJAVASP.class
```

The following commands connect to the database named
`MY_DB2_DATABASE` and install the .jar file.

```
db2 "connect to MY_DB2_DATABASE user `master_username` using `master_password`"

db2 "call sqlj.install_jar('file:/tmp/MYJAVASP.jar','MYJAVASP')"
db2 "call sqlj.refresh_classes()"
```

#### Step 3: Register the external stored procedure

After you install the .jar file on your RDS for Db2 database, register it as a
stored procedure by running the `db2 CREATE PROCEDURE` or `db2
 REPLACE PROCEDURE` command.

The following example shows you how to connect to the database and register the Java routine created in the previous step as a stored procedure.

```
db2 "connect to MY_DB2_DATABASE user `master_username` using `master_password`"

create procedure TESTSP.MYJAVASP (in input char(6))
specific myjavasp
dynamic result sets 0
deterministic
language java
parameter style java
no dbinfo
fenced
threadsafe
modifies sql data
program type sub
external name 'MYJAVASP!my_JAVASP';
```

#### Step 4: Validate the external stored procedure

Use the following steps to test the sample external stored procedure
that was registered in the previous step.

###### To validate the external stored procedure

1. Create a table like `TEST.TEST_TABLE` in the following example.

```
db2 "create table TEST.TEST_TABLE(C1 char(6), C2 date)"
```

2. Call the new external stored procedure. The call returns a status of `0`.

```
db2 "call TESTSP.MYJAVASP('test')"
Return Status = 0
```

3. Query the table you created in step 1 to verify the results of the stored procedure call.

```
db2 "SELECT * from TEST.TEST_TABLE"
```

The query produces output similar to the following example:

```
C1     C2
------ ----------
test   02/05/2024
```
