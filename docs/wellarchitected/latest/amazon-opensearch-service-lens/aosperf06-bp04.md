# AOSPERF06-BP04 Evaluate `filter_path` criteria

Reduce response and request sizes by optimizing the filter_path
criteria, minimizing download traffic.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome**: Reduced response
and request size.

**Benefits of establishing this best
practice:** Reduced download traffic.

## Implementation guidance

Responses from the `_index` and `_bulk` APIs carry extensive
information, which is valuable for troubleshooting or implementing
retry logic. However, due to bandwidth considerations, indexing a
32-byte document, for instance, results in a 339-byte response
(including headers).

This response size might seem minimal, but if you index 1,000,000
documents per day (or approximately 11.5 documents per second),
339 bytes per response works out to 10.17 GB of download traffic
per month.

### Implementation steps

- Use `filter_path` with the APIs that you call frequently,
  such as the `_index` and `_bulk` APIs. For example:

```
PUT *opensearch-domain*/<index-name>
        /_doc/1?filter_path=result,_shards.total
        POST
        *opensearch-domain*/_bulk?filter_path=-took,-items.index._*
```

## Resources

- [Reducing
  response size](../../../opensearch-service/latest/developerguide/indexing.md#indexing-size "../../../opensearch-service/latest/developerguide/indexing.md#indexing-size")
