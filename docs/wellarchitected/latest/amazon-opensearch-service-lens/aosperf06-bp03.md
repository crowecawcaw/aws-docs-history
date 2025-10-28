# AOSPERF06-BP03 Implement HTTP compression

Reduce request and response payload sizes by enabling GZIP
compression.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome**: GZIP compression
is enabled in the OpenSearch Service domain, reducing the size of
data being ingested or requested.

**Benefits of establishing this best
practice:** Reduce the payload size of requests and
responses.

## Implementation guidance

In OpenSearch Service domains, GZIP compression can be used to
compress HTTP requests and responses. This compression helps
reduce document size, lowering bandwidth usage and latency,
resulting in improved transfer speeds.

### Implementation steps

- To use compression, include the following headers in the
  HTTP requests of your application:

```
'Accept-Encoding': 'gzip'
```

```
'Content-Encoding': 'gzip'
```

## Resources

- [Compressing
  HTTP requests in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/gzip.md "../../../opensearch-service/latest/developerguide/gzip.md")
