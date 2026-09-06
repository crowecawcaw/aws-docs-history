

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# PG\_DEFAULT\_ACL
<a name="r_PG_DEFAULT_ACL"></a>

Stores information about default access privileges. For more information on default access privileges, see [ALTER DEFAULT PRIVILEGES](r_ALTER_DEFAULT_PRIVILEGES.md).

PG\_DEFAULT\_ACL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_PG_DEFAULT_ACL-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| defacluser | integer | ID of the user to which the listed privileges are applied. | 
| defaclnamespace | oid  | The object ID of the schema where default privileges are applied. The default value is 0 if no schema is specified. | 
| defaclobjtype | character | The type of object to which default privileges are applied. Valid values are as follows: + r – relation (table or view) <br />+ f – function <br />+ p – stored procedure  | 
| defaclacl |  aclitem[] | A string that defines the default privileges for the specified user or user group and object type. <br />If the privileges are granted to a user, the string is in the following form: <br />*`{ username=privilegestring/grantor } `*<br />*username* <br />The name of the user to which privileges are granted. If *username* is omitted, the privileges are granted to PUBLIC. <br />If the privileges are granted to a user group, the string is in the following form:<br />*`{ "group groupname=privilegestring/grantor" } `*<br />*privilegestring* <br />A string that specifies which privileges are granted. <br />Valid values are: + `a` – INSERT (append) <br />+ `r` – SELECT (read) <br />+ `w` – UPDATE (write) <br />+ `d` – DELETE <br />+ `R` – RULE <br />+ `x` – Grants the privilege to create a foreign key constraint ( REFERENCES).<br />+ `t` – TRIGGER <br />+ `X` – EXECUTE <br />+ `U` – USAGE <br />+ `C` – CREATE <br />+ `T` – CREATE TEMP <br />+ `D` – DROP <br />+ `P` – TRUNCATE <br />+ `A` – ALTER <br />+ `*` – Indicates that the user receiving the preceding privilege can in turn grant the same privilege to others (WITH GRANT OPTION).<br />A string holding all privilege code chars, in order by bitmask position, looks like "arwdRxtXUCTDPA".<br />*grantor* <br />The name of the user that granted the privileges. <br />The following example indicates that the user `admin` granted all privileges, including WITH GRANT OPTION, to the user `dbuser`. <pre>dbuser=r*a*w*d*x*X*/admin</pre> | 

## Example
<a name="r_PG_DEFAULT_ACL-example"></a>

The following query returns all default privileges defined for the database. 

```
select pg_get_userbyid(d.defacluser) as user, 
n.nspname as schema, 
case d.defaclobjtype when 'r' then 'tables' when 'f' then 'functions' end 
as object_type, 
array_to_string(d.defaclacl, ' + ')  as default_privileges 
from pg_catalog.pg_default_acl d 
left join pg_catalog.pg_namespace n on n.oid = d.defaclnamespace;

 user  | schema | object_type |              default_privileges
-------+--------+-------------+-------------------------------------------------------
 admin | tickit | tables      | user1=r/admin + "group group1=a/admin" + user2=w/admin
```

The result in the preceding example shows that for all new tables created by user `admin` in the `tickit` schema, `admin` grants SELECT privileges to `user1`, INSERT privileges to `group1`, and UPDATE privileges to `user2`.