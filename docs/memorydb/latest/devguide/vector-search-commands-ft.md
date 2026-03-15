# FT.INFO

**Syntax**

```
FT.INFO <index-name>
```

Output from the FT.INFO page is an array of key value pairs as described in the following table:

| Key                 | Value type                 | Description                                        |
| ------------------- | -------------------------- | -------------------------------------------------- |
| index_name          | string                     | Name of the index                                  |
| creation_timestamp  | integer                    | Unix-style timestamp of creation time              |
| key_type            | string                     | HASH or JSON                                       |
| key_prefixes        | array of strings           | Key prefixes for this index                        |
| fields              | array of field information | Fields of this index                               |
| space_usage         | integer                    | Memory bytes used by this index                    |
| fullext_space_usage | integer                    | Memory bytes used by non-vector fields             |
| vector_space_usage  | integer                    | Memory bytes used by vector fields                 |
| num_docs            | integer                    | Number of keys currently contained in the index    |
| num_indexed_vectors | integer                    | Number of vectors currently contained in the index |
| current_lag         | integer                    | Recent delay of ingestion (milliSeconds)           |
| backfill_status     | string                     | One of: Completed, InProgres, Paused or Failed     |

The following table describes the information for each field:

| Key        | Value type | Description                          |
| ---------- | ---------- | ------------------------------------ |
| identifier | string     | name of field                        |
| field_name | string     | Hash member name or JSON Path        |
| type       | string     | one of: Numeric, Tag, Text or Vector |
| option     | string     | ignore                               |

If the field is of type Vector, additional information will be present depending on the algorithm.

For the HNSW algorithm:

| Key              | Value type | Description                           |
| ---------------- | ---------- | ------------------------------------- |
| algorithm        | string     | HNSW                                  |
| data_type        | string     | FLOAT32                               |
| distance_metric  | string     | one of: L2, IP or Cosine              |
| initial_capacity | integer    | Initial size of vector field index    |
| current_capacity | integer    | Current size of vector field index    |
| maximum_edges    | integer    | M parameter at creation               |
| ef_construction  | integer    | EF_CONSTRUCTION parameter at creation |
| ef_runtime       | integer    | EF_RUNTIME parameter at creation      |

For the FLAT algorithm:

| Key              | Value type | Description                        |
| ---------------- | ---------- | ---------------------------------- |
| algorithm        | string     | FLAT                               |
| data_type        | string     | FLOAT32                            |
| distance_metric  | string     | one of: L2, IP or Cosine           |
| initial_capacity | integer    | Initial size of vector field index |
| current_capacity | integer    | Current size of vector field index |
