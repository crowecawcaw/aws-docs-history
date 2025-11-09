# Handling

sequences in active-active replication

An RDS for PostgreSQL DB instance with the `pgactive` extension uses two different
sequence mechanisms to generate unique values.

###### Global Sequences

To use a global sequence, create a local sequence with the `CREATE SEQUENCE`
statement. Use `pgactive.pgactive_snowflake_id_nextval(seqname)` instead of
`usingnextval(seqname)` to get the next unique value of the sequence.

The following example creates a global sequence:

```
`app=>` CREATE TABLE gstest (
      id bigint primary key,
      parrot text
    );
```

```
`app=>`CREATE SEQUENCE gstest_id_seq OWNED BY gstest.id;
```

```
`app=>` ALTER TABLE gstest \
      ALTER COLUMN id SET DEFAULT \
      pgactive.pgactive_snowflake_id_nextval('gstest_id_seq');
```

###### Partitioned sequences

In split-step or partitioned sequences, a normal PostgreSQL sequence is used on each
node. Each sequence increments by the same amount and starts at different offsets. For
example, with step 100, the node 1 generates sequence as 101, 201, 301, and so on and the
node 2 generates sequence as 102, 202, 302, and so on. This scheme works well even if the
nodes can't communicate for extended periods, but requires that the designer specify a
maximum number of nodes when establishing the schema and requires per-node configuration.
Mistakes can easily lead to overlapping sequences.

It is relatively simple to configure this approach with `pgactive` by creating
the desired sequence on a node as follows:

```

CREATE TABLE some_table (generated_value bigint primary key);
```

```
`app=>` CREATE SEQUENCE some_seq INCREMENT 100 OWNED BY some_table.generated_value;
```

```
`app=>` ALTER TABLE some_table ALTER COLUMN generated_value SET DEFAULT nextval('some_seq');

```

Then call `setval` on each node to give a different offset starting value as
follows.

```
`app=>`
-- On node 1
SELECT setval('some_seq', 1);

-- On node 2
SELECT setval('some_seq', 2);

```
