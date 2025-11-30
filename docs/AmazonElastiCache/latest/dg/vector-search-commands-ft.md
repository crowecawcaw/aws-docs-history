# FT.INFO

**Syntax**

```
FT.INFO <index-name>
```

Vector search augments the [FT.INFO](https://valkey.io/commands/info/ "https://valkey.io/commands/info/") command with several additional sections of statistics and counters. A request to retrieve the section SEARCH will retrieve all of the following statistics:

| Key name                     | Value type                     | Description                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| index_name                   | string                         | Name of the index                                                                                                                                                                                                                                                                                      |
| index_options                | string                         | Reserved. Currently set to "0"                                                                                                                                                                                                                                                                         |
| index_definition             | array                          | See below for definition of these array elements.                                                                                                                                                                                                                                                      |
| attributes                   | array of attribute information | One element in this array for each defined attribute, see below for attribute information definition.                                                                                                                                                                                                  |
| num_docs                     | integer                        | Number of keys currently contained in the index                                                                                                                                                                                                                                                        |
| num_terms                    | integer                        | Reserved. Currently set to "0".                                                                                                                                                                                                                                                                        |
| record_count                 | integer                        | The sum of the "size" field for each attribute.                                                                                                                                                                                                                                                        |
| hash_indexing_failures       | integer                        | Number of times that an attribute couldn't be converted to the declared attribute type. Despite the name this also applies to JSON keys.                                                                                                                                                               |
| backfill_in_progress         | integer                        | If a backfill is currently in progress this will be a '1' otherwise it will be a '0'                                                                                                                                                                                                                   |
| backfill_percent_complete    | float                          | Estimate of backfill completion, a fractional number in the range [0..1]                                                                                                                                                                                                                               |
| mutation_queue_size          | integer                        | Number of keys waiting to update the index.                                                                                                                                                                                                                                                            |
| recent_mutations_queue_delay | integer                        | Estimate of delay (in seconds) of index update. 0 if no updates are in progress.                                                                                                                                                                                                                       |
| state                        | string                         | Backfill state: "ready" indicates that backfill completed successfully. "backfill_in_progress" indicates that backfill is proceeding. "backfill_paused_by_oom" means that backfilling has been paused due to a low memory condition. Once the low memory condition is resolved, backill will continue. |

The index_definition structure is an array of key/value pairs defined as:

| Key name      | Value type | Description                                                                                                                                           |
| ------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| key_type      | string     | Either the string 'JSON' or the string 'HASH'                                                                                                         |
| prefixes      | array      | Each element in the array is a defined prefix for the index. If no prefixes were specified when the index was create, this array will have 0 entries. |
| default_score | string     | Reserved. Currently set to "1"                                                                                                                        |

Attribute information: Attribute information is type-specific.

Numeric attributes:

| Key        | Value type | Description                                                           |
| ---------- | ---------- | --------------------------------------------------------------------- |
| identifier | string     | Location of the attribute within a key. Hash member name or JSON path |
| alias      | string     | Name of attribute used in query descriptions.                         |
| type       | string     | The string "NUMERIC"                                                  |
| size       | integer    | The number of keys with valid numeric values in this attribute.       |

Tag attributes:

| Key name      | Value type | Description                                                                                         |
| ------------- | ---------- | --------------------------------------------------------------------------------------------------- |
| identifier    | string     | Location of the attribute within a key. Hash member name or JSON path                               |
| alias         | string     | Name of attribute used in query descriptions.                                                       |
| type          | string     | The string "TAG"                                                                                    |
| SEPARATOR     | character  | The separator character defined when the index was created                                          |
| CASESENSITIVE | n/a        | This key has no associated value. It is present only if the attribute was created with this option. |
| size          | integer    | The number of keys with valid tag values in this attribute                                          |

Vector attributes:

| Key name   | Value type | Description                                                           |
| ---------- | ---------- | --------------------------------------------------------------------- |
| identifier | string     | Location of the attribute within a key. Hash member name or JSON path |
| alias      | string     | Name of attribute used in query descriptions.                         |
| type       | string     | The string "VECTOR"                                                   |
| index      | character  | For further description of vector index, see below.                   |

Vector index description:

| Key name        | Value type | Description                                               |
| --------------- | ---------- | --------------------------------------------------------- |
| capacity        | string     | Current capacity of index                                 |
| dimensions      | string     | Number of elements in each vector                         |
| distance_metric | string     | One of "COSINE", "L2" or "IP"                             |
| size            | array      | Description of vector index, see below.                   |
| data_type       | string     | Declared datatype. Only "FLOAT32" is currently supported. |
| algorithm       | array      | Further description of the vector search algorithm.       |

FLAT Vector search algorithm Description:

| Key name   | Value type | Description                        |
| ---------- | ---------- | ---------------------------------- |
| name       | string     | Algorithm name: FLAT               |
| block_size | number     | Size of a block of the FLAT index. |

HNSW Vector Index Description:

| Key name        | Value type | Description                              |
| --------------- | ---------- | ---------------------------------------- |
| name            | string     | Algorithm name: HNSW                     |
| m               | number     | The "M" parameter for HNSW               |
| ef_construction | number     | The "ef_construction" parameter for HNSW |
| ef_runtime      | number     | The "ef_runtime" parameter for HNSW.     |
