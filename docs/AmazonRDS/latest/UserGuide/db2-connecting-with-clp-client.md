# Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 CLP

You can use a command line utility such as IBM Db2 CLP to connect to Amazon RDS for Db2 DB
instances. This utility is part of IBM Data Server Runtime Client. To
download the clientfrom IBM Fix Central,
see [IBM Data
Server Client Packages Version 11.5 Mod 8 Fix Pack 0](https://www.ibm.com/support/pages/node/6830885 "https://www.ibm.com/support/pages/node/6830885") in IBM
Support.

###### Topics

- [Terminology](#db2-connecting-ibm-clp-terms "#db2-connecting-ibm-clp-terms")
- [Installing the client](#db2-connecting-ibm-clp-install-client "#db2-connecting-ibm-clp-install-client")
- [Connecting to a DB instance](#db2-connecting-ibm-clp-connect-db-instance "#db2-connecting-ibm-clp-connect-db-instance")
- [Troubleshooting connections to your RDS for Db2 DB instance](#db2-troubleshooting-connections-clp "#db2-troubleshooting-connections-clp")

## Terminology

The following terms help explain commands used when [connecting to your RDS for Db2 DB
instance](#db2-connecting-ibm-clp-connect-db-instance "#db2-connecting-ibm-clp-connect-db-instance").

**catalog tcpip node**

This command registers a remote database node with a local Db2 client,
which makes the node accessible to the client application. To catalog a
node, you provide information such as the server's host name, port number,
and communication protocol. The cataloged node then represents a target
server where one or more remote databases reside. For more information, see
[CATALOG TCPIP/TCPIP4/TCPIP6 NODE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-tcpip-node "https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-tcpip-node") in
the IBM Db2 documentation.

**catalog database**

This command registers a remote database with a local Db2 client, which
makes the database accessible to the client application. To catalog a
database, you provide information such as the database's alias, the node on
which it resides, and the authentication type needed to connect to the
database. For more information, see [CATALOG DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-database") in the
IBM Db2 documentation.

## Installing the client

After [downloading the package for Linux](#db2-downloading-package "#db2-downloading-package"),
install the client using root or administrator privileges.

###### Note

To install the client on AIX or Windows, follow the
same procedure but modify the commands for your operating system.

###### To install the client on Linux

1. Run **`./db2_install -f sysreq`** and
   choose **`yes`** to accept the
   license.
2. Choose the location to install the client.
3. Run **`clientInstallDir/instance/db2icrt -s
 client`
   `instance_name`**. Replace
   `instance_name` with a valid operating system user
   on Linux.
   In
   Linux,
   the Db2 DB instance name is tied to the operating system username.

This command creates a **`sqllib`**
directory in the home directory of the designated user on
Linux.

## Connecting to a DB instance

To connect to your RDS for Db2 DB instance, you need its DNS name and port number. For
information about finding them, see [Finding the endpoint](db2-finding-instance-endpoint.md "db2-finding-instance-endpoint.md"). You also need to know the
database name, master username, and master password that you defined when you created
your RDS for Db2 DB instance. For more information about finding them, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").

###### To connect to an RDS for Db2 DB instance with IBM Db2 CLP

1. Sign in with the username that you specified during the IBM Db2 CLP client
   installation.
2. Catalog your RDS for Db2 DB instance. In the following example, replace
   `node_name`, `dns_name`,
   and `port` with a name for the node in the local
   catalog, the DNS name for your DB instance, and the port number.

```
db2 catalog TCPIP node `node_name` remote `dns_name` server `port`
```

**Example**

```
db2 catalog TCPIP node remnode remote database-1.123456789012.us-east-1.amazonaws.com server 50000
```

3. Catalog the `rdsadmin` database and your database. This will allow
   you to connect to the `rdsadmin` database to perform some
   administrative tasks using Amazon RDS stored procedures. For more information, see
   [Administering your RDS for Db2 DB instance](db2-administering-db-instance.md "db2-administering-db-instance.md").

In the following example, replace `database_alias`,
`node_name`, and
`database_name` with aliases for this database, the
name of the node defined in the previous step, and the name of your database.
`server_encrypt` encrypts your username and password over the
network.

```
db2 catalog database rdsadmin [ as `database_alias` ] at node `node_name` authentication server_encrypt

db2 catalog database `database_name` [ as `database_alias` ] at node `node_name` authentication server_encrypt
```

**Example**

```
db2 catalog database rdsadmin at node remnode authentication server_encrypt

db2 catalog database testdb as rdsdb2 at node remnode authentication server_encrypt
```

4. Connect to your RDS for Db2 database. In the following example, replace
   `rds_database_alias`,
   `master_username`, and
   `master_password` with the name of your database,
   the master username, and master password of your RDS for Db2 DB instance.

```
db2 connect to `rds_database_alias` user `master_username` using `master_password`
```

This command produces output similar to the following example:

```
Database Connection Information

    Database server        = DB2/LINUXX8664 11.5.9.0
    SQL authorization ID   = ADMIN
    Local database alias   = TESTDB
```

5. Run queries and view results. The following example shows a SQL statement that
   selects the database you created.

```
db2 "select current server from sysibm.dual"
```

This command produces output similar to the following example:

```
1
    ------------------
    TESTDB

    1 record(s) selected.
```

## Troubleshooting connections to your RDS for Db2 DB instance

If you receive the following `NULLID` error, it usually indicates that your
client and RDS for Db2 server versions don't match. For supported Db2 client versions, see
[Supported combinations of clients, drivers and server levels](https://www.ibm.com/docs/en/db2/11.5?topic=communications-supported-combinations-clients-drivers-server-levels "https://www.ibm.com/docs/en/db2/11.5?topic=communications-supported-combinations-clients-drivers-server-levels") in the
IBM Db2 documentation.

```
db2 "select * from syscat.tables"
SQL0805N Package "NULLID.SQLC2O29 0X4141414141454A69" was not found.
SQLSTATE=51002
```

After you receive this error, you must bind packages from your older Db2 client to a
Db2 server version supported by RDS for Db2.

###### To bind packages from an older Db2 client to a newer Db2 server

1. Locate the bind files on the client machine. Typically, these files are
   located in the **bnd** directory of the Db2
   client's installation path and have the extension **.bnd**.
2. Connect to the Db2 server. In the following example, replace
   `database_name` with the name of your Db2 server.
   Replace `master_username` and
   `master_password` with your information. This user
   has `DBADM` authority.

```
db2 connect to `database_name` user `master_username` using `master_password`
```

3.  Run the `bind` command to bind the packages.
    1. Navigate to the directory where the bind files exist on the client
       machine.
    2. Run the `bind` command for each file.

    The following options are required:

        * `blocking all` – Binds all packages in the
         bind file in a single database request.
        * `grant public` – Grants permission to
         `public` to execute the
         package.
        * `sqlerror continue` – Specifies that the
         `bind` process continues even if errors
         occur.

    For more information about the `bind` command see [BIND command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-bind "https://www.ibm.com/docs/en/db2/11.5?topic=commands-bind") in the
    IBM Db2 documentation.

4.  Verify that the bind was successful by either querying the
    `syscat.package` catalog view or checking the message returned
    after the `bind` command.

For more information, see [DB2 v11.5 Bind File and Package Name List](https://www.ibm.com/support/pages/node/6190455 "https://www.ibm.com/support/pages/node/6190455") in IBM
Support.
