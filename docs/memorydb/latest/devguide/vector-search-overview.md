# Vector search overview

Vector search is built on the creation, maintenance and use of indexes. Each vector search operation specifies a single index
and its operation is confined to that index, i.e., operations on one index are unaffected by operations on any other index.
Except for the operations to create and destroy indexes, any number of operations may be issued against any index at any time, meaning that at the cluster
level, multiple operations against multiple indexes may be in progress simultaneously.

Individual indexes are named objects that exist in a unique namespace, which is separate from the other Valkey and Redis OSS namespaces: keys, functions, etc. Each index is conceptually similar to a
conventional database table in that it’s structured in two dimensions: column and rows.
Each row in the table corresponds to a key. Each column in the index corresponds to a member or portion of that key.
Within this document the terms key, row and record are identical and used interchangeably.
Similarly the terms column, field, path and member are essentially identical and are also used interchangeably.

There are no special commands to add, delete or modify indexed data.
Rather the existing **HASH** or **JSON** commands that modify a key that is in an index also automatically update the index.

###### Topics

- [Indexes and the Valkey and Redis OSS keyspace](#vector-search-indexes-keyspaces "#vector-search-indexes-keyspaces")
- [Index field types](#vector-search-index-field-types "#vector-search-index-field-types")
- [Vector index algorithms](#vector-search-index-algorithms "#vector-search-index-algorithms")
- [Vector search query expression](#vector-search-query-expression "#vector-search-query-expression")
- [INFO command](#vector-search-ft.info "#vector-search-ft.info")
- [Vector search security](#vector-search-security "#vector-search-security")

## Indexes and the Valkey and Redis OSS keyspace

Indexes are constructed and maintained over a subset of the Valkey and Redis OSS keyspace. Multiple indexes may choose disjoint or overlapping subsets of the keyspace without limitation. The keyspace for each index is defined by a list of key prefixes that are provided when the index is created.
The list of prefixes is optional and if omitted, the entire keyspace will be part of that index.
Indexes are also typed in that they only cover keys that have a matching type. Currently, only JSON and HASH indexes are supported.
A HASH index only indexes HASH keys covered by its prefix list and similarly a JSON index only indexes JSON keys that are covered by its prefix list.
Keys within an index’s keyspace prefix list that do not have the designated type are ignored and do not affect search operations.

When a HASH or JSON command modifies a key that is within a keyspace of an index that index is updated. This process involves extracting
the declared fields for each index and updating the index with the new value. The update process is done in a background thread,
meaning that the indexes are only eventually consistent with their keyspace contents.
Thus an insert or update of a key will not be visible in search results for a short period of time. During periods of heavy system load and/or heavy mutation of data, the visibility delay can become longer.

The creation of an index is multi-step process. The first step is to execute the [FT.CREATE](vector-search-commands-ft.md "vector-search-commands-ft.md") command which defines the index.
Successful execution of a create automatically initiates the second step – backfilling. The backfill process runs in a background thread and scans the
key space for keys that are within the new index’s prefix list.
Each key that is found is added to the index. Eventually the entire keyspace is scanned, completing the index creation process.
Note that while the backfill process is running, mutations of indexed keys is permitted, there is no restriction and the index backfill process will not complete until all keys are properly indexed. Query operations attempted while an index is undergoing backfill are not allowed and are terminated with an error.
The completion of the backfilling process can be determined from the output of the `FT.INFO` command for that index ('backfill_status').

## Index field types

Each field (column) of an index has a specific type that is declared when the index is created and a location within a key. For HASH keys the location is the field name within the HASH.
For JSON keys the location is a JSON path description. When a key is modified the data associated with the declared fields is extracted, converted to the declared type and stored in the index.
If the data is missing or cannot be successfully converted to the declared type, then that field is omitted from the index. There are four types of fields, as explained following:

- **Number fields** contain a single number. For JSON fields, the numeric rules of JSON numbers must be followed. For HASH, the field is expected to contain the ASCII text of a number written in the standard format for fixed or floating point numbers. Regardless of the representation within the key, this field is converted to a 64-bit floating point number for storage within the index. Number fields can be used with the range search operator.
  Because the underlying numbers are stored in floating point with it’s precision limitations, the usual rules about numeric comparisons for floating point numbers apply.
- **Tag fields** contain zero or more tag values coded as a single UTF-8 string. The string is parsed into tag values using a separator character (default is a comma but can be overridden)
  with leading and trailing white space removed. Any number of tag values can be contained in a single tag field. Tag fields can be used to filter queries for tag value equivalence with either case-sensitive or case-insensitive comparison.
- **Text fields** contain a blob of bytes which need not be UTF-8 compliant. Text fields can be used to decorate query results with application-meaningful values. For example a URL or the contents of a document, etc.
- **Vector fields** contain a vector of numbers also known as an embedding. Vector fields support K-nearest neighbor searching (KNN) of fixed sized vectors
  using a specified algorithm and distance metric. For HASH indexes, the field should contain the entire vector encoded in binary format (_little-endian IEEE 754_).
  For JSON keys the path should reference an array of the correct size filled with numbers. Note that when a JSON array is used as a vector field, the internal representation of the
  array within the JSON key is converted into the format required by the selected algorithm, reducing memory consumption and precision. Subsequent read operations using the JSON commands will yield the reduced precision value.

## Vector index algorithms

Two vector index algorithms are provided:

- **Flat** – The Flat algorithm is a brute force linear processing of each vector in the index, yielding exact answers within the bounds of the precision of the distance computations.
  Because of the linear processing of the index, run times for this algorithm can be very high for large indexes.
- **HNSW (Hierarchical Navigable Small Worlds)** – The HNSW algorithm is an alternative that provides an approximation of the correct answer in exchange for substantially lower execution times.
  The algorithm is controlled by three parameters `M`, `EF_CONSTRUCTION` and `EF_RUNTIME`. The first two parameters are specified at index creation time and cannot be changed.
  The `EF_RUNTIME` parameter has a default value that is specified at index creation, but can be overridden on any individual query operation afterward.
  These three parameters interact to balance memory and CPU consumption during ingestion and query operations as well as control the quality of the approximation of an exact KNN search (known as recall ratio).

Both vector search algorithms (Flat and HNSW) support an optional `INITIAL_CAP` parameter. When specified, this parameter pre-allocates memory for the indexes, resulting in reduced memory management
overhead and increased vector ingestion rates.

Vector search algorithms like HNSW may not efficiently handle deleting or overwriting of previously inserted vectors. Use of these operations can result in excess index memory consumption and/or degraded recall quality.
Reindexing is one method for restoring optimal memory usage and/or recall.

## Vector search query expression

The [FT.SEARCH](vector-search-commands-ft.md "vector-search-commands-ft.md") and
[FT.AGGREGATE](vector-search-commands-ft.md "vector-search-commands-ft.md")
commands require a query expression. This expression is a single string parameter which is composed of one or more operators.
Each operator uses one field in the index to identify a subset of the keys in the index. Multiple operators may be combined using boolean
combiners as well as parentheses to further enhance or restrict the collected set of keys (or resultset).

### Wildcard

The wildcard operator, the asterisk (‘\*’), matches all keys in the index.

### Numeric range

The numeric range operator has the following syntax:

```
<range-search> ::= '@' <numeric-field-name> ':' '[' <bound> <bound> ']'
<bound>  ::= <number> | '(' <number>
<number> ::= <integer> | <fixed-point> | <floating-point> | 'Inf' | '-Inf' | '+Inf'
```

The <numeric-field-name> must be a declared field of type `NUMERIC`. By default the bound is inclusive but a
leading open parenthesis [‘(’] can be used to make a bound exclusive. Range search can be converted into a single relational comparison
(<, <=, >, >=) by using `Inf`, `+Inf` or `-Inf` as one of the bounds. Regardless of the numeric format specified (integer, fixed-point, floating-point, infinity) the number is converted to 64-bit floating point to perform comparisons, reducing precision accordingly.

###### Examples

```
@numeric-field:[0 10]                      // 0   <= <value> <= 10
@numeric-field:[(0 10]                     // 0   <  <value> <= 10
@numeric-field:[0 (10]                     // 0   <= <value> <  10
@numeric-field:[(0 (10]                    // 0   <  <value> <  10
@numeric-field:[1.5 (Inf]                  // 1.5 <= value
```

### Tag compare

The tag compare operator has the following syntax:

```
<tag-search> ::= '@' <tag-field-name> ':' '{' <tag> [ '|' <tag> ]* '}'
```

If any of the tags in the operator match any of the tags in the tag field of the record, then the record is included in the resultset.
The field designed by the `<tag-field-name>` must be a field of the index declared with type `TAG`. Examples of a tag compare are:

```
@tag-field:{ atag }
@tag-field: { tag1 | tag2 }
```

### Boolean combinations

The result sets of a numeric or tag operator can be combined using boolean logic: and/or. Parentheses can be used to group operators and/or change the evaluation order. The syntax of boolean logic operators is:

```
<expression> ::= <phrase> | <phrase> '|' <expression> | '(' <expression> ')'
<phrase> ::= <term> | <term> <phrase>
<term> ::= <range-search> | <tag-search> | '*'
```

Multiple terms combined into a phrase are "and"-ed. Multiple phrases combined with the pipe (‘|’) are “or”-ed.

### Vector search

Vector indexes support two different searching methods: nearest neighbor and range. A nearest neighbor search locates a number, K, of the vectors in the index that are closest to the provided (reference) vector — this is colloquially called KNN for ‘K’ nearest neighbors. The syntax for a KNN search is:

```
<vector-knn-search> ::= <expression> '=>[KNN' <k> '@' <vector-field-name> '$' <parameter-name> <modifiers> ']'
<modifiers> ::= [ 'EF_RUNTIME' <integer> ] [ 'AS' <distance-field-name>]
```

A vector KNN search is only applied to the vectors that satisfy the `<expression>` which can be any combination of the operators defined above: wildcard, range search, tag search and/or boolean combinations thereof.

- `<k>` is an integer specifying the number of nearest neighbor vectors to be returned.
- `<vector-field-name>` must specify a declared field of type `VECTOR`.
- `<parameter-name>` field specifies one of the entries for the
  `PARAM` table of the `FT.SEARCH` or `FT.AGGREGATE` command.
  This parameter is the reference vector value for distance computations. The value of the vector is encoded into the `PARAM` value in _little-endian IEEE 754_ binary format (same encoded as for a HASH vector field)
- For vector indexes of type HNSW, the optional `EF_RUNTIME` clause can be used to override the default value of the `EF_RUNTIME` parameter that was
  established when the index was created.
- The optional `<distance-field-name>` provides a field name for the resultset to contain the computed distance between
  the reference vector and the located key.

A range search locates all vectors within a specified distance (radius) from a reference vector. The syntax for a range search is:

```
<vector-range-search> ::= ‘@’ <vector-field-name> ‘:’ ‘[’ ‘VECTOR_RANGE’ ( <radius> | ‘$’ <radius-parameter> )  $<reference-vector-parameter> ‘]’ [ ‘=’ ‘>’ ‘{’ <modifiers> ‘}’ ]
<modifiers> ::= <modifier> | <modifiers>, <modifier>
<modifer> ::= [ ‘$yield_distance_as’ ‘:’ <distance-field-name> ] [ ‘$epsilon’ ‘:’ <epsilon-value> ]
```

Where:

- `<vector-field-name>`is the name of the vector field to be searched.
- `<radius> or $<radius-parameter>` is the numerical distance limit for search.
- `$<reference-vector-parameter>` is the name of the parameter that contains the reference vector. The value of the vector is encoded into the PARAM value in little-endian IEEE 754 binary format (same encoding as for a HASH vector field)
- The optional `<distance-field-name>` provides a field name for the resultset to contain the computed distance between the reference vector and each key.
- The optional `<epsilon-value>` controls the boundary of the search
  operation, vectors within the distance `<radius> * (1.0 +
<epsilon-value>)` are traversed looking for candidate
  results. The default is .01.

## INFO command

Vector search augments the Valkey and Redis OSS [INFO](https://valkey.io/commands/info/ "https://valkey.io/commands/info/") command with several additional sections of statistics and counters. A request to retrieve the section `SEARCH` will retrieve all
of the following sections:

### `search_memory` section

| Name                     | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| search_used_memory_bytes | Number of bytes of memory consumed in all search data structures |
| search_used_memory_human | Human readable version of above                                  |

### `search_index_stats` section

| Name                             | Description                                        |
| -------------------------------- | -------------------------------------------------- |
| search_number_of_indexes         | Number of created indexes                          |
| search_num_fulltext_indexes      | Number of non-vector fields in all indexes         |
| search_num_vector_indexes        | Number of vector fields in all indexes             |
| search_num_hash_indexes          | Number of indexes on HASH type keys                |
| search_num_json_indexes          | Number of indexes on JSON type keys                |
| search_total_indexed_keys        | Total number of keys in all indexes                |
| search_total_indexed_vectors     | Total number of vectors in all indexes             |
| search_total_indexed_hash_keys   | Total number of keys of type HASH in all indexes   |
| search_total_indexed_json_keys   | Total number of keys of tytpe JSON in all indexes  |
| search_total_index_size          | Bytes used by all indexes                          |
| search_total_fulltext_index_size | Bytes used by non-vector index structures          |
| search_total_vector_index_size   | Bytes used by vector index structures              |
| search_max_index_lag_ms          | Ingestion delay during last ingestion batch update |

### `search_ingestion` section

| Name                              | Description                                                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| search_background_indexing_status | Status of ingestion. `NO_ACTIVITY` means idle. Other values indicate there are keys in the process of being ingested. |
| search_ingestion_paused           | Except while restarting, this should always be "no".                                                                  |

### `search_backfill` section

###### Note

Some of the fields documented in this section are only visible when a backfill is currently in progress.

| Name                                        | Description                                            |
| ------------------------------------------- | ------------------------------------------------------ |
| search_num_active_backfills                 | Number of current backfill activities                  |
| search_backfills_paused                     | Except when out of memory, this should always be "no". |
| search_current_backfill_progress_percentage | % completion (0-100) of the current backfill           |

### `search_query` section

| Name                      | Description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| search_num_active_queries | Number of `FT.SEARCH` and `FT.AGGREGATE` commands currently in progress |

## Vector search security

[ACL (Access Control Lists)](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/") security mechanisms for both command and data access are extended to control the search facility.
ACL control of individual search commands is fully supported. A new ACL category, `@search`, is provided and many of the existing categories (`@fast`, `@read`, `@write`, etc.)
are updated to include the new commands. Search commands do not modify key data, meaning that the existing ACL machinery for write access is preserved. The access rules for HASH and JSON operations are not modified
by the presence of an index; normal key-level access control is still applied to those commands.

Search commands with an index also have their access controlled through ACL. Access checks are performed at the whole-index level, not at the per-key level.
This means that access to an index is granted to a user only if that user has permission to access all possible keys within the keyspace prefix list of that index.
In other words, the actual contents of an index don’t control the access. Rather, it is the theoretical contents of an index as defined by the prefix list which is used for the security check.
It can be easy to create a situation where a user has read and/or write access to a key but is unable to access an index containing that key.
Note that only read access to the keyspace is required to create or use an index – the presence or absence of write access is not considered.

For more information on using ACLs with MemoryDB see [Authenticating users with Access Control Lists (ACLs)](clusters.md "clusters.md").
