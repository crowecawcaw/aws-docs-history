# The

structure of JSON training data configuration files

The training configuration file refers to CSV files saved by the export
process in the `nodes/` and `edges/` folders.

Each file under `nodes/` stores information about nodes that
have the same property-graph node label. Each column in a node file stores
either the node ID or the node property. The first line of the file contains
a header that specifies the `~id` or property name for each column.

Each file under `edges/` stores information about nodes that
have the same property-graph edge label. Each column in a node file stores
either the source node ID, the destination node ID, or the edge property.
The first line of the file contains a header specifying the `~from`,
`~to`, or property name for each column.

The training data configuration file has three top-level elements:

```
{
  "version" : "v2.0",
  "query_engine" : "gremlin",
  "graph" : [ `...` ]
}
```

- `version`   –  
  (String) The version of configuration file being used.
- `query_engine`   –  
  (String) The query language used for exporting the graph data. Currently,
  only "gremlin" is valid.
- `graph`   –  
  (JSON array) lists one or more configuration objects that contain model parameters
  for each of the nodes and edges that will be used.

The configuration objects in the graph array have the structure described
in the next section.

## Contents

of a configuration object listed in the `graph` array

A configuration object in the `graph` array can contain three top-level nodes:

```
    {
      "edges"    : [ `...` ],
      "nodes"    : [ `...` ],
      "warnings" : [ `...` ],
    }
```

- `edges`   –   (array of JSON objects)
  Each JSON object specifies a set of parameters to define how an edge in the graph
  will be treated during the model processing and training.
  This is only used with the Gremlin engine.
- `nodes`   –   (array of JSON objects)
  Each JSON object specifies a set of parameters to define how a node in the graph
  will be treated during the model processing and training.
  This is only used with the Gremlin engine.
- `warnings`   –   (array of JSON objects)
  Each object contains a warning generated during the data export process.

## Contents of an edge

configuration object listed in an `edges` array

An edge configuration object listed in an `edges` array can contain
the following top-level fields:

```
      {
        "file_name" : "`(path to a CSV file)`",
        "separator" : "`(separator character)`",
        "source"    : ["`(column label for starting node ID)`", "`(starting node type)`"],
        "relation"  : ["`(column label for the relationship name)`", "`(the prefix name for the relationship name)`"],
        "dest"      : ["`(column label for ending node ID)`", "`(ending node type)`"],
        "features"  : [`(array of feature objects)`],
        "labels"    : [`(array of label objects)`]
      }
```

- **`file_name`**   –  
  A string specifying the path to a CSV file that stores information about edges
  having the same property-graph label.

The first line of that file contains a header line of column labels.

The first two column labels are `~from` and `~to`.
The first column (the `~from` column) stores the ID of the edge's
starting node, and the second (the `~to` column) stores the ID of
the edge's ending node.

The remaining column labels in the header line specify, for each remaining
column, the name of the edge property whose values have been exported into
that column.

- **`separator`**   –  
  A string containing the delimiter that separates columns in that CSV file.
- **`source`**   –  
  A JSON array containing two strings that specify the starting node of the edge.
  The first string contains the header name of the column that the starting node
  ID is stored in. The second string specifies the node type.
- **`relation`**   –  
  A JSON array containing two strings that specify the edge's relation type.
  The first string contains the header name of the column that the relation
  name (`relname`) is stored in. The second string contains the
  prefix for the relation name (`prefixname`).

The full relation type consists of the two strings combined, with a hyphen
character between them, like this:
``prefixname`-`relname``.

If the first string is empty, all edges have the same relation type, namely
the `prefixname` string.

- **`dest`**   –  
  A JSON array containing two strings that specify the ending node of the edge.
  The first string contains the header name of the column that the node
  ID is stored in. The second string specifies the node type.
- **`features`**   –  
  A JSON array of property-value feature objects. Each property-value feature
  object contains the following fields:
  - **feature**   –  
    A JSON array of three strings. The first string contains the header name
    of the column that contains the property value. The second string contains
    the feature name. The third string contains the feature type.
  - **norm**   –  
    (_Optional_) Specifies a normalization method to
    apply to the property values.

- **`labels`**   –  
  A JSON array of objects. Each of the objects defines a target feature of the
  edges, and specifies the proportions of the edges that the training and
  validation stages should take. Each object contains the following fields:
  - **label**   –  
    A JSON array of two strings. The first string contains the header name
    of the column that contains the target feature property value. The
    second string specifies one of the following target task types:
    - `"classification"`   –  
      An edge classification task. The property values provided in
      the column identified by the first string in the `label` array
      are treated as categorical values. For an edge classification task,
      the first string in the `label` array can't be empty.
    - `"regression"`   –  
      An edge regression task. The property values provided in the column
      identified by the first string in the `label` array
      are treated as numerical values. For an edge regression task,
      the first string in the `label` array can't be empty.
    - `"link_prediction"`   –  
      A link prediction task. No property values are required. For a link
      prediction task, the first string in the `label` array
      is ignored.

  - **`split_rate`**   –  
    A JSON array containing three numbers between zero and one that add up to one
    and that represent an estimate of the proportions of nodes that the training,
    validation, and test stages will use, respectively. Either this field or the
    `custom_split_filenames` can be defined, but not both. See [split_rate](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-split_rate "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-split_rate").
  - **`custom_split_filenames`**   –  
    A JSON object that specifies the file names for the files that define the
    training, validation and test populations. Either this field or `split_rate`
    can be defined, but not both. See [Custom train-validation-test proportions](#machine-learning-custom-stages-splits "#machine-learning-custom-stages-splits") for more information.

## Contents of a node

configuration object listed in a `nodes` array

A node configuration object listed in a `nodes` array can contain
the following fields:

```
      {
        "file_name" : "`(path to a CSV file)`",
        "separator" : "`(separator character)`",
        "node"      : ["`(column label for the node ID)`", "`(node type)`"],
        "features"  : [`(feature array)`],
        "labels"    : [`(label array)`],
      }
```

- **`file_name`**   –  
  A string specifying the path to a CSV file that stores information about nodes
  having the same property-graph label.

The first line of that file contains a header line of column labels.

The first column label is `~id`, and the first column (the
`~id` column) stores the node ID.

The remaining column labels in the header line specify, for each remaining
column, the name of the node property whose values have been exported into
that column.

- **`separator`**   –  
  A string containing the delimiter that separates columns in that CSV file.
- **`node`**   –  
  A JSON array containing two strings. The first string contains the header name
  of the column that stores node IDs. The second string specifies the node type
  in the graph, which corresponds to a property-graph label of the node.
- **`features`**   –  
  A JSON array of node feature objects. See [Contents of a feature
  object listed in a features array for a node or edge](#machine-learning-graph-node-features-config "#machine-learning-graph-node-features-config").
- **`labels`**   –  
  A JSON array of node label objects. See [Contents of a node
  label object listed in a node labels array](#machine-learning-graph-node-labels-config "#machine-learning-graph-node-labels-config").

## Contents of a feature

object listed in a `features` array for a node or edge

A node feature object listed in a node `features` array can contain
the following top-level fields:

- **`feature`**   –  
  A JSON array of three strings. The first string contains the header name
  of the column that contains the property value for the feature. The second
  string contains the feature name.

The third string contains the feature type. Valid feature types are listed
in [Possible values of the
type field for features](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-feature-types "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-feature-types").

- **`norm`**   –  
  This field is required for numerical features. It specifies a normalization
  method to use on numeric values. Valid values are `"none"`,
  `"min-max"`, and "standard". See [The norm field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-norm "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-norm") for details.
- **`language`**   –  
  The language field specifies the language being used in text property values. Its
  usage depends on the text encoding method:
  - For [text_fasttext](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features")
    encoding, this field is required, and must specify one of the following languages:

        - `en`   (English)
        - `zh`   (Chinese)
        - `hi`   (Hindi)
        - `es`   (Spanish)
        - `fr`   (French)

    However, `text_fasttext` cannot handle more than one language at a time.

  - For [text_sbert](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features")
    encoding, this field is not used, since SBERT encoding is multilingual.
  - For [text_word2vec](machine-learning-feature-encoding.md#machine-learning-word2vec-features "machine-learning-feature-encoding.md#machine-learning-word2vec-features")
    encoding, this field is optional, since `text_word2vec` only supports English.
    If present, it must specify the name of the English language model:

  ```
  "language" : "en_core_web_lg"
  ```

  - For [tfidf](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features")
    encoding, this field is not used.

- **`max_length`**   –  
  This field is optional for [text_fasttext](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features")
  features, where it specifies the maximum number of tokens in an input text feature
  that will be encoded. Input text after `max_length` is reached is
  ignored. For example, setting max_length to 128 indicates that any tokens after
  the 128th in a text sequence are ignored.
- **`separator`**  –  
  This field is used optionally with `category`, `numerical` and
  `auto` features. It specifies a character that can be used to split a
  property value into multiple categorical values or numerical values.

See [The separator field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-separator "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-separator").

- **`range`**  –  
  This field is required for `bucket_numerical` features. It specifies
  the range of numerical values that are to be divided into buckets.

See [The range field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-range "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-range").

- **`bucket_cnt`**  –  
  This field is required for `bucket_numerical` features. It specifies
  the number of buckets that the numerical range defined by the `range`
  parameter should be divided into.

See [Bucket-numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features "machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features").

- **`slide_window_size`**  –  
  This field is used optionally with `bucket_numerical` features to
  assign values to more than one bucket.

See [The slide_window_size field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-slide_window_size "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-slide_window_size").

- **`imputer`**  –  
  This field is used optionally with `numerical`, `bucket_numerical`,
  and `datetime` features to provide an imputation technique for filling
  in missing values. The supported imputation techniques are `"mean"`,
  `"median"`, and `"most_frequent"`.

See [The imputer field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-imputer "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-imputer").

- **`max_features`**  –  
  This field is used optionally by `text_tfidf` features to specify the
  maximum number of terms to encode.

See [The max_features field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-max_features "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-max_features").

- **`min_df`**  –  
  This field is used optionally by `text_tfidf` features to specify the
  minimum document frequency of terms to encode

See [The min_df field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-min_df "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-min_df").

- **`ngram_range`**  –  
  This field is used optionally by `text_tfidf` features to specify a
  range of numbers of words or tokens to considered as potential individual terms to
  encode

See [The ngram_range field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-ngram_range "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-ngram_range").

- **`datetime_parts`**  –  
  This field is used optionally by `datetime` features to specify which
  parts of the datetime value to encode categorically.

See [The datetime_parts field](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-datetime_parts "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-datetime_parts").

## Contents of a node

label object listed in a node `labels` array

A label object listed in a node `labels` array defines a node target
feature and specifies the proportions of nodes that the training, validation, and test
stages will use. Each object can contain the following fields:

```
      {
        "label"      : ["`(column label for the target feature property value)`", "`(task type)`"],
        "split_rate" : [`(training proportion)`, `(validation proportion)`, `(test proportion)`],
        "custom_split_filenames" : {"train": "`(training file name)`", "valid": "`(validation file name)`", "test": "`(test file name)`"},
        "separator"  : "`(separator character for node-classification category values)`",
      }
```

- **`label`**   –  
  A JSON array containing two strings. The first string contains the header name
  of the column that stores the property values for the feature. The second string
  specifies the target task type, which can be:
  - `"classification"`   –  
    A node classification task. The property values in the specified column are
    used to create a categorical feature.
  - `"regression"`   –  
    A node regression task. The property values in the specified column are
    used to create a numerical feature.

- **`split_rate`**   –  
  A JSON array containing three numbers between zero and one that add up to one and
  represent an estimate of the proportions of nodes that the training, validation,
  and test stages will use, respectively. See [split_rate](machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-split_rate "machine-learning-neptune_ml-targets.md#machine-learning-property-graph-neptune_ml-targets-split_rate").
- **`custom_split_filenames`**   –  
  A JSON object that specifies the file names for the files that define the
  training, validation and test populations. Either this field or `split_rate`
  can be defined, but not both. See [Custom train-validation-test proportions](#machine-learning-custom-stages-splits "#machine-learning-custom-stages-splits") for more information.
- **`separator`**   –  
  A string containing the delimiter that separates categorical feature values for
  a classification task.

###### Note

If no label object is provided for both edges and nodes, the task is
automatically assumed to be link prediction, and edges are randomly split into
90% for training and 10% for validation.

## Custom train-validation-test proportions

By default, the `split_rate` parameter is used by Neptune ML to
split the graph randomly into training, validation and test populations using the
proportions defined in this parameter. To have more precise control over which
entities are used in these different populations, files can be created that
explicitly define them, and then the [training data
configuration file can be edited](machine-learning-processing-training-config-file.md "machine-learning-processing-training-config-file.md") to map these indexing files to the
populations. This mapping is specified by a JSON object for the
[custom_split_filesnames](#custom_split_filenames "#custom_split_filenames")
key in the training configuration file. If this option is used, filenames must be
provided for the `train` and `validation` keys, and is
optional for the `test` key.

The formatting of these files should match the [Gremlin data format](bulk-load-tutorial-format-gremlin.md#bulk-load-tutorial-format-gremlin-systemheaders "bulk-load-tutorial-format-gremlin.md#bulk-load-tutorial-format-gremlin-systemheaders").
Specifically, for node-level tasks, each file should contain a column with the
`~id` header that lists the node IDs, and for edge-level tasks, the
files should specify `~from` and `~to` to indicate the
source and destination nodes of the edges, respectively. These files need to
be placed in the same Amazon S3 location as the exported data that is used for data
processing (see: [outputS3Path](export-parameters.md#export-parameters-outputS3Path "export-parameters.md#export-parameters-outputS3Path")).

For property classification or regression tasks, these files can optionally
define the labels for the machine-learning task. In that case the files need to
have a property column with the same header name as is [defined in the training
data configuration file](#machine-learning-graph-node-labels-config "#machine-learning-graph-node-labels-config"). If property labels are defined in both the
exported node and edge files and the custom-split files, priority is given
to the custom-split files.
