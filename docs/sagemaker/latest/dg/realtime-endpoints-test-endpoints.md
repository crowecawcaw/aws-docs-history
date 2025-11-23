# Invoke models for real-time

inference

After you use Amazon SageMaker AI to deploy a model to an endpoint, you can interact with the model
by sending inference requests to it. To send an inference request to a model, you invoke the
endpoint that hosts it. You can invoke your endpoints using Amazon SageMaker Studio, the AWS
SDKs, or the AWS CLI.

## Invoke Your Model Using

Amazon SageMaker Studio

After you deploy your model to an endpoint, you can view the endpoint through
Amazon SageMaker Studio and test your endpoint by sending single inference requests.

###### Note

SageMaker AI only supports endpoint testing in Studio for real-time endpoints.

###### To send a test inference request to your endpoint

1. Launch Amazon SageMaker Studio.
2. In the navigation pane on the left, choose **Deployments**.
3. From the dropdown, choose **Endpoints**.
4. Find for your endpoint by name, and choose the name in the table. The endpoint
   names listed in the **Endpoints** panel are defined when you
   deploy a model. The Studio workspace opens the **Endpoint**
   page in a new tab.
5. Choose the **Test inference** tab.
6. For **Testing Options**, select one of the following:
   1. Select **Test the sample request** to immediately send
      a request to your endpoint. Use the **JSON editor** to provide
      sample data in JSON format, and choose **Send Request** to
      submit the request to your endpoint. After submitting your request, Studio
      shows the inference output in a card to the right of the JSON editor.
   2. Select **Use Python SDK example code** to view the code
      for sending a request to the endpoint. Then, copy the code example from the
      **Example inference request** section and run the code from
      your testing environment.

The top of the card shows the type of request that was sent to the endpoint (only JSON
is accepted). The card shows the following fields:

- **Status** – displays one of the following status types:
  - `Success` – The request succeeded.
  - `Failed` – The request failed. A response appears under **Failure
    Reason**.
  - `Pending` – While the inference request is pending, the status shows a
    spinning, circular icon.

- **Execution Length** – How long the invocation took (end time minus
  the start time) in milliseconds.
- **Request Time** – How many minutes have passed since the request was
  sent.
- **Result Time** – How many minutes have passed since the result was
  returned.

## Invoke Your Model by Using the

AWS SDK for Python (Boto3)

If you want to invoke a model endpoint in your application code, you can use one of
the AWS SDKs, including the AWS SDK for Python (Boto3). To invoke your endpoint with this SDK, you
use one of the following Python methods:

- `invoke_endpoint` – Sends an inference request to a model
  endpoint and returns the response that the model generates.

This method returns the inference payload as one response after the model
finishes generating it. For more information, see [invoke_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint.html") in the _AWS SDK for Python (Boto3) API Reference_.

- `invoke_endpoint_with_response_stream` – Sends an inference
  request to a model endpoint and streams the response incrementally while the
  model generates it.

With this method, your application receives parts of the response as soon as
the parts become available. For more information, see [invoke_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint.html") in the _AWS SDK for Python (Boto3) API Reference_.

Use this method only to invoke models that support inference streaming.

Before you can use these methods in your application code, you must initialize a SageMaker AI
Runtime client, and you must specify the name of your endpoint. The following example
sets up the client and endpoint for the rest of the examples that follow:

```
import boto3

sagemaker_runtime = boto3.client(
    "sagemaker-runtime", region_name='`aws_region`')

endpoint_name='`endpoint-name`'

```

### Invoke to Get an Inference Response

The following example uses the `invoke_endpoint` method to invoke an
endpoint with the AWS SDK for Python (Boto3):

```
# Gets inference from the model hosted at the specified endpoint:
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    Body=bytes('{"features": ["This is great!"]}', 'utf-8')
    )

# Decodes and prints the response body:
print(response['Body'].read().decode('utf-8'))
```

This example provide input data in the `Body` field for SageMaker AI to pass to
the model. This data must be in the same format that was used for training. The
example assigns the response to the `response` variable.

The `response` variable provides access to the HTTP status, the name of
the deployed model, and other fields. The following snippet prints the HTTP status
code:

```
print(response["HTTPStatusCode"])
```

### Invoke to Stream an

Inference Response

If you deployed a model that supports inference streaming, you can invoke the
model to receive its inference payload as a stream of parts. The model delivers
these parts incrementally as the model generates them. When an application receives
an inference stream, the application doesn't need to wait for the model to generate
the whole response payload. Instead, the application immediately receives parts of
the response as they become available.

By consuming an inference stream in your application, you can create interactions
where your users perceive the inference to be fast because they get the first part
immediately. You can implement streaming to support fast interactive experiences,
such as chatbots, virtual assistants, and music generators. For example, you could
create a chatbot that incrementally shows the text generated by a large language
model (LLM).

To get an inference stream, you can use the
`invoke_endpoint_with_response_stream` method. In the response body,
the SDK provides an `EventStream` object, which gives the inference as a
series of `PayloadPart` objects.

###### Example Inference Stream

The following example is a stream of `PayloadPart` objects:

```
{'PayloadPart': {'Bytes': b'{"outputs": [" a"]}\n'}}
{'PayloadPart': {'Bytes': b'{"outputs": [" challenging"]}\n'}}
{'PayloadPart': {'Bytes': b'{"outputs": [" problem"]}\n'}}
. . .
```

In each payload part, the `Bytes` field provides a portion of the
inference response from the model. This portion can be any content type that a model
generates, such as text, image, or audio data. In this example, the portions are
JSON objects that contain generated text from an LLM.

Usually, the payload part contains a discrete chunk of data from the model. In
this example, the discrete chunks are whole JSON objects. Occasionally, the
streaming response splits the chunks over multiple payload parts, or it combines
multiple chunks into one payload part. The following example shows a chunk of data
in JSON format that's split over two payload parts:

```
{'PayloadPart': {'Bytes': b'{"outputs": '}}
{'PayloadPart': {'Bytes': b'[" problem"]}\n'}}
```

When you write application code that processes an inference stream, include logic
that handles these occasional splits and combinations of data. As one strategy, you
could write code that concatenates the contents of `Bytes` while your
application receives the payload parts. By concatenating the example JSON data here,
you would combine the data into a newline-delimited JSON body. Then, your code could
process the stream by parsing the whole JSON object on each line.

The following example shows the newline-delimited JSON that you would create when
you concatenate the example contents of `Bytes`:

```
{"outputs": [" a"]}
{"outputs": [" challenging"]}
{"outputs": [" problem"]}
. . .
```

###### Example Code to Process an Inference Stream

The following example Python class, `SmrInferenceStream`, demonstrates how
you can process an inference stream that sends text data in JSON format:

```
import io
import json

# Example class that processes an inference stream:
class SmrInferenceStream:

    def __init__(self, sagemaker_runtime, endpoint_name):
        self.sagemaker_runtime = sagemaker_runtime
        self.endpoint_name = endpoint_name
        # A buffered I/O stream to combine the payload parts:
        self.buff = io.BytesIO()
        self.read_pos = 0

    def stream_inference(self, request_body):
        # Gets a streaming inference response
        # from the specified model endpoint:
        response = self.sagemaker_runtime\
            .invoke_endpoint_with_response_stream(
                EndpointName=self.endpoint_name,
                Body=json.dumps(request_body),
                ContentType="application/json"
        )
        # Gets the EventStream object returned by the SDK:
        event_stream = response['Body']
        for event in event_stream:
            # Passes the contents of each payload part
            # to be concatenated:
            self._write(event['PayloadPart']['Bytes'])
            # Iterates over lines to parse whole JSON objects:
            for line in self._readlines():
                resp = json.loads(line)
                part = resp.get("outputs")[0]
                # Returns parts incrementally:
                yield part

    # Writes to the buffer to concatenate the contents of the parts:
    def _write(self, content):
        self.buff.seek(0, io.SEEK_END)
        self.buff.write(content)

    # The JSON objects in buffer end with '\n'.
    # This method reads lines to yield a series of JSON objects:
    def _readlines(self):
        self.buff.seek(self.read_pos)
        for line in self.buff.readlines():
            self.read_pos += len(line)
            yield line[:-1]
```

This example processes the inference stream by doing the following:

- Initializes a SageMaker AI Runtime client and sets the name of a model endpoint.
  Before you can get an inference stream, the model that the endpoint hosts must
  support inference streaming.
- In the example `stream_inference` method, receives a request body
  and passes it to the `invoke_endpoint_with_response_stream` method of
  the SDK.
- Iterates over each event in the `EventStream` object that the SDK
  returns.
- From each event, gets the contents of the `Bytes` object in the
  `PayloadPart` object.
- In the example `_write` method, writes to a buffer to concatenate
  the contents of the `Bytes` objects. The combined contents form a
  newline-delimited JSON body.
- Uses the example `_readlines` method to get an iterable series of
  JSON objects.
- In each JSON object, gets a piece of the inference.
- With the `yield` expression, returns the pieces
  incrementally.

The following example creates and uses a `SmrInferenceStream`
object:

```
request_body = {"inputs": ["Large model inference is"],
                "parameters": {"max_new_tokens": 100,
                               "enable_sampling": "true"}}
smr_inference_stream = SmrInferenceStream(
    sagemaker_runtime, endpoint_name)
stream = smr_inference_stream.stream_inference(request_body)
for part in stream:
    print(part, end='')
```

This example passes a request body to the `stream_inference` method. It
iterates over the response to print each piece that the inference stream returns.

The example assumes that the model at the specified endpoint is an LLM that generates
text. The output from this example is a body of generated text that prints
incrementally:

```
a challenging problem in machine learning. The goal is to . . .
```

## Invoke Your Model by Using the

AWS CLI

You can invoke your model endpoint by running commands with the AWS Command Line Interface (AWS CLI). The
AWS CLI supports standard inference requests with the `invoke-endpoint`
command, and it supports asynchronous inference requests with the
`invoke-endpoint-async` command.

###### Note

The AWS CLI doesn't support streaming inference requests.

The following example uses the `invoke-endpoint` command to send an
inference request to a model endpoint:

```
aws sagemaker-runtime invoke-endpoint \
    --endpoint-name `endpoint_name` \
    --body `fileb://$file_name` \
    `output_file.txt`
```

For the `--endpoint-name` parameter, provide the endpoint name that you
specified when you created the endpoint. For the `--body` parameter, provide
input data for SageMaker AI to pass to the model. The data must be in the same format that was
used for training. This example shows how to send binary data to your endpoint.

For more information on when to use `file://` over
`fileb://` when passing the contents of a file to a parameter of
the AWS CLI, see [Best Practices for Local File Parameters](https://aws.amazon.com/blogs/developer/best-practices-for-local-file-parameters/ "https://aws.amazon.com/blogs/developer/best-practices-for-local-file-parameters/").

For more information, and to see additional parameters that you can pass, see [`invoke-endpoint`](../../../cli/latest/reference/sagemaker-runtime/invoke-endpoint.md "../../../cli/latest/reference/sagemaker-runtime/invoke-endpoint.md") in the _AWS CLI Command Reference_.

If the `invoke-endpoint` command succeeds it returns a response such as the
following:

```
{
    "ContentType": "<content_type>; charset=utf-8",
    "InvokedProductionVariant": "<Variant>"
}
```

If the command doesn't succeed, check whether the input payload is in the correct
format.

View the output of the invocation by checking the file output file (`output_file.txt` in this example).

```
more output_file.txt
```

## Invoke Your Model by Using the

AWS SDK for Python

### Invoke to Bidirectionally Stream an Inference Request and Response

If you want to invoke a model endpoint in your application code to supports
bidirectional streaming, you can use the [new experimental SDK for
Python](https://github.com/awslabs/aws-sdk-python "https://github.com/awslabs/aws-sdk-python") that supports bidirectional streaming capability with HTTP/2 support.
This SDK enables real-time, two-way communication between your client application and
the SageMaker endpoint, allowing you to send inference requests incrementally while
simultaneously receiving streaming responses as the model generates them. This is
particularly useful for interactive applications where both the client and server need
to exchange data continuously over a persistent connection.

###### Note

The new experimental SDK is different from the standard Boto3 SDK and supports
persistent bidirectional connections for data exchange. While using the experimental
Python SDK we strongly advise strict pinning to a version of the SDK for any
non-experimental use cases.

To invoke your endpoint with bidirectional streaming, use the
`invoke_endpoint_with_bidirectional_stream` method. This method establishes a persistent
connection that allows you to stream multiple payload chunks to your model while
receiving responses in real-time as the model processes data. The connection remains
open until you explicitly close the input stream or the endpoint closes the connection,
supporting up to 30 minutes of connection time.

### Prerequisites

Before you can use bidirectional streaming in your application code, you must:

1. Install the experimental SageMaker Runtime HTTP/2 SDK
2. Set up AWS credentials for your SageMaker Runtime client
3. Deploy a model that supports bidirectional streaming to a SageMaker endpoint

### Set up the bidirectional streaming client

The following example shows how to initialize the required components for bidirectional streaming:

```
from sagemaker_runtime_http2.client import SageMakerRuntimeHTTP2Client
from sagemaker_runtime_http2.config import Config, HTTPAuthSchemeResolver
from smithy_aws_core.identity import EnvironmentCredentialsResolver
from smithy_aws_core.auth.sigv4 import SigV4AuthScheme

# Configuration
AWS_REGION = "us-west-2"
BIDI_ENDPOINT = f"https://runtime.sagemaker.{AWS_REGION}.amazonaws.com:8443"
ENDPOINT_NAME = "your-endpoint-name"

# Initialize the client configuration
config = Config(
    endpoint_uri=BIDI_ENDPOINT,
    region=AWS_REGION,
    aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
    auth_scheme_resolver=HTTPAuthSchemeResolver(),
    auth_schemes={"aws.auth#sigv4": SigV4AuthScheme(service="sagemaker")}
)

# Create the SageMaker Runtime HTTP/2 client
client = SageMakerRuntimeHTTP2Client(config=config)
```

### Complete bidirectional streaming client

The following example demonstrates how to create a bidirectional streaming client that sends multiple text payloads to a SageMaker endpoint and processes responses in real-time:

```
import asyncio
import logging
from sagemaker_runtime_http2.client import SageMakerRuntimeHTTP2Client
from sagemaker_runtime_http2.config import Config, HTTPAuthSchemeResolver
from sagemaker_runtime_http2.models import (
    InvokeEndpointWithBidirectionalStreamInput,
    RequestStreamEventPayloadPart,
    RequestPayloadPart
)
from smithy_aws_core.identity import EnvironmentCredentialsResolver
from smithy_aws_core.auth.sigv4 import SigV4AuthScheme

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SageMakerBidirectionalClient:

    def __init__(self, endpoint_name, region="us-west-2"):
        self.endpoint_name = endpoint_name
        self.region = region
        self.client = None
        self.stream = None
        self.response_task = None
        self.is_active = False

    def _initialize_client(self):
        bidi_endpoint = f"runtime.sagemaker.{self.region}.amazonaws.com:8443"
        config = Config(
            endpoint_uri=bidi_endpoint,
            region=self.region,
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
            auth_scheme_resolver=HTTPAuthSchemeResolver(),
            auth_schemes={"aws.auth#sigv4": SigV4AuthScheme(service="sagemaker")}
        )
        self.client = SageMakerRuntimeHTTP2Client(config=config)

    async def start_session(self):
        """Establish a bidirectional streaming connection with the endpoint."""
        if not self.client:
            self._initialize_client()

        logger.info(f"Starting session with endpoint: {self.endpoint_name}")
        self.stream = await self.client.invoke_endpoint_with_bidirectional_stream(
            InvokeEndpointWithBidirectionalStreamInput(endpoint_name=self.endpoint_name)
        )
        self.is_active = True

        # Start processing responses concurrently
        self.response_task = asyncio.create_task(self._process_responses())

    async def send_message(self, message):
        """Send a single message to the endpoint."""
        if not self.is_active:
            raise RuntimeError("Session not active. Call start_session() first.")

        logger.info(f"Sending message: {message}")
        payload = RequestPayloadPart(bytes_=message.encode('utf-8'))
        event = RequestStreamEventPayloadPart(value=payload)
        await self.stream.input_stream.send(event)

    async def send_multiple_messages(self, messages, delay=1.0):
        """Send multiple messages with a delay between each."""
        for message in messages:
            await self.send_message(message)
            await asyncio.sleep(delay)

    async def end_session(self):
        """Close the bidirectional streaming connection."""
        if not self.is_active:
            return

        await self.stream.input_stream.close()
        self.is_active = False
        logger.info("Stream closed")

        # Cancel the response processing task
        if self.response_task and not self.response_task.done():
            self.response_task.cancel()

    async def _process_responses(self):
        """Process incoming responses from the endpoint."""
        try:
            output = await self.stream.await_output()
            output_stream = output[1]

            while self.is_active:
                result = await output_stream.receive()

                if result is None:
                    logger.info("No more responses")
                    break

                if result.value and result.value.bytes_:
                    response_data = result.value.bytes_.decode('utf-8')
                    logger.info(f"Received: {response_data}")

        except Exception as e:
            logger.error(f"Error processing responses: {e}")

# Example usage
async def run_bidirectional_client():
    client = SageMakerBidirectionalClient(endpoint_name="your-endpoint-name")

    try:
        # Start the session
        await client.start_session()

        # Send multiple messages
        messages = [
            "I need help with",
            "my account balance",
            "I can help with that",
            "and recent charges"
        ]
        await client.send_multiple_messages(messages)

        # Wait for responses to be processed
        await asyncio.sleep(2)

        # End the session
        await client.end_session()
        logger.info("Session ended successfully")

    except Exception as e:
        logger.error(f"Client error: {e}")
        await client.end_session()

if __name__ == "__main__":
    asyncio.run(run_bidirectional_client())
```

The client initializes the SageMaker Runtime HTTP/2 client with the regional
endpoint URI on port 8443, which is required for bidirectional streaming
connections. The start\_`session()` method calls
`invoke_endpoint_with_bidirectional_stream()` to establish the persistent connection
and creates an asynchronous task to process incoming responses concurrently.

The `send_event()` method wraps payload data in the appropriate request objects and
sends them through the input stream, while the `_process_responses()` method
continuously listens for and processes responses from the endpoint as they arrive.
This bidirectional approach enables real-time interaction where both sending
requests and receiving responses happen simultaneously over the same
connection.
