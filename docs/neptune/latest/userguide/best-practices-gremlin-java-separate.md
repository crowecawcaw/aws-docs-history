# Create separate Gremlin Java client

objects for read and write endpoints

You can increase performance by only performing writes on the writer endpoint and
reading from one or more read-only endpoints.

```
Client readerClient = Cluster.build("https://`reader-endpoint`")
          ...
          .connect()

Client writerClient = Cluster.build("https://`writer-endpoint`")
          ...
          .connect()
```
