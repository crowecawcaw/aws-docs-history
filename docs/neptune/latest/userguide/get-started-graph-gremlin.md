# Using Gremlin to access graph data in Amazon Neptune

You can use the Gremlin Console to experiment with TinkerPop graphs and queries in a REPL
(read-eval-print loop) environment.

The following tutorial walks you through using the Gremlin console to
add vertices, edges, properties, and more to a Neptune graph, highlights some
differences in the Neptune-specific Gremlin implementation.

###### Note

This example assumes that you have completed the following:

- You have connected using SSH to an Amazon EC2 instance.
- You have created a Neptune cluster as detailed in
  [Create Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md").
- You have installed the Gremlin console as described in
  [Installing the Gremlin console](access-graph-gremlin-console.md "access-graph-gremlin-console.md").

###### Using the Gremlin Console

1. Change directories into the folder where the Gremlin console files
   are unzipped.

```
cd apache-tinkerpop-gremlin-console-3.7.2
```

2. Enter the following command to run the Gremlin Console.

```
bin/gremlin.sh
```

You should see the following output:

```
         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
plugin activated: tinkerpop.server
plugin activated: tinkerpop.utilities
plugin activated: tinkerpop.tinkergraph
gremlin>
```

You are now at the `gremlin>` prompt. You enter the remaining steps at
this prompt. 3. At the `gremlin>` prompt, enter the following to connect to the
Neptune DB instance.

```
:remote connect tinkerpop.server conf/neptune-remote.yaml
```

4. At the `gremlin>` prompt, enter the following to switch to remote mode.
   This sends all Gremlin queries to the remote connection.

```
:remote console
```

5. **Add vertex with label and property.**

```
g.addV('person').property('name', 'justin')
```

The vertex is assigned a `string` ID containing a GUID. All vertex IDs
are strings in Neptune. 6. **Add a vertex with custom id.**

```
g.addV('person').property(id, '1').property('name', 'martin')
```

The `id` property is not quoted. It is a keyword for the ID of the
vertex. The vertex ID here is a string with the number `1` in it.

Normal property names must be contained in quotation marks. 7. **Change property or add property if it doesn't
exist.**

```
g.V('1').property(single, 'name', 'marko')
```

Here you are changing the `name` property for the vertex from the
previous step. This removes all existing values from the `name`
property.

If you didn't specify `single`, it instead appends the value to the
`name` property if it hasn't done so already. 8. **Add property, but append property if property already has a
value.**

```
g.V('1').property('age', 29)
```

Neptune uses set cardinality as the default action.

This command adds the `age` property with the value `29`, but
it does not replace any existing values.

If the `age` property already had a value, this command appends
`29` to the property. For example, if the `age` property was
`27`, the new value would be `[ 27, 29 ]`. 9. **Add multiple vertices.**

```
g.addV('person').property(id, '2').property('name', 'vadas').property('age', 27).iterate()
g.addV('software').property(id, '3').property('name', 'lop').property('lang', 'java').iterate()
g.addV('person').property(id, '4').property('name', 'josh').property('age', 32).iterate()
g.addV('software').property(id, '5').property('name', 'ripple').property('lang', 'java').iterate()
g.addV('person').property(id, '6').property('name', 'peter').property('age', 35)
```

You can send multiple statements at the same time to Neptune.

Statements can be separated by newline (`'\n'`), spaces (`'
 '`), semicolon (`'; '`), or nothing (for example:
`g.addV(‘person’).iterate()g.V()` is valid).

###### Note

The Gremlin Console sends a separate command at every newline (`'\n'`), so they are
each a separate transaction in that case. This example has all the commands on separate
lines for readability. Remove the newline (`'\n'`) characters to send it as a
single command via the Gremlin Console.

All statements other than the last statement must end in a terminating step, such as
`.next()` or `.iterate()`, or they will not run. The Gremlin
Console does not require these terminating steps. Use `.iterate` whenever
you don't need the results to be serialized.

All statements that are sent together are included in a single transaction and
succeed or fail together. 10. **Add edges.**

```
g.V('1').addE('knows').to(__.V('2')).property('weight', 0.5).iterate()
g.addE('knows').from(__.V('1')).to(__.V('4')).property('weight', 1.0)
```

Here are two different ways to add an edge. 11. **Add the rest of the Modern graph.**

```
g.V('1').addE('created').to(__.V('3')).property('weight', 0.4).iterate()
g.V('4').addE('created').to(__.V('5')).property('weight', 1.0).iterate()
g.V('4').addE('knows').to(__.V('3')).property('weight', 0.4).iterate()
g.V('6').addE('created').to(__.V('3')).property('weight', 0.2)

```

12. **Delete a vertex.**

```
g.V().has('name', 'justin').drop()
```

Removes the vertex with the `name` property equal to
`justin`.

###### Important

_Stop here, and you have the full Apache TinkerPop Modern
graph. The examples in the [Traversal section](https://tinkerpop.apache.org/docs/current/reference/#graph-traversal-steps "https://tinkerpop.apache.org/docs/current/reference/#graph-traversal-steps") of the TinkerPop documentation use the Modern
graph._ 13. **Run a traversal.**

```
g.V().hasLabel('person')
```

Returns all `person` vertices. 14. **Run a Traversal with values (valueMap()).**

```
g.V().has('name', 'marko').out('knows').valueMap()
```

Returns key, value pairs for all vertices that `marko` “knows.” 15. **Specify multiple labels.**

```
g.addV("Label1::Label2::Label3")
```

Neptune supports multiple labels for a vertex. When you create a label, you can
specify multiple labels by separating them with `::`.

This example adds a vertex with three different labels.

The `hasLabel` step matches this vertex with any of those three labels:
`hasLabel("Label1")`, `hasLabel("Label2")`, and
`hasLabel("Label3")`.

The `::` delimiter is reserved for this use only.

You cannot specify multiple labels in the `hasLabel` step. For example,
`hasLabel("Label1::Label2")` does not match anything. 16. **Specify Time/date**.

```
g.V().property(single, 'lastUpdate', datetime('2018-01-01T00:00:00'))
```

Neptune does not support Java Date. Use the `datetime()` function
instead. `datetime()` accepts an ISO8061-compliant `datetime`

string.

It supports the following formats: `YYYY-MM-DD, YYYY-MM-DDTHH:mm`,
`YYYY-MM-DDTHH:mm:SS`, and `YYYY-MM-DDTHH:mm:SSZ`. 17. **Delete vertices, properties, or edges.**

```
g.V().hasLabel('person').properties('age').drop().iterate()
g.V('1').drop().iterate()
g.V().outE().hasLabel('created').drop()
```

Here are several drop examples.

###### Note

The `.next()` step does not work with `.drop()`. Use
`.iterate()` instead. 18. When you are finished, enter the following to exit the Gremlin Console.

```
:exit
```

###### Note

Use a semicolon (`;`) or a newline character (`\n`) to separate
each statement.

Each traversal preceding the final traversal must end in `iterate()` to be
executed. Only the data from the final traversal is returned.
