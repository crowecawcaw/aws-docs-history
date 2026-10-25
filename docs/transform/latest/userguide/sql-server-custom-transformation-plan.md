

# Custom transformation plan
<a name="sql-server-custom-transformation-plan"></a>

Before conversion begins, AWS Transform presents a transformation plan that you review and customize. The plan defines which job phases run, how AWS Transform converts your schema (type mappings, schema name mappings, and other rules), and where the converted schema is deployed. Changes you make here drive the entire conversion workflow. To proceed with the defaults, approve the plan; to change it, edit the plan and resubmit, or describe the changes you want in the chat.

## Job plan
<a name="custom-plan-job-plan"></a>

The job plan defines the sequence of phases for your conversion job. Each phase builds on the previous one. You can turn off any optional phase by setting **Run?** to **No**. If you skip a phase, any phase that depends on it is skipped automatically. Required phases cannot be turned off.


| Phase | Depends on | Default behavior | 
| --- | --- | --- | 
| Schema conversion | — | Converts SQL Server objects to PostgreSQL DDL | 
| Target provisioning | Schema conversion | Creates a new Aurora PostgreSQL cluster | 
| Schema deployment | Target provisioning | Deploys the converted schema to the target cluster | 
| Synthetic test data | Schema deployment | Generates test data and loads it into the target | 
| Application code transformation | Schema deployment | Transforms the .NET source code database access layer | 

## Conversion and custom rules
<a name="custom-plan-conversion-rules"></a>

When AWS Transform converts SQL Server to PostgreSQL, data types and schema names are mapped using built-in defaults that handle common cases. You can override these rules to control how specific types are converted and where objects land in PostgreSQL. Every field is optional — change only what you need, and everything else uses the default. You can edit the rule values directly, or describe the changes you want in plain language and AWS Transform applies the matching rules.

### Type mappings
<a name="custom-plan-type-mappings"></a>

Override any SQL Server to PostgreSQL type mapping. For example, map `BIT` to `INT` instead of the default `NUMERIC(1,0)`, or map `MONEY` to `DECIMAL(19,4)`. Each rule needs a unique rule ID, a source type (SQL Server), and a target type (PostgreSQL).

**Important**  
**Chain-replacement warning:** AWS Transform applies type mappings in sequence. If you override `NVARCHAR` to `VARCHAR` but leave the default `VARCHAR` to `CITEXT` mapping active, `NVARCHAR` columns still become `CITEXT`. To get `VARCHAR` output, also override the `VARCHAR` rule (`VARCHAR` to `VARCHAR`) to break the chain. The same applies to any character type that the `citext` extension maps to `CITEXT`.

The following table lists the default type mappings. The `citext` extension is always active and maps all character types to `CITEXT` (case-insensitive text).


| Source (SQL Server) | Target (PostgreSQL) | 
| --- | --- | 
| INT | INTEGER | 
| BIGINT | BIGINT | 
| SMALLINT | SMALLINT | 
| TINYINT | SMALLINT | 
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
| NTEXT | CITEXT | 
| TEXT | CITEXT | 
| SYSNAME | VARCHAR(128) | 
| IMAGE | BYTEA | 
| UNIQUEIDENTIFIER | UUID | 
| XML | XML | 
| SQL\_VARIANT | JSONB | 
| HIERARCHYID | TEXT | 

### Schema name mappings
<a name="custom-plan-schema-mappings"></a>

Set the PostgreSQL schema name for each SQL Server schema. By default, the `dbo` schema becomes `<db_name>_dbo` and every other schema follows `<db_name>_<schema>`, so that more than one database can load into one target database without a naming conflict.
+ The new schema name must end with the name of the source schema. You can add any prefix in front of it. AWS Transform identifies each source schema after conversion by removing the prefix, so a name that does not end with the source schema name is rejected (for example, `archive` to `archive_history` or `archive` to `legacy_data`).
+ Two placeholders are filled in at conversion time: `<db_name>` becomes the database name, and `<schema>` becomes the source schema name.
+ A key is the name of one source schema. Prefix it with a database name to scope the rule to one database, in the form `Database.Schema` (a colon, `Database:Schema`, also works). Use `*` in place of a schema name to match all schemas of a database.
+ A rule for a named schema takes priority over a `*` rule, and a key with a database name takes priority over one without. If no rule applies to a schema, it keeps its original name.
+ The `dbo` schema is the one schema whose name you can replace completely, because validation treats `dbo` and `public` as the same default schema. For a single-database migration, `"dbo": "public"` is the common choice.

**Important**  
Do not send more than one database to a single shared schema such as `public`. If two source databases contain a table with the same name, a conflict occurs and the later table fails to create. Keep the default namespacing unless you have a plan for this.

### Other conversion rules
<a name="custom-plan-other-rules"></a>

Strip schema prefixes  
Schema-name prefixes to remove during conversion (for example, `gold_`). Empty by default.

Function mappings  
Override how SQL Server functions map to PostgreSQL. Each rule needs a source (for example, `GETDATE`) and a target (for example, `CURRENT_TIMESTAMP`). Expression targets are kept verbatim. Built-in defaults apply otherwise (for example, `NEWID` to `uuid_generate_v4`).

Identifier conventions  
Prefixes for generated routine identifiers: parameters (default `p_`), variables (default `v_`), and temporary tables (default `temp_`).

Object handling  
**Identity strategy:** `GENERATED BY DEFAULT` (default, migration-friendly) or `GENERATED ALWAYS`. **Procedure result strategy:** `refcursor` (default; the caller fetches a cursor) or `function` (the procedure becomes a function the caller selects, which is an application-code change).

Native function mappings  
Map a SQL Server function or UDF to a native PostgreSQL equivalent (for example, `fn_Split` to `STRING_TO_TABLE`) instead of carrying a stub. Each rule needs a source function and a target expression.

Identifier abbreviations  
Readable abbreviations used when an identifier exceeds the PostgreSQL 63-character limit. Each rule needs a term (for example, `reconciliation`) and an abbreviation (for example, `recon`).

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