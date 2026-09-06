

# Streaming query results with Gremlin
<a name="access-graph-gremlin-streaming"></a>

When you run a Gremlin traversal that returns a large number of results, Neptune streams them back to the client in batches over the WebSocket connection. Neptune sends result batches as they are produced, without waiting for the client to request more. This can be advantageous if you want to process results as they are being returned from the server, but requires using lazy iteration patterns to avoid collecting the full result set into memory.

Neptune sends results in batches of 64 per WebSocket frame by default. You cannot change this server-side default, but the batch size can be overridden on a per-request basis from the client using the [`batchSize`](https://tinkerpop.apache.org/docs/current/reference/#gremlin-java-configuration) request option (called `Tokens.ARGS_BATCH_SIZE` in the Java driver, or `connectionPool.resultIterationBatchSize` as a driver-level default).

For details on configuring `batchSize` in other language drivers, see the Configuration section for each driver in the [Apache TinkerPop Gremlin Drivers and Variants](https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants) documentation.

Because the server pushes results automatically, client-side backpressure is handled implicitly through TCP and WebSocket flow control. If the client is slow to read from the socket, the server's writes will eventually block until the client catches up.

**Important**  
Streaming is most effective with traversals that can produce results incrementally. Traversals that include `order()`, `groupCount()`, `group()`, `dedup()`, or other steps that require the full traversal to complete before emitting results will cause Neptune to materialize the entire result set in memory before streaming begins. In these cases, batching still reduces per-frame serialization overhead, but does not reduce server-side memory usage.

## Consuming results incrementally
<a name="access-graph-gremlin-streaming-usage"></a>

To process results as they arrive, iterate lazily using `hasNext()` / `next()` or equivalent APIs rather than collecting all results into a list. You can use `next(batchSize)` to pull results in application-level batches, allowing you to perform intermediate work between batches while the server continues producing results.

**Example Java (GLV bytecode)**  

```
GraphTraversalSource g = traversal().withRemote(connection);

int batchSize = 10;
int batchNum = 0;
var traversal = g.V().hasLabel("movie").values("title").limit(1000);
while (traversal.hasNext()) {
    var batch = traversal.next(batchSize);
    batchNum++;
    for (var title : batch) {
        System.out.println("  " + title);
    }

    // Do other intermediary work here between batch calls
    System.out.println("Batch " + batchNum + " processing complete\n");
}
```

**Example Python**  

```
g = traversal().with_remote(connection)

BATCH_SIZE = 10
batch_num = 0
t = g.V().has_label('movie').values('title').limit(1000)
while t.has_next():
    batch = t.next(BATCH_SIZE)
    batch_num += 1
    for title in batch:
        print(f"  {title}")

    # Do other intermediary work here between batch calls
    print(f"Batch {batch_num} processing complete\n")
```

**Example Go**  

```
// The Go driver does not support next(n), so batches are accumulated manually.
g := gremlingo.Traversal_().WithRemote(connection)

resultSet, err := g.V().HasLabel("movie").Values("title").Limit(1000).GetResultSet()
if err != nil {
    log.Fatal(err)
}

batchSize := 10
batchNum := 0
for {
    var batch []interface{}
    for i := 0; i < batchSize; i++ {
        result, ok, err := resultSet.One() // returns (value, ok, error); ok is false when results are exhausted
        if err != nil {
            log.Fatal(err)
        }
        if !ok {
            break
        }
        batch = append(batch, result)
    }
    if len(batch) == 0 {
        break
    }
    batchNum++
    for _, v := range batch {
        fmt.Printf("  %v\n", v)
    }

    // Do other intermediary work here between batch calls
    fmt.Printf("Batch %d processing complete\n\n", batchNum)
}
```

**Example .NET**  

```
var g = Traversal().WithRemote(connection);

var batchSize = 10;
var batchNum = 0;
var traversal = g.V().HasLabel("movie").Values<string>("title").Limit<string>(1000);
while (traversal.HasNext())
{
    var batch = traversal.Next(batchSize);
    batchNum++;
    foreach (var title in batch)
    {
        Console.WriteLine($"  {title}");
    }

    // Do other intermediary work here between batch calls
    Console.WriteLine($"Batch {batchNum} processing complete\n");
}
```

**Example Node.js**  

```
// The Node.js driver does not support next(n), so batches are accumulated manually.
const g = traversal().withRemote(connection);

const batchSize = 10;
let batchNum = 0;
const t = g.V().hasLabel('movie').values('title').limit(1000);
while (true) {
    const batch = [];
    for (let i = 0; i < batchSize; i++) {
        const result = await t.next();
        if (result.done) break;
        batch.push(result.value);
    }
    if (batch.length === 0) break;
    batchNum++;
    for (const title of batch) {
        console.log(`  ${title}`);
    }

    // Do other intermediary work here between batch calls
    console.log(`Batch ${batchNum} processing complete\n`);
}
```

## Eager vs. incremental consumption
<a name="access-graph-gremlin-streaming-avoid"></a>

Streaming allows you to process results incrementally as additional data is being fetched and returned. The following methods block until the entire result set is collected into memory, preventing your application from acting on results as they arrive:
+ **Java:** `toList()` or `toSet()`
+ **Python:** `toList()` or `toSet()`
+ **Go:** `ToList()`, `ToSet()`, or `GetResultSet().GetAll()`
+ **.NET:** `ToList()` or `Promise()`
+ **Node.js:** `toList()`

**Note**  
Data still flows incrementally over the WebSocket connection even when using these methods. The difference is that your application cannot process individual results until the entire collection is complete. To process results as they arrive, use the lazy iteration or batch patterns shown in the examples above.