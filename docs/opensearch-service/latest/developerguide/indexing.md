# Indexing data in Amazon OpenSearch Service

Because Amazon OpenSearch Service uses a REST API, numerous methods exist for indexing documents. You can
use standard clients like [curl](https://curl.haxx.se/ "https://curl.haxx.se/") or any programming
language that can send HTTP requests. To further simplify the process of interacting with
it, OpenSearch Service has clients for many programming languages. Advanced users can skip directly to
[Loading streaming data into Amazon OpenSearch Service](integrations.md "integrations.md").

We strongly recommend that you use Amazon OpenSearch Ingestion to ingest data, which is a fully
managed data collector built within OpenSearch Service. For more information, see [Amazon OpenSearch Ingestion](ingestion.md "ingestion.md").

For an introduction to indexing, see the [OpenSearch
documentation](https://docs.opensearch.org/latest/opensearch/index-data/ "https://docs.opensearch.org/latest/opensearch/index-data/").

## Naming restrictions for indexes

OpenSearch Service indexes have the following naming restrictions:

- All letters must be lowercase.
- Index names cannot begin with `_` or `-`.
- Index names can't contain spaces, commas, `:`, `"`,
  `*`, `+`, `/`, `\`,
  `|`, `?`, `#`, `>`, or
  `<`.

Don't include sensitive information in index, type, or document ID names. OpenSearch Service uses
these names in its Uniform Resource Identifiers (URIs). Servers and applications often
log HTTP requests, which can lead to unnecessary data exposure if URIs contain sensitive
information:

```
2018-10-03T23:39:43 198.51.100.14 200 "GET https://`opensearch-domain`/dr-jane-doe/flu-patients-2018/202-555-0100/ HTTP/1.1"
```

Even if you don't have [permissions](ac.md "ac.md") to view the associated
JSON document, you could infer from this fake log line that one of Dr. Doe's patients
with a phone number of 202-555-0100 had the flu in 2018.

If OpenSearch Service detects a real or percieved IP address in an index name (for example,
`my-index-12.34.56.78.91`), it masks the IP address. A call to
`_cat/indices` yields the following response:

```
green open my-index-x.x.x.x.91    soY19tBERoKo71WcEScidw 5 1 0 0   2kb  1kb
```

To prevent unnecessary confusion, avoid including IP addresses in index names.

## Reducing response size

Responses from the `_index` and `_bulk` APIs contain quite a bit
of information. This information can be useful for troubleshooting requests or for
implementing retry logic, but can use considerable bandwidth. In this example, indexing
a 32 byte document results in a 339 byte response (including headers):

```
PUT `opensearch-domain`/more-movies/_doc/1
{"title": "Back to the Future"}
```

**Response**

```
{
  "_index": "more-movies",
  "_type": "_doc",
  "_id": "1",
  "_version": 4,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 2,
    "failed": 0
  },
  "_seq_no": 3,
  "_primary_term": 1
}
```

This response size might seem minimal, but if you index 1,000,000 documents per
day—approximately 11.5 documents per second—339 bytes per response works
out to 10.17 GB of download traffic per month.

If data transfer costs are a concern, use the `filter_path` parameter to
reduce the size of the OpenSearch Service response, but be careful not to filter out fields that you
need in order to identify or retry failed requests. These fields vary by client. The
`filter_path` parameter works for all OpenSearch Service REST APIs, but is especially
useful with APIs that you call frequently, such as the `_index` and
`_bulk` APIs:

```
PUT `opensearch-domain`/more-movies/_doc/1?filter_path=result,_shards.total
{"title": "Back to the Future"}
```

**Response**

```
{
  "result": "updated",
  "_shards": {
    "total": 2
  }
}
```

Instead of including fields, you can exclude fields with a `-` prefix.
`filter_path` also supports wildcards:

```
POST `opensearch-domain`/_bulk?filter_path=-took,-items.index._*
{ "index": { "_index": "more-movies", "_id": "1" } }
{"title": "Back to the Future"}
{ "index": { "_index": "more-movies", "_id": "2" } }
{"title": "Spirited Away"}

```

**Response**

```
{
  "errors": false,
  "items": [
    {
      "index": {
        "result": "updated",
        "status": 200
      }
    },
    {
      "index": {
        "result": "updated",
        "status": 200
      }
    }
  ]
}
```

## Index codecs

Index codecs determine how the stored fields on an index are compressed and stored on
disk. The index codec is controlled by the static `index.codec` setting,
which specifies the compression algorithm. This setting impacts the index shard size and
operation performance.

For a list of supported codecs and their performance characteristics, see [Supported codecs](https://opensearch.org/docs/latest/im-plugin/index-codecs/#supported-codecs "https://opensearch.org/docs/latest/im-plugin/index-codecs/#supported-codecs") in the OpenSearch documentation.

When you choose an index codec, consider the following:

- To avoid the challenges of changing the codec setting of an existing index,
  test a representative workload in a non-production environment before using a
  new codec setting. For more information, see [Changing an index codec](https://opensearch.org/docs/latest/im-plugin/index-codecs/#changing-an-index-codec "https://opensearch.org/docs/latest/im-plugin/index-codecs/#changing-an-index-codec").
- You can't use [Zstandard
  compression codecs](https://opensearch.org/docs/latest/im-plugin/index-codecs/ "https://opensearch.org/docs/latest/im-plugin/index-codecs/") (`"index.codec": "zstd"` or
  `"index.codec": "zstd_no_dict"`) for [k-NN](https://opensearch.org/docs/latest/search-plugins/knn/index/ "https://opensearch.org/docs/latest/search-plugins/knn/index/") or [Security
  Analytics](https://opensearch.org/docs/latest/security-analytics/index/ "https://opensearch.org/docs/latest/security-analytics/index/") indexes.
