

# Data type support by SQL engine
<a name="sql-reference-supported-data-types-dialect"></a>

AWS Clean Rooms supports multiple SQL engines and dialects. Understanding the data type systems across these implementations is crucial for successful data collaboration and analysis. The following tables show the equivalent data types across AWS Clean Rooms SQL, Snowflake SQL, and Spark SQL. 

## Numeric data types
<a name="numeric-data-types-table"></a>

Numeric types represent various kinds of numbers, from precise integers to approximate floating-point values. The choice of numeric type affects both storage requirements and computational precision. Integer types vary by byte size, while decimal and floating-point types offer different precision and scale options. 


| Data type | AWS Clean Rooms SQL | Snowflake SQL | Spark SQL | Description | 
| --- | --- | --- | --- | --- | 
| 8-byte Integer | BIGINT | Not supported | BIGINT, LONG | Signed integers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807. | 
| 4-byte Integer | INT | Not supported | INT, INTEGER | Signed integers from -2,147,483,648 to 2,147,483,647 | 
| 2-byte Integer | SMALLINT  | Not supported | SMALLINT, SHORT | Signed integers from -32,768 to 32,767 | 
| 1-byte Integer | Not supported | Not supported | TINYINT, BYTE | Signed integers from -128 to 127 | 
|  Double Precision Float | DOUBLE, DOUBLE PRECISION | FLOAT, FLOAT4, FLOAT8, DOUBLE, DOUBLE PRECISION, REAL | DOUBLE | 8-byte double-precision floating point numbers | 
| Single Precision Float | REAL, FLOAT | Not supported | FLOAT | 4-byte single-precision floating point numbers | 
| Decimal (fixed precision) | DECIMAL  | DECIMAL, NUMERIC, NUMBER Snowflake automatically aliases smaller-width exact numeric types (INT, BIGINT, SMALLINT, etc.) to NUMBER.  | DECIMAL, NUMERIC,  | Arbitrary-precision signed decimal numbers | 
| Decimal (with precision) | DECIMAL(p) | DECIMAL(p), NUMBER(p) | DECIMAL(p) | Fixed-precision decimal numbers | 
| Decimal (with scale) | DECIMAL(p,s) | DECIMAL(p,s), NUMBER(p,s) | DECIMAL(p,s) | Fixed-precision decimal numbers with scale | 

## Boolean data types
<a name="boolean-data-types-table"></a>

Boolean types represent simple true/false logical values. These types are consistent across SQL engines and are commonly used for flags, conditions, and logical operations. 


| Data type | AWS Clean Rooms SQL | Snowflake SQL | Spark SQL | Description | 
| --- | --- | --- | --- | --- | 
| Boolean  | BOOLEAN  | BOOLEAN  | BOOLEAN  | Represents true/false values  | 

## Date and time data types
<a name="date-time-data-types-table"></a>

Date and time types handle temporal data, with varying levels of precision and time zone awareness. These types support different formats for storing dates, times, and timestamps, with options for including or excluding time zone information. 


| Data type | AWS Clean Rooms SQL | Snowflake SQL | Spark SQL | Description | 
| --- | --- | --- | --- | --- | 
| Date  | DATE  | DATE  | DATE  | Date values (year, month, day) without time zone | 
| Time  | TIME  | Not supported | Not supported | Time of day in UTC, without time zone | 
| Time with TZ | TIMETZ  | Not supported | Not supported | Time of day in UTC, with time zone | 
| Timestamp  | TIMESTAMP  | TIMESTAMP, TIMESTAMP\_NTZ | TIMESTAMP\_NTZ |  Timestamp without time zone NTZ indicates "No Time Zone"  | 
| Timestamp with TZ | TIMESTAMPTZ  | TIMESTAMP\_LTZ | TIMESTAMP, TIMESTAMP\_LTZ | Timestamp with local time zone LTZ indicates "Local Time Zone"  | 

## Character data types
<a name="character-data-types-table"></a>

Character types store textual data, offering both fixed-length and variable-length options. These types handle text strings and binary data, with optional length specifications to control storage allocation. 


| Data type | AWS Clean Rooms SQL | Snowflake SQL | Spark SQL | Description | 
| --- | --- | --- | --- | --- | 
| Fixed-length Character  | CHAR  | CHAR, CHARACTER | CHAR, CHARACTER | Fixed-length character string | 
| Fixed-length Character with Length | CHAR(n) | CHAR(n), CHARACTER(n) | CHAR(n), CHARACTER(n) | Fixed-length character string with specified length | 
| Variable-length Character | VARCHAR  | VARCHAR, STRING, TEXT | VARCHAR, STRING | Variable-length character string | 
| Variable-length Character with Length | VARCHAR(n) | VARCHAR(n), STRING(n), TEXT(n) | VARCHAR(n) | Variable-length character string with length limit  | 
| Binary  | VARBYTE  | BINARY, VARBINARY | BINARY  | Binary byte sequence | 
| Binary with Length | VARBYTE(n) | Not supported | Not supported | Binary byte sequence with length limit | 

## Structured data types
<a name="structured-data-types-table"></a>

Structured types allow for complex data organization by combining multiple values into single fields. These include arrays for ordered collections, maps for key-value pairs, and structs for creating custom data structures with named fields. 


| Data type | AWS Clean Rooms SQL | Snowflake SQL | Spark SQL | Description | 
| --- | --- | --- | --- | --- | 
| Array  | ARRAY<type> | ARRAY(type) | ARRAY<type> | Ordered sequence of elements of the same type Array types must contain elements of the same type  | 
| Map  | MAP<key,value> | MAP(key,value) | MAP<key,value> | Collection of key-value pairs Map types must contain elements of the same type  | 
| Struct  | STRUCT< field1: type1, field2: type2> |  OBJECT( field1 type1, field2 type2 ) | STRUCT< field1: type1, field2: type2 > | Structure with named fields of specified types Structured type syntax may vary slightly between implementations  | 
| Super  | SUPER  | Not supported | Not supported | Flexible type supporting all data types including complex types | 