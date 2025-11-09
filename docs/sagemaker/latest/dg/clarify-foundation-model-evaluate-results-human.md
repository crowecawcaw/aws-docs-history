# Understand the results

of a human evaluation job

When you created a model evaluation job that uses human workers you selected one or more _metric types_. When members of the workteam evaluate a response in the worker portal their responses are saved in the `humanAnswers` json object. How those responses are stored change based on the metric type selected when the job was created.

The following sections explain these differences, and provide examples.

## JSON output reference

When a model evaluation job is completed the results are saved in Amazon S3 as a JSON file. The
JSON object contains three high level nodes `humanEvaluationResult`,
`inputRecord`, and `modelResponses`.The
`humanEvaluationResult` key is a high level node that contains the
responses from the workteam assigned to the model evaluation job.
The`inputRecord` key is a high level node that contains the prompts
provided to the model(s) when the model evaluation job was created. The
`modelResponses` key is a high level node that contains the responses
to the prompts from the model(s).

The following table summarizes the key value pairs found in the JSON output from the model evaluation job.

The proceeding sections provide more granular details about each key value pair.

| Parameter            | Example                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `flowDefinitionArn`  | `arn:aws:sagemaker:us-west-2:`111122223333`:flow-definition/`flow-definition-name``                                                                                                                                                                                                                                                                                                                                                                 | The ARN of the human review workflow (flow definition) that created the human loop.    |
| `humanAnswers`       | A list of JSON objects specific to the evaluation metrics selected. To learn more see, [Key values pairs found under humanAnswers](#clarify-foundation-model-evaluate-humanAnswers "#clarify-foundation-model-evaluate-humanAnswers").                                                                                                                                                                                                              | A list of JSON objects that contain workers responses.                                 |
| `humanLoopName`      | `system-generated-hash`                                                                                                                                                                                                                                                                                                                                                                                                                             | A system generated 40-character hex string.                                            |
| `inputRecord`        | `<br>"inputRecord": {<br>"prompt": {<br>"text": "Who invented the airplane?"<br>},<br>"category": "Airplanes",<br>"referenceResponse": {<br>"text": "Orville and Wilbur Wright"<br>},<br>"responses":<br>[{<br>"modelIdentifier": "meta-textgeneration-llama-codellama-7b",<br>"text": "The Wright brothers, Orville and Wilbur Wright are widely credited with inventing and manufacturing the world's first successful airplane."<br>}]<br>}<br>` | A JSON object that contains an entry prompt from the input dataset.                    |
| `modelResponses`     | ``<br>"modelResponses": [{<br>"modelIdentifier": "arn:aws:bedrock:`us-west-2`::foundation-model/`model-id`",<br>"text": "the-models-response-to-the-prompt"<br>}]<br>``                                                                                                                                                                                                                                                                             | The individual responses from the models.                                              |
| `inputContent`       | ``<br>{<br>"additionalDataS3Uri":"s3://`user-specified-S3-URI-path`/datasets/`dataset-name`/records/`record-number`/human-loop-additional-data.json",<br>"evaluationMetrics":[<br>{<br>"description":"`brief-name`",<br>"metricName":"`metric-name`",<br>"metricType":"IndividualLikertScale"<br>}<br>],<br>"instructions":"example instructions"<br>}<br>``                                                                                        | The human loop input content required to start human loop<br>in your Amazon S3 bucket. |
| `modelResponseIdMap` | `<br>{<br>"0": "sm-margaret-meta-textgeneration-llama-2-7b-1711485008-0612",<br>"1": "jumpstart-dft-hf-llm-mistral-7b-ins-20240327-043352"<br>}<br>`                                                                                                                                                                                                                                                                                                | Describes how each model is represented in the `answerContent`.                        |

### Key values pairs found under `humanEvaluationResult`

The following key value pairs around found under the `humanEvaluationResult` in the output of your model evaluation job.

For the key value pairs associated with `humanAnswers`, see [Key values pairs found under humanAnswers](#clarify-foundation-model-evaluate-humanAnswers "#clarify-foundation-model-evaluate-humanAnswers").

**`flowDefinitionArn`**

- The ARN of the flow definition used to complete the model evaluation job.
- _Example:_`arn:aws:sagemaker:us-west-2:`111122223333`:flow-definition/`flow-definition-name``

**`humanLoopName`**

- A system generated 40-character hex string.

**`inputContent`**

- This key value describes the _metric types_, and the instructions your provided for workers in the worker portal.
  - `additionalDataS3Uri`: The location in Amazon S3 where the instructions for workers is saved.
  - `instructions`: The instructions you provided to workers in the worker portal.
  - `evaluationMetrics`: The name of the metric and it's description. The key value `metricType` is the tool provided to workers to evaluate the models' responses.

**`modelResponseIdMap`**

- This key value pair identifies the full names of the models selected, and how worker choices are mapped to the models in the `humanAnswers` key value pairs.

### Key values pairs found under `inputRecord`

The following entries describe the `inputRecord` key value pairs.

**`prompt`**

- The text of the prompt sent to the model.

**`category`**

- An optional category that classifies the prompt. Visible to workers in the worker portal during the model evaluation.
- _Example:_`"American cities"`

**`referenceResponse`**

- An optional field from the input JSON used to specify the ground truth you want workers to reference during the evaluation

**`responses`**

- An optional field from the input JSON that contains responses from other models.

An example JSON input record.

```
{
  "prompt": {
     "text": "Who invented the airplane?"
  },
  "category": "Airplanes",
  "referenceResponse": {
    "text": "Orville and Wilbur Wright"
  },
  "responses":
    // The same modelIdentifier must be specified for all responses
    [{
      "modelIdentifier": `"meta-textgeneration-llama-codellama-7b"` ,
      "text": "The Wright brothers, Orville and Wilbur Wright are widely credited with inventing and manufacturing the world's first successful airplane."
    }]
}
```

### Key values pairs found under `modelResponses`

An array of key value pairs that contains the responses from the models, and which model provided the responses.

**`text`**

- The model's response to the prompt.

**`modelIdentifier`**

- The name of the model.

### Key values pairs found under `humanAnswers`

An array of key value pairs that contains the responses from the models, and how workers evaluated the models.

**`acceptanceTime`**

- When the worker accepted the task in the worker portal.

**`submissionTime`**

- When the worker submitted their response.

**`timeSpentInSeconds`**

- How long the worker spent completing the task.

**`workerId`**

- The ID of the worker who completed the task.

**`workerMetadata`**

- Metadata about which workteam was assigned to this model evaluation job.

#### Format of the `answerContent` JSON array

The structure of answer depends on the evaluation metrics selected when model evaluation job was created. Each worker response or answer is recorded in a new JSON object.

**`answerContent`**

- `evaluationResults` contains the worker's responses.
  - When **Choice buttons** is selected, the results from each worker are as `"evaluationResults": "comparisonChoice"`.

  `metricName`: The name of the metric

  `result`: The JSON object indicates which model the worker selected using either a `0` or `1`. To see which value a model is mapped to see, `modelResponseIdMap`.
  - When **Likert scale, comparison** is selected, the results from each worker are as `"evaluationResults": "comparisonLikertScale"`.

  `metricName`: The name of the metric.

  `leftModelResponseId`: Indicates which `modelResponseIdMap` was shown on the left side of the worker portal.

  `rightModelResponseId`: Indicates which `modelResponseIdMap` was shown on the left side of the worker portal.

  `result`: The JSON object indicates which model the worker selected using either a `0` or `1`. To see which value a model is mapped to see, `modelResponseIdMap`
  - When **Ordinal rank** is selected, the results from each worker are as `"evaluationResults": "comparisonRank"`.

  `metricName`: The name of the metric

  `result`: An array of JSON objects. For each model (`modelResponseIdMap`) workers provide a `rank`.

  ```
  "result": [{
  	"modelResponseId": "0",
  	"rank": 1
  }, {
  	"modelResponseId": "1",
  	"rank": 1
  }]
  ```

  - When **Likert scale, evaluation of a single model response** is selected, the results a worker are saved in `"evaluationResults": "individualLikertScale"`. This is a JSON array containing the scores for `metricName` specified when the job was created.

  `metricName`: The name of the metric.

  `modelResponseId`: The model that is scored. To see which value a model is mapped to see, `modelResponseIdMap`.

  `result`: A key value pair indicating the likert scale value selected by the worker.
  - When **Thumbs up/down** is selected, the results from a worker are saved as a JSON array `"evaluationResults": "thumbsUpDown"`.

  `metricName`: The name of the metric.

  `result`: Either `true` or `false` as it relates to the `metricName`. When a worker chooses thumbs up, `"result" : true`.

## Example output from a model evaluation job output

The following JSON object is an example model evaluation job output that is saved in Amazon S3. To learn more about each key values pair, see the [JSON output reference](#clarify-foundation-model-evaluate-results-human-ref "#clarify-foundation-model-evaluate-results-human-ref").

For clarity this job only contains the responses from a two workers. Some key value pairs may have also been truncated for readability

```
{
	"humanEvaluationResult": {
		"flowDefinitionArn": "arn:aws:sagemaker:`us-west-2`:`111122223333`:flow-definition/`flow-definition-name`",
        "humanAnswers": [
            {
                "acceptanceTime": "2024-06-07T22:31:57.066Z",
                "answerContent": {
                    "evaluationResults": {
                        "comparisonChoice": [
                            {
                                "metricName": "Fluency",
                                "result": {
                                    "modelResponseId": "0"
                                }
                            }
                        ],
                        "comparisonLikertScale": [
                            {
                                "leftModelResponseId": "0",
                                "metricName": "Coherence",
                                "result": 1,
                                "rightModelResponseId": "1"
                            }
                        ],
                        "comparisonRank": [
                            {
                                "metricName": "Toxicity",
                                "result": [
                                    {
                                        "modelResponseId": "0",
                                        "rank": 1
                                    },
                                    {
                                        "modelResponseId": "1",
                                        "rank": 1
                                    }
                                ]
                            }
                        ],
                        "individualLikertScale": [
                            {
                                "metricName": "Correctness",
                                "modelResponseId": "0",
                                "result": 2
                            },
                            {
                                "metricName": "Correctness",
                                "modelResponseId": "1",
                                "result": 3
                            },
                            {
                                "metricName": "Completeness",
                                "modelResponseId": "0",
                                "result": 1
                            },
                            {
                                "metricName": "Completeness",
                                "modelResponseId": "1",
                                "result": 4
                            }
                        ],
                        "thumbsUpDown": [
                            {
                                "metricName": "Accuracy",
                                "modelResponseId": "0",
                                "result": true
                            },
                            {
                                "metricName": "Accuracy",
                                "modelResponseId": "1",
                                "result": true
                            }
                        ]
                    }
                },
                "submissionTime": "2024-06-07T22:32:19.640Z",
                "timeSpentInSeconds": 22.574,
                "workerId": "ead1ba56c1278175",
                "workerMetadata": {
                    "identityData": {
                        "identityProviderType": "Cognito",
                        "issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_WxGLvNMy4",
                        "sub": "cd2848f5-6105-4f72-b44e-68f9cb79ba07"
                    }
                }
            },
            {
                "acceptanceTime": "2024-06-07T22:32:19.721Z",
                "answerContent": {
                    "evaluationResults": {
                        "comparisonChoice": [
                            {
                                "metricName": "Fluency",
                                "result": {
                                    "modelResponseId": "1"
                                }
                            }
                        ],
                        "comparisonLikertScale": [
                            {
                                "leftModelResponseId": "0",
                                "metricName": "Coherence",
                                "result": 1,
                                "rightModelResponseId": "1"
                            }
                        ],
                        "comparisonRank": [
                            {
                                "metricName": "Toxicity",
                                "result": [
                                    {
                                        "modelResponseId": "0",
                                        "rank": 2
                                    },
                                    {
                                        "modelResponseId": "1",
                                        "rank": 1
                                    }
                                ]
                            }
                        ],
                        "individualLikertScale": [
                            {
                                "metricName": "Correctness",
                                "modelResponseId": "0",
                                "result": 3
                            },
                            {
                                "metricName": "Correctness",
                                "modelResponseId": "1",
                                "result": 4
                            },
                            {
                                "metricName": "Completeness",
                                "modelResponseId": "0",
                                "result": 1
                            },
                            {
                                "metricName": "Completeness",
                                "modelResponseId": "1",
                                "result": 5
                            }
                        ],
                        "thumbsUpDown": [
                            {
                                "metricName": "Accuracy",
                                "modelResponseId": "0",
                                "result": true
                            },
                            {
                                "metricName": "Accuracy",
                                "modelResponseId": "1",
                                "result": false
                            }
                        ]
                    }
                },
                "submissionTime": "2024-06-07T22:32:57.918Z",
                "timeSpentInSeconds": 38.197,
                "workerId": "bad258db224c3db6",
                "workerMetadata": {
                    "identityData": {
                        "identityProviderType": "Cognito",
                        "issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_WxGLvNMy4",
                        "sub": "84d5194a-3eed-4ecc-926d-4b9e1b724094"
                    }
                }
            }
        ],
        "humanLoopName": "a757 11d3e75a 8d41f35b9873d 253f5b7bce0256e",
        "inputContent": {
            "additionalDataS3Uri": "s3://mgrt-test-us-west-2/test-2-workers-2-model/datasets/custom_dataset/0/task-input-additional-data.json",
            "instructions": "worker instructions provided by the model evaluation job administrator",
            "evaluationMetrics": [
                {
                    "metricName": "Fluency",
                    "metricType": "ComparisonChoice",
                    "description": "Measures the linguistic quality of a generated text."
                },
                {
                    "metricName": "Coherence",
                    "metricType": "ComparisonLikertScale",
                    "description": "Measures the organization and structure of a generated text."
                },
                {
                    "metricName": "Toxicity",
                    "metricType": "ComparisonRank",
                    "description": "Measures the harmfulness of a generated text."
                },
                {
                    "metricName": "Accuracy",
                    "metricType": "ThumbsUpDown",
                    "description": "Indicates the accuracy of a generated text."
                },
                {
                    "metricName": "Correctness",
                    "metricType": "IndividualLikertScale",
                    "description": "Measures a generated answer's satisfaction in the context of the question."
                },
                {
                    "metricName": "Completeness",
                    "metricType": "IndividualLikertScale",
                    "description": "Measures a generated answer's inclusion of all relevant information."
                }
            ],
            "disableRandomization": "true"
        },
        "modelResponseIdMap": {
            "0": "sm-margaret-meta-textgeneration-llama-2-7b-1711485008-0612",
            "1": "jumpstart-dft-hf-llm-mistral-7b-ins-20240327-043352"
        }
    },
    "inputRecord": {
        "prompt": {
            "text": "What is high intensity interval training?"
        },
        "category": "Fitness",
        "referenceResponse": {
            "text": "High-Intensity Interval Training (HIIT)"
        }
    },
    "modelResponses": [
        {
            "text": "High Intensity Interval Training (HIIT) is a form of exercise that alternates between periods of high intensity work and low intensity recovery.HIIT is an excellent way to increase your fitness and improve your health, but it can be difficult to get started.In this article, we will",
            "modelIdentifier": "sm-margaret-meta-textgeneration-llama-2-7b-1711485008-0612"
        },
        {
            "text": "High intensity interval training is a form of exercise consisting of short bursts of maximum effort followed by periods of rest. The theory behind HIIT is that it can often be more effective at improving cardiovascular and metabolic health than longer, lower intensity workouts.The work intervals can range in length depending on the specific type of exercise, but are typically between 20 and 90 seconds. The recovery periods are generally longer, lasting between 1 and 5 minutes. This pattern is then repeated for multiple sets.\n\nSince the work intervals are high intensity, they require more effort from your body and therefore result in a greater calorie burn. The body also continues to burn calories at an increased rate after the workout due to an effect called excess post exercise oxygen consumption (EPOC), also know as the afterburn effect.\n\nHIIT is a versatile form of training that can be adapted to different fitness levels and can be performed using a variety of exercises including cycling, running, bodyweight movements, and even swimming. It can be done in as little as 20 minutes once or twice a week, making it an efficient option for busy individuals.\n\nWhat are the benefits of high intensity interval training",
            "modelIdentifier": "jumpstart-dft-hf-llm-mistral-7b-ins-20240327-043352"
        }
    ]
}
```
