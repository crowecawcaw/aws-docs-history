

# Object type rules
<a name="sc-default-rules-object-types-oracle"></a>

The following table lists how DMS Schema Conversion converts Oracle object types to PostgreSQL. You can't change these rules, except where a table names a conversion setting.


| Source object type | Converted to | 
| --- | --- | 
| Schema, table, view, trigger, column, index, constraint, sequence, partition, subpartition | Same kind of object in PostgreSQL. | 
| External table | Not converted — reported as unsupported. | 
| Global temporary table | View, plus a set-returning function, a trigger function, and an INSTEAD OF trigger that together emulate session-private temporary data. For more information, see [Conversions that create additional target objects](#sc-default-rules-object-types-oracle-additional). | 
| View constraint | Not converted — reported as unsupported. | 
| Procedure | PostgreSQL procedure by default; PostgreSQL function when Convert procedures to functions is enabled. For more information, see [Settings that affect procedure conversion](#sc-default-rules-object-types-oracle-procedures). | 
| Function | Function. | 
| Package | Not created as an object — its members are flattened into the schema. For more information, see [Oracle packages — naming of every package member](sc-default-rules-naming-oracle.md#sc-default-rules-naming-oracle-packages). | 
| Materialized view | Table by default (setting Materialized view conversion as = TABLE); a PostgreSQL materialized view when the setting is MATERIALIZED\_VIEW. For more information, see [Oracle to PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md). | 
| Materialized view log | Not converted — reported as unsupported. | 
| Object type | Composite type. | 
| Collection type (VARRAY, nested table) | A domain over an array of the element type. DMS Schema Conversion can also create a composite type <type>$c with one column, column\_value, so that TABLE(collection) queries return COLUMN\_VALUE. It does this, for example, for every collection whose element is a built-in type. The VARRAY size limit and the NOT NULL element constraint aren't converted. For more information, see [Conversions that create additional target objects](#sc-default-rules-object-types-oracle-additional). | 
| Synonym | No target object. References to a private synonym are rewritten to the underlying object. For a public synonym the engine can generate a wrapper view or routine in the public schema. | 
| Database link | Foreign server that uses the postgres\_fdw wrapper, plus a user mapping. References to remote objects become foreign tables when the link is associated with a remote server. For more information, see [Conversions that create additional target objects](#sc-default-rules-object-types-oracle-additional). | 
| Cluster (index or hash) | Not converted. Each table stored in the cluster is converted as an ordinary table without the CLUSTER clause. Both the cluster and each of its tables are reported as action items. | 
| DBMS\_JOB job | Not converted — reported as unsupported. | 
| Scheduler job, program, schedule | Not converted — reported as unsupported. | 
| Advanced Queuing queue, subscriber | Not converted — reported as unsupported. | 

## Settings that affect procedure conversion
<a name="sc-default-rules-object-types-oracle-procedures"></a>

By default, a source procedure is converted to a PostgreSQL `PROCEDURE` that is invoked with `CALL`; its output parameters remain procedure parameters. When the setting *Convert procedures to functions* is enabled, the procedure is converted to a PostgreSQL `FUNCTION` instead: it returns `void` if the procedure has no output parameters, otherwise it returns the `OUT` parameters. Overloaded procedures in a package receive the `$p` suffix, which becomes `$f` when they are converted to functions. For the setting values and defaults, see [Oracle to PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md).

## Conversions that create additional target objects
<a name="sc-default-rules-object-types-oracle-additional"></a>

Some source constructs have no single PostgreSQL equivalent. To reproduce their behavior, DMS Schema Conversion generates extra objects — such as triggers, trigger functions, sequences, domains, types, views, or constraints — alongside the converted object. This section lists every such case, what is generated, and how the generated objects are named.


| Source construct | What is generated | Generated names | When | 
| --- | --- | --- | --- | 
| Identity column with DEFAULT ON NULL | PostgreSQL identity columns can't accept an explicit NULL, so a sequence, a trigger function, and a trigger emulate the Oracle behavior. | seq\_<table>$def\_on\_null, <table>$tr\_fn\_ind\_on\_null, <table>$tr\_ind\_on\_null | When DEFAULT ON NULL is used | 
| Non-identity column with DEFAULT ON NULL | A trigger and trigger function replace an inserted NULL with the default expression. | trigger\_don$<table>, f\_trigger\_don$<table> | When DEFAULT ON NULL is used | 
| Virtual column whose converted expression is not IMMUTABLE | A plain column plus a trigger and trigger function that recompute it. Immutable expressions become GENERATED ALWAYS AS (…) STORED with no extra objects. | trigger\_vc$<table>, f\_trigger\_vc$<table> | When the expression is not immutable | 
| Global temporary table | A view named after the source table, a set-returning function that creates a session-local temporary table on first use and returns its rows, a trigger function that applies inserts, updates, and deletes to that table, and an INSTEAD OF trigger on the view. The source ON COMMIT setting is carried to the temporary table. | view <table>, function <table>(), trigger function <table>\_iud(), trigger <table>\_iud, session table <table>$tmp | Always | 
| Table, when Generate row ID is set to generate an identity column | A rowid column defined as BIGINT GENERATED ALWAYS AS IDENTITY, so code that relies on ROWID keeps working. PostgreSQL creates the backing sequence implicitly, and no constraint is added. | Additional column rowid only; no separate objects are generated. | Only when the setting is enabled (off by default) | 
| Table, when Generate row ID is set to generate a character domain column | A rowid column of the extension pack type aws\_oracle\_data.rowid that defaults to NEXTVAL('<table>\_rowid\_seq'), the sequence that feeds it, and a constraint on the column: PRIMARY KEY when the table has no primary key, or UNIQUE when it already has one. For a temporary table the sequence is created as a temporary sequence. DMS Schema Conversion raises AI 5597 if the table exceeds the supported column count after the column is added. | column rowid, sequence <table>\_rowid\_seq, constraint pk\_<table>\_rowid (no primary key) or <table>\_rowid\_key (primary key exists) | Only when the setting is enabled (off by default) | 
| Trigger | Every trigger needs a trigger function. | <trigger>$<table> (falls back to the trigger name if too long) | Always | 
| Package | Flattened into the schema: one routine per member, an initialization procedure, and for each package cursor an open stub and a fetch routine. Package variables live in the extension pack state store rather than as objects. | <package>$<member>, <package>$init, …$o (and …$FETCH where needed) | Always | 
| Cursor declared in a package or routine and used across routines | A function that opens and returns the cursor. | <package>$<cursor> | When the cursor is shared | 
| Record type | A composite type; where a record variable has field defaults, a constructor function is generated to initialize it. | <type>$r plus constructor function | Always / when defaults exist | 
| Collection type (VARRAY, nested table) | A domain over an array of the element type, and in some cases a composite type with one column, column\_value. The VARRAY size limit and NOT NULL element constraint aren't converted. | <type>, <type>$c | Always. <type>$c for every built-in element type and some others. | 
| Collection type declared in a package or routine | A domain over an array of the element type, with a CHECK constraint for the VARRAY size limit and one for NOT NULL elements. | Domain <owner>$<type>, where <owner> is the standalone routine or package that declares the type. A hash suffix $<hash> is added when several routines in one package declare types with the same name. Constraints: <domain>\_lim (VARRAY size) and <domain>\_nn (NOT NULL elements). | Always. Each constraint only when the source declares the size limit or NOT NULL. | 
| Associative array (INDEX BY), declared in a package or routine | No domain. Each variable holds the array name, and the extension pack functions aws\_oracle\_ext.array$\* store the elements at run time. For an associative array of a built-in type or of another collection, DMS Schema Conversion also creates a composite type with one column, column\_value. | Composite type <owner>$<type>$c. Variable: VARCHAR(100) with the same name as the Oracle variable. | Always. The composite type only when the element is a built-in type or another collection. | 
| Package exception | A function that returns the exception's error code: the code from PRAGMA EXCEPTION\_INIT, or 1 if there is none. | <package>$<exception>() | Always | 
| Exception declared in a procedure, function, or block | A local variable of type aws\_oracle\_ext.ora\_exception that holds the exception name. If the exception has PRAGMA EXCEPTION\_INIT, DMS Schema Conversion also declares a SMALLINT variable that holds the code. | <exception>, <exception>$code | Always | 
| Public synonym | The engine can generate a wrapper in the target public schema: a view (SELECT \* FROM <object>) for a table or view, a wrapper procedure or function for a routine. Private synonyms produce no object. | public.<synonym> | For supported target objects; a synonym to a package produces nothing | 
| Built-in function or package with no native equivalent (DBMS\_OUTPUT, UTL\_\*, SYSDATE semantics, …) | Rewritten to call an extension pack function. No object is generated in your schema, but the extension pack must be installed. | aws\_oracle\_ext.\* | Whenever such a function is referenced | 
| Database link | A foreign server that uses the postgres\_fdw wrapper, plus a user mapping. The mapping is created FOR the user in the link's CONNECT TO clause for a private link, or FOR current\_user for a public link. Its password option is the placeholder user\_password, so replace it with real credentials. For a public link, grant USAGE on the foreign server to the role that connects to your target. | server <link>, user mapping FOR <connect-to user> or FOR current\_user | Always | 
| Reference to a remote table, view, materialized view, or synonym over a database link | A foreign table in the schema that contains the referencing object, named for the entire remote reference. DMS Schema Conversion reads the remote structure through the link, rewrites every reference to use the foreign table, and creates each foreign table once however many objects reference it. | <local schema>."<remote schema>.<remote object>@<link>", with SERVER "<link>" and OPTIONS (schema\_name …, table\_name …) | When the link is associated with a remote server. Otherwise the reference can't be resolved and AI 5668 is raised | 