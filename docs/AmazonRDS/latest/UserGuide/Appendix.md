# RDS for Oracle character sets

RDS for Oracle supports two types of character sets: the DB character set and national character set.

## DB character set

The Oracle database character set is used in the `CHAR`, `VARCHAR2`,
and `CLOB` data types. The database also uses this character set for metadata
such as table names, column names, and SQL statements. The Oracle database character set
is typically referred to as the _DB character set_.

You set the character set when you create a DB instance. You can't change the DB character set after you create
the database.

### Supported DB character sets

The following table lists the Oracle DB character sets that are supported in Amazon RDS. You can use a value from this
table with the `--character-set-name` parameter of the AWS CLI [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command or with the
`CharacterSetName` parameter of the Amazon RDS API [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") operation.

###### Note

The character set for a CDB is always AL32UTF8. You can set a different character set for the PDB only.

| Value          | Description                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| AL32UTF8       | Unicode 5.0 UTF-8 Universal character set (default)                                                                                            |
| AR8ISO8859P6   | ISO 8859-6 Latin/Arabic                                                                                                                        |
| AR8MSWIN1256   | Microsoft Windows Code Page 1256 8-bit Latin/Arabic                                                                                            |
| BLT8ISO8859P13 | ISO 8859-13 Baltic                                                                                                                             |
| BLT8MSWIN1257  | Microsoft Windows Code Page 1257 8-bit Baltic                                                                                                  |
| CL8ISO8859P5   | ISO 88559-5 Latin/Cyrillic                                                                                                                     |
| CL8MSWIN1251   | Microsoft Windows Code Page 1251 8-bit Latin/Cyrillic                                                                                          |
| EE8ISO8859P2   | ISO 8859-2 East European                                                                                                                       |
| EL8ISO8859P7   | ISO 8859-7 Latin/Greek                                                                                                                         |
| EE8MSWIN1250   | Microsoft Windows Code Page 1250 8-bit East European                                                                                           |
| EL8MSWIN1253   | Microsoft Windows Code Page 1253 8-bit Latin/Greek                                                                                             |
| IW8ISO8859P8   | ISO 8859-8 Latin/Hebrew                                                                                                                        |
| IW8MSWIN1255   | Microsoft Windows Code Page 1255 8-bit Latin/Hebrew                                                                                            |
| JA16EUC        | EUC 24-bit Japanese                                                                                                                            |
| JA16EUCTILDE   | Same as JA16EUC except for mapping of wave dash and tilde to and<br>from Unicode                                                               |
| JA16SJIS       | Shift-JIS 16-bit Japanese                                                                                                                      |
| JA16SJISTILDE  | Same as JA16SJIS except for mapping of wave dash and tilde to and<br>from Unicode                                                              |
| KO16MSWIN949   | Microsoft Windows Code Page 949 Korean                                                                                                         |
| NE8ISO8859P10  | ISO 8859-10 North European                                                                                                                     |
| NEE8ISO8859P4  | ISO 8859-4 North and Northeast European                                                                                                        |
| TH8TISASCII    | Thai Industrial Standard 620-2533-ASCII 8-bit                                                                                                  |
| TR8MSWIN1254   | Microsoft Windows Code Page 1254 8-bit Turkish                                                                                                 |
| US7ASCII       | ASCII 7-bit American                                                                                                                           |
| UTF8           | Unicode 3.0 UTF-8 Universal character set, CESU-8 compliant                                                                                    |
| VN8MSWIN1258   | Microsoft Windows Code Page 1258 8-bit Vietnamese                                                                                              |
| WE8ISO8859P1   | Western European 8-bit ISO 8859 Part 1                                                                                                         |
| WE8ISO8859P15  | ISO 8859-15 West European                                                                                                                      |
| WE8ISO8859P9   | ISO 8859-9 West European and Turkish                                                                                                           |
| WE8MSWIN1252   | Microsoft Windows Code Page 1252 8-bit West European                                                                                           |
| ZHS16GBK       | GBK 16-bit Simplified Chinese                                                                                                                  |
| ZHT16HKSCS     | Microsoft Windows Code Page 950 with Hong Kong Supplementary<br>Character Set HKSCS-2001. Character set conversion is based on<br>Unicode 3.0. |
| ZHT16MSWIN950  | Microsoft Windows Code Page 950 Traditional Chinese                                                                                            |
| ZHT32EUC       | EUC 32-bit Traditional Chinese                                                                                                                 |

### NLS_LANG environment

variable

A _locale_ is a set of information addressing linguistic and cultural requirements that
corresponds to a given language and country. Setting the NLS_LANG environment variable in your client's
environment is the simplest way to specify locale behavior for Oracle. This variable sets the language and
territory used by the client application and the database server. It also indicates the client's character set,
which corresponds to the character set for data entered or displayed by a client application. For more
information on NLS_LANG and character sets, see [What is a character set or code page?](http://www.oracle.com/technetwork/database/database-technologies/globalization/nls-lang-099431.html#_Toc110410570 "http://www.oracle.com/technetwork/database/database-technologies/globalization/nls-lang-099431.html#_Toc110410570") in the Oracle documentation.

### NLS initialization

parameters

You can also set the following National Language Support (NLS) initialization parameters at the instance
level for an Oracle DB instance in Amazon RDS:

- NLS_COMP
- NLS_DATE_FORMAT
- NLS_LENGTH_SEMANTICS
- NLS_NCHAR_CONV_EXCP
- NLS_SORT
- NLS_TIME_FORMAT
- NLS_TIME_TZ_FORMAT
- NLS_TIMESTAMP_FORMAT
- NLS_TIMESTAMP_TZ_FORMAT

For information about modifying instance parameters, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

You can set other NLS initialization parameters in your SQL client. For example, the following statement
sets the NLS_LANGUAGE initialization parameter to GERMAN in a SQL client that is connected to an Oracle DB
instance:

```
ALTER SESSION SET NLS_LANGUAGE=GERMAN;
```

For information about connecting to an Oracle DB instance with a SQL client, see [Connecting to your Oracle DB instance](USER_ConnectToOracleInstance.md "USER_ConnectToOracleInstance.md").

## National character

set

The national character set is used in the `NCHAR`, `NVARCHAR2`, and
`NCLOB` data types. The national character set is typically referred to
as the _NCHAR character set_. Unlike the DB character set, the
NCHAR character set doesn't affect database metadata.

The NCHAR character set supports the following character sets:

- AL16UTF16 (default)
- UTF8

You can specify either value with the `--nchar-character-set-name` parameter of the [create-db-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html") command (AWS CLI version 2 only). If you use the Amazon RDS API, specify the
`NcharCharacterSetName` parameter of [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") operation. You can't change the national character set after you create the
database.

For more information about Unicode in Oracle databases, see [Supporting multilingual databases with unicode](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/supporting-multilingual-databases-with-unicode.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/supporting-multilingual-databases-with-unicode.html") in the Oracle
documentation.
