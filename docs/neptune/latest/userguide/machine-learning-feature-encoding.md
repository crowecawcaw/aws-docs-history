# Feature encoding in Neptune ML

Property values come in different formats and data types. To achieve good performance
in machine learning, it is essential to convert those values to numerical encodings known
as _features_.

Neptune ML performs feature extraction and encoding as part of the data-export and
data-processing steps, using feature-encoding techniques described here.

###### Note

If you plan to implement your own feature encoding in a custom model
implementation, you can disable the automatic feature encoding in the data preprocessing
stage by selecting `none` as the feature encoding type. No feature encoding
then occurs on that node or edge property, and instead the raw property values are
parsed and saved in a dictionary. Data preprocessing still creates the DGL graph from
the exported dataset, but the constructed DGL graph doesn't have the pre-processed
features for training.

You should use this option only if you plan to perform your custom feature
encoding as part of custom model training. See [Custom models in Neptune ML](machine-learning-custom-models.md "machine-learning-custom-models.md") for details.

## Categorical features in Neptune ML

A property that can take one or more distinct values from a fixed list of
possible values is a categorical feature. In Neptune ML, categorical features
are encoded using [one-hot
encoding](https://en.wikipedia.org/wiki/One-hot "https://en.wikipedia.org/wiki/One-hot"). The following example shows how the property name of different foods
is one-hot encoded according to its category:

```

    Food        Veg.   Meat   Fruit    Encoding
   ---------    ----   ----   -----    --------
    Apple         0      0      1         001
    Chicken       0      1      0         010
    Broccoli      1      0      0         100
```

###### Note

The maximum number of categories in any categorical feature is 100.
If a property has more than 100 categories of value, only the most common 99 of them
are placed in distinct categories, and the rest are placed in a special category
named `OTHER`.

## Numerical features in Neptune ML

Any property whose values are real numbers can be encoded as a numerical feature in
Neptune ML. Numerical features are encoded using floating-point numbers.

You can specify a data-normalization method to use when encoding numerical
features, like this: `"norm": "`normalization technique`"`.
The following normalization techniques are supported:

- **"none"**   –  
  Don't normalize the numerical values during encoding.
- **"min-max"**   –  
  Normalize each value by subtracting the minimum value from it and then
  dividing it by the difference between the maximum value and the minimum.
- **"standard"**   –  
  Normalize each value by dividing it by the sum of all the values.

## Bucket-numerical features in Neptune ML

Rather than representing a numerical property using raw numbers, you
can condense numerical values into categories. For example, you could divide
people's ages into categories such as kids (0-20), young adults (20-40), middle-aged
people (40-60) and elders (from 60 on). Using these numerical buckets, you would be
transforming a numerical property into a kind of categorical feature.

In Neptune ML, you can cause a numerical property to be encoded as a bucket-numerical
feature, you must provide two things:

- A numerical range in the form, `"range": [`a`,
`b`]` , where `a` and `b`
  are integers.
- A bucket count, in the form `"bucket_cnt":
`c``, where`c` is the number of buckets,
  also an integer.

Neptune ML then calculates the size of each bucket as `( b - a ) / c` ,
and encodes each numeric value as the number of whatever bucket it falls into. Any value
less than `a` is considered to belong in the first bucket, and any value
greater than `b` is considered to belong in the last bucket.

You can also, optionally, make numeric values fall into more than one bucket, by
specifying a slide-window size, like this: `"slide_window_size":
 `s``, where`s`is a number.
 Neptune ML then transforms each numeric value`v`of the property into
 a range from `v - s/2`  through  `v + s/2`, and assigns the value
`v` to every bucket that the range covers.

Finally, you can also optionally provide a way of filling in missing values
for numerical features and bucket-numerical features. You do this using `"imputer": "`imputation technique` "`,
where the imputation technique is one of `"mean"`, `"median"`,
or `"most-frequent"`. If you don't specify an imputer, a missing value
can cause processing to halt.

## Text feature encoding in Neptune ML

For free-form text, Neptune ML can use several different models to convert the
sequence of tokens in a property value string into a fixed-size real-value vector:

- [text_fasttext](#machine-learning-fasttext-features "#machine-learning-fasttext-features")   –  
  Uses [fastText](https://fasttext.cc/ "https://fasttext.cc/") encoding. This is the recommended
  encoding for features that use one and only one of the five languages that fastText supports.
- [text_sbert](#machine-learning-sbert-features "#machine-learning-sbert-features")   –  
  Uses the [Sentence
  BERT](https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models "https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models") (SBERT) encoding models. This is the recommended encoding for text that
  `text_fasttext` does not support.
- [text_word2vec](#machine-learning-word2vec-features "#machine-learning-word2vec-features")   –  
  Uses the [Word2Vec](https://wikipedia.org/wiki/Word2vec "https://wikipedia.org/wiki/Word2vec") algorithms originally
  published by [Google](https://code.google.com/archive/p/word2vec/ "https://code.google.com/archive/p/word2vec/") to
  encode text. Word2Vec only supports English.
- [text_tfidf](#machine-learning-tfidf-features "#machine-learning-tfidf-features")   –  
  Uses a [term frequency–inverse document
  frequency](https://wikipedia.org/wiki/Tf-idf "https://wikipedia.org/wiki/Tf-idf") (TF-IDF) vectorizer for encoding text. TF-IDF encoding supports
  statistical features that the other encodings do not.

### _fastText_ encoding of text property values in Neptune ML

Neptune ML can use the [fastText](https://fasttext.cc/ "https://fasttext.cc/")
models to convert text property values into fixed-size real-value vectors. This is
the recommended encoding method for text property values in any one of the five
languages that fastText supports:

- `en`   (English)
- `zh`   (Chinese)
- `hi`   (Hindi)
- `es`   (Spanish)
- `fr`   (French)

Note that fastText cannot handle sentences containing words in more than one
language.

The `text_fasttext` method can optionally take `max_length`
field that specifies the maximum number of tokens in a text property value
that will be encoded, after which the string is truncated. This can improve performance
when text property values contain long strings, because if `max_length`
is not specified, fastText encodes all the tokens regardless of the string length.

This example specifies that French movie titles are encoded using fastText:

```
{
    "file_name" : "nodes/movie.csv",
    "separator" : ",",
    "node" : ["~id", "movie"],
    "features" : [
      {
        "feature": ["title", "title", "text_fasttext"],
        "language": "fr",
        "max_length": 1024
      }
    ]
  }
```

### Sentence BERT (SBERT) encoding of text features in Neptune ML

Neptune ML can convert the sequence of tokens in a string property value into a
fixed-size real-value vector using [Sentence
BERT](https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models "https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models") (SBERT) models. Neptune supports two SBERT methods: `text_sbert128`,
which is the default if you just specify `text_sbert`, and `text_sbert512`.
The difference between the two is the maximum length of a text property value string that is
encoded. The `text_sbert128` encoding truncates text strings after encoding
128 tokens, while `text_sbert512` truncates text strings after encoding
512 tokens. As a result, `text_sbert512` requires more processing
time than `text_sbert128`. Both methods are slower than `text_fasttext`.

SBERT encoding is multilingual, so there is no need to specify a language for the
property value text you are encoding. SBERT supports many languages, and can encode a
sentence that contains more than one language. If you are encoding property values containing
text in a language or languages that fastText does not support, SBERT is the recommended
encoding method.

The following example specifies that movie titles are encoded as SBERT up to a
maximum of 128 tokens:

```
{
    "file_name" : "nodes/movie.csv",
    "separator" : ",",
    "node" : ["~id", "movie"],
    "features" : [
      { "feature": ["title", "title", "text_sbert128"] }
    ]
  }
```

### Word2Vec encoding of text features in Neptune ML

Neptune ML can encode string property values as a Word2Vec feature ([Word2Vec algorithms](https://wikipedia.org/wiki/Word2vec "https://wikipedia.org/wiki/Word2vec")
were originally published by [Google](https://code.google.com/archive/p/word2vec/ "https://code.google.com/archive/p/word2vec/")). The `text_word2vec`
method encodes the tokens in a string as a dense vector using one of the [spaCy trained models](https://spacy.io/models "https://spacy.io/models"). This only supports the
English language using the [en_core_web_lg](https://spacy.io/models/en#en_core_web_lg "https://spacy.io/models/en#en_core_web_lg") model).

The following example specifies that movie titles are encoded using Word2Vec:

```
{
    "file_name" : "nodes/movie.csv",
    "separator" : ",",
    "node" : ["~id", "movie"],
    "features" : [
      {
        "feature": ["title", "title", "text_word2vec"],
        "language": "en_core_web_lg"
      }
    ]
  }
```

Note that the language field is optional, since the English `en_core_web_lg`
model is the only one that Neptune supports.

### TF-IDF encoding of text features in Neptune ML

Neptune ML can encode text property values as `text_tfidf` features.
This encoding converts the sequence of words in the text into a numeric vector
using a [term frequency–inverse document
frequency](https://wikipedia.org/wiki/Tf-idf "https://wikipedia.org/wiki/Tf-idf") (TF-IDF) vectorizer, followed by a dimensionality-reduction operation.

[TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf "https://en.wikipedia.org/wiki/Tf%E2%80%93idf") (term
frequency – inverse document frequency) is a numerical value intended to measure how
important a word is in a document set. It is calculated by dividing the number of
times a word appears in a given property value by the total number of such property
values that it appears in.

For example, if the word "kiss" appears twice in a given movie title (say,
"kiss kiss bang bang"), and "kiss" appears in the title of 4 movies in all, then
the TF-IDF value of "kiss" in the "kiss kiss bang bang" title would be
`2 / 4` .

The vector that is initially created has **_d_**
dimensions, where **_d_** is
the number of unique terms in all property values of that type. The
dimensionality-reduction operation uses a random sparse projection to reduce
that number to a maximum of 100. The vocabulary of a graph is then generated
by merging all the `text_tfidf` features in it.

You can control the TF-IDF vectorizer in several ways:

- **`max_features`**   –  
  Using the `max_features` parameter, you can limit the number of terms
  in `text_tfidf` features to the most common ones. For example, if you
  set `max_features` to 100, only the top 100 most commonly used terms
  are included. The default value for `max_features` if you don't
  explicitly set it is 5,000.
- **`min_df`**   –  
  Using the `min_df` parameter, you can limit the number of terms
  in `text_tfidf` features to ones having at least a specified
  document frequency. For example, if you set `min_df` to 5, only
  terms that appear in at least 5 different property values are used.
  The default value for `min_df` if you don't explicitly set it is

2.

- **`ngram_range`**   –  
  The `ngram_range` parameter determines what combinations of words
  are treated as terms. For example, if you set `ngram_range`
  to `[2, 4]`, the following 6 terms would be found in the
  "kiss kiss bang bang" title:

      + *2-word terms*:  "kiss kiss", "kiss bang", and "bang bang".
      + *3-word terms*:  "kiss kiss bang" and "kiss bang bang".
      + *4-word terms*:  "kiss kiss bang bang".

  The default setting for `ngram_range` is `[1, 1]`.

## Datetime features in Neptune ML

Neptune ML can convert parts of `datetime` property values into categorical
features by encoding them as [one-hot
arrays](https://en.wikipedia.org/wiki/One-hot "https://en.wikipedia.org/wiki/One-hot"). Use the `datetime_parts` parameter to specify one or more of
the following parts to encode: `["year", "month", "weekday", "hour"]`. If you
don't set `datetime_parts`, by default all four parts are encoded.

For example, if the range of datetime values spans the years 2010 through 2012, the
four parts of the datetime entry `2011-04-22 01:16:34` are as follows:

- **year**   –  
  `[0, 1, 0]`.

Since there are only 3 years in the span (2010, 2011, and 2012), the one-hot
array has three entries, one for each year.

- **month**   –  
  `[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]`.

Here, the one-hot array has an entry for each month of the year.

- **weekday**   –  
  `[0, 0, 0, 0, 1, 0, 0]`.

The ISO 8601 standard states that Monday is the first day
of the week, and since April 22, 2011 was a Friday, the corresponding
one-hot weekday array is hot in the fifth position.

- **hour**   –  
  `[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`.

The hour 1 AM is set in a 24-member one-hot array.

Day of the month, minute, and second are not encoded categorically.

If the total `datetime` range in question only includes dates within
a single year, no `year` array is encoded.

You can specify an imputation strategy to fill in missing `datetime`
values, using the `imputer` parameter and one of the strategies available
for numerical features.

## Auto feature encoding in Neptune ML

Instead of manually specifying the feature encoding methods to use for the properties
in your graph, you can set `auto` as a feature encoding method. Neptune ML
then attempts to infer the best feature encoding for each property based on its underlying
data type.

Here are some of the heuristics that Neptune ML uses in selecting the appropriate
feature encodings:

- If the property has only numeric values and can be cast into numeric data
  types, then Neptune ML generally encodes it as a numeric value. However, if the number
  of unique values for the property is less than 10% of the total number of values and the
  cardinality of those unique values is less than 100, then Neptune ML uses a categorical
  encoding.
- If the property values can be cast to a `datetime` type, then
  Neptune ML encodes them as a `datetime` feature.
- If the property values can be coerced to booleans (1/0 or True/False), then
  Neptune ML uses category encoding.
- If the property is a string with more than 10% of its values unique, and
  the average number of tokens per value is greater than or equal to 3, the Neptune ML
  infers the property type to be text and automatically detects the language being used.
  If the language detected is one of the ones supported by [fastText](#machine-learning-fasttext-features "#machine-learning-fasttext-features"), namely English, Chinese,
  Hindi, Spanish and French, then Neptune ML uses `text_fasttext` to encode
  the text. Othewise, Neptune ML uses [text_sbert](#machine-learning-sbert-features "#machine-learning-sbert-features").
- If the property is a string not classified as a text feature then Neptune
  ML presumes it to be a categorical feature and uses category encoding.
- If each node has its own unique value for a property that is inferred to
  be a category feature, Neptune ML drops the property from the training graph because
  it is probably an ID that would not be informative for learning.
- If the property is known to contain valid Neptune separators such as
  semicolons (";"), then Neptune ML can only treat the property as `MultiNumerical`
  or `MultiCategorical`.
  - Neptune ML first tries to encode the values as numeric features.
    if this succeeds, Neptune ML uses numerical encoding to create numeric vector
    features.
  - Otherwise, Neptune ML encodes the values as multi-categorical.

- If Neptune ML cannot infer the data type of a property's values,
  Neptune MLdrops the property from the training graph.
