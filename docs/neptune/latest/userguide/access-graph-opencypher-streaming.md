

# Streaming query results with the Bolt protocol
<a name="access-graph-opencypher-streaming"></a>

When you run an openCypher query that returns a large number of records, you don't have to load the entire result set into client memory at once. Neptune supports result streaming over the Bolt protocol, which lets the driver fetch records in batches and process them incrementally as they arrive. This can be advantageous if you want to process results as they are being returned from the server, but requires configuring `FetchSize` and using lazy iteration to avoid loading the full result set into memory.

This works through the [Bolt v4.0 PULL mechanism](https://neo4j.com/docs/bolt/current/bolt/message/#messages-pull). Instead of requesting all records in a single message, the driver sends a PULL request with a batch size. For example, "give me the next 50 records." Neptune sends back that number of records along with a flag indicating whether more are available. The driver then requests the next batch when the client is ready, and this continues until the result set is fully consumed.

You control the batch size using the `FetchSize` setting in the driver's session configuration. Combined with lazy iteration (processing records one at a time as they're returned), this bounds client-side memory usage regardless of how large the total result set is.

**Important**  
`FetchSize` controls the flow of data between server and client. It does not affect how Neptune executes the query. Neptune begins executing the query and producing results as soon as it receives the RUN message. Results are buffered server-side until the client requests them with a PULL message. If the client does not consume results within the configured query timeout, Neptune terminates the query, discards buffered results, and releases server-side resources. There is no separate server-side buffer limit; buffering continues until the client pulls the results or the query timeout is reached.  
Streaming is most effective with non-aggregating queries that can produce results incrementally. Queries that include `ORDER BY`, aggregation functions (such as `count()`, `collect()`, or `sum()`), or `DISTINCT` require Neptune to compute the full result set before returning any records. In these cases, `FetchSize` still limits client-side memory usage per batch, but the server must hold the entire result set in memory before streaming begins.

**Note**  
The openCypher HTTPS endpoint delivers results using HTTP chunked transfer encoding, which streams data to the client as it is produced. However, the client cannot control the pace of delivery. There is no equivalent of `FetchSize` for the HTTPS endpoint. To control client-side memory consumption with large result sets, use a Bolt driver connection with `FetchSize` configured.

## Configuring FetchSize and processing results in batches
<a name="access-graph-opencypher-streaming-usage"></a>

Set `FetchSize` on the session or driver configuration to control how many records the driver requests from Neptune per PULL message. Note that `FetchSize` controls the driver-to-server flow, not application-level batching. To process results in application-level batches (for example, to perform intermediate work between groups of records), use a helper method that accumulates records from the driver's lazy iterator.

The following examples show both: configuring `FetchSize` on the session, and using a helper method to group records into application-level batches for processing.

**Example Java**  

```
static void processBatches(Result result, int size,
        Consumer<List<Record>> handler) {
    var batch = new ArrayList<Record>();
    while (result.hasNext()) {
        batch.add(result.next());
        if (batch.size() >= size) {
            handler.accept(batch);
            batch = new ArrayList<>();
        }
    }
    if (!batch.isEmpty()) handler.accept(batch);
}

// Usage:
try (Session session = driver.session(SessionConfig.builder()
        .withFetchSize(50)
        .withDefaultAccessMode(AccessMode.READ)
        .build())) {

    Result result = session.run("MATCH (m:movie) RETURN m.title AS title");
    processBatches(result, 10, batch -> {
        for (var record : batch) {
            System.out.println(record.get("title").asString());
        }

        // Do other intermediary work here between batch calls
    });
    result.consume();
}
```

**Example Python**  

```
async def batched(result, size):
    batch = []
    async for record in result:
        batch.append(record)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch

# Usage:
async with driver.session(fetch_size=50) as session:
    result = await session.run("MATCH (m:movie) RETURN m.title AS title")
    async for batch in batched(result, 10):
        for record in batch:
            print(record["title"])

        # Do other intermediary work here between batch calls
```

**Example Go**  

```
func processBatches(ctx context.Context, result neo4j.ResultWithContext,
        size int, handler func([]*neo4j.Record)) error {
    var batch []*neo4j.Record
    for result.Next(ctx) {
        batch = append(batch, result.Record())
        if len(batch) >= size {
            handler(batch)
            batch = nil
        }
    }
    if len(batch) > 0 {
        handler(batch)
    }
    return result.Err()
}

// Usage:
session := driver.NewSession(ctx, neo4j.SessionConfig{
    AccessMode: neo4j.AccessModeRead,
    FetchSize:  50,
})
defer session.Close(ctx)

result, err := session.Run(ctx,
    "MATCH (m:movie) RETURN m.title AS title", nil)
if err != nil {
    log.Fatal(err)
}

if err := processBatches(ctx, result, 10, func(batch []*neo4j.Record) {
    for _, record := range batch {
        title, _ := record.Get("title")
        fmt.Println(title)
    }

    // Do other intermediary work here between batch calls
}); err != nil {
    log.Fatal(err)
}
```

**Example .NET**  

```
static async IAsyncEnumerable<List<IRecord>> Batched(
        IResultCursor result, int size)
{
    var batch = new List<IRecord>();
    while (await result.FetchAsync())
    {
        batch.Add(result.Current);
        if (batch.Count >= size)
        {
            yield return batch;
            batch = new List<IRecord>();
        }
    }
    if (batch.Count > 0) yield return batch;
}

// Usage:
await using var session = driver.AsyncSession(o => o
    .WithFetchSize(50)
    .WithDefaultAccessMode(AccessMode.Read));

var result = await session.RunAsync("MATCH (m:movie) RETURN m.title AS title");
await foreach (var batch in Batched(result, 10))
{
    foreach (var record in batch)
    {
        Console.WriteLine(record["title"].As<string>());
    }

    // Do other intermediary work here between batch calls
}
```

**Example Node.js**  

```
// Uses for-await-of on the Result's async iterator (Neo4j driver v5+).
// This is pull-based: the driver pauses fetching while the loop body
// executes, providing natural backpressure. This is preferred over
// result.subscribe(), which is push-based and continues delivering
// records during async processing.
async function* batched(result, size) {
    let batch = [];
    for await (const record of result) {
        batch.push(record);
        if (batch.length >= size) {
            yield batch;
            batch = [];
        }
    }
    if (batch.length > 0) yield batch;
}

// Usage:
const session = driver.session({
    defaultAccessMode: neo4j.session.READ,
    fetchSize: 50
});

try {
    const result = session.run('MATCH (m:movie) RETURN m.title AS title');
    for await (const batch of batched(result, 10)) {
        for (const record of batch) {
            console.log(record.get('title'));
        }

        // Do other intermediary work here between batch calls
    }
} finally {
    await session.close();
}
```

## Eager vs. incremental consumption
<a name="access-graph-opencypher-streaming-avoid"></a>

The following methods block until the entire result set is collected into memory, preventing your application from acting on results as they arrive:
+ **Java:** `result.list()`
+ **Python:** `result.data()`, `list(result)`
+ **Go:** `result.Collect(ctx)`, `neo4j.EagerResultTransformer`
+ **.NET:** `result.ToListAsync()`
+ **Node.js:** `const { records } = await result`

To process results incrementally, use the lazy iteration and batch helper patterns shown in the examples above.