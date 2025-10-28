# Making predictions based on evolving graph data

With a continuously changing graph, you may want to create new batch predictions
periodically using fresh data. Querying pre-computed predictions (transductive
inference) can be significantly faster than generating new predictions on the fly
based on the very latest data (inductive inference). Both approaches have their place,
depending on how rapidly your data changes and on your performance requirements.

## The difference between inductive and transductive inference

When performing transductive inference, Neptune looks up and returns
predictions that were pre-computed at the time of training.

When performing inductive inference, Neptune constructs the relevant
subgraph and fetches its properties. The DGL GNN model then applies data
processing and model evaluation in real-time.

Inductive inference can therefore generate predictions involving nodes
and edges that were not present at the time of training and that reflect
the current state of the graph. This comes, however, at the cost of higher
latency.

If your graph is dynamic, you may want to use inductive inference to be sure to
take into account the latest data, but if your graph is static, transductive inference
is faster and more efficient.

Inductive inference is disabled by default. You can enable it for a query
by using the Gremlin [Neptune#ml.inductiveInference](machine-learning-gremlin-inference-query-predicates.md#machine-learning-gremlin-inference-neptune-ml-inductiveInference "machine-learning-gremlin-inference-query-predicates.md#machine-learning-gremlin-inference-neptune-ml-inductiveInference")
predicate in the query as follows:

```
.with( "Neptune#ml.inductiveInference")
```
