# Setting the default edition for a DB instance

You can redefine database objects in a private environment called an edition. You
can use edition-based redefinition to upgrade an application's database objects with
minimal downtime.

You can set the default edition of an Amazon RDS Oracle DB instance using the Amazon RDS
procedure `rdsadmin.rdsadmin_util.alter_default_edition`.

The following example sets the default edition for the Amazon RDS Oracle DB instance to
`RELEASE_V1`.

```
EXEC rdsadmin.rdsadmin_util.alter_default_edition('RELEASE_V1');
```

The following example sets the default edition for the Amazon RDS Oracle DB instance
back to the Oracle default.

```
EXEC rdsadmin.rdsadmin_util.alter_default_edition('ORA$BASE');
```

For more information about Oracle edition-based redefinition, see [About
editions and edition-based redefinition](https://docs.oracle.com/database/121/ADMIN/general.htm#ADMIN13167 "https://docs.oracle.com/database/121/ADMIN/general.htm#ADMIN13167") in the Oracle
documentation.
