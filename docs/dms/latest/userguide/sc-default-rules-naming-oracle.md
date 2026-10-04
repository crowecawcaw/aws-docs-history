

# Naming rules
<a name="sc-default-rules-naming-oracle"></a>

The following naming rules apply when your source database is Oracle. DMS Schema Conversion applies your transformation rules first, and then applies the default rules for case, prefixes, uniqueness, and length to the result.

## Naming by object type
<a name="sc-default-rules-naming-oracle-objecttypes"></a>

The following table lists the rule that DMS Schema Conversion applies to each kind of database object. Where DMS Schema Conversion generates a name rather than deriving it from the source, the table shows the pattern.


| Object type | Naming rule | Example | 
| --- | --- | --- | 
| Schema | Mapped directly; Oracle has no database level above the schema. Case is reversed. | HR → hr | 
| Table, view | Schema-qualified, case reversed. | HR.EMPLOYEES → hr.employees | 
| Materialized view | Same name; becomes an ordinary table by default (Materialized view conversion as). | MV\_ACCOUNT → TABLE hr.mv\_account | 
| Global temporary table | The view keeps the source table name; the set-returning function takes the same name, the trigger function and INSTEAD OF trigger add the \_iud suffix, and the session-local table adds the $tmp suffix. | GTT\_ORDERS → view gtt\_orders, function gtt\_orders(), trigger function gtt\_orders\_iud(), trigger gtt\_orders\_iud, session table gtt\_orders$tmp | 
| Column | Case reversed if a plain identifier. | EMPLOYEE\_ID → employee\_id | 
| Index | Keeps its name, case reversed. Not renamed for uniqueness, because Oracle index names are already unique within a schema. | ADDRESS\_CUSTOMER\_IX → address\_customer\_ix | 
| Constraint | A user-named constraint keeps its name (case reversed). A system-generated name (SYS\_C…) is dropped by default and PostgreSQL assigns its own (<table>\_pkey, <table>\_<column>\_key, …); enable Convert system constraint names using original to keep the SYS\_C… name. | PK\_EMP → pk\_emp; SYS\_C00173685 on EMPLOYEES → unnamed, becomes employees\_pkey | 
| Trigger | Keeps its name, case reversed. The generated trigger function is named <trigger>$<table>. | TIB\_OFFICE on ACCOUNT → trigger tib\_office, function tib\_office$account | 
| Sequence | Schema-qualified. | HR.EMP\_SEQ → hr.emp\_seq | 
| Sequence generated for an identity column with DEFAULT ON NULL | Derived from the table with a fixed prefix and suffix. | identity column on EMPLOYEES → seq\_employees$def\_on\_null | 
| Synonym | No target object; references are rewritten to the name of the object the synonym points at. A synonym to a package produces no target name. | EMP (synonym for HR.EMPLOYEES) → hr.employees | 
| Partition | Table name and partition name joined with an underscore. | partition P1 of EMPLOYEES → employees\_p1 | 
| Subpartition | Table name and subpartition name joined with an underscore. | subpartition SP1 of EMPLOYEES → employees\_sp1 | 
| Procedure, function | Schema-qualified. Members of a package are flattened — see Package and its members and the package section that follows. | HR.CALC\_PAY → hr.calc\_pay | 
| Package and its members | Flattened into the schema — see the package section that follows. | HR.MY\_PKG.DO\_WORK → hr.my\_pkg$do\_work | 
| Parameter | Mapped name; no prefix is added, unlike SQL Server. | P\_EMPNO → p\_empno | 
| Variable | Mapped name. Inside a trigger, the correlation names become new and old. | V\_TOTAL → v\_total; :NEW.SALARY → new.salary | 
| Cursor (package level) | Flattened like other package members, plus an open stub with the $o suffix. | GLOBAL\_CURSORS.CURSOR\_OUT\_PARAM → global\_cursors$cursor\_out\_param, …$o | 
| Package exception | Function named <package>$<exception>, returning the exception's error code. | E\_INVALID\_STATE in MY\_PKG → hr.my\_pkg$e\_invalid\_state() | 
| Object type | Composite type, same name; attributes become the fields. | ADDRESS\_T → hr.address\_t (street, city, state, …) | 
| Record type | Composite type with a record suffix. | HR.EMP\_REC → hr.emp\_rec$r | 
| Nested table / VARRAY type | Domain over an array of the element type, same name. | ADDRESS\_TAB (TABLE OF ADDRESS\_T) → DOMAIN hr.address\_tab AS hr.address\_t[] | 
| Collection type over a built-in type | Type with a collection suffix. | HR.ID\_LIST (TABLE OF NUMBER) → hr.id\_list$c | 
| Database link | Foreign server named after the link, case reversed. The user mapping is named for the link's CONNECT TO user for a private link, or current\_user for a public link. | EC2ORA12EE\_PRIVATE connecting as MIN\_PRIVS → server ec2ora12ee\_private, mapping FOR MIN\_PRIVS | 
| Database link reference | When the link is associated with a remote server, the reference becomes a foreign table in the local schema whose name is the whole remote reference, quoted. | test\_ora\_remote.tbl\_dblink\_simple@test\_ora\_remote\_dblink → test\_ora\_pg."test\_ora\_remote.tbl\_dblink\_simple@test\_ora\_remote\_dblink" | 
| Cluster, DBMS\_JOB, scheduler job / program / schedule, AQ queue / subscriber, materialized view log | Not converted — no target name. | — | 
| Attribute, constant, LOB, argument, view constraint | Not standalone objects; named as fields, parameters, or columns of their parent object. | — | 

## Settings that affect naming
<a name="sc-default-rules-naming-oracle-settings"></a>

Several conversion settings change how DMS Schema Conversion generates names: *Convert procedures to functions*, *Materialized view conversion as*, *Convert system constraint names using original*, *Generate row ID*, *Create stubs in separate schema*, and *Convert unsupported built-ins to stubs*. For their values and defaults, see [Oracle to PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md). The following naming rules assume the default values.

## Transformation rules that affect naming
<a name="sc-default-rules-naming-oracle-transformation"></a>

Transformation rules let you override the name of selected objects. You can rename them; add, remove, or replace a prefix or suffix; or force lowercase. DMS Schema Conversion applies transformation rules before the default naming rules, so casing, uniqueness, and truncation still run afterward on the name that you specify. For the rule syntax, actions, and object locators, see [Transformation rules in DMS Schema Conversion](sc-transformation-rules.md). The following naming rules assume that no transformation rules are defined.

## Case sensitivity
<a name="sc-default-rules-naming-oracle-case"></a>

The following describes how DMS Schema Conversion handles the case of source object names. PostgreSQL folds unquoted identifiers to lowercase, so the case that a name arrives in determines whether you can use it unquoted in the target.

**Note**  
**Plain identifiers.** Most naming rules apply only to a *plain identifier* — a name matching `^[A-Za-z_][0-9A-Za-z$_]*$` that isn't a target reserved word. Any name containing spaces, dots, quotes, or non-ASCII characters is left exactly as it is, and is quoted in the target instead. This is the single most useful rule to remember: **if a name isn't a plain identifier, its case is never changed.**

**Warning**  
**Oracle case handling is a reversal, not a lowercase.** Because Oracle stores unquoted identifiers in uppercase, an all-uppercase name becomes lowercase in PostgreSQL (`ACCOUNT` → `account`). An all-lowercase source name, which is possible only if it was quoted in Oracle, becomes *uppercase* in PostgreSQL (`tbl_quoted_lowercase` → `"TBL_QUOTED_LOWERCASE"`). A mixed-case name keeps its spelling in PostgreSQL, quoted to preserve the case (`CaseSensitive` → `"CaseSensitive"`). Any name that isn't all-uppercase in Oracle therefore comes out double-quoted in PostgreSQL and must be quoted wherever it's referenced. Reserved words and names that aren't plain identifiers are exceptions: even when they're all-uppercase, they keep their source spelling and are quoted (`SELECT` → `"SELECT"`). To get uniformly lowercase, unquoted target names, add a `convert-lowercase` transformation rule.

### Examples
<a name="sc-default-rules-naming-oracle-case-examples"></a>


| Source name | Converted name | Why | 
| --- | --- | --- | 
| ACCOUNT | account | All uppercase in Oracle, so the target name is lowercase and needs no quoting | 
| tbl\_quoted\_lowercase | "TBL\_QUOTED\_LOWERCASE" | Lowercase in Oracle, which is only possible when quoted, so the target name reverses to upper and keeps quotes | 
| CaseSensitive | "CaseSensitive" | Mixed case, so the target name keeps the source spelling and is quoted to keep it | 
| allowed$\_chars | "ALLOWED$\_CHARS" | $ and \_ are valid in a plain identifier, so the target name is uppercase and is quoted to keep it | 
| S P A C E S | "S P A C E S" | Not a plain identifier, so the target name keeps the source spelling; the spaces require quoting | 
| contains.dot | "contains.dot" | Not a plain identifier, so the target name keeps the source spelling; the dot requires quoting | 
| ЯК\_Є | "ЯК\_Є" | Not a plain identifier, so the target name keeps the source spelling; the non-ASCII characters require quoting | 
| NOT | "NOT" | A reserved word, so the target name keeps the source spelling and is quoted | 

## Oracle packages — naming of every package member
<a name="sc-default-rules-naming-oracle-packages"></a>

PostgreSQL has no package concept. DMS Schema Conversion therefore *flattens* each package: it doesn't create the package itself as an object, and it creates every member directly in the package's schema with the package name carried as a prefix. A `$` separates the parts, because it's legal in a PostgreSQL identifier but can't appear in an unquoted Oracle name — so a generated name can never collide with a real source name.


| Package member | Becomes | Name pattern | Example | 
| --- | --- | --- | --- | 
| Package itself | Nothing — the package isn't created as an object. Its name survives only as a prefix on its members. | — | HR.MY\_PKG → no object; my\_pkg$ prefixes every member | 
| Procedure | Function or procedure in the package's schema | schema.package$procedure | MY\_PKG.DO\_WORK → hr.my\_pkg$do\_work | 
| Function | Function in the package's schema | schema.package$function | MY\_PKG.GET\_NAME → hr.my\_pkg$get\_name | 
| Overloaded procedure | Function, with a kind suffix to keep overloads distinct | schema.package$procedure$p | MY\_PKG.DO\_WORK (two overloads) → hr.my\_pkg$do\_work$p | 
| Overloaded function | Function, with a kind suffix to keep overloads distinct | schema.package$function$f | MY\_PKG.GET\_NAME (two overloads) → hr.my\_pkg$get\_name$f | 
| Nested subprogram (a routine declared inside another routine) | Standalone routine, since PostgreSQL can't nest routines. The enclosing routine's name is not part of the target name — a hash disambiguates instead. | schema.package$nested$hash | INNER declared inside MY\_PKG.OUTER → hr.my\_pkg$inner$3f2a1b | 
| Cursor | Routine that opens the cursor, plus a fetch routine | schema.package$cursor, open stub …$o, fetch …$FETCH | MY\_PKG.EMP\_CUR → hr.my\_pkg$emp\_cur, hr.my\_pkg$emp\_cur$o, hr.my\_pkg$emp\_cur$FETCH | 
| Record type | Composite type | schema.package$type$r | MY\_PKG.EMP\_REC → hr.my\_pkg$emp\_rec$r | 
| Record type declared inside a packaged routine | Composite type. Treated as an auto-generated object, so the enclosing routine's name is replaced by a hash. | schema.package$type$hash$r | EMP\_REC declared inside MY\_PKG.DO\_WORK → hr.my\_pkg$emp\_rec$3f2a1b$r | 
| Collection type over a built-in type | Type or domain, with a collection suffix | schema.package$type$c | MY\_PKG.ID\_LIST (TABLE OF NUMBER) → hr.my\_pkg$id\_list$c | 
| Non-record type declared inside a packaged routine | Type. Also auto-generated, so a hash replaces the enclosing routine's name. | schema.package$type$hash | MY\_TYPE declared inside MY\_PKG.DO\_WORK → hr.my\_pkg$my\_type$3f2a1b | 
| Type owned by a package member that isn't a routine | Type | schema.package$owner$type | MY\_TYPE owned by cursor MY\_PKG.EMP\_CUR → hr.my\_pkg$emp\_cur$my\_type | 
| Package-level variable | Not a named object. Package state is held in an extension pack key/value store, keyed by schema, package, and variable name, so it keeps Oracle's session-scoped behavior. | accessed via aws\_oracle\_ext.getglobalvariable(…) / setglobalvariable(…) | G\_COUNT NUMBER := 1 in MY\_PKG → perform aws\_oracle\_ext.setglobalvariable(proutinename => 'hr.my\_pkg', pvariable => 'g\_count', pval => 1) | 
| Package-level constant | Same store. A constant is registered once, in the package's initialization routine, with the option {"constant": true}. | setglobalvariable(…, poptions => '{"constant": true}') | C\_MAX CONSTANT NUMBER := 100 in MY\_PKG → aws\_oracle\_ext.getglobalvariable(proutinename => 'hr.my\_pkg', pvariable => 'c\_max') | 
| Package initialization block | Procedure that runs the package body's initialization section | schema.package$init | BEGIN … END block of MY\_PKG body → hr.my\_pkg$init | 
| Initialization companion for a packaged routine | Routine generated alongside a converted routine that needs initialization | schema.package$routine$init | MY\_PKG.DO\_WORK → hr.my\_pkg$do\_work$init | 

**Warning**  
**Package variables and constants aren't converted into named objects.** An Oracle package variable keeps its value for the life of a session, which no PostgreSQL schema object reproduces. DMS Schema Conversion instead stores package state in an extension pack key/value store keyed by schema, package, and variable name, and rewrites every read and write into a getter or setter call. This preserves the session-scoped semantics, but it means that you won't find a column, variable, or sequence in the target that corresponds to a package variable.

### Suffixes used in generated names
<a name="sc-default-rules-naming-oracle-packages-suffixes"></a>

The following suffixes apply to the PostgreSQL targets that are documented here. Other target engines use different package-flattening conventions.


| Suffix | Meaning | 
| --- | --- | 
| $ | Separator between every flattened name part — package, owner routine, member name. | 
| $p | Marks an overloaded procedure, so overloads don't collide. | 
| $f | Marks an overloaded function, so overloads don't collide. | 
| $r | Marks a record type converted to a composite type. | 
| $c | Marks a collection type built over a built-in or system type. | 
| $o | Marks the open stub routine generated for a package cursor. | 
| $FETCH | Marks the fetch routine generated for a package cursor, where one is needed. | 
| $<hash> | Disambiguates auto-generated objects — anything declared inside a routine, such as a nested subprogram or a locally declared type — and is also appended when a name has to be truncated. | 

**Note**  
**Length budget.** Because these suffixes are added after the name is built, the truncation limit is reduced to leave room for them — by two characters for cursors and types (`$o`, `$r`, `$c`), and by the length of the overload suffix for overloaded routines. A flattened name such as `package$routine$type$r` can therefore be truncated even when the original Oracle name was comfortably within Oracle's own limit.

## Name length and truncation
<a name="sc-default-rules-naming-length-oracle"></a>

PostgreSQL limits identifiers to 63 bytes, whereas Oracle allows 128 bytes. Names most often exceed the PostgreSQL limit because of the names that DMS Schema Conversion assembles itself — merged schema names and flattened Oracle package members such as `package$routine$type$r`. The limit is a property of the target engine and isn't configurable.

DMS Schema Conversion shortens a name that's too long and adds a `$` plus a short hash. For example, the 69-character Oracle table `EXAMPLE_OF_A_TEST_TABLE_WITH_A_NAME_LENGTH_GREATER_THAN_64_CHARACTERS` becomes `example_of_a_test_table_with_a_name_length_greater_tha$cbd395b8`.

DMS Schema Conversion derives the hash from the object's full owner path — and, for routines, from the parameter signature as well — so two long names that share a prefix still convert to different target names instead of colliding.

## Reserved words treated as non-plain identifiers
<a name="sc-default-rules-naming-reserved-oracle"></a>

DMS Schema Conversion doesn't treat a source name that matches one of the following PostgreSQL reserved words as a plain identifier. It keeps the name exactly as spelled in your source and quotes it in the target. Because the name is quoted, you must quote it everywhere that you reference it in the target.

For an Oracle source, a table named `SELECT` becomes `"SELECT"`.

`ALL`, `ANALYSE`, `ANALYZE`, `AND`, `ANY`, `ARRAY`, `AS`, `ASC`, `ASYMMETRIC`, `BOTH`, `CASE`, `CAST`, `CHECK`, `COLLATE`, `COLUMN`, `CONSTRAINT`, `CREATE`, `CURRENT_CATALOG`, `CURRENT_DATE`, `CURRENT_ROLE`, `CURRENT_SCHEMA`, `CURRENT_TIME`, `CURRENT_TIMESTAMP`, `CURRENT_USER`, `DAY_HOUR`, `DEFAULT`, `DEFERRABLE`, `DESC`, `DISTINCT`, `DO`, `ELSE`, `END`, `EXCEPT`, `EXTRACT`, `FALSE`, `FETCH`, `FOR`, `FOREIGN`, `FROM`, `GRANT`, `GROUP`, `HAVING`, `IN`, `INITIALLY`, `INTERSECT`, `INTO`, `LATERAL`, `LEADING`, `LEFT`, `LIMIT`, `LOCALTIME`, `LOCALTIMESTAMP`, `NOT`, `NULL`, `OFFSET`, `ON`, `ONLY`, `OR`, `ORDER`, `OUTER`, `PLACING`, `PRIMARY`, `REFERENCES`, `RETURNING`, `RIGHT`, `SELECT`, `SESSION_USER`, `SOME`, `SQLSTATE`, `SYMMETRIC`, `TABLE`, `THEN`, `TO`, `TRAILING`, `TRUE`, `UNION`, `UNIQUE`, `UPDATE`, `USER`, `USING`, `VARIADIC`, `WHEN`, `WHERE`, `WINDOW`, `WITH`