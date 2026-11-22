

# Custom transformation plan

Before conversion begins, AWS Transform presents a transformation plan that you review and customize. The plan defines which job phases run, how AWS Transform converts your schema (type mappings, schema name mappings, and other rules), and where the converted schema is deployed. Changes you make here drive the entire conversion workflow. To proceed with the defaults, approve the plan; to change it, edit the plan and resubmit, or describe the changes you want in the chat.

## Job plan
<a name="custom-plan-job-plan"></a>

The job plan defines the sequence of phases for your conversion job. Each phase builds on the previous one. To turn off an optional phase, clear its check box in the plan form, or set **Run?** to **No** in the plan file. If you turn off a phase, AWS Transform also turns off every phase that depends on it. Required phases cannot be turned off.


| Phase | Depends on | Default behavior | 
| --- | --- | --- | 
| Schema conversion | — | Converts SQL Server objects to PostgreSQL DDL | 
| Target provisioning | Schema conversion | Creates a new Aurora PostgreSQL cluster | 
| Schema deployment | Target provisioning | Deploys the converted schema to the target cluster | 
| Synthetic test data | Schema deployment | Generates test data and loads it into the target | 
| Application code transformation | Schema deployment | Transforms the .NET source code database access layer | 

## Conversion and custom rules
<a name="custom-plan-conversion-rules"></a>

When AWS Transform converts SQL Server to PostgreSQL, it uses default rules for data types and schema names. They fit most jobs. To change them, edit the rules text under **Schema transformation customization** in the plan form or the plan file, or describe the changes in the chat. The rules are free text, so you can edit the listed rules or write new ones as sentences. Leave the text unchanged to keep the default rules. Any rule you do not change keeps its default.

For example, the following rules text changes one type mapping, one schema mapping, and one identifier abbreviation.

```
- Type mappings: MONEY → DECIMAL(19,4)
- Schema mappings: SalesDB.dbo → sales_dbo
Abbreviate reconciliation to recon.
```

You can change the following kinds of rules:
+ **Type mappings** – how a SQL Server data type converts, for example `MONEY` to `DECIMAL(19,4)`.
+ **Schema mappings** – the PostgreSQL schema name for each source schema, for example `dbo` to `public`.
+ **Strip schema prefixes** – prefixes to remove from schema names, for example `gold_`.
+ **Function mappings** – how a SQL Server function converts, for example `GETDATE` to `CURRENT_TIMESTAMP`.
+ **Native function mappings** – a native PostgreSQL function for a SQL Server function, for example `fn_Split` to `STRING_TO_TABLE`.
+ **Identifier conventions** – prefixes for parameters, variables, and temporary tables, for example `in_` instead of `p_` for parameters.
+ **Object handling** – identity column generation, and whether procedures return a cursor or become functions, for example `GENERATED ALWAYS` for identity columns.
+ **Identifier abbreviations** – short forms for identifiers longer than 63 characters, for example `reconciliation` to `recon`.
+ **Multi-database schema suffix** – the last word of the generated `dbo` schema name, for example `public`.

For details about the multi-database schema suffix, see [Multi-database schema suffix](#custom-plan-multi-db-schema-suffix).

**Note**  
Function mappings and native function mappings apply only when stored procedure analysis is available for your job. Otherwise, AWS Transform does not apply them and tells you which ones it skipped.

### Type mappings
<a name="custom-plan-type-mappings"></a>

Override any SQL Server to PostgreSQL type mapping. For example, map `BIT` to `INT` instead of the default `NUMERIC(1,0)`, or map `MONEY` to `DECIMAL(19,4)`. Name the SQL Server type and the PostgreSQL type that it becomes.

**Important**  
**Chain-replacement warning:** AWS Transform applies type mappings in sequence, so a type can change more than once. By default, `NVARCHAR(n)` maps to `VARCHAR(n)`, and `VARCHAR` maps to `CITEXT`, so `NVARCHAR(n)` ends as `CITEXT`. `NCHAR(n)` ends as `CITEXT` the same way, through `CHAR`. If you map `NVARCHAR` to `VARCHAR` but keep the default `VARCHAR` to `CITEXT` mapping, `NVARCHAR` columns still become `CITEXT`. To get `VARCHAR` output, also map `VARCHAR` to `VARCHAR`. The same applies to `NCHAR` and `CHAR`.

The following table lists the default type mappings and the PostgreSQL type that each source type ends as. Because the `citext` extension is always active, `VARCHAR`, `NVARCHAR`, `CHAR`, and `NCHAR` become `CITEXT` (case-insensitive text). `TEXT` and `NTEXT` stay `TEXT`.


| Source (SQL Server) | Target (PostgreSQL) | 
| --- | --- | 
| INT | INTEGER | 
| BIGINT | BIGINT | 
| SMALLINT | SMALLINT | 
| TINYINT | SMALLINT | 
| UTINYINT | SMALLINT | 
| BIT | NUMERIC(1,0) | 
| MONEY | NUMERIC(19,4) | 
| SMALLMONEY | NUMERIC(10,4) | 
| FLOAT | DOUBLE PRECISION | 
| REAL | REAL | 
| DATETIME | TIMESTAMP(3) | 
| SMALLDATETIME | TIMESTAMP(0) | 
| DATE | DATE | 
| TIME | TIME | 
| VARCHAR | CITEXT | 
| NVARCHAR | CITEXT | 
| CHAR | CITEXT | 
| NCHAR | CITEXT | 
| NTEXT | TEXT | 
| TEXT | TEXT | 
| SYSNAME | VARCHAR(128) | 
| IMAGE | BYTEA | 
| UNIQUEIDENTIFIER | UUID | 
| XML | XML | 
| SQL\_VARIANT | JSONB | 
| HIERARCHYID | TEXT | 

`VARCHAR(MAX)` and `NVARCHAR(MAX)` become `TEXT`.

### Schema name mappings
<a name="custom-plan-schema-mappings"></a>

Set the PostgreSQL schema name for each SQL Server schema. By default, the `dbo` schema becomes `<db_name>_dbo` and every other schema follows `<db_name>_<schema>`, so that more than one database can load into one target database without a naming conflict.
+ The new schema name must end with the name of the source schema. You can add any prefix in front of it. AWS Transform identifies each source schema after conversion by removing the prefix, so a name that does not end with the source schema name is rejected (for example, `archive` to `archive_history` or `archive` to `legacy_data`).
+ Two placeholders are filled in at conversion time: `<db_name>` becomes the database name, and `<schema>` becomes the source schema name.
+ A schema mapping names one source schema. Prefix it with a database name to scope the mapping to one database, in the form `Database.Schema` (a colon, `Database:Schema`, also works). Use `*` in place of a schema name to match all schemas of a database.
+ A mapping for a named schema takes priority over a `*` mapping, and a mapping with a database name takes priority over one without. If no mapping applies to a schema, it keeps its original name.
+ The `dbo` schema is the one schema whose name you can replace completely, because validation treats `dbo` and `public` as the same default schema. For a single-database migration, mapping `dbo` to `public` is the common choice.

**Important**  
Do not send more than one database to a single shared schema such as `public`. If two source databases contain a table with the same name, a conflict occurs and the later table fails to create. Keep the default namespacing unless you have a plan for this.

#### Multi-database schema suffix
<a name="custom-plan-multi-db-schema-suffix"></a>

This rule sets the last word of the generated `dbo` schema name, which is `<db_name>_dbo` by default. The value can be `dbo` (the default) or `public`. For example, with `public`, the `dbo` schema of a database named {{mydb}} becomes `{{mydb}}_public`. A schema mapping that names `dbo`, or a `*` mapping, takes priority (see [Schema name mappings](#custom-plan-schema-mappings)), and this rule then changes nothing. To rename `dbo` completely, map `dbo` to `public` instead.

### Other conversion rules
<a name="custom-plan-other-rules"></a>

Strip schema prefixes  
Schema-name prefixes to remove during conversion (for example, `gold_`). Empty by default.

Function mappings  
Override how SQL Server functions map to PostgreSQL, for example `GETDATE` to `CURRENT_TIMESTAMP`. A target can be an expression, and AWS Transform keeps it as written. Built-in defaults apply otherwise (for example, `NEWID` to `uuid_generate_v4`).

Identifier conventions  
Prefixes for generated routine identifiers: parameters (default `p_`), variables (default `v_`), and temporary tables (default `temp_`).

Object handling  
**Identity strategy:** `GENERATED BY DEFAULT` (default, migration-friendly) or `GENERATED ALWAYS`. **Procedure result strategy:** `refcursor` (default; the caller fetches a cursor) or `function` (the procedure becomes a function the caller selects, which is an application-code change).

Native function mappings  
Map a SQL Server function or user-defined function (UDF) to a native PostgreSQL equivalent (for example, `fn_Split` to `STRING_TO_TABLE`) instead of carrying a stub.

Identifier abbreviations  
Readable abbreviations used when an identifier exceeds the PostgreSQL 63-character limit, for example `reconciliation` to `recon`.

The following conversion settings always use their defaults and cannot be overridden: the `citext`, `uuid-ossp`, `pgcrypto`, and `postgis` extensions; lowercase identifier casing; and built-in T-SQL pattern conversions (for example, `TRY/CATCH` to `EXCEPTION` and `OUTPUT` to `RETURNING`).

## Target provisioning
<a name="custom-plan-target-provisioning"></a>

The converted PostgreSQL schema is deployed to an Aurora PostgreSQL cluster. By default, AWS Transform provisions a new cluster (`db.r6g.2xlarge`, private, with auto-generated credentials). To deploy to an existing cluster instead, provide a cluster identifier and a credentials secret.


| Setting | Notes | 
| --- | --- | 
| Cluster identifier | Leave empty to create a new cluster. Provide an identifier to use an existing cluster. | 
| Instance class | Compute instance size (default db.r6g.2xlarge). | 
| Publicly accessible | Whether the cluster allows public internet access (default No). | 
| Secret name | Optional for a new cluster (credentials are auto-generated); required for an existing cluster. | 
| Target database | Database name on the target cluster (default postgres). | 
| Subnet IDs | Optional VPC subnet placement. | 
| Security group IDs | Optional network access rules. | 
| Target Region | Optional. Leave empty to use the job Region. | 

### Requirements for an existing cluster
<a name="custom-plan-existing-cluster-requirements"></a>

If you provide a cluster identifier, the cluster and its credentials secret must meet all of the following requirements. AWS Transform validates them together and reports anything missing in a single message.

**Target cluster**
+ The engine must be Aurora PostgreSQL.
+ The cluster must be in the same AWS account and Region as the job.
+ The cluster must be tagged `Project=atx-db-modernization` and `Owner=database-connector`. The IAM role is scoped to these tags, so an untagged cluster cannot be used.
+ The cluster must be in `available` status when AWS Transform validates it — not stopped, and not mid-modification.

**Credentials secret (AWS Secrets Manager)**
+ A secret is required for an existing cluster. AWS Transform never creates credentials for a cluster it did not provision, and never modifies your secret.
+ The secret must be tagged `Project=atx-db-modernization` and `Owner=database-connector`.
+ The secret must contain JSON with `username` and `password` fields, for example `{"username": "dbuser", "password": "..."}`.
+ The secret must be in the same Region as the cluster. Cross-Region secret access is not supported.