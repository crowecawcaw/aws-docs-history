# Cassandra Query Language (CQL) elements in Amazon Keyspaces

Learn about the Cassandra Query Language (CQL) elements that are supported by Amazon Keyspaces,
including identifiers, constants, terms, and data types.

###### Topics

- [Identifiers](#cql.elements.identifier "#cql.elements.identifier")
- [Constants](#cql.elements.constants "#cql.elements.constants")
- [Terms](#cql.elements.term "#cql.elements.term")
- [Data types](#cql.data-types "#cql.data-types")
- [JSON encoding of Amazon Keyspaces data types](#cql.data-types.JSON "#cql.data-types.JSON")

## Identifiers

Identifiers (or names) are used to identify tables, columns, and other objects. An
identifier can be quoted or not quoted. The following applies.

```
identifier          ::=  unquoted_identifier | quoted_identifier
unquoted_identifier ::=  re('[a-zA-Z][a-zA-Z0-9_]*')
quoted_identifier   ::=  '"' (any character where " can appear if doubled)+ '"'
```

## Constants

The following constants are defined.

```
constant ::=  string | integer | float | boolean | uuid | blob | NULL
string   ::=  '\'' (any character where ' can appear if doubled)+ '\''
              '$$' (any character other than '$$') '$$'
integer  ::=  re('-?[0-9]+')
float    ::=  re('-?[0-9]+(\.[0-9]*)?([eE][+-]?[0-9+])?') | NAN | INFINITY
boolean  ::=  TRUE | FALSE
uuid     ::=  hex{8}-hex{4}-hex{4}-hex{4}-hex{12}
hex      ::=  re("[0-9a-fA-F]")
blob     ::=  '0' ('x' | 'X') hex+
```

## Terms

A term denotes the kind of values that are supported. Terms are defined by the
following.

```
**term**                 ::=  constant | literal | function_call | arithmetic_operation | type_hint | bind_marker
**literal**              ::=  collection_literal | tuple_literal
**function\_call**        ::=  identifier '(' [ term (',' term)* ] ')'
**arithmetic\_operation** ::=  '-' term | term ('+' | '-' | '*' | '/' | '%') term
```

## Data types

Amazon Keyspaces supports the following data types:

### String types

| Data type | Description                                                              |
| --------- | ------------------------------------------------------------------------ |
| `ascii`   | Represents an ASCII character string.                                    |
| `text`    | Represents a UTF-8 encoded string.                                       |
| `varchar` | Represents a UTF-8 encoded string (`varchar` is<br>an alias for `text`). |

### Numeric types

| Data type | Description                                                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bigint`  | Represents a 64-bit signed long.                                                                                                                          |
| `counter` | Represents a 64-bit signed integer counter. For more<br>information, see [Counters](#cql.data-types.numeric.counters "#cql.data-types.numeric.counters"). |
| `decimal` | Represents a variable-precision decimal.                                                                                                                  |
| `double`  | Represents a 64-bit IEEE 754 floating point.                                                                                                              |
| `float`   | Represents a 32-bit IEEE 754 floating point.                                                                                                              |
| `int`     | Represents a 32-bit signed int.                                                                                                                           |
| `varint`  | Represents an integer value within the +/-10^38<br>range.                                                                                                 |

#### Counters

A `counter` column contains a 64-bit signed integer. The
counter value is incremented or decremented using the [UPDATE](cql.dml.md "cql.dml.md") statement, and it cannot be set directly.
This makes `counter` columns useful for tracking counts. For
example, you can use counters to track the number of entries in a log file
or the number of times a post has been viewed on a social network. The
following restrictions apply to `counter` columns:

- A column of type `counter` cannot be part of the
  `primary key` of a table.
- In a table that contains one or more columns of type
  `counter`, all columns in that table must be of type
  `counter`.

In cases where a counter update fails (for example, because of timeouts or
loss of connection with Amazon Keyspaces), the client doesn't know whether the counter
value was updated. If the update is retried, the update to the counter value
might get applied a second time.

### Blob type

| Data type | Description                 |
| --------- | --------------------------- |
| `blob`    | Represents arbitrary bytes. |

### Boolean type

| Data type | Description                   |
| --------- | ----------------------------- |
| `boolean` | Represents `true` or `false`. |

### Time-related types

| Data type   | Description                                                                                                                                                                                                                             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date`      | A string in the format `<yyyy>-<mm>-<dd>`.                                                                                                                                                                                              |
| `timestamp` | 64-bit signed integer representing the date and time since epoch (January 1 1970 at 00:00:00 GMT) in milliseconds.                                                                                                                      |
| `timeuuid`  | Represents a [version 1 UUID](<https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)> "https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)"). |

### Collection types

| Data type | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| `list`    | Represents an ordered collection of literal elements.                  |
| `map`     | Represents an unordered collection of key-value<br>pairs.              |
| `set`     | Represents an unordered collection of one or more literal<br>elements. |

You declare a collection column by using the collection type followed by
another data type (for example, `TEXT` or `INT`) in angled
brackets. You can create a column with a `SET` of `TEXT`,
or you can create a `MAP` of `TEXT` and `INT`
key-value pairs, as shown in the following example.

```
SET <TEXT>
MAP <TEXT, INT>
```

A _non-frozen_ collection allows you to make
updates to each individual collection element. Client-side timestamps and Time to Live (TTL)
settings are stored for individual elements.

When you use the `FROZEN` keyword on a collection type, the values
of the collection are serialized into a single immutable value, and Amazon Keyspaces treats
them like a `BLOB`. This is a _frozen_ collection. An `INSERT` or `UPDATE`
statement overwrites the entire frozen collection. You can't make updates to
individual elements inside a frozen collection.

Client-side timestamps and Time to Live (TTL) settings apply to the entire frozen
collection, not to individual elements. `Frozen` collection columns
can be part of the `PRIMARY KEY` of a table.

You can nest frozen collections. For example, you can define a
`MAP` within a `SET` if the `MAP` is using
the `FROZEN` keyword, as shown in the following example.

```
SET <FROZEN> <MAP <TEXT, INT>>>
```

Amazon Keyspaces supports nesting of up to 8 levels of frozen collections by default.
For more information, see [Amazon Keyspaces service quotas](quotas.md#table "quotas.md#table"). For more information about
functional differences with Apache Cassandra, see [FROZEN
collections](functional-differences.md#functional-differences.frozen-collections "functional-differences.md#functional-differences.frozen-collections"). For more information
about CQL syntax, see [CREATE TABLE](cql.ddl.md#cql.ddl.table.create "cql.ddl.md#cql.ddl.table.create") and [ALTER TABLE](cql.ddl.md#cql.ddl.table.alter "cql.ddl.md#cql.ddl.table.alter").

### Tuple type

The `tuple` data type represents a bounded group of literal
elements. You can use a tuple as an alternative to a `user defined
 type`. You don't need to use the `FROZEN` keyword for
tuples. This is because a tuple is always frozen and you can't update elements
individually.

### Other types

| Data type | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| `inet`    | A string representing an IP address, in either IPv4 or IPv6<br>format. |

### Static

In an Amazon Keyspaces table with clustering columns, you can use the `STATIC`
keyword to create a static column of any type.

The following statement is an example of this.

```
my_column INT STATIC
```

For more information about
working with static columns, see [Estimate capacity consumption for static columns in Amazon Keyspaces](static-columns.md "static-columns.md").

### User-defined types (UDTs)

Amazon Keyspaces supports user-defined types (UDTs). You can use any valid Amazon Keyspaces data type to create a UDT,
including collections and other existing UDTs. You create UDTs in a keyspace and can use them to define
columns in any table in the keyspace.

For more information about CQL syntax, see [User-defined types (UDTs)](cql.ddl.md "cql.ddl.md"). For more information about
working with UDTs, see [User-defined types (UDTs) in Amazon Keyspaces](udts.md "udts.md").

To review how many UDTs are supported per keyspace, supported levels of nesting,
and other default values and quotas related to UDTs, see [Quotas and default values for user-defined types (UDTs) in Amazon Keyspaces](quotas.md#quotas-udts "quotas.md#quotas-udts").

## JSON encoding of Amazon Keyspaces data types

Amazon Keyspaces offers the same JSON data type mappings as Apache Cassandra.
The following table describes the data types Amazon Keyspaces accepts in `INSERT JSON` statements and the data types Amazon Keyspaces uses when
returning data with the `SELECT JSON` statement.

For single-field data types such as `float`, `int`, `UUID`, and `date`, you also can
insert data as a `string`.
For compound data types and collections, such as `tuple`, `map`, and `list`, you can also insert
data as JSON or as an encoded `JSON string`.

| JSON data type | Data types accepted in `INSERT JSON` statements | Data types returned in `SELECT JSON` statements | Notes                                                                                                                                    |
| -------------- | ----------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `ascii`        | `string`                                        | `string`                                        | Uses JSON character escape `\u`.                                                                                                         |
| `bigint`       | `integer, string`                               | `integer`                                       | String must be a valid 64-bit integer.                                                                                                   |
| `blob`         | `string`                                        | `string`                                        | String should begin with `0x` followed by an even number of hex digits.                                                                  |
| `boolean`      | `boolean, string`                               | `boolean`                                       | String must be either `true` or `false`.                                                                                                 |
| `date`         | `string`                                        | `string`                                        | Date in format `YYYY-MM-DD`, timezone UTC.                                                                                               |
| `decimal`      | `integer, float, string`                        | `float`                                         | Can exceed 32-bit or 64-bit IEEE-754 floating point precision in client-side decoder.                                                    |
| `double`       | `integer, float, string`                        | `float`                                         | String must be a valid integer or float.                                                                                                 |
| `float`        | `integer, float, string`                        | `float`                                         | String must be a valid integer or float.                                                                                                 |
| `inet`         | `string`                                        | `string`                                        | IPv4 or IPv6 address.                                                                                                                    |
| `int`          | `integer, string`                               | `integer`                                       | String must be a valid 32-bit integer.                                                                                                   |
| `list`         | `list, string`                                  | `list`                                          | Uses the native JSON list representation.                                                                                                |
| `map`          | `map, string`                                   | `map`                                           | Uses the native JSON map representation.                                                                                                 |
| `smallint`     | `integer, string`                               | `integer`                                       | String must be a valid 16-bit integer.                                                                                                   |
| `set`          | `list, string`                                  | `list`                                          | Uses the native JSON list representation.                                                                                                |
| `text`         | `string`                                        | `string`                                        | Uses JSON character escape `\u`.                                                                                                         |
| `time`         | `string`                                        | `string`                                        | Time of day in format `HH-MM-SS[.fffffffff]`.                                                                                            |
| `timestamp`    | `integer, string`                               | `string`                                        | A timestamp. String constants allow you to store timestamps as dates. Date stamps with format<br>`YYYY-MM-DD HH:MM:SS.SSS` are returned. |
| `timeuuid`     | `string`                                        | `string`                                        | Type 1 UUID. See [constants](#cql.elements.constants "#cql.elements.constants") for the UUID format.                                     |
| `tinyint`      | `integer, string`                               | `integer`                                       | String must be a valid 8-bit integer.                                                                                                    |
| `tuple`        | `list, string`                                  | `list`                                          | Uses the native JSON list representation.                                                                                                |
| `UDT`          | `map, string`                                   | `map`                                           | Uses the native JSON map representation with field names as keys.                                                                        |
| `uuid`         | `string`                                        | `string`                                        | See [constants](#cql.elements.constants "#cql.elements.constants") for the UUID format.                                                  |
| `varchar`      | `string`                                        | `string`                                        | Uses JSON character escape `\u`.                                                                                                         |
| `varint`       | `integer, string`                               | `integer`                                       | Variable length; might overflow 32-bit or 64-bit integers in client-side decoder.                                                        |
