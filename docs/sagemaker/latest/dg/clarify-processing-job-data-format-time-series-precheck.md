# Pre-check

endpoint request and response for time series data

You are advised to deploy your model to a SageMaker AI real-time inference endpoint
and send requests to the endpoint. Manually examine the requests and responses
to make sure that both are compliant with the requirements in the [Endpoint requests for time series data](clarify-processing-job-data-format-time-series-request-jsonlines.md "clarify-processing-job-data-format-time-series-request-jsonlines.md") and
[Endpoint
response for time series data](clarify-processing-job-data-format-time-series-response-json.md "clarify-processing-job-data-format-time-series-response-json.md") sections.
If your model container supports batch requests, you can start with a single record
request and then try two or more records.

The following commands demonstrate how to request a response using the AWS CLI.
The AWS CLI is pre-installed in Studio and SageMaker Notebook instances.
To install the AWS CLI, follow the [installation
guide](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name $ENDPOINT_NAME \
  --content-type $CONTENT_TYPE \
  --accept $ACCEPT_TYPE \
  --body $REQUEST_DATA \
  $CLI_BINARY_FORMAT \
  /dev/stderr 1>/dev/null
```

The parameters are defined as follows:

- $ENDPOINT NAME — The name of the endpoint.
- $CONTENT_TYPE — The MIME type of the request (model container input).
- $ACCEPT_TYPE — The MIME type of the response (model container output).
- $REQUEST_DATA — The requested payload string.
- $CLI_BINARY_FORMAT — The format of the command line interface (CLI)
  parameter. For AWS CLI v1, this parameter should remain blank. For v2, this
  parameter should be set to `--cli-binary-format raw-in-base64-out`.

###### Note

AWS CLI v2 passes binary parameters as base64-encoded strings by default.
The following request and response examples to and from the endpoint use AWS CLI v1.

Example 1
In the following code example, the request consists of a single record.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-json \
  --content-type application/json \
  --accept application/json \
  --body '{"target": [1, 2, 3, 4, 5],
    "start": "2024-01-01 01:00:00"}' \
/dev/stderr 1>/dev/null
```

The following snippet shows the corresponding response output.

```
{'predictions': {'mean': [1, 2, 3, 4, 5]}
```

Example 2
In the following code example, the request contains two records.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-json-2 \
  --content-type application/json \
  --accept application/json \
  --body $'{"instances": [{"target":[1, 2, 3],
    "start":"2024-01-01 01:00:00",
    "dynamic_feat":[[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]]}], {"target":[1, 2, 3],
    "start":"2024-01-02 01:00:00",
    "dynamic_feat":[[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]]}]}' \
dev/stderr 1>/dev/null
```

The response output is the following:

```
{'predictions': [{'mean': [1, 2, 3, 4, 5]}, {'mean': [1, 2, 3, 4, 5]}]}
```
