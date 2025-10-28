# An alternate way to connect to the Gremlin console

**Drawbacks of the normal connection approach**

The most common way to connect to the Gremlin console is the one explained above,
using commands like this at the `gremlin>` prompt:

```
gremlin> :remote connect tinkerpop.server conf/`(file name)`.yaml
gremlin> :remote console
```

This works well, and lets you send queries to Neptune. However, it takes the
Groovy script engine out of the loop, so Neptune treats all queries as pure Gremlin.
This means that the following query forms fail:

```
gremlin> 1 + 1
gremlin> x = g.V().count()
```

The closest you can get to using a variable when connected this way is to use
the `result` variable maintained by the console and send the query using
`:>`, like this:

```
gremlin> :remote console
==>All scripts will now be evaluated locally - type ':remote console' to return to remote mode for Gremlin Server - [krl-1-cluster.cluster-ro-cm9t6tfwbtsr.us-east-1.neptune.amazonaws.com/172.31.19.217:8182]
gremlin> :> g.V().count()
==>4249

gremlin> println(result)
[result{object=4249 class=java.lang.Long}]

gremlin> println(result['object'])
[4249]
```

 

**A different way to connect**

You can also connect to the Gremlin console in a different way, which
you may find nicer, like this:

```
gremlin> g = traversal().withRemote('conf/neptune.properties')
```

Here `neptune.properties` takes this form:

```
gremlin.remote.remoteConnectionClass=org.apache.tinkerpop.gremlin.driver.remote.DriverRemoteConnection
gremlin.remote.driver.clusterFile=conf/my-cluster.yaml
gremlin.remote.driver.sourceName=g
```

The `my-cluster.yaml` file should look like this:

```
hosts: [`my-cluster-abcdefghijk.us-east-1.neptune.amazonaws.com`]
port: 8182
serializer: { className: org.apache.tinkerpop.gremlin.util.ser.GraphBinaryMessageSerializerV1,
              config: { serializeResultToString: false } }
connectionPool: { enableSsl: true }
```

###### Note

Serializers were moved from the `gremlin-driver` module to the new `gremlin-util` module in
version 3.7.0. The package changed from org.apache.tinkerpop.gremlin.driver.ser to
org.apache.tinkerpop.gremlin.util.ser.

Configuring the Gremlin console connection like that lets you make the following
kinds of queries successfully:

```
gremlin> 1+1
==>2

gremlin> x=g.V().count().next()
==>4249

gremlin> println("The answer was ${x}")
The answer was 4249
```

You can avoid displaying the result, like this:

```
gremlin> x=g.V().count().next();[]
gremlin> println(x)
4249
```

All the usual ways of querying (without the terminal step) continue to work.
For example:

```
gremlin> g.V().count()
==>4249
```

You can even use the [`g.io().read()`](https://tinkerpop.apache.org/docs/current/reference/#io-step "https://tinkerpop.apache.org/docs/current/reference/#io-step")
step to load a file with this kind of connection.
