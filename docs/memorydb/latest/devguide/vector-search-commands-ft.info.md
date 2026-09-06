

# FT.INFO
<a name="vector-search-commands-ft.info"></a>

**Syntax**

```
FT.INFO <index-name>
```

Output from the FT.INFO page is an array of key value pairs as described in the following table:


| Key | Value type | Description | 
| --- | --- | --- | 
| index\_name | string | Name of the index | 
| creation\_timestamp | integer | Unix-style timestamp of creation time | 
| key\_type | string | HASH or JSON | 
| key\_prefixes | array of strings | Key prefixes for this index | 
| fields | array of field information | Fields of this index | 
| space\_usage | integer | Memory bytes used by this index | 
| fullext\_space\_usage | integer | Memory bytes used by non-vector fields | 
| vector\_space\_usage | integer | Memory bytes used by vector fields | 
| num\_docs | integer | Number of keys currently contained in the index | 
| num\_indexed\_vectors | integer | Number of vectors currently contained in the index | 
| current\_lag | integer | Recent delay of ingestion (milliSeconds) | 
| backfill\_status | string | One of: Completed, InProgres, Paused or Failed  | 

The following table describes the information for each field:


| Key | Value type | Description | 
| --- | --- | --- | 
| identifier | string | name of field | 
| field\_name | string | Hash member name or JSON Path | 
| type | string | one of: Numeric, Tag, Text or Vector | 
| option | string | ignore | 

If the field is of type Vector, additional information will be present depending on the algorithm. 

For the HNSW algorithm:


| Key | Value type | Description | 
| --- | --- | --- | 
| algorithm | string | HNSW | 
| data\_type | string | FLOAT32 | 
| distance\_metric | string | one of: L2, IP or Cosine | 
| initial\_capacity | integer | Initial size of vector field index | 
| current\_capacity | integer | Current size of vector field index | 
| maximum\_edges | integer | M parameter at creation | 
| ef\_construction | integer | EF\_CONSTRUCTION parameter at creation | 
| ef\_runtime | integer | EF\_RUNTIME parameter at creation | 

For the FLAT algorithm:


| Key | Value type | Description | 
| --- | --- | --- | 
| algorithm | string | FLAT | 
| data\_type | string | FLOAT32 | 
| distance\_metric | string | one of: L2, IP or Cosine | 
| initial\_capacity | integer | Initial size of vector field index | 
| current\_capacity | integer | Current size of vector field index | 