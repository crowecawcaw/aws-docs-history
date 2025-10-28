# Pre-check

endpoint request and response for tabular data

We recommend that you deploy your model to a SageMaker AI real-time inference endpoint,
and send requests to the endpoint. Manually examine the requests and responses to
make sure that both are compliant with the requirements in the [Endpoint
requests for tabular data](clarify-processing-job-data-format-tabular-request.md "clarify-processing-job-data-format-tabular-request.md") section and the
[Endpoint
response for tabular data](clarify-processing-job-data-format-tabular-response.md "clarify-processing-job-data-format-tabular-response.md") section. If your
model container supports batch requests, you can start with a single record request,
and then try two or more records.

The following commands show how to request a response using the AWS CLI. The AWS CLI
is pre-installed in SageMaker Studio and SageMaker Notebook instances. To
install the AWS CLI, follow this [installation
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

The parameters are defined, as follows.

- `$ENDPOINT NAME` – The name of the endpoint.
- `$CONTENT_TYPE` – The MIME type of the request (model
  container input).
- `$ACCEPT_TYPE` – The MIME type of the response (model
  container output).
- `$REQUEST_DATA` – The requested payload string.
- `$CLI_BINARY_FORMAT` – The format of the command line
  interface (CLI) parameter. For AWS CLI v1, this parameter should remain blank.
  For v2, this parameter should be set to `--cli-binary-format
raw-in-base64-out`.

###### Note

AWS CLI v2 passes binary parameters as base64-encoded strings [by default](../../../cli/latest/userguide/cliv2-migration.md#cliv2-migration-binaryparam "../../../cli/latest/userguide/cliv2-migration.md#cliv2-migration-binaryparam").
