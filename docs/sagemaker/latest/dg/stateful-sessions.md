# Stateful sessions with Amazon SageMaker AI models

When you send requests to an Amazon SageMaker AI inference endpoint, you can choose to route the
requests to a _stateful session_. During a stateful
session, you send multiple inference requests to the same ML instance, and the instance
facilitates the session.

Normally, when you invoke an inference endpoint, Amazon SageMaker AI routes your request to any one
ML instance among the multiple instances that the endpoint hosts. This routing behavior
helps minimize latency by evenly distributing your inference traffic. However, one outcome
of the routing behavior is that you can't predict which instance will serve your request.

This unpredictability is a limitation if you intend to send your request to a _stateful model_. A stateful model has a container that caches
the context data that it receives from inference requests. Because the data is cached, you
can interact with the container by sending multiple requests, and with each request, you
don't need to include the full context of the interaction. Instead, the model draws from the
cached context data to inform its prediction.

Stateful models are ideal when the context data for the interaction is very large, such as
when it includes the following:

- Large text files
- Long chat histories
- Multimedia data (images, video, and audio) for multimodal models
  In these cases, if you pass the full context with every prompt, the network latency of
  your requests is slowed, and responsiveness of your application is diminished.

Before your inference endpoint can support a stateful session, it must host a stateful
model. The implementation of the stateful model is owned by you. Amazon SageMaker AI makes it possible
for you to route your requests to a stateful session, but it doesn't provide stateful models
that you can deploy and use.

For an example notebook and model container that demonstrates how stateful interactions
are implemented, see [Example implementation](#stateful-sessions-example-notebook "#stateful-sessions-example-notebook").

For information about implementing stateful models with TorchServe, see [Stateful Inference](https://github.com/pytorch/serve/tree/master/examples/stateful/sequence_continuous_batching "https://github.com/pytorch/serve/tree/master/examples/stateful/sequence_continuous_batching") in the TorchServe GitHub repository.

## How stateful sessions work

During a stateful session, your application interacts with your model container in the
following ways.

###### To start a stateful session

1. To start a session with a stateful model that's hosted by Amazon SageMaker AI, your
   client sends an [`InvokeEndpoint`](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md") request with the SageMaker API. For the
   `SessionID` request parameter, the client tells SageMaker AI to start a
   new session by specifying the value `NEW_SESSION`. In the request
   payload, the client also tells the container to start a new session. The syntax
   of this statement varies based on your container implementation. It depends on
   how your container code handles the request payload.

The following example starts a new session by using the SDK for Python (Boto3):

```
import boto3
import sagemaker
import json

payload = {
"requestType":"NEW_SESSION"
}
payload = json.dumps(payload)

smr = boto3.client(
    'sagemaker-runtime',
    region_name="`region_name`",
    endpoint_url="`endoint_url`")

create_session_response = smr.invoke_endpoint(
    EndpointName="`endpoint_name`",
    Body=`payload`,
    ContentType="application/json",
    SessionId="NEW_SESSION")
```

2. Your model container handles your client's request by starting a new session.
   For the session, it caches the data that the client sends in the request
   payload. It also creates a session ID, and it sets a time to live (TTL)
   timestamp. This timestamp indicates when the session expires. The container must
   provide the session ID and timestamp to Amazon SageMaker AI by setting the following HTTP
   header in the response:

```
X-Amzn-SageMaker-Session-Id: `session_id`; Expires=`yyyy`-`mm`-`ddThh`:`mm`:`ssZ`
```

3. In the response to the `InvokeEndpoint` request, Amazon SageMaker AI provides
   the session ID and TTL timestamp for the `NewSessionID` response
   parameter.

The following example extracts the session ID from the
`invoke_endpoint` response:

```
session_id = create_session_response['ResponseMetadata']['HTTPHeaders']['x-amzn-sagemaker-new-session-id'].split(';')[0]
```

###### To continue a stateful session

- To use the same session for a subsequent inference request, your client sends
  another `InvokeEndpoint` request. For the `SessionID`
  request parameter, it specifies the ID of the session. With this ID, SageMaker AI routes
  the request to the same ML instance where the session was started. Because your
  container has already cached the original request payload, your client doesn't
  need to pass the same context data that was in the original request.

The following example continues a session by passing the session ID with the
`SessionId` request parameter:

```
smr.invoke_endpoint(
    EndpointName="`endpoint_name`",
    Body=`payload`,
    ContentType="application/json",
    SessionId=session_id)
```

###### To close a stateful session

1. To close a session, your client sends a final `InvokeEndpoint`
   request. For the `SessionID` request parameter, the client provides
   the ID of the session. In the payload in the request body, your client states
   that the container should close the session. The syntax of this statement varies
   based on your container implementation.

The following example closes a session:

```
payload = {
    "requestType":"CLOSE"
}
payload = json.dumps(payload)

closeSessionResponse = smr.invoke_endpoint(
    EndpointName="`endpoint_name`",
    Body=payload,
    ContentType="application/json",
    SessionId=session_id)
```

2. When it closes the session, the container returns the session ID to SageMaker AI by
   setting the following HTTP header in the response:

```
X-Amzn-SageMaker-Closed-Session-Id: `session_id`
```

3. In the response to the `InvokeEndpoint` request from the client,
   SageMaker AI provides the session ID for the `ClosedSessionId` response
   parameter.

The following example extracts the closed session ID from the
`invoke_endpoint` response:

```
closed_session_id = closeSessionResponse['ResponseMetadata']['HTTPHeaders']['x-amzn-sagemaker-closed-session-id'].split(';')[0]
```

## Example implementation

The following example notebook demonstrates how to implement the container for a
stateful model. It also demonstrates how a client application starts, continues, and
closes a stateful session.

[LLaVA stateful inference with SageMaker AI](https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/LLava/torchserve/workspace/llava_stateful_deploy_infer.ipynb "https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/LLava/torchserve/workspace/llava_stateful_deploy_infer.ipynb")

The notebook uses the [LLaVA: Large Language and Vision Assistant](https://github.com/haotian-liu/LLaVA/tree/main "https://github.com/haotian-liu/LLaVA/tree/main") model, which accepts images and
text prompts. The notebook uploads an image to the model, and then it asks questions
about the image without having to resend the image for every request. The model
container uses the TorchServe framework. It caches the image data in GPU memory.
