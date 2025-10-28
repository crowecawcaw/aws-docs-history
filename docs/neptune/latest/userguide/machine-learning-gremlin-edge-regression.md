# Gremlin edge regression queries in Neptune ML

Edge regression is similar to edge classification, except that the value inferred
from the ML model is numeric. For edge regression, Neptune ML supports the same queries
as for classification.

Key points to note are:

- You need to use the ML predicate `"Neptune#ml.regression"` to configure
  the `properties()` step for this use-case.
- The `"Neptune#ml.limit"` and `"Neptune#ml.threshold"`
  predicates are not applicable in this use-case.
- For filtering on the value, you need to specify the value as numerical.

## Syntax of a Gremlin edge regression query

For a simple graph where `User` is the head node, `Movie`
is the tail node, and `Rated` is the edge that connects them, here is an
example edge regression query that finds the numeric rating value, referred to as score here,
for the edge `Rated`:

```
g.with("Neptune#ml.endpoint","edge-regression-movie-lens-endpoint")
 .with("Neptune#ml.iamRoleArn","arn:aws:iam::0123456789:role/sagemaker-role")
 .E("rating_1","rating_2","rating_3")
 .properties("score").with("Neptune#ml.regression")
```

You can also filter on a value inferred from the ML regression model. For the
existing `Rated` edges (from `User` to `Movie`)
identified by `"rating_1"`, `"rating_2"`, and `"rating_3"`,
where the edge property `Score` is not present for these ratings, you can
use a query like following to infer `Score` for the edges where it is
greater than or equal to 9:

```
g.with("Neptune#ml.endpoint","edge-regression-movie-lens-endpoint")
 .with("Neptune#ml.iamRoleArn","arn:aws:iam::0123456789:role/sagemaker-role")
 .E("rating_1","rating_2","rating_3")
 .properties("score").with("Neptune#ml.regression")
 .value().is(P.gte(9))
```

## Using inductive inference in an edge regression query

Supposing you were to add a new edge to an existing graph, in a Jupyter notebook,
like this:

```
%%gremlin
g.V('1').as('fromV')
.V('2').as('toV')
.addE('eLabel1').from('fromV').to('toV').property(id, 'e101')
```

You could then use an inductive inference query to get a score that took into
account the new edge:

```
%%gremlin
g.with("Neptune#ml.endpoint", "er-ep")
 .with("Neptune#ml.iamRoleArn", "arn:aws:iam::123456789012:role/NeptuneMLRole")
 .E('e101').properties("score")
 .with("Neptune#ml.regression")
 .with("Neptune#ml.inductiveInference")
```

Because the query is not deterministic, the results would vary somewhat
if you run it multiple times, based on the random neighborhood:

```
# First time
==>ep[score->96]

# Second time
==>ep[score->91]
```

If you need more consistent results, you could make the query deterministic:

```
%%gremlin
g.with("Neptune#ml.endpoint", "er-ep")
 .with("Neptune#ml.iamRoleArn", "arn:aws:iam::123456789012:role/NeptuneMLRole")
 .E('e101').properties("score")
 .with("Neptune#ml.regression")
 .with("Neptune#ml.inductiveInference")
 .with("Neptune#ml.deterministic")
```

Now the results will be more or less the same every time you run the query:

```
# First time
==>ep[score->96]

# Second time
==>ep[score->96]
```
