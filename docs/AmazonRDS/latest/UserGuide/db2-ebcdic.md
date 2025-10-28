# EBCDIC collation for Db2 databases on Amazon RDS

Amazon RDS for Db2 supports EBCDIC collation for Db2 databases. You can only specify an EBCDIC
collation sequence for a database when you create the database by using the Amazon RDS [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database") stored procedure.

When you create an RDS for Db2 DB instance by using the AWS Management Console, AWS CLI, or RDS API, you
can specify a database name. If you specify a database name, Amazon RDS creates a database with
the default collation of `SYSTEM`. If you need to create a database with EBCDIC
collation, don't specify a database name when you create a DB instance.

The collation for a database in RDS for Db2 is set at the time of creation and is
immutable.

###### To create a Db2 database with EBCDIC collation

1. If you don't have an RDS for Db2 DB instance, create a DB instance but don't specify
   a database name You can create a DB instance by using the AWS Management Console, AWS CLI, or RDS
   API. For more information, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").
2. Create a Db2 database and set the collation option to an EBCDIC value by calling
   the `rdsadmin.create_database` stored procedure. For more information,
   see [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database").

###### Important

After you create a database using the stored procedure, you can't change the collation
sequence. If you want a database to use a different collation sequence, drop the
database by calling the [rdsadmin.drop_database](db2-sp-managing-databases.md#db2-sp-drop-database "db2-sp-managing-databases.md#db2-sp-drop-database") stored procedure.
Then, create a database with the required collation sequence.
