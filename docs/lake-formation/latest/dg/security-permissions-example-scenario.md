# Permissions example scenario

The following scenario helps demonstrate how you can set up permissions to secure access to data in AWS Lake Formation.

Shirley is a data administrator. She wants to set up a data lake for her company,
AnyCompany. Currently, all data is stored in Amazon S3. John is a marketing manager and needs write
access to customer purchasing information (contained in
`s3://customerPurchases`). A marketing analyst, Diego, joins John this
summer. John needs the ability to grant Diego access to perform queries on the data without
involving Shirley.

Mateo, from finance, needs access to query accounting data (for example, `s3://transactions`).
He wants to query the transactions data in tables in a database (`Finance_DB`) that the finance team uses.
His manager, Arnav, can give him access to the `Finance_DB`.
Although he shouldn’t be able to modify accounting data, he needs the ability to convert data into a format (schema) suitable for forecasting.
This data will be stored in a separate bucket (`s3://financeForecasts`) that he can modify.

To summarize:

- Shirley is the data lake administrator.
- John requires `CREATE_DATABASE` and `CREATE_TABLE` permission to
  create new databases and tables in the Data Catalog.
- John also requires `SELECT`, `INSERT`, and `DELETE`
  permissions on tables he creates.
- Diego requires `SELECT` permission on the table to run queries.
  The employees of AnyCompany perform the following actions to set up permissions. The API
  operations shown in this scenario show a simplified syntax for clarity.

1. Shirley registers the Amazon S3 path containing customer purchasing information with
   Lake Formation.

```
RegisterResource(ResourcePath("s3://customerPurchases"), false, Role_ARN )
```

2. Shirley grants John access to the Amazon S3 path containing customer purchasing
   information.

```
GrantPermissions(John, S3Location("s3://customerPurchases"), [DATA_LOCATION_ACCESS]) )
```

3. Shirley grants John permission to create databases.

```
GrantPermissions(John, catalog, [CREATE_DATABASE])
```

4. John creates the database `John_DB`. John automatically has
   `CREATE_TABLE` permission on that database because he created it.

```
CreateDatabase(John_DB)
```

5. John creates the table `John_Table` pointing to
   `s3://customerPurchases`. Because he created the table, he has all
   permissions on it, and can grant permissions on it.

```
CreateTable(John_DB, John_Table)
```

6. John allows his analyst, Diego, access to the table `John_Table`.

```
 GrantPermissions(Diego, John_Table, [SELECT])
```

7. John allows his analyst, Diego, access to the `s3://customerPurchases/London/`.
   Because Shirley already registered `s3://customerPurchases`, its subfolders are registered with Lake Formation.

```
 GrantDataLakePrivileges( 123456789012/datalake, Diego, [DATA_LOCATION_ACCESS], [], S3Location("s3://customerPurchases/London/") )
```

8. John allows his analyst, Diego, to create tables in database `John_DB`.

```
 GrantDataLakePrivileges( 123456789012/datalake, Diego, John_DB, [CREATE_TABLE], [] )
```

9. Diego creates a table in `John_DB` at `s3://customerPurchases/London/` and automatically gets `ALTER`, `DROP`, `SELECT`, `INSERT`, and `DELETE` permissions.

```
 CreateTable( 123456789012/datalake, John_DB, Diego_Table )
```
