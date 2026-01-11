# User-defined types (UDTs)

_UDT_ – A grouping of fields and data types that you can use to
define a single column in Amazon Keyspaces. Valid data types for UDTs are all supported Cassandra
data types, including collections and other UDTs that you've already created in the same
keyspace. For more information about supported Cassandra data types, see [Cassandra data type support](cassandra-apis.md#cassandra-data-type "cassandra-apis.md#cassandra-data-type").

```
user_defined_type::= udt_name
udt_name::= [ keyspace_name '.' ] identifier
```

###### Statements for types

- [CREATE TYPE](#cql.ddl.type.create "#cql.ddl.type.create")
- [DROP TYPE](#cql.ddl.type.drop "#cql.ddl.type.drop")

## CREATE TYPE

Use the `CREATE TYPE` statement to create a new type.

Syntax

```
**create\_type\_statement** ::=  CREATE TYPE [ IF NOT EXISTS ] *udt\_name*    '('*field\_definition* ( ',' *field\_definition*)* ')'
            field_definition::= identifier cql_type
```

Where:

- `IF NOT EXISTS` prevents `CREATE TYPE` from failing
  if the type already exists. (Optional)
- `*udt\_name*` is the fully-qualified name of the UDT in type
  format, for example `my_keyspace.my_type`. If you define the current keyspace with the
  `USE` statement, you don't need to specify the keyspace name.
- `*field\_definition*` consists of a name and a type.

The following table shows examples of allowed UDT names. The first columns shows how to enter the name when you create
the type, the second column shows how Amazon Keyspaces formats the name internally. Amazon Keyspaces expects the formatted name for operations like `GetType`.

| Entered name               | Formatted name           | Note                                                                                                                                 |
| -------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `MY_UDT`                   | `my_udt`                 | Without double-quotes, Amazon Keyspaces converts all upper-case characters to lower-case.                                            |
| `"MY_UDT"`                 | `MY_UDT`                 | With double-quotes, Amazon Keyspaces respects the upper-case characters, and removes the double-quotes from the formatted name.      |
| `"1234"`                   | `1234`                   | With double-quotes, the name can begin with a number, and Amazon Keyspaces removes the double-quotes from the formatted name.        |
| `"Special_Ch@r@cters<>!!"` | `Special_Ch@r@cters<>!!` | With double-quotes, the name can contain special characters, and Amazon Keyspaces removes the double-quotes from the formatted name. |
| `"nested""""""quotes"`     | `nested"""quotes`        | Amazon Keyspaces removes the outer double-quotes and the escape double-quotes from the formatted name.                               |

Examples

```
CREATE TYPE my_keyspace.phone (
    country_code int,
    number text
);
```

You can nest UDTs if the nested UDT is frozen. For more information about default
values and quotas for types, see [Amazon Keyspaces UDT quotas and default values](quotas.md#udt-table "quotas.md#udt-table").

```
CREATE TYPE my_keyspace.user (
    first_name text,
    last_name text,
    phones FROZEN<phone>
);
```

For more code examples that show how to create UDTs, see [User-defined types (UDTs) in Amazon Keyspaces](udts.md "udts.md").

## DROP TYPE

Use the `DROP TYPE` statement to delete a UDT. You can only delete a type that's not in use
by another type or table.

Syntax

```
**drop\_type\_statement** ::=  DROP TYPE [ IF EXISTS ] *udt\_name*
```

Where:

- `IF EXISTS` prevents `DROP TYPE` from failing
  if the type doesn't exist. (Optional)
- `*udt\_name*` is the fully-qualified name of the UDT in type
  format, for example `my_keyspace.my_type`. If you define the current keyspace with the
  `USE` statement, you don't need to specify the keyspace name.

Example

```
DROP TYPE udt_name;
```
