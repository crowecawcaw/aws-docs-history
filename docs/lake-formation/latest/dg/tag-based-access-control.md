# Lake Formation tag-based access control

Lake Formation tag-based access control (LF-TBAC) is an authorization strategy that defines
permissions based on attributes. In Lake Formation, these attributes are called _LF-Tags_. You can attach LF-Tags to Data Catalog resources, and grant
permissions to Lake Formation principals on those resources using these LF-Tags. Lake Formation allows
operations on those resources when the principal has granted access to a tag value that matches
the resource tag value.

LF-TBAC is helpful in environments that are growing rapidly and helps with situations where
policy management becomes cumbersome.

LF-TBAC is the recommended method to use to grant Lake Formation permissions
when there is a large number of Data Catalog objects including federated catalogs, databases, tables, and views.
Lake Formation supports tag-based access control for federated catalogs of Amazon S3 tables, Amazon Redshift data warehouses, and federated data sources such as Amazon DynamoDB, SQL Server, and Snowflake.

###### Note

IAM tags are not the same as LF-Tags. These tags are not interchangeable. LF-Tags
are used to grant Lake Formation permissions and IAM tags are used to define IAM policies.

## How Lake Formation tag-based access control works

Each LF-Tag is a key-value pair, such as `department=sales` or
`classification=restricted`. A key can have multiple defined values, such as
`department=sales,marketing,engineering,finance`.

To use the LF-TBAC method, data lake administrators and data engineers perform the
following tasks.

| Task                                                                                                                                                                                             | Task details                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| 1. Define the properties and relationships of LF-Tags.                                                                                                                                           | -                                                                                                                             |
| 2. Create the LF-Tag creators in Lake Formation.                                                                                                                                                 | [Adding LF-Tag creators](TBAC-adding-tag-creator.md "TBAC-adding-tag-creator.md")                                             |
| 3. Create the LF-Tag in Lake Formation.                                                                                                                                                          | [Creating LF-Tags](TBAC-creating-tags.md "TBAC-creating-tags.md")                                                             |
| 4. Assign LF-Tags to Data Catalog resources.                                                                                                                                                     | [Assigning LF-Tags to Data Catalog resources](TBAC-assigning-tags.md "TBAC-assigning-tags.md")                                |
| 5. Grant permissions to other principals to assign LF-Tags to resources,<br>optionally with the grant option.                                                                                    | [Managing LF-Tag value<br>permissions](TBAC-granting-tags.md "TBAC-granting-tags.md")                                         |
| 6. Grant LF-Tag expressions to principals, optionally with the grant<br>option.                                                                                                                  | [Granting data lake permissions using the<br>LF-TBAC method](granting-catalog-perms-TBAC.md "granting-catalog-perms-TBAC.md") |
| 7. (Recommended) After verifying that principals have access to the correct<br>resources through the LF-TBAC method, revoke permissions that were granted by using<br>the named resource method. | -                                                                                                                             |

Consider the case where you must grant permissions to three principals on three databases
and seven tables.

![Three figures of users are at the left, arranged vertically. At the right are three databases labeled A, B, and C, arranged vertically. Database A has two tables labeled A.1 and A.2, database B has tables labels B.1 and B.2, and Database C has three tables labeled C.1, C.2, and C.3. Seventeen arrows connect the users to the databases and tables, indicating grants on the databases and tables to the users.](images/TBAC_example_discreet.png)

To achieve the permissions indicated in the preceding diagram by using the named resource
method, you would have to make 17 grants, as follows (in pseudo-code).

```
GRANT CREATE_TABLE ON Database A TO PRINCIPAL 1
GRANT SELECT, INSERT ON Table A.1 TO PRINCIPAL 1
GRANT SELECT, INSERT ON Table A.2 TO PRINCIPAL 1
GRANT SELECT, INSERT ON Table B.2 TO PRINCIPAL 1
...
GRANT SELECT, INSERT ON Table A.2 TO PRINCIPAL 2
GRANT CREATE_TABLE ON Database B TO PRINCIPAL 2
...
GRANT SELECT, INSERT ON Table C.3 TO PRINCIPAL 3
```

Now consider how you would grant permissions by using LF-TBAC. The following diagram
indicates that you've assigned LF-Tags to databases and tables, and has granted permissions
on LF-Tags to principals.

In this example, the LF-Tags represent areas of the data lake that contain
analytics for different modules of an enterprise resource planning (ERP) application suite.
You can use them to control access to the analytics data for the various modules. All
LF-Tags have the key `module` and possible values `Sales`,
`Orders`, and `Customers`. An example LF-Tag looks like
this:

```
module=Sales
```

The diagram shows only the LF-Tag values.

![Like the previous diagram, three figures of users are at the left, arranged vertically, and at the right are three databases labeled A, B, and C, arranged vertically. Database A has two tables labeled A.1 and A.2, database B has tables labels B.1 and B.2, and Database C has three tables labeled C.1, C.2, and C.3. There are no arrows between the users and the databases and tables. Instead, labeled "flags" next to the users indicate that user1 has been granted the LF-Tags Sales and Customers, user 2 has been granted the LF-Tag Orders, and user 3 has been granted the LF-Tag Customers. Flags next to the databases and tables indicate the following assignments ofLF-Tags to databases and tables: Database A: Sales. Table A1: A dimmed flag indicates that Sales was inherited from Database A. Table A2: Orders, but a dimmed flag indicates that Sales was inherited from Database A. Database B: Orders. Table B.1 and B.2 inherit Orders, and Table B.2 has Customers. Database C has Customers, and Tables C.1, C.2, and C.3 inherit Customers. The C tables don't have any other assignments.](images/TBAC_example_tags.png)

###### Tag assignments to Data Catalog resources and inheritance

Tables inherit LF-Tags from databases and columns inherit LF-Tags from tables.
Inherited values can be overridden. In the preceding diagram, dimmed LF-Tags are
inherited.

Because of inheritance, the data lake administrator needs to make only the five following
LF-Tag assignments to resources (in pseudo-code).

```
ASSIGN TAGS module=Sales TO database A
ASSIGN TAGS module=Orders TO table A.2
ASSIGN TAGS module=Orders TO database B
ASSIGN TAGS module=Customers TO table B.2
ASSIGN TAGS module=Customers TO database C
```

###### Tag grants to principals

After assigning LF-Tags to the databases and tables, the data lake administrator must
make only four grants of LF-Tags to principals, as follows (in pseudo-code).

```
GRANT TAGS module=Sales TO Principal 1
GRANT TAGS module=Customers TO Principal 1
GRANT TAGS module=Orders TO Principal 2
GRANT TAGS module=Customers TO Principal 3
```

Now, a principal with the `module=Sales`LF-Tag can access Data Catalog resources
with the `module=Sales` LF-Tag (for example, database A), a principal with the
`module=Customers` LF-Tag can access resources with the
`module=Customers` LF-Tag, and so on.

The preceding grant commands are incomplete. This is because although they indicate
through LF-Tags the Data Catalog resources that the principals have permissions on, they don't
indicate exactly which Lake Formation permissions (such as `SELECT`, `ALTER`) the
principals have on those resources. Therefore, the following pseudo-code commands are a more
accurate representation of how Lake Formation permissions are granted on Data Catalog resources through
LF-Tags.

```
GRANT (CREATE_TABLE ON DATABASES) ON TAGS module=Sales TO Principal 1
GRANT (SELECT, INSERT ON TABLES)  ON TAGS module=Sales TO Principal 1
GRANT (CREATE_TABLE ON DATABASES) ON TAGS module=Customers TO Principal 1
GRANT (SELECT, INSERT ON TABLES)  ON TAGS module=Customers TO Principal 1
GRANT (CREATE_TABLE ON DATABASES) ON TAGS module=Orders TO Principal 2
GRANT (SELECT, INSERT ON TABLES)  ON TAGS module=Orders TO Principal 2
GRANT (CREATE_TABLE ON DATABASES) ON TAGS module=Customers TO Principal 3
GRANT (SELECT, INSERT ON TABLES)  ON TAGS module=Customers TO Principal 3
```

###### Putting it together - Resulting permissions on resources

Given the LF-Tags assigned to the databases and tables in the preceding diagram, and
the LF-Tags granted to the principals in the diagram, the following table lists the Lake Formation
permissions that the principals have on the databases and tables.

| Principal   | Permissions Granted Through LF-Tags                                                                                                                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Principal 1 | • `CREATE_TABLE` on database A<br>• `SELECT`, `INSERT` on table A.1<br>• `SELECT`, `INSERT` on table B.2<br>• `CREATE_TABLE` on database C<br>• `SELECT`, `INSERT` on table C.1<br>• `SELECT`, `INSERT` on table C.2<br>• `SELECT`, `INSERT` on table C.3 |
| Principal 2 | • `SELECT`, `INSERT` on table A.2<br>• `CREATE_TABLE` on database B<br>• `SELECT`, `INSERT` on table B.1                                                                                                                                                  |
| Principal 3 | • `SELECT`, `INSERT` on table B.2<br>• `CREATE_TABLE` on database C<br>• `SELECT`, `INSERT` on table C.1<br>• `SELECT`, `INSERT` on table C.2<br>• `SELECT`, `INSERT` on table C.3                                                                        |

###### Bottom line

In this simple example, using five assignment operations and eight grant operations, the
data lake administrator was able to specify 17 permissions. When there are tens of databases
and hundreds of tables, the advantage of the LF-TBAC method over the named resource method
becomes clear. In the hypothetical case of the need to grant every principal access to every
resource, and where `n(P)` is the number of principals and `n(R)` is
the number of resources:

- With the named resource method, the number of grants required is `n(P)` ✕
  `n(R)`.
- With the LF-TBAC method, using a single LF-Tag, the total of the number of grants to
  principals and assignments to resources is `n(P)` + `n(R)`.

###### See also

- [Managing LF-Tags for metadata access control](managing-tags.md "managing-tags.md")
- [Granting data lake permissions using the
  LF-TBAC method](granting-catalog-perms-TBAC.md "granting-catalog-perms-TBAC.md")

###### Topics

- [Managing LF-Tags for metadata access control](managing-tags.md "managing-tags.md")
- [Managing LF-Tag expressions for metadata access
  control](managing-tag-expressions.md "managing-tag-expressions.md")
- [Managing LF-Tag value
  permissions](TBAC-granting-tags.md "TBAC-granting-tags.md")
