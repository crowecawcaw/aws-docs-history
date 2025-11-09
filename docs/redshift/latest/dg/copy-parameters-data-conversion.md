Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data conversion parameters

As it loads the table, COPY attempts to implicitly convert the strings in the
source data to the data type of the target column. If you need to specify a
conversion that is different from the default behavior, or if the default conversion
results in errors, you can manage data conversions by specifying the following
parameters. For more information on the syntax of these parameters, see
[COPY syntax](r_COPY.md#r_COPY-syntax "r_COPY.md#r_COPY-syntax").

- [ACCEPTANYDATE](#copy-acceptanydate "#copy-acceptanydate")
- [ACCEPTINVCHARS](#copy-acceptinvchars "#copy-acceptinvchars")
- [BLANKSASNULL](#copy-blanksasnull "#copy-blanksasnull")
- [DATEFORMAT](#copy-dateformat "#copy-dateformat")
- [EMPTYASNULL](#copy-emptyasnull "#copy-emptyasnull")
- [ENCODING](#copy-encoding "#copy-encoding")
- [ESCAPE](#copy-escape "#copy-escape")
- [EXPLICIT_IDS](#copy-explicit-ids "#copy-explicit-ids")
- [FILLRECORD](#copy-fillrecord "#copy-fillrecord")
- [IGNOREBLANKLINES](#copy-ignoreblanklines "#copy-ignoreblanklines")
- [IGNOREHEADER](#copy-ignoreheader "#copy-ignoreheader")
- [NULL AS](#copy-null-as "#copy-null-as")
- [REMOVEQUOTES](#copy-removequotes "#copy-removequotes")
- [ROUNDEC](#copy-roundec "#copy-roundec")
- [TIMEFORMAT](#copy-timeformat "#copy-timeformat")
- [TRIMBLANKS](#copy-trimblanks "#copy-trimblanks")
- [TRUNCATECOLUMNS](#copy-truncatecolumns "#copy-truncatecolumns")

###### Data conversion parameters

ACCEPTANYDATE

Allows any date format, including invalid formats such as `00/00/00
 00:00:00`, to be loaded without generating an error. This parameter
applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
the DATEFORMAT parameter. If the date format for the data doesn't match the
DATEFORMAT specification, Amazon Redshift inserts a NULL value into that
field.

ACCEPTINVCHARS [AS]
['*replacement\_char*']

Enables loading of data into VARCHAR columns even if the data contains
invalid UTF-8 characters. When ACCEPTINVCHARS is specified, COPY replaces
each invalid UTF-8 character with a string of equal length consisting of the
character specified by _replacement_char_. For example,
if the replacement character is '`^`', an invalid three-byte
character will be replaced with '`^^^`'.

The replacement character can be any ASCII character except NULL. The
default is a question mark ( ? ). For information about invalid UTF-8
characters, see [Multibyte character load
errors](multi-byte-character-load-errors.md "multi-byte-character-load-errors.md").

COPY returns the number of rows that contained invalid UTF-8 characters,
and it adds an entry to the [STL_REPLACEMENTS](r_STL_REPLACEMENTS.md "r_STL_REPLACEMENTS.md") system table for each affected row,
up to a maximum of 100 rows for each node slice. Additional invalid UTF-8
characters are also replaced, but those replacement events aren't
recorded.

If ACCEPTINVCHARS isn't specified, COPY returns an error whenever it
encounters an invalid UTF-8 character.

ACCEPTINVCHARS is valid only for VARCHAR columns.

BLANKSASNULL

Loads blank fields, which consist of only white space characters, as
NULL. This option applies only to CHAR and VARCHAR columns. Blank fields for
other data types, such as INT, are always loaded with NULL. For example, a
string that contains three space characters in succession (and no other
characters) is loaded as a NULL. The default behavior, without this option,
is to load the space characters as is.

DATEFORMAT [AS] {'_dateformat_string_' | 'auto' }

If no DATEFORMAT is specified, the default format is
`'YYYY-MM-DD'`. For example, an alternative valid format is
`'MM-DD-YYYY'`.

If the COPY command doesn't recognize the format of your date or time
values, or if your date or time values use different formats, use the
`'auto'` argument with the DATEFORMAT or TIMEFORMAT parameter.
The `'auto'` argument recognizes several formats that aren't
supported when using a DATEFORMAT and TIMEFORMAT string. The
`'auto'`' keyword is case-sensitive. For more information, see
[Using automatic recognition with DATEFORMAT and
TIMEFORMAT](automatic-recognition.md "automatic-recognition.md").

The date format can include time information (hour, minutes, seconds),
but this information is ignored. The AS keyword is optional. For more
information, see [DATEFORMAT and TIMEFORMAT
strings](r_DATEFORMAT_and_TIMEFORMAT_strings.md "r_DATEFORMAT_and_TIMEFORMAT_strings.md").

EMPTYASNULL

Indicates that Amazon Redshift should load empty CHAR and VARCHAR fields as
NULL. Empty fields for other data types, such as INT, are always loaded with
NULL. Empty fields occur when data contains two delimiters in succession
with no characters between the delimiters. EMPTYASNULL and NULL AS '' (empty
string) produce the same behavior.

ENCODING [AS] _file_encoding_

Specifies the encoding type of the load data. The COPY command converts
the data from the specified encoding into UTF-8 during loading.

Valid values for _file_encoding_ are as
follows:

- `UTF8`
- `UTF16`
- `UTF16LE`
- `UTF16BE`
- `ISO88591`

The default is `UTF8`.

Source file names must use UTF-8 encoding.

The following files must use UTF-8 encoding, even if a different encoding
is specified for the load data:

- Manifest files
- JSONPaths files

The argument strings provided with the following parameters must use
UTF-8:

- FIXEDWIDTH '_fixedwidth_spec_'
- ACCEPTINVCHARS '_replacement_char_'
- DATEFORMAT '_dateformat_string_'
- TIMEFORMAT '_timeformat_string_'
- NULL AS '_null_string_'

Fixed-width data files must use UTF-8 encoding. The field widths are
based on the number of characters, not the number of bytes.

All load data must use the specified encoding. If COPY encounters a
different encoding, it skips the file and returns an error.

If you specify `UTF16`, then your data must have a byte order
mark (BOM). If you know whether your UTF-16 data is little-endian (LE) or
big-endian (BE), you can use `UTF16LE` or `UTF16BE`,
regardless of the presence of a BOM.

To use ISO-8859-1 encoding specify `ISO88591`.
For more information, see [ISO/IEC 8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1 "https://en.wikipedia.org/wiki/ISO/IEC_8859-1") in _Wikipedia_.

ESCAPE

When this parameter is specified, the backslash character
(`\`) in input data is treated as an escape character. The
character that immediately follows the backslash character is loaded into
the table as part of the current column value, even if it is a character
that normally serves a special purpose. For example, you can use this
parameter to escape the delimiter character, a quotation mark, an embedded
newline character, or the escape character itself when any of these
characters is a legitimate part of a column value.

If you specify the ESCAPE parameter in combination with the REMOVEQUOTES
parameter, you can escape and retain quotation marks (`'` or
`"`) that might otherwise be removed. The default null string,
`\N`, works as is, but it can also be escaped in the input
data as `\\N`. As long as you don't specify an alternative null
string with the NULL AS parameter, `\N` and `\\N`
produce the same results.

###### Note

The control character `0x00` (NUL) can't be escaped and
should be removed from the input data or converted. This character is
treated as an end of record (EOR) marker, causing the remainder of the
record to be truncated.

You can't use the ESCAPE parameter for FIXEDWIDTH loads, and you can't
specify the escape character itself; the escape character is always the
backslash character. Also, you must ensure that the input data contains the
escape character in the appropriate places.

Here are some examples of input data and the resulting loaded data when
the ESCAPE parameter is specified. The result for row 4 assumes that the
REMOVEQUOTES parameter is also specified. The input data consists of two
pipe-delimited fields:

```
1|The quick brown fox\[newline]
jumped over the lazy dog.
2| A\\B\\C
3| A \| B \| C
4| 'A Midsummer Night\'s Dream'
```

The data loaded into column 2 looks like this:

```
The quick brown fox
jumped over the lazy dog.
A\B\C
A|B|C
A Midsummer Night's Dream
```

###### Note

Applying the escape character to the input data for a load is the
responsibility of the user. One exception to this requirement is when you
reload data that was previously unloaded with the ESCAPE parameter. In
this case, the data will already contain the necessary escape
characters.

The ESCAPE parameter doesn't interpret octal, hex, Unicode, or other
escape sequence notation. For example, if your source data contains the
octal line feed value (`\012`) and you try to load this data with
the ESCAPE parameter, Amazon Redshift loads the value `012` into the
table and doesn't interpret this value as a line feed that is being
escaped.

In order to escape newline characters in data that originates from
Microsoft Windows platforms, you might need to use two escape characters:
one for the carriage return and one for the line feed. Alternatively, you
can remove the carriage returns before loading the file (for example, by
using the dos2unix utility).

EXPLICIT_IDS

Use EXPLICIT_IDS with tables that have IDENTITY columns if you want to
override the autogenerated values with explicit values from the source data
files for the tables. If the command includes a column list, that list must
include the IDENTITY columns to use this parameter. The data format for
EXPLICIT_IDS values must match the IDENTITY format specified by the CREATE
TABLE definition.

When you run a COPY command against a table with the EXPLICIT_IDS option, Amazon Redshift
does not check the uniqueness of IDENTITY columns in the table.

If a column is defined with GENERATED BY DEFAULT AS IDENTITY, then it can be
copied. Values are generated or updated with values that you supply. The EXPLICIT_IDS
option isn't required. COPY doesn't update the identity high watermark.

For an example of a COPY command using EXPLICIT_IDS, see
[Load VENUE with explicit values for an IDENTITY column](r_COPY_command_examples.md#r_COPY_command_examples-load-venue-with-explicit-values-for-an-identity-column "r_COPY_command_examples.md#r_COPY_command_examples-load-venue-with-explicit-values-for-an-identity-column").

FILLRECORD

Allows data files to be loaded when contiguous columns are missing at the
end of some of the records. The missing columns are loaded as NULLs. For
text and CSV formats, if the missing column is a VARCHAR column, zero-length
strings are loaded instead of NULLs. To load NULLs to VARCHAR columns from
text and CSV, specify the EMPTYASNULL keyword. NULL substitution only works
if the column definition allows NULLs.

For example, if the table definition contains four nullable CHAR columns,
and a record contains the values `apple, orange, banana, mango`,
the COPY command could load and fill in a record that contains only the
values `apple, orange`. The missing CHAR values would be loaded
as NULL values.

IGNOREBLANKLINES

Ignores blank lines that only contain a line feed in a data file and does
not try to load them.

IGNOREHEADER [ AS ] _number_rows_

Treats the specified _number_rows_ as a file header
and doesn't load them. Use IGNOREHEADER to skip file headers in all files
in a parallel load.

NULL AS '_null_string_'

Loads fields that match _null_string_ as NULL, where
_null_string_ can be any string. If your data includes
a null terminator, also referred to as NUL (UTF-8 0000) or binary zero
(0x000), COPY treats it as any other character. For example, a record containing '1' || NUL || '2' is copied as string of length 3 bytes.
If a field contains only NUL, you can use NULL AS to replace the null
terminator with NULL by specifying `'\0'` or
`'\000'`—for example, `NULL AS '\0'` or
`NULL AS '\000'`. If a field contains a string that ends with
NUL and NULL AS is specified, the string is inserted with NUL at the end. Do
not use '\n' (newline) for the _null_string_ value.
Amazon Redshift reserves '\n' for use as a line delimiter. The default
_null_string_ is `'\N`'.

###### Note

If you attempt to load nulls into a column defined as NOT NULL, the
COPY command will fail.

REMOVEQUOTES

Removes surrounding quotation marks from strings in the incoming data.
All characters within the quotation marks, including delimiters, are
retained. If a string has a beginning single or double quotation mark but no
corresponding ending mark, the COPY command fails to load that row and
returns an error. The following table shows some simple examples of strings
that contain quotation marks and the resulting loaded values.

| Input String               | Loaded Value with REMOVEQUOTES Option  |
| -------------------------- | -------------------------------------- | ------------------------- | ----------- |
| "The delimiter is a pipe ( | )<br>character"                        | The delimiter is a pipe ( | ) character |
| 'Black'                    | Black                                  |
| "White"                    | White                                  |
| Blue'                      | Blue'                                  |
| 'Blue                      | _Value not loaded: error<br>condition_ |
| "Blue                      | _Value not loaded: error<br>condition_ |
| ' ' 'Black' ' '            | ' 'Black' '                            |
| ' '                        | _<white space>_                        |

ROUNDEC

Rounds up numeric values when the scale of the input value is greater
than the scale of the column. By default, COPY truncates values when
necessary to fit the scale of the column. For example, if a value of
`20.259` is loaded into a DECIMAL(8,2) column, COPY truncates
the value to `20.25` by default. If ROUNDEC is specified, COPY
rounds the value to `20.26`. The INSERT command always rounds
values when necessary to match the column's scale, so a COPY command with
the ROUNDEC parameter behaves the same as an INSERT command.

TIMEFORMAT [AS] {'_timeformat_string_' | 'auto' |
'epochsecs' | 'epochmillisecs' }

Specifies the time format. If no TIMEFORMAT is specified, the default
format is `YYYY-MM-DD HH:MI:SS` for TIMESTAMP columns or
`YYYY-MM-DD HH:MI:SSOF` for TIMESTAMPTZ columns, where
`OF` is the offset from Coordinated Universal Time (UTC). You
can't include a time zone specifier in the
_timeformat_string_. To load TIMESTAMPTZ data that is
in a format different from the default format, specify 'auto'; for more
information, see [Using automatic recognition with DATEFORMAT and
TIMEFORMAT](automatic-recognition.md "automatic-recognition.md"). For more information about
_timeformat_string_, see [DATEFORMAT and TIMEFORMAT
strings](r_DATEFORMAT_and_TIMEFORMAT_strings.md "r_DATEFORMAT_and_TIMEFORMAT_strings.md").

The `'auto'` argument recognizes several formats that aren't
supported when using a DATEFORMAT and TIMEFORMAT string. If the COPY command
doesn't recognize the format of your date or time values, or if your date
and time values use formats different from each other, use the
`'auto'` argument with the DATEFORMAT or TIMEFORMAT parameter.
For more information, see [Using automatic recognition with DATEFORMAT and
TIMEFORMAT](automatic-recognition.md "automatic-recognition.md").

If your source data is represented as epoch time, that is the number of
seconds or milliseconds since January 1, 1970, 00:00:00 UTC, specify
`'epochsecs'` or `'epochmillisecs'`.

The `'auto'`, `'epochsecs'`, and
`'epochmillisecs'` keywords are case-sensitive.

The AS keyword is optional.

TRIMBLANKS

Removes the trailing white space characters from a VARCHAR string. This
parameter applies only to columns with a VARCHAR data type.

TRUNCATECOLUMNS

Truncates data in columns to the appropriate number of characters so that
it fits the column specification. Applies only to columns with a VARCHAR or
CHAR data type, and rows 4 MB or less in size.
