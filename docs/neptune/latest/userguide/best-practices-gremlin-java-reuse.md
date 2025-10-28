# Re-use the client object across multiple threads

Re-use the same client (or `GraphTraversalSource`) object across multiple
threads. That is, create a shared instance of a `org.apache.tinkerpop.gremlin.driver.Client`
class in your application rather than doing so in every thread. The `Client`
object is thread safe, and the overhead of initializing it is considerable.

This also applies to `GraphTraversalSource`, which creates a `Client`
object internally. For example, the following code causes a new `Client` object
to be instantiated:

```
import static org.apache.tinkerpop.gremlin.process.traversal.AnonymousTraversalSource.traversal;

  /////

GraphTraversalSource traversal = traversal()
                                   .withRemote(DriverRemoteConnection.using(cluster));
```
