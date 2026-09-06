

# Oracle to PostgreSQL conversion settings
<a name="schema-conversion-oracle-postgresql"></a>

The following settings apply when the source is Oracle and the target is Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL. You can configure these settings using the AWS Management Console or the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation.

This topic covers settings specific to the Oracle to PostgreSQL conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section names `ORACLE_TO_POSTGRESQL`, `ORACLE_TO_POSTGRESQL_14`, or `ORACLE_TO_POSTGRESQL_15`. All three versioned sections accept the same keys. To find which section names your project uses, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

Each setting shows the AWS Management Console label followed by the API and AWS CLI parameter name in parentheses. Use the parameter name when configuring settings with the API or AWS CLI. The settings are listed in the same order that they appear in the AWS Management Console.

**Target engine version** (`ORACLE_TO_POSTGRESQL_target_engine_version`)  
Choose the engine version for your target database. This setting is the PostgreSQL major version feature set that DMS Schema Conversion targets for conversion, and it determines which versioned settings section DMS Schema Conversion applies (`ORACLE_TO_POSTGRESQL_14` or `ORACLE_TO_POSTGRESQL_15`). The value `15` targets the features of PostgreSQL 15 and later versions, and `14` targets the features of PostgreSQL 14, so your target database can run a later version than the value you choose (for example, a value of `15` for a PostgreSQL 16 target). Unlike the other settings on this page, this setting isn't stored in a conversion path section. Instead, it's stored in the top-level `Conversion version` section, as shown in the following example.  

```
{
  "Conversion version": {
    "ORACLE_TO_POSTGRESQL_target_engine_version": "15"
  }
}
```
**Type:** String (`14` \| `15`)  
**Default:** `15`

**Materialized views** (`MaterializedViewConvert`)  
Specifies how DMS Schema Conversion converts Oracle materialized views on the target.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-oracle-postgresql.html)
**Type:** String (`TABLE` \| `MATERIALIZED_VIEW`)  
**Default:** `TABLE`

**Generate row id** (`GenerateRowId`)  
Your source Oracle database can use the `ROWID` pseudocolumn. PostgreSQL doesn't support similar functionality. This setting specifies whether DMS Schema Conversion emulates the `ROWID` pseudocolumn in the converted code, and which data type DMS Schema Conversion uses for emulation.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-oracle-postgresql.html)
**Type:** String (enum)  
**Default:** `false`

Select the conversion settings that are specific to your source Oracle code.

**Use the optimized data type mapping for columns of the NUMBER data type** (`UseOptimizedMappingForNumberConversion`)  
Specifies whether DMS Schema Conversion maps each Oracle `NUMBER` column to the best fitting numeric data type based on the precision and scale.  
+ `true` — DMS Schema Conversion maps each `NUMBER` column to the most specific PostgreSQL numeric type (for example, `SMALLINT`, `INTEGER`, or `BIGINT`) based on its precision and scale.
+ `false` — DMS Schema Conversion maps all `NUMBER` columns to `NUMERIC`.
**Type:** Boolean (`true` \| `false`)  
**Default:** `true`

**Use a native PostgreSQL TO\_CHAR function** (`ToCharFunctionOracle`)  
Specifies whether DMS Schema Conversion emulates the Oracle `TO_CHAR` function in the converted code.  
+ `false` — DMS Schema Conversion emulates the Oracle `TO_CHAR` behavior in the converted code.
+ `true` — DMS Schema Conversion converts `TO_CHAR` and `TO_NCHAR` calls to the native PostgreSQL `TO_CHAR` function. Select this to avoid emulation when your format strings are compatible with PostgreSQL.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Use a native PostgreSQL TO\_DATE function** (`ToDateFunctionOracle`)  
Specifies whether DMS Schema Conversion emulates the Oracle `TO_DATE` function in the converted code.  
+ `false` — DMS Schema Conversion emulates the Oracle `TO_DATE` behavior in the converted code.
+ `true` — DMS Schema Conversion converts `TO_DATE` calls to the native PostgreSQL `TO_DATE` function.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Use a native PostgreSQL TO\_NUMBER function** (`ToNumber`)  
Specifies whether DMS Schema Conversion emulates the Oracle `TO_NUMBER` function in the converted code.  
+ `false` — DMS Schema Conversion emulates the Oracle `TO_NUMBER` behavior in the converted code.
+ `true` — DMS Schema Conversion converts `TO_NUMBER` calls to the native PostgreSQL `TO_NUMBER` function.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Improve the performance of the converted code where the database and applications use the same time zone** (`ToTimeZone`)  
Specifies whether DMS Schema Conversion emulates time zones in the converted code.  
+ `true` — DMS Schema Conversion doesn't emulate time zones. Use this when your database and applications use the same time zone. The converted code runs faster.
+ `false` — DMS Schema Conversion emulates time zones in the converted code.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Populate converted sequences with the last value generated on the source side** (`AlertSequenceRestart`)  
Specifies whether DMS Schema Conversion continues converted sequences from the last value generated on the source.  
+ `true` — DMS Schema Conversion sets each converted sequence to start from the last value generated on the source, so sequences continue without conflicts.
+ `false` — DMS Schema Conversion starts converted sequences from their default initial value.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Convert primary and foreign key columns of the NUMBER data type to the BIGINT data type** (`ConvertNumberToBigint`)  
Specifies whether DMS Schema Conversion converts primary key and foreign key columns of the `NUMBER` data type to `BIGINT`. Use with caution to avoid data loss if your source database stores floating-point numbers in these columns.  
+ `true` — DMS Schema Conversion maps primary key and foreign key `NUMBER` columns to `BIGINT`.
+ `false` — DMS Schema Conversion uses the standard numeric mapping for these columns.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Convert only active triggers and constraints** (`IgnoreDisabledTriggersConstraints`)  
Specifies whether DMS Schema Conversion skips deactivated triggers and constraints during conversion.  
+ `true` — DMS Schema Conversion converts only active triggers and constraints and skips deactivated ones.
+ `false` — DMS Schema Conversion converts all triggers and constraints, including deactivated ones.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Convert the dynamic SQL code that is created in called routines** (`ConvertOutputAsDynamic`)  
Specifies whether DMS Schema Conversion converts string variables that are referenced outside the routine as dynamic SQL.  
+ `true` — DMS Schema Conversion converts string variables that are referenced outside the routine as dynamic SQL.
+ `false` — DMS Schema Conversion doesn't convert these string variables as dynamic SQL.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Convert procedures to functions** (`ConvertProceduresToFunction`)  
Specifies whether DMS Schema Conversion converts Oracle stored procedures to PostgreSQL void functions.  
+ `true` — DMS Schema Conversion converts Oracle stored procedures to PostgreSQL void functions.
+ `false` — DMS Schema Conversion converts Oracle stored procedures to PostgreSQL procedures.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Keep the names of system generated constraints** (`ConvertSysConstraintNamesUsingOriginal`)  
Specifies whether DMS Schema Conversion keeps the original Oracle system-generated constraint names in the target. Use this option if your source Oracle code uses system-generated constraint names to create constraints with the same names in your target database.  
+ `true` — DMS Schema Conversion keeps the original Oracle system-generated constraint names in the target.
+ `false` — DMS Schema Conversion generates new constraint names.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Set the time zone of your source database** (`UseDefaultTimeZoneForSysdateEmulation`)  
Specifies whether the function that emulates the Oracle `SYSDATE` function uses the time zone in `DefaultTimeZoneForSysdateEmulation`, so that the converted code returns the same values as your source database.  
+ `true` — DMS Schema Conversion uses the time zone specified in `DefaultTimeZoneForSysdateEmulation` for `SYSDATE` emulation.
+ `false` — DMS Schema Conversion uses the default time zone for `SYSDATE` emulation.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`DefaultTimeZoneForSysdateEmulation`  
The time zone that DMS Schema Conversion uses when `SYSDATE` emulation is turned on with `UseDefaultTimeZoneForSysdateEmulation`. Specify a valid IANA time zone name, such as `UTC`, `America/New_York`, or `Europe/Berlin`. This value has no effect when `UseDefaultTimeZoneForSysdateEmulation` is `false`.  
**Type:** String (IANA time zone name)  
**Default:** `UTC`

**Note**  
The AWS Management Console lists an additional option, **Add extension pack functions that raise user-defined exceptions**, between **Convert procedures to functions** and **Keep the names of system generated constraints**. This option is configured only in the AWS Management Console and isn't available through the API or AWS CLI. The related severity-level behavior is controlled by the `ShowSeverityLevelInSql` common setting. For more information, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

Choose the Orafce built-in routines to use in the converted code. Orafce is a PostgreSQL extension that provides routines compatible with Oracle built-in functions. Each routine has a dedicated Boolean setting. When you set a routine to `true`, DMS Schema Conversion converts the matching Oracle built-in function to its Orafce routine. When you set it to `false`, DMS Schema Conversion leaves the function as an action item for manual review. To use these routines, the orafce extension must be available on your target database. All of these routines default to `false`. Set a routine to `true` only after you verify that the function's behavior in your usage is compatible with the Orafce routine.


| Setting name | Oracle built-in function | 
| --- | --- | 
| AddMonthsBuiltinFunctionOracle | ADD\_MONTHS | 
| BitandBuiltinFunctionOracle | BITAND | 
| CoshBuiltinFunctionOracle | COSH | 
| DbmsAssertBuiltinFunctionOracle | DBMS\_ASSERT package | 
| DbmsOutputBuiltinFunctionOracle | DBMS\_OUTPUT package | 
| DbmsRandomBuiltinFunctionOracle | DBMS\_RANDOM package | 
| DbtimezoneBuiltinFunctionOracle | DBTIMEZONE | 
| DecodeBuiltinFunctionOracle | DECODE | 
| DumpBuiltinFunctionOracle | DUMP | 
| InstrBuiltinFunctionOracle | INSTR | 
| InstrbBuiltinFunctionOracle | INSTRB | 
| LastDayBuiltinFunctionOracle | LAST\_DAY | 
| LengthBuiltinFunctionOracle | LENGTH | 
| LengthbBuiltinFunctionOracle | LENGTHB | 
| ListaggBuiltinFunctionOracle | LISTAGG | 
| LnnvlBuiltinFunctionOracle | LNNVL | 
| LpadBuiltinFunctionOracle | LPAD | 
| LtrimBuiltinFunctionOracle | LTRIM | 
| MedianBuiltinFunctionOracle | MEDIAN | 
| MonthsBetweenBuiltinFunctionOracle | MONTHS\_BETWEEN | 
| NanvlBuiltinFunctionOracle | NANVL | 
| NextDayBuiltinFunctionOracle | NEXT\_DAY | 
| NlssortBuiltinFunctionOracle | NLSSORT | 
| Nvl2BuiltinFunctionOracle | NVL2 | 
| NvlBuiltinFunctionOracle | NVL | 
| RoundDateFmtBuiltinFunctionOracle | ROUND (date) | 
| RoundNumberBuiltinFunctionOracle | ROUND (number) | 
| RpadBuiltinFunctionOracle | RPAD | 
| RtrimBuiltinFunctionOracle | RTRIM | 
| SessiontimezoneBuiltinFunctionOracle | SESSIONTIMEZONE | 
| SinhBuiltinFunctionOracle | SINH | 
| SubstrBuiltinFunctionOracle | SUBSTR | 
| SubstrbBuiltinFunctionOracle | SUBSTRB | 
| SysdateBuiltinFunctionOracle | SYSDATE | 
| TanhBuiltinFunctionOracle | TANH | 
| ToCharDatetimeBuiltinFunctionOracle | TO\_CHAR (datetime) | 
| ToCharNumberBuiltinFunctionOracle | TO\_CHAR (number) | 
| ToDateBuiltinFunctionOracle | TO\_DATE | 
| ToMultiByteBuiltinFunctionOracle | TO\_MULTI\_BYTE | 
| ToNumberBuiltinFunctionOracle | TO\_NUMBER | 
| ToSingleByteBuiltinFunctionOracle | TO\_SINGLE\_BYTE | 
| TruncDateBuiltinFunctionOracle | TRUNC (date) | 
| TruncNumberBuiltinFunctionOracle | TRUNC (number) | 

Each routine is a separate Boolean key. The following example turns on the Orafce routines for the Oracle `ADD_MONTHS`, `NVL`, and `SUBSTR` functions. Add or remove keys to match the functions in your source code, and apply the same keys to each section name that your project uses.

```
{
  "ORACLE_TO_POSTGRESQL_15": {
    "AddMonthsBuiltinFunctionOracle": true,
    "NvlBuiltinFunctionOracle": true,
    "SubstrBuiltinFunctionOracle": true
  }
}
```

Configure how DMS Schema Conversion handles Oracle built-in objects that PostgreSQL doesn't support.

**Convert unsupported built-in objects to stub objects** (`ConvUnsupportedBuiltinsToStubs`)  
Specifies whether DMS Schema Conversion substitutes unsupported built-in objects with stub objects.  
+ `false` — DMS Schema Conversion leaves unsupported built-in objects as action items in the assessment report.
+ `true` — DMS Schema Conversion replaces each unsupported built-in object with a stub object that has the same signature. The converted object compiles, so you can deploy and test the rest of the schema before you address individual stubs.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Create stub objects in a separate schema** (`CreateStubsInSeparateSchema`)  
Specifies whether DMS Schema Conversion creates stub objects in a separate schema. This option appears in the AWS Management Console only when **Convert unsupported built-in objects to stub objects** is selected, and it takes effect only when that option is enabled.  
+ `true` — DMS Schema Conversion creates stub objects in a separate schema. This keeps your application schemas clean and makes it easy to identify which stubs still need implementation.
+ `false` — DMS Schema Conversion creates stub objects in the same schema as the converted object.
**Type:** Boolean (`true` \| `false`)  
**Default:** `true`

## Example: configure Oracle to PostgreSQL settings
<a name="schema-conversion-oracle-postgresql-example"></a>

The following example keeps materialized views as PostgreSQL materialized views, emulates the `ROWID` pseudocolumn by using the `bigint` data type, and converts procedures to functions. Apply the same settings to each section name that your project uses (check the output of [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first).

```
{
  "ORACLE_TO_POSTGRESQL_15": {
    "MaterializedViewConvert": "MATERIALIZED_VIEW",
    "GenerateRowId": "true",
    "ConvertProceduresToFunction": true
  },
  "ORACLE_TO_POSTGRESQL_14": {
    "MaterializedViewConvert": "MATERIALIZED_VIEW",
    "GenerateRowId": "true",
    "ConvertProceduresToFunction": true
  },
  "ORACLE_TO_POSTGRESQL": {
    "MaterializedViewConvert": "MATERIALIZED_VIEW",
    "GenerateRowId": "true",
    "ConvertProceduresToFunction": true
  }
}
```