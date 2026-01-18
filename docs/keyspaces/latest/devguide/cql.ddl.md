# Keyspaces

A _keyspace_ groups related tables that are
relevant for one or more applications. In terms of a relational database management
system (RDBMS), keyspaces are roughly similar to databases, tablespaces, or similar
constructs.

###### Note

In Apache Cassandra, keyspaces determine how data is replicated among multiple
storage nodes. However, Amazon Keyspaces is a fully managed service: The details of its
storage layer are managed on your behalf. For this reason, keyspaces in Amazon Keyspaces
are logical constructs only, and aren't related to the underlying physical
storage.

For information about quota limits and constraints for Amazon Keyspaces keyspaces, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

###### Statements for keyspaces

- [CREATE KEYSPACE](#cql.ddl.keyspace.create "#cql.ddl.keyspace.create")
- [ALTER KEYSPACE](#cql.ddl.keyspace.alter "#cql.ddl.keyspace.alter")
- [DROP KEYSPACE](#cql.ddl.keyspace.drop "#cql.ddl.keyspace.drop")
- [USE](#cql.ddl.keyspace.use "#cql.ddl.keyspace.use")

## CREATE KEYSPACE

Use the `CREATE KEYSPACE` statement to create a new
keyspace.

Syntax

```
**create\_keyspace\_statement** ::=
    CREATE KEYSPACE [ IF NOT EXISTS ] *keyspace\_name*
    WITH *options*

```

Where:

- `*keyspace\_name*` is the
  name of the keyspace to be created.
- _options_ are one or more of the
  following:
  - `REPLICATION` – A map that indicates the
    replication strategy for the keyspace:
    - `SingleRegionStrategy` – For a
      single-Region keyspace. (Required)
    - `NetworkTopologyStrategy` – Specify
      at least two AWS Regions. The
      replication factor for each Region is three.
      (Optional)

  - `DURABLE_WRITES` – Writes to Amazon Keyspaces are always
    durable, so this option isn't required. However, if specified,
    the value must be `true`.
  - `TAGS` – A list of key-value pair tags to be
    attached to the resource when you create it. (Optional)

Example

Create a keyspace as follows.

```
CREATE KEYSPACE `my_keyspace`
    WITH REPLICATION = {'class': 'SingleRegionStrategy'} and TAGS ={'key1':'val1', 'key2':'val2'} ;

```

To create a multi-Region keyspace, specify
`NetworkTopologyStrategy` and include at least two AWS Regions.
The replication factor for each Region is three.

```
CREATE KEYSPACE `my_keyspace`
    WITH REPLICATION = {'class':'NetworkTopologyStrategy', 'us-east-1':'3', 'ap-southeast-1':'3','eu-west-1':'3'};
```

## ALTER KEYSPACE

You can use the `ALTER KEYSPACE WITH` statement for the following _options_

- `REPLICATION` – Use this option to add a new AWS Region replica to a keyspace. You can add a new
  Region to a single-Region or to a multi-Region keyspace.
- `TAGS` – Use this option to add or remove tags from a keyspace.

Syntax

```
**alter\_keyspace\_statement** ::=
    ALTER KEYSPACE *keyspace\_name*
    WITH *options*
```

Where:

- `*keyspace\_name*` is the
  name of the keyspace to be altered.
- _options_ are one of the following:
  - `ADD | DROP TAGS` – A list of key-value pair tags to be added or
    removed from the keyspace.
  - `REPLICATION` – A map that indicates the replication strategy for the keyspace;
    - `class`– `NetworkTopologyStrategy` defines the keyspace
      as a multi-Region keyspace.
    - `region`– Specify one
      additional AWS Region for this keyspace. The replication factor for each Region is three.
    - `CLIENT_SIDE_TIMESTAMPS` – The default is `DISABLED`. You can only
      change the status to `ENABLED`.

Examples

Alter a keyspace as shown in the following example to add tags.

```
ALTER KEYSPACE `my_keyspace` ADD TAGS {'key1':'val1', 'key2':'val2'};

```

To add a third Region to a multi-Region keyspace, you can use the following statement.

```
ALTER KEYSPACE `my_keyspace`
WITH REPLICATION = {
    'class': 'NetworkTopologyStrategy',
    'us-east-1': '3',
    'us-west-2': '3',
    'us-west-1': '3'
} AND CLIENT_SIDE_TIMESTAMPS = {'status': 'ENABLED'};
```

## DROP KEYSPACE

Use the `DROP KEYSPACE` statement to remove a
keyspace—including all of its contents, such as tables.

Syntax

```
**drop\_keyspace\_statement** ::=
    DROP KEYSPACE [ IF EXISTS ] *keyspace\_name*
```

Where:

- _keyspace_name_ is the name of the
  keyspace to be dropped.

Example

```
DROP KEYSPACE my_keyspace;
```

## USE

Use the `USE` statement to define the current keyspace. This allows you
to refer to objects bound to a specific keyspace, for example tables and types,
without using the fully qualified name that includes the keyspace prefix.

Syntax

```
**use\_statement** ::=
    USE *keyspace\_name*
```

Where:

- _keyspace_name_ is the name of the
  keyspace to be used.

Example

```
USE my_keyspace;
```
