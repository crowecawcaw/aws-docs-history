# FT.CREATE

Creates an index and initiates a backfill of that index. For more information, see [Vector search overview](vector-search-overview.md "vector-search-overview.md") for details on index construction.

**Syntax**

```
FT.CREATE <index-name>
ON HASH | JSON
[PREFIX <count> <prefix1> [<prefix2>...]]
SCHEMA
(<field-identifier> [AS <alias>]
  NUMERIC
| TAG [SEPARATOR <sep>] [CASESENSITIVE]
| TEXT
| VECTOR [HNSW|FLAT] <attr_count> [<attribute_name> <attribute_value>])

)+

```

**Schema**

- Field identifier:

      + For hash keys, field identifier is A field name.
      + For JSON keys, field identifier is A JSON path.

  For more information, see [Index field types](vector-search-overview.md#vector-search-index-field-types "vector-search-overview.md#vector-search-index-field-types").

- Field types:

      + TAG: For more information, see [Tags](https://redis.io/docs/interact/search-and-query/advanced-concepts/tags/ "https://redis.io/docs/interact/search-and-query/advanced-concepts/tags/") .
      + NUMERIC: Field contains a number.
      + TEXT: Field contains any blob of data.
      + VECTOR: vector field that supports vector search.




      	- Algorithm – can be HNSW (Hierarchical Navigable Small World) or FLAT (brute force).
      	- `attr_count` – number of attributes that will be passed as algorithm configuration, this includes both names and values.
      	- `{attribute_name} {attribute_value}` – algorithm-specific key/value pairs that define index configuration.


      	For FLAT algorithm, attributes are:


      	Required:




      		* DIM – Number of dimensions in the vector.
      		* DISTANCE\_METRIC – Can be one of [L2 | IP | COSINE].
      		* TYPE – Vector type. The only supported type is `FLOAT32`.
      	Optional:




      		* INITIAL\_CAP – Initial vector capacity in the index affecting memory allocation size of the index.
      	For HNSW algorithm, attributes are:


      	Required:




      		* TYPE – Vector type. The only supported type is `FLOAT32`.
      		* DIM – Vector dimension, specified as a positive integer. Maximum: 32768
      		* DISTANCE\_METRIC – Can be one of [L2 | IP | COSINE].
      	Optional:




      		* INITIAL\_CAP – Initial vector capacity in the index affecting memory allocation size of the index. Defaults to 1024.
      		* M – Number of maximum allowed outgoing edges for each node in the graph in each layer. on layer zero the maximal number of outgoing edges will be 2M. Default is 16 Maximum is 512.
      		* EF\_CONSTRUCTION – controls the number of vectors examined during index construction. Higher values for this parameter will improve recall ratio at the expense of longer index creation times. Default value is 200. Maximum value is 4096.
      		* EF\_RUNTIME – controls the number of vectors examined during query operations. Higher values for this parameter can yield improved recall at the expense of longer query times. The value of this parameter can be overriden on a per-query basis. Default value is 10. Maximum value is 4096.

  **Return**

Returns a simple string OK message or error reply.

**Examples**

###### Note

The following example uses arguments native to [valkey-cli](https://valkey.io/topics/cli/ "https://valkey.io/topics/cli/"), such as de-quoting and de-escaping of data, before sending it to Valkey or Redis OSS. To use other programming-language clients
(Python, Ruby, C#, etc.), follow those environments' handling rules for dealing with strings and binary data. For more information on supported clients, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")

###### Example 1: Create some indexes

Create an index for vectors of size 2

```
FT.CREATE hash_idx1 ON HASH PREFIX 1 hash: SCHEMA vec AS VEC VECTOR HNSW 6 DIM 2 TYPE FLOAT32 DISTANCE_METRIC L2
OK
```

Create a 6-dimensional JSON index using the HNSW algorithm:

```
FT.CREATE json_idx1 ON JSON PREFIX 1 json: SCHEMA $.vec AS VEC VECTOR HNSW 6 DIM 6 TYPE FLOAT32 DISTANCE_METRIC L2
OK
```

###### Example 2: Populate some data

The following commands are formatted so they can be executed as arguments to the redis-cli terminal program.
Developers using programming-language clients (such Python, Ruby, C#, etc.) will need to follow their environment's
handling rules for dealing with strings and binary data.

Creating some hash and json data:

```
HSET hash:0 vec "\x00\x00\x00\x00\x00\x00\x00\x00"
HSET hash:1 vec "\x00\x00\x00\x00\x00\x00\x80\xbf"
JSON.SET json:0 . '{"vec":[1,2,3,4,5,6]}'
JSON.SET json:1 . '{"vec":[10,20,30,40,50,60]}'
JSON.SET json:2 . '{"vec":[1.1,1.2,1.3,1.4,1.5,1.6]}'
```

Note the following:

- The keys of the hash and JSON data have the prefixes of their index definitions.
- The vectors are at the appropriate paths of the index definitions.
- The hash vectors are entered as hex data while the JSON data is entered as numbers.
- The vectors are the appropriate lengths, the two-dimensional hash vector entries have two floats worth of hex data, the six-dimensional json vector entries have six numbers.

###### Example 3: Delete and re-create an index

```
FT.DROPINDEX json_idx1
OK

FT.CREATE json_idx1 ON JSON PREFIX 1 json: SCHEMA $.vec AS VEC VECTOR FLAT 6 DIM 6 TYPE FLOAT32 DISTANCE_METRIC L2
OK
```

Note the new JSON index uses the `FLAT` algorithm instead of the `HNSW` algorithm. Also note that it will re-index the existing JSON data:

```
FT.SEARCH json_idx1 "*=>[KNN 100 @VEC $query_vec]" PARAMS 2 query_vec "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" DIALECT 2
1) (integer) 3
2) "json:2"
3) 1) "__VEC_score"
   2) "11.11"
   3) "$"
   4) "[{\"vec\":[1.1, 1.2, 1.3, 1.4, 1.5, 1.6]}]"
4) "json:0"
5) 1) "__VEC_score"
   2) "91"
   3) "$"
   4) "[{\"vec\":[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]}]"
6) "json:1"
7) 1) "__VEC_score"
   2) "9100"
   3) "$"
   4) "[{\"vec\":[10.0, 20.0, 30.0, 40.0, 50.0, 60.0]}]"
```
