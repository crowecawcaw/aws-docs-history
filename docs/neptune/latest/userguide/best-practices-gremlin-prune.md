# Pruning Records with the Creation Time

Property

You can prune stale records by storing the creation time as a property on vertices and
dropping them periodically.

If you need to store data for a specific lifetime and then remove it from the graph
(vertex time to live), you can store a timestamp property at the creation of the vertex. You
can then periodically issue a `drop()` query for all vertices that were created
before a certain time; for example:

```
g.V().has(“timestamp”, lt(datetime('2018-10-11')))
```
