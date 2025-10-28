# UUID function

The UUID function generates a Universally Unique Identifier (UUID).

UUIDs are globally unique identifiers that are commonly used to provide unique
identifiers for various purposes, such as:

- Identifying database records or other data entities.
- Generating unique names or keys for files, directories, or other resources.
- Tracking and correlating data across distributed systems.
- Providing unique identifiers for network packets, software components, or other
  digital assets.
  The UUID function generates a UUID value that is unique with a very high probability,
  even across distributed systems and over long periods of time. UUIDs are typically
  generated using a combination of the current timestamp, the computer's network address, and
  other random or pseudo-random data, ensuring that each generated UUID is highly unlikely to
  conflict with any other UUID.

In the context of a SQL query, the UUID function can be used to generate unique
identifiers for new records being inserted into a database, or to provide unique keys for
data partitioning, indexing, or other purposes where a unique identifier is
required.

###### Note

The UUID function is non-deterministic.

## Syntax

```
uuid()
```

## Arguments

The UUID function takes no argument.

## Return type

UUID returns a universally unique identifier (UUID) string. The value is returned as
a canonical UUID 36-character string.

## Example

The following example generates a Universally Unique Identifier (UUID). The output is
a 36-character string representing a Universally Unique Identifier.

```
SELECT uuid();
 46707d92-02f4-4817-8116-a4c3b23e6266
```
