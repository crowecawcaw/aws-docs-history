

# Data type rules
<a name="sc-default-rules-data-types-oracle"></a>

The following rules apply when you convert an Oracle database to Amazon Aurora PostgreSQL or Amazon RDS for PostgreSQL.

**NUMBER columns**  
The setting *Use the optimized data type mapping for columns of the NUMBER data type* is enabled by default. As a result, a `NUMBER` column normally becomes `INTEGER` (precision <= 9, scale 0), `BIGINT` (precision 10–18, scale 0), `DOUBLE PRECISION` (scale > 0 and precision \+ scale <= 15), or otherwise `NUMERIC`. An unconstrained `NUMBER` becomes `NUMERIC` and raises AI 5984. Any other `NUMBER(p,s)` becomes `NUMERIC(p,s)`. The following table lists these rules.

**Context matters**  
Some data type rules depend on where the type is used, such as a table column, a variable inside a procedure, or a routine parameter. The same source type can convert differently in each context.

Amazon Aurora PostgreSQL and Amazon RDS for PostgreSQL share one rule set, so the rules on this page apply to both targets.

## Table columns
<a name="sc-default-rules-data-types-oracle-columns"></a>

The following rules apply to columns in tables. DMS Schema Conversion evaluates the rules in the order shown.


| Source data type | Applies when | Target data type | Notes | 
| --- | --- | --- | --- | 
| ANYDATA | Always | JSONB | None | 
| BFILE | Always | CHARACTER VARYING(255) | AI 5212: PostgreSQL doesn't support the BFILE data type | 
| BINARY\_DOUBLE | Always | DOUBLE PRECISION | None | 
| BINARY\_FLOAT | Always | REAL | None | 
| BLOB | Always | BYTEA | None | 
| CHAR(n) | Always | CHARACTER(n) | None | 
| CHARACTER(n) | Always | CHARACTER(n) | None | 
| CLOB | Always | TEXT | None | 
| DATE | Always | TIMESTAMP(0) WITHOUT TIME ZONE | None | 
| FLOAT | Always | DOUBLE PRECISION | None | 
| INTERVAL DAY(p) TO SECOND(s) | Always | INTERVAL DAY TO SECOND(s) | None | 
| INTERVAL YEAR(p) TO MONTH | Always | INTERVAL YEAR TO MONTH | None | 
| LONG | Always | TEXT | None | 
| LONG RAW | Always | BYTEA | None | 
| NCHAR(n) | Always | CHARACTER(n) | None | 
| NCHAR VARYING(n) | Length between 1 and 4000 | CHARACTER VARYING(n) | None | 
| NCLOB | Always | TEXT | None | 
| NUMBER | Identity column | BIGINT | None | 
| NUMBER(p,0) | Precision ≤ 9, scale 0 | INTEGER | None | 
| NUMBER(p,0) | Precision 10–18, scale 0 | BIGINT | None | 
| NUMBER(\*,0) | No precision, scale 0 | NUMERIC(38,0) | AI 5984: DMS SC uses the NUMERIC data type to convert the column because you haven't specified the precision and scale values in your source code. Your converted code can work faster if you use the optimized data type mapping | 
| NUMBER(\*,s) | No precision, scale given | NUMERIC(38,s) | AI 5984: DMS SC uses the NUMERIC data type to convert the column because you haven't specified the precision and scale values in your source code. Your converted code can work faster if you use the optimized data type mapping | 
| NUMBER(p,s) | Scale > 0 and precision \+ scale ≤ 15 | DOUBLE PRECISION | None | 
| NUMBER | No precision or scale | NUMERIC | AI 5984: DMS SC uses the NUMERIC data type to convert the column because you haven't specified the precision and scale values in your source code. Your converted code can work faster if you use the optimized data type mapping | 
| NUMBER(p,s) | Scale > 0 and precision \+ scale > 15, or scale = 0 and precision ≥ 19 | NUMERIC(p,s) | None | 
| NVARCHAR2(n) | Always | CHARACTER VARYING(n) | None | 
| RAW | Always | BYTEA | None | 
| ROWID | Always | CHARACTER(255) | AI 5550: PostgreSQL doesn't support the ROWID data type | 
| SDO\_GEOMETRY | Always | GEOMETRY | None | 
| SDO\_POINT\_TYPE | Always | GEOMETRY | None | 
| TIMESTAMP(p) | Precision ≤ 6 | TIMESTAMP(p) WITHOUT TIME ZONE | None | 
| TIMESTAMP(p) WITH TIME ZONE | Precision ≤ 6 | TIMESTAMP(p) WITH TIME ZONE | None | 
| TIMESTAMP(p) WITH LOCAL TIME ZONE | Precision ≤ 6 | TIMESTAMP(p) WITHOUT TIME ZONE | None | 
| TIMESTAMP(p) | Precision > 6 | TIMESTAMP(6) WITHOUT TIME ZONE | AI 5213: PostgreSQL ensures support of microseconds for time, datetime, and timestamp data types | 
| TIMESTAMP(p) WITH TIME ZONE | Precision > 6 | TIMESTAMP(6) WITH TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIMESTAMP(p) WITH LOCAL TIME ZONE | Precision > 6 | TIMESTAMP(6) WITHOUT TIME ZONE | AI 5553: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| UROWID | Always | CHARACTER VARYING(8000) | AI 5551: PostgreSQL doesn't support the UROWID data type | 
| VARCHAR(n) | Length ≤ 4000 | CHARACTER VARYING(n) | None | 
| VARCHAR2(n) | Always | CHARACTER VARYING(n) | None | 
| XMLTYPE | Always | XML | None | 
| any unrecognized type | Always | VARCHAR(8000) | AI 5028: DMS SC can't convert object definitions with the unsupported ⟨any unrecognized type⟩ data type | 

## Procedure and function parameters
<a name="sc-default-rules-data-types-oracle-parameters"></a>

The following rules apply to parameters in procedures and functions.


| Source data type | Applies when | Target data type | Notes | 
| --- | --- | --- | --- | 
| ANYDATA | Always | JSONB | None | 
| BFILE | Always | CHARACTER VARYING | AI 5212: PostgreSQL doesn't support the BFILE data type | 
| BINARY\_DOUBLE | Always | DOUBLE PRECISION | None | 
| BINARY\_FLOAT | Always | REAL | None | 
| BINARY\_INTEGER | Always | INTEGER | None | 
| BLOB | Always | BYTEA | None | 
| BOOLEAN | Always | BOOLEAN | None | 
| CHAR | Always | CHARACTER | None | 
| CHAR VARYING | Always | CHARACTER VARYING | None | 
| CHARACTER | Always | CHARACTER | None | 
| CHARACTER VARYING | Always | CHARACTER VARYING | None | 
| CLOB | Always | TEXT | None | 
| DATE | Always | TIMESTAMP WITHOUT TIME ZONE | None | 
| DEC | Always | NUMERIC | None | 
| DECIMAL | Always | NUMERIC | None | 
| DOUBLE PRECISION | Always | DOUBLE PRECISION | None | 
| FLOAT | Always | DOUBLE PRECISION | None | 
| INT | Always | NUMERIC | None | 
| INTEGER | Always | NUMERIC | None | 
| INTERVAL DAY TO SECOND | Always | INTERVAL DAY TO SECOND | None | 
| INTERVAL YEAR TO MONTH | Always | INTERVAL YEAR TO MONTH | None | 
| LONG | Always | TEXT | None | 
| LONG RAW | Always | BYTEA | None | 
| NCHAR | Always | CHARACTER | None | 
| NCHAR VARYING | Always | TEXT | None | 
| NCLOB | Always | TEXT | None | 
| NUMBER | Always | DOUBLE PRECISION | None | 
| NUMERIC | Always | DOUBLE PRECISION | None | 
| NVARCHAR2 | Always | TEXT | None | 
| PLS\_INTEGER | Always | INTEGER | None | 
| RAW | Always | BYTEA | None | 
| REAL | Always | DOUBLE PRECISION | None | 
| ROWID | Always | CHARACTER | AI 5550: PostgreSQL doesn't support the ROWID data type | 
| SDO\_GEOMETRY | Always | GEOMETRY | None | 
| SDO\_POINT\_TYPE | Always | GEOMETRY | None | 
| SMALLINT | Always | NUMERIC | None | 
| SYS\_REFCURSOR | Always | REFCURSOR | None | 
| TIMESTAMP | Always | TIMESTAMP WITHOUT TIME ZONE | None | 
| TIMESTAMP WITH LOCAL TIME ZONE | Always | TIMESTAMP WITHOUT TIME ZONE | None | 
| TIMESTAMP WITH TIME ZONE | Always | TIMESTAMP WITH TIME ZONE | None | 
| UROWID | Always | TEXT | AI 5551: PostgreSQL doesn't support the UROWID data type | 
| VARCHAR | Always | TEXT | None | 
| VARCHAR2 | Always | TEXT | None | 
| XMLTYPE | Always | XML | None | 
| any unrecognized type | Always | CHARACTER VARYING | AI 5028: DMS SC can't convert object definitions with the unsupported ⟨any unrecognized type⟩ data type | 

## Variables in code objects
<a name="sc-default-rules-data-types-oracle-variables"></a>

The following rules apply to variables that are declared inside code objects, and to the target data type of a `CAST` expression in your source code.


| Source data type | Applies when | Target data type | Notes | 
| --- | --- | --- | --- | 
| ANYDATA | Always | JSONB | None | 
| BFILE | Always | CHARACTER VARYING(255) | AI 5212: PostgreSQL doesn't support the BFILE data type | 
| BINARY\_DOUBLE | Always | DOUBLE PRECISION | None | 
| BINARY\_FLOAT | Always | REAL | None | 
| BINARY\_INTEGER | Always | INTEGER | None | 
| BLOB | Always | BYTEA | None | 
| BOOLEAN | Always | BOOLEAN | None | 
| CHAR(n) | Length is specified | CHARACTER(n) | None | 
| CHAR | All other cases | CHARACTER(1) | None | 
| CHARACTER(n) | Always | CHARACTER(n) | None | 
| CHARACTER VARYING(n) | Always | CHARACTER VARYING(n) | None | 
| CLOB | Always | TEXT | None | 
| DATE | Always | TIMESTAMP(0) WITHOUT TIME ZONE | None | 
| DEC(p,s) | 0 < s ≤ p | NUMERIC(p,s) | None | 
| DEC(p,s) | Scale greater than p | NUMERIC(s,s) | None | 
| DEC, DEC(p), DEC(p,0), DEC(p,s) with negative s | Always | CHARACTER VARYING(8000) | AI 5028: DMS SC can't convert object definitions with the unsupported DEC data type | 
| DECIMAL(p,s) | 0 < s ≤ p | NUMERIC(p,s) | None | 
| DECIMAL(p,s) | Scale greater than p | NUMERIC(s,s) | None | 
| DECIMAL, DECIMAL(p), DECIMAL(p,0), DECIMAL(p,s) with negative s | Always | CHARACTER VARYING(8000) | AI 5028: DMS SC can't convert object definitions with the unsupported DECIMAL data type | 
| DOUBLE PRECISION | Always | DOUBLE PRECISION | None | 
| DSINTERVAL\_UNCONSTRAINED | Always | INTERVAL DAY TO SECOND(6) | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| FLOAT | Always | DOUBLE PRECISION | None | 
| INT | Always | NUMERIC(38) | None | 
| INTEGER | Always | NUMERIC(38) | None | 
| INTERVAL DAY(p) TO SECOND(s) | Always | INTERVAL DAY TO SECOND(s) | None | 
| INTERVAL DAY TO SECOND | Always | INTERVAL DAY TO SECOND | None | 
| INTERVAL YEAR(p) TO MONTH | Always | INTERVAL YEAR TO MONTH | None | 
| INTERVAL YEAR TO MONTH | Always | INTERVAL YEAR TO MONTH | None | 
| LONG | Always | TEXT | None | 
| LONG RAW | Always | BYTEA | None | 
| NATURAL | Always | INTEGER | None | 
| NATURALN | Always | INTEGER | None | 
| NCHAR(n) | Always | CHARACTER(n) | None | 
| NCHAR VARYING(n) | Always | CHARACTER VARYING(n) | None | 
| NCLOB | Always | TEXT | None | 
| NUMBER(p,s) | Scale between 0 and p | NUMERIC(p,s) | None | 
| NUMBER(p,s) | Scale not specified | NUMERIC(p,0) | None | 
| NUMBER(p,s) | Scale greater than p | NUMERIC(s,s) | None | 
| NUMBER(p) | Precision is specified | NUMERIC(p) | None | 
| NUMBER | All other cases | DOUBLE PRECISION | None | 
| NUMERIC(p,s) | Scale between 0 and p | NUMERIC(p,s) | None | 
| NUMERIC(p,s) | Scale not specified | NUMERIC(p,0) | None | 
| NUMERIC(p,s) | Scale greater than p | NUMERIC(s,s) | None | 
| NUMERIC | All other cases | DOUBLE PRECISION | None | 
| NVARCHAR2(n) | Always | CHARACTER VARYING(n) | None | 
| PLS\_INTEGER | Always | INTEGER | None | 
| POSITIVE | Always | INTEGER | None | 
| POSITIVEN | Always | INTEGER | None | 
| RAW | Always | BYTEA | None | 
| REAL | Always | DOUBLE PRECISION | None | 
| ROWID | Always | CHAR(255) | AI 5550: PostgreSQL doesn't support the ROWID data type | 
| SDO\_GEOMETRY | Always | GEOMETRY | None | 
| SDO\_POINT\_TYPE | Always | GEOMETRY | None | 
| SIGNTYPE | Always | INTEGER | None | 
| SIMPLE\_DOUBLE | Always | DOUBLE PRECISION | None | 
| SIMPLE\_FLOAT | Always | REAL | None | 
| SIMPLE\_INTEGER | Always | INTEGER | None | 
| SMALLINT | Always | NUMERIC(38) | None | 
| STRING(n) | Always | CHARACTER VARYING(n) | None | 
| SYS\_REFCURSOR | Always | REFCURSOR | None | 
| TIMESTAMP(p) | Precision ≤ 6 | TIMESTAMP(p) WITHOUT TIME ZONE | None | 
| TIMESTAMP(p) WITH TIME ZONE | Precision ≤ 6 | TIMESTAMP(p) WITH TIME ZONE | None | 
| TIMESTAMP(p) WITH LOCAL TIME ZONE | Precision ≤ 6 | TIMESTAMP(p) WITHOUT TIME ZONE | None | 
| TIMESTAMP(p) | Precision > 6 | TIMESTAMP(6) WITHOUT TIME ZONE | AI 5213: PostgreSQL ensures support of microseconds for time, datetime, and timestamp data types | 
| TIMESTAMP(p) WITH TIME ZONE | Precision > 6 | TIMESTAMP(6) WITH TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIMESTAMP(p) WITH LOCAL TIME ZONE | Precision > 6 | TIMESTAMP(6) WITHOUT TIME ZONE | AI 5553: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIMESTAMP | All other cases | TIMESTAMP(6) WITHOUT TIME ZONE | None | 
| TIMESTAMP WITH LOCAL TIME ZONE | Always | TIMESTAMP(6) WITHOUT TIME ZONE | None | 
| TIMESTAMP WITH TIME ZONE | Always | TIMESTAMP(6) WITH TIME ZONE | None | 
| TIMESTAMP\_LTZ\_UNCONSTRAINED | Always | TIMESTAMP(6) WITH TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIMESTAMP\_TZ\_UNCONSTRAINED | Always | TIMESTAMP(6) WITH TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIMESTAMP\_UNCONSTRAINED | Always | TIMESTAMP(6) WITHOUT TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIME\_TZ\_UNCONSTRAINED | Always | TIME(6) WITH TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| TIME\_UNCONSTRAINED | Always | TIME(6) WITHOUT TIME ZONE | AI 5552: PostgreSQL ensures support of microseconds for the time, datetime, and timestamp data types | 
| UROWID(n) | Always | CHARACTER VARYING(n) | AI 5551: PostgreSQL doesn't support the UROWID data type | 
| VARCHAR(n) | Always | CHARACTER VARYING(n) | None | 
| VARCHAR2(n) | Always | CHARACTER VARYING(n) | None | 
| XMLTYPE | Always | XML | None | 
| YMINTERVAL\_UNCONSTRAINED | Always | INTERVAL YEAR TO MONTH | None | 
| any unrecognized type | Always | CHARACTER VARYING(8000) | AI 5028: DMS SC can't convert object definitions with the unsupported ⟨any unrecognized type⟩ data type | 