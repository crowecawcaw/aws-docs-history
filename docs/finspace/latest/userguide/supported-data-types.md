After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Supported data types and file formats in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Amazon FinSpace provides support for a variety of data types in structured data and file formats.

## Supported column types and values for structured data

FinSpace currently supports the following data types for the columns of structured data

- String
- Char
- Integer
- Tiny Integer
- Small Integer
- Big Integer
- Float
- Double
- Date. Supported Date format is yyyy-MM-dd. For example, 2016-12-31
- Datetime. Support Datetime format is yyyy-MM-dd HH:mm:ss. For example, 2016-12-31 15:30:00
- Boolean
- Binary

## Supported file formats

Files of any format can be ingested into FinSpace, but data view creation is only supported for the following formats:

- CSV – Only UTF-8 encoding is supported
- JSON
- Parquet
- XML

## Format options for loading data

FinSpace supports following formatting options when loading data in supported formats types. Currently, the only formats that FinSpace supports are CSV, JSON, Parquet, and XML.

###### Note

The FinSpace web application only supports ingestion for CSV format for creation of data views and comma delimited and `withHeader` option. Other formats are supported with SDK.

## CSV

This value designates comma-separated-values as the data format (for example, see RFC 4180 and RFC 7111).

You can use the following `formatParams` values with `FormatType="csv"`:

1. `separator` – Specifies the delimiter character. The default is a comma "," but any other character can be specified.
2. `escaper` – Specifies a character to use for escaping. This option is used only when reading CSV files. The default value is none. If enabled, the character that immediately follows is used as-is, except for a small set of well-known escapes (\n, \r, \t, and \0).
3. `quoteChar` – Specifies the character to use for quoting. The default is a double quote ("). Set this to -1 to disable quoting entirely.
4. `multiLine` – A Boolean value that specifies whether a single record can span multiple lines. This can occur when a field contains a quoted new-line character. You must set this option to "True" if any record spans multiple lines. The default value is "False", which allows for more aggressive file-splitting during parsing.
5. `withHeader` – A Boolean value that specifies whether to treat the first line as a header. The default value is "True".
6. `skipFirst` – A Boolean value that specifies whether to skip the first data line. The default value is "False".

###### Note

If any of the default values are changed, all format values must be supplied.

## JSON

This value designates a JavaScript Object Notation data format.

You can use the following `formatParams` values with `FormatType="json"`:

1. `jsonPath` – A JsonPath expression that identifies an object to be read into records. This is particularly useful when a file contains
   records nested inside an outer array. For example, the following JsonPath expression targets the id field of a JSON object.

`format="json", format_options={"jsonPath": "$.id"}`

## Parquet

This value designates Apache Parquet as the data format.

There are no `formatParams` values for `FormatType="parquet"`.

## XML

This value designates XML as the data format, parsed through a fork of the [XML data source for Apache spark](https://github.com/databricks/spark-xml "https://github.com/databricks/spark-xml") parser.

You can use the following `formatParams` values with `FormatType="xml"`:

1. `rowTag` – Specifies the XML tag in the file to treat as a row. Row tags cannot be self-closing.
2. `encoding` – Specifies the character encoding. The default value is "UTF-8".
3. `excludeAttribute` – A Boolean value that specifies whether you want to exclude attributes in elements or not. The default value is "false".
4. `treatEmptyValuesAsNulls` – A Boolean value that specifies whether to treat white space as a null value. The default value is "false".
5. `attributePrefix` – A prefix for attributes to differentiate them from elements. This prefix is used for field names. The default value is "\_".
6. `valueTag` – The tag used for a value when there are attributes in the element that have no child. The default is "\_VALUE".
7. `ignoreSurroundingSpaces` – A Boolean value that specifies whether the white space that surrounds values should be ignored. The default value is "false".
