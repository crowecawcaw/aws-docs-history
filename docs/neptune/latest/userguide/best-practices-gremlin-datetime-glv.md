# Using Native Date and Time for GLV

Time Data

If you are using a Gremlin Language Variant (GLV), you must use the native date and time
classes and functions provided by the programming language for Gremlin time data.

The official TinkerPop libraries are all Gremlin Language Variant libraries.

- [Go](https://tinkerpop.apache.org/docs/current/reference/#gremlin-go "https://tinkerpop.apache.org/docs/current/reference/#gremlin-go")
- [Java](https://tinkerpop.apache.org/docs/current/reference/#gremlin-java "https://tinkerpop.apache.org/docs/current/reference/#gremlin-java")
- [Javascript](https://tinkerpop.apache.org/docs/current/reference/#gremlin-javascript "https://tinkerpop.apache.org/docs/current/reference/#gremlin-javascript")
- [.NET](https://tinkerpop.apache.org/docs/current/reference/#gremlin-dotnet "https://tinkerpop.apache.org/docs/current/reference/#gremlin-dotnet")
- [Python](https://tinkerpop.apache.org/docs/current/reference/#gremlin-python "https://tinkerpop.apache.org/docs/current/reference/#gremlin-python")

###### Important

This page only applies to Gremlin Language Variant (GLV) libraries. If you are using a method where you send
the Gremlin query as text string, you must use Gremlin's `datetime()` function. This includes the
Gremlin Console, text strings using the HTTP REST API or directly submitting Gremlin strings via the drivers.

###### Go

The following is a partial example in Go that creates a single property named 'date' for the vertex with an ID
of '3'. It sets the value to be a date generated using the Go time.Now() function.

```
import ( "time" )

g.V('3').property('date', time.Now()).next();
```

For a complete example for connecting to Neptune using Go, see
[Using a Go client to connect to a Neptune DB instance](access-graph-gremlin-go.md "access-graph-gremlin-go.md").

###### Java

The following is a partial example in Java that creates a single property named
'`date`' for the vertex with an ID of '`3`'. It sets the value to be
a date generated using the Java `Date()` constructor.

```
import java.util.date

g.V('3').property('date', new Date()).next();
```

For a complete example for connecting to Neptune using Java, see [Using a Java client to connect to a Neptune DB
instance](access-graph-gremlin-java.md "access-graph-gremlin-java.md").

###### Node.js (JavaScript)

The following is a partial example in JavaScript that creates a single property named
'`date`' for the vertex with an ID of '`3`'. It sets the value to be
a date generated using the Node.js `Date()` constructor.

```
g.V('3').property('date', new Date()).next()
```

For a complete example for connecting to Neptune using Node.js, see [Using Node.js to connect to a Neptune DB
instance](access-graph-gremlin-node-js.md "access-graph-gremlin-node-js.md") .

###### .NET (C#)

The following is a partial example in C# that creates a single property named
'`date`' for the vertex with an ID of '`3`'. It sets the value to be
a date generated using the .NET `*DateTime*.*UtcNow*` property.

```
Using System;

g.V('3').property('date', DateTime.UtcNow).next()
```

For a complete example for connecting to Neptune using C#, see [Using .NET to connect to a Neptune DB
instance](access-graph-gremlin-dotnet.md "access-graph-gremlin-dotnet.md").

###### Python

The following is a partial example in Python that creates a single property named
'`date`' for the vertex with an ID of '`3`'. It sets the value to be
a date generated using the Python `datetime.now()` method.

```
import datetime

g.V('3').property('date',datetime.datetime.now()).next()
```

For a complete example for connecting to Neptune using Python, see [Using Python to connect to a Neptune DB
instance](access-graph-gremlin-python.md "access-graph-gremlin-python.md").
