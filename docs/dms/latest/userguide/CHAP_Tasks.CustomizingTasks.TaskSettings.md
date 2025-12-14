# Character substitution task settings

You can specify that your replication task perform character substitutions on
the target database for all source database columns with the AWS DMS
`STRING` or `WSTRING` data type. For information about how to use a task configuration file to set task settings, see [Task settings example](CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example").

You can configure
character substitution for any task with endpoints from the following source and
target databases:

- Source databases:
  - Oracle
  - Microsoft SQL Server
  - MySQL
  - PostgreSQL
  - SAP Adaptive Server Enterprise (ASE)
  - IBM Db2 LUW

- Target databases:

      + Oracle
      + Microsoft SQL Server
      + MySQL
      + PostgreSQL
      + SAP Adaptive Server Enterprise (ASE)
      + Amazon Redshift

  You can specify character substitutions using the
  `CharacterSetSettings` parameter in your task settings. These
  character substitutions occur for characters specified using the Unicode code
  point value in hexadecimal notation. You can implement the substitutions in two
  phases, in the following order if both are specified:

1. **Individual character replacement**
   – AWS DMS can replace the values of selected characters on the
   source with specified replacement values of corresponding characters on
   the target. Use the `CharacterReplacements` array in
   `CharacterSetSettings` to select all source characters
   having the Unicode code points you specify. Use this array also to
   specify the replacement code points for the corresponding characters on
   the target.

To select all characters on the source that have a given code point,
set an instance of `SourceCharacterCodePoint` in the
`CharacterReplacements` array to that code point. Then
specify the replacement code point for all equivalent target characters
by setting the corresponding instance of
`TargetCharacterCodePoint` in this array. To delete
target characters instead of replacing them, set the appropriate
instances of `TargetCharacterCodePoint` to zero (0). You can
replace or delete as many different values of target characters as you
want by specifying additional pairs of
`SourceCharacterCodePoint` and
`TargetCharacterCodePoint` settings in the
`CharacterReplacements` array. If you specify the same
value for multiple instances of `SourceCharacterCodePoint`,
the value of the last corresponding setting of
`TargetCharacterCodePoint` applies on the target.

For example, suppose that you specify the following values for
`CharacterReplacements`.

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

In this example, AWS DMS replaces all characters with the source code
point hex value 62 on the target by characters with the code point value 61. Also, AWS DMS replaces all characters with the source code point 42 on
the target by characters with the code point value 41. In other words,
AWS DMS replaces all instances of the letter `'b'`on the target
by the letter `'a'`. Similarly, AWS DMS replaces all instances
of the letter `'B'` on the target by the letter
`'A'`. 2. **Character set validation and
replacement** – After any individual character
replacements complete, AWS DMS can make sure that all target characters
have valid Unicode code points in the single character set that you
specify. You use `CharacterSetSupport` in
`CharacterSetSettings` to configure this target character
verification and modification. To specify the verification character
set, set `CharacterSet` in `CharacterSetSupport`
to the character set's string value. (The possible values for
`CharacterSet` follow.) You can have AWS DMS modify the
invalid target characters in one of the following ways:

    * Specify a single replacement Unicode code point for all
     invalid target characters, regardless of their current code
     point. To configure this replacement code point, set
     `ReplaceWithCharacterCodePoint` in
     `CharacterSetSupport` to the specified
     value.
    * Configure the deletion of all invalid target characters by
     setting `ReplaceWithCharacterCodePoint` to zero
     (0).

For example, suppose that you specify the following values for
`CharacterSetSupport`.

```
"CharacterSetSettings": {
    "CharacterSetSupport": {
        "CharacterSet": "UTF16_PlatformEndian",
        "ReplaceWithCharacterCodePoint": 0
    }
}
```

In this example, AWS DMS deletes any characters found on the target that
are invalid in the `"UTF16_PlatformEndian"` character set.
So, any characters specified with the hex value `2FB6` are
deleted. This value is invalid because this is a 4-byte Unicode code
point and UTF16 character sets accept only characters with 2-byte code
points.

###### Note

The replication task completes all of the specified character
substitutions before starting any global or table-level transformations that
you specify through table mapping. For more information about table mapping,
see [Using table mapping to
specify task settings](CHAP_Tasks.CustomizingTasks.md "CHAP_Tasks.CustomizingTasks.md").

Character substitution doesn't support LOB data types. This includes any datatype that
DMS considers to be a LOB data type. For example, the `Extended` datatype in
Oracle is considered to be a LOB. For more information about source datatypes, see
[Source data types for Oracle](CHAP_Source.md#CHAP_Source.Oracle.DataTypes "CHAP_Source.md#CHAP_Source.Oracle.DataTypes")
following.

The values that AWS DMS supports for `CharacterSet` appear in the
table following.

|                               |                                |                                |
| ----------------------------- | ------------------------------ | ------------------------------ |
| `UTF-8`                       | `ibm-860_P100-1995`            | `ibm-280_P100-1995`            |
| `UTF-16`                      | `ibm-861_P100-1995`            | `ibm-284_P100-1995`            |
| `UTF-16BE`                    | `ibm-862_P100-1995`            | `ibm-285_P100-1995`            |
| `UTF-16LE`                    | `ibm-863_P100-1995`            | `ibm-290_P100-1995`            |
| `UTF-32`                      | `ibm-864_X110-1999`            | `ibm-297_P100-1995`            |
| `UTF-32BE`                    | `ibm-865_P100-1995`            | `ibm-420_X120-1999`            |
| `UTF-32LE`                    | `ibm-866_P100-1995`            | `ibm-424_P100-1995`            |
| `UTF16_PlatformEndian`        | `ibm-867_P100-1998`            | `ibm-500_P100-1995`            |
| `UTF16_OppositeEndian`        | `ibm-868_P100-1995`            | `ibm-803_P100-1999`            |
| `UTF32_PlatformEndian`        | `ibm-869_P100-1995`            | `ibm-838_P100-1995`            |
| `UTF32_OppositeEndian`        | `ibm-878_P100-1996`            | `ibm-870_P100-1995`            |
| `UTF-16BE,version=1`          | `ibm-901_P100-1999`            | `ibm-871_P100-1995`            |
| `UTF-16LE,version=1`          | `ibm-902_P100-1999`            | `ibm-875_P100-1995`            |
| `UTF-16,version=1`            | `ibm-922_P100-1999`            | `ibm-918_P100-1995`            |
| `UTF-16,version=2`            | `ibm-1168_P100-2002`           | `ibm-930_P120-1999`            |
| `UTF-7`                       | `ibm-4909_P100-1999`           | `ibm-933_P110-1995`            |
| `IMAP-mailbox-name`           | `ibm-5346_P100-1998`           | `ibm-935_P110-1999`            |
| `SCSU`                        | `ibm-5347_P100-1998`           | `ibm-937_P110-1999`            |
| `BOCU-1`                      | `ibm-5348_P100-1997`           | `ibm-939_P120-1999`            |
| `CESU-8`                      | `ibm-5349_P100-1998`           | `ibm-1025_P100-1995`           |
| `ISO-8859-1`                  | `ibm-5350_P100-1998`           | `ibm-1026_P100-1995`           |
| `US-ASCII`                    | `ibm-9447_P100-2002`           | `ibm-1047_P100-1995`           |
| `gb18030`                     | `ibm-9448_X100-2005`           | `ibm-1097_P100-1995`           |
| `ibm-912_P100-1995`           | `ibm-9449_P100-2002`           | `ibm-1112_P100-1995`           |
| `ibm-913_P100-2000`           | `ibm-5354_P100-1998`           | `ibm-1122_P100-1999`           |
| `ibm-914_P100-1995`           | `ibm-1250_P100-1995`           | `ibm-1123_P100-1995`           |
| `ibm-915_P100-1995`           | `ibm-1251_P100-1995`           | `ibm-1130_P100-1997`           |
| `ibm-1089_P100-1995`          | `ibm-1252_P100-2000`           | `ibm-1132_P100-1998`           |
| `ibm-9005_X110-2007`          | `ibm-1253_P100-1995`           | `ibm-1137_P100-1999`           |
| `ibm-813_P100-1995`           | `ibm-1254_P100-1995`           | `ibm-4517_P100-2005`           |
| `ibm-5012_P100-1999`          | `ibm-1255_P100-1995`           | `ibm-1140_P100-1997`           |
| `ibm-916_P100-1995`           | `ibm-5351_P100-1998`           | `ibm-1141_P100-1997`           |
| `ibm-920_P100-1995`           | `ibm-1256_P110-1997`           | `ibm-1142_P100-1997`           |
| `iso-8859_10-1998`            | `ibm-5352_P100-1998`           | `ibm-1143_P100-1997`           |
| `iso-8859_11-2001`            | `ibm-1257_P100-1995`           | `ibm-1144_P100-1997`           |
| `ibm-921_P100-1995`           | `ibm-5353_P100-1998`           | `ibm-1145_P100-1997`           |
| `iso-8859_14-1998`            | `ibm-1258_P100-1997`           | `ibm-1146_P100-1997`           |
| `ibm-923_P100-1998`           | `macos-0_2-10.2`               | `ibm-1147_P100-1997`           |
| `ibm-942_P12A-1999`           | `macos-6_2-10.4`               | `ibm-1148_P100-1997`           |
| `ibm-943_P15A-2003`           | `macos-7_3-10.2`               | `ibm-1149_P100-1997`           |
| `ibm-943_P130-1999`           | `macos-29-10.2`                | `ibm-1153_P100-1999`           |
| `ibm-33722_P12A_P12A-2009_U2` | `macos-35-10.2`                | `ibm-1154_P100-1999`           |
| `ibm-33722_P120-1999`         | `ibm-1051_P100-1995`           | `ibm-1155_P100-1999`           |
| `ibm-954_P101-2007`           | `ibm-1276_P100-1995`           | `ibm-1156_P100-1999`           |
| `euc-jp-2007`                 | `ibm-1006_P100-1995`           | `ibm-1157_P100-1999`           |
| `ibm-1373_P100-2002`          | `ibm-1098_P100-1995`           | `ibm-1158_P100-1999`           |
| `windows-950-2000`            | `ibm-1124_P100-1996`           | `ibm-1160_P100-1999`           |
| `ibm-950_P110-1999`           | `ibm-1125_P100-1997`           | `ibm-1164_P100-1999`           |
| `ibm-1375_P100-2008`          | `ibm-1129_P100-1997`           | `ibm-1364_P110-2007`           |
| `ibm-5471_P100-2006`          | `ibm-1131_P100-1997`           | `ibm-1371_P100-1999`           |
| `ibm-1386_P100-2001`          | `ibm-1133_P100-1997`           | `ibm-1388_P103-2001`           |
| `windows-936-2000`            | `ISO_2022,locale=ja,version=0` | `ibm-1390_P110-2003`           |
| `ibm-1383_P110-1999`          | `ISO_2022,locale=ja,version=1` | `ibm-1399_P110-2003`           |
| `ibm-5478_P100-1995`          | `ISO_2022,locale=ja,version=2` | `ibm-5123_P100-1999`           |
| `euc-tw-2014`                 | `ISO_2022,locale=ja,version=3` | `ibm-8482_P100-1999`           |
| `ibm-964_P110-1999`           | `ISO_2022,locale=ja,version=4` | `ibm-16684_P110-2003`          |
| `ibm-949_P110-1999`           | `ISO_2022,locale=ko,version=0` | `ibm-4899_P100-1998`           |
| `ibm-949_P11A-1999`           | `ISO_2022,locale=ko,version=1` | `ibm-4971_P100-1999`           |
| `ibm-970_P110_P110-2006_U2`   | `ISO_2022,locale=zh,version=0` | `ibm-9067_X100-2005`           |
| `ibm-971_P100-1995`           | `ISO_2022,locale=zh,version=1` | `ibm-12712_P100-1998`          |
| `ibm-1363_P11B-1998`          | `ISO_2022,locale=zh,version=2` | `ibm-16804_X110-1999`          |
| `ibm-1363_P110-1997`          | `HZ`                           | `ibm-37_P100-1995,swaplfnl`    |
| `windows-949-2000`            | `x11-compound-text`            | `ibm-1047_P100-1995,swaplfnl`  |
| `windows-874-2000`            | `ISCII,version=0`              | `ibm-1140_P100-1997,swaplfnl`  |
| `ibm-874_P100-1995`           | `ISCII,version=1`              | `ibm-1141_P100-1997,swaplfnl`  |
| `ibm-1162_P100-1999`          | `ISCII,version=2`              | `ibm-1142_P100-1997,swaplfnl`  |
| `ibm-437_P100-1995`           | `ISCII,version=3`              | `ibm-1143_P100-1997,swaplfnl`  |
| `ibm-720_P100-1997`           | `ISCII,version=4`              | `ibm-1144_P100-1997,swaplfnl`  |
| `ibm-737_P100-1997`           | `ISCII,version=5`              | `ibm-1145_P100-1997,swaplfnl`  |
| `ibm-775_P100-1996`           | `ISCII,version=6`              | `ibm-1146_P100-1997,swaplfnl`  |
| `ibm-850_P100-1995`           | `ISCII,version=7`              | `ibm-1147_P100-1997,swaplfnl`  |
| `ibm-851_P100-1995`           | `ISCII,version=8`              | `ibm-1148_P100-1997,swaplfnl`  |
| `ibm-852_P100-1995`           | `LMBCS-1`                      | `ibm-1149_P100-1997,swaplfnl`  |
| `ibm-855_P100-1995`           | `ibm-37_P100-1995`             | `ibm-1153_P100-1999,swaplfnl`  |
| `ibm-856_P100-1995`           | `ibm-273_P100-1995`            | `ibm-12712_P100-1998,swaplfnl` |
| `ibm-857_P100-1995`           | `ibm-277_P100-1995`            | `ibm-16804_X110-1999,swaplfnl` |
| `ibm-858_P100-1997`           | `ibm-278_P100-1995`            | `ebcdic-xml-us`                |
