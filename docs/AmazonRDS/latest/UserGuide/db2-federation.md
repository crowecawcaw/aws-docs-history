# Amazon RDS for Db2 federation

You can use your Amazon RDS for Db2 database as a federated database. After setting up
federation for RDS for Db2, you will be able to access and query data across multiple databases
from your RDS for Db2 database. Federation saves you from needing to migrate data to your
RDS for Db2 database or consolidate data into a single database.

By using your RDS for Db2 database as a federated database, you can continue to access to all
RDS for Db2 features and can take advantage of various AWS services, all while keeping your
data in different databases. You can set up both homogeneous federation which connects
different databases of the same type, or heterogeneous federation which connects different
databases of different types.

You first connect your Db2 database in RDS for Db2 to remote databases. Then you can run
queries against all your connected databases. For example, you can run a SQL JOIN statement
that joins tables in your RDS for Db2 database with tables in a remote Db2 on z/OS database.

###### Topics

- [Homogeneous federation](#db2-federation-homogeneous "#db2-federation-homogeneous")
- [Heterogeneous federation](#db2-federation-heterogeneous "#db2-federation-heterogeneous")

## Homogeneous federation

You can set up homogeneous federation between your RDS for Db2 database and the following
Db2 family of products:

- Db2 for Linux, UNIX, Windows (LUW)
- Db2 iSeries
- Db2 for z/OS

RDS for Db2 homogeneous federation doesn't support the following actions:

- Running `CATALOG` commands to set up a node directory and a remote
  database on an RDS for Db2 host database
- Settting up Workload Balancing (WLB) when federating to Db2 on z/OS
- Configuring the IBM data server driver configuration file
  (`db2dsdriver.cfg`)

RDS for Db2 homogeneous federation has the following requirements:

- You must create the DRDA wrapper in `UNFENCED` mode. If you don't,
  then federation won't work in RDS for Db2.
- You must allow incoming and outgoing traffic from your RDS for Db2 host database
  to your remote host databases. For more information, see [Provide access to your DB instance in your VPC by
  creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup "CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup").

###### Topics

- [Step 1: Create a DRDA wrapper
  and a federated server](#db2-federation-homogeneous-create "#db2-federation-homogeneous-create")
- [Step 2: Create a user
  mapping](#db2-federation-homogeneous-map "#db2-federation-homogeneous-map")
- [Step 3: Check the
  connection](#db2-federation-homogeneous-check "#db2-federation-homogeneous-check")

### Step 1: Create a DRDA wrapper

and a federated server

For homogeneous federation, create a DRDA wrapper and a federated server. The
connection to the remote host uses `HOST`, `PORT`, and
`DBNAME`.

Choose one of the following methods based on the type of your remote Db2
database:

- **Db2 for Linux, UNIX, and Windows (LUX)
  database** – Run the following SQL commands. In the
  following example, replace `server_name` with the
  name of the server that you will use for federation. Replace
  `db2_version` with the version of your remote
  Db2 database. Replace `username` and
  `password` with your credentials for the remote
  Db2 database you want to connect to. Replace
  `db_name`, `dns_name`,
  and `port` with the appropriate values for the
  remote Db2 database you want to connect to.

```
create wrapper drda options(DB2_FENCED 'N');
create server `server_name` type DB2/LUW wrapper drda version '`db2_version`' authorization "`master_username`" password "`master_password`" options (add DBNAME '`db_name`',add HOST '`dns_name`',add PORT '`port`');
```

**Example**

```
create wrapper drda options(DB2_FENCED 'N');
create server SERVER1 type DB2/LUW wrapper drda version '11.5' authorization "sysuser" password "******" options (add DBNAME 'TESTDB2',add HOST 'ip-123-45-67-899.us-west-1.compute.internal',add PORT '25010');
```

- **Db2 iSeries** – Run the following
  SQL commands. In the following example, replace
  `wrapper_name` and
  `library_name` with a name for your DRDA
  wrapper and the [wrapper library file](https://www.ibm.com/docs/en/db2/11.5?topic=wrapper-db2-library-files "https://www.ibm.com/docs/en/db2/11.5?topic=wrapper-db2-library-files"). Replace
  `server_name` with the name of the server that
  you will use for federation. Replace `db2_version`
  with the version of your remote Db2 database. Replace
  `username` and
  `password` with your credentials for the remote
  Db2 database you want to connect to. Replace
  `dns_name`, `port`,
  and `db_name` with the appropriate values for the
  remote Db2 database you want to connect to.

```
create wrapper `wrapper_name` library '`library name`' options(DB2_FENCED 'N');
create server `server_name` type db2/mvs version `db2_version` wrapper `wrapper_name` authorization "`sername`" password "`password`" options (HOST '`dns_name`', PORT '`port`', DBNAME '`db_name`');
```

**Example**

```
create wrapper WRAPPER1 library 'libdb2drda.so' options(DB2_FENCED 'N');
create server SERVER1 type db2/mvs version 11 wrapper WRAPPER1 authorization "sysuser" password "******" options (HOST 'test1.123.com', PORT '446', DBNAME 'STLEC1');
```

- **Db2 for z/OS** – Run the following
  SQL commands. In the following example, replace
  `wrapper_name` and
  `library_name` with a name for your DRDA
  wrapper and the [wrapper library file](https://www.ibm.com/docs/en/db2/11.5?topic=wrapper-db2-library-files "https://www.ibm.com/docs/en/db2/11.5?topic=wrapper-db2-library-files"). Replace
  `server_name` with the name of the server that
  you will use for federation. Replace `db2_version`
  with the version of your remote Db2 database. Replace
  `username` and
  `password` with your credentials for the remote
  Db2 database you want to connect to. Replace
  `dns_name`, `port`,
  and `db_name` with the appropriate values for the
  remote Db2 database you want to connect to.

```
create wrapper `wrapper_name` library '`library_name`' options(DB2_FENCED 'N');
create server `server_name` type db2/mvs version `db2_version` wrapper `wrapper_name` authorization "`username`" password "`password`" options (HOST '`dns_name`', PORT '`port`', DBNAME '`db_name`');
```

**Example**

```
create wrapper WRAPPER1 library 'libdb2drda.so' OPTIONS(DB2_FENCED 'N');
create server SERVER1 type db2/mvs version 11 wrapper WRAPPER1 authorization "sysuser" password "******" options (HOST 'test1.123.com', PORT '446', DBNAME 'STLEC1');
```

### Step 2: Create a user

mapping

Create a user mapping to associate your federated server with your data source
server by running the following SQL command. In the following example, replace
`server_name` with the name of the remote server than
you want to perform operations on. This is the server that you created in [step 1](#db2-federation-homogeneous-create "#db2-federation-homogeneous-create"). Replace
`username` and `password` with
your credentials for this remote server.

```
create user mapping for user server `server_name` options (REMOTE_AUTHID '`username`', REMOTE_PASSWORD '`password`');
```

For more information, see [User
mappings](https://www.ibm.com/docs/en/db2/11.5?topic=systems-user-mappings "https://www.ibm.com/docs/en/db2/11.5?topic=systems-user-mappings") in the IBM Db2 documentation.

### Step 3: Check the

connection

Confirm that setting up your federation was successful by checking the connection.
Open a session to send native SQL commands to your remote data source using the SET
PASSTHRU command, and then create a table on the remote data server.

1. Open and close a session to submit SQL to a data source. In the following
   example, replace `server_name` with the name of the
   server that you created for federation in step 1.

```
set passthru `server_name`;
```

2. Create a new table. In the following example, replace
   `column_name`,
   `data_type`, and
   `value` with the appropriate items for your
   table.

```
create table `table_name` ( `column_name` `data_type`(`value`), `column_name` `data_type`(`value`);
```

For more information, see [CREATE TABLE statement](https://www.ibm.com/docs/en/db2-event-store/2.0.0?topic=statements-create-table "https://www.ibm.com/docs/en/db2-event-store/2.0.0?topic=statements-create-table") in the IBM Db2 documentation. 3. Create an index, insert values for rows into the table, and reset the
connection. Resetting the connection drops the connection but retains the
back-end processes. In the following example, replace
`index_name`,
`table_name`,
`column_name`, and
`columnx_value` with your information.

```
create index `index_name` on `table_name`(`column_name`);
insert into `table_name` values(`column1_value`,`column2_value`,`column3_value`);
insert into `table_name` values(`column1_value`,`column2_value`,`column3_value`);
set passthru reset;

connect reset;
```

4. Connect to your remote Db2 database, create a nickname for your remote
   server, and perform operations. When you are done accessing data in the
   remote Db2 database, reset and then terminate the connection. In the
   following example, replace `database_name` with the
   name of your remote Db2 database. Replace
   `nickname` with a name. Replace
   `server_name` and
   `table_name` with the name of the remote server
   and table on that server that you want to perform operations on. Replace
   `username` with the information for your remote
   server. Replace `sql_command` with the operation to
   perform on the remote server.

```
connect to `database_name`;
create nickname `nickname` for `server_name`."`username`"."`table_name`";
select `sql_command` from `nickname`;
connect reset;
terminate;
```

**Example**

The following example creates a pass-through session to allow operations on the
federated server `testdb10`.

Next, it creates the table `t1` with three columns with different data
types.

Then, the example creates the index `i1_t1` on three columns in table
`t1`. Afterwards, it inserts two rows with values for these three
columns, and then disconnects.

Last, the example connects to the remote Db2 database `testdb2` and
creates a nickname for the table `t1` in the federated server
`testdb10`. It creates the nickname with the username
`TESTUSER` for that data source. An SQL command outputs all data from
the table `t1`. The example disconnects and ends the session.

```
set passthru testdbl0;

create table t1 ( c1 decimal(13,0), c2 char(200), c3 int);

create index i1_t1 on t1(c3);
insert into t1 values(1,'Test',1);
insert into t1 values(2,'Test 2',2);
connect reset;

connect to testdb2;
create nickname remote_t1 for testdbl0."TESTUSER"."T1";
select * from remote_t1;
connect reset;
terminate;
```

## Heterogeneous federation

You can set up heterogeneous federation between your RDS for Db2 database and other data
sources such as Oracle and Microsoft SQL Server. For a complete list of data sources
that Db2 LUW supports, see [Data Source Support Matrix of Federation Bundled in Db2 LUW V11.5](https://www.ibm.com/support/pages/data-source-support-matrix-federation-bundled-db2-luw-v115 "https://www.ibm.com/support/pages/data-source-support-matrix-federation-bundled-db2-luw-v115") on the
IBM Support site.

RDS for Db2 heterogeneous federation doesn't support the following items:

- Native wrappers for the other data sources
- JDBC wrappers for the other data sources
- Federation to Sybase, Informix, and Teradata data sources because these data
  sources require client software installation on RDS for Db2

RDS for Db2 heterogeneous federation has the following requirements:

- RDS for Db2 only supports the ODBC wrapper method.
- If you create an explicit definition of a wrapper, then you must set the
  option `DB2_FENCED` to `'N'`. For a list of valid wrapper
  options for ODBC, see [ODBC
  options](https://www.ibm.com/docs/en/db2/11.5?topic=options-odbc "https://www.ibm.com/docs/en/db2/11.5?topic=options-odbc") in the IBM Db2 documentation.
- You must allow incoming and outgoing traffic from your RDS for Db2 host database
  to your remote host database. For more information, see [Provide access to your DB instance in your VPC by
  creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup "CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup").

For information about federation to Oracle, see [How to query Oracle by using
Db2 Federation and the ODBC driver?](https://www.ibm.com/support/pages/node/6431133 "https://www.ibm.com/support/pages/node/6431133") on the IBM Support site.

For more information about data sources that support federation, see [Data Source Support Matrix of
Federation Bundled in Db2 LUW V11.5](https://www.ibm.com/support/pages/node/957245 "https://www.ibm.com/support/pages/node/957245") on the IBM Support site.

###### Topics

- [Step 1: Create an ODBC
  wrapper](#db2-federation-heteogenous-define-wrapper "#db2-federation-heteogenous-define-wrapper")
- [Step 2: Create a federated
  server](#db2-federation-heterogeneous-create "#db2-federation-heterogeneous-create")
- [Step 3: Create a user
  mapping](#db2-federation-heterogeneous-map "#db2-federation-heterogeneous-map")
- [Step 4: Check the
  connection](#db2-federation-heterogeneous-check "#db2-federation-heterogeneous-check")

### Step 1: Create an ODBC

wrapper

Create a wrapper by running the following command:

```
db2 "create wrapper odbc options( module '/home/rdsdb/sqllib/federation/odbc/lib/libodbc.so')"
```

### Step 2: Create a federated

server

Create a federated server by running the following command. In the following
example, replace `server_name` with the name of the server
that you will use for federation. Replace `wrapper_type`
with the appropriate wrapper. Replace `db_version` with the
version of your remote database. Replace `dns_name`,
`port`, and `service_name`
with the appropriate values for the remote database that you want to connect to.

```
db2 "create server `server_name` type `wrapper_type` version `db_version` options (HOST '`dns_name`', PORT '`port`', SERVICE_NAME '`service_name`')“
```

For information about wrapper types, see [Data Source Support Matrix
of Federation Bundled in Db2 LUW V11.5](https://www.ibm.com/support/pages/node/957245 "https://www.ibm.com/support/pages/node/957245") on the IBM Support site.

**Example**

The following example creates a federated server for a remote Oracle
database.

```
db2 "create server server1 type oracle_odbc version 12.1 options (HOST 'test1.amazon.com', PORT '1521', SERVICE_NAME 'pdborcl.amazon.com')“
```

### Step 3: Create a user

mapping

Create a user mapping to associate your federated server with your data source
server by running the following SQL command. In the following example, replace
`server_name` with the name of the remote server than
you want to perform operations on. This is the server that you created in [step 2](#db2-federation-heterogeneous-create "#db2-federation-heterogeneous-create"). Replace
`username` and `password` with
your credentials for this remote server.

```
create user mapping for user server `server_name` options (REMOTE_AUTHID '`username`', REMOTE_PASSWORD '`password`');
```

For more information, see [User
mappings](https://www.ibm.com/docs/en/db2/11.5?topic=systems-user-mappings "https://www.ibm.com/docs/en/db2/11.5?topic=systems-user-mappings") in the IBM Db2 documentation.

### Step 4: Check the

connection

Confirm that setting up your federation was successful by checking the connection.
Open a session to send native SQL commands to your remote data source using the SET
PASSTHRU command, and then create a table on the remote data server.

1. Open and close a session to submit SQL to a data source. In the following
   example, replace `server_name` with the name of the
   server that you created for federation in [step 2](#db2-federation-heterogeneous-create "#db2-federation-heterogeneous-create").

```
set passthru `server_name`;
```

2. Create a new table. In the following example, replace
   `column_name`,
   `data_type`, and
   `value` with the appropriate items for your
   table.

```
create table `table_name` ( `column_name` `data_type`(`value`), `column_name` `data_type`(`value`);
```

For more information, see [CREATE TABLE statement](https://www.ibm.com/docs/en/db2-event-store/2.0.0?topic=statements-create-table "https://www.ibm.com/docs/en/db2-event-store/2.0.0?topic=statements-create-table") in the IBM Db2 documentation. 3. Create an index, insert values for rows into the table, and reset the
connection. Resetting the connection drops the connection but retains the
back-end processes. In the following example, replace
`index_name`,
`table_name`,
`column_name`, and
`columnx_value` with your information.

```
create index `index_name` on `table_name`(`column_name`);
insert into `table_name` values(`column1_value`,`column2_value`,`column3_value`);
insert into `table_name` values(`column1_value`,`column2_value`,`column3_value`);
set passthru reset;

connect reset;
```

4. Connect to your remote Db2 database, create a nickname for your remote
   server, and perform operations. When you are done accessing data in the
   remote Db2 database, reset and then terminate the connection. In the
   following example, replace `database_name` with the
   name of your remote Db2 database. Replace
   `nickname` with a name. Replace
   `server_name` and
   `table_name` with the name of the remote server
   and table on that server that you want to perform operations on. Replace
   `username` with the information for your remote
   server. Replace `sql_command` with the operation to
   perform on the remote server.

```
connect to `database_name`;
create nickname `nickname` for `server_name`."`username`"."`table_name`";
select `sql_command` from `nickname`;
connect reset;
terminate;
```

**Example**

The following example creates a pass-through session to allow operations on the
federated server `testdb10`.

Next, it creates the table `t1` with three columns with different data
types.

Then, the example creates the index `i1_t1` on three columns in table
`t1`. Afterwards, it inserts two rows with values for these three
columns, and then disconnects.

Last, the example connects to the remote Db2 database `testdb2` and
creates a nickname for the table `t1` in the federated server
`testdb10`. It creates the nickname with the username
`TESTUSER` for that data source. An SQL command outputs all data from
the table `t1`. The example disconnects and ends the session.

```
set passthru testdbl0;

create table t1 ( c1 decimal(13,0), c2 char(200), c3 int);

create index i1_t1 on t1(c3);
insert into t1 values(1,'Test',1);
insert into t1 values(2,'Test 2',2);
connect reset;

connect to testdb2;
create nickname remote_t1 for testdbl0."TESTUSER"."T1";
select * from remote_t1;
connect reset;
terminate;
```
