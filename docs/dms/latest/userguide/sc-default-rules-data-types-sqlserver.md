

# Data type rules
<a name="sc-default-rules-data-types-sqlserver"></a>

The following rules apply when you convert a Microsoft SQL Server database to Amazon Aurora PostgreSQL or Amazon RDS for PostgreSQL.

**Context matters**  
Some data type rules depend on where the type is used, such as a table column, a variable inside a procedure, or a routine parameter. The same source type can convert differently in each context.

Amazon Aurora PostgreSQL and Amazon RDS for PostgreSQL share one rule set, so the rules on this page apply to both targets.

## Table columns, procedure and function parameters
<a name="sc-default-rules-data-types-sqlserver-all"></a>

The following rules apply to table columns and to procedure and function parameters.


| Source data type | Applies when | Target data type | Notes | 
| --- | --- | --- | --- | 
| BIGINT | Always | BIGINT | None | 
| BINARY | Always | BYTEA | None | 
| BIT | Always | NUMERIC(1,0) | None | 
| CHAR(n) | Length is specified | CHAR(n) | None | 
| CHAR | No length specified | CHAR(1) | None | 
| DATE | Always | DATE | None | 
| DATETIME | Always | TIMESTAMP WITHOUT TIME ZONE | None | 
| DATETIME2(p) | Precision ≤ 6 | TIMESTAMP(p) WITHOUT TIME ZONE | None | 
| DATETIME2 | All other cases | TIMESTAMP(6) WITHOUT TIME ZONE | None | 
| DATETIMEOFFSET(p) | Precision ≤ 6 | TIMESTAMP(p) WITH TIME ZONE | None | 
| DATETIMEOFFSET | All other cases | TIMESTAMP(6) WITH TIME ZONE | None | 
| DECIMAL | Identity column, precision 1–5 | SMALLINT | None | 
| DECIMAL | Identity column, precision 6–13 | INTEGER | None | 
| DECIMAL | Identity column, precision 14–19 | BIGINT | None | 
| DECIMAL | Identity column, precision 20–38 | BIGINT | AI 7936: PostgreSQL doesn't support identity columns of the DECIMAL or NUMERIC data type with precision greater than 19 | 
| DECIMAL(p,s) | Precision and scale are specified | NUMERIC(p,s) | None | 
| DECIMAL(p) | Precision is specified | NUMERIC(p,0) | None | 
| DECIMAL | All other cases | NUMERIC(18,0) | None | 
| DOUBLE PRECISION | Always | DOUBLE PRECISION | None | 
| FLOAT | Always | DOUBLE PRECISION | None | 
| GEOGRAPHY | Always | GEOGRAPHY | None | 
| GEOMETRY | Always | GEOMETRY | None | 
| HIERARCHYID | Always | VARCHAR(8000) | AI 7657: PostgreSQL doesn't support the hierarchyid data type | 
| IMAGE | Always | BYTEA | None | 
| INT | Always | INTEGER | None | 
| MONEY | Always | NUMERIC(19,4) | None | 
| NCHAR(n) | Length between 1 and 4000 | CHAR(n) | None | 
| NCHAR | No length specified | CHAR(1) | None | 
| NTEXT | Always | TEXT | None | 
| NUMERIC | Identity column, precision 1–5 | SMALLINT | None | 
| NUMERIC | Identity column, precision 6–13 | INTEGER | None | 
| NUMERIC | Identity column, precision 14–19 | BIGINT | None | 
| NUMERIC | Identity column, precision 20–38 | BIGINT | AI 7936: PostgreSQL doesn't support identity columns of the DECIMAL or NUMERIC data type with precision greater than 19 | 
| NUMERIC(p,s) | Precision and scale are specified | NUMERIC(p,s) | None | 
| NUMERIC(p) | Precision is specified | NUMERIC(p,0) | None | 
| NUMERIC | All other cases | NUMERIC(18,0) | None | 
| NVARCHAR | Length is MAX | TEXT | None | 
| NVARCHAR(n) | Length ≥ 1 | VARCHAR(n) | None | 
| NVARCHAR | No length specified | VARCHAR(1) | None | 
| REAL | Always | DOUBLE PRECISION | None | 
| ROWVERSION | Always | BIGINT | None | 
| SMALLDATETIME | Always | TIMESTAMP WITHOUT TIME ZONE | None | 
| SMALLINT | Always | SMALLINT | None | 
| SMALLMONEY | Always | NUMERIC(10,4) | None | 
| SQL\_VARIANT | Always | VARCHAR(8000) | AI 7658: PostgreSQL doesn't support the sql\_variant data type | 
| SYSNAME | Always | VARCHAR(128) | None | 
| TEXT | Always | TEXT | None | 
| TIME(p) | Precision ≤ 6 | TIME(p) WITHOUT TIME ZONE | None | 
| TIME | All other cases | TIME(6) WITHOUT TIME ZONE | None | 
| TIMESTAMP | Always | BIGINT | None | 
| TINYINT | Always | SMALLINT | None | 
| UNIQUEIDENTIFIER | Always | UUID | None | 
| VARBINARY | Always | BYTEA | None | 
| VARCHAR | Length is MAX | TEXT | None | 
| VARCHAR(n) | Length between 1 and 8000 | VARCHAR(n) | None | 
| VARCHAR | No length specified | VARCHAR(1) | None | 
| XML | Always | XML | None | 
| any unrecognized type | Always | VARCHAR(8000) | None | 

## CAST and CONVERT
<a name="sc-default-rules-data-types-sqlserver-cast"></a>

The following rules apply to the target data type in a `CAST` or `CONVERT` expression. When a character type has no length, SQL Server uses a length of 30 in these expressions, and DMS Schema Conversion keeps that length. All other data types convert as described in [Table columns, procedure and function parameters](#sc-default-rules-data-types-sqlserver-all).


| Source data type | Applies when | Target data type | Notes | 
| --- | --- | --- | --- | 
| CHAR | No length specified | CHAR(30) | None | 
| NCHAR | No length specified | CHAR(30) | None | 
| NVARCHAR | No length specified | VARCHAR(30) | None | 
| VARCHAR | No length specified | VARCHAR(30) | None | 