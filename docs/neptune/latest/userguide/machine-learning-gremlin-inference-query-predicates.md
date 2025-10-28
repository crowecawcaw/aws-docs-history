# Neptune ML predicates used in Gremlin inference queries

## `Neptune#ml.deterministic`

This predicate is an option for inductive inference queries — that is,
for queries that include the [Neptune#ml.inductiveInference](#machine-learning-gremlin-inference-neptune-ml-inductiveInference "#machine-learning-gremlin-inference-neptune-ml-inductiveInference")
predicate.

When using inductive inference, the Neptune engine creates the appropriate
subgraph to evaluate the trained GNN model, and the requirements of this subgraph
depend on parameters of the final model. Specifically, the `num-layer`
parameter determines the number of traversal hops from the target nodes or edges,
and the `fanouts` parameter specifies how many neighbors to sample at
each hop (see [HPO
parameters](machine-learning-customizing-hyperparams.md "machine-learning-customizing-hyperparams.md")).

By default, inductive inference queries run in non-deterministic mode,
in which Neptune builds the neighborhood randomly. When making predictions,
this normal random-neighbor sampling sometimes result in different predictions.

When you include `Neptune#ml.deterministic` in an inductive
inference query, the Neptune engine attempts to sample neighbors in a
deterministic way so that multiple invocations of the same query return
the same results every time. The results can't be guaranteed to be completely
deterministic, however, because changes to the underlying graph and artifacts
of distributed systems can still introduce fluctuations.

You include the `Neptune#ml.deterministic` predicate in a
query like this:

```
.with("Neptune#ml.deterministic")
```

If the `Neptune#ml.deterministic` predicate is included in
a query that doesn't also include `Neptune#ml.inductiveInference`,
it is simply ignored.

## `Neptune#ml.disableInductiveInferenceMetadataCache`

This predicate is an option for inductive inference queries — that is,
for queries that include the [Neptune#ml.inductiveInference](#machine-learning-gremlin-inference-neptune-ml-inductiveInference "#machine-learning-gremlin-inference-neptune-ml-inductiveInference")
predicate.

For inductive inference queries, Neptune uses a metadata file stored in
Amazon S3 to decide the number of hops and the fanout while building the neighborhood.
Neptune normally caches this model metadata to avoid fetching the file from Amazon S3
repeatedly. Caching can be disabled by including the
`Neptune#ml.disableInductiveInferenceMetadataCache` predicate in the
query. Although it may be slower for Neptune to fetch the metadata directly from
Amazon S3, it is useful when the SageMaker AI endpoint has been updated after retraining or
transformation and the cache is stale.

You include the `Neptune#ml.disableInductiveInferenceMetadataCache`
predicate in a query like this:

```
.with("Neptune#ml.disableInductiveInferenceMetadataCache")
```

Here is how a sample query might look in a Jupyter notebook:

```
%%gremlin
g.with("Neptune#ml.endpoint", "ep1")
 .with("Neptune#ml.iamRoleArn", "arn:aws:iam::123456789012:role/NeptuneMLRole")
 .with("Neptune#ml.disableInductiveInferenceMetadataCache")
 .V('101').properties("rating")
 .with("Neptune#ml.regression")
 .with("Neptune#ml.inductiveInference")
```

## `Neptune#ml.endpoint`

The `Neptune#ml.endpoint` predicate is used in a `with()`
step to specify the inference endpoint, if necessary:

```
 .with("Neptune#ml.endpoint", "`the model's SageMaker AI inference endpoint`")
```

You can identify the endpoint either by its `id` or its URL.
For example:

```
 .with( "Neptune#ml.endpoint", "node-classification-movie-lens-endpoint" )
```

Or:

```
 .with( "Neptune#ml.endpoint", "https://runtime.sagemaker.us-east-1.amazonaws.com/endpoints/node-classification-movie-lens-endpoint/invocations" )
```

###### Note

If you [set
the neptune_ml_endpoint parameter](machine-learning-cluster-setup.md#machine-learning-set-inference-endpoint-cluster-parameter "machine-learning-cluster-setup.md#machine-learning-set-inference-endpoint-cluster-parameter") in your Neptune DB cluster
parameter group to the endpoint `id` or URL, you don't need to include the
`Neptune#ml.endpoint` predicate in each query.

## `Neptune#ml.iamRoleArn`

`Neptune#ml.iamRoleArn` is used in a `with()` step to
specify the ARN of the SageMaker AI execution IAM role, if necessary:

```
 .with("Neptune#ml.iamRoleArn", "`the ARN for the SageMaker AI execution IAM role`")
```

For information about how to create the SageMaker AI execution IAM role, see [Create a custom NeptuneSageMakerIAMRole role](machine-learning-manual-setup.md#ml-manual-setup-sm-role "machine-learning-manual-setup.md#ml-manual-setup-sm-role").

###### Note

If you [set the
neptune_ml_iam_role parameter](machine-learning-cluster-setup.md#machine-learning-enabling-create-param-group "machine-learning-cluster-setup.md#machine-learning-enabling-create-param-group") in your Neptune DB cluster
parameter group to the ARN of your SageMaker AI execution IAM role, you don't need
to include the `Neptune#ml.iamRoleArn` predicate in each query.

## Neptune#ml.inductiveInference

Transductive inference is enabled by default in Gremlin. To make a [real-time inductive inference](machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference "machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference")
query, include the `Neptune#ml.inductiveInference` predicate like
this:

```
.with("Neptune#ml.inductiveInference")
```

If your graph is dynamic, inductive inference is often the best choice, but
if your graph is static, transductive inference is faster and more efficient.

## `Neptune#ml.limit`

The `Neptune#ml.limit` predicate optionally limits the number of
results returned per entity:

```
 .with( "Neptune#ml.limit", `2` )
```

By default, the limit is 1, and the maximum number that can be set is 100.

## `Neptune#ml.threshold`

The `Neptune#ml.threshold` predicate optionally establishes a cutoff
threshold for result scores:

```
 .with( "Neptune#ml.threshold", `0.5D` )
```

This lets you discard all results with scores below the specified threshold.

## `Neptune#ml.classification`

The `Neptune#ml.classification` predicate is attached to the
`properties()` step to establish that the properties need to be
fetched from the SageMaker AI endpoint of the node classification model:

```
 .properties( "`property key of the node classification model`" ).with( "Neptune#ml.classification" )
```

## `Neptune#ml.regression`

The `Neptune#ml.regression` predicate is attached to the
`properties()` step to establish that the properties need to be
fetched from the SageMaker AI endpoint of the node regression model:

```
 .properties( "`property key of the node regression model`" ).with( "Neptune#ml.regression" )
```

## `Neptune#ml.prediction`

The `Neptune#ml.prediction` predicate is attached to `in()`
and `out()` steps to establish that this a link-prediction query:

```
 .in("`edge label of the link prediction model`").with("Neptune#ml.prediction").hasLabel("`target node label`")
```

## `Neptune#ml.score`

The `Neptune#ml.score` predicate is used in Gremlin node or edge
classification queries to fetch a machine-learning confidence Score. The
`Neptune#ml.score` predicate should be passed together with the query
predicate in the `properties()` step to obtain an ML confidence score
for node or edge classification queries.

You can find a node classification example with [other node classification
examples](machine-learning-gremlin-vertex-classification-queries.md#machine-learning-gremlin-node-class-other-queries "machine-learning-gremlin-vertex-classification-queries.md#machine-learning-gremlin-node-class-other-queries"), and an edge classification example in the [edge classification section](machine-learning-gremlin-edge-classification-queries.md "machine-learning-gremlin-edge-classification-queries.md").
