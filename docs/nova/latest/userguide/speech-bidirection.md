# Using the Bidirectional Streaming API

###### Note

This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Sonic guide, visit [Getting started](../nova2-userguide/sonic-getting-started.md "../nova2-userguide/sonic-getting-started.md").

The Amazon Nova Sonic model uses the `InvokeModelWithBidirectionalStream` API, which enables real-time bidirectional streaming conversations. This differs from traditional request-response patterns by maintaining an open channel for continuous audio streaming in both directions.

The following AWS SDKs support the new bidirectional streaming API:

- [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/")
- [AWS SDK for C++](https://aws.amazon.com/sdk-for-cpp/ "https://aws.amazon.com/sdk-for-cpp/")
- [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")
- [AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/")
- [AWS SDK for Kotlin](https://aws.amazon.com/sdk-for-kotlin/ "https://aws.amazon.com/sdk-for-kotlin/")
- [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/")
- [AWS SDK for Rust](https://aws.amazon.com/sdk-for-rust/ "https://aws.amazon.com/sdk-for-rust/")
- [AWS SDK for Swift](https://aws.amazon.com/sdk-for-swift/ "https://aws.amazon.com/sdk-for-swift/")
  Python developers can use this [new experimental SDK](https://github.com/awslabs/aws-sdk-python "https://github.com/awslabs/aws-sdk-python") that makes it easier to use the bidirectional streaming capabilities of Amazon Nova Sonic.

The following code examples will help you get started with the bidirectional API. For a complete list of examples, see the Amazon Nova Sonic [Github Samples](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech") page.

The following examples can be used to set up the client and begin using the bidirectional API.

Python

```
def _initialize_client(self):
    """Initialize the Bedrock client."""
    config = Config(
        endpoint_uri=f"https://bedrock-runtime.{self.region}.amazonaws.com",
        region=self.region,
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
        http_auth_scheme_resolver=HTTPAuthSchemeResolver(),
        http_auth_schemes={"aws.auth#sigv4": SigV4AuthScheme()}
    )
    self.bedrock_client = BedrockRuntimeClient(config=config)
```

Java

```
// The nettyBuilder is optional and mentioned here for clarity, all our APIs support http2
// and will default to the protocol if the netty builder is not specified.
NettyNioAsyncHttpClient.Builder nettyBuilder = NettyNioAsyncHttpClient.builder()
        .readTimeout(Duration.of(180, ChronoUnit.SECONDS))
        .maxConcurrency(20)
        .protocol(Protocol.HTTP2)
        .protocolNegotiation(ProtocolNegotiation.ALPN);


BedrockRuntimeAsyncClient client = BedrockRuntimeAsyncClient.builder()
        .region(Region.US_EAST_1)
        .credentialsProvider(ProfileCredentialsProvider.create("`NOVA-PROFILE`"))
        .httpClientBuilder(nettyBuilder)
        .build();
```

Node.js

```
const { BedrockRuntimeClient } = require("@aws-sdk/client-bedrock-runtime");
const { NodeHttp2Handler } = require("@smithy/node-http-handler");
const { fromIni } = require("@aws-sdk/credential-provider-ini");

// Configure HTTP/2 client for bidirectional streaming
// (This is optional, all our APIs support http2 so we will default to http2 if handler is not specified)
const nodeHttp2Handler = new NodeHttp2Handler({
    requestTimeout: 300000,
    sessionTimeout: 300000,
    disableConcurrentStreams: false,
    maxConcurrentStreams: 20,
});

// Create a Bedrock client
const client = new BedrockRuntimeClient({
    region: "us-east-1",
    credentials: fromIni({ profile: "`NOVA-PROFILE`" }), // Or use other credential providers
    requestHandler: nodeHttp2Handler,
});
```

The following examples can be used to handle events with the bidirectional API.

Python

```
self.stream_response = await self.bedrock_client.invoke_model_with_bidirectional_stream(
                InvokeModelWithBidirectionalStreamInput(model_id=self.model_id)
            )
self.is_active = True
```

```
async def _process_responses(self):
        """Process incoming responses from Bedrock."""
        try:
            while self.is_active:
                try:
                    output = await self.stream_response.await_output()
                    result = await output[1].receive()
                    if result.value and result.value.bytes_:
                        try:
                            response_data = result.value.bytes_.decode('utf-8')
                            json_data = json.loads(response_data)

                            # Handle different response types
                            if 'event' in json_data:
                                if 'contentStart' in json_data['event']:
                                    content_start = json_data['event']['contentStart']
                                    # set role
                                    self.role = content_start['role']
                                    # Check for speculative content
                                    if 'additionalModelFields' in content_start:
                                        try:
                                            additional_fields = json.loads(content_start['additionalModelFields'])
                                            if additional_fields.get('generationStage') == 'SPECULATIVE':
                                                self.display_assistant_text = True
                                            else:
                                                self.display_assistant_text = False
                                        except json.JSONDecodeError:
                                            print("Error parsing additionalModelFields")
                                elif 'textOutput' in json_data['event']:
                                    text_content = json_data['event']['textOutput']['content']
                                    role = json_data['event']['textOutput']['role']
                                    # Check if there is a barge-in
                                    if '{ "interrupted" : true }' in text_content:
                                        self.barge_in = True

                                    if (self.role == "ASSISTANT" and self.display_assistant_text):
                                        print(f"Assistant: {text_content}")
                                    elif (self.role == "USER"):
                                        print(f"User: {text_content}")

                                elif 'audioOutput' in json_data['event']:
                                    audio_content = json_data['event']['audioOutput']['content']
                                    audio_bytes = base64.b64decode(audio_content)
                                    await self.audio_output_queue.put(audio_bytes)
                                elif 'toolUse' in json_data['event']:
                                    self.toolUseContent = json_data['event']['toolUse']
                                    self.toolName = json_data['event']['toolUse']['toolName']
                                    self.toolUseId = json_data['event']['toolUse']['toolUseId']
                                elif 'contentEnd' in json_data['event'] and json_data['event'].get('contentEnd', {}).get('type') == 'TOOL':
                                    toolResult = await self.processToolUse(self.toolName, self.toolUseContent)
                                    toolContent = str(uuid.uuid4())
                                    await self.send_tool_start_event(toolContent)
                                    await self.send_tool_result_event(toolContent, toolResult)
                                    await self.send_tool_content_end_event(toolContent)
                                elif 'completionEnd' in json_data['event']:
                                    # Handle end of conversation, no more response will be generated
                                    print("End of response sequence")


                            # Put the response in the output queue for other components
                            await self.output_queue.put(json_data)
                        except json.JSONDecodeError:
                            await self.output_queue.put({"raw_data": response_data})
                except StopAsyncIteration:
                    # Stream has ended
                    break
                except Exception as e:
                   # Handle ValidationException properly
                    if "ValidationException" in str(e):
                        error_message = str(e)
                        print(f"Validation error: {error_message}")
                    else:
                        print(f"Error receiving response: {e}")
                    break

        except Exception as e:
            print(f"Response processing error: {e}")
        finally:
            self.is_active = False
```

Java

```
public class ResponseHandler implements InvokeModelWithBidirectionalStreamResponseHandler {
    @Override
    public void responseReceived(InvokeModelWithBidirectionalStreamResponse response) {
        // Handle initial response
        log.info("Bedrock Nova Sonic request id: {}", response.responseMetadata().requestId());
    }

    @Override
    public void onEventStream(SdkPublisher<InvokeModelWithBidirectionalStreamOutput> sdkPublisher) {
        log.info("Bedrock Nova S2S event stream received");
        var completableFuture = sdkPublisher.subscribe((output) -> output.accept(new Visitor() {
            @Override
            public void visitChunk(BidirectionalOutputPayloadPart event) {
                log.info("Bedrock S2S chunk received, converting to payload");
                String payloadString =
                        StandardCharsets.UTF_8.decode((event.bytes().asByteBuffer().rewind().duplicate())).toString();
                log.info("Bedrock S2S payload: {}", payloadString);
                    delegate.onNext(payloadString);
            }
        }));

        // if any of the chunks fail to parse or be handled ensure to send an error or they will get lost
        completableFuture.exceptionally(t -> {
            delegate.onError(new Exception(t));
            return null;
        });
    }

    @Override
    public void exceptionOccurred(Throwable throwable) {
        // Handle errors
        System.err.println("Error: " + throwable.getMessage());
        throwable.printStackTrace();
    }

    @Override
    public void complete() {
        // Handle completion
        System.out.println("Stream completed");
    }
}
```

Node.js

```
for await (const event of response.body) {
        if (!session.isActive) {
          console.log(`Session ${sessionId} is no longer active, stopping response processing`);
          break;
        }
        if (event.chunk?.bytes) {
          try {
            this.updateSessionActivity(sessionId);
            const textResponse = new TextDecoder().decode(event.chunk.bytes);

            try {
              const jsonResponse = JSON.parse(textResponse);
              if (jsonResponse.event?.contentStart) {
                this.dispatchEvent(sessionId, 'contentStart', jsonResponse.event.contentStart);
              } else if (jsonResponse.event?.textOutput) {
                this.dispatchEvent(sessionId, 'textOutput', jsonResponse.event.textOutput);
              } else if (jsonResponse.event?.audioOutput) {
                this.dispatchEvent(sessionId, 'audioOutput', jsonResponse.event.audioOutput);
              } else if (jsonResponse.event?.toolUse) {
                this.dispatchEvent(sessionId, 'toolUse', jsonResponse.event.toolUse);

                // Store tool use information for later
                session.toolUseContent = jsonResponse.event.toolUse;
                session.toolUseId = jsonResponse.event.toolUse.toolUseId;
                session.toolName = jsonResponse.event.toolUse.toolName;
              } else if (jsonResponse.event?.contentEnd &&
                jsonResponse.event?.contentEnd?.type === 'TOOL') {

                // Process tool use
                console.log(`Processing tool use for session ${sessionId}`);
                this.dispatchEvent(sessionId, 'toolEnd', {
                  toolUseContent: session.toolUseContent,
                  toolUseId: session.toolUseId,
                  toolName: session.toolName
                });

                console.log("calling tooluse");
                console.log("tool use content : ", session.toolUseContent)
                // function calling
                const toolResult = await this.processToolUse(session.toolName, session.toolUseContent);

                // Send tool result
                this.sendToolResult(sessionId, session.toolUseId, toolResult);

                // Also dispatch event about tool result
                this.dispatchEvent(sessionId, 'toolResult', {
                  toolUseId: session.toolUseId,
                  result: toolResult
                });
              } else {
                // Handle other events
                const eventKeys = Object.keys(jsonResponse.event || {});
                console.log(`Event keys for session ${sessionId}: `, eventKeys)
                console.log(`Handling other events`)
                if (eventKeys.length > 0) {
                  this.dispatchEvent(sessionId, eventKeys[0], jsonResponse.event);
                } else if (Object.keys(jsonResponse).length > 0) {
                  this.dispatchEvent(sessionId, 'unknown', jsonResponse);
                }
              }
            } catch (e) {
              console.log(`Raw text response for session ${sessionId}(parse error): `, textResponse);
            }
          } catch (e) {
            console.error(`Error processing response chunk for session ${sessionId}: `, e);
          }
        } else if (event.modelStreamErrorException) {
          console.error(`Model stream error for session ${sessionId}: `, event.modelStreamErrorException);
          this.dispatchEvent(sessionId, 'error', {
            type: 'modelStreamErrorException',
            details: event.modelStreamErrorException
          });
        } else if (event.internalServerException) {
          console.error(`Internal server error for session ${sessionId}: `, event.internalServerException);
          this.dispatchEvent(sessionId, 'error', {
            type: 'internalServerException',
            details: event.internalServerException
          });
        }
      }
```

The following examples can be used to create a request with the bidirectional API.

Python

```
self.stream_response = await self.bedrock_client.invoke_model_with_bidirectional_stream(
                InvokeModelWithBidirectionalStreamInput(model_id="amazon.nova-sonic-v1:0")
            )
```

Java

```
InvokeModelWithBidirectionalStreamRequest request =
   InvokeModelWithBidirectionalStreamRequest.builder()
   .modelId("amazon.nova-sonic-v1:0")
   .build();
```

Node.js

```
const request = new InvokeModelWithBidirectionalStreamCommand({
            modelId: "amazon.nova-sonic-v1:0",
            body: generateOrderedStream(), //initial request
        });
```

The following examples can be used to initiate a request with the bidirectional API.

Python

```
    START_SESSION_EVENT = '''{
        "event": {
            "sessionStart": {
            "inferenceConfiguration": {
                "maxTokens": 1024,
                "topP": 0.9,
                "temperature": 0.7
                }
            }
        }
    }'''

    event = InvokeModelWithBidirectionalStreamInputChunk(
            value=BidirectionalInputPayloadPart(bytes_=START_SESSION_EVENT.encode('utf-8'))
    )
    try:
        await self.stream_response.input_stream.send(event)
    except Exception as e:
        print(f"Error sending event: {str(e)}")
```

Java

```
// Create ReplayProcessor with time-based expiry (cleans up messages after 1 minute)
ReplayProcessor<InvokeModelWithBidirectionalStreamInput> publisher = ReplayProcessor.createWithTime(
                1, TimeUnit.MINUTES, Schedulers.io()
);

// Create response handler
ResponseHandler responseHandler = new ResponseHandler();

// Initiate bidirectional stream
CompletableFuture<Void> completableFuture = client.invokeModelWithBidirectionalStream(
    request, publisher, responseHandler);

// Handle completion and errors properly
completableFuture.exceptionally(throwable -> {
    publisher.onError(throwable);
    return null;
});

completableFuture.thenApply(result -> {
    publisher.onComplete();
    return result;
});

// Send session start event
String sessionStartJson = """
{
  "event": {
    "sessionStart": {
      "inferenceConfiguration": {
        "maxTokens": 1024,
        "topP": 0.9,
        "temperature": 0.7
      }
    }
  }
}""";

publisher.onNext(
    InvokeModelWithBidirectionalStreamInput.chunkBuilder()
        .bytes(SdkBytes.fromUtf8String(sessionStartJson))
        .build()
);
```

Node.js

```
const command = new InvokeModelWithBidirectionalStreamCommand({
        modelId: "amazon.nova-sonic-v1:0",
        body: generateChunks(),
    });
async function* generateChunks() {
        // Send initialization events
        for (const event of initEvents) {
            const eventJson = JSON.stringify(event);
            console.log(`Sending event: ${eventJson.substring(0, 50)}...`);
            yield {
                chunk: {
                    bytes: textEncoder.encode(eventJson),
                },
            };
            await new Promise(resolve => setTimeout(resolve, 30));
        }
}
const initEvents = [
        {
            event: {
                sessionStart: {
                    inferenceConfiguration: {
                        maxTokens: 1024,
                        topP: 0.9,
                        temperature: 0.7
                    }
                }
            }
        },
        {
        ...
        }
];
```
