# The

`EnableExplanations` expression

The `EnableExplanations` parameter is a [`JMESPath`](https://jmespath.org/ "https://jmespath.org/") Boolean expression
string. It is evaluated for **each record** in the
explainability request. If this parameter is evaluated to be **true**, then the record will be explained. If this parameter is
evaluated to be **false**, then explanations are not be
generated.

SageMaker Clarify deserializes the model container output for each record into a JSON
compatible data structure, and then uses the `EnableExplanations`
parameter to evaluate the data.

###### Notes

There are two options for records depending on the format of the model
container output.

- If the model container output is in CSV format, then a record is
  loaded as a JSON array.
- If the model container output is in JSON Lines format, then a record
  is loaded as a JSON object.
  The `EnableExplanations` parameter is a JMESPath expression that can be
  passed either during the `InvokeEndpoint` or
  `CreateEndpointConfig` operations. If the JMESPath expression that
  you supplied is not valid, the endpoint creation will fail. If the expression is
  valid, but the expression evaluation result is unexpected, then the endpoint will be
  created successfully, but an error will be generated when the endpoint is invoked.
  Test your `EnableExplanations` expression by using the
  `InvokeEndpoint` API, and then apply it to the endpoint
  configuration.

The following are some examples of valid `EnableExplanations`
expression. In the examples, a JMESPath expression encloses a literal using backtick
characters. For example, `true` means true.

| Expression (string representation)                  | Model container output (string representation)                      | Evaluation result (Boolean) | Meaning                                                                                                                                                                                                                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| '`true`'                                            | (N/A)                                                               | True                        | Activate online explainability unconditionally.                                                                                                                                                                                                                |
| '`false`'                                           | (N/A)                                                               | False                       | Deactivate online explainability unconditionally.                                                                                                                                                                                                              |
| '[1]>`0.5`'                                         | '1,0.6'                                                             | True                        | For each record, the model container outputs its predicted label and probability. Explains a record if its probability (at index 1) is greater than 0.5.                                                                                                       |
| 'probability>`0.5`'                                 | '{"predicted_label":1,"probability":0.6}'                           | True                        | For each record, the model container outputs JSON data. Explain a record if its probability is greater than 0.5.                                                                                                                                               |
| '!contains(probabilities[:-1], max(probabilities))' | '{"probabilities": [0.4, 0.1, 0.4], "labels":["cat","dog","fish"]}' | False                       | For a multi-class model: Explains a record if its predicted label (the class that has the max probability value) is the last class. Literally, the expression means that the max probability value is not in the list of probabilities excluding the last one. |
