

# Using the `datetime( )` Method for Groovy Time Data
<a name="best-practices-gremlin-datetime"></a>

Neptune provides the `datetime` method for specifying dates and times for queries sent in the Gremlin **Groovy** variant. This includes the Gremlin Console, text strings using the HTTP REST API, and any other serialization that uses Groovy. 

**Important**  
This *only* applies to methods where you send the Gremlin query as a *text string*. If you are using a Gremlin Language Variant, you must use the native date classes and functions for the language. For more information, see the next section, [Using Native Date and Time for GLV Time Data](best-practices-gremlin-datetime-glv.md).  
Starting with TinkerPop `3.5.2` (introduced in [Neptune engine release 1.1.1.0](engine-releases-1.1.1.0.md)), `datetime` is an integral part of TinkerPop.

You can use the `datetime` method to store and compare dates:

```
g.V('3').property('date',datetime('2001-02-08'))
```

```
g.V().has('date',gt(datetime('2000-01-01')))
```