

# Object type rules
<a name="sc-default-rules-object-types-sqlserver"></a>

The following table lists how DMS Schema Conversion converts SQL Server object types to PostgreSQL. You can't change these rules, except where a table names a conversion setting.


| Source object type | Converted to | 
| --- | --- | 
| Database | Not created as an object. | 
| Schema, table, view, column, index, constraint, sequence, partition | Same kind of object in PostgreSQL. | 
| Graph table, external table | Not converted — reported as unsupported. | 
| Trigger | PostgreSQL trigger plus a generated trigger function. | 
| Scalar function | Function. | 
| Table-valued function | Function RETURNS TABLE. | 
| Inline table-valued function | Set-returning function RETURNS TABLE. | 
| Aggregate (CLR) function | Not converted. | 
| Procedure | PostgreSQL procedure by default; PostgreSQL function when Convert procedures to functions is enabled. For more information, see [Settings that affect procedure conversion](#sc-default-rules-object-types-sqlserver-procedures). | 
| User-defined type (alias type) | Domain. | 
| User-defined table type | Composite type. | 
| Synonym | Not converted — reported as unsupported. | 
| XML schema collection | Not converted — reported as unsupported. | 
| Partition scheme, partition function | Not created as objects — folded into the partitioned table's definition. | 
| Database trigger, server trigger, linked server, endpoint, assembly, SQL Agent job / alert / operator / schedule | Not converted — reported as unsupported. | 

## Settings that affect procedure conversion
<a name="sc-default-rules-object-types-sqlserver-procedures"></a>

By default, a source procedure is converted to a PostgreSQL `PROCEDURE` that is invoked with `CALL`; its output parameters remain procedure parameters. When the setting *Convert procedures to functions* is enabled, the procedure is converted to a PostgreSQL `FUNCTION` instead: it returns `void` if the procedure has no output parameters, otherwise it returns the `OUT` parameters. If a SQL Server procedure returns a status value, the converted procedure also receives an `INOUT return_code` parameter that carries the return status. This also applies when you convert procedures to functions. For the setting values and defaults, see [SQL Server to PostgreSQL conversion settings](schema-conversion-sql-server-postgresql.md).

## Conversions that create additional target objects
<a name="sc-default-rules-object-types-sqlserver-additional"></a>

Some source constructs have no single PostgreSQL equivalent. To reproduce their behavior, DMS Schema Conversion generates extra objects — such as triggers, trigger functions, sequences, domains, types, views, or constraints — alongside the converted object. This section lists every such case, what is generated, and how the generated objects are named.


| Source construct | What is generated | Generated names | When | 
| --- | --- | --- | --- | 
| TIMESTAMP / ROWVERSION column | Column becomes BIGINT. A trigger function and a BEFORE INSERT OR UPDATE trigger are generated to assign the next value and to reject explicit writes to the column. | fn\_tr\_<table>\_biu, tr\_<table>\_biu; uses the extension pack sequence aws\_sqlserver\_ext\_data.inc\_seq\_rowversion | Always | 
| Computed column whose converted expression is not IMMUTABLE (e.g. uses GETDATE(), SUSER\_SNAME(), a user function) | A plain column is created and a trigger function plus trigger keep it up to date and block direct modification. Computed columns with IMMUTABLE expressions become GENERATED ALWAYS AS (…) STORED and need no extra objects. | fn\_tr\_<table>\_biu, tr\_<table>\_biu (one pair per table, shared with the ROWVERSION case) | When the expression is not immutable | 
| Table with SPARSE columns and a COLUMN\_SET | Two triggers and two trigger functions maintain the XML column set on insert and on update. | tr\_<table>\_bi / fn\_tr\_<table>\_bi and tr\_<table>\_bu / fn\_tr\_<table>\_bu | Always when both features are present | 
| System-versioned temporal table | A history trigger and trigger function write previous row versions to the history table. | tr\_hist\_<table>, fn\_tr\_hist\_<table> | Always | 
| Trigger | Every trigger needs a trigger function in PostgreSQL. A trigger that uses both inserted and deleted where PostgreSQL can't provide both transition tables is split into several triggers, and an empty placeholder function is generated for events with no usable transition table. | fn\_<trigger>; split triggers keep the source name with an event suffix | Always | 
| User-defined table type | A composite type, a domain defined as an array of that type (so table-valued parameters can be passed), and a helper function that populates it. | <type>$aws$t plus its array domain and helper function | Always | 
| User-defined (alias) type | A domain over the base type. No further objects. | <schema>.<type> | Always | 
| String column, when Use CITEXT for all string data types is enabled | Character columns and variables whose collation is not case-sensitive become CITEXT; CREATE EXTENSION IF NOT EXISTS citext is emitted before the schema. Because CITEXT has no length, a CHECK constraint on the character length is added for every column that had one, so the source limit is preserved. With the setting off (the default) no CITEXT is used, whatever the source collation. | extension citext; one check constraint per column | Only when the setting is enabled (off by default) | 
| IDENTITY(seed, increment) column | GENERATED ALWAYS AS IDENTITY (START WITH … INCREMENT BY …). PostgreSQL creates the backing sequence implicitly, so no separate object appears in the converted schema. | — | Always | 
| Built-in function with no native equivalent (for example TODATETIMEOFFSET(), DATETIMEFROMPARTS(), a bit conversion) | The expression is rewritten to call an extension pack function. No object is generated in your schema, but the extension pack must be installed on the target. Functions that the extension pack doesn't emulate are left in place and reported as action items instead. | aws\_sqlserver\_ext.\* | Whenever such a function is referenced | 
| Procedure that returns a status | An extra INOUT return\_code int DEFAULT 0 parameter is appended to carry the SQL Server return status. It keeps this exact name — the par\_ prefix isn't applied to it. The parameter is added in both conversion modes, whether the procedure becomes a PostgreSQL procedure or a function. | parameter return\_code | When the source procedure returns a status value or sets one in a TRY…CATCH block | 
| GEOGRAPHY / GEOMETRY column | Types map to PostGIS GEOGRAPHY / GEOMETRY; the target must have PostGIS installed. | extension postgis (required, not generated) | Always | 