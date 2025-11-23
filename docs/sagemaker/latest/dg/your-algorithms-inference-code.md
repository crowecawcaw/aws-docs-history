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
- [Container Contract to Support Bidirectional Streaming Capabilities](#your-algorithms-inference-algo-bidi "#your-algorithms-inference-algo-bidi")
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
- [InvokeEndpointWithResponseStream](../APIReference/API_runtime_InvokeEndpointWithBidirectionalStream.md "../APIReference/API_runtime_InvokeEndpointWithBidirectionalStream.md")

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
- A customer’s model container that supports bidirectional streaming
  must:
  - support WebSockets connections on port 8080 to /invocations-bidirectional-stream by default.
  - have a web server listening on port 8080 and must accept POST requests to the /ping endpoints.
  - In addition to container health checks over HTTP, container must
    respond with Pong Frame per ([RFC6455](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3")), for WebSocket Ping Frame sent.

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

###### Example invocation functions for bidirectional streaming

The following examples demonstrate how the code in your container can process
streaming inference request and responses. These examples handle streaming requests
that client applications send by using the InvokeEndpointWithBidirectionalStream
action.

A container with bidirectional streaming capability handles streaming inference
requests where parts are incrementally generated at the client and streamed to the
container. It returns the model's inference back to the client as a series of parts
as the model generates them. Client applications start receiving responses
immediately when they're available. They don't need to wait for request to the fully
generated at the client or for the model to generate the entire response. You can
implement bidirectional streaming to support fast interactive experiences, such as
chatbots, interactive voice AI assistants and real-time translations for a more
real-time experience.

FastAPI
FastAPI is a web framework for building APIs with Python.

```
import sys
import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
...
@app.websocket("/invocations-bidirectional-stream")
async def websocket_invoke(websocket: WebSocket):
    """
    WebSocket endpoint with RFC 6455 ping/pong and fragmentation support

    Handles:
    - Text messages (JSON) - including fragmented frames
    - Binary messages - including fragmented frames
    - Ping frames (automatically responds with pong)
    - Pong frames (logs receipt)
    - Fragmented frames per RFC 6455 Section 5.4
    """
    await manager.connect(websocket)

    # Fragment reassembly buffers per RFC 6455 Section 5.4
    text_fragments = []
    binary_fragments = []

    while True:
        # Use receive() to handle all WebSocket frame types
        message = await websocket.receive()
        print(f"Received message: {message}")
        if message["type"] == "websocket.receive":
            if "text" in message:
                # Handle text frames (including fragments)
                text_data = message["text"]
                more_body = message.get("more_body", False)

                if more_body:
                    # This is a fragment, accumulate it
                    text_fragments.append(text_data)
                    print(f"Received text fragment: {len(text_data)} chars (more coming)")
                else:
                    # This is the final frame or a complete message
                    if text_fragments:
                        # Reassemble fragmented message
                        text_fragments.append(text_data)
                        complete_text = "".join(text_fragments)
                        text_fragments.clear()
                        print(f"Reassembled fragmented text message: {len(complete_text)} chars total")
                        await handle_text_message(websocket, complete_text)
                    else:
                        # Complete message in single frame
                        await handle_text_message(websocket, text_data)

            elif "bytes" in message:
                # Handle binary frames (including fragments)
                binary_data = message["bytes"]
                more_body = message.get("more_body", False)

                if more_body:
                    # This is a fragment, accumulate it
                    binary_fragments.append(binary_data)
                    print(f"Received binary fragment: {len(binary_data)} bytes (more coming)")
                else:
                    # This is the final frame or a complete message
                    if binary_fragments:
                        # Reassemble fragmented message
                        binary_fragments.append(binary_data)
                        complete_binary = b"".join(binary_fragments)
                        binary_fragments.clear()
                        print(f"Reassembled fragmented binary message: {len(complete_binary)} bytes total")
                        await handle_binary_message(websocket, complete_binary)
                    else:
                        # Complete message in single frame
                        await handle_binary_message(websocket, binary_data)

        elif message["type"] == "websocket.ping":
            # Handle ping frames - RFC 6455 Section 5.5.2
            ping_data = message.get("bytes", b"")
            print(f"Received PING frame with payload: {ping_data}")
            # FastAPI automatically sends pong response

        elif message["type"] == "websocket.pong":
            # Handle pong frames
            pong_data = message.get("bytes", b"")
            print(f"Received PONG frame with payload: {pong_data}")

        elif message["type"] == "websocket.close":
            # Handle close frames - RFC 6455 Section 5.5.1
            close_code = message.get("code", 1000)
            close_reason = message.get("reason", "")
            print(f"Received CLOSE frame - Code: {close_code}, Reason: '{close_reason}'")

            # Send close frame response if not already closing
            try:
                await websocket.close(code=close_code, reason=close_reason)
                print(f"Sent CLOSE frame response - Code: {close_code}")
            except Exception as e:
                print(f"Error sending close frame: {e}")
            break

        elif message["type"] == "websocket.disconnect":
            print("Client initiated disconnect")
            break

        else:
            print(f"Received unknown message type: {message['type']}")
            break


async def handle_binary_message(websocket: WebSocket, binary_data: bytes):
    """Handle incoming binary messages (complete or reassembled from fragments)"""
    print(f"Processing complete binary message: {len(binary_data)} bytes")

    try:
        # Echo back the binary data
        await websocket.send_bytes(binary_data)
    except Exception as e:
        print(f"Error handling binary message: {e}")

async def handle_text_message(websocket: WebSocket, data: str):
    """Handle incoming text messages"""
    try:
        # Send response back to the same client
        await manager.send_personal_message(data, websocket)
    except Exception as e:
        print(f"Error handling text message: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        print("Starting server on port 8080...")
        uvicorn.run(app, host="0.0.0.0", port=8080)
    else:
        print("Usage: python app.py serve")
        sys.exit(1)

if __name__ == "__main__":
    main()

```

In this example, the `websocket_invoke` function handles
the inference request that SageMaker AI sends to the
`/invocations-bidirectional-stream` endpoint. It shows
handling stream requests and stream responses back to the client.

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

Additionally, a container that is capable of handling bidirectional streaming requests
must respond with a Pong Frame (per WebSocket protocol [RFC6455](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3"))
to a Ping Frame. If no Pong Frame is received for 5 consecutive Pings, the connection to
container will be closed by SageMaker AI platform. SageMaker AI platform will also
respond to Ping Frames from model container with Pong Frames.

## Container Contract to Support Bidirectional Streaming Capabilities

If you want to host your model container as SageMaker AI endpoint that supports
bidirectional streaming capabilities, the model container must support the contract
below:

**1. Bidirectional Docker Label**

The model container should have a Docker label indicating to the SageMaker AI platform
that bidirectional streaming capability is supported on this container.

```
com.amazonaws.sagemaker.capabilities.bidirectional-streaming=true
```

**2. Support WebSocket Connection for
invocations**

A customer’s model container that supports bi-directional streaming must support WebSockets connections on port 8080 to `/invocations-bidirectional-stream` by default.

This path can be overridden by passing X-Amzn-SageMaker-Model-Invocation-Path header when invoking InvokeEndpointWithBidirectionalStream API. Additionally, users can specify a query string to be appended to this path by passing X-Amzn-SageMaker-Model-Query-String header when invoking InvokeEndpointWithBidirectionalStream API.

**3. Request Stream Handling**

The InvokeEndpointWithBidirectionalStream API input payloads are streamed in as a
series of PayloadParts, which is just a wrapper of a binary chunk (“Bytes”: **_<Blob>_**):

```
{
   "PayloadPart": {
      "Bytes": <Blob>,
      "DataType": <String: UTF8 | BINARY>,
      "CompletionState": <String: PARTIAL | COMPLETE>
      "P": <String>
   }
}
```

**3.1. Data Frames**

SageMaker AI passes the input PayloadParts to Model container as WebSocket Data Frames
([RFC6455-Section-5.6](https://datatracker.ietf.org/doc/html/rfc6455#section-5.6 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.6"))

1. SageMaker AI does not inspect into the binary chunk.
2. On receiving an input PayloadPart
   - SageMaker AI creates exactly one WebSocket Data Frame from
     `PayloadPart.Bytes`, then pass it to model container.
   - If `PayloadPart.DataType = UTF8`, SageMaker AI creates a Text Data Frame
   - If `PayloadPart.DataType` does not present or `PayloadPart.DataType = BINARY`, SageMaker AI creates a Binary Data Frame

3. For a sequence of PayloadParts with `PayloadPart.CompletionState =
PARTIAL`, and terminated by a PayloadPart with
   `PayloadPart.CompletionState = COMPLETE`, SageMaker AI translates
   them into WebSocket fragmented message [RFC6455-Section-5.4: Fragmentation](https://datatracker.ietf.org/doc/html/rfc6455#section-5.4 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.4"):
   - The initial PayloadPart with `PayloadPart.CompletionState = PARTIAL` will be translated into a WebSocket Data Frame, with FIN bit clear.
   - The subsequent PayloadParts with `PayloadPart.CompletionState = PARTIAL` will be translated into WebSocket Continuation Frames with FIN bit clear.
   - The final PayloadPart with `PayloadPart.CompletionState = COMPLETE` will be translated into WebSocket Continuation Frame with FIN bit set.

4. SageMaker AI does not encode or decode the binary chunk from the input PayloadPart, the bytes are passed to model container as-is.
5. SageMaker AI does not combine multiple input PayloadParts into one BinaryDataFrame.
6. SageMaker AI does not chunk one input PayloadPart into multiple BinaryDataFrames.

**Example: Fragmented Message Flow**

```
Client sends:
PayloadPart 1: {Bytes: "Hello ", DataType: "UTF8", CompletionState: "PARTIAL"}
PayloadPart 2: {Bytes: "World", DataType: "UTF8", CompletionState: "COMPLETE"}

Container receives:
Frame 1: Text Data Frame with "Hello " (FIN=0)
Frame 2: Continuation Frame with "World" (FIN=1)
```

**3.2. Control Frames**

Besides Data Frames, SageMaker AI also sends Control Frames to model container ([RFC6455-Section-5.5](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5")):

1. Close Frame: SageMaker AI may send Close Frame ([RFC6455-Section-5.5.1](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.1 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.1")) to model container should the connection be
   closed for any reason.
2. Ping Frame: SageMaker AI send Ping Frame ([RFC6455-Section-5.5.2](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2")) once every 60 seconds, model container must
   respond with Pong Frame. If no Pong Frame ([RFC6455-Section-5.5.3](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3")) is received for 5 consecutive Pings, the
   connection will be closed by SageMaker AI.
3. Pong Frame: SageMaker AI will respond to Ping Frames from model container with Pong Frames.

**4. Response Stream Handling**

The output are streamed out as a series of PayloadParts, ModelStreamErrors or
InternalStreamFailures.

```
{
   "PayloadPart": {
      "Bytes": <Blob>,
      "DataType": <String: UTF8 | BINARY>,
      "CompletionState": <String: PARTIAL | COMPLETE>,
   },
   "ModelStreamError": {
      "ErrorCode": <String>,
      "Message": <String>
   },
   "InternalStreamFailure": {
      "Message": <String>
   }
}
```

**4.1. Data Frames**

SageMaker AI convert Data Frames received from model container into output
PayloadParts:

1. On receiving a WebSocket Text Data Frame from the model container, SageMaker AI gets the raw bytes from the Text Data Frame, and wraps it into a response PayloadPart, meanwhile set `PayloadPart.DataType = UTF8`.
2. On receiving a WebSocket Binary Data Frame from the model container, SageMaker AI directly wraps the bytes from the data frame into a response PayloadPart, meanwhile set `PayloadPart.DataType = BINARY`.
3. For fragmented message as defined in [RFC6455-Section-5.4: Fragmentation](https://datatracker.ietf.org/doc/html/rfc6455#section-5.4 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.4"):
   - The initial Data Frame with FIN bit clear will be translated into a PayloadPart with `PayloadPart.CompletionState = PARTIAL`.
   - The subsequent Continuation Frames with FIN bit clear will be translated into PayloadParts with `PayloadPart.CompletionState = PARTIAL`.
   - The final Continuation Frame with FIN bit set will be translated into PayloadPart with `PayloadPart.CompletionState = COMPLETE`.

4. SageMaker AI does not encode or decode the bytes received from model containers, the bytes are passed to model container as-is.
5. SageMaker AI does not combine multiple Data Frames received from model container into one response PayloadPart.
6. SageMaker AI does not chunk a Data Frame received from model container into multiple response PayloadParts.

**Example: Streaming Response Flow**

```
Container sends:
Frame 1: Text Data Frame with "Generating" (FIN=0)
Frame 2: Continuation Frame with " response..." (FIN=1)

Client receives:
PayloadPart 1: {Bytes: "Generating", DataType: "UTF8", CompletionState: "PARTIAL"}
PayloadPart 2: {Bytes: " response...", DataType: "UTF8", CompletionState: "COMPLETE"}
```

**4.2. Control Frames**

SageMaker AI responds to the following Control Frames from the model container:

1. On receiving a Close Frame ([RFC6455-Section-5.5.1](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.1 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.1")) from model container, SageMaker AI will wrap
   the status code ([RFC6455-Section-7.4](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4 "https://datatracker.ietf.org/doc/html/rfc6455#section-7.4")) and failure messages into ModelStreamError,
   and stream it back to the end user.
2. On receiving a Ping Frame ([RFC6455-Section-5.5.2](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2")) from model container, SageMaker AI will
   respond with Pong Frame.
3. Pong Frame([RFC6455-Section-5.5.3](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3 "https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3")): If no Pong Frame is received for 5
   consecutive Pings, the connection will be closed by SageMaker AI.
