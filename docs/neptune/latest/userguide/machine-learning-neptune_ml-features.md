# The features field

in neptune_ml

Property values and RDF literals come in different formats and data types. To achieve
good performance in machine learning, it is essential to convert those values to
numerical encodings known as _features_.

Neptune ML performs feature extraction and encoding as part of the data-export and
data-processing steps, as described in [Feature encoding in Neptune ML](machine-learning-feature-encoding.md "machine-learning-feature-encoding.md").

For property-graph datasets, the export process automatically infers `auto`
features for string properties and for numeric properties that contain multiples values.
For numeric properties containing single values, it infers `numerical` features.
For date properties it infers `datetime` features.

If you want to override an auto-inferred feature specification, or add a
bucket numerical, TF-IDF, FastText, or SBERT specification for a property,
you can control the feature encoding using the features field.

###### Note

You can only use the `features` field to control the feature
specifications for property-graph data, not for RDF data.

For free-form text, Neptune ML can use several different models to convert the sequence
of tokens in a string property value into a fixed-size real-value vector:

- [text_fasttext](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features")   –  
  Uses [fastText](https://fasttext.cc/ "https://fasttext.cc/") encoding. This is the recommended
  encoding for features that use one and only one of the five languages that fastText supports.
- [text_sbert](machine-learning-feature-encoding.md#machine-learning-sbert-features "machine-learning-feature-encoding.md#machine-learning-sbert-features")   –  
  Uses the [Sentence
  BERT](https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models "https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models") (SBERT) encoding models. This is the recommended encoding for text that
  `text_fasttext` does not support.
- [text_word2vec](machine-learning-feature-encoding.md#machine-learning-word2vec-features "machine-learning-feature-encoding.md#machine-learning-word2vec-features")   –  
  Uses [Word2Vec](https://wikipedia.org/wiki/Word2vec "https://wikipedia.org/wiki/Word2vec") algorithms originally
  published by [Google](https://code.google.com/archive/p/word2vec/ "https://code.google.com/archive/p/word2vec/") to
  encode text. Word2Vec only supports English.
- [text_tfidf](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features")   –  
  Uses a [term frequency–inverse document
  frequency](https://wikipedia.org/wiki/Tf-idf "https://wikipedia.org/wiki/Tf-idf") (TF-IDF) vectorizer for encoding text. TF-IDF encoding supports
  statistical features that the other encodings do not.
  The `features` field contains a JSON array of node property features.
  Objects in the array can contain the following fields:

###### Contents

- [node](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-node "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-node")
- [edge](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-edge "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-edge")
- [property](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-property "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-property")
- [type](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-feature-types "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-feature-types")
- [norm](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-norm "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-norm")
- [language](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-language "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-language")
- [max_length](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-max_length "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-max_length")
- [separator](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-separator "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-separator")
- [range](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-range "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-range")
- [bucket_cnt](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-bucket_cnt "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-bucket_cnt")
- [slide_window_size](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-slide_window_size "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-slide_window_size")
- [imputer](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-imputer "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-imputer")
- [max_features](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-max_features "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-max_features")
- [min_df](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-min_df "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-min_df")
- [ngram_range](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-ngram_range "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-ngram_range")
- [datetime_parts](machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-datetime_parts "machine-learning-neptune_ml-features.md#machine-learning-neptune_ml-features-datetime_parts")

## The node field in features

The `node` field specifies a property-graph label of a feature vertex.
For example:

```
  "node": "Person"
```

If a vertex has multiple labels, use an array to contain them. For example:

```
  "node": ["Admin", "Person"]
```

## The edge field in features

The `edge` field specifies the edge type of a feature edge. An edge type
consists of an array containing the property-graph label(s) of the source vertex, the
property-graph label of the edge, and the property-graph label(s) of the destination
vertex. You must supply all three values when specifying an edge feature. For example:

```
  "edge": ["User", "reviewed", "Movie"]
```

If a source or destination vertex of an edge type has multiple labels, use another
array to contain them. For example:

```
  "edge": [["Admin", "Person"]. "edited", "Post"]
```

## The property field in features

Use the property parameter to specify a property of the vertex identified by the
`node` parameter. For example:

```
  "property" : "age"
```

## Possible values of the

type field for features

The `type` parameter specifies the type of feature being defined.
For example:

```
  "type": "bucket_numerical"
```

###### Possible values of the `type` parameter

- **`"auto"`**   –  
  Specifies that Neptune ML should automatically detect the property type and
  apply a proper feature encoding. An `auto` feature can also have an
  optional `separator` field.

See [Auto feature encoding in Neptune ML](machine-learning-feature-encoding.md#machine-learning-auto-encoding "machine-learning-feature-encoding.md#machine-learning-auto-encoding").

- **`"category"`**   –  
  This feature encoding represents a property value as one of a number of
  categories. In other words, the feature can take one or more discrete values.
  A `category` feature can also have an optional `separator` field.

See [Categorical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-categorical-features "machine-learning-feature-encoding.md#machine-learning-categorical-features").

- **`"numerical"`**   –  
  This feature encoding represents numerical property values as numbers
  in a continuous interval where "greater than" and "less than" have meaning.

A `numerical` feature can also have optional `norm`,
`imputer`, and `separator` fields.

See [Numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-numerical-features "machine-learning-feature-encoding.md#machine-learning-numerical-features").

- **`"bucket_numerical"`**   –  
  This feature encoding divides numerical property values into a set of
  _buckets_ or categories.

For example, you could encode people's ages in 4 buckets: kids (0-20),
young-adults (20-40), middle-aged (40-60), and elders (60 and up).

A `bucket_numerical` feature requires a `range`
and a `bucket_cnt` field, and can optionally also include
an `imputer` and/or `slide_window_size` field.

See [Bucket-numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features "machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features").

- **`"datetime"`**   –  
  This feature encoding represents a datetime property value as an array of
  these categorical features: year, month, weekday, and hour.

One or more of these four categories can be eliminated using the
`datetime_parts` parameter.

See [Datetime features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-datetime-features "machine-learning-feature-encoding.md#machine-learning-datetime-features").

- **`"text_fasttext"`**   –  
  This feature encoding converts property values that consist of
  sentences or free-form text into numeric vectors using [fastText](https://fasttext.cc/ "https://fasttext.cc/") models. It supports five
  languages, namely English (`en`), Chinese (`zh`),
  Hindi (`hi`), Spanish (`es`), and French
  (`fr`). For text property values in any one those five
  languages, `text_fasttext` is the recommended encoding.
  However, it cannot handle cases where the same sentence contains
  words in more than one language.

For other languages than the ones that fastText supports, use
`text_sbert` encoding.

If you have many property value text strings longer than, say,
120 tokens, use the `max_length` field to limit
the number of tokens in each string that `"text_fasttext"` encodes.

See [fastText encoding of text property values in Neptune ML](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features").

- **`"text_sbert"`**   –  
  This encoding converts text property values into numeric vectors using [Sentence
  BERT](https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models "https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models") (SBERT) models. Neptune supports two SBERT methods, namely `text_sbert128`,
  which is the default if you just specify `text_sbert`, and `text_sbert512`.
  The difference between them is the maximum number of tokens in a text property that gets
  encoded. The `text_sbert128` encoding only encodes the first 128 tokens, while
  `text_sbert512` encodes up to 512 tokens. As a result, using `text_sbert512`
  can require more processing time than `text_sbert128`. Both methods are slower than
  `text_fasttext`.

The `text_sbert`\*`` methods support many
languages, and can encode a sentence that contains more than one language.

See [Sentence BERT (SBERT) encoding of text features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-sbert-features "machine-learning-feature-encoding.md#machine-learning-sbert-features").

- **`"text_word2vec"`**   –  
  This encoding converts text property values into numeric vectors using
  [Word2Vec](https://wikipedia.org/wiki/Word2vec "https://wikipedia.org/wiki/Word2vec") algorithms.
  It only supports English.

See [Word2Vec encoding of text features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-word2vec-features "machine-learning-feature-encoding.md#machine-learning-word2vec-features").

- **`"text_tfidf"`**   –  
  This encoding converts text property values into numeric vectors using a [term frequency–inverse document frequency](https://wikipedia.org/wiki/Tf-idf "https://wikipedia.org/wiki/Tf-idf")
  (TF-IDF) vectorizer.

You define the parameters of a `text_tfidf` feature encoding
using the `ngram_range` field, the `min_df` field, and
the `max_features` field.

See [TF-IDF encoding of text features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features").

- **`"none"`**   –  
  Using the `none` type causes no feature encoding to occur.
  The raw property values are parsed and saved instead.

Use `none` only if you plan to perform your own custom feature
encoding as part of custom model training.

## The norm field

This field is required for numerical features. It specifies a normalization
method to use on numeric values:

```
"norm": "min-max"
```

The following normalization methods are supported:

- **"min-max"**   –  
  Normalize each value by subtracting the minimum value from it and then
  dividing it by the difference between the maximum value and the minimum.
- **"standard"**   –  
  Normalize each value by dividing it by the sum of all the values.
- **"none"**   –  
  Don't normalize the numerical values during encoding.

See [Numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-numerical-features "machine-learning-feature-encoding.md#machine-learning-numerical-features").

## The language field

The language field specifies the language used in text property values. Its usage
depends on the text encoding method:

- For [text_fasttext](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features")
  encoding, this field is required, and must specify one of the following languages:
  - `en`   (English)
  - `zh`   (Chinese)
  - `hi`   (Hindi)
  - `es`   (Spanish)
  - `fr`   (French)

- For [text_sbert](machine-learning-feature-encoding.md#machine-learning-fasttext-features "machine-learning-feature-encoding.md#machine-learning-fasttext-features")
  encoding, this field is not used, since SBERT encoding is multilingual.
- For [text_word2vec](machine-learning-feature-encoding.md#machine-learning-word2vec-features "machine-learning-feature-encoding.md#machine-learning-word2vec-features")
  encoding, this field is optional, since `text_word2vec` only supports English.
  If present, it must specify the name of the English language model:

```
"language" : "en_core_web_lg"
```

- For [text_tfidf](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features")
  encoding, this field is not used.

## The max_length field

The `max_length` field is optional for `text_fasttext`
features, where it specifies the maximum number of tokens in an input text feature
that will be encoded. Input text that is longer than `max_length` is
truncated. For example, setting max_length to 128 indicates that any tokens after
the 128th in a text sequence will be ignored:

```
"max_length": 128
```

## The separator field

This field is used optionally with `category`, `numerical` and
`auto` features. It specifies a character that can be used to split a property
value into multiple categorical values or numerical values:

```
"separator": ";"
```

Only use the `separator` field when the property stores multiple
delimited values in a single string, such as `"Actor;Director"` or
`"0.1;0.2"`.

See [Categorical features](machine-learning-feature-encoding.md#machine-learning-categorical-features "machine-learning-feature-encoding.md#machine-learning-categorical-features"),
[Numerical features](machine-learning-feature-encoding.md#machine-learning-numerical-features "machine-learning-feature-encoding.md#machine-learning-numerical-features"),
and [Auto encoding](machine-learning-feature-encoding.md#machine-learning-auto-encoding "machine-learning-feature-encoding.md#machine-learning-auto-encoding").

## The range field

This field is required for `bucket_numerical` features. It specifies
the range of numerical values that are to be divided into buckets, in the format
`[`lower-bound`, `upper-bound`]`:

```
"range" : [20, 100]
```

If a property value is smaller than the lower bound then it is assigned to the
first bucket, or if it's larger than the upper bound, it's assigned to the last bucket.

See [Bucket-numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features "machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features").

## The bucket_cnt field

This field is required for `bucket_numerical` features. It specifies
the number of buckets that the numerical range defined by the `range`
parameter should be divided into:

```
"bucket_cnt": 10
```

See [Bucket-numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features "machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features").

## The slide_window_size field

This field is used optionally with `bucket_numerical` features to
assign values to more than one bucket:

```
"slide_window_size": 5
```

The way a slide window works is that Neptune ML takes the window size
**`s`** and transforms each numeric
value **`v`** of a property into
a range from `v - s/2` through `v + s/2` . The value
is then assigned to every bucket that the range overlaps.

See [Bucket-numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features "machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features").

## The imputer field

This field is used optionally with `numerical` and `bucket_numerical`
features to provide an imputation technique for filling in missing values:

```
"imputer": "mean"
```

The supported imputation techniques are:

- `"mean"`
- `"median"`
- `"most-frequent"`

If you don't include the imputer parameter, data preprocessing halts and exits
when a missing value is encountered.

See [Numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-numerical-features "machine-learning-feature-encoding.md#machine-learning-numerical-features") and [Bucket-numerical features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features "machine-learning-feature-encoding.md#machine-learning-bucket_numerical-features").

## The max_features field

This field is used optionally by `text_tfidf` features to specify the
maximum number of terms to encode:

```
"max_features": 100
```

A setting of 100 causes the TF-IDF vectorizer to encode only the 100 most
common terms. The default value if you don't include `max_features`
is 5,000.

See [TF-IDF encoding of text features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features").

## The min_df field

This field is used optionally by `text_tfidf` features to specify the
minimum document frequency of terms to encode:

```
"min_df": 5
```

A setting of 5 indicates that a term must appear in at least 5 different property
values in order to be encoded.

The default value if you don't include the `min_df` parameter is
`2`.

See [TF-IDF encoding of text features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features").

## The ngram_range field

This field is used optionally by `text_tfidf` features to specify what
size sequences of words or tokens should be considered as potential individual terms to encode:

```
"ngram_range": [2, 4]
```

The value `[2, 4]` specifies that sequences of 2, 3 and 4 words should be
considered as potential individual terms.

The default if you don't explicitly set `ngram_range` is `[1, 1]`,
meaning that only single words or tokens are considered as terms to encode.

See [TF-IDF encoding of text features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-tfidf-features "machine-learning-feature-encoding.md#machine-learning-tfidf-features").

## The datetime_parts field

This field is used optionally by `datetime` features to specify which
parts of the datetime value to encode categorically:

```
"datetime_parts": ["weekday", "hour"]
```

If you don't include `datetime_parts`, by default Neptune ML
encodes the year, month, weekday and hour parts of the datetime value. The value
`["weekday", "hour"]` indicates that only the weekday and hour of
datetime values should be encoded categorically in the feature.

If one of the parts does not have more than one unique value in the
training set, it is not encoded.

See [Datetime features in Neptune ML](machine-learning-feature-encoding.md#machine-learning-datetime-features "machine-learning-feature-encoding.md#machine-learning-datetime-features").
