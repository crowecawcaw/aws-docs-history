# INSERT

Use the `INSERT` statement to add a row to a table.

Syntax

```
**insert\_statement** ::=  INSERT INTO table_name ( names_values | json_clause )
                      [ IF NOT EXISTS ]
                      [ USING update_parameter ( AND update_parameter )* ]
**names\_values**     ::=  names VALUES tuple_literal
**json\_clause**      ::=  JSON string [ DEFAULT ( NULL | UNSET ) ]
**names**            ::=  '(' column_name ( ',' column_name )* ')'


```

Example

```
INSERT INTO "myGSGKeyspace".employees_tbl (id, name, project, region, division, role, pay_scale, vacation_hrs, manager_id)
VALUES ('012-34-5678','Russ','NightFlight','US','Engineering','IC',3,12.5, '234-56-7890') ;
```

Update parameters

`INSERT` supports the following values as
`update_parameter`:

- `TTL` – A time value in seconds. The maximum configurable value is 630,720,000 seconds, which is the equivalent of 20 years.
- `TIMESTAMP` – A `bigint` value representing the number of microseconds since the standard base time
  known as the epoch: January 1 1970 at 00:00:00 GMT.
  A timestamp in Amazon Keyspaces has to fall between the range of 2 days in the past and 5 minutes in the future.
  Example

```
INSERT INTO `my_table` (userid, time, subject, body, user)
        VALUES (B79CB3BA-745E-5D9A-8903-4A02327A7E09, 96a29100-5e25-11ec-90d7-b5d91eceda0a, 'Message', 'Hello','205.212.123.123')
        USING TTL 259200;
```

JSON support

For a table that maps JSON-encoded data types to Amazon Keyspaces data types, see [JSON encoding of Amazon Keyspaces data types](cql.md#cql.data-types.JSON "cql.md#cql.data-types.JSON").

You can use the `JSON` keyword to insert a `JSON`-encoded
map as a single row. For columns that exist in the table but are omitted in the JSON
insert statement, use `DEFAULT UNSET` to preserve the existing values.
Use `DEFAULT NULL` to write a NULL value into each row of omitted columns
and overwrite the existing values (standard write charges apply). `DEFAULT
 NULL` is the default option.

Example

```
INSERT INTO "myGSGKeyspace".employees_tbl JSON '{"id":"012-34-5678",
                                                 "name": "Russ",
                                                 "project": "NightFlight",
                                                 "region": "US",
                                                 "division": "Engineering",
                                                 "role": "IC",
                                                 "pay_scale": 3,
                                                 "vacation_hrs": 12.5,
                                                 "manager_id": "234-56-7890"}';
```

If the JSON data contains duplicate keys, Amazon Keyspaces stores the last value for the key
(similar to Apache Cassandra). In the following example, where the duplicate key is
`id`, the value `234-56-7890` is used.

Example

```
INSERT INTO "myGSGKeyspace".employees_tbl JSON '{"id":"012-34-5678",
                                                 "name": "Russ",
                                                 "project": "NightFlight",
                                                 "region": "US",
                                                 "division": "Engineering",
                                                 "role": "IC",
                                                 "pay_scale": 3,
                                                 "vacation_hrs": 12.5,
                                                 "id": "234-56-7890"}';
```
