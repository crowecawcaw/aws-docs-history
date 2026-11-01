

# Reporting usage for inference pricing
<a name="ml-inference-metering"></a>

If your product uses inference pricing, your container reports how many inferences each request or streaming session used. SageMaker AI passes the count to AWS Marketplace, which charges the buyer your price for each inference. What your container sends depends on how the buyer calls the endpoint. This topic covers real-time requests, streaming responses, and bidirectional streams.

With hourly pricing, your container doesn't report anything. SageMaker AI meters instance hours for you, and any counts that your container reports aren't charged.

Every report uses the dimension `inference.count`. It's the only dimension that AWS Marketplace accepts for machine learning products, and you can't add your own. Instead, you decide what one inference means and count accordingly. For guidance on choosing a unit, see [Inference pricing](machine-learning-pricing.md#ml-pricing-inference).

Your container runs a web server that answers requests from SageMaker AI on port 8080. You add the usage report to the responses that this server sends. The examples in this topic use FastAPI, a Python web framework that supports both HTTP and WebSocket connections. Any web framework works.

**Topics**
+ [Real-time requests](#ml-inference-metering-realtime)
+ [Streaming responses](#ml-inference-metering-response-stream)
+ [Bidirectional streams](#ml-inference-metering-bidi)
+ [Testing your usage reporting](#ml-inference-metering-test)

## Real-time requests
<a name="ml-inference-metering-realtime"></a>

When a buyer calls `InvokeEndpoint`, SageMaker AI sends the request to your container at `/invocations`. By default, AWS Marketplace charges one inference for each successful response (HTTP `2XX`). To charge a different number, add the `X-Amzn-Inference-Metering` header to your response. The following example charges three inferences:

```
X-Amzn-Inference-Metering: {"Dimension": "inference.count", "ConsumedUnits": 3}
```
+ `ConsumedUnits` is the number of inferences for this request. It can be a decimal, for example `2.5`. To charge nothing for a request, send `0`.
+ Responses with other status codes aren't charged.
+ If the header isn't valid, SageMaker AI fails the buyer's request with a validation error. The header isn't valid when it isn't JSON, when `ConsumedUnits` is missing or negative, or when `Dimension` is anything other than `inference.count`.

The following FastAPI example charges one inference for each image in the request.

```
import json

from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.post("/invocations")
async def invocations(request: Request):
    images = load_images(await request.body())  # your code
    labels = classify(images)  # your model code
    return Response(
        content=json.dumps(labels),
        media_type="application/json",
        headers={
            "X-Amzn-Inference-Metering": json.dumps(
                {"Dimension": "inference.count", "ConsumedUnits": len(images)}
            )
        },
    )
```

If your server uses Flask, as in [Creating model package images](ml-model-package-images.md), set the header on the response object: `response.headers["X-Amzn-Inference-Metering"] = json.dumps({"Dimension": "inference.count", "ConsumedUnits": len(images)})`.

## Streaming responses
<a name="ml-inference-metering-response-stream"></a>

When a buyer calls `InvokeEndpointWithResponseStream`, there's no default count. If your container doesn't send the `X-Amzn-Inference-Metering` header, the buyer isn't charged for the request.

Send the header with the response headers, before the first part of the response body. SageMaker AI reads the count when the response starts, so you can't change it after streaming begins. AWS Marketplace charges for the request only if the stream completes successfully. If you don't know the final size of the response at the start, base the count on what you do know, such as one per request or the size of the input. The validation rules for real-time requests also apply.

```
import json

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.post("/invocations")
async def invocations(request: Request):
    prompt = await request.json()
    units = 1  # known before the first part is sent, for example one per request
    return StreamingResponse(
        generate_tokens(prompt),  # your async generator
        media_type="text/plain",
        headers={
            "X-Amzn-Inference-Metering": json.dumps(
                {"Dimension": "inference.count", "ConsumedUnits": units}
            )
        },
    )
```

## Bidirectional streams
<a name="ml-inference-metering-bidi"></a>

When a buyer calls `InvokeEndpointWithBidirectionalStream`, there's also no default count. Your container reports usage while the session runs, on a second WebSocket connection called the *metadata connection*. If your container doesn't report usage, the buyer isn't charged for the session.

Your container must already support bidirectional streams, including the Docker label and the `/invocations-bidirectional-stream` WebSocket path. For how to build one, see [Support streaming responses and bidirectional streams](ml-model-package-images.md#ml-model-package-images-streaming). For the full contract, see [Container contract to support bidirectional streaming capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-bidi) in the *Amazon SageMaker AI Developer Guide*.

**To report usage on bidirectional streams**

1. **Opt in.** When SageMaker AI opens the data connection, include the following header in your WebSocket upgrade (101) response.

   ```
   X-Amzn-SageMaker-Metadata-Stream-Supported: true
   ```

   You can also include these optional headers:


**Optional headers for the metadata connection**  

<table>
<thead>
  <tr><th>Header</th><th>Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>X-Amzn-SageMaker-Metadata-Stream-Required</code></td><td><code>true</code> or <code>false</code> (default <code>false</code>)</td><td>If <code>true</code>, SageMaker AI stops the session when the metadata connection fails. Takes effect only when <code>X-Amzn-SageMaker-Metadata-Stream-Supported</code> is <code>true</code>.</td></tr>
  <tr><td><code>X-Amzn-SageMaker-Metadata-Invocation-Path</code></td><td>A path, without the leading slash</td><td>Changes the path of the metadata connection. The default is <code>/invocations-bidirectional-stream-metadata</code>.</td></tr>
</tbody>
</table>


1. **Accept the metadata connection.** Right after your upgrade response, SageMaker AI opens the metadata connection. Both connections carry the same `X-Amzn-SageMaker-Request-Id` header, so you can match the metadata connection to its session. Your container must accept the connection within 5 seconds. Register the session before you send the upgrade response, so that the metadata connection finds it.

1. **Send metering records.** Send each record as a JSON object in its own WebSocket text frame.

   ```
   {"Metering": {"Dimension": "inference.count", "ConsumedUnits": 2, "ClientToken": "8b3c2d41-1f0a-4c55-9a1e-2f4a7a0c6e19"}}
   ```


**Metering record fields**  

<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>Metering.Dimension</code></td><td>Yes</td><td>Must be <code>inference.count</code>. Records with any other value aren't charged.</td></tr>
  <tr><td><code>Metering.ConsumedUnits</code></td><td>Yes</td><td>The inferences used since your previous record. Each record is charged separately, so don't send a running total. Must be 0 or more. A record with 0 isn't charged. Can be a decimal, for example <code>2.5</code>.</td></tr>
  <tr><td><code>Metering.ClientToken</code></td><td>No</td><td>A unique ID for the record, up to 64 characters. If a token repeats on the same connection, SageMaker AI keeps only the first record.</td></tr>
</tbody>
</table>


   Follow these limits:
   + Each message can be up to 512 characters.
   + Send one record per frame, in text frames only.
   + Send at most one record per second on each connection. Records sent faster can be dropped.
   + A session can last up to 30 minutes.

   Report usage as it accrues, for example once a second. If a session ends unexpectedly, the usage that you already reported is still charged.

1. **End the session.** When SageMaker AI closes the data connection, send one final record that covers all unreported usage, and then close the metadata connection. Send the final record right away, because SageMaker AI accepts records for only a few seconds after the session ends.

   Keep the metadata connection open until the data connection closes. If the metadata connection closes during the session, SageMaker AI doesn't reopen it, so usage after that point isn't reported. If you don't close it after the session, SageMaker AI keeps the session's connections open until they time out.

SageMaker AI drops records that break these rules without returning an error to your container. Test your integration before you publish.

### What happens when the metadata connection fails
<a name="ml-inference-metering-bidi-failures"></a>


**Effect of the Required header on metadata connection failures**  

| Event | `Required` is `true` | `Required` is `false` (default) | 
| --- | --- | --- | 
| The metadata connection doesn't open | The buyer's request fails with HTTP 424. | The session continues, and its usage isn't reported. | 
| The metadata connection drops during the session | The session ends with a `ModelStreamError` event. | The session continues, and later usage isn't reported. | 
| A record isn't valid | SageMaker AI drops the record, and the connection stays open. | SageMaker AI drops the record, and the connection stays open. | 

### Example
<a name="ml-inference-metering-bidi-example"></a>

The following FastAPI example reports seconds of audio once a second, sends the final count when the session ends, and then closes the metadata connection. It assumes that audio arrives in binary frames, and `transcribe` stands in for your model code.

```
import asyncio
import json
import uuid

from fastapi import FastAPI, WebSocket

app = FastAPI()


class MeteringSession:
    """Usage for one bidirectional stream, keyed by the SageMaker request ID."""

    def __init__(self) -> None:
        self.units = 0
        self.ended = asyncio.Event()

    def add(self, units: int) -> None:
        self.units += units

    def take(self) -> int:
        units, self.units = self.units, 0
        return units


sessions: dict[str, MeteringSession] = {}


@app.websocket("/invocations-bidirectional-stream")
async def data_stream(websocket: WebSocket):
    request_id = websocket.headers["x-amzn-sagemaker-request-id"]
    session = sessions[request_id] = MeteringSession()  # register before accepting
    await websocket.accept(
        headers=[(b"x-amzn-sagemaker-metadata-stream-supported", b"true")]
    )
    try:
        async for audio_chunk in websocket.iter_bytes():
            transcript, seconds = transcribe(audio_chunk)  # your model code
            await websocket.send_text(transcript)
            session.add(seconds)
    finally:
        session.ended.set()


@app.websocket("/invocations-bidirectional-stream-metadata")
async def metadata_stream(websocket: WebSocket):
    request_id = websocket.headers["x-amzn-sagemaker-request-id"]
    session = sessions.get(request_id)
    if session is None:
        await websocket.close(code=1008)
        return
    await websocket.accept()
    while True:
        try:
            await asyncio.wait_for(session.ended.wait(), timeout=1)  # wake once a second
        except asyncio.TimeoutError:
            pass
        ended = session.ended.is_set()  # read before taking units
        units = session.take()  # units since the previous record
        if units:
            await websocket.send_text(json.dumps({
                "Metering": {
                    "Dimension": "inference.count",
                    "ConsumedUnits": units,
                    "ClientToken": str(uuid.uuid4()),
                }
            }))
        if ended:
            break
    sessions.pop(request_id, None)
    await websocket.close()
```

## Testing your usage reporting
<a name="ml-inference-metering-test"></a>

**To test your usage reporting**

1. Publish your product with Limited visibility. Subscribe from your seller account or an allowlisted account. For more information, see [Machine learning product lifecycle](ml-product-lifecycle.md).

1. Send requests or sessions with a known amount of usage, for example a 12-minute audio file at one inference per minute.

1. Check that the charge matches. The usage appears in your seller reports and on the buyer's AWS bill under the usage type `{{region-code}}-SMMP:inference.count.m.i.c`, for example `USE1-SMMP:inference.count.m.i.c` in US East (N. Virginia). Allow time for reports to update.

1. For bidirectional streams, also test a session that ends early and a session where the metadata connection drops.