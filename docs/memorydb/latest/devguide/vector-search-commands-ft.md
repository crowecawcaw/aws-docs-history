# FT.AGGREGATE

A superset of the FT.SEARCH command, it allows substantial additional processing of the keys selected by the query expression.

**Syntax**

```
FT.AGGREGATE index query
  [LOAD * | [count field [field ...]]]
  [TIMEOUT timeout]
  [PARAMS count name value [name value ...]]
  [FILTER expression]
  [LIMIT offset num]
  [GROUPBY count property [property ...] [REDUCE function count arg [arg ...] [AS name] [REDUCE function count arg [arg ...] [AS name] ...]] ...]]
  [SORTBY count [ property ASC | DESC [property ASC | DESC ...]] [MAX num]]
  [APPLY expression AS name]

```

- FILTER, LIMIT, GROUPBY, SORTBY and APPLY clauses can be repeated multiple times in any order and be freely intermixed. They are applied in the order specified with the output of one clause feeding the input of the next clause.
- In the above syntax, a “property” is either a field declared in the [FT.CREATE](vector-search-commands-ft.md "vector-search-commands-ft.md") command for this index OR the output of a previous APPLY clause or REDUCE function.
- The LOAD clause is restricted to loading fields that have been declared in the index. “LOAD \*” will load all fields declared in the index.
- The following reducer functions are supported: COUNT, COUNT_DISTINCTISH, SUM, MIN, MAX, AVG, STDDEV, QUANTILE, TOLIST, FIRST_VALUE, and RANDOM_SAMPLE. For more information, see [Aggregations](https://redis.io/docs/interact/search-and-query/search/aggregations/ "https://redis.io/docs/interact/search-and-query/search/aggregations/")
- LIMIT <offset> <count>: Retains records starting at <offset> and continuing for up to <count>, all other records are discarded.
- PARAMS: Two times the number of key value pairs. Param key/value pairs can be referenced from within the query expression.
  **Return**

Returns an array or error reply.

- If the operation completes successfully, it returns an array. The first element is an integer with no particular meaning (should be ignored). The remaining elements are the results output by the last stage. Each element is an array of field name and value pairs.
- If the index is in progress of being back-filled, the command immediately returns an error reply.
- If timeout is reached, the command returns an error reply.
