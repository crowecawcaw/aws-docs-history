# Keyword requirements for managed data

identifiers

To detect certain types of sensitive data by using managed data identifiers, Amazon Macie
requires a keyword to be in proximity of the data. If this is the case for a particular type of
data, reference topics in this section indicate the keyword requirements for that data.

If a keyword has to be in proximity of a particular type of data, the keyword typically has
to be within 30 characters (inclusively) of the data. Additional proximity requirements vary based
on the file type or storage format of an Amazon Simple Storage Service (Amazon S3) object.

Structured columnar data

For columnar data, a keyword has to be part of the same value or in the name of the column
or field that stores a value. This is the case for Microsoft Excel workbooks, CSV files, and
TSV files.

For example, if the value for a field contains both _SSN_
and a nine-digit number that uses the syntax of a US Social Security number (SSN), Macie can
detect the SSN in the field. Similarly, if the name of a column contains _SSN_, Macie can detect each SSN in the column. Macie treats the values
in that column as being in proximity of the keyword _SSN_.

Structured record-based data

For record-based data, a keyword has to be part of the same value or in the name of an
element in the path to the field or array that stores a value. This is the case for Apache Avro
object containers, Apache Parquet files, JSON files, and JSON Lines files.

For example, if the value for a field contains both _credentials_ and a character sequence that uses the syntax of an AWS secret
access key, Macie can detect the key in the field. Similarly, if the path to a field is
`$.credentials.aws.key`, Macie can detect an AWS secret access key in the field.
Macie treats the value in the field as being in proximity of the keyword _credentials_.

Unstructured data

For unstructured data, a keyword typically has to be within 30 characters (inclusively) of
the data. There aren't any additional proximity requirements. This is the case for Adobe
Portable Document Format files, Microsoft Word documents, email messages, and non-binary text
files other than CSV, JSON, JSON Lines, and TSV files. This includes any structured data, such
as tables or XML, in these types of files.

Keywords aren’t case sensitive. In addition, if a keyword contains a space, Macie
automatically matches keyword variations that don’t contain the space or contain an underscore (\_)
or a hyphen (-) instead of the space. In certain cases, Macie also expands or abbreviates a
keyword to address common variations of the keyword.

For a demonstration of how keywords provide context and help
Macie detect specific types of sensitive data, watch the following video:
