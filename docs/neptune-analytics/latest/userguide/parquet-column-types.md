# Supported Parquet column types

###### Parquet data types:

- NULL
- BOOLEAN
- FLOAT
- DOUBLE
- STRING
- SIGNED INTEGER: UINT8, UINT16, UINT32, UINT64
- MAP: Only supports one-level. Does not support nested.
- LIST: Only supports one-level. Does not support nested.

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
