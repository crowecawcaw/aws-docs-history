# Amazon Neptune ML for machine learning on graphs

There is often valuable information in large connected datasets that can be hard to
extract using queries based on human intuition alone. Machine learning (ML) techniques
can help find hidden correlations in graphs with billions of relationships. These
correlations can be helpful for recommending products, predicting credit worthiness,
identifying fraud, and many other things.

The Neptune ML feature makes it possible to build and train useful machine learning
models on large graphs in hours instead of weeks. To accomplish this, Neptune ML
uses graph neural network (GNN) technology powered by [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") and the [Deep Graph Library (DGL)](https://www.dgl.ai/ "https://www.dgl.ai/")
(which is [open-source](https://github.com/dmlc/dgl/ "https://github.com/dmlc/dgl/")). Graph neural networks
are an emerging field in artificial intelligence (see, for example, [A Comprehensive Survey on Graph Neural
Networks](https://arxiv.org/abs/1901.00596 "https://arxiv.org/abs/1901.00596")). For a hands-on tutorial about using GNNs with DGL, see [Learning graph neural networks with Deep Graph Library](https://www.amazon.science/videos-webinars/learning-graph-neural-networks-with-deep-graph-library "https://www.amazon.science/videos-webinars/learning-graph-neural-networks-with-deep-graph-library").

###### Note

Graph vertices are identified in Neptune ML models as "nodes". For example,
vertex classification uses a node-classification machine learning model, and vertex
regression uses a node-regression model.

## What Neptune ML can do

Neptune supports both transductive inference, which returns predictions that were
pre-computed at the time of training, based on your graph data at that time, and
inductive inference, which returns applies data processing and model evaluation in
real time, based on current data. See [The difference between inductive and transductive inference](machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference "machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference").

Neptune ML can train machine learning models to support five different
categories of inference:

###### Types of inference task currently supported by Neptune ML

- **Node classification**   –  
  predicting the categorical feature of a vertex property.

For example, given the movie _The Shawshank Redemption_,
Neptune ML can predict its `genre` property as `story`
from a candidate set of `[story, crime, action, fantasy, drama, family, ...]`.

There are two types of node-classification tasks:

    + **Single-class classification**:
     In this kind of task, each node has only one target feature. For example,
     the property, `Place_of_birth` of `Alan Turing` has
     the value `UK`.
    + **Multi-class classification**:
     In this kind of task, each node can have more than one target feature.
     For example, the property `genre` of the film
     *The Godfather* has the values `crime`
     and `story`.

- **Node regression**   –  
  predicting a numerical property of a vertex.

For example, given the movie _Avengers: Endgame_,
Neptune ML can predict that its property `popularity` has a
value of `5.0`.

- **Edge classification**   –  
  predicting the categorical feature of an edge property.

There are two types of edge-classification tasks:

    + **Single-class classification**:
     In this kind of task, each edge has only one target feature. For example,
     a ratings edge between a user and a movie might have the property,
     `liked`, with a value of either "Yes" or "No".
    + **Multi-class classification**:
     In this kind of task, each edge can have more than one target feature.
     For example, a ratings between a user and movie might have multiple values
     for the property tag such as "Funny", "Heartwarming", "Chilling", and
     so on.

- **Edge regression**   –  
  predicting a numerical property of an edge.

For example, a rating edge between a user and a movie might have the
numerical property, `score`, for which Neptune ML could
predict a value given a user and a movie.

- **Link prediction**   –  
  predicting the most likely destination nodes for a particular
  source node and outgoing edge, or the most likely source nodes for a given
  destination node and incoming edge.

For example, with a drug-disease knowledge graph, given `Aspirin` as the
source node, and `treats` as the outgoing edge, Neptune ML can predict the
most relevant destination nodes as `heart disease`, `fever`,
and so on.

Or, with the Wikimedia knowledge graph, given `President-of` as the
edge or relation and `United-States` as the destination node, Neptune ML
can predict the most relevant heads as `George Washington`,
`Abraham Lincoln`, `Franklin D. Roosevelt`, and so on.

###### Note

Node classification and Edge classification only support string values.
That means that numerical property values such as `0` or `1`
are not supported, although the string equivalents `"0"` and `"1"`
are. Similarly, the Boolean property values `true` and `false`
don't work, but `"true"` and `"false"` do.

With Neptune ML, you can use machine learning models that fall in two
general categories:

###### Types of machine learning model currently supported by Neptune ML

- **Graph Neural Network (GNN) models**   –  
  These include [Relational Graph
  Convolutional Networks (R-GCNs)](https://arxiv.org/abs/1703.06103 "https://arxiv.org/abs/1703.06103"). GNN models work for all three types
  of task above.
- **Knowledge-Graph Embedding (KGE) models**   –  
  These include `TransE`, `DistMult`, and `RotatE`
  models. They only work for link prediction.

**User defined models**   –  
Neptune ML also lets you provide your own custom model implementation for all
the types of tasks listed above. You can use the [Neptune ML toolkit](https://github.com/awslabs/neptuneml-toolkit "https://github.com/awslabs/neptuneml-toolkit")
to develop and test your python-based custom model implementation before using
the Neptune ML training API with your model. See [Custom models in Neptune ML](machine-learning-custom-models.md "machine-learning-custom-models.md") for details about how to
structure and organize your implementation so that it's compatible with
Neptune ML's training infrastructure.
