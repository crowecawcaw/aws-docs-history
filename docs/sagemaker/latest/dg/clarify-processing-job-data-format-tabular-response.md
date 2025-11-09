# Endpoint

response for tabular data

After the SageMaker Clarify processing job receives an inference endpoint invocation's
response, it deserializes the response payload and extracts predictions from it. Use
the analysis configuration `accept_type` parameter to specify the data
format of the response payload. If `accept_type` is not provided, the
SageMaker Clarify processing job will use the value of the content_type parameter as the model
output format. For more information about `accept_type`, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The predictions could either consist of predicted labels for bias analysis, or
probability values (scores) for feature importance analysis. In the
`predictor` analysis configuration, the following three parameters
extract the predictions.

- The parameter `probability` is used to locate the probability
  values (scores) in the endpoint response.
- The parameter `label` is used to locate the predicted labels in
  the endpoint response.
- (Optional) The parameter `label_headers` provides the predicted
  labels for a multiclass model.
  The following guidelines pertain to endpoint responses in CSV, JSON Lines, and
  JSON formats.

## Endpoint Response is in CSV format

If the response payload is in CSV format (MIME type: `text/csv`),
the SageMaker Clarify processing job deserializes each row. It then extracts the predictions
from the deserialized data using the column indexes provided in the analysis
configuration. The rows in the response payload must match the records in the
request payload.

The following tables provide examples of response data in different formats
and for different problem types. Your data can vary from these examples, as long
as the predictions can be extracted according to the analysis
configuration.

The following sections show example endpoint responses in CSV formats.

The following table is an example endpoint response for regression and
binary classification problems.

| Endpoint request payload                                | Endpoint response payload (string<br>representation) |
| ------------------------------------------------------- | ---------------------------------------------------- |
| Single record.                                          | '0.6'                                                |
| Two records (results in one line, divided by<br>comma). | '0.6,0.3'                                            |
| Two records (results in two lines).                     | '0.6\n0.3'                                           |

For the previous example, the endpoint outputs a single probability
value (score) of the predicted label. To extract probabilities using the
index and use them for feature importance analysis, set the analysis
configuration parameter `probability` to column index
`0`. These probabilities can also be used for bias
analysis if they're converted to binary value by using the
`probability_threshold` parameter. For more information
about `probability_threshold`, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The following table is an example endpoint response for a multiclass
problem.

| Endpoint request payload                                | Endpoint response payload (string<br>representation) |
| ------------------------------------------------------- | ---------------------------------------------------- |
| Single record of a multiclass model (three<br>classes). | '0.1,0.6,0.3'                                        |
| Two records of a multiclass model (three<br>classes).   | '0.1,0.6,0.3\n0.2,0.5,0.3'                           |

For the previous example, the endpoint outputs a list of probabilities
(scores). If no index is provided, all values are extracted and used for
feature importance analysis. If the analysis configuration parameter
`label_headers` is provided. Then the SageMaker Clarify processing
job can select the label header of the max probability as the predicted
label, which can be used for bias analysis. For more information about
`label_headers`, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The following table is an example endpoint response for regression and
binary classification problems.

| Endpoint request payload                               | Endpoint response payload (string<br>representation) |
| ------------------------------------------------------ | ---------------------------------------------------- |
| Single record                                          | '1'                                                  |
| Two records (results in one line, divided by<br>comma) | '1,0'                                                |
| Two records (results in two lines)                     | '1\n0'                                               |

For the previous example, the endpoint outputs the predicted label
instead of probability. Set the `label` parameter of the
`predictor` configuration to column index `0`
so that the predicted labels can be extracted using the index and used
for bias analysis.

The following table is an example endpoint response for regression and
binary classification problems.

| Endpoint request payload | Endpoint response payload (string<br>representation) |
| ------------------------ | ---------------------------------------------------- |
| Single record            | '1,0.6'                                              |
| Two records              | '1,0.6\n0,0.3'                                       |

For the previous example, the endpoint outputs the predicted label
followed by its probability. Set the `label` parameter of the
`predictor` configuration to column index `0`,
and set `probability` to column index `1` to
extract both parameter values.

A multiclass model trained by Amazon SageMaker Autopilot can be configured to output the
string representation of the list of predicted labels and probabilities
. The following example table shows an example endpoint response from a
model that is configured to output `predicted_label`,
`probability`, `labels`, and
`probabilities`.

| Endpoint request payload | Endpoint response payload (string<br>representation)                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Single record            | '"dog",0.6,"[\'cat\', \'dog\', \'fish\']","[0.1,<br>0.6, 0.3]"'                                                                |
| Two records              | '"dog",0.6,"[\'cat\', \'dog\', \'fish\']","[0.1,<br>0.6, 0.3]"\n""cat",0.7,[\'cat\', \'dog\',<br>\'fish\']","[0.7, 0.2, 0.1]"' |

For the previous example, the SageMaker Clarify processing job can be configured
in the following ways to extract the predictions.

For bias analysis, the previous example can be configured as one of
the following.

- Set the `label` parameter of the
  `predictor` configuration to `0` to
  extract the predicted label.
- Set the parameter to `2` to extract the predicted
  labels, and set `probability` to `3` to
  extract the corresponding probabilities. The SageMaker Clarify processing
  job can automatically determine the predicted label by
  identifying the label with the highest probability value.
  Referring to the previous example of a single record, the model
  predicts three labels: `cat`, `dog`, and
  `fish`, with corresponding probabilities of
  `0.1`, `0.6`, and `0.3`.
  Based on these probabilities, the predicted label is
  `dog`, as it has the highest probability value of
  `0.6`.
- Set `probability` to `3` to extract the
  probabilities. If `label_headers` is provided, then
  the SageMaker Clarify processing job can automatically determine the
  predicted label by identifying the label header with the highest
  probability value.
  For feature importance analysis, the previous example can be
  configured as follows.

- Set `probability` to `3` extract the
  probabilities of all the predicted labels. Then, feature
  attributions will be computed for all the labels. If the
  customer doesn’t specify `label_headers`, then the
  predicted labels will be used as label headers in the analysis
  report.

## Endpoint Response is in JSON Lines format

If the response payload is in JSON Lines format (MIME type:
`application/jsonlines`), the SageMaker Clarify processing job deserializes
each line as JSON. It then extracts predictions from the deserialized data using
JMESPath expressions provided in analysis configuration. The lines in the
response payload must match the records in the request payload. The following
tables shows examples of response data in different formats. Your data can vary
from these examples, as long as the predictions can be extracted according to
the analysis configuration.

The following sections show example endpoint responses in JSON Lines
formats.

The following table is an example endpoint response that only outputs
the probability value (score).

| Endpoint request payload | Endpoint response payload (string<br>representation) |
| ------------------------ | ---------------------------------------------------- |
| Single record            | '{"score":0.6}'                                      |
| Two records              | '{"score":0.6}\n{"score":0.3}'                       |

For the previous example, set the analysis configuration parameter
`probability` to JMESPath expression "score" to extract
its value.

The following table is an example endpoint response that only outputs
the predicted label.

| Endpoint request payload | Endpoint response payload (string<br>representation) |
| ------------------------ | ---------------------------------------------------- |
| Single record            | '{"prediction":1}'                                   |
| Two records              | '{"prediction":1}\n{"prediction":0}'                 |

For the previous example, set the `label` parameter of the
predictor configuration to JMESPath expression `prediction`.
Then, the SageMaker Clarify processing job can extract the predicted labels for bias
analysis. For more information, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The following table is an example endpoint response that outputs the
predicted label and its score.

| Endpoint request payload | Endpoint response payload (string<br>representation)         |
| ------------------------ | ------------------------------------------------------------ |
| Single record            | '{"prediction":1,"score":0.6}'                               |
| Two records              | '{"prediction":1,"score":0.6}\n{"prediction":0,"score":0.3}' |

For the previous example, set the `label` parameter of the
`predictor` configuration to JMESPath expression
"prediction" to extract the predicted labels. Set
`probability` to JMESPath expression "score" to extract
the probability. For more information, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The following table is an example endpoint response from a multiclass
model that outputs the following:

- A list of predicted labels.
- Probabilities, and the selected predicted label and its
  probability.

| Endpoint request payload | Endpoint response payload (string<br>representation)                                                                                                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single record            | '{"predicted_label":"dog","probability":0.6,"predicted_labels":["cat","dog","fish"],"probabilities":[0.1,0.6,0.3]}'                                                                                                                    |
| Two records              | '{"predicted_label":"dog","probability":0.6,"predicted_labels":["cat","dog","fish"],"probabilities":[0.1,0.6,0.3]}\n{"predicted_label":"cat","probability":0.7,"predicted_labels":["cat","dog","fish"],"probabilities":[0.7,0.2,0.1]}' |

For the previous example, the SageMaker Clarify processing job can be configured
in several ways to extract the predictions.

For bias analysis, the previous example can be configured as **one** of the following.

- Set the `label` parameter of the
  `predictor` configuration to JMESPath expression
  "predicted_label" to extract the predicted label.
- Set the parameter to JMESPath expression "predicted_labels" to
  extract the predicted labels. Set `probability` to
  JMESPath expression "probabilities" to extract their
  probabilities. The SageMaker Clarify job automatically determine the
  predicted label by identifying the label with the highest
  probability value.
- Set `probability` to JMESPath expression
  "probabilities" to extract their probabilities. If
  `label_headers` is provided, then the SageMaker Clarify
  processing job can automatically determine the predicted label
  by identifying the label with the highest probability
  value.
  For feature importance analysis, do the following.

- Set `probability` to the JMESPath expression
  "probabilities" to extract their probabilities of all the
  predicted labels. Then, feature attributions will be computed
  for all the labels.

## Endpoint Response is in JSON format

If the response payload is in JSON format (MIME type:
`application/json`), the SageMaker Clarify processing job deserializes the
entire payload as JSON. It then extracts predictions from the deserialized data
using JMESPath expressions provided in the analysis configuration. The records
in the response payload must match the records in the request payload.

The following sections show example endpoint responses in JSON formats. The
sections contain tables with examples of response data in different formats and
for different problem types. Your data can vary from these examples, as long as
the predictions can be extracted according to the analysis configuration.

The following table is an example response from an endpoint that only
outputs the probability value (score).

| Endpoint request payload | Endpoint response payload (string<br>representation) |
| ------------------------ | ---------------------------------------------------- |
| Single record            | '[0.6]'                                              |
| Two records              | '[0.6,0.3]'                                          |

For the previous example, there is no line break in the response
payload. Instead, a single JSON object contains a list of scores, one
for each record in the request. Set the analysis configuration parameter
`probability` to JMESPath expression "[\*]" to extract the
value.

The following table is an example response from an endpoint that only
outputs the predicted label.

| Endpoint request payload | Endpoint response payload (string<br>representation) |
| ------------------------ | ---------------------------------------------------- |
| Single record            | '{"predicted_labels":[1]}'                           |
| Two records              | '{"predicted_labels":[1,0]}'                         |

Set the `label` parameter of the `predictor`
configuration to JMESPath expression "predicted_labels", and then the
SageMaker Clarify processing job can extract the predicted labels for bias
analysis.

The following table is an example response from an endpoint that
outputs the predicted label and its score.

| Endpoint request payload | Endpoint response payload (string<br>representation)                |
| ------------------------ | ------------------------------------------------------------------- |
| Single record            | '{"predictions":[{"label":1,"score":0.6}'                           |
| Two records              | ‘{"predictions":[{"label":1,"score":0.6},{"label":0,"score":0.3}]}' |

For the previous example, set the `label` parameter of the
`predictor` configuration to the JMESPath expression
"predictions[\*].label" to extract the predicted labels. Set
`probability` to JMESPath expression
"predictions[\*].score" to extract the probability.

The following table is an example response from an endpoint that from
a multiclass model that outputs the following:

- A list of predicted labels.
- Probabilities, and the selected predicted label and its
  probability.

| Endpoint request payload | Endpoint response payload (string<br>representation)                                                                                                                                                                                    |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single record            | '[{"predicted_label":"dog","probability":0.6,"predicted_labels":["cat","dog","fish"],"probabilities":[0.1,0.6,0.3]}]'                                                                                                                   |
| Two records              | '[{"predicted_label":"dog","probability":0.6,"predicted_labels":["cat","dog","fish"],"probabilities":[0.1,0.6,0.3]},{"predicted_label":"cat","probability":0.7,"predicted_labels":["cat","dog","fish"],"probabilities":[0.7,0.2,0.1]}]' |

The SageMaker Clarify processing job can be configured in several ways to extract
the predictions.

For bias analysis, the previous example can be configured as **one** of the following.

- Set the `label` parameter of the
  `predictor` configuration to JMESPath expression
  "[\*].predicted_label" to extract the predicted label.
- Set the parameter to JMESPath expression
  "[\*].predicted_labels" to extract the predicted labels. Set
  `probability` to JMESPath expression
  "[\*].probabilities" to extract their probabilities. The SageMaker Clarify
  processing job can automatically determine the predicted label
  by identifying the label with the highest proximity
  value.
- Set `probability` to JMESPath expression
  "[\*].probabilities" to extract their probabilities. If
  `label_headers` is provided, then the SageMaker Clarify
  processing job can automatically determine the predicted label
  by identifying the label with the highest probability
  value.
  For feature importance analysis, set `probability` to
  JMESPath expression "[\*].probabilities" to extract their probabilities
  of all the predicted labels. Then, feature attributions will be computed
  for all the labels.
