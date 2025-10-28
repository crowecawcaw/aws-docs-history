# The targets field in

a neptune_ml object

The `targets` field in a JSON training data export configuration
contains an array of target objects that specify a training task and and the machine-learning
class labels for training this task. The contents of the target objects varies depending
on whether you are training on property-graph data or RDF data.

For property-graph node classification and regression tasks, target objects in the
array can look like this:

```
{
  "node": "`(node property-graph label)`",
  "property": "`(property name)`",
  "type" : "`(used to specify classification or regression)`",
  "split_rate": [0.8,0.2,0.0],
  "separator": ","
}
```

For property-graph edge classification, regression or link prediction tasks, they
can look like this:

```
{
  "edge": "`(edge property-graph label)`",
  "property": "`(property name)`",
  "type" : "`(used to specify classification, regression or link_prediction)`",
  "split_rate": [0.8,0.2,0.0],
  "separator": ","
}
```

For RDF classification and regression tasks, target objects in the array can look
like this:

```
{
  "node": "`(node type of an RDF node)`",
  "predicate": "`(predicate IRI)`",
  "type" : "`(used to specify classification or regression)`",
  "split_rate": [0.8,0.2,0.0]
}
```

For RDF link prediction tasks, target objects in the array can look like this::

```
{
  "subject": "`(source node type of an edge)`",
  "predicate": "`(relation type of an edge)`",
  "object": "`(destination node type of an edge)`",
  "type" : "link_prediction",
  "split_rate": [0.8,0.2,0.0]
}
```

Target objects can contain the following fields:

###### Contents

- [Property-graph target fields](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets")
  - [node](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-node "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-node")
  - [edge](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-edge "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-edge")
  - [property](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-property "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-property")
  - [type](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-type "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-type")
  - [split_rate](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-split_rate "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-split_rate")
  - [separator](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-separator "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-separator")

- [RDF target fields](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets")
  - [node](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-node "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-node")
  - [subject](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-subject "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-subject")
  - [predicate](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-predicate "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-predicate")
  - [object](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-object "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-object")
  - [type](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-type "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-type")
  - [split_rate](machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-split_rate "machine-learning-neptune_ml-targets.md#machine-learning-RDF-neptune_ml-targets-split_rate")

## Fields in a property-graph target object

### The node (vertex) field in a target object

The property-graph label of a target node (vertex). A target object must contain
a `node` element or an `edge` element, but not both.

A `node` can take either a single value, like this:

```
  "node": "Movie"
```

Or, in the case of a multi-label vertex, it can take an array of values,
like this:

```
  "node": ["Content", "Movie"]
```

### The edge field in a property-graph target object

Specifies a target edge by its start node label(s), its own label, and its
end-node label(s). A target object must contain an `edge` element or a
`node` element, but not both.

The value of an `edge` field is a JSON array of three strings that represent the
start-node's property-graph label(s), the property-graph label of
the edge itself, and the end-node's property-graph label(s), like this:

```
  "edge": ["Person_A", "knows", "Person_B"]
```

If the start node and/or end node has multiple labels, enclose them in an array,
like this:

```
  "edge": [ ["Admin", Person_A"], "knows", ["Admin", "Person_B"] ]
```

### The property field in a property-graph target object

Specifies a property of the target vertex or edge, like this:

```
  "property" : "rating"
```

This field is required, except when the target task is link prediction.

### The type field in a property-graph target object

Indicates the type of target task to be performed on the `node` or
`edge`, like this:

```
  "type" : "regression"
```

The supported task types for nodes are:

- `classification`
- `regression`

The supported task types for edges are:

- `classification`
- `regression`
- `link_prediction`

This field is required.

### The split_rate field in a property-graph target object

(_Optional_) An estimate of the proportions of nodes or edges
that the training, validation, and test stages will use, respectively. These
proportions are represented by a JSON array of three numbers between zero and one that
add up to one:

```
"split_rate": [0.7, 0.1, 0.2]
```

If you do not supply the optional `split_rate` field, the default
estimated value is `[0.9, 0.1, 0.0]` for classification and regression tasks, and `[0.9,0.05, 0.05]`
for link prediction tasks.

### The separator field in a property-graph target object

(_Optional_) Used with a classification task.

The `separator` field specifies a character used to split a target
property value into multiple categorical values when it is used to store multiple
category values in a string. For example:

```
"separator": "|"
```

The presence of a `separator` field indicates that the task is a
multi-target classification task.

## Fields in an RDF target object

### The node field in an RDF target object

Defines the node type of target nodes. Used with node classification tasks or node
regression tasks. The node type of a node in RDF is defined by:

```
  node_id, <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>, node_type
```

An RDF `node` can only take a single value, like this:

```
  "node": "http://aws.amazon.com/neptune/csv2rdf/class/Movie"
```

### The subject field in an RDF target object

For link prediction tasks, `subject` defines the source node type
of target edges.

```
  "subject": "http://aws.amazon.com/neptune/csv2rdf/class/Director"
```

###### Note

For link prediction tasks, `subject` should be used together
with `predicate` and `object`. If any of these three is not
provided, all edges are treated as the training target.

### The predicate field in an RDF target object

For node classification and node regression tasks, `predicate` defines
what literal data is used as the target node feature of a target node.

```
  "predicate": "http://aws.amazon.com/neptune/csv2rdf/datatypeProperty/genre"
```

###### Note

If the target nodes have only one predicate defining the target node feature,
the `predicate` field can be omitted.

For link prediction tasks, `predicate` defines the relation type of
target edges:

```
"predicate": "http://aws.amazon.com/neptune/csv2rdf/datatypeProperty/direct"
```

###### Note

For link prediction tasks, `predicate` should be used together
with `subject` and `object`. If any of these three is not
provided, all edges are treated as the training target.

### The object field in an RDF target object

For link prediction tasks, `object` defines the destination node type of target edges:

```
  "object": "http://aws.amazon.com/neptune/csv2rdf/class/Movie"
```

###### Note

For link prediction tasks, `object` should be used together
with `subject` and `predicate`. If any of these three is not
provided, all edges are treated as the training target.

### The type field in an RDF target object

Indicates the type of target task to be performed, like this:

```
  "type" : "regression"
```

The supported task types for RDF data are:

- `link_prediction`
- `classification`
- `regression`

This field is required.

### The `split_rate` field in a property-graph target object

(_Optional_) An estimate of the proportions of nodes or edges
that the training, validation, and test stages will use, respectively. These
proportions are represented by a JSON array of three numbers between zero and one that
add up to one:

```
"split_rate": [0.7, 0.1, 0.2]
```

If you do not supply the optional `split_rate` field, the default
estimated value is `[0.9, 0.1, 0.0]`.
