# Managing collations and

character sets for Amazon RDS for Microsoft SQL Server

This topic provide guidance on how to manage collations and character sets for Microsoft SQL
Server in Amazon RDS. It explains how to configure collations during database creation and
modify them later, ensuring proper handling of text data based on language and locale
requirements. Additionally, it covers best practices for maintaining compatibility and
performance in SQL Server environments in Amazon RDS.

SQL Server supports collations at multiple levels. You set the default server collation
when you create the DB instance. You can override the collation in the database, table, or
column level.

###### Topics

- [Server-level collation for Microsoft SQL Server](#Appendix.SQLServer.CommonDBATasks.Collation.Server "#Appendix.SQLServer.CommonDBATasks.Collation.Server")
- [Database-level collation for Microsoft SQL Server](#Appendix.SQLServer.CommonDBATasks.Collation.Database-Table-Column "#Appendix.SQLServer.CommonDBATasks.Collation.Database-Table-Column")

## Server-level collation for Microsoft SQL Server

When you create a Microsoft SQL Server DB instance, you can set the server collation that you want to use. If you don't choose a
different collation, the server-level collation defaults to SQL_Latin1_General_CP1_CI_AS. The server collation is applied by
default to all databases and database objects.

###### Note

You can't change the collation when you restore from a DB snapshot.

Currently, Amazon RDS supports the following server collations:

| Collation                                  | Description                                                                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arabic_CI_AS                               | Arabic, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                   |
| Chinese_PRC_BIN2                           | Chinese-PRC, binary code point sort order                                                                                                                                             |
| Chinese_PRC_CI_AS                          | Chinese-PRC, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                              |
| Chinese_Taiwan_Stroke_CI_AS                | Chinese-Taiwan-Stroke, case-insensitive, accent-sensitive, kanatype-insensitive,<br>width-insensitive                                                                                 |
| Danish_Norwegian_CI_AS                     | Danish-Norwegian, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                         |
| Danish_Norwegian_CI_AS_KS                  | Danish-Norwegian, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive                                                                                           |
| Danish_Norwegian_CI_AS_KS_WS               | Danish-Norwegian, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive                                                                                             |
| Danish_Norwegian_CI_AS_WS                  | Danish-Norwegian, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive                                                                                           |
| Danish_Norwegian_CS_AI                     | Danish-Norwegian, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive                                                                                         |
| Danish_Norwegian_CS_AI_KS                  | Danish-Norwegian, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive                                                                                           |
| Finnish_Swedish_100_BIN                    | Finnish-Swedish-100, binary sort                                                                                                                                                      |
| Finnish_Swedish_100_BIN2                   | Finnish-Swedish-100, binary code point comparison sort                                                                                                                                |
| Finnish_Swedish_100_CI_AI                  | Finnish-Swedish-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive                                                                                    |
| Finnish_Swedish_100_CI_AS                  | Finnish-Swedish-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                      |
| Finnish_Swedish_CI_AS                      | Finnish, Swedish, and Swedish (Finland), case-insensitive, accent-sensitive, kanatype-insensitive,<br>width-insensitive                                                               |
| French_CI_AS                               | French, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                   |
| Greek_CI_AS                                | Greek, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                    |
| Greek_CS_AS                                | Greek, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                      |
| Hebrew_BIN                                 | Hebrew, binary sort                                                                                                                                                                   |
| Hebrew_CI_AS                               | Hebrew, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                   |
| Japanese_BIN                               | Japanese, binary sort                                                                                                                                                                 |
| Japanese_CI_AS                             | Japanese, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                 |
| Japanese_CS_AS                             | Japanese, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                   |
| Japanese_XJIS_140_CI_AS                    | Japanese, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive                                       |
| Japanese_XJIS_140_CI_AS_KS_VSS             | Japanese, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive                                           |
| Japanese_XJIS_140_CI_AS_VSS                | Japanese, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive                                         |
| Japanese_XJIS_140_CS_AS_KS_WS              | Japanese, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive                                             |
| Korean_Wansung_CI_AS                       | Korean-Wansung, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                           |
| Latin1_General_100_BIN                     | Latin1-General-100, binary sort                                                                                                                                                       |
| Latin1_General_100_BIN2                    | Latin1-General-100, binary code point sort order                                                                                                                                      |
| Latin1_General_100_BIN2_UTF8               | Latin1-General-100, binary code point sort order, UTF-8 encoded                                                                                                                       |
| Latin1_General_100_CI_AS                   | Latin1-General-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                       |
| Latin1_General_100_CI_AS_SC_UTF8           | Latin1-General-100, case-insensitive, accent-sensitive, supplementary characters, UTF-8 encoded                                                                                       |
| Latin1_General_BIN                         | Latin1-General, binary sort                                                                                                                                                           |
| Latin1_General_BIN2                        | Latin1-General, binary code point sort order                                                                                                                                          |
| Latin1_General_CI_AI                       | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive                                                                                         |
| Latin1_General_CI_AS                       | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                           |
| Latin1_General_CI_AS_KS                    | Latin1-General, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive                                                                                             |
| Latin1_General_CS_AS                       | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                             |
| Modern_Spanish_CI_AS                       | Modern-Spanish, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                           |
| Polish_CI_AS                               | Polish, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                   |
| SQL_1xCompat_CP850_CI_AS                   | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 49 on Code Page 850 for non-Unicode Data       |
| SQL_Latin1_General_CP1_CI_AI               | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 54 on Code Page 1252 for non-Unicode Data    |
| **SQL_Latin1_General_CP1_CI_AS (default)** | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 52 on Code Page 1252 for non-Unicode Data      |
| SQL_Latin1_General_CP1_CS_AS               | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode<br>Data, SQL Server Sort Order 51 on Code Page 1252 for non-Unicode Data        |
| SQL_Latin1_General_CP437_CI_AI             | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 34 on Code Page 437 for non-Unicode Data     |
| SQL_Latin1_General_CP850_BIN               | Latin1-General, binary sort order for Unicode Data, SQL Server Sort Order 40 on Code Page 850 for non-Unicode Data                                                                    |
| SQL_Latin1_General_CP850_BIN2              | Latin1-General, binary code point sort order for Unicode Data, SQL Server Sort Order 40 on<br>Code Page 850 for non-Unicode Data                                                      |
| SQL_Latin1_General_CP850_CI_AI             | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 44 on Code Page 850 for non-Unicode Data        |
| SQL_Latin1_General_CP850_CI_AS             | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 42 on Code Page 850 for non-Unicode Data       |
| SQL_Latin1_General_Pref_CP850_CI_AS        | Latin1-General-Pref, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 183 on Code Page 850 for non-Unicode Data |
| SQL_Latin1_General_CP1256_CI_AS            | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 146 on Code Page 1256 for non-Unicode Data     |
| SQL_Latin1_General_CP1255_CS_AS            | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for<br>Unicode Data, SQL Server Sort Order 137 on Code Page 1255 for non-Unicode Data       |
| Thai_CI_AS                                 | Thai, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                     |
| Turkish_CI_AS                              | Turkish, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive                                                                                                  |

You can also retrieve the list of supported collations programmatically using the AWS CLI:

```
aws rds describe-db-engine-versions --engine sqlserver-ee --list-supported-character-sets --query 'DBEngineVersions[].SupportedCharacterSets[].CharacterSetName' | sort -u
```

To choose the collation:

- If you're using the Amazon RDS console, when creating a new DB instance choose
  **Additional configuration**, then enter the collation in the **Collation** field. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- If you're using the AWS CLI, use the `--character-set-name` option with the
  `create-db-instance` command. For more information, see
  [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md").
- If you're using the Amazon RDS API, use the `CharacterSetName` parameter with the
  `CreateDBInstance` operation. For more information, see
  [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md").

## Database-level collation for Microsoft SQL Server

You can change the default collation at the database, table, or column level by overriding
the collation when creating a new database or database object. For example, if your default
server collation is SQL_Latin1_General_CP1_CI_AS, you can change it to Mohawk_100_CI_AS for
Mohawk collation support. Even arguments in a query can be type-cast to use a different
collation if necessary.

For example, the following query would change the default collation for the AccountName
column to Mohawk_100_CI_AS

```
CREATE TABLE [dbo].[Account]
	(
	    [AccountID] [nvarchar](10) NOT NULL,
	    [AccountName] [nvarchar](100) COLLATE Mohawk_100_CI_AS NOT NULL
	) ON [PRIMARY];
```

The Microsoft SQL Server DB engine supports Unicode by the built-in NCHAR, NVARCHAR,
and NTEXT data types. For example, if you need CJK support, use these Unicode data types
for character storage and override the default server collation when creating your
databases and tables. Here are several links from Microsoft covering collation and
Unicode support for SQL Server:

- [Working with collations](http://msdn.microsoft.com/en-us/library/ms187582%28v=sql.105%29.aspx "http://msdn.microsoft.com/en-us/library/ms187582%28v=sql.105%29.aspx")
- [Collation and international terminology](http://msdn.microsoft.com/en-us/library/ms143726%28v=sql.105%29 "http://msdn.microsoft.com/en-us/library/ms143726%28v=sql.105%29")
- [Using
  SQL Server collations](http://msdn.microsoft.com/en-us/library/ms144260%28v=sql.105%29.aspx "http://msdn.microsoft.com/en-us/library/ms144260%28v=sql.105%29.aspx")
- [International considerations for databases and database engine
  applications](http://msdn.microsoft.com/en-us/library/ms190245%28v=sql.105%29.aspx "http://msdn.microsoft.com/en-us/library/ms190245%28v=sql.105%29.aspx")
