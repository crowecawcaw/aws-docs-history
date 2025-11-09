# RDS for PostgreSQL collations

for EBCDIC and other mainframe migrations

RDS for PostgreSQL versions 10 and higher include ICU version 60.2, which is based on
Unicode 10.0 and includes collations from the Unicode Common Locale Data Repository,
CLDR 32. These software internationalization libraries ensure that character
encodings are presented in a consistent way, regardless of operating system or
platform. For more information about Unicode CLDR-32, see the [CLDR 32 Release
Note](https://cldr.unicode.org/index/downloads/cldr-32 "https://cldr.unicode.org/index/downloads/cldr-32") on the Unicode CLDR website. You can learn more about the
internationalization components for Unicode (ICU) at the [ICU Technical Committee (ICU-TC)](https://icu.unicode.org/home "https://icu.unicode.org/home")
website. For information about ICU-60, see [Download ICU 60](https://icu.unicode.org/download/60 "https://icu.unicode.org/download/60").

Starting with version 14.3, RDS for PostgreSQL also includes collations that help with
data integration and conversion from EBCDIC-based systems. The extended binary coded
decimal interchange code or _EBCDIC_ encoding is commonly used by
mainframe operating systems. These Amazon RDS-provided collations are narrowly defined to
sort only those Unicode characters that directly map to EBCDIC code pages. The
characters are sorted in EBCDIC code-point order to allow for data validation after
conversion. These collations don't include denormalized forms, nor do they
include Unicode characters that don't directly map to a character on the source
EBCDIC code page.

The character mappings between EBCDIC code pages and Unicode code points are based
on tables published by IBM. The complete set is available from IBM as a [compressed file](http://download.boulder.ibm.com/ibmdl/pub/software/dw/java/cdctables.zip "http://download.boulder.ibm.com/ibmdl/pub/software/dw/java/cdctables.zip") for download. RDS for PostgreSQL used these mappings with
tools provided by the ICU to create the collations listed in the tables in this
section. The collation names include a language and country as required by the ICU.
However, EBCDIC code pages don't specify languages, and some EBCDIC code pages
cover multiple countries. That means that the language and country portion of the
collation names in the table are arbitrary, and they don't need to match the
current locale. In other words, the code page number is the most important part of
the collation name in this table. You can use any of the collations listed in the
following tables in any RDS for PostgreSQL database.

- [Unicode to EBCDIC collations table](#ebcdic-table "#ebcdic-table") – Some
  mainframe data migration tools internally use LATIN1 or LATIN9 to encode and
  process data. Such tools use round-trip schemes to preserve data integrity
  and support reverse conversion. The collations in this table can be used by
  tools that process data using LATIN1 encoding, which doesn't require
  special handling.
- [Unicode to LATIN9 collations table](#latin9-table "#latin9-table") – You can
  use these collations in any RDS for PostgreSQL database.

In the following table, you find collations available in RDS for PostgreSQL that map
EBCDIC code pages to Unicode code points. We recommend that you use the collations
in this table for application development that requires sorting based on the
ordering of IBM code pages.

| PostgreSQL collation name | Description of code-page mapping and sort order                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| da-DK-cp277-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 277 (per conversion tables) are sorted in IBM CP 277 code<br>point order |
| de-DE-cp273-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 273 (per conversion tables) are sorted in IBM CP 273 code<br>point order |
| en-GB-cp285-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 285 (per conversion tables) are sorted in IBM CP 285 code<br>point order |
| en-US-cp037-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 037 (per conversion tables) are sorted in IBM CP 37 code<br>point order  |
| es-ES-cp284-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 284 (per conversion tables) are sorted in IBM CP 284 code<br>point order |
| fi-FI-cp278-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 278 (per conversion tables) are sorted in IBM CP 278 code<br>point order |
| fr-FR-cp297-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 297 (per conversion tables) are sorted in IBM CP 297 code<br>point order |
| it-IT-cp280-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 280 (per conversion tables) are sorted in IBM CP 280 code<br>point order |
| nl-BE-cp500-x-icu         | Unicode characters that directly map to IBM EBCDIC Code<br>Page 500 (per conversion tables) are sorted in IBM CP 500 code<br>point order |

Amazon RDS provides a set of additional collations that sort Unicode code points that
map to LATIN9 characters using the tables published by IBM, in the order of the
original code points according to the EBCDIC code page of the source data.

| PostgreSQL collation name | Description of code-page mapping and sort order                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| da-DK-cp1142m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1142 (per conversion tables)<br>are sorted in IBM CP 1142 code point order |
| de-DE-cp1141m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1141 (per conversion tables)<br>are sorted in IBM CP 1141 code point order |
| en-GB-cp1146m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1146 (per conversion tables)<br>are sorted in IBM CP 1146 code point order |
| en-US-cp1140m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1140 (per conversion tables)<br>are sorted in IBM CP 1140 code point order |
| es-ES-cp1145m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1145 (per conversion tables)<br>are sorted in IBM CP 1145 code point order |
| fi-FI-cp1143m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1143 (per conversion tables)<br>are sorted in IBM CP 1143 code point order |
| fr-FR-cp1147m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1147 (per conversion tables)<br>are sorted in IBM CP 1147 code point order |
| it-IT-cp1144m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1144 (per conversion tables)<br>are sorted in IBM CP 1144 code point order |
| nl-BE-cp1148m-x-icu       | Unicode characters that map to LATIN9 characters originally<br>converted from IBM EBCDIC Code Page 1148 (per conversion tables)<br>are sorted in IBM CP 1148 code point order |

In the following, you can find an example of using an RDS for PostgreSQL
collation.

```
`db1=>` SELECT pg_import_system_collations('pg_catalog');
 `pg_import_system_collations
-----------------------------
 36`
`db1=>` SELECT '¤' < 'a' col1;
 `col1
------
 t`
`db1=>` SELECT '¤' < 'a' COLLATE "da-DK-cp277-x-icu" col1;
 `col1
------
 f`
```

We recommend that you use the collations in the [Unicode to EBCDIC collations table](#ebcdic-table "#ebcdic-table") and in the [Unicode to LATIN9 collations table](#latin9-table "#latin9-table") for application development that requires sorting
based on the ordering of IBM code pages. The following collations (suffixed with the
letter “b”) are also visible in `pg_collation`, but are intended for use
by mainframe data integration and migration tools at AWS that map code pages with
specific code point shifts and require special handling in collation. In other
words, the following collations aren't recommended for use.

- da-DK-277b-x-icu
- da-DK-1142b-x-icu
- de-DE-cp273b-x-icu
- de-DE-cp1141b-x-icu
- en-GB-cp1146b-x-icu
- en-GB-cp285b-x-icu
- en-US-cp037b-x-icu
- en-US-cp1140b-x-icu
- es-ES-cp1145b-x-icu
- es-ES-cp284b-x-icu
- fi-FI-cp1143b-x-icu
- fr-FR-cp1147b-x-icu
- fr-FR-cp297b-x-icu
- it-IT-cp1144b-x-icu
- it-IT-cp280b-x-icu
- nl-BE-cp1148b-x-icu
- nl-BE-cp500b-x-icu
  To learn more about migrating applications from mainframe environments to AWS,
  see [What is
  AWS Mainframe Modernization?](../../../m2/latest/userguide/what-is-m2.md "../../../m2/latest/userguide/what-is-m2.md").

For more information about managing collations in PostgreSQL, see [Collation
Support](https://www.postgresql.org/docs/current/collation.html "https://www.postgresql.org/docs/current/collation.html") in the PostgreSQL documentation.
