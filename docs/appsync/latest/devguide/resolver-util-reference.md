# AWS AppSync resolver mapping template utility reference

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider
using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

AWS AppSync defines a set of utilities that you can use within a GraphQL resolver to
simplify interactions with data sources. Some of these utilities are for general use with any
data source, such as generating IDs or timestamps. Others are specific to a type of data
source. The following utilities are available:

- [Utility helpers in $util](utility-helpers-in-util.md "utility-helpers-in-util.md") - The $util variable contains general utility
  methods to help you work with data. Unless otherwise specified, all utilities use the
  UTF-8 character set.
- [AppSync directives](aws-appsync-directives.md "aws-appsync-directives.md") - AppSync exposes directives to facilitate developer
  productivity when writing in VTL.
- [Time helpers in $util.time](time-helpers-in-util-time.md "time-helpers-in-util-time.md") - The $util.time variable contains datetime
  methods to help generate timestamps, convert between datetime formats, and parse
  datetime strings. The syntax for datetime formats is based on [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html "https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html"), which you can reference for further documentation.
- [List helpers in
  $util.list](list-helpers-in-util-list.md "list-helpers-in-util-list.md") - $util.list contains methods to help with common List operations
  such as removing or retaining items from a list for filtering use cases.
- [Map helpers in $util.map](utility-helpers-in-map.md "utility-helpers-in-map.md") - $util.map contains methods to help with common
  Map operations such as removing or retaining items from a Map for filtering use
  cases.
- [DynamoDB
  helpers in $util.dynamodb](dynamodb-helpers-in-util-dynamodb.md "dynamodb-helpers-in-util-dynamodb.md") - $util.dynamodb contains helper methods that make
  it easier to write and read data to Amazon DynamoDB, such as automatic type mapping and
  formatting.
- [Amazon RDS helpers in $util.rds](rds-helpers-in-util-rds.md "rds-helpers-in-util-rds.md") - $util.rds contains helper methods that
  format RDS operations by getting rid of extraneous data in result outputs.
- [HTTP helpers in
  $util.http](http-helpers-in-utils-http.md "http-helpers-in-utils-http.md") - The $util.http utility provides helper methods that you can use
  to manage HTTP request parameters and to add response headers.
- [XML helpers in $util.xml](xml-helpers-in-utils-xml.md "xml-helpers-in-utils-xml.md") - $util.xml contains helper methods that can make
  it easier to translate XML responses to JSON or a Dictionary.
- [Transformation helpers in $util.transform](transformation-helpers-in-utils-transform.md "transformation-helpers-in-utils-transform.md") - $util.transform contains helper
  methods that make it easier to perform complex operations against data sources, such as
  DynamoDB filter operations.
- [Math helpers in $util.math](math-helpers-in-util-math.md "math-helpers-in-util-math.md") - $util.math contains methods to help with
  common Math operations.
- [String helpers in $util.str](str-helpers-in-util-str.md "str-helpers-in-util-str.md") - $util.str contains methods to help with common
  String operations.
- [Extensions](extensions.md "extensions.md") - $extensions contains a set of methods to make additional actions within your
  resolvers.
