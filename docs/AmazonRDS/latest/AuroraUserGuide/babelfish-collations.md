

# Understanding Collations in Babelfish for Aurora PostgreSQL
<a name="babelfish-collations"></a>

When you create an Aurora PostgreSQL DB cluster with Babelfish, you choose a collation for your data. A *collation* specifies the sort order and bit patterns that produce the text or characters in a given written human language. A collation includes rules comparing data for a given set of bit patterns. Collation is related to localization. Different locales affect character mapping, sort order, and the like. Collation attributes are reflected in the names of various collations. For information about attributes, see the [Babelfish collation attributes table](#bfish-collation-attributes-table). 

Babelfish maps SQL Server collations to comparable collations provided by Babelfish. Babelfish predefines Unicode collations with culturally sensitive string comparisons and sort orders. Babelfish also provides a way to translate the collations in your SQL Server DB to the closest-matching Babelfish collation. Locale-specific collations are provided for different languages and regions. 

Some collations specify a code page that corresponds to a client-side encoding. Babelfish automatically translates from the server encoding to the client encoding depending on the collation of each output column. 

Babelfish supports the collations listed in the [Babelfish supported collations table](#bfish-collations-table). Babelfish maps SQL Server collations to comparable collations provided by Babelfish. 

Babelfish uses version 153.80 of the International Components for Unicode (ICU) collation library. For more information about ICU collations, see [ Collation](https://unicode-org.github.io/icu/userguide/collation/) in the ICU documentation. To learn more about PostgreSQL and collation, see [Collation Support](https://www.postgresql.org/docs/current/collation.html) in the the PostgreSQL documentation.

**Topics**
+ [DB cluster parameters that control collation and locale](#babelfish-collations.parameters)
+ [Deterministic and nondeterministic collations in Babelfish](#babelfish-collations.deterministic-nondeterministic)
+ [Collations supported at database level in Babelfish](#babelfish-collations.database-level)
+ [Server and object Collations in Babelfish](#babelfish-collations.reference-tables-supported-collations)
+ [Default Collation behavior in Babelfish](#babelfish-collations-default)
+ [Managing collations](collation.managing.md)
+ [Collation limitations and behavior differences](collation.limitations.md)

## DB cluster parameters that control collation and locale
<a name="babelfish-collations.parameters"></a><a name="collation-related-parameters"></a>

The following parameters affect collation behavior. 

**babelfishpg\_tsql.default\_locale**  
This parameter specifies the default locale used by the collation. This parameter is used in combination with attributes listed in the [Babelfish collation attributes table](#bfish-collation-attributes-table) to customize collations for a specific language and region. The default value for this parameter is `en-US`.  
The default locale applies to all Babelfish collation names that start with "BBF" and to all SQL Server collations that are mapped to Babelfish collations. Changing the setting for this parameter on an existing Babelfish DB cluster doesn't affect the locale of existing collations. For the list of collations, see the [Babelfish supported collations table](#bfish-collations-table). 

**babelfishpg\_tsql.server\_collation\_name**  
This parameter specifies the default collation for the server (Aurora PostgreSQL DB cluster instance) and the database. The default value is `sql_latin1_general_cp1_ci_as`. The `server_collation_name` has to be a `CI_AS` collation because in T-SQL, the server collation determines how identifiers are compared.  
When you create your Babelfish DB cluster, you choose the **Collation name** from the selectable list. These include the collations listed in the [Babelfish supported collations table](#bfish-collations-table). Don't modify the `server_collation_name` after the Babelfish database is created.

The settings you choose when you create your Babelfish for Aurora PostgreSQL DB cluster are stored in the DB cluster parameter group associated with the cluster for these parameters and set its collation behavior.

## Deterministic and nondeterministic collations in Babelfish
<a name="babelfish-collations.deterministic-nondeterministic"></a>

Babelfish supports deterministic and nondeterministic collations:
+ A *deterministic collation* evaluates characters that have identical byte sequences as equal. That means that `x` and `X` aren't equal in a deterministic collation. Deterministic collations can be case-sensitive (CS) and accent-sensitive (AS).
+ A *nondeterministic collation* doesn't need an identical match. A nondeterministic collation evaluates `x` and `X` as equal. Nondeterministic collations are case-insensitive (CI) or accent-insensitive (AI), or both.

In the table following, you can find some behavior differences between Babelfish and PostgreSQL when using nondeterministic collations.


| Babelfish | PostgreSQL | 
| --- | --- | 
| Supports the LIKE clause for CI\_AS collations. | Doesn't support the LIKE clause on nondeterministic collations. | 
| Supports the LIKE clause only on the following AI collations from Babelfish version 4.2.0:+ bbf\_unicode\_cp1250\_ci\_ai<br />+ bbf\_unicode\_cp1250\_cs\_ai<br />+ bbf\_unicode\_cp1257\_ci\_ai<br />+ bbf\_unicode\_cp1257\_cs\_ai<br />+ bbf\_unicode\_cp1\_ci\_ai<br />+ bbf\_unicode\_cp1\_cs\_ai<br />+ estonian\_ci\_ai<br />+ finnish\_swedish\_ci\_ai<br />+ french\_ci\_ai<br />+ latin1\_general\_ci\_ai<br />+ latin1\_general\_cs\_ai<br />+ modern\_spanish\_ci\_ai<br />+ polish\_ci\_ai<br />+ sql\_latin1\_general\_cp1\_ci\_ai<br />+ sql\_latin1\_general\_cp1\_cs\_ai<br />+ traditional\_spanish\_ci\_ai | Doesn't support the LIKE clause on nondeterministic collations. | 

For a list of other limitations and behavior differences for Babelfish compared to SQL Server and PostgreSQL, see [Collation limitations and behavior differences](collation.limitations.md). 

Babelfish and SQL Server follow a naming convention for collations that describe the collation attributes, as shown in the table following.<a name="bfish-collation-attributes-table"></a>


| Attribute | Description | 
| --- | --- | 
| AI | Accent-insensitive. | 
| AS | Accent-sensitive. | 
| BIN2 | BIN2 requests data to be sorted in code point order. Unicode code point order is the same character order for UTF-8, UTF-16, and UCS-2 encodings. Code point order is a fast deterministic collation. | 
| CI | Case-insensitive. | 
| CS | Case-sensitive. | 
| PREF | To sort uppercase letters before lowercase letters, use a PREF collation. If comparison is case-insensitive, the uppercase version of a letter sorts before the lowercase version, if there is no other distinction. The ICU library supports uppercase preference with `colCaseFirst=upper`, but not for CI\_AS collations.<br />PREF can be applied only to `CS_AS` deterministic collations. | 

## Collations supported at database level in Babelfish
<a name="babelfish-collations.database-level"></a>

The following collations are supported at database level in Babelfish:
+ bbf\_unicode\_bin2
+ bbf\_unicode\_cp1\_ci\_ai
+ bbf\_unicode\_cp1\_ci\_as
+ bbf\_unicode\_cp1250\_ci\_ai
+ bbf\_unicode\_cp1250\_ci\_as
+ bbf\_unicode\_cp1257\_ci\_ai
+ bbf\_unicode\_cp1257\_ci\_as
+ estonian\_ci\_ai
+ estonian\_ci\_as
+ finnish\_swedish\_ci\_ai
+ finnish\_swedish\_ci\_as
+ french\_ci\_ai
+ french\_ci\_as
+ latin1\_general\_bin2
+ latin1\_general\_ci\_ai
+ latin1\_general\_ci\_as
+ latin1\_general\_90\_bin2
+ latin1\_general\_100\_bin2
+ latin1\_general\_140\_bin2
+ modern\_spanish\_ci\_ai
+ modern\_spanish\_ci\_as
+ polish\_ci\_ai
+ polish\_ci\_as
+ sql\_latin1\_general\_cp1\_ci\_ai
+ sql\_latin1\_general\_cp1\_ci\_as
+ sql\_latin1\_general\_cp1250\_ci\_as
+ sql\_latin1\_general\_cp1251\_ci\_as
+ sql\_latin1\_general\_cp1257\_ci\_as
+ traditional\_spanish\_ci\_ai
+ traditional\_spanish\_ci\_as

**Note**  
To use a different collation at the database level, ensure it matches the server-level collation. For more information, see [Server and object Collations in Babelfish](#babelfish-collations.reference-tables-supported-collations)

## Server and object Collations in Babelfish
<a name="babelfish-collations.reference-tables-supported-collations"></a>

Use the following collations as a server collation or an object collation.<a name="bfish-collations-table"></a>


| Collation ID | Notes | 
| --- | --- | 
| bbf\_unicode\_general\_ci\_as | Supports case-insensitive comparison and the LIKE operator. | 
| bbf\_unicode\_cp1\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1252.txt) also known as CP1252. | 
| bbf\_unicode\_CP1250\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1250.txt) used to represent texts in Central European and Eastern European languages that use Latin script. | 
| bbf\_unicode\_CP1251\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1251.txt) for languages that use the Cyrillic script. | 
| bbf\_unicode\_cp1253\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1253.txt) used to represent modern Greek. | 
| bbf\_unicode\_cp1254\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1254.txt) that supports Turkish. | 
| bbf\_unicode\_cp1255\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1255.txt) that supports Hebrew. | 
| bbf\_unicode\_cp1256\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1256.txt) used to write languages that use Arabic script. | 
| bbf\_unicode\_cp1257\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1257.txt) used to support Estonian, Latvian, and Lithuanian languages. | 
| bbf\_unicode\_cp1258\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1258.txt) used to write Vietnamese characters. | 
| bbf\_unicode\_cp874\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit874.txt) used to write Thai characters. | 
| sql\_latin1\_general\_cp1250\_ci\_as | [Nondeterministic single-byte character encoding](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1250.txt) used to represent Latin characters. | 
| sql\_latin1\_general\_cp1251\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1251.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1252.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1253\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1253.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1254\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1254.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1255\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1255.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1256\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1256.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1257\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1257.txt) that supports Latin characters. | 
| sql\_latin1\_general\_cp1258\_ci\_as | [Nondeterministic collation](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1258.txt) that supports Latin characters. | 
| chinese\_prc\_ci\_as | Nondeterministic collation that supports Chinese (PRC). | 
| cyrillic\_general\_ci\_as | Nondeterministic collation that supports Cyrillic. | 
| finnish\_swedish\_ci\_as | Nondeterministic collation that supports Finnish. | 
| french\_ci\_as | Nondeterministic collation that supports French. | 
| japanese\_ci\_as | Nondeterministic collation that supports Japanese. Supported in Babelfish 2.1.0 and higher releases. | 
| korean\_wansung\_ci\_as | Nondeterministic collation that supports Korean (with dictionary sort). | 
| latin1\_general\_ci\_as | Nondeterministic collation that supports Latin characters. | 
| modern\_spanish\_ci\_as | Nondeterministic collation that supports Modern Spanish. | 
| polish\_ci\_as | Nondeterministic collation that supports Polish. | 
| thai\_ci\_as | Nondeterministic collation that supports Thai. | 
| traditional\_spanish\_ci\_as | Nondeterministic collation that supports Spanish (traditional sort). | 
| turkish\_ci\_as | Nondeterministic collation that supports Turkish. | 
| ukrainian\_ci\_as | Nondeterministic collation that supports Ukrainian. | 
| vietnamese\_ci\_as | Nondeterministic collation that supports Vietnamese. | 

You can use the following collations as object collations.<a name="bfish-icu-collations-table"></a>


| Dialect | Deterministic options | Nondeterministic options | 
| --- | --- | --- | 
| Arabic | Arabic\_CS\_AS | Arabic\_CI\_AS<br />Arabic\_CI\_AI | 
| Arabic script | BBF\_Unicode\_CP1256\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1256\_CS\_AS | BBF\_Unicode\_CP1256\_CI\_AI<br />BBF\_Unicode\_CP1256\_CS\_AI | 
| Binary | latin1\_general\_bin2<br />BBF\_Unicode\_BIN2 | – | 
| Central European and Eastern European languages that use Latin script | BBF\_Unicode\_CP1250\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1250\_CS\_AS | BBF\_Unicode\_CP1250\_CI\_AI<br />BBF\_Unicode\_CP1250\_CS\_AI | 
| Chinese | Chinese\_PRC\_CS\_AS | Chinese\_PRC\_CI\_AS<br />Chinese\_PRC\_CI\_AI | 
| Cyrillic\_General | Cyrillic\_General\_CS\_AS | Cyrillic\_General\_CI\_AS<br />Cyrillic\_General\_CI\_AI | 
| Cyrillic script | BBF\_Unicode\_CP1251\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1251\_CS\_AS | BBF\_Unicode\_CP1251\_CI\_AI<br />BBF\_Unicode\_CP1251\_CS\_AI | 
| Estonian | Estonian\_CS\_AS | Estonian\_CI\_AS<br />Estonian\_CI\_AI | 
| Estonian, Latvian, and Lithuanian | BBF\_Unicode\_CP1257\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1257\_CS\_AS | BBF\_Unicode\_CP1257\_CI\_AI<br />BBF\_Unicode\_CP1257\_CS\_AI | 
| Finnish\_Swedish | Finnish\_Swedish\_CS\_AS | Finnish\_Swedish\_CI\_AS<br />Finnish\_Swedish\_CI\_AI | 
| French | French\_CS\_AS | French\_CI\_AS<br />French\_CI\_AI | 
| Greek | Greek\_CS\_AS | Greek\_CI\_AS<br />Greek\_CI\_AI | 
| Hebrew | BBF\_Unicode\_CP1255\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1255\_CS\_AS<br />Hebrew\_CS\_AS | BBF\_Unicode\_CP1255\_CI\_AI<br />BBF\_Unicode\_CP1255\_CS\_AI<br />Hebrew\_CI\_AS<br />Hebrew\_CI\_AI | 
| Japanese (Babelfish 2.1.0 and higher) | Japanese\_CS\_AS | Japanese\_CI\_AI<br />Japanese\_CI\_AS | 
| Korean\_Wamsung | Korean\_Wamsung\_CS\_AS | Korean\_Wamsung\_CI\_AS<br />Korean\_Wamsung\_CI\_AI | 
| Latin characters for code page CP1252 | latin1\_general\_cs\_as<br />BBF\_Unicode\_General\_CS\_AS<br />BBF\_Unicode\_General\_Pref\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1\_CS\_AS<br />BBF\_Unicode\_CP1\_CS\_AS | latin1\_general\_ci\_as<br />latin1\_general\_ci\_ai<br />latin1\_general\_cs\_ai<br />BBF\_Unicode\_General\_CI\_AI<br />BBF\_Unicode\_General\_CS\_AI<br />BBF\_Unicode\_CP1\_CI\_AI<br />BBF\_Unicode\_CP1\_CS\_AI | 
| Modern Greek | BBF\_Unicode\_CP1253\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1253\_CS\_AS | BBF\_Unicode\_CP1253\_CI\_AI<br />BBF\_Unicode\_CP1253\_CS\_AI | 
| Modern\_Spanish | Modern\_Spanish\_CS\_AS | Modern\_Spanish\_CI\_AS<br />Modern\_Spanish\_CI\_AI | 
| Mongolian | Mongolian\_CS\_AS | Mongolian\_CI\_AS<br />Mongolian\_CI\_AI | 
| Polish | Polish\_CS\_AS | Polish\_CI\_AS<br />Polish\_CI\_AI | 
| Thai | BBF\_Unicode\_CP874\_CS\_AS<br />BBF\_Unicode\_Pref\_CP874\_CS\_AS<br />Thai\_CS\_AS | BBF\_Unicode\_CP874\_CI\_AI<br />BBF\_Unicode\_CP874\_CS\_AI<br />Thai\_CI\_AS, Thai\_CI\_AI | 
| Traditional\_Spanish | Traditional\_Spanish\_CS\_AS | Traditional\_Spanish\_CI\_AS<br />Traditional\_Spanish\_CI\_AI | 
| Turkish | BBF\_Unicode\_CP1254\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1254\_CS\_AS<br />Turkish\_CS\_AS | BBF\_Unicode\_CP1254\_CI\_AI<br />BBF\_Unicode\_CP1254\_CS\_AI<br />Turkish\_CI\_AS, Turkish\_CI\_AI | 
| Ukranian | Ukranian\_CS\_AS | Ukranian\_CI\_AS<br />Ukranian\_CI\_AI | 
| Vietnamese | BBF\_Unicode\_CP1258\_CS\_AS<br />BBF\_Unicode\_Pref\_CP1258\_CS\_AS<br />Vietnamese\_CS\_AS | BBF\_Unicode\_CP1258\_CI\_AI<br />BBF\_Unicode\_CP1258\_CS\_AI<br />Vietnamese\_CI\_AS<br />Vietnamese\_CI\_AI | 

## Default Collation behavior in Babelfish
<a name="babelfish-collations-default"></a>

Earlier, the default collation of the collatable datatypes was `pg_catalog.default`. The datatypes and the objects that depends on these datatypes follows cases-sensitive collation. This condition potentially impacts the T-SQL objects of the data set with case-insensitive collation. Starting with Babelfish 2.3.0, the default collation for the collatable data types (except TEXT and NTEXT) is the same as the collation in the `babelfishpg_tsql.server_collation_name` parameter. When you upgrade to Babelfish 2.3.0, the default collation is picked automatically at the time of DB cluster creation, which doesn't create any visible impact. 