# Tabular data

Tabular data refers to data that can be loaded into a two-dimensional data frame. In
the frame, each row represents a record, and each record has one or more columns. The
values within each data frame cell can be of numerical, categorical, or text data
types.

## Tabular dataset

prerequisites

Prior to analysis, your dataset should have had any necessary pre-processing steps
already applied. This includes data cleaning or feature engineering.

You can provide one or multiple datasets. If you provide multiple datasets, use
the following to identify them to the SageMaker Clarify processing job.

- Use either a [ProcessingInput](../APIReference/API_ProcessingInput.md "../APIReference/API_ProcessingInput.md") named `dataset` or the analysis
  configuration `dataset_uri` to specify the main dataset. For more
  information about `dataset_uri`, see the parameters list in [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").
- Use the `baseline` parameter provided in the analysis
  configuration file. The baseline dataset is required for SHAP analysis. For
  more information about the analysis configuration file, including examples,
  see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The following table lists supported data formats, their file extensions, and MIME
types.

| Data format | File extension | MIME type               |
| ----------- | -------------- | ----------------------- |
| CSV         | csv            | `text/csv`              |
| JSON Lines  | jsonl          | `application/jsonlines` |
| JSON        | json           | `application/json`      |
| Parquet     | parquet        | "application/x-parquet" |

The following sections show example tabular datasets in CSV, JSON Lines, and
Apache Parquet formats.

The SageMaker Clarify processing job is designed to load CSV data files in the [csv.excel](https://docs.python.org/3/library/csv.html#csv.excel "https://docs.python.org/3/library/csv.html#csv.excel") dialect. However, it's flexible enough to support
other line terminators, including `\n` and
`\r`.

For compatibility, all CSV data files provided to the SageMaker Clarify processing job
must be encoded in UTF-8.

If your dataset does not contain a header row, do the following:

- Set the analysis configuration label to index `0`. This
  means that the first column is the ground truth label.
- If the parameter `headers` is set, set
  `label` to the label column header to indicate the
  location of the label column. All other columns are designated as
  features.

The following is an example of a dataset that does not contain a
header row.

```
1,5,2.8,2.538,This is a good product
0,1,0.79,0.475,Bad shopping experience
...
```

If your data contains a header row, set the parameter `label`
to index `0`. To indicate the location of the label column, use
the ground truth label header `Label`. All other columns are
designated as features.

The following is an example of a dataset that contains a header
row.

```
Label,Rating,A12,A13,Comments
1,5,2.8,2.538,This is a good product
0,1,0.79,0.475,Bad shopping experience
...
```

JSON is a flexible format for representing structured data that contains
any level of complexity. The SageMaker Clarify support for JSON is not restricted to any
specific format and thus allows for more flexible data formats in comparison
to datasets in CSV or JSON Lines formats. This guide shows you how to set an
analysis configuration for tabular data in JSON format.

###### Note

To ensure compatibility, all JSON data files provided to the SageMaker Clarify
processing job must be encoded in UTF-8.

The following is example input data with records that contain a top-level
key, a list of features, and a label.

```
[
    {"features":[1,5,2.8,2.538,"This is a good product"],"label":1},
    {"features":[0,1,0.79,0.475,"Bad shopping experience"],"label":0},
    ...
]
```

An example configuration analysis for the previous input example dataset
should set the following parameters:

- The `label` parameter should use the [JMESPath](https://jmespath.org/ "https://jmespath.org/") expression
  `[*].label` to extract the ground truth label for
  each record in the dataset. The JMESPath expression should produce a
  list of labels where the ith label
  corresponds to the ith record.
- The `features` parameter should use the JMESPath
  expression `[*].features` to extract an array of features
  for each record in the dataset. The JMESPath expression should
  produce a 2D array or matrix where the
  ith row contains the feature values
  for corresponding to the ith
  record.

The following is example input data with records that contains a
top-level key and a nested key that contains a list of features and
labels for each record.

```
{
    "data": [
        {"features":[1,5,2.8,2.538,"This is a good product"],"label":1}},
        {"features":[0,1,0.79,0.475,"Bad shopping experience"],"label":0}}
    ]
}
```

An example configuration analysis for the previous input example dataset
should set the following parameters:

- The `label` parameter uses the [JMESPath](https://jmespath.org/ "https://jmespath.org/") expression
  `data[*].label` to extract the ground truth label for
  each record in the dataset. The JMESPath expression should produce a
  list of labels where the ith label is for
  the ith record.
- The `features` parameter uses the JMESPath expression
  `data[*].features` to extract the array of
  features, for each record in the dataset. The JMESPath expression
  should produce a 2D array or matrix where the
  ith row contains the feature values
  for the ith record.
  JSON Lines is a text format for representing structured data where each
  line is a valid JSON object. Currently SageMaker Clarify processing jobs only support
  SageMaker AI Dense Format JSON Lines. To conform to the required format, all of the
  features of a record should be listed in a single JSON array. For more
  information about JSON Lines, see [JSONLINES request format](cdf-inference.md#cm-jsonlines "cdf-inference.md#cm-jsonlines").

###### Note

All JSON Lines data files provided to the SageMaker Clarify processing job must be
encoded in UTF-8 to ensure compatibility.

The following is an example of how to set an analysis configuration for a
record that contains a **top-level key** and a
**list** of elements.

```
{"features":[1,5,2.8,2.538,"This is a good product"],"label":1}
{"features":[0,1,0.79,0.475,"Bad shopping experience"],"label":0}
...
```

The configuration analysis for the previous dataset example should set the
parameters as follows:

- To indicate the location of the ground truth label, the parameter
  `label` should be set to the JMESPath expression
  `label`.
- To indicate the location of the array of features, the parameter
  `features` should be set to the JMESPath expression
  `features`.
  The following is an example of how to set an analysis configuration for a
  record that contains a **top-level key** and a
  **nested key** that contains a **list** of elements.

```
{"data":{"features":[1,5,2.8,2.538,"This is a good product"],"label":1}}
{"data":{"features":[0,1,0.79,0.475,"Bad shopping experience"],"label":0}}
...
```

The configuration analysis for the previous dataset example should set the
parameters as follows:

- The parameter `label` should be set to the JMESPath
  expression `data.label` to indicate the location of the
  ground truth label.
- The parameter `features` should be set to the JMESPath
  expression `data.features` to indicate the location of
  the array of features.
  [Parquet](https://parquet.apache.org/ "https://parquet.apache.org/") is a
  column-oriented binary data format. Currently, SageMaker Clarify processing jobs support
  loading Parquet data files only when the processing instance count is
  `1`.

Because SageMaker Clarify processing jobs don’t support endpoint request or endpoint
response in Parquet format, you must specify the data format of the endpoint
request by setting the analysis configuration parameter
`content_type` to a supported format. For more information,
see `content_type` in [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The Parquet data must have column names that are formatted as strings. Use
the analysis configuration `label` parameter to set the label
column name to indicate the location of the ground truth labels. All other
columns are designated as features.
