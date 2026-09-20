

# Streaming audio
<a name="al-streaming"></a>

Ambient documentation processes audio in real time over a streaming connection. Your application opens a connection, sends audio chunks as event-encoded messages, and receives transcription results as the conversation progresses. Ambient documentation supports two streaming transports: HTTP/2 and WebSocket (`wss://`). Both transports deliver the same capability, with the same authentication and authorization requirements, quotas, and throttling. Session behavior — creation, streaming, and termination — is identical across both transports.


| Transport | Best for | Signing | 
| --- | --- | --- | 
| HTTP/2 | Server-side and native applications using the AWS SDKs | Handled automatically by the SDK | 
| WebSocket (`wss://`) | Web browsers and other clients without SDK support | You sign each frame yourself using SigV4 | 

**Note**  
A session is bound to the transport on which it was started. You cannot start a session on one transport and resume it on the other. If you pause and resume a session, the resumed session must use the same transport that started the session.

If your audio has two channels, you can use channel identification to transcribe the speech from each channel separately. Ambient documentation currently supports audio with up to two channels. In your transcript, channels are assigned the labels `ch_0` and `ch_1`.

In addition to the standard transcript sections (transcripts and items), requests with channel identification enabled include a channel\_labels section. This section contains each utterance or punctuation mark, grouped by channel, and its associated channel label, timestamps, and confidence score. Note that if a person on one channel speaks at the same time as a person on a separate channel, timestamps for each channel overlap while the individuals are speaking over each other.

**Topics**
+ [Streaming over HTTP/2](#al-streaming-http2)
+ [Streaming over WebSocket](#al-streaming-websocket)
+ [Streaming best practices](#al-streaming-best-practices)

## Streaming over HTTP/2
<a name="al-streaming-http2"></a>

HTTP/2 is the streaming transport used by the AWS SDKs, and is suited to server-side and native applications. Your application establishes an HTTP/2 connection, sends audio chunks and control events as event-stream messages, and receives transcript events in real time over the same connection. When you use an AWS SDK, the SDK handles connection setup, request signing, and event-stream encoding for you.

For detailed HTTP/2 streaming setup and event stream encoding, see the [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html).

### Using the AWS SDKs
<a name="al-using-sdks"></a>

When you use an AWS SDK over HTTP/2, integration follows the same overall shape regardless of language:

1. Build a client for the service and open the streaming connection.

1. Publish a single configuration event first, carrying your channel definitions, encounter context, and note template settings.

1. Publish a sequence of audio events, reading your audio source in fixed-size chunks and pacing sends at roughly real time. See [Chunking walkthrough](#al-streaming-chunking-walkthrough) for the chunk size and pacing this requires.

1. Publish a single session control event with type `END_OF_SESSION` when the conversation ends.

1. Handle transcript events on the response stream as they arrive, and close the client when the stream completes.

The SDK handles connection setup, request signing, and event-stream encoding for you — you’re responsible for steps 2 through 4: assembling the event sequence and feeding audio at the right pace.

#### Java 2.x
<a name="al-using-sdks-java"></a>

The following code example shows how to set up an Amazon Connect Health ambient documentation streaming session using the AWS SDK for Java 2.x. It captures audio from a microphone, publishes it as a sequence of configuration, audio, and session control events, and prints transcript segments as they arrive.

```
package com.example.connecthealth;

import io.reactivex.rxjava3.core.BackpressureStrategy;
import io.reactivex.rxjava3.core.Flowable;
import org.reactivestreams.Publisher;
import org.reactivestreams.Subscriber;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.http.nio.netty.NettyNioAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.connecthealth.ConnectHealthAsyncClient;
import software.amazon.awssdk.services.connecthealth.model.*;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.TargetDataLine;
import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UncheckedIOException;
import java.util.Arrays;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;

public class MedicalScribeStreamingApp {
    private static final int CHUNK_SIZE_IN_BYTES = 30720; // <= 32000 (service max); pace sends at ~1 second of audio per cycle
    private static final int SAMPLE_RATE = 16000;
    private static final Region REGION = Region.US_WEST_2;
    private static final String SESSION_ID = UUID.randomUUID().toString();
    private static final String DOMAIN_ID = "your-domain-id";
    private static final String SUBSCRIPTION_ID = "your-subscription-id";
    private static final String OUTPUT_S3_URI = "s3://your-bucket/output/";
    private static ConnectHealthAsyncClient client;

    public static void main(String[] args) {
        client = ConnectHealthAsyncClient.builder()
                .credentialsProvider(getCredentials())
                .httpClientBuilder(NettyNioAsyncHttpClient.builder())
                .region(REGION)
                .build();
        try {
            StartMedicalScribeListeningSessionRequest request =
                    StartMedicalScribeListeningSessionRequest.builder()
                            .sessionId(SESSION_ID)
                            .domainId(DOMAIN_ID)
                            .subscriptionId(SUBSCRIPTION_ID)
                            .languageCode(MedicalScribeLanguageCode.EN_US)
                            .mediaSampleRateHertz(SAMPLE_RATE)
                            .mediaEncoding(MedicalScribeMediaEncoding.PCM)
                            .build();

            MedicalScribeInputStream endSessionEvent =
                    MedicalScribeInputStream.sessionControlEventBuilder()
                            .type(MedicalScribeSessionControlEventType.END_OF_SESSION)
                            .build();

            CompletableFuture<Void> result = client.startMedicalScribeListeningSession(
                    request,
                    new AudioStreamPublisher(
                            getStreamFromMic(),
                            getConfigurationEvent(),
                            endSessionEvent
                    ),
                    getResponseHandler()
            );
            result.get();
            client.close();
        } catch (Exception e) {
            System.err.println("Error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static AudioInputStream getStreamFromMic() throws LineUnavailableException {
        AudioFormat format = new AudioFormat(SAMPLE_RATE, 16, 1, true, false);
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);
        if (!AudioSystem.isLineSupported(info)) {
            throw new LineUnavailableException("Microphone line not supported");
        }
        TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
        line.open(format);
        line.start();
        System.out.println("Recording... Press Enter to stop");
        Thread monitorThread = new Thread(() -> {
            try {
                System.in.read();
                line.stop();
                line.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        monitorThread.setDaemon(true);
        monitorThread.start();
        return new AudioInputStream(
                new BufferedInputStream(new AudioInputStream(line)),
                format,
                AudioSystem.NOT_SPECIFIED
        );
    }

    private static AwsCredentialsProvider getCredentials() {
        return DefaultCredentialsProvider.create();
    }

    private static StartMedicalScribeListeningSessionResponseHandler getResponseHandler() {
        return StartMedicalScribeListeningSessionResponseHandler.builder()
                .onResponse(r -> {
                    System.out.println("Session started: " + r.sessionId());
                    System.out.println("Domain ID: " + r.domainId());
                    System.out.println("Subscription ID: " + r.subscriptionId());
                    System.out.println("Request ID: " + r.requestId());
                })
                .onError(e -> {
                    System.err.println("Stream error: " + e.getMessage());
                    e.printStackTrace();
                })
                .onComplete(() -> {
                    System.out.println("=== Stream completed successfully ===");
                })
                .subscriber(event -> {
                    if (event instanceof MedicalScribeTranscriptEvent) {
                        MedicalScribeTranscriptSegment segment =
                                ((MedicalScribeTranscriptEvent) event).transcriptSegment();
                        if (segment != null && segment.content() != null) {
                            System.out.printf("[%s][Channel %s] %s%n",
                                    segment.isPartial() ? "PARTIAL" : "FINAL",
                                    segment.channelId(),
                                    segment.content()
                            );
                        }
                    }
                })
                .build();
    }

    private static MedicalScribeConfigurationEvent getConfigurationEvent() {
        return MedicalScribeConfigurationEvent.builder()
                .postStreamActionSettings(
                        MedicalScribePostStreamActionSettings.builder()
                                .outputS3Uri(OUTPUT_S3_URI)
                                .clinicalNoteGenerationSettings(
                                        ClinicalNoteGenerationSettings.builder()
                                                .noteTemplateSettings(
                                                        NoteTemplateSettings.fromManagedTemplate(
                                                                ManagedTemplate.builder()
                                                                        .templateType(ManagedNoteTemplate.SOAP)
                                                                        .build()
                                                        )
                                                )
                                                .build()
                                )
                                .build()
                )
                .channelDefinitions(Arrays.asList(
                        MedicalScribeChannelDefinition.builder()
                                .channelId(0)
                                .participantRole(MedicalScribeParticipantRole.CLINICIAN)
                                .build(),
                        MedicalScribeChannelDefinition.builder()
                                .channelId(1)
                                .participantRole(MedicalScribeParticipantRole.PATIENT)
                                .build()
                ))
                .build();
    }

    private static class AudioStreamPublisher implements Publisher<MedicalScribeInputStream> {
        private final InputStream audioInputStream;
        private final MedicalScribeConfigurationEvent configEvent;
        private final MedicalScribeInputStream endSessionEvent;

        private AudioStreamPublisher(
                AudioInputStream audioInputStream,
                MedicalScribeConfigurationEvent configEvent,
                MedicalScribeInputStream endSessionEvent) {
            this.audioInputStream = audioInputStream;
            this.configEvent = configEvent;
            this.endSessionEvent = endSessionEvent;
        }

        @Override
        public void subscribe(Subscriber<? super MedicalScribeInputStream> subscriber) {
            createAudioFlowable()
                    .doOnComplete(() -> {
                        try {
                            audioInputStream.close();
                        } catch (IOException e) {
                            throw new UncheckedIOException(e);
                        }
                    })
                    .subscribe(subscriber);
        }

        private Flowable<MedicalScribeInputStream> createAudioFlowable() {
            Flowable<MedicalScribeInputStream> configFlow = Flowable.just(
                    MedicalScribeInputStream.fromConfigurationEvent(configEvent)
            );
            Flowable<MedicalScribeInputStream> audioFlow = Flowable.create(emitter -> {
                byte[] buffer = new byte[CHUNK_SIZE_IN_BYTES];
                int bytesRead;
                try {
                    while (!emitter.isCancelled() && (bytesRead = audioInputStream.read(buffer)) > 0) {
                        byte[] audioData = bytesRead < buffer.length
                                ? Arrays.copyOfRange(buffer, 0, bytesRead)
                                : buffer;
                        MedicalScribeInputStream audioEvent =
                                MedicalScribeInputStream.fromAudioEvent(
                                        MedicalScribeAudioEvent.builder()
                                                .audioChunk(SdkBytes.fromByteArray(audioData))
                                                .build()
                                );
                        emitter.onNext(audioEvent);
                    }
                    emitter.onComplete();
                } catch (IOException e) {
                    emitter.onError(e);
                }
            }, BackpressureStrategy.BUFFER);
            Flowable<MedicalScribeInputStream> endFlow = Flowable.just(endSessionEvent);
            return Flowable.concat(configFlow, audioFlow, endFlow);
        }
    }
}
```

## Streaming over WebSocket
<a name="al-streaming-websocket"></a>

WebSocket support lets you stream audio for ambient documentation from a web browser or other WebSocket client. All WebSocket connections use TLS (`wss://`).

### WebSocket endpoint
<a name="al-websocket-endpoint"></a>

Connect to the WebSocket endpoint for the Region where you use ambient documentation:


| Region | Endpoint | 
| --- | --- | 
| US-EAST-1 |  `wss://streaming.health-agent.us-east-1.api.aws/medical-scribe-stream-websocket`  | 
| US-WEST-2 |  `wss://streaming.health-agent.us-west-2.api.aws/medical-scribe-stream-websocket`  | 

### Authenticating a WebSocket connection
<a name="al-websocket-auth"></a>

You authenticate a WebSocket connection with a presigned URL. To create the presigned URL, sign a `GET` request to the WebSocket endpoint with AWS Signature Version 4 (SigV4) and embed the signing parameters (`X-Amz-Algorithm`, `X-Amz-Credential`, `X-Amz-Date`, `X-Amz-Expires`, `X-Amz-Signature`, and `X-Amz-SignedHeaders`) and the session parameters as query string parameters. The service validates the presigned URL when the connection is established. If the presigned URL is invalid, expired, or unauthorized, the service rejects the session by returning an error and closing the connection.

The maximum value for `X-Amz-Expires` is 60 seconds (1 minute). After the connection is established, the signature from the presigned URL becomes the seed signature used to sign each subsequent event-stream frame, providing continuous authorization for the life of the connection.

No new IAM action is required for WebSocket. The service authorizes WebSocket connections with the same `health-agent:StartMedicalScribeListeningSession` permission used for HTTP/2 streaming.

The following example shows the format of a presigned WebSocket URL. Line breaks are added for readability.

```
wss://streaming.health-agent.us-west-2.api.aws/medical-scribe-stream-websocket
    ?X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=<access-key>/<date>/<region>/health-agent/aws4_request
    &X-Amz-Date=<ISO8601-datetime>
    &X-Amz-Expires=60
    &X-Amz-Security-Token=<session-token>
    &X-Amz-SignedHeaders=host
    &X-Amz-Signature=<signature>
```

### Signing event-stream frames
<a name="al-websocket-signing"></a>

Every event-stream frame you send after the upgrade — configuration, audio, and session control — must be individually signed. Each frame carries two event-stream headers: `:date` (the signing timestamp) and `:chunk-signature` (the frame signature). Frame signatures form a chain: each signature is computed from the previous frame’s signature, and the first frame chains from the `X-Amz-Signature` value in the presigned URL.

To sign a frame, build a string to sign using the `AWS4-HMAC-SHA256-PAYLOAD` algorithm, then compute an HMAC-SHA256 over it with a SigV4 signing key derived for the request date, Region, and `health-agent` service. The string to sign has the following format:

```
AWS4-HMAC-SHA256-PAYLOAD
<date>                       # signing time, ISO 8601 basic format (YYYYMMDDTHHMMSSZ)
<date-stamp>/<region>/health-agent/aws4_request
<prior-signature>            # hex; for the first frame, the X-Amz-Signature from the presigned URL
<hashed-headers>             # SHA-256 hex digest of the encoded :date header
<hashed-payload>             # SHA-256 hex digest of the frame payload
```

Compute the signature and attach it to the frame:

1.  `signature = HMAC-SHA256(signingKey, stringToSign)`, encoded as a hex string.

1. Add the `:date` and `:chunk-signature` headers to the frame, then send it.

1. Store this `signature` and use it as the `<prior-signature>` when signing the next frame.

The signing key is derived the same way as for any SigV4 request: chain HMAC-SHA256 over the date stamp, Region, service name (`health-agent`), and `aws4_request`, starting from your secret access key prefixed with `AWS4`.

### Sending audio over WebSocket
<a name="al-websocket-streaming"></a>

After the connection is established, send your session configuration, then stream audio as binary audio events. Each `binaryAudioEvent` carries a chunk of raw PCM or FLAC bytes. The service returns transcript events over the same connection in real time. To end the session, send an `END_OF_SESSION` session control event.

### WebSocket client recommendations
<a name="al-websocket-client-behavior"></a>

The service signals the end of a session by sending a WebSocket close frame. Design your client to handle connection closure gracefully:
+  **Wait for the server close frame before closing the connection.** After you send `END_OF_SESSION`, the service sends any final transcript results and then a close frame. If a send fails or an error occurs, the service may send a structured error frame followed by a close frame. Closing the connection immediately can discard these final messages, so wait for the server to close the connection.
+  **Use the close status code to determine the outcome.** A close code of `1000` (Normal Closure) indicates the session completed successfully. Any other close code indicates an error, and the close reason provides additional detail.
+  **Apply a bounded timeout as a safeguard.** To avoid waiting indefinitely if the connection becomes unresponsive, close the connection after a reasonable grace period if no server close frame is received.

The AWS SDKs do not support WebSocket streaming. To stream over WebSocket, connect to the endpoint directly as described in this section. The [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html) documents the API operations and their request and response parameters, which apply to both transports.

## Streaming best practices
<a name="al-streaming-best-practices"></a>

How you deliver audio has a direct effect on whether a session stays healthy. The single most important practice is to deliver audio in small chunks, at close to real time — never buffer several seconds of audio and send it in one large burst. Following the guidance in this section prevents stalled streams and `InvalidSignatureException` errors that terminate a session under load.

### Recommendations at a glance
<a name="al-streaming-recommendations"></a>

If you read nothing else in this section, follow these five rules:
+  **Send \~1 second of audio (or less) per message** — never buffer many seconds and send one large burst.
+  **Keep each audio chunk ≤ 30,720 bytes** (the service hard maximum is 32,000 bytes).
+  **Keep each send cycle well under the \~1 MB flow-control window** (\~90–120 KB at 48 kHz mono).
+  **Pace sends at \~500–1000 ms** (700 ms works well) so audio goes out at roughly real time.
+  **Don’t sign audio far ahead of delivery** — stale signatures are the main cause of dropped streams.

### Why delivery rate matters
<a name="al-streaming-why-rate-matters"></a>

Every audio event you send is individually signed with AWS Signature Version 4 (SigV4). The signature is stamped with the time the frame was signed (when you enqueue it) and is accepted only within a fixed validity window from that time — sitting in a buffer does not re-sign or refresh it. If you sign a large batch of audio in advance and the service can’t read it quickly enough, the oldest frames wait in the connection’s send buffer. The service validates each frame’s signature only when it finally reads that frame; if a frame is read after its signature’s validity window has passed, the signature is now too old, so the service rejects it as invalid and ends the stream — even though the signature was correct when it was created. Two limits combine to cause this:
+  **SigV4 signature validity — 5 minutes.** When the service finally reads a message whose signature is older than 5 minutes, it raises `InvalidSignatureException` and terminates the stream.
+  **HTTP/2 flow-control window — approximately 1 MB (1,048,576 bytes).** If you push a burst larger than the window can drain, messages queue in the buffer. Under sustained back-pressure the backlog grows, and messages sit long enough for their signatures to expire.

For example, suppose you buffer 10 seconds of 48 kHz, 16-bit, mono PCM and send it in one burst. That is about 960 KB of audio, all signed within the same instant, which nearly saturates the \~1 MB flow-control window in a single shot. Each 7-second cycle adds another 960 KB before the previous burst has fully drained, so the backlog grows. Eventually the oldest queued frame is read more than 5 minutes after it was signed, and the whole stream is rejected with `InvalidSignatureException` — even though the connection never actually stalled.

### Chunking walkthrough
<a name="al-streaming-chunking-walkthrough"></a>

Whatever language or transport you use, the pattern is the same:

1. Capture or read audio into a buffer at real time.

1. Split the buffer into chunks no larger than 30,720 bytes.

1. Wrap each chunk in an audio event and send it.

1. Pace your sends so that you emit roughly 1 second of audio per cycle (about every 500–1000 ms), rather than emitting everything at once.

1. When the visit ends, send a session control event with type `END_OF_SESSION`.

Language-agnostic pseudocode:

```
CHUNK_SIZE = 30720          # bytes; <= service max of 32000
SEND_INTERVAL_MS = 700      # pace sends at roughly real time

loop while capturing:
    buffer = read_available_audio()      # ~1 second of PCM or less
    for offset in range(0, len(buffer), CHUNK_SIZE):
        chunk = buffer[offset : offset + CHUNK_SIZE]
        send_audio_event(chunk)          # one event per chunk
    sleep(SEND_INTERVAL_MS)

send_session_control_event(END_OF_SESSION)
```

The AWS SDKs stream over HTTP/2 and handle SigV4 signing for you; your responsibility is to feed audio in appropriately sized chunks at a real-time pace. For example, with the AWS SDK for Java 2.x you read the source in `CHUNK_SIZE_IN_BYTES` buffers and publish each buffer as a `MedicalScribeAudioEvent`:

```
static final int CHUNK_SIZE_IN_BYTES = 30720; // <= 32000 (service max)

byte[] audioBytes = new byte[CHUNK_SIZE_IN_BYTES];
int len;
while ((len = audioStream.read(audioBytes)) != -1) {
    byte[] chunk = (len == audioBytes.length) ? audioBytes : Arrays.copyOf(audioBytes, len);
    MedicalScribeAudioEvent event = MedicalScribeAudioEvent.builder()
            .audioChunk(SdkBytes.fromByteArray(chunk))
            .build();
    subscriber.onNext(MedicalScribeInputStream.fromAudioEvent(event));
    // pace so that ~1 second of audio is emitted per cycle
}
```

**Note**  
If you use the AWS SDK for JavaScript (`@aws-sdk/client-connecthealth`), Node.js version 20 or later is required.

### Audio data-rate reference
<a name="al-streaming-data-rate"></a>

Use these rates to size your chunks and send intervals. Data rate = sample rate × 2 bytes per sample × number of channels.


| Sample rate | Channels | Data rate | \~1 second of audio | 
| --- | --- | --- | --- | 
| 16,000 Hz | Mono | 32,000 bytes/sec | \~32 KB (2 chunks) | 
| 16,000 Hz | Stereo | 64,000 bytes/sec | \~64 KB (3 chunks) | 
| 48,000 Hz | Mono | 96,000 bytes/sec | \~96 KB (3–4 chunks) | 
| 48,000 Hz | Stereo | 192,000 bytes/sec | \~192 KB (7 chunks) | 

At 48 kHz mono (96,000 bytes/sec), one second of audio is about 96 KB, which splits into three to four chunks of 30,720 bytes — a small, safe per-cycle burst.