# Neptune full-text search parameters

Amazon Neptune uses the following parameters for specifying full-text OpenSearch queries
in both Gremlin and SPARQL:

- **`queryType`**   –  
  (_Required_) The type of OpenSearch query. (For a list of query types, see the [OpenSearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/full-text-queries.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/full-text-queries.html")). Neptune supports the following OpenSearch query types:
  - [simple_query_string](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-simple-query-string-query.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-simple-query-string-query.html")   –  
    Returns documents based on a provided query string, using a parser with a
    limited but fault-tolerant Lucene syntax. This is the default query type.

  This query uses a simple syntax to parse and split the
  provided query string into terms based on special operators.
  The query then analyzes each term independently before
  returning matching documents.

  While its syntax is more limited than the `query_string` query,
  the `simple_query_string` query does not return errors
  for invalid syntax. Instead, it ignores any invalid parts of the query string.
  - [match](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html")   –  
    The `match` query is the standard query for performing a
    full-text search, including options for fuzzy matching.
  - [prefix](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-prefix-query.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-prefix-query.html")   –  
    Returns documents that contain a specific prefix in a provided field.
  - [fuzzy](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html")   –  
    Returns documents that contain terms similar to the search term,
    as measured by a Levenshtein edit distance.

  An edit distance is the number of one-character changes needed
  to turn one term into another. These changes can include:

      - Changing a character (box to fox).
      - Removing a character (black to lack).
      - Inserting a character (sic to sick).
      - Transposing two adjacent characters (act to cat).

  To find similar terms, the fuzzy query creates a set of all possible
  variations and expansions of the search term within a specified edit distance
  and then returns exact matches for each of those variants.
  - [term](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html")   –  
    Returns documents that contain an exact match of a specified term
    in one of the specified fields.

  You can use the `term` query to find documents based
  on a precise value such as a price, a product ID, or a username.

  ###### Warning

  Avoid using the term query for text fields. By default,
  OpenSearch changes the values of text fields as part of its analysis,
  which can make finding exact matches for text field values difficult.

  To search text field values, use the match query instead.
  - [query_string](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html")   –  
    Returns documents based on a provided query string, using a parser
    with a strict syntax (Lucene syntax).

  This query uses a syntax to parse and split the provided query
  string based on operators, such as AND or NOT. The query then
  analyzes each split text independently before returning matching
  documents.

  You can use the `query_string` query to create a
  complex search that includes wildcard characters, searches across
  multiple fields, and more. While versatile, the query is strict
  and returns an error if the query string includes any invalid
  syntax.

  ###### Warning

  Because it returns an error for any invalid syntax, we
  don’t recommend using the `query_string` query
  for search boxes.

  If you don’t need to support a query syntax, consider
  using the `match` query. If you need the features
  of a query syntax, use the `simple_query_string`
  query, which is less strict.

- **`field`**   –  
  The field in OpenSearch against which to run the search. This can be omitted
  only if the `queryType` allows it (as `simple_query_string`
  and `query_string` do), in which case the search is against all fields.
  In Gremlin, it is implicit.

Multiple fields can be specified if the query allows it, as do
`simple_query_string` and `query_string`.

- **`query`**   –   (_Required_) The query to run
  against OpenSearch. The contents of this field might vary according to the queryType.
  Different queryTypes accept different syntaxes, as `Regexp` does, for example.
  In Gremlin, `query` is implicit.
- **`maxResults`**   –   The maximum number
  of results to return. The default is the `index.max_result_window`
  OpenSearch setting, which itself defaults to 10,000. The `maxResults`
  parameter can specify any number lower than that.

###### Important

If you set `maxResults` to a value higher than
the OpenSearch `index.max_result_window` value and try to
retrieve more than `index.max_result_window` results, OpenSearch
fails with a `Result window is too large` error. However, Neptune
handles this gracefully without propagating the error. Keep this in mind if
you are trying to fetch more than `index.max_result_window` results.

- **`minScore`**   –   The minimum score a
  search result must have to be returned. See [OpenSearch
  relevance documentation](https://www.elastic.co/guide/en/elasticsearch/guide/current/scoring-theory.html "https://www.elastic.co/guide/en/elasticsearch/guide/current/scoring-theory.html") for an explanation of result scoring.
- **`batchSize`**   –   Neptune always
  fetches data in batches (the default batch size is 100). You can use this
  parameter to tune performance. The batch size cannot exceed the
  `index.max_result_window` OpenSearch setting, which defaults
  to 10,000.
- **`sortBy`**   –  
  An optional parameter that lets you sort the results returned by OpenSearch
  by one of the following:

      + *A particular string field in the document*   –  


      For example, in a SPARQL query, you could specify:



      ```
          neptune-fts:config neptune-fts:sortBy foaf:name .
      ```

      In a similar Gremlin query, you could specify:



      ```
          .withSideEffect('Neptune#fts.sortBy', 'name')
      ```
      + *A particular non-string field (`long`, `double`, etc.) in the document*   –  


      Note that when sorting on a non-string field, you need to append `.value` to the field name
       to differentiate it from a string field.


      For example, in a SPARQL query, you could specify:



      ```
          neptune-fts:config neptune-fts:sortBy foaf:name.value .
      ```

      In a similar Gremlin query, you could specify:



      ```
          .withSideEffect('Neptune#fts.sortBy', 'name.value')
      ```
      + `score`   –   Sort by match score (the default).


      If the `sortOrder` parameter is present but `sortBy` is not
       present, the results are sorted by `score` in the order specified by
       `sortOrder`.
      + `id`   –   Sort by ID, which means the SPARQL subject URI
       or the Gremlin vertex or edge ID.


      For example, in a SPARQL query, you could specify:



      ```
          neptune-fts:config neptune-fts:sortBy 'Neptune#fts.entity_id' .
      ```

      In a similar Gremlin query, you could specify:



      ```
          .withSideEffect('Neptune#fts.sortBy', 'Neptune#fts.entity_id')
      ```
      + `label`   –   Sort by label.


      For example, in a SPARQL query, you could specify:



      ```
          neptune-fts:config neptune-fts:sortBy 'Neptune#fts.entity_type' .
      ```

      In a similar Gremlin query, you could specify:



      ```
          .withSideEffect('Neptune#fts.sortBy', 'Neptune#fts.entity_type')
      ```
      + `doc_type`   –   Sort by document type (that is, SPARQL or Gremlin).


      For example, in a SPARQL query, you could specify:



      ```
          neptune-fts:config neptune-fts:sortBy 'Neptune#fts.document_type' .
      ```

      In a similar Gremlin query, you could specify:



      ```
          .withSideEffect('Neptune#fts.sortBy', 'Neptune#fts.document_type')
      ```

  By default, OpenSearch results are not sorted and their order is non-deterministic,
  meaning that the same query may return items in a different order each time it is run.
  For this reason, if the result set is greater than `max_result_window`, a quite different
  subset of the total results could be returned every time a query is run. By sorting, however, you
  can make the results of different runs more directly comparable.

If no `sortOrder` parameter accompanies `sortBy`, descending
(`DESC`) order from greatest to least is used.

- **`sortOrder`**   –  
  An optional parameter that lets you specify whether OpenSearch results are sorted
  from least to greatest or from greatest to least (the default):

######

    + `ASC`   –   Ascending order, from least to
     greatest.
    + `DESC`   –   Descending order, from greatest
     to least.


    This is the default value, used when the `sortBy` parameter is present
     but no `sortOrder` is specified.

If neither `sortBy` nor `sortOrder` is present, OpenSearch
results are not sorted by default.
