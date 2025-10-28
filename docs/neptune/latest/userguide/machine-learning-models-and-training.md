# Models and model training in Amazon Neptune ML

Neptune ML uses Graph Neural Networks (GNN) to create models for the various
machine-learning tasks. Graph neural networks have been shown to obtain state-of-the-art
results for graph machine learning tasks and are excellent at extracting informative
patterns from graph structured data.

## Graph neural networks (GNNs) in Neptune ML

Graph Neural Networks (GNNs) belong to a family of neural networks that compute
node representations by taking into account the structure and features of nearby nodes.
GNNs complement other traditional machine learning and neural network methods that are
not well-suited for graph data.

GNNs are used to solve machine-learning tasks such as node classification and
regression (predicting properties of nodes) and edge classification and regression
(predicting properties of edges) or link prediction (predicting whether two nodes
in the graph should be connected or not).

In general, using a GNN for a machine learning task involves two stages:

- An encoding stage, where the GNN computes a d-dimensional vector
  for each node in the graph. These vectors are also called _representations_
  or _embeddings_.
- A decoding stage, which makes predictions based on the encoded representations.

For node classification and regression, the node representations are used directly
for the classification and regression tasks. For edge classification and regression,
the node representations of the incident nodes on an edge are used as input for
the classification or regression. For link prediction, an edge likelihood score is
computed by using a pair of node representations and an edge type representation.

The [Deep Graph Library (DGL)](https://www.dgl.ai/ "https://www.dgl.ai/") facilitates
the efficient definition and training of GNNs for these tasks.

Different GNN models are unified under the formulation of message passing.
In this view, the representation for a node in a graph is calculated using the node's
neighbors' representations (the messages), together with the node's initial
representation. In NeptuneML, the initial representation of a node is derived
from the features extracted from its node properties, or is learnable and depends
on the identity of the node.

Neptune ML also provides the option to concatenate node features and learnable
node representations to serve as the original node representation.

For the various tasks in Neptune ML involving graphs with node properties,
we use the [Relational Graph Convolutional
Network](https://arxiv.org/abs/1703.06103 "https://arxiv.org/abs/1703.06103") (R-GCN)) to perform the encoding stage. R-GCN is a GNN architecture
that is well-suited for graphs that have multiple node and edge types (these are
known as heterogeneous graphs).

The R-GCN network consists of a fixed number of layers, stacked one after the
other. Each layer of the R-GCN uses its learnable model parameters to aggregate
information from the immediate, 1-hop neighborhood of a node. Since subsequent
layers use the previous layer's output representations as input, the radius of
the graph neighborhood that influences a node's final embedding depends on the
number of layers (`num-layer`), of the R-GCN network.

For example, this means that a 2-layer network uses information from nodes
that are 2 hops away.

To learn more about GNNs, see [A
Comprehensive Survey on Graph Neural Networks](https://arxiv.org/abs/1901.00596 "https://arxiv.org/abs/1901.00596"). For more information about
the Deep Graph Library (DGL), visit the DGL [webpage](https://www.dgl.ai/ "https://www.dgl.ai/").
For a hands-on tutorial about using DGL with GNNs, see [Learning
graph neural networks with Deep Graph Library](https://www.amazon.science/videos-webinars/learning-graph-neural-networks-with-deep-graph-library "https://www.amazon.science/videos-webinars/learning-graph-neural-networks-with-deep-graph-library").

## Training Graph Neural Networks

In machine learning, the process of getting a model to learn how to make good
predictions for a task is called model training. This is usually performed by
specifying a particular objective to optimize, as well as an algorithm to use to
perform this optimization.

This process is employed in training a GNN to learn good representations for
the downstream task as well. We create an objective function for that task that is
minimized during model training. For example, for node classification, we use [CrossEntropyLoss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html "https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html")
as the objective, which penalizes misclassifications, and for node regression we
minimize [MeanSquareError](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html "https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html").

The objective is usually a loss function that takes the model predictions
for a particular data point and compares them to the ground-truth value for that
data point. It returns the loss value, which shows how far off the model's
predictions are. The goal of the training process is to minimize the loss and
ensure that model predictions are close to the ground-truth.

The optimization algorithm used in deep learning for the training process
is usually a variant of gradient descent. In Neptune ML, we use [Adam](https://arxiv.org/pdf/1412.6980.pdf "https://arxiv.org/pdf/1412.6980.pdf"), which is an algorithm
for first-order gradient-based optimization of stochastic objective functions
based on adaptive estimates of lower-order moments.

While the model training process tries to ensure that the learned model
parameters are close to the minima of the objective function, the overall
performance of a model also depends on the model's _hyperparameters_,
which are model settings that aren't learned by the training algorithm. For
example, the dimensionality of the learned node representation, `num-hidden`,
is a hyperparameter that affects model performance. Therefore, it is
common in machine learning to perform hyperparameter optimization (HPO) to
choose the suitable hyperparameters.

Neptune ML uses a SageMaker AI hyperparameter tuning job to launch multiple
instances of model training with different hyperparameter configurations
to try to find the best model for a range of hyperparameters settings.
See [Customizing model
hyperparameter configurations in Neptune ML](machine-learning-customizing-hyperparams.md "machine-learning-customizing-hyperparams.md").

## Knowledge graph embedding models in Neptune ML

Knowledge graphs (KGs) are graphs that encode information about different entities
(nodes) and their relations (edges). In Neptune ML, knowledge graph embedding models
are applied by default for performing link prediction when the graph does not contain
node properties, only relations with other nodes. Although, R-GCN models with learnable
embeddings can also be used for these graphs by specifying the model type as `"rgcn"`,
knowledge graph embedding models are simpler and are designed to be effective for
learning representations for large scale knowledge graphs.

Knowledge graph embedding models are used in a link prediction task to predict the
nodes or relations that complete a triple `(**h**,
 **r**, **t**)` where
`**h**` is the source node,
`**r**` is the relation type and
`**t**` is the destination node.

The knowledge graph embedding models implemented in Neptune ML are `distmult`,
`transE`, and `rotatE`. To learn more about knowledge graph embedding
models, see [DGL-KE](https://github.com/awslabs/dgl-ke "https://github.com/awslabs/dgl-ke").

## Training custom models in Neptune ML

Neptune ML lets you define and implement custom models of your own, for particular
scenarios. See [Custom models in Neptune ML](machine-learning-custom-models.md "machine-learning-custom-models.md") for information about how to implement
a custom model and how to use Neptune ML infrastructure to train it.
