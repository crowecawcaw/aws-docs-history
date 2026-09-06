

# Oracle synonyms
<a name="chap-oracle-aurora-mysql.special.synonyms"></a>

With AWS DMS, you can create database objects called synonyms that act as aliases for other schema objects. A synonym is an alternative name for a table, view, sequence, procedure, function, package, materialized view, Java schema object, or other synonym. Synonyms provide data abstraction by hiding the underlying identity of an object, allowing multiple database objects to be referenced by a single name.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  |  ![One star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-1.png)  |  [Synonyms](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.synonyms)  | Use stored procedures and functions to abstract instance-wide objects. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.synonyms.oracle"></a>

Synonyms are database objects that serve as alternative identifiers for other database objects. The referenced database object is called the 'base object' and may reside in the same database, another database on the same instance, or on a remote server.

Synonyms provide an abstraction layer to isolate client application code from changes to the name or location of the base object.

In Oracle, synonyms are often used to simplify the object’s name to avoid referring to the other schema as well as for security reasons.

For example, table A resides in schema A, and the client application accesses it through a synonym. Table A needs to be moved to another schema. To make the move seamless, only the synonym definition should be updated. Without synonyms, the client application code must be rewritten to access the other schema or to change the connection string. Instead, you can create a synonym called Table A and it will transparently redirect the calling application to the new schema without any code changes.

You can create synonyms for the following objects:
+ Assembly (CLR) stored procedures, table-valued functions, scalar functions, and aggregate functions.
+ Stored procedures and functions.
+ User-defined tables including local and global temporary tables.
+ Views.

### Syntax
<a name="chap-oracle-aurora-mysql.special.synonyms.oracle.syntax"></a>

```
CREATE [OR REPLACE] [EDITIONABLE | NONEDITIONABLE]
[PUBLIC] SYNONYM [schema .] synonym_name
FOR [schema .] object_name [@ dblink];
```

Use the `EDITIONABLE` and `NONEDITIONABLE` options to determine if this object will be private or public. For more information, see [Editioned and Noneditioned Objects](https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/editions.html#GUID-F0D940E0-618D-4656-982E-1C5E49FCCD42) in the *Oracle documentation*.

### Examples
<a name="chap-oracle-aurora-mysql.special.synonyms.oracle.examples"></a>

The following example creates a synonym object `local_emps` that refers to the `usa.emps` table:

```
CREATE SYNONYM local_emps FOR usa.emps;
```

**Note**  
To refer to `local_emps` after you run the preceding command, run your commands or queries against `usa.emps`.

For more information, see [CREATE SYNONYM](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-SYNONYM.html) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.synonyms.mysql"></a>

 Aurora MySQL doesn’t support synonyms and there is no known generic workaround.

A partial workaround is to use encapsulating views as an abstraction layer for accessing tables or views. Similarly, you can also use functions or stored procedures that call other functions or stored procedures.

**Note**  
Synonyms are often used in conjunction with Database Links, which are not supported by Aurora MySQL.

For more information, see [MySQL Fully-Qualified Table Names](chap-oracle-aurora-mysql.special.dblinks.md), [Views](chap-oracle-aurora-mysql.special.views.md), [User-Defined Functions](chap-oracle-aurora-mysql.sql.udfs.md), and [Stored Procedures](chap-oracle-aurora-mysql.sql.stored.md).