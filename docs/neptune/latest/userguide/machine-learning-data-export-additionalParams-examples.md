# Examples

of using parameters within additionalParams for tuning model-training configuration

The following examples demonstrate how to utilize the "additionalParams" feature in property-graph and RDF data models to
configure various aspects of the model training process for a Neptune ML application. The examples cover a wide range of
functionality, including specifying default split rates for training/validation/test data, defining node classification,
regression, and link prediction tasks, as well as configuring different feature types such as numerical buckets, text embeddings,
datetime, and categorical data. These detailed configurations allow you to tailor the machine learning pipeline to your
specific data and modeling requirements, unlocking the full potential of the Neptune ML capabilities.

###### Contents

- [Property-graph examples using additionalParams](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-examples "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-examples")
  - [Specifying a default split rate for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-default-split-rate-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-default-split-rate-example")
  - [Specifying a node-classification task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-node-classification-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-node-classification-example")
  - [Specifying a multi-class node classification task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-multi-class-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-multi-class-example")
  - [Specifying a node regression task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-node-regression-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-node-regression-example")
  - [Specifying an edge-classification task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-edge-classification-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-edge-classification-example")
  - [Specifying a multi-class edge classification task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-multi-edge-classification-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-multi-edge-classification-example")
  - [Specifying an edge regression for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-edge-regression-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-edge-regression-example")
  - [Specifying a link prediction task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-link-prediction-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-link-prediction-example")
  - [Specifying a numerical bucket feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-numeric-bucket-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-numeric-bucket-example")
  - [Specifying a Word2Vec feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-word2vec-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-word2vec-example")
  - [Specifying a FastText feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-fasttext-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-fasttext-example")
  - [Specifying a Sentence BERT feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-sbert-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-sbert-example")
  - [Specifying a TF-IDF feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-tf-idf-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-tf-idf-example")
  - [Specifying a datetime feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-datetime-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-datetime-example")
  - [Specifying a category feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-category-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-category-example")
  - [Specifying a numerical feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-numerical-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-numerical-example")
  - [Specifying an auto feature](machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-auto-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-property-graph-additionalParams-auto-example")

- [RDF examples using additionalParams](machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-examples "machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-examples")
  - [Specifying a default split rate for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-default-split-rate-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-default-split-rate-example")
  - [Specifying a node-classification task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-node-classification-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-node-classification-example")
  - [Specifying a node regression task for model-training configuration](machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-node-regression-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-node-regression-example")
  - [Specifying
    a link prediction task for particular edges](machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-link-prediction-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-link-prediction-example")
  - [Specifying
    a link prediction task for all edges](machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-link-prediction-example "machine-learning-data-export-additionalParams-examples.md#machine-learning-RDF-additionalParams-link-prediction-example")

## Property-graph examples using additionalParams

### Specifying a default split rate for model-training configuration

In the following example, the `split_rate` parameter sets the default
split rate for model training. If no default split rate is specified, the training uses
a value of [0.9, 0.1, 0.0]. You can override the default value on a per-target basis
by specifying a `split_rate` for each target.

In the following example, the `default split_rate` field indicates
that a split rate of `[0.7,0.1,0.2]` should be used unless overridden on
a per-target basis:"

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "split_rate": [0.7,0.1,0.2],
    "targets": [
      `(...)`
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying a node-classification task for model-training configuration

To indicate which node property contains labeled examples for training purposes,
add a node classification element to the `targets` array, using `"type" :
 "classification"`. Add a `split_rate` field if you want to override
the default split rate.

In the following example, the `node` target indicates that the
`genre` property of each `Movie` node should be treated
as a node class label. The `split_rate` value overrides the default
split rate:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "node": "Movie",
        "property": "genre",
        "type": "classification",
        "split_rate": [0.7,0.1,0.2]
      }
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying a multi-class node classification task for model-training configuration

To indicate which node property contains multiple labeled examples for training
purposes, add a node classification element to the targets array, using `"type" :
 "classification"`, and `separator` to specify a character that can be
used to split a target property value into multiple categorical values. Add a
`split_rate` field if you want to override the default split rate.

In the following example, the `node` target indicates that the
`genre` property of each `Movie` node should be treated
as a node class label. The `separator` field indicates that each
genre property contains multiple semicolon-separated values:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "node": "Movie",
        "property": "genre",
        "type": "classification",
        "separator": ";"
      }
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying a node regression task for model-training configuration

To indicate which node property contains labeled regressions for training purposes,
add a node regression element to the targets array, using `"type" : "regression"`.
Add a split_rate field if you want to override the default split rate.

The following `node` target indicates that the `rating`
property of each `Movie` node should be treated as a node regression label:

```
    "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "node": "Movie",
        "property": "rating",
        "type" : "regression",
        "split_rate": [0.7,0.1,0.2]
      }
    ],
    "features": [
      `...`
    ]
  }
}
```

### Specifying an edge-classification task for model-training configuration

To indicate which edge property contains labeled examples for training purposes,
add an edge element to the `targets` array, using `"type" : "regression"`.
Add a split_rate field if you want to override the default split rate.

The following `edge` target indicates that the `metAtLocation`
property of each `knows` edge should be treated as an edge class label:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "edge": ["Person", "knows", "Person"],
        "property": "metAtLocation",
        "type": "classification"
      }
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying a multi-class edge classification task for model-training configuration

To indicate which edge property contains multiple labeled examples for training purposes,
add an edge element to the `targets` array, using `"type" : "classification"`,
and a `separator` field to specify a character used to split a target property
value into multiple categorical values. Add a `split_rate` field if you want to
override the default split rate.

The following `edge` target indicates that the `sentiment`
property of each `repliedTo` edge should be treated as an edge class label.
The separator field indicates that each sentiment property contains multile comma-separated
values:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "edge": ["Person", "repliedTo", "Message"],
        "property": "sentiment",
        "type": "classification",
        "separator": ","
      }
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying an edge regression for model-training configuration

To indicate which edge property contains labeled regression examples for training
purposes, add an `edge` element to the `targets` array, using
`"type" : "regression"`. Add a `split_rate` field if you want
to override the default split rate.

The following `edge` target indicates that the `rating`
property of each `reviewed` edge should be treated as an edge regression:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "edge": ["Person", "reviewed", "Movie"],
        "property": "rating",
        "type" : "regression"
      }
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying a link prediction task for model-training configuration

To indicate which edges should be used for link prediction training purposes, add
an edge element to the targets array using `"type" : "link_prediction"`.
Add a `split_rate` field if you want to override the default split rate.

The following `edge` target indicates that `cites` edges
should be used for link prediction:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "edge": ["Article", "cites", "Article"],
        "type" : "link_prediction"
      }
    ],
    "features": [
      `(...)`
    ]
  }
}
```

### Specifying a numerical bucket feature

You can specify a numerical data feature for a node property by adding
`"type": "bucket_numerical"` to the `features` array.

The following `node` feature indicates that the `age`
property of each `Person` node should be treated as a numerical
bucket feature:

```
  "additionalParams": {
  "neptune_ml": {
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Person",
        "property": "age",
        "type": "bucket_numerical",
        "range": [1, 100],
        "bucket_cnt": 5,
        "slide_window_size": 3,
        "imputer": "median"
      }
    ]
  }
}
```

### Specifying a `Word2Vec` feature

You can specify a `Word2Vec` feature for a node property by adding
`"type": "text_word2vec"` to the `features` array.

The following `node` feature indicates that the `description`
property of each `Movie` node should be treated as a `Word2Vec`
feature:

```
"additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Movie",
        "property": "description",
        "type": "text_word2vec",
        "language": "en_core_web_lg"
      }
    ]
  }
}
```

### Specifying a `FastText` feature

You can specify a `FastText` feature for a node property by adding
`"type": "text_fasttext"` to the `features` array. The
`language` field is required, and must specify one of the following
languages codes:

- `en`   (English)
- `zh`   (Chinese)
- `hi`   (Hindi)
- `es`   (Spanish)
- `fr`   (French)

Note that the `text_fasttext` encoding cannot handle more than
one language at a time in a feature.

The following `node` feature indicates that the French `description`
property of each `Movie` node should be treated as a `FastText`
feature:

```
"additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Movie",
        "property": "description",
        "type": "text_fasttext",
        "language": "fr",
        "max_length": 1024
      }
    ]
  }
}
```

### Specifying a `Sentence BERT` feature

You can specify a `Sentence BERT` feature for a node property by adding
`"type": "text_sbert"` to the `features` array. You don't need
to specify the language, since the method automatically encodes text features using
a multilingual language model.

The following `node` feature indicates that the `description`
property of each `Movie` node should be treated as a `Sentence BERT`
feature:

```
"additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Movie",
        "property": "description",
        "type": "text_sbert128",
      }
    ]
  }
}
```

### Specifying a `TF-IDF` feature

You can specify a `TF-IDF` feature for a node property by adding
`"type": "text_tfidf"` to the `features` array.

The following `node` feature indicates that the `bio`
property of each `Person` node should be treated as a `TF-IDF`
feature:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Movie",
        "property": "bio",
        "type": "text_tfidf",
        "ngram_range": [1, 2],
        "min_df": 5,
        "max_features": 1000
      }
    ]
  }
}
```

### Specifying a `datetime` feature

The export process automatically infers `datetime` features for date
properties. However, if you want to limit the `datetime_parts` used for
a `datetime` feature, or override a feature specification so that a property
that would normally be treated as an `auto` feature is explicitly treated as a
`datetime` feature, you can do so by adding a `"type": "datetime"`
to the features array.

The following `node` feature indicates that the `createdAt`
property of each `Post` node should be treated as a `datetime`
feature:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Post",
        "property": "createdAt",
        "type": "datetime",
        "datetime_parts": ["month", "weekday", "hour"]
      }
    ]
  }
}
```

### Specifying a `category` feature

The export process automatically infers `auto` features for string
properties and numeric properties containing multiples values. For numeric properties
containing single values, it infers `numerical` features. For date
properties it infers `datetime` features.

If you want to override a feature specification so that a property is treated
as a categorical feature, add a `"type": "category"` to the features array.
If the property contains multiple values, include a `separator` field.
For example:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Post",
        "property": "tag",
        "type": "category",
        "separator": "|"
      }
    ]
  }
}
```

### Specifying a `numerical` feature

The export process automatically infers `auto` features for string
properties and numeric properties containing multiples values. For numeric properties
containing single values, it infers `numerical` features. For date
properties it infers `datetime` features.

If you want to override a feature specification so that a property is treated as a
`numerical` feature, add `"type": "numerical"` to the features array.
If the property contains multiple values, include a `separator` field.
For example:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "Recording",
        "property": "duration",
        "type": "numerical",
        "separator": ","
      }
    ]
  }
}
```

### Specifying an `auto` feature

The export process automatically infers `auto` features for string
properties and numeric properties containing multiples values. For numeric properties
containing single values, it infers `numerical` features. For date
properties it infers `datetime` features.

If you want to override a feature specification so that a property is treated
as an `auto` feature, add `"type": "auto"` to the features array.
If the property contains multiple values, include a `separator` field.
For example:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      `...`
    ],
    "features": [
      {
        "node": "User",
        "property": "role",
        "type": "auto",
        "separator": ","
      }
    ]
  }
}
```

## RDF examples using `additionalParams`

### Specifying a default split rate for model-training configuration

In the following example, the `split_rate` parameter sets the default
split rate for model training. If no default split rate is specified, the training uses
a value of [0.9, 0.1, 0.0]. You can override the default value on a per-target basis
by specifying a `split_rate` for each target.

In the following example, the `default split_rate` field indicates
that a split rate of `[0.7,0.1,0.2]` should be used unless overridden on
a per-target basis:"

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "split_rate": [0.7,0.1,0.2],
    "targets": [
      `(...)`
    ]
  }
}
```

### Specifying a node-classification task for model-training configuration

To indicate which node property contains labeled examples for training purposes,
add a node classification element to the `targets` array, using `"type" :
 "classification"`. Add a node field to indicate the node type of target nodes.
Add a `predicate` field to define which literal data is used as the target
node feature of the target node. Add a `split_rate` field if you want to
override the default split rate.

In the following example, the `node` target indicates that the
`genre` property of each `Movie` node should be treated
as a node class label. The `split_rate` value overrides the default
split rate:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "node": "http://aws.amazon.com/neptune/csv2rdf/class/Movie",
        "predicate": "http://aws.amazon.com/neptune/csv2rdf/datatypeProperty/genre",
        "type": "classification",
        "split_rate": [0.7,0.1,0.2]
      }
    ]
  }
}
```

### Specifying a node regression task for model-training configuration

To indicate which node property contains labeled regressions for training purposes,
add a node regression element to the targets array, using `"type" : "regression"`.
Add a `node` field to indicate the node type of target nodes. Add a
`predicate` field to define which literal data is used as the target node
feature of the target node. Add a `split_rate` field if you want to override
the default split rate.

The following `node` target indicates that the `rating`
property of each `Movie` node should be treated as a node regression label:

```
    "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "node": "http://aws.amazon.com/neptune/csv2rdf/class/Movie",
        "predicate": "http://aws.amazon.com/neptune/csv2rdf/datatypeProperty/rating",
        "type": "regression",
        "split_rate": [0.7,0.1,0.2]
      }
    ]
  }
}
```

### Specifying

a link prediction task for particular edges

To indicate which edges should be used for link prediction training purposes, add
an edge element to the targets array using `"type" : "link_prediction"`.
Add `subject`, `predicate` and `object` fields to
specify the edge type. Add a `split_rate` field if you want to override
the default split rate.

The following `edge` target indicates that `directed` edges
that connect `Directors` to `Movies` should be used for link
prediction:

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "subject": "http://aws.amazon.com/neptune/csv2rdf/class/Director",
        "predicate": "http://aws.amazon.com/neptune/csv2rdf/datatypeProperty/directed",
        "object": "http://aws.amazon.com/neptune/csv2rdf/class/Movie",
        "type" : "link_prediction"
      }
    ]
  }
}
```

### Specifying

a link prediction task for all edges

To indicate that all edges should be used for link prediction training purposes,
add an `edge` element to the targets array using `"type" :
 "link_prediction"`. Do not add `subject`, `predicate`, or
`object` fields. Add a `split_rate` field if you want to override
the default split rate.

```
  "additionalParams": {
  "neptune_ml": {
    "version": "v2.0",
    "targets": [
      {
        "type" : "link_prediction"
      }
    ]
  }
}
```
