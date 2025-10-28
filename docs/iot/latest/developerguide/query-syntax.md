# Query syntax

In fleet indexing, you use a query syntax to specify queries.

## Supported features

The query syntax supports the following features:

- Terms and phrases
- Searching fields
- Prefix search
- Range search
- Boolean operators `AND`, `OR`, `NOT`, and
  `–`. The hyphen is used to exclude something from search results (for
  example, `thingName:(tv* AND -plasma)`).
- Grouping
- Field grouping
- Escaping special characters (such as with \*\*)
- Leading wildcard use is limited to 1 query term per query. For example, you cannot
  search for `thingName:*my` and `thingGroupNames:*echo` in the same
  query. Queries that include a leading wildcard have a max
  query length of 100 characters.

###### Note

If you have a high limit increase granted for fleet indexing APIs, you may not be
able to use the leading wildcard feature for those specific APIs until your limit is
decreased.

## Unsupported features

The query syntax doesn't support the following features:

- Regular expressions
- Boosting
- Ranking
- Fuzzy searches
- Proximity search
- Sorting
- Aggregation
- Special characters: ```, `@`, `#`, `%`,
`\`, `/`, `'`, `;`, and `,`.
  Note that `,` is only supported in geoqueries.

## Notes

A few things to note about the query language:

- The default operator is AND. A query for `"thingName:abc thingType:xyz"`
  is equivalent to `"thingName:abc AND thingType:xyz"`.
- If a field isn't specified, AWS IoT searches for the term in all the registry, Device
  Shadow, and Device Defender fields.
- All field names are case sensitive.
- Search is case insensitive. Words are separated by white-space characters as defined
  by Java's `Character.isWhitespace(int)`.
- Indexing of Device Shadow data (unnamed shadows and named shadows) includes
  reported, desired, delta, and metadata sections.
- Device shadow and registry versions aren't searchable, but are present in the
  response.
- The maximum number of terms in a query is twelve.
- The special character `,` is only supported in geoqueries.
