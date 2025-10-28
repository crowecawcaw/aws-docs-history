# Invoke your endpoint

###### Note

We recommend that you [test your
model deployment in Amazon SageMaker Canvas](canvas-deploy-model-test.md "canvas-deploy-model-test.md") before invoking a SageMaker AI endpoint programmatically.

You can use your Amazon SageMaker Canvas models that you've deployed to a SageMaker AI endpoint in production with your
applications. Invoke the endpoint programmatically the same way that you invoke
any other [SageMaker AI real-time endpoint](realtime-endpoints.md "realtime-endpoints.md"). Invoking an endpoint programmatically returns a
response object which contains the same fields described in
[Test your deployment](canvas-deploy-model-test.md "canvas-deploy-model-test.md").

For more detailed information about how to programmatically invoke endpoints, see
[Invoke models for real-time
inference](realtime-endpoints-test-endpoints.md "realtime-endpoints-test-endpoints.md").

The following Python examples show you how to invoke your endpoint based on the model
type.

The following example shows you how to invoke a JumpStart foundation model
that you've deployed to an endpoint.

```
import boto3
import pandas as pd

client = boto3.client("runtime.sagemaker")
body = pd.DataFrame(
    [['feature_column1', 'feature_column2'],
    ['feature_column1', 'feature_column2']]
).to_csv(header=False, index=False).encode("utf-8")

response = client.invoke_endpoint(
    EndpointName="endpoint_name",
    ContentType="text/csv",
    Body=body,
    Accept="application/json"
)
```

The following example shows you how to invoke numeric or categorical
prediction models.

```
import boto3
import pandas as pd

client = boto3.client("runtime.sagemaker")
body = pd.DataFrame(['feature_column1', 'feature_column2'], ['feature_column1', 'feature_column2']).to_csv(header=False, index=False).encode("utf-8")

response = client.invoke_endpoint(
    EndpointName="endpoint_name",
    ContentType="text/csv",
    Body=body,
    Accept="application/json"
)
```

The following example shows you how to invoke time series forecasting models.
For a complete example of how to test invoke a time series forecasting model, see
[Time-Series Forecasting with Amazon SageMaker Autopilot](https://github.com/aws/amazon-sagemaker-examples/blob/eef13dae197a6e588a8bc111aba3244f99ee0fbb/autopilot/autopilot_time_series.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/eef13dae197a6e588a8bc111aba3244f99ee0fbb/autopilot/autopilot_time_series.ipynb").

```
import boto3
import pandas as pd

csv_path = './real-time-payload.csv'
data = pd.read_csv(csv_path)

client = boto3.client("runtime.sagemaker")

body = data.to_csv(index=False).encode("utf-8")

response = client.invoke_endpoint(
    EndpointName="endpoint_name",
    ContentType="text/csv",
    Body=body,
    Accept="application/json"
)
```

The following example shows you how to invoke image prediction models.

```
import boto3
client = boto3.client("runtime.sagemaker")
with open("example_image.jpg", "rb") as file:
    body = file.read()
    response = client.invoke_endpoint(
        EndpointName="endpoint_name",
        ContentType="application/x-image",
        Body=body,
        Accept="application/json"
    )
```

The following example shows you how to invoke text prediction models.

```
import boto3
import pandas as pd

client = boto3.client("runtime.sagemaker")
body = pd.DataFrame([["Example text 1"], ["Example text 2"]]).to_csv(header=False, index=False).encode("utf-8")

response = client.invoke_endpoint(
    EndpointName="endpoint_name",
    ContentType="text/csv",
    Body=body,
    Accept="application/json"
)
```
