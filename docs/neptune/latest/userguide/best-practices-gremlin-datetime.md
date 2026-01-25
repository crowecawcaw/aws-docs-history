# Using the `datetime( )` Function

for Gremlin Scripts

Gremlin's `datetime()` function can be used to specify dates and times for
queries sent as script based requests.

###### Important

This _only_ applies to methods where you send
the Gremlin query as a _text string_. If you are using a Gremlin Language Variant,
you must use the native date classes and functions for the language. For more information,
see the next section, [Using Native Date and Time for GLV
Time Data](best-practices-gremlin-datetime-glv.md "best-practices-gremlin-datetime-glv.md").

You can use the `datetime` method to store and compare dates:

```
g.V('3').property('date',datetime('2001-02-08'))
```

```
g.V().has('date',gt(datetime('2000-01-01')))
```
