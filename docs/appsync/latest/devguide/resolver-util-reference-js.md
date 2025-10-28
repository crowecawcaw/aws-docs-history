# AWS AppSync JavaScript runtime features for

resolvers and functions

The `APPSYNC_JS` runtime environment provides functionality similar to [ECMAScript (ES) version 6.0](https://262.ecma-international.org/6.0/ "https://262.ecma-international.org/6.0/"). It
supports a subset of its features and provides some additional methods (utilities) that are
not part of the ES specifications. The following topics list all the supported language
features:

- [Supported runtime features](supported-features.md "supported-features.md") - Learn more about supported core features,
  primitive objects, built-in objects and functions, etc.
- [Built-in utilities](built-in-util-js.md "built-in-util-js.md") - The util variable contains general utility methods to
  help you work with data. Unless otherwise specified, all utilities use the UTF-8
  character set.
- [Built-in modules](built-in-modules-js.md "built-in-modules-js.md") - Learn more about how built-in modules can help write
  JavaScript resolvers and functions.
- [Runtime
  utilities](runtime-utils-js.md "runtime-utils-js.md") - The runtime library provides utilities to control or modify the
  runtime properties of your resolvers and functions.
- [Time helpers in
  util.time](time-helpers-in-util-time-js.md "time-helpers-in-util-time-js.md") - The util.time variable contains datetime methods to help
  generate timestamps, convert between datetime formats, and parse datetime strings. The
  syntax for datetime formats is based on [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html "https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html"), which you can reference for further documentation.
- [DynamoDB
  helpers in util.dynamodb](dynamodb-helpers-in-util-dynamodb-js.md "dynamodb-helpers-in-util-dynamodb-js.md") - util.dynamodb contains helper methods that make
  it easier to write and read data to Amazon DynamoDB, such as automatic type mapping and
  formatting.
- [HTTP helpers in
  util.http](http-helpers-in-utils-http-js.md "http-helpers-in-utils-http-js.md") - The util.http utility provides helper methods that you can use
  to manage HTTP request parameters and to add response headers.
- [Transformation helpers in util.transform](transformation-helpers-in-utils-transform-js.md "transformation-helpers-in-utils-transform-js.md") - util.transform contains helper
  methods that make it easier to perform complex operations against data sources.
- [String helpers in
  util.str](str-helpers-in-util-str-js.md "str-helpers-in-util-str-js.md") - util.str contains methods to help with common String
  operations.
- [Extensions](extensions-js.md "extensions-js.md") - extensions contains a set of methods to make additional actions within your
  resolvers.
- [XML helpers in
  util.xml](xml-helpers-in-util-xml-js.md "xml-helpers-in-util-xml-js.md") - util.xml contains methods to help with XML string
  conversion.

###### Note

Currently, this reference only applies to runtime version **1.0.0**.
