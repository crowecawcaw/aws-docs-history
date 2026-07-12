# Understanding CDC records

Aurora DSQL CDC delivers each change as a JSON record. The record uses an envelope structure
with operation type, before and after row images, and source metadata.

## How records map to Amazon Kinesis

Aurora DSQL writes each CDC record as a single Kinesis record. The Kinesis record's
`Data` field contains the JSON payload. Aurora DSQL uses a randomized Kinesis
partition key to distribute CDC records evenly across shards. To read all changes, consume
all shards on the Kinesis data stream. If a record exceeds the Kinesis record size limit,
Aurora DSQL splits it across multiple Kinesis records. For details, see
[Handling oversized records](#cdc-oversized-records "#cdc-oversized-records").

###### Note

A Kinesis record has one `Data` blob. The primary key values appear in
the JSON payload's `before` field for deletes, or the `after`
field for inserts and updates. To extract the primary key for downstream processing, read
it from the appropriate field in the payload.

## Primary key in the payload

For tables with a primary key, the primary key column values appear in the payload:

- For **inserts** and
  **updates**, the payload includes the primary key columns
  along with all other columns in the `after` field.
- For **deletes**, the primary key columns appear in the
  `before` field.

For example, consider a table with a composite primary key:

```
CREATE TABLE order_items (
    order_id INT,
    item_id INT,
    quantity INT,
    price NUMERIC,
    PRIMARY KEY (order_id, item_id)
);
```

A delete on this table produces a payload where
`"before": {"order_id": 1001, "item_id": 42}`.

## Record payload

The payload uses the following JSON envelope format.

###### INSERT example

The following example shows a CDC record for an `INSERT` operation:

```
{
    "type": "full",
    "op": "c",
    "before": null,
    "after": {"order_id": 1001, "item_id": 42, "quantity": 5, "price": "29.99"},
    "source": {
        "version": "1.0",
        "ts_ms": 1705318200000,
        "ts_ns": 1705318200000000000,
        "txId": "ffthunp5stx6ffs2vyfqoatmfu",
        "schema": "public",
        "table": "order_items",
        "db": "postgres",
        "cluster": "kmabugltfmjdaj2siqr2qbxgju"
    },
    "ts_ms": 1705318200125,
    "ts_ns": 1705318200125483291
}
```

###### UPDATE example

The following example shows a CDC record for an `UPDATE` operation:

```
{
    "type": "full",
    "op": "u",
    "before": null,
    "after": {"order_id": 1001, "item_id": 42, "quantity": 10, "price": "29.99"},
    "source": {
        "version": "1.0",
        "ts_ms": 1705318300000,
        "ts_ns": 1705318300000000000,
        "txId": "qvtiesgmd55cvlfukm3dfuotji",
        "schema": "public",
        "table": "order_items",
        "db": "postgres",
        "cluster": "kmabugltfmjdaj2siqr2qbxgju"
    },
    "ts_ms": 1705318300125,
    "ts_ns": 1705318300125483291
}
```

###### DELETE example

For a `DELETE` on a table with a primary key, the `before` field
contains the primary key values:

```
{
    "type": "full",
    "op": "d",
    "before": {"order_id": 1001, "item_id": 42},
    "after": null,
    "source": {
        "version": "1.0",
        "ts_ms": 1705318400000,
        "ts_ns": 1705318400000000000,
        "txId": "xyzabc123def456ghi789jklmno",
        "schema": "public",
        "table": "order_items",
        "db": "postgres",
        "cluster": "kmabugltfmjdaj2siqr2qbxgju"
    },
    "ts_ms": 1705318400125,
    "ts_ns": 1705318400125483291
}
```

## Payload fields

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`           | The record type. `full` for a complete record that includes inline<br>`before` and `after` values. `chunked` for a main<br>record that references fragment records for one or both images. `fragment`<br>for an individual piece of a chunked image. For details, see<br>[Handling oversized records](#cdc-oversized-records "#cdc-oversized-records").                                                                                           |
| `op`             | Operation type. `c` = create (insert), `u` = update,<br>`d` = delete. The `op` reflects the row's net effect<br>across the transaction: a row that didn't exist before the transaction receives<br>`c`, a pre-existing row that the transaction modified receives<br>`u`, and a pre-existing row that the transaction removed receives<br>`d`. For details, see<br>[Write-set compaction](#cdc-write-set-compaction "#cdc-write-set-compaction"). |
| `before`         | For deletes on tables with a primary key, contains the primary key values of the<br>deleted row. Aurora DSQL sets this field to `null` for inserts, updates, and<br>deletes on tables without a primary key.                                                                                                                                                                                                                                      |
| `after`          | The full row state after the change, including all columns. Aurora DSQL sets this field<br>to `null` for deletes.                                                                                                                                                                                                                                                                                                                                 |
| `chunked`        | Present only when `type` is `chunked`. Contains reassembly<br>metadata for the `before` image, the `after` image, or both.<br>Aurora DSQL omits the chunked image from the top-level `before` or<br>`after` field and places it under `chunked` instead. For<br>details, see [Handling oversized records](#cdc-oversized-records "#cdc-oversized-records").                                                                                       |
| `source.version` | The CDC source metadata format version. The current version is<br>`1.0`.                                                                                                                                                                                                                                                                                                                                                                          |
| `source.ts_ms`   | The transaction commit timestamp in milliseconds since the Unix epoch, Coordinated<br>Universal Time (UTC).                                                                                                                                                                                                                                                                                                                                       |
| `source.ts_ns`   | Transaction commit timestamp in nanoseconds, UTC. The highest precision timestamp<br>available. Use this field to establish a total order of transactions.                                                                                                                                                                                                                                                                                        |
| `source.txId`    | A unique transaction identifier, encoded as base32. All records from the same<br>transaction share the same `txId` value. Use this field to group records<br>that belong to the same transaction.                                                                                                                                                                                                                                                 |
| `source.schema`  | The PostgreSQL schema name (for example, `public`).                                                                                                                                                                                                                                                                                                                                                                                               |
| `source.table`   | The table name.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `source.db`      | The database name. Always `postgres` for Aurora DSQL.                                                                                                                                                                                                                                                                                                                                                                                             |
| `source.cluster` | The Aurora DSQL cluster identifier.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ts_ms`          | The time at which the CDC system processed the record, in milliseconds, UTC. The<br>difference between `ts_ms` and `source.ts_ms` is a measure of<br>replication lag.                                                                                                                                                                                                                                                                             |
| `ts_ns`          | The time at which the CDC system processed the record, in nanoseconds, UTC.                                                                                                                                                                                                                                                                                                                                                                       |

## Format details

The following details describe how Aurora DSQL CDC formats records. Design your app to
handle these behaviors.

- **Full after-image for inserts and updates.** Aurora DSQL
  includes the complete row state in the `after` field for all writes. The
  `before` field is `null` for inserts and updates. Aurora DSQL emits
  `op: "c"` for inserts and `op: "u"` for updates.
- **Write-set compaction.** Aurora DSQL compacts the write set
  of each transaction before publishing, emitting at most one record per row. For details and
  examples, see [Write-set compaction](#cdc-write-set-compaction "#cdc-write-set-compaction").
- **Post-change row state only.** CDC records include the
  full row state after each change. The state of the row before an update isn't
  included. For deletes on tables with a primary key, the `before` field
  contains the primary key values.
- **Numeric types serialized as strings.** Aurora DSQL
  serializes `numeric` and `decimal` values as JSON strings to
  preserve exact precision.
- **Binary data encoded as Base64.** Aurora DSQL encodes
  `bytea` values as Base64 strings.
- **Special floating-point and numeric values.** Aurora DSQL
  serializes NaN and ±Infinity as the strings `"NaN"`,
  `"Infinity"`, and `"-Infinity"`. This applies to
  `real`, `double precision`, and `numeric` types.
- **JSON columns serialized as JSON strings.** Aurora DSQL
  serializes `json` column values as JSON strings that contain the raw JSON text
  stored in the column. Parse the string value in your app (for example, with
  `JSON.parse` in JavaScript or `json.loads` in Python) to access the
  underlying JSON value.
- **Overflow values emitted as null.** If a value
  can't be represented in the target JSON type during serialization, Aurora DSQL emits
  JSON `null` for that column. This applies to `interval` values
  whose total microseconds exceed the 64-bit signed integer range
  (±9,223,372,036,854,775,807 microseconds, approximately ±292,271 years).
  Design your app to handle unexpected `null` values in columns that aren't
  nullable in the database schema.
- **Oversized records split into chunks.** If a record
  exceeds the Amazon Kinesis record size limit, Aurora DSQL splits the affected
  `before` or `after` image into fragments and delivers them as
  separate Kinesis records so you still receive the change. Design your app to reassemble
  the images. For details, see
  [Handling oversized records](#cdc-oversized-records "#cdc-oversized-records").

## Write-set compaction

Aurora DSQL compacts the write set of each committed transaction before publishing CDC
records. Aurora DSQL compares each row's state before the transaction to its state after,
and emits at most one record per row reflecting the net effect.

### Compaction rules

Aurora DSQL determines the `op` code based on the row's net state
change:

**`op: "c"` (create)**
The row is new. It didn't exist before the transaction and exists
after. The `after` field contains the final row state.

**`op: "u"` (update)**
The row existed before the transaction and still exists after. The
`after` field contains the final row state. Aurora DSQL compacts operations, not
row content.

**`op: "d"` (delete)**
The row existed before the transaction and doesn't exist after. The
`before` field contains only the primary key values.

**No record**
The row didn't exist before the transaction and doesn't exist
after (for example, an insert followed by a delete in the same transaction). Aurora DSQL
recognizes zero net change and doesn't publish a record.

## Handling oversized records

When a CDC record's serialized JSON exceeds 9 MiB, Aurora DSQL splits the
`before` and/or `after` images, delivering multiple Kinesis records.
Each record contains a top-level `type` field that indicates its structure:
`full` for a complete record, `chunked` for a main record that
references fragments, and `fragment` for an individual piece of a chunked
image. The `op`, `source`, `ts_ms`, and
`ts_ns` fields on a chunked main record behave the same as on a full record.
Records that fit in a single Kinesis record have `type` set to
`full` and don't require any extra handling.

A `chunk_id` is stable across retries. If Aurora DSQL redelivers a fragment,
it carries the same `chunk_id` as the original delivery, so your app can
continue buffering under the same identifier without handling partial sets from previous
attempts.

###### Main record

A chunked main record replaces the top-level `before` or
`after` field for the split image with a `chunked` object that
describes how to reassemble it. Each entry under `chunked` has
a `chunk_id` (the identifier that links fragments to this record),
`total_fragments` (the number of fragments that make up that image), and
`crc32c` (a CRC32C checksum, as a decimal string, over the reassembled image
text). If one image is inline and the other is chunked, the inline image still
appears at the top level as either a value or `null`.

```
{
    "type": "chunked",
    "op": "c",
    "before": null,
    "after": null,
    "source": {
        "version": "1.0",
        "ts_ms": 1705318200000,
        "ts_ns": 1705318200000000000,
        "txId": "ffthunp5stx6ffs2vyfqoatmfu",
        "schema": "public",
        "table": "order_items",
        "db": "postgres",
        "cluster": "`cluster-id`"
    },
    "chunked": {
        "after": {
            "chunk_id": "`chunk-id`",
            "total_fragments": 3,
            "crc32c": "2073618257"
        }
    },
    "ts_ms": 1705318200125,
    "ts_ns": 1705318200125483291
}
```

###### Fragment record

Each fragment is its own Kinesis record with `type` set to
`fragment` and three fields: `chunk_id` matches the value in
the corresponding `chunked.before.chunk_id` or
`chunked.after.chunk_id` on the main record, `index` is the
zero-based position of the fragment within the image, and `data` is a
segment of the image's JSON text split on UTF-8 character boundaries (each
fragment's `data` value is a valid UTF-8 string on its own). Because
Aurora DSQL CDC uses `UNORDERED` mode and randomized partition keys, fragments
and the main record can arrive on different shards and in any order. To read all
fragments, consume all shards on the Kinesis data stream. For more information about
delivery ordering, see [Ordering](cdc-streams.md#cdc-ordering "cdc-streams.md#cdc-ordering").

```
{
    "type": "fragment",
    "chunk_id": "`chunk-id`",
    "index": 0,
    "data": "`partial-JSON-text`"
}
```

To reassemble an oversized image, buffer each record with `type`
`fragment` by its `chunk_id`. When you receive a main record with
`type` `chunked`, wait until you have
`total_fragments` fragments for each `chunk_id` referenced under
`chunked.before` or `chunked.after`, sort the fragments by
`index` ascending, and concatenate the `data` strings. The
concatenated result is the original `before` or `after` object as
JSON text—parse it to access the column values. To verify delivery integrity,
compute CRC32C over the concatenated string and compare the result to
`chunked.before.crc32c` or `chunked.after.crc32c`.

## Data type serialization

The following tables describe how Aurora DSQL serializes each PostgreSQL data type in CDC
records.

### Integer types

| PostgreSQL type     | JSON representation    | Example               |
| ------------------- | ---------------------- | --------------------- |
| `smallint` (`int2`) | JSON number            | `42`                  |
| `integer` (`int4`)  | JSON number            | `1001`                |
| `bigint` (`int8`)   | JSON number            | `9223372036854775807` |
| `oid`               | JSON number (unsigned) | `16384`               |

Values of `bigint` beyond ±2^53 might lose precision in JavaScript
environments. Use BigInt or arbitrary-precision libraries in those cases.

### Floating-point types

| PostgreSQL type               | JSON representation | Example             | Notes                                                                                                                                    |
| ----------------------------- | ------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `real` (`float4`)             | JSON number         | `3.14159`           | NaN and ±Infinity are serialized as the strings `"NaN"`,<br>`"Infinity"`, `"-Infinity"`.                                                 |
| `double precision` (`float8`) | JSON number         | `3.141592653589793` | Same special value handling as `real`.                                                                                                   |
| `numeric` / `decimal`         | JSON string         | `"123.45"`          | Always a string to preserve exact precision. NaN and ±Infinity are serialized<br>as the strings `"NaN"`, `"Infinity"`,<br>`"-Infinity"`. |

### Boolean

| PostgreSQL type | JSON representation | Example           |
| --------------- | ------------------- | ----------------- |
| `boolean`       | JSON boolean        | `true` or `false` |

### Character types

| PostgreSQL type        | JSON representation | Example                            |
| ---------------------- | ------------------- | ---------------------------------- |
| `varchar` / `text`     | JSON string         | `"Hello, world!"`                  |
| `bpchar` (`char(n)`)   | JSON string         | `"ABC"` (trailing spaces stripped) |
| `name`                 | JSON string         | `"pg_class"`                       |
| `"char"` (single-byte) | JSON string         | `"A"`                              |

### Binary

| PostgreSQL type | JSON representation  | Example              |
| --------------- | -------------------- | -------------------- |
| `bytea`         | JSON string (Base64) | `"SGVsbG8gV29ybGQh"` |

### Date and time types

| PostgreSQL type | JSON representation                            | Example            | Notes                                                                                                                                                                                                                                                                                                                                             |
| --------------- | ---------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date`          | JSON number (days since Unix epoch)            | `19797`            | `+infinity` and `-infinity` are represented as sentinel day<br>counts derived from epoch-offset arithmetic. These values don't correspond to<br>meaningful calendar dates.                                                                                                                                                                        |
| `time`          | JSON number (microseconds since midnight)      | `52200123456`      |                                                                                                                                                                                                                                                                                                                                                   |
| `timetz`        | JSON number (microseconds since midnight, UTC) | `52200123456`      | The local time is adjusted to UTC by applying the stored timezone offset (seconds west<br>of UTC). The result is wrapped to the range [0, 86400000000) microseconds.                                                                                                                                                                              |
| `timestamp`     | JSON number (microseconds since Unix epoch)    | `1710510600123456` | ±Infinity maps to sentinel values: `9223372036825200000`<br>for `+infinity` and `-9223372036832400000` for<br>`-infinity`.                                                                                                                                                                                                                        |
| `timestamptz`   | JSON number (microseconds since Unix epoch)    | `1710510600123456` | Stored and emitted in UTC. Same ±infinity sentinel values as<br>`timestamp`.                                                                                                                                                                                                                                                                      |
| `interval`      | JSON number (approximate total microseconds)   | `2802603000000`    | Months are approximated as 30.4375 days (2,629,800 seconds). The total is<br>computed as `(months × 2,629,800 + days × 86,400) ×<br>1,000,000 + microseconds`. If the result exceeds the 64-bit signed integer<br>range (±9,223,372,036,854,775,807 microseconds, approximately<br>±292,271 years), Aurora DSQL emits JSON `null` for the column. |

### Other types

| PostgreSQL type | JSON representation                          | Example                                  |
| --------------- | -------------------------------------------- | ---------------------------------------- |
| `uuid`          | JSON string (standard 8-4-4-4-12 hex format) | `"550e8400-e29b-41d4-a716-446655440000"` |
| `oidvector`     | JSON empty array                             | `[]`                                     |
| `json`          | JSON string containing the raw JSON text     | `"{\"key\": \"value\"}"`                 |

### NULL values

For any data type, `NULL` column values are represented as JSON
`null`.

## Schema evolution in CDC records

When you modify a table's schema—for example, by adding, dropping, or
renaming a column—CDC records reflect the change starting from the transaction that
committed the DDL change. Records from transactions committed before the DDL change use the
previous schema. For example:

- If you add a column, records from earlier transactions don't include the new
  column. Records from the adding transaction onward include the new column.
- If you drop a column, records from the dropping transaction onward no longer include
  that column.
- If you rename a column, records from the renaming transaction onward use the new
  column name.

Track schema changes in your downstream consumer by inspecting the column names
present in each record's `after` and `before` fields. The
`source.version` field in each record identifies the CDC envelope format.
