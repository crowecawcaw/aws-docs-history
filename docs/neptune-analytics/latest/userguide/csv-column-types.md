# Supported CSV column types

- Bool (or Boolean) - Allowed values: `true`, `false`. Indicates a Boolean field.
  Any value other than `true` will be treated as `false`.
- FLOAT - Range: 32-bit IEEE 754 floating point including Infinity, INF, -Infinity, -INF and NaN (not-a-number).
- DOUBLE - Range: 64-bit IEEE 754 floating point including Infinity, INF, -Infinity, -INF and NaN (not-a-number).
- STRING -
  - Quotation marks are optional. Commas, newline, and carriage return characters are automatically escaped
    if they are included in a string surrounded by double quotation marks (`"`).
    Example: `"Hello, World"`.
  - To include quotation marks in a quoted string, you can escape the quotation mark by using two in a row:
    Example: `"Hello ""World"""`.
  - Arrays of strings are allowed, but strings in an array cannot include the semicolon (`;`)
    character unless it is escaped using a backslash (`\;`).
  - If you want to surround strings in an array with quotation marks, you must surround the whole array
    with one set of quotation marks. Example: `"String one; String 2; String 3"`.

- Datetime - The datetime values can be provided in either the XSD format, or one of the following formats:
  - yyyy-MM-dd
  - yyyy-MM-ddTHH:mm
  - yyyy-MM-ddTHH:mm:ss
  - yyyy-MM-ddTHH:mm:ssZ
  - yyyy-MM-ddTHH:mm:ss.SSSZ
  - yyyy-MM-ddTHH:mm:ss[+|-]hhmm
  - yyyy-MM-ddTHH:mm:ss.SSS[+|-]hhmm

- SIGNED INTEGER -
  - Byte: -128 to 127
  - Short: -32768 to 32767
  - Int: -2^31 to 2^31-1
  - Long: -2^63 to 2^63-1

###### Neptune -specific:

- A column type `Any` is supported in the user columns. An `Any` type is a type “syntactic sugar” for
  all of the other types we support. It is extremely useful if a user column has multiple types in it. The payload of an
  `Any` type value is a list of json strings as follows: `"{""value"": ""10"", ""type"": ""Int""};{""value"": 
""1.0"", ""type"": ""Float""}"` , which has a `value` field and a `type` field in each
  individual json string. The column header of an `Any` type is `propertyname:Any`. The cardinality
  value of an `Any` column is `set`, meaning that the column can accept multiple values.
  - Neptune Analytics supports the following types in an `Any` type: `Bool` (or `Boolean`),
    `Byte`, `Short`, `Int`, `Long`, `UnsignedByte`,
    `UnsignedShort`, `UnsignedInt`, `UnsignedLong`, `Float`, `Double`,
    `Date`, `dateTime`, and `String`.
  - `Vector` type is not supported in `Any` type.
  - Nested `Any` type is not supported. For example, `"{""value"": "{""value"": ""10"", ""type"": 
""Int""}", ""type"": ""Any""}"`.
