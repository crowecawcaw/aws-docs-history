# SQL naming rules

The following sections explain the SQL naming rules in AWS Clean Rooms.

###### Topics

- [Configured table association names
  and columns](#confg-table-and-column-naming-rules "#confg-table-and-column-naming-rules")
- [Reserved words](#reserved-words "#reserved-words")

## Configured table association names

and columns

Members who can query use configured table association names as table names in queries.
Configured table association names and configured table columns can be aliased in queries.

The following naming rules apply to configured table association names, configured table
column names, and aliases:

- They must use only alphanumeric, underscore (\_), or hyphen (-) characters but
  can't start or end with a hyphen.
  - (_Custom analysis rule only_) They can use
    the dollar sign ($) but can't use a pattern that follows a dollar-quoted string
    constant.

  A dollar-quoted string constant consists of:

      - a dollar sign ($)
      - an optional "tag" of zero or more characters
      - another dollar sign
      - arbitrary sequence of characters that makes up the string
       content
      - a dollar sign ($)
      - the same tag that began the dollar quote
      - a dollar sign


      For example: `$$invalid$$`

- They can't contain consecutive hyphen (-) characters.
- They can't begin with any of the following prefixes:

`padb_`, `pg_`, `stcs_`, `stl_`,
`stll_`, `stv_`, `svcs_`, `svl_`,
`svv_`, `sys_`, `systable_`

- They can't contain backslash characters (\) , quotation marks ('), or spaces that
  aren't double-quoted.
- If they start with a non-alphabetical character, they must be within double-quotes
  (" ").
- If they contain a hyphen (-) character, they must be within double-quotes ("
  ").
- They must be between 1 and 127 characters in length.
- [Reserved words](#reserved-words "#reserved-words") must be within double-quotes
  (" ").
- The following column names are reserved can't be used in AWS Clean Rooms (even with
  quotes):
  - oid
  - tableoid
  - xmin
  - cmin
  - xmax
  - cmax
  - ctid

## Reserved words

The following is a list of reserved words in AWS Clean Rooms.

|                        |                    |                   |                      |
| ---------------------- | ------------------ | ----------------- | -------------------- |
| AES128                 | DELTA32KDESC       | LEADING           | PRIMARY              |
| AES256ALL              | DISTINCT           | LEFTLIKE          | RAW                  |
| ALLOWOVERWRITEANALYSE  | DO                 | LIMIT             | READRATIO            |
| ANALYZE                | DISABLE            | LOCALTIME         | RECOVERREFERENCES    |
| AND                    | ELSE               | LOCALTIMESTAMP    | REJECTLOG            |
| ANY                    | EMPTYASNULLENABLE  | LUN               | RESORT               |
| ARRAY                  | ENCODE             | LUNS              | RESPECT              |
| AS                     | ENCRYPT            | LZO               | RESTORE              |
| ASC                    | ENCRYPTIONEND      | LZOP              | RIGHTSELECT          |
| AUTHORIZATION          | EXCEPT             | MINUS             | SESSION_USER         |
| AZ64                   | EXPLICITFALSE      | MOSTLY16          | SIMILAR              |
| BACKUPBETWEEN          | FOR                | MOSTLY32          | SNAPSHOT             |
| BINARY                 | FOREIGN            | MOSTLY8NATURAL    | SOME                 |
| BLANKSASNULLBOTH       | FREEZE             | NEW               | SYSDATESYSTEM        |
| BYTEDICT               | FROM               | NOT               | TABLE                |
| BZIP2CASE              | FULL               | NOTNULL           | TAG                  |
| CAST                   | GLOBALDICT256      | NULL              | TDES                 |
| CHECK                  | GLOBALDICT64KGRANT | NULLSOFF          | TEXT255              |
| COLLATE                | GROUP              | OFFLINEOFFSET     | TEXT32KTHEN          |
| COLUMN                 | GZIPHAVING         | OID               | TIMESTAMP            |
| CONSTRAINT             | IDENTITY           | OLD               | TO                   |
| CREATE                 | IGNOREILIKE        | ON                | TOPTRAILING          |
| CREDENTIALSCROSS       | IN                 | ONLY              | TRUE                 |
| CURRENT_DATE           | INITIALLY          | OPEN              | TRUNCATECOLUMNSUNION |
| CURRENT_TIME           | INNER              | OR                | UNIQUE               |
| CURRENT_TIMESTAMP      | INTERSECT          | ORDER             | UNNEST               |
| CURRENT_USER           | INTERVAL           | OUTER             | USING                |
| CURRENT_USER_IDDEFAULT | INTO               | OVERLAPS          | VERBOSE              |
| DEFERRABLE             | IS                 | PARALLELPARTITION | WALLETWHEN           |
| DEFLATE                | ISNULL             | PERCENT           | WHERE                |
| DEFRAG                 | JOIN               | PERMISSIONS       | WITH                 |
| DELTA                  | LANGUAGE           | PIVOTPLACING      | WITHOUT              |
