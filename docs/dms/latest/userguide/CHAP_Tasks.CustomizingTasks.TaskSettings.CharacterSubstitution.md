

# Character substitution task settings
<a name="CHAP_Tasks.CustomizingTasks.TaskSettings.CharacterSubstitution"></a>

You can specify that your replication task perform character substitutions on the target database for all source database columns with the AWS DMS `STRING` or `WSTRING` data type. For information about how to use a task configuration file to set task settings, see [Task settings example](CHAP_Tasks.CustomizingTasks.TaskSettings.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example). 

You can configure character substitution for any task with endpoints from the following source and target databases:
+ Source databases:
  + Oracle
  + Microsoft SQL Server
  + MySQL
  + MariaDB
  + PostgreSQL
  + SAP Adaptive Server Enterprise (ASE)
  + IBM Db2 LUW
+ Target databases:
  + Oracle
  + Microsoft SQL Server
  + MySQL
  + MariaDB
  + PostgreSQL
  + SAP Adaptive Server Enterprise (ASE)
  + Amazon Redshift

You can specify character substitutions using the `CharacterSetSettings` parameter in your task settings. These character substitutions occur for characters specified using the Unicode code point value in hexadecimal notation. You can implement the substitutions in two phases, in the following order if both are specified:

1. **Individual character replacement** – AWS DMS can replace the values of selected characters on the source with specified replacement values of corresponding characters on the target. Use the `CharacterReplacements` array in `CharacterSetSettings` to select all source characters having the Unicode code points you specify. Use this array also to specify the replacement code points for the corresponding characters on the target. 

   To select all characters on the source that have a given code point, set an instance of `SourceCharacterCodePoint` in the `CharacterReplacements` array to that code point. Then specify the replacement code point for all equivalent target characters by setting the corresponding instance of `TargetCharacterCodePoint` in this array. To delete target characters instead of replacing them, set the appropriate instances of `TargetCharacterCodePoint` to zero (0). You can replace or delete as many different values of target characters as you want by specifying additional pairs of `SourceCharacterCodePoint` and `TargetCharacterCodePoint` settings in the `CharacterReplacements` array. If you specify the same value for multiple instances of `SourceCharacterCodePoint`, the value of the last corresponding setting of `TargetCharacterCodePoint` applies on the target.

   For example, suppose that you specify the following values for `CharacterReplacements`.

   ```
   "CharacterSetSettings": {
       "CharacterReplacements": [ {
           "SourceCharacterCodePoint": 62,
           "TargetCharacterCodePoint": 61
           }, {
           "SourceCharacterCodePoint": 42,
           "TargetCharacterCodePoint": 41
           }
       ]
   }
   ```

   In this example, AWS DMS replaces all characters with the source code point hex value 62 on the target by characters with the code point value 61. Also, AWS DMS replaces all characters with the source code point 42 on the target by characters with the code point value 41. In other words, AWS DMS replaces all instances of the letter `'b'`on the target by the letter `'a'`. Similarly, AWS DMS replaces all instances of the letter `'B'` on the target by the letter `'A'`.

1. **Character set validation and replacement** – After any individual character replacements complete, AWS DMS can make sure that all target characters have valid Unicode code points in the single character set that you specify. You use `CharacterSetSupport` in `CharacterSetSettings` to configure this target character verification and modification. To specify the verification character set, set `CharacterSet` in `CharacterSetSupport` to the character set's string value. (The possible values for `CharacterSet` follow.) You can have AWS DMS modify the invalid target characters in one of the following ways:
   + Specify a single replacement Unicode code point for all invalid target characters, regardless of their current code point. To configure this replacement code point, set `ReplaceWithCharacterCodePoint` in `CharacterSetSupport` to the specified value.
   + Configure the deletion of all invalid target characters by setting `ReplaceWithCharacterCodePoint` to zero (0).

   For example, suppose that you specify the following values for `CharacterSetSupport`.

   ```
   "CharacterSetSettings": {
       "CharacterSetSupport": {
           "CharacterSet": "UTF16_PlatformEndian",
           "ReplaceWithCharacterCodePoint": 0
       }
   }
   ```

   In this example, AWS DMS deletes any characters found on the target that are invalid in the `"UTF16_PlatformEndian"` character set. So, any characters specified with the hex value `2FB6` are deleted. This value is invalid because this is a 4-byte Unicode code point and UTF16 character sets accept only characters with 2-byte code points.

**Note**  
The replication task completes all of the specified character substitutions before starting any global or table-level transformations that you specify through table mapping. For more information about table mapping, see [Using table mapping to specify task settings](CHAP_Tasks.CustomizingTasks.TableMapping.md).  
Character substitution doesn't support LOB data types. This includes any datatype that DMS considers to be a LOB data type. For example, the `Extended` datatype in Oracle is considered to be a LOB. For more information about source datatypes, see [Source data types for Oracle](CHAP_Source.Oracle.md#CHAP_Source.Oracle.DataTypes) following. 

The values that AWS DMS supports for `CharacterSet` appear in the table following.


|  |  |  | 
| --- |--- |--- |
| UTF-8 | ibm-860\_P100-1995 | ibm-280\_P100-1995 | 
| UTF-16 | ibm-861\_P100-1995 | ibm-284\_P100-1995 | 
| UTF-16BE | ibm-862\_P100-1995 | ibm-285\_P100-1995 | 
| UTF-16LE | ibm-863\_P100-1995 | ibm-290\_P100-1995 | 
| UTF-32 | ibm-864\_X110-1999 | ibm-297\_P100-1995 | 
| UTF-32BE | ibm-865\_P100-1995 | ibm-420\_X120-1999 | 
| UTF-32LE | ibm-866\_P100-1995 | ibm-424\_P100-1995 | 
| UTF16\_PlatformEndian | ibm-867\_P100-1998 | ibm-500\_P100-1995 | 
| UTF16\_OppositeEndian | ibm-868\_P100-1995 | ibm-803\_P100-1999 | 
| UTF32\_PlatformEndian | ibm-869\_P100-1995 | ibm-838\_P100-1995 | 
| UTF32\_OppositeEndian | ibm-878\_P100-1996 | ibm-870\_P100-1995 | 
| UTF-16BE,version=1 | ibm-901\_P100-1999 | ibm-871\_P100-1995 | 
| UTF-16LE,version=1 | ibm-902\_P100-1999 | ibm-875\_P100-1995 | 
| UTF-16,version=1 | ibm-922\_P100-1999 | ibm-918\_P100-1995 | 
| UTF-16,version=2 | ibm-1168\_P100-2002 | ibm-930\_P120-1999 | 
| UTF-7 | ibm-4909\_P100-1999 | ibm-933\_P110-1995 | 
| IMAP-mailbox-name | ibm-5346\_P100-1998 | ibm-935\_P110-1999 | 
| SCSU | ibm-5347\_P100-1998 | ibm-937\_P110-1999 | 
| BOCU-1 | ibm-5348\_P100-1997 | ibm-939\_P120-1999 | 
| CESU-8 | ibm-5349\_P100-1998 | ibm-1025\_P100-1995 | 
| ISO-8859-1 | ibm-5350\_P100-1998 | ibm-1026\_P100-1995 | 
| US-ASCII | ibm-9447\_P100-2002 | ibm-1047\_P100-1995 | 
| gb18030 | ibm-9448\_X100-2005 | ibm-1097\_P100-1995 | 
| ibm-912\_P100-1995 | ibm-9449\_P100-2002 | ibm-1112\_P100-1995 | 
| ibm-913\_P100-2000 | ibm-5354\_P100-1998 | ibm-1122\_P100-1999 | 
| ibm-914\_P100-1995 | ibm-1250\_P100-1995 | ibm-1123\_P100-1995 | 
| ibm-915\_P100-1995 | ibm-1251\_P100-1995 | ibm-1130\_P100-1997 | 
| ibm-1089\_P100-1995 | ibm-1252\_P100-2000 | ibm-1132\_P100-1998 | 
| ibm-9005\_X110-2007 | ibm-1253\_P100-1995 | ibm-1137\_P100-1999 | 
| ibm-813\_P100-1995 | ibm-1254\_P100-1995 | ibm-4517\_P100-2005 | 
| ibm-5012\_P100-1999 | ibm-1255\_P100-1995 | ibm-1140\_P100-1997 | 
| ibm-916\_P100-1995 | ibm-5351\_P100-1998 | ibm-1141\_P100-1997 | 
| ibm-920\_P100-1995 | ibm-1256\_P110-1997 | ibm-1142\_P100-1997 | 
| iso-8859\_10-1998 | ibm-5352\_P100-1998 | ibm-1143\_P100-1997 | 
| iso-8859\_11-2001 | ibm-1257\_P100-1995 | ibm-1144\_P100-1997 | 
| ibm-921\_P100-1995 | ibm-5353\_P100-1998 | ibm-1145\_P100-1997 | 
| iso-8859\_14-1998 | ibm-1258\_P100-1997 | ibm-1146\_P100-1997 | 
| ibm-923\_P100-1998 | macos-0\_2-10.2 | ibm-1147\_P100-1997 | 
| ibm-942\_P12A-1999 | macos-6\_2-10.4 | ibm-1148\_P100-1997 | 
| ibm-943\_P15A-2003 | macos-7\_3-10.2 | ibm-1149\_P100-1997 | 
| ibm-943\_P130-1999 | macos-29-10.2 | ibm-1153\_P100-1999 | 
| ibm-33722\_P12A\_P12A-2009\_U2 | macos-35-10.2 | ibm-1154\_P100-1999 | 
| ibm-33722\_P120-1999 | ibm-1051\_P100-1995 | ibm-1155\_P100-1999 | 
| ibm-954\_P101-2007 | ibm-1276\_P100-1995 | ibm-1156\_P100-1999 | 
| euc-jp-2007 | ibm-1006\_P100-1995 | ibm-1157\_P100-1999 | 
| ibm-1373\_P100-2002 | ibm-1098\_P100-1995 | ibm-1158\_P100-1999 | 
| windows-950-2000 | ibm-1124\_P100-1996 | ibm-1160\_P100-1999 | 
| ibm-950\_P110-1999 | ibm-1125\_P100-1997 | ibm-1164\_P100-1999 | 
| ibm-1375\_P100-2008 | ibm-1129\_P100-1997 | ibm-1364\_P110-2007 | 
| ibm-5471\_P100-2006 | ibm-1131\_P100-1997 | ibm-1371\_P100-1999 | 
| ibm-1386\_P100-2001 | ibm-1133\_P100-1997 | ibm-1388\_P103-2001 | 
| windows-936-2000 | ISO\_2022,locale=ja,version=0 | ibm-1390\_P110-2003 | 
| ibm-1383\_P110-1999 | ISO\_2022,locale=ja,version=1 | ibm-1399\_P110-2003 | 
| ibm-5478\_P100-1995 | ISO\_2022,locale=ja,version=2 | ibm-5123\_P100-1999 | 
| euc-tw-2014 | ISO\_2022,locale=ja,version=3 | ibm-8482\_P100-1999 | 
| ibm-964\_P110-1999 | ISO\_2022,locale=ja,version=4 | ibm-16684\_P110-2003 | 
| ibm-949\_P110-1999 | ISO\_2022,locale=ko,version=0 | ibm-4899\_P100-1998 | 
| ibm-949\_P11A-1999 | ISO\_2022,locale=ko,version=1 | ibm-4971\_P100-1999 | 
| ibm-970\_P110\_P110-2006\_U2 | ISO\_2022,locale=zh,version=0 | ibm-9067\_X100-2005 | 
| ibm-971\_P100-1995 | ISO\_2022,locale=zh,version=1 | ibm-12712\_P100-1998 | 
| ibm-1363\_P11B-1998 | ISO\_2022,locale=zh,version=2 | ibm-16804\_X110-1999 | 
| ibm-1363\_P110-1997 | HZ | ibm-37\_P100-1995,swaplfnl | 
| windows-949-2000 | x11-compound-text | ibm-1047\_P100-1995,swaplfnl | 
| windows-874-2000 | ISCII,version=0 | ibm-1140\_P100-1997,swaplfnl | 
| ibm-874\_P100-1995 | ISCII,version=1 | ibm-1141\_P100-1997,swaplfnl | 
| ibm-1162\_P100-1999 | ISCII,version=2 | ibm-1142\_P100-1997,swaplfnl | 
| ibm-437\_P100-1995 | ISCII,version=3 | ibm-1143\_P100-1997,swaplfnl | 
| ibm-720\_P100-1997 | ISCII,version=4 | ibm-1144\_P100-1997,swaplfnl | 
| ibm-737\_P100-1997 | ISCII,version=5 | ibm-1145\_P100-1997,swaplfnl | 
| ibm-775\_P100-1996 | ISCII,version=6 | ibm-1146\_P100-1997,swaplfnl | 
| ibm-850\_P100-1995 | ISCII,version=7 | ibm-1147\_P100-1997,swaplfnl | 
| ibm-851\_P100-1995 | ISCII,version=8 | ibm-1148\_P100-1997,swaplfnl | 
| ibm-852\_P100-1995 | LMBCS-1 | ibm-1149\_P100-1997,swaplfnl | 
| ibm-855\_P100-1995 | ibm-37\_P100-1995 | ibm-1153\_P100-1999,swaplfnl | 
| ibm-856\_P100-1995 | ibm-273\_P100-1995 | ibm-12712\_P100-1998,swaplfnl | 
| ibm-857\_P100-1995 | ibm-277\_P100-1995 | ibm-16804\_X110-1999,swaplfnl | 
| ibm-858\_P100-1997 | ibm-278\_P100-1995 | ebcdic-xml-us | 