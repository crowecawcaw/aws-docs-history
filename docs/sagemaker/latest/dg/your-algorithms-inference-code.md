# Custom Inference Code with Hosting

Services

This section explains how Amazon SageMaker AI interacts with a Docker container that runs your own
inference code for hosting services. Use this information to write inference code and create
a Docker image.

###### Topics

- [How SageMaker AI Runs Your Inference
  Image](#your-algorithms-inference-code-run-image "#your-algorithms-inference-code-run-image")
- [How SageMaker AI Loads Your
  Model Artifacts](#your-algorithms-inference-code-load-artifacts "#your-algorithms-inference-code-load-artifacts")
- [How Your Container
  Should Respond to Inference Requests](#your-algorithms-inference-code-container-response "#your-algorithms-inference-code-container-response")
- [How Your Container Should
  Respond to Health Check (Ping) Requests](#your-algorithms-inference-algo-ping-requests "#your-algorithms-inference-algo-ping-requests")
- [Use a Private Docker Registry
  for Real-Time Inference Containers](your-algorithms-containers-inference-private.md "your-algorithms-containers-inference-private.md")

## How SageMaker AI Runs Your Inference

Image

To configure a container to run as an executable, use an `ENTRYPOINT`
instruction in a Dockerfile. Note the following:

- For model inference, SageMaker AI runs the container as:

```
docker run `image` serve
```

SageMaker AI overrides default `CMD` statements in a container by
specifying the `serve` argument after the image name. The
`serve` argument overrides arguments that you provide with the
`CMD` command in the Dockerfile.

- SageMaker AI expects all containers to run with root users. Create your container so
  that it uses only root users. When SageMaker AI runs your container, users that do not
  have root-level access can cause permissions issues.
- We recommend that you use the `exec` form of the
  `ENTRYPOINT` instruction:

```
ENTRYPOINT ["executable", "param1", "param2"]
```

For example:

```
ENTRYPOINT ["python", "k_means_inference.py"]
```

The `exec` form of the `ENTRYPOINT` instruction starts
the executable directly, not as a child of `/bin/sh`. This
enables it to receive signals like `SIGTERM` and `SIGKILL`
from the SageMaker API operations, which is a requirement.

 

For example, when you use the [`CreateEndpoint`](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API to create an endpoint, SageMaker AI
provisions the number of ML compute instances required by the endpoint
configuration, which you specify in the request. SageMaker AI runs the Docker container
on those instances.

 

If you reduce the number of instances backing the endpoint (by calling the
[`UpdateEndpointWeightsAndCapacities`](../APIReference/API_UpdateEndpointWeightsAndCapacities.md "../APIReference/API_UpdateEndpointWeightsAndCapacities.md") API), SageMaker AI runs a
command to stop the Docker container on the instances that are being terminated.
The command sends the `SIGTERM` signal, then it sends the
`SIGKILL` signal thirty seconds later.

 

If you update the endpoint (by calling the [`UpdateEndpoint`](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md") API), SageMaker AI launches another set of ML
compute instances and runs the Docker containers that contain your inference
code on them. Then it runs a command to stop the previous Docker containers. To
stop a Docker container, command sends the `SIGTERM` signal, then it
sends the `SIGKILL` signal 30 seconds later.

- SageMaker AI uses the container definition that you provided in your [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") request to set environment variables and
  the DNS hostname for the container as follows:

   
  - It sets environment variables using the
    `ContainerDefinition.Environment` string-to-string
    map.
  - It sets the DNS hostname using the
    `ContainerDefinition.ContainerHostname`.

- If you plan to use GPU devices for model inferences (by specifying GPU-based
  ML compute instances in your
  `CreateEndpointConfig` request), make sure that your containers
  are `nvidia-docker` compatible. Don't bundle NVIDIA drivers with the
  image. For more
  information about `nvidia-docker`, see [NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker "https://github.com/NVIDIA/nvidia-docker").
- You can't use the `tini` initializer as your entry point in SageMaker AI
  containers because it gets confused by the `train` and
  `serve` arguments.

## How SageMaker AI Loads Your

Model Artifacts

In your [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API request, you can use either the
`ModelDataUrl` or `S3DataSource` parameter to identify the S3
location where model artifacts are stored. SageMaker AI copies your model artifacts from the S3
location to the `/opt/ml/model` directory for use by your inference
code. Your container has read-only access to `/opt/ml/model`. Do not
write to this directory.

The `ModelDataUrl` must point to a tar.gz file. Otherwise, SageMaker AI won't
download the file.

If you trained your model in SageMaker AI, the model artifacts are saved as a single
compressed tar file in Amazon S3. If you trained your model outside SageMaker AI, you need to
create this single compressed tar file and save it in a S3 location. SageMaker AI decompresses
this tar file into /opt/ml/model directory before your container starts.

For deploying large models, we recommend that you follow [Deploying uncompressed models](large-model-inference-uncompressed.md "large-model-inference-uncompressed.md").

## How Your Container

Should Respond to Inference Requests

To obtain inferences, the client application sends a POST request to the SageMaker AI
endpoint. SageMaker AI passes the request to the container, and returns the inference result
from the container to the client.

For more information about the inference requests that your container will receive,
see the following actions in the _Amazon SageMaker AI API Reference_:

- [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md")
- [InvokeEndpointAsync](../APIReference/API_runtime_InvokeEndpointAsync.md "../APIReference/API_runtime_InvokeEndpointAsync.md")
- [InvokeEndpointWithResponseStream](../APIReference/API_runtime_InvokeEndpointWithResponseStream.md "../APIReference/API_runtime_InvokeEndpointWithResponseStream.md")

###### Requirements for inference containers

To respond to inference requests, your container must meet the following
requirements:

- SageMaker AI strips all `POST` headers except those supported by
  `InvokeEndpoint`. SageMaker AI might add additional headers. Inference
  containers must be able to safely ignore these additional headers.
- To receive inference requests, the container must have a web server listening
  on port 8080 and must accept `POST` requests to the
  `/invocations` and `/ping` endpoints.
- A customer's model containers must accept socket connection requests within
  250 ms.
- A customer's model containers must respond to requests within 60 seconds. The
  model itself can have a maximum processing time of 60 seconds before responding
  to the `/invocations`. If your model is going to take 50-60 seconds
  of processing time, the SDK socket timeout should be set to be 70
  seconds.

###### Example invocation functions

The following examples demonstrate how the code in your container can process
inference requests. These examples handle requests that client applications send by
using the InvokeEndpoint action.

FastAPI
FastAPI is a web framework for building APIs with Python.

```
from fastapi import FastAPI, status, Request, Response
. . .
app = FastAPI()
. . .
@app.post('/invocations')
async def invocations(request: Request):
    # model() is a hypothetical function that gets the inference output:
    model_resp = await model(Request)

    response = Response(
        content=model_resp,
        status_code=status.HTTP_200_OK,
        media_type="text/plain",
    )
    return response
. . .
```

In this example, the `invocations` function handles the
inference request that SageMaker AI sends to the `/invocations`
endpoint.

Flask
Flask is a framework for developing web applications with
Python.

```
import flask
. . .
app = flask.Flask(__name__)
. . .
@app.route('/invocations', methods=["POST"])
def invoke(request):
    # model() is a hypothetical function that gets the inference output:
    resp_body = model(request)
    return flask.Response(resp_body, mimetype='text/plain')

```

In this example, the `invoke` function handles the
inference request that SageMaker AI sends to the `/invocations`
endpoint.

###### Example invocation functions for streaming requests

The following examples demonstrate how the code in your inference container can
process streaming inference requests. These examples handle requests that client
applications send by using the InvokeEndpointWithResponseStream action.

When a container handles a streaming inference request, it returns the model's
inference as a series of parts incrementally as the model generates them. Client
applications start receiving responses immediately when they're available. They
don't need to wait for the model to generate the entire response. You can implement
streaming to support fast interactive experiences, such as chatbots, virtual
assistants, and music generators.

FastAPI
FastAPI is a web framework for building APIs with Python.

```
from starlette.responses import StreamingResponse
from fastapi import FastAPI, status, Request
. . .
app = FastAPI()
. . .
@app.post('/invocations')
async def invocations(request: Request):
    # Streams inference response using HTTP chunked encoding
    async def generate():
        # model() is a hypothetical function that gets the inference output:
        yield await model(Request)
        yield "\n"

    response = StreamingResponse(
        content=generate(),
        status_code=status.HTTP_200_OK,
        media_type="text/plain",
    )
    return response
. . .
```

In this example, the `invocations` function handles the
inference request that SageMaker AI sends to the `/invocations`
endpoint. To stream the response, the example uses the
`StreamingResponse` class from the Starlette
framework.

Flask
Flask is a framework for developing web applications with
Python.

```
import flask
. . .
app = flask.Flask(__name__)
. . .
@app.route('/invocations', methods=["POST"])
def invocations(request):
    # Streams inference response using HTTP chunked encoding

    def generate():
        # model() is a hypothetical function that gets the inference output:
        yield model(request)
        yield "\n"
    return flask.Response(
        flask.stream_with_context(generate()), mimetype='text/plain')
. . .
```

In this example, the `invocations` function handles the
inference request that SageMaker AI sends to the `/invocations`
endpoint. To stream the response, the example uses the
`flask.stream_with_context` function from the Flask
framework.

## How Your Container Should

Respond to Health Check (Ping) Requests

SageMaker AI launches new inference containers in the following situations:

- Responding to `CreateEndpoint`, `UpdateEndpoint`, and
  `UpdateEndpointWeightsAndCapacities` API calls
- Security patching
- Replacing unhealthy instances

Soon after container startup, SageMaker AI starts sending periodic GET requests to the
`/ping` endpoint.

The simplest requirement on the container is to respond with an HTTP 200 status code
and an empty body. This indicates to SageMaker AI that the container is ready to accept
inference requests at the `/invocations` endpoint.

If the container does not begin to pass health checks by consistently responding with
200s during the 8 minutes after startup, the new instance launch fails. This causes
`CreateEndpoint` to fail, leaving the endpoint in a failed state. The
update requested by `UpdateEndpoint` isn't completed, security patches
aren't applied, and unhealthy instances aren't replaced.

While the minimum bar is for the container to return a static 200, a container
developer can use this functionality to perform deeper checks. The request timeout on
`/ping` attempts is 2 seconds.
