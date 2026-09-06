

# Setting character sets and collations for RDS Custom for SQL Server DB instances
<a name="custom-reqs-limits-MS.collation"></a>

## Overview
<a name="custom-reqs-limits-MS.collation.overview"></a>

With RDS Custom for SQL Server DB instances, you can configure the character set and collation settings that determine how data is stored and sorted. Character sets define which characters are allowed, while collations specify the rules for sorting and comparing data. It't important to set the appropriate character sets and collations for applications that work with multilingual data or have specific sorting requirements. For example, you might need to handle accented characters and define language-specific sorting rules, or maintain data integrity across different locales. The following sections provide information on character set and collation support for your RDS Custom for SQL Server DB instances.

RDS Custom for SQL Server supports a wide range of server collations, both in traditional and UTF-8 encoding, for the SQL\_Latin, Japanese, German, and Arabic locales. The default server collation is `SQL_Latin1_General_CP1_CI_AS`, however, you can select another supported collation to use. You can select a collation using the same procedure that RDS for SQL Server uses. For more information, see [Managing collations and character sets for Amazon RDS for Microsoft SQL Server](Appendix.SQLServer.CommonDBATasks.Collation.md).

## Considerations
<a name="custom-reqs-limits-MS.collation.considerations"></a>

The following requirements and limitations apply when working with server collations on RDS Custom for SQL Server:
+ You can set the server collation when you create an RDS Custom for SQL Server DB instance. You can't modify the server-level collation after the DB instance is created.
+ You can't modify the server level collation when restoring from a DB snapshot or during a point in time recovery (PITR).
+ When you create a DB instance from an RDS Custom for SQL Server CEV, the DB instance doesn't inherit the server collation from the CEV. Instead, the default server collation of `SQL_Latin1_General_CP1_CI_AS` is used. If you've configured a non-default server collation on a RDS Custom for SQL Server CEV and want to use that same server collation on a new DB instance, be sure to select that same collation when you create the DB instance from the CEV.
**Note**  
If the collation you select while creating the DB instance is different from the collation of the CEV, the Microsoft SQL Server system databases on the new RDS Custom for SQL Server DB instance will be rebuilt to use the updated collation. The rebuild process is only performed on the new RDS Custom for SQL Server DB instance and has no impact on the CEV itself. Any previous modifications that you made to the system databases on the CEV will not be retained on the new RDS Custom for SQL Server DB instance once the system databases are rebuilt. Examples of some modifications include user-defined objects in the `master` database, scheduled jobs in the `msdb` database, or changes to default database settings in the `model` database on your CEV. You can manually recreate your modifications once the new RDS Custom for SQL Server DB instance is created. 
+ When you create a DB instance from an RDS Custom for SQL Server custom engine version (CEV) and select a different collation from that of the CEV, ensure that your golden image (AMI) used for CEV creation meets the following requirements so the Microsoft SQL Server system databases on the new DB instance can be rebuilt:
  + For SQL Server 2022, ensure the `setup.exe` file is located in the following path: `C:\Program Files\Microsoft SQL Server\160\Setup Bootstrap\SQL2022\setup.exe`
  + For SQL Server 2019, ensure the `setup.exe` file is located in the following path: `C:\Program Files\Microsoft SQL Server\150\Setup Bootstrap\SQL2019\setup.exe`
  + Copies of the data and log templates for the `master`, `model`, and `msdb` databases must exist in their default locations. For more information, see [Rebuild system databases](https://learn.microsoft.com/en-us/sql/relational-databases/databases/rebuild-system-databases?view=sql-server-ver16#Restrictions         ) in the Microsoft public documentation.
  + Ensure your SQL Server Database Engine uses `NT Service\MSSQLSERVER `or `NT AUTHORITY\NETWORK SERVICE` as the service account. Any other account will not have the required permissions on the `C:\` drive when configuring a non-default server collation for the DB instance.
+ If the server collation selected for a new DB instance is the same as that configured on your CEV, the Microsoft SQL Server system databases on the new RDS Custom for SQL Server DB instance do not undergo the rebuild process. Any previous modifications that you made to the system databases on the CEV will automatically persist to the new RDS Custom for SQL Server DB instance. 

## Supported collations
<a name="custom-reqs-limits-MS.collation.supportedCollations"></a>

You can set your collation to one of the values listed in the following table.


| Collation | Description | 
| --- |--- |
| Arabic\_100\_BIN | Arabic-100, binary sort | 
| Arabic\_100\_BIN2 | Arabic-100, binary code point comparison sort | 
| Arabic\_100\_CI\_AI | Arabic-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_100\_CI\_AI\_KS | Arabic-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_100\_CI\_AI\_KS\_SC | Arabic-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CI\_AI\_KS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AI\_KS\_WS | Arabic-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_100\_CI\_AI\_KS\_WS\_SC | Arabic-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CI\_AI\_KS\_WS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AI\_SC | Arabic-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CI\_AI\_SC\_UTF8 | Arabic-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AI\_WS | Arabic-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_100\_CI\_AI\_WS\_SC | Arabic-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CI\_AI\_WS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AS | Arabic-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_100\_CI\_AS\_KS | Arabic-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_100\_CI\_AS\_KS\_SC | Arabic-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CI\_AS\_KS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AS\_KS\_WS | Arabic-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_100\_CI\_AS\_KS\_WS\_SC | Arabic-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CI\_AS\_KS\_WS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AS\_SC | Arabic-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CI\_AS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CI\_AS\_WS | Arabic-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_100\_CI\_AS\_WS\_SC | Arabic-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CI\_AS\_WS\_SC\_UTF8 | Arabic-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AI | Arabic-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_100\_CS\_AI\_KS | Arabic-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_100\_CS\_AI\_KS\_SC | Arabic-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CS\_AI\_KS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AI\_KS\_WS | Arabic-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_100\_CS\_AI\_KS\_WS\_SC | Arabic-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CS\_AI\_KS\_WS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AI\_SC | Arabic-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CS\_AI\_SC\_UTF8 | Arabic-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AI\_WS | Arabic-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_100\_CS\_AI\_WS\_SC | Arabic-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CS\_AI\_WS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AS | Arabic-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_100\_CS\_AS\_KS | Arabic-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_100\_CS\_AS\_KS\_SC | Arabic-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CS\_AS\_KS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AS\_KS\_WS | Arabic-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_100\_CS\_AS\_KS\_WS\_SC | Arabic-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CS\_AS\_KS\_WS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AS\_SC | Arabic-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Arabic\_100\_CS\_AS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Arabic\_100\_CS\_AS\_WS | Arabic-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_100\_CS\_AS\_WS\_SC | Arabic-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Arabic\_100\_CS\_AS\_WS\_SC\_UTF8 | Arabic-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Arabic\_BIN | Arabic, binary sort | 
| Arabic\_BIN2 | Arabic, binary code point comparison sort | 
| Arabic\_CI\_AI | Arabic, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_CI\_AI\_KS | Arabic, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_CI\_AI\_KS\_WS | Arabic, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_CI\_AI\_WS | Arabic, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_CI\_AS | Arabic, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_CI\_AS\_KS | Arabic, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_CI\_AS\_KS\_WS | Arabic, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_CI\_AS\_WS | Arabic, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_CS\_AI | Arabic, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_CS\_AI\_KS | Arabic, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_CS\_AI\_KS\_WS | Arabic, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_CS\_AI\_WS | Arabic, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Arabic\_CS\_AS | Arabic, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Arabic\_CS\_AS\_KS | Arabic, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Arabic\_CS\_AS\_KS\_WS | Arabic, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Arabic\_CS\_AS\_WS | Arabic, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Chinese\_PRC\_BIN2 | Chinese-PRC, binary code point comparison sort | 
| Chinese\_PRC\_CI\_AS | Chinese-PRC, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Chinese\_Taiwan\_Stroke\_CI\_AS | Chinese-Taiwan-Stroke, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Danish\_Norwegian\_CI\_AS | Danish-Norwegian, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Finnish\_Swedish\_CI\_AS | Finnish-Swedish, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| French\_CI\_AS | French, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_100\_BIN | German-PhoneBook-100, binary sort | 
| German\_PhoneBook\_100\_BIN2 | German-PhoneBook-100, binary code point comparison sort | 
| German\_PhoneBook\_100\_CI\_AI | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_100\_CI\_AI\_KS | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_100\_CI\_AI\_KS\_SC | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AI\_KS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AI\_KS\_WS | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_100\_CI\_AI\_KS\_WS\_SC | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AI\_KS\_WS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AI\_SC | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AI\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AI\_WS | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| German\_PhoneBook\_100\_CI\_AI\_WS\_SC | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AI\_WS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AS | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_100\_CI\_AS\_KS | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_100\_CI\_AS\_KS\_SC | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AS\_KS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AS\_KS\_WS | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_100\_CI\_AS\_KS\_WS\_SC | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AS\_KS\_WS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AS\_SC | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CI\_AS\_WS | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| German\_PhoneBook\_100\_CI\_AS\_WS\_SC | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CI\_AS\_WS\_SC\_UTF8 | German-PhoneBook-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CS\_AI | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_100\_CS\_AI\_KS | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_100\_CS\_AI\_KS\_SC | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CS\_AI\_KS\_SC\_UTF8 | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CS\_AI\_KS\_WS | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_100\_CS\_AI\_KS\_WS\_SC | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CS\_AI\_KS\_WS\_SC\_UTF8 | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CS\_AI\_SC | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CS\_AI\_SC\_UTF8 | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CS\_AI\_WS | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| German\_PhoneBook\_100\_CS\_AI\_WS\_SC | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CS\_AI\_WS\_SC\_UTF8 | German-PhoneBook-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CS\_AS | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_100\_CS\_AS\_KS | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_100\_CS\_AS\_KS\_SC | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| German\_PhoneBook\_100\_CS\_AS\_KS\_SC\_UTF8 | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_100\_CS\_AS\_KS\_WS | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_100\_CS\_AS\_KS\_WS\_SC | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| German\_PhoneBook\_100\_CS\_AS\_KS\_WS\_SC\_UTF8 | German-PhoneBook-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| German\_PhoneBook\_BIN | German-PhoneBook, binary sort | 
| German\_PhoneBook\_BIN2 | German-PhoneBook, binary code point comparison sort | 
| German\_PhoneBook\_CI\_AI | German-PhoneBook, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_CI\_AI\_KS | German-PhoneBook, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_CI\_AI\_KS\_WS | German-PhoneBook, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_CI\_AI\_WS | German-PhoneBook, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| German\_PhoneBook\_CI\_AS | German-PhoneBook, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_CI\_AS\_KS | German-PhoneBook, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_CI\_AS\_KS\_WS | German-PhoneBook, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_CI\_AS\_WS | German-PhoneBook, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| German\_PhoneBook\_CS\_AI | German-PhoneBook, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_CS\_AI\_KS | German-PhoneBook, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_CS\_AI\_KS\_WS | German-PhoneBook, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_CS\_AI\_WS | German-PhoneBook, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| German\_PhoneBook\_CS\_AS | German-PhoneBook, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| German\_PhoneBook\_CS\_AS\_KS | German-PhoneBook, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| German\_PhoneBook\_CS\_AS\_KS\_WS | German-PhoneBook, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| German\_PhoneBook\_CS\_AS\_WS | German-PhoneBook, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Hebrew\_BIN | Hebrew, binary sort | 
| Hebrew\_CI\_AS | Hebrew, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_90\_BIN | Japanese-90, binary sort | 
| Japanese\_90\_BIN2 | Japanese-90, binary code point comparison sort | 
| Japanese\_90\_CI\_AI | Japanese-90, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_90\_CI\_AI\_KS | Japanese-90, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_90\_CI\_AI\_KS\_SC | Japanese-90, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CI\_AI\_KS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AI\_KS\_WS | Japanese-90, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_90\_CI\_AI\_KS\_WS\_SC | Japanese-90, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CI\_AI\_KS\_WS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AI\_SC | Japanese-90, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CI\_AI\_SC\_UTF8 | Japanese-90, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AI\_WS | Japanese-90, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_90\_CI\_AI\_WS\_SC | Japanese-90, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CI\_AI\_WS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AS | Japanese-90, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_90\_CI\_AS\_KS | Japanese-90, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_90\_CI\_AS\_KS\_SC | Japanese-90, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CI\_AS\_KS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AS\_KS\_WS | Japanese-90, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_90\_CI\_AS\_KS\_WS\_SC | Japanese-90, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CI\_AS\_KS\_WS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AS\_SC | Japanese-90, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CI\_AS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CI\_AS\_WS | Japanese-90, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_90\_CI\_AS\_WS\_SC | Japanese-90, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CI\_AS\_WS\_SC\_UTF8 | Japanese-90, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AI | Japanese-90, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_90\_CS\_AI\_KS | Japanese-90, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_90\_CS\_AI\_KS\_SC | Japanese-90, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CS\_AI\_KS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AI\_KS\_WS | Japanese-90, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_90\_CS\_AI\_KS\_WS\_SC | Japanese-90, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CS\_AI\_KS\_WS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AI\_SC | Japanese-90, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CS\_AI\_SC\_UTF8 | Japanese-90, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AI\_WS | Japanese-90, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_90\_CS\_AI\_WS\_SC | Japanese-90, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CS\_AI\_WS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AS | Japanese-90, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_90\_CS\_AS\_KS | Japanese-90, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_90\_CS\_AS\_KS\_SC | Japanese-90, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CS\_AS\_KS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AS\_KS\_WS | Japanese-90, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_90\_CS\_AS\_KS\_WS\_SC | Japanese-90, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CS\_AS\_KS\_WS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AS\_SC | Japanese-90, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_90\_CS\_AS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_90\_CS\_AS\_WS | Japanese-90, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_90\_CS\_AS\_WS\_SC | Japanese-90, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_90\_CS\_AS\_WS\_SC\_UTF8 | Japanese-90, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_BIN | Japanese, binary sort | 
| Japanese\_BIN2 | Japanese, binary code point comparison sort | 
| Japanese\_Bushu\_Kakusu\_100\_BIN | Japanese-Bushu-Kakusu-100, binary sort | 
| Japanese\_Bushu\_Kakusu\_100\_BIN2 | Japanese-Bushu-Kakusu-100, binary code point comparison sort | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_KS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_KS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_KS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_KS\_WS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_KS\_WS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_KS\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_WS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_WS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AI\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_KS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_KS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_KS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_KS\_WS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_KS\_WS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_KS\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_WS | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_WS\_SC | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CI\_AS\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_KS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_KS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_KS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_KS\_WS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_KS\_WS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_KS\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_WS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_WS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AI\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_KS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_KS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_KS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_KS\_WS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_KS\_WS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_KS\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_WS | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_WS\_SC | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_Bushu\_Kakusu\_100\_CS\_AS\_WS\_SC\_UTF8 | Japanese-Bushu-Kakusu-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_BIN | Japanese-Bushu-Kakusu-140, binary sort | 
| Japanese\_Bushu\_Kakusu\_140\_BIN2 | Japanese-Bushu-Kakusu-140, binary code point comparison sort | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_WS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplement ary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_KS\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_WS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AI\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_WS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_KS\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_WS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CI\_AS\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_WS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_KS\_WS\_VSS\_UTF8 | Japanese-Bushu-Kaku su-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_WS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AI\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_WS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_KS\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_WS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_WS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_WS\_VSS | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_Bushu\_Kakusu\_140\_CS\_AS\_WS\_VSS\_UTF8 | Japanese-Bushu-Kakusu-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_CI\_AI | Japanese, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_CI\_AI\_KS | Japanese, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_CI\_AI\_KS\_WS | Japanese, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_CI\_AI\_WS | Japanese, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_CI\_AS | Japanese, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_CI\_AS\_KS | Japanese, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_CI\_AS\_KS\_WS | Japanese, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_CI\_AS\_WS | Japanese, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_CS\_AI | Japanese, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_CS\_AI\_KS | Japanese, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_CS\_AI\_KS\_WS | Japanese, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_CS\_AI\_WS | Japanese, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_CS\_AS | Japanese, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_CS\_AS\_KS | Japanese, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_CS\_AS\_KS\_WS | Japanese, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_CS\_AS\_WS | Japanese, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Unicode\_BIN | Japanese-Unicode, binary sort | 
| Japanese\_Unicode\_BIN2 | Japanese-Unicode, binary code point comparison sort | 
| Japanese\_Unicode\_CI\_AI | Japanese-Unicode, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Unicode\_CI\_AI\_KS | Japanese-Unicode, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Unicode\_CI\_AI\_KS\_WS | Japanese-Unicode, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Unicode\_CI\_AI\_WS | Japanese-Unicode, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Unicode\_CI\_AS | Japanese-Unicode, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Unicode\_CI\_AS\_KS | Japanese-Unicode, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Unicode\_CI\_AS\_KS\_WS | Japanese-Unicode, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Unicode\_CI\_AS\_WS | Japanese-Unicode, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Unicode\_CS\_AI | Japanese-Unicode, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Unicode\_CS\_AI\_KS | Japanese-Unicode, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Unicode\_CS\_AI\_KS\_WS | Japanese-Unicode, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Unicode\_CS\_AI\_WS | Japanese-Unicode, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_Unicode\_CS\_AS | Japanese-Unicode, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_Unicode\_CS\_AS\_KS | Japanese-Unicode, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_Unicode\_CS\_AS\_KS\_WS | Japanese-Unicode, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_Unicode\_CS\_AS\_WS | Japanese-Unicode, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_XJIS\_100\_BIN | Japanese-XJIS-100, binary sort | 
| Japanese\_XJIS\_100\_BIN2 | Japanese-XJIS-100, binary code point comparison sort | 
| Japanese\_XJIS\_100\_CI\_AI | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CI\_AI\_KS | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CI\_AI\_KS\_SC | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AI\_KS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AI\_KS\_WS | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CI\_AI\_KS\_WS\_SC | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AI\_KS\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AI\_SC | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AI\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AI\_WS | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CI\_AI\_WS\_SC | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AI\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AS | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CI\_AS\_KS | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CI\_AS\_KS\_SC | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AS\_KS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AS\_KS\_WS | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CI\_AS\_KS\_WS\_SC | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AS\_KS\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AS\_SC | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CI\_AS\_WS | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CI\_AS\_WS\_SC | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CI\_AS\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AI | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CS\_AI\_KS | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CS\_AI\_KS\_SC | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AI\_KS\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AI\_KS\_WS | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CS\_AI\_KS\_WS\_SC | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AI\_KS\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AI\_SC | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AI\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AI\_WS | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CS\_AI\_WS\_SC | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AI\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AS | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CS\_AS\_KS | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Japanese\_XJIS\_100\_CS\_AS\_KS\_SC | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AS\_KS\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AS\_KS\_WS | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive | 
| Japanese\_XJIS\_100\_CS\_AS\_KS\_WS\_SC | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AS\_KS\_WS\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AS\_SC | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters | 
| Japanese\_XJIS\_100\_CS\_AS\_SC\_UTF8 | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Japanese\_XJIS\_100\_CS\_AS\_WS | Japanese-XJIS-100, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive | 
| Japanese\_XJIS\_140\_BIN | Japanese-XJIS-140, binary sort | 
| Japanese\_XJIS\_140\_BIN2 | Japanese-XJIS-140, binary code point comparison sort | 
| Japanese\_XJIS\_140\_CI\_AI | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_KS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_VSS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_WS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_WS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_WS\_VSS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_KS\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_VSS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_WS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_WS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AI\_WS\_VSS | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AI\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_KS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_VSS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_WS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_WS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_WS\_VSS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_KS\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_VSS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_WS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_WS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CI\_AS\_WS\_VSS | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CI\_AS\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-insensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_KS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_VSS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_WS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_WS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_WS\_VSS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_KS\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_VSS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_WS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_WS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AI\_WS\_VSS | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AI\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-insensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_KS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_VSS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_WS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_WS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_WS\_VSS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_KS\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-sensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_VSS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_WS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_WS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector insensitive, UTF8 | 
| Japanese\_XJIS\_140\_CS\_AS\_WS\_VSS | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive | 
| Japanese\_XJIS\_140\_CS\_AS\_WS\_VSS\_UTF8 | Japanese-XJIS-140, case-sensitive, accent-sensitive, kanatype-insensitive, width-sensitive, supplementary characters, variation selector sensitive, UTF8 | 
| Korean\_Wansung\_CI\_AS | Korean-Wansung, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Latin1\_General\_100\_BIN | Latin1-General-100, binary sort | 
| Latin1\_General\_100\_BIN2 | Latin1-General-100, binary code point comparison sort | 
| Latin1\_General\_100\_BIN2\_UTF8 | Latin1-General-100, binary code point comparison sort, UTF8 | 
| Latin1\_General\_100\_CI\_AS | Latin1-General-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Latin1\_General\_100\_CI\_AS\_SC\_UTF8 | Latin1-General-100, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive, supplementary characters, UTF8 | 
| Latin1\_General\_BIN | Latin1-General, binary sort | 
| Latin1\_General\_BIN2 | Latin1-General, binary code point comparison sort | 
| Latin1\_General\_CI\_AI | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive | 
| Latin1\_General\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Latin1\_General\_CI\_AS\_KS | Latin1-General, case-insensitive, accent-sensitive, kanatype-sensitive, width-insensitive | 
| Latin1\_General\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| Modern\_Spanish\_CI\_AS | Modern-Spanish, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 
| SQL\_1xCompat\_CP850\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 49 on Code Page 850 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1\_CI\_AI | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 54 on Code Page 1252 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 52 on Code Page 1252 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 51 on Code Page 1252 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1250\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 82 on Code Page 1250 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1250\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 81 on Code Page 1250 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1251\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 106 on Code Page 1251 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1251\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 105 on Code Page 1251 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1253\_CI\_AI | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 124 on Code Page 1253 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1253\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 114 on Code Page 1253 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1253\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 113 on Code Page 1253 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1254\_CI\_AS | Turkish, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 130 on Code Page 1254 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1254\_CS\_AS | Turkish, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 129 on Code Page 1254 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1255\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 138 on Code Page 1255 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1255\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 137 on Code Page 1255 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1256\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 146 on Code Page 1256 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1256\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 145 on Code Page 1256 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1257\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 154 on Code Page 1257 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP1257\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 153 on Code Page 1257 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP437\_BIN | Latin1-General, binary sort for Unicode Data, SQL Server Sort Order 30 on Code Page 437 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP437\_BIN2 | Latin1-General, binary code point comparison sort for Unicode Data, SQL Server Sort Order 30 on Code Page 437 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP437\_CI\_AI | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 34 on Code Page 437 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP437\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 32 on Code Page 437 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP437\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 31 on Code Page 437 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP850\_BIN | Latin1-General, binary sort for Unicode Data, SQL Server Sort Order 40 on Code Page 850 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP850\_BIN2 | Latin1-General, binary code point comparison sort for Unicode Data, SQL Server Sort Order 40 on Code Page 850 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP850\_CI\_AI | Latin1-General, case-insensitive, accent-insensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 44 on Code Page 850 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP850\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 42 on Code Page 850 for non-Unicode Data | 
| SQL\_Latin1\_General\_CP850\_CS\_AS | Latin1-General, case-sensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 41 on Code Page 850 for non-Unicode Data | 
| SQL\_Latin1\_General\_Pref\_CP1\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 53 on Code Page 1252 for non-Unicode Data | 
| SQL\_Latin1\_General\_Pref\_CP437\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 33 on Code Page 437 for non-Unicode Data | 
| SQL\_Latin1\_General\_Pref\_CP850\_CI\_AS | Latin1-General, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive for Unicode Data, SQL Server Sort Order 43 on Code Page 850 for non-Unicode Data | 
| Thai\_CI\_AS | Thai, case-insensitive, accent-sensitive, kanatype-insensitive, width-insensitive | 