# Gremlin edge classification queries in Neptune ML

For Gremlin edge classification in Neptune ML:

- The model is trained on one property of the edges. The set of unique
  values of this property is referred to as a set of classes.
- The class or categorical property value of an edge can be inferred
  from the edge classification model, which is useful when this property is not
  already attached to the edge.
- In order to fetch one or more classes from an edge classification
  model, you need to use the `with()` step with the predicate,
  `"Neptune#ml.classification"` to configure the `properties()`
  step. The output format is similar to what you would expect if those were edge
  properties.

###### Note

Edge classification only works with string property values.
That means that numerical property values such as `0` or `1`
are not supported, although the string equivalents `"0"` and `"1"`
are. Similarly, the Boolean property values `true` and `false`
don't work, but `"true"` and `"false"` do.

Here is an example of an edge classification query that requests a
confidence score using the `Neptune#ml.score` predicate:

```
g.with("Neptune#ml.endpoint","edge-classification-movie-lens-endpoint")
 .with("Neptune#ml.iamRoleArn","arn:aws:iam::0123456789:role/sagemaker-role")
 .E("relationship_1","relationship_2","relationship_3")
 .properties("knows_by", "Neptune#ml.score").with("Neptune#ml.classification")
```

The response would look like this:

```
==>p[knows_by->"Family"]
==>p[Neptune#ml.score->0.01234567]
==>p[knows_by->"Friends"]
==>p[Neptune#ml.score->0.543210]
==>p[knows_by->"Colleagues"]
==>p[Neptune#ml.score->0.10101]
```

## Syntax of a Gremlin edge classification query

For a simple graph where `User` is the head and tail node, and
`Relationship` is the edge that connects them, an example edge classification
query is:

```
g.with("Neptune#ml.endpoint","edge-classification-social-endpoint")
 .with("Neptune#ml.iamRoleArn","arn:aws:iam::0123456789:role/sagemaker-role")
 .E("relationship_1","relationship_2","relationship_3")
 .properties("knows_by").with("Neptune#ml.classification")
```

The output of this query would look something like the following:

```
==>p[knows_by->"Family"]
==>p[knows_by->"Friends"]
==>p[knows_by->"Colleagues"]
```

In the query above, the `E()` and `properties()` steps
are used as follows:

- The `E()` step contains the set of edges for which you want to
  fetch the classes from the edge-classification model:

```
.E("relationship_1","relationship_2","relationship_3")
```

- The `properties()` step contains the key on which the model
  was trained, and has `.with("Neptune#ml.classification")` to indicate
  that this is an edge classification ML inference query.

Multiple property keys are not currently supported in a
`properties().with("Neptune#ml.classification")` step. For example,
the following query results in an exception being thrown:

```
g.with("Neptune#ml.endpoint","edge-classification-social-endpoint")
 .with("Neptune#ml.iamRoleArn","arn:aws:iam::0123456789:role/sagemaker-role")
 .E("relationship_1","relationship_2","relationship_3")
 .properties("knows_by", "other_label").with("Neptune#ml.classification")
```

For specific error messages, see [List of exceptions for Neptune ML Gremlin inference queries](machine-learning-gremlin-exceptions.md "machine-learning-gremlin-exceptions.md").

A `properties().with("Neptune#ml.classification")` step can
be used in combination with any of the following steps:

- `value()`
- `value().is()`
- `hasValue()`
- `has(value,"")`
- `key()`
- `key().is()`
- `hasKey()`
- `has(key,"")`
- `path()`

## Using inductive inference in an edge classification query

Supposing you were to add a new edge to an existing graph, in a Jupyter notebook,
like this:

```
%%gremlin
g.V('1').as('fromV')
.V('2').as('toV')
.addE('eLabel1').from('fromV').to('toV').property(id, 'e101')
```

You could then use an inductive inference query to get a scale that took into
account the new edge:

```
%%gremlin
g.with("Neptune#ml.endpoint", "ec-ep")
 .with("Neptune#ml.iamRoleArn", "arn:aws:iam::123456789012:role/NeptuneMLRole")
 .E('e101').properties("scale", "Neptune#ml.score")
 .with("Neptune#ml.classification")
 .with("Neptune#ml.inductiveInference")
```

Because the query is not deterministic, the results would vary somewhat
if you run it multiple times, based on the random neighborhood:

```
# First time
==>vp[scale->Like]
==>vp[Neptune#ml.score->0.12345678]

# Second time
==>vp[scale->Like]
==>vp[Neptune#ml.score->0.21365921]
```

If you need more consistent results, you could make the query deterministic:

```
%%gremlin
g.with("Neptune#ml.endpoint", "ec-ep")
 .with("Neptune#ml.iamRoleArn", "arn:aws:iam::123456789012:role/NeptuneMLRole")
 .E('e101').properties("scale", "Neptune#ml.score")
 .with("Neptune#ml.classification")
 .with("Neptune#ml.inductiveInference")
 .with("Neptune#ml.deterministic")
```

Now the results will be more or less the same every time you run the query:

```
# First time
==>vp[scale->Like]
==>vp[Neptune#ml.score->0.12345678]

# Second time
==>vp[scale->Like]
==>vp[Neptune#ml.score->0.12345678]
```
