

# Ambient documentation
<a name="ambient-documentation"></a>

Ambient documentation captures patient-clinician conversations in real time and generates structured clinical documentation for provider review. The service combines speech recognition with generative AI to produce clinical notes, extract medical terminology, identify speaker roles, and classify dialogue segments.

**Important**  
Amazon Connect Health ambient documentation produces probabilistic results. Output accuracy varies based on audio quality, background noise, speaker clarity, medical terminology complexity, and context-specific language. All output must be reviewed for accuracy by a trained medical professional before use in patient care.

Amazon Connect Health ambient documentation is available in the US East (N. Virginia) (`us-east-1`) and US West (Oregon) (`us-west-2`) Regions.

**Topics**
+ [How ambient documentation works](#al-how-it-works)
+ [Technical requirements](#al-technical-requirements)
+ [Supported medical specialties](#al-supported-specialties)
+ [Consent and patient notification](#al-consent)
+ [Subscription management](#al-subscription-management)
+ [Streaming audio](#al-streaming)
+ [Storage](#al-storage)
+ [Patient context](#al-patient-context)
+ [Clinical note templates](#al-templates)
+ [Outputs](#al-outputs)

## How ambient documentation works
<a name="al-how-it-works"></a>

Ambient documentation uses real-time audio streaming over HTTP/2 or WebSocket. The workflow includes:

1.  **Create a subscription** — Associate a provider with the ambient documentation agent. Subscriptions are automatically created in activated mode.

1.  **Stream audio** — Your application streams audio from the patient-clinician conversation to Amazon Connect Health over HTTP/2 or WebSocket. The service transcribes the audio in real time and identifies speakers.

1.  **Generate documentation** — After the conversation ends, the service generates structured clinical notes, evidence mappings, and an after-visit summary based on the configured template.

1.  **Retrieve outputs** — The service writes the transcript, clinical documentation, and after-visit summary to your configured Amazon S3 bucket.

## Technical requirements
<a name="al-technical-requirements"></a>
+  **Supported language** — US English (en-US)
+  **Supported audio formats** — FLAC, PCM
+  **Encoding** — PCM 16-bit
+  **Sample rate** — 16,000 Hz or higher

## Supported medical specialties
<a name="al-supported-specialties"></a>

Ambient documentation currently supports the following specialties:
+ Allergy Immunology
+ Cardiology
+ Dermatology
+ Endocrinology
+ Gastroenterology
+ Hematology/Oncology
+ Infectious Disease
+ Nephrology
+ Neurology
+ OBGYN
+ Oncology
+ Ophthalmology
+ Orthopedics
+ Otolaryngology
+ Pain Medicine
+ Pediatrics
+ Primary Care
+ Psychiatry
+ Pulmonology
+ Rheumatology
+ Surgery
+ Urology

## Consent and patient notification
<a name="al-consent"></a>

Amazon Connect Health ambient documentation uses AI to capture and transcribe clinical conversations in real time. Because this feature records spoken communications that may contain protected health information (PHI), customers and their downstream integrators are responsible for complying with all applicable consent, recording, and privacy laws. This includes obtaining all legally required consents before enabling ambient documentation for any patient encounter. AWS does not collect consent from patients on your behalf.

Appropriate consent must be obtained from each patient and anyone present in the room when ambient documentation is used. As part of obtaining consent, patients should be informed that the visit will be recorded and used by an AI service provider to create clinical notes, that their information may be shared with service providers, and that they can decline without any impact on their care. Customers and integrators should maintain records of patient consent, in accordance with applicable state law and internal retention policies. Customers should ensure that consent is obtained in accordance with their organization’s privacy practices.

Sample language:

"Before we begin, I want to let you know that today’s visit will be recorded and monitored by an AI service provider to help with documentation. Do you consent to proceed?"

## Subscription management
<a name="al-subscription-management"></a>

### Create a subscription
<a name="al-create-subscription"></a>

To create a subscription, call the `CreateSubscription` API operation. This generates a unique `subscriptionId` that you use to authorize the user and start streaming sessions. Subscriptions are automatically created in activated mode.

**Tip**  
Create the subscription on the user’s first use to align subscription start with actual usage.

### Deactivate a subscription
<a name="al-deactivate-subscription"></a>

To temporarily stop a subscription from accepting new streaming sessions, call the `DeactivateSubscription` API operation. A deactivated subscription retains its configuration and can be reactivated later. In-progress streams complete normally.

**Important**  
Deactivating a subscription immediately forfeits any remaining free trial period. If a subscription that was deactivated during a free trial is reactivated later, it is reactivated as a paid subscription.

### Reactivate a subscription
<a name="al-reactivate-subscription"></a>

Deactivated subscriptions can be reactivated by calling the `ActivateSubscription` API operation with the `subscriptionId`. Paid metering begins immediately upon reactivation.

## Streaming audio
<a name="al-streaming"></a>

Ambient documentation processes audio in real time over a streaming connection. Your application opens a connection, sends audio chunks as event-encoded messages, and receives transcription results as the conversation progresses. Ambient documentation supports two streaming transports: HTTP/2 and WebSocket (`wss://`). Both transports deliver the same capability, with the same authentication and authorization requirements, quotas, and throttling. Session behavior — creation, streaming, and termination — is identical across both transports.

**Note**  
A session is bound to the transport on which it was started. You cannot start a session on one transport and resume it on the other. If you pause and resume a session, the resumed session must use the same transport that started the session.

If your audio has two channels, you can use channel identification to transcribe the speech from each channel separately. Ambient documentation currently supports audio with up to two channels. In your transcript, channels are assigned the labels `ch_0` and `ch_1`.

In addition to the standard transcript sections (transcripts and items), requests with channel identification enabled include a channel\_labels section. This section contains each utterance or punctuation mark, grouped by channel, and its associated channel label, timestamps, and confidence score. Note that if a person on one channel speaks at the same time as a person on a separate channel, timestamps for each channel overlap while the individuals are speaking over each other.

### Streaming over HTTP/2
<a name="al-streaming-http2"></a>

HTTP/2 is the streaming transport used by the AWS SDKs, and is suited to server-side and native applications. Your application establishes an HTTP/2 connection, sends audio chunks and control events as event-stream messages, and receives transcript events in real time over the same connection. When you use an AWS SDK, the SDK handles connection setup, request signing, and event-stream encoding for you.

For detailed HTTP/2 streaming setup and event stream encoding, see the [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html).

#### Using the AWS SDKs
<a name="al-using-sdks"></a>

The following code example shows how to set up an Amazon Connect Health ambient documentation streaming session using the AWS SDK for Java 2.x.

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
    private static final int CHUNK_SIZE_IN_BYTES = 6400;
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

### Streaming over WebSocket
<a name="al-streaming-websocket"></a>

WebSocket support lets you stream audio for ambient documentation from a web browser or other WebSocket client. All WebSocket connections use TLS (`wss://`).

#### WebSocket endpoint
<a name="al-websocket-endpoint"></a>

Connect to the WebSocket endpoint for the Region where you use ambient documentation:


| Region | Endpoint | 
| --- | --- | 
| US-EAST-1 |  `wss://streaming.health-agent.us-east-1.api.aws/medical-scribe-stream-websocket`  | 
| US-WEST-2 |  `wss://streaming.health-agent.us-west-2.api.aws/medical-scribe-stream-websocket`  | 

#### Authenticating a WebSocket connection
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

#### Signing event-stream frames
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

#### Sending audio over WebSocket
<a name="al-websocket-streaming"></a>

After the connection is established, send your session configuration, then stream audio as binary audio events. Each `binaryAudioEvent` carries a chunk of raw PCM or FLAC bytes. The service returns transcript events over the same connection in real time. To end the session, send an `END_OF_SESSION` session control event.

#### WebSocket client recommendations
<a name="al-websocket-client-behavior"></a>

The service signals the end of a session by sending a WebSocket close frame. Design your client to handle connection closure gracefully:
+  **Wait for the server close frame before closing the connection.** After you send `END_OF_SESSION`, the service sends any final transcript results and then a close frame. If a send fails or an error occurs, the service may send a structured error frame followed by a close frame. Closing the connection immediately can discard these final messages, so wait for the server to close the connection.
+  **Use the close status code to determine the outcome.** A close code of `1000` (Normal Closure) indicates the session completed successfully. Any other close code indicates an error, and the close reason provides additional detail.
+  **Apply a bounded timeout as a safeguard.** To avoid waiting indefinitely if the connection becomes unresponsive, close the connection after a reasonable grace period if no server close frame is received.

The AWS SDKs do not support WebSocket streaming. To stream over WebSocket, connect to the endpoint directly as described in this section. The [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html) documents the API operations and their request and response parameters, which apply to both transports.

## Storage
<a name="al-storage"></a>

An S3 storage location must be specified at the start of a session. Output artifacts are stored at the following base location:

 `s3://{customer-provided-uri}/health-agent-listening-session/{domainId}/{subscriptionId}/{sessionId}/post-stream-action/` 

Clinical notes are stored in a `clinical-notes` folder at this base location.

## Patient context
<a name="al-patient-context"></a>

Patient context provides the agent with clinical history before the conversation through the `encounterContext` API parameter. The `encounterContext` object contains the field `unstructuredContext`, which accepts up to 10 KB of text data for each session. When you include patient context, the agent uses it to enrich the generated documentation with background information that was not explicitly discussed during the visit.

Patient context can include:
+ Prior encounter notes and visit summaries
+ Active medication lists
+ Problem lists and diagnoses
+ Allergies and immunizations
+ Relevant lab and imaging reports
+ Surgical and family history
+ Patient’s preferred pronouns, used when referring to the patient in generated clinical output

The context is used throughout the generated note to improve specificity and accuracy when the necessary information is not present in the transcript alone, with evidence mapping to source materials for clinician review.

**Note**  
The following example uses fictional patient data for illustration purposes only.

 **Example patient context** 

```
## Patient Information
Name: Patricia Underwood
Age: 28 years
Sex: female
Pronouns: she/her
MEDICATIONS:
Ondansetron 4mg PO PRN - Nausea/vomiting
Dicyclomine 20mg PO BID PRN - Abdominal cramping
Sertraline 50mg PO daily - Depression
Ferrous sulfate 325mg PO TID - Iron deficiency anemia
ALLERGIES: NKDA (No Known Drug Allergies)
PAST MEDICAL HISTORY:
Brainstem pilocytic astrocytoma diagnosed 04/2010
Posterior fossa craniotomy with gross total resection 05/12/2010
Hyperprolactinemia diagnosed 08/2013
Autoimmune hemolytic anemia diagnosed 12/2012
Splenomegaly secondary to autoimmune hemolytic anemia 01/2013
Major depressive disorder diagnosed 08/2012
Substance use disorder (heroin) in sustained remission since 04/2011
Tobacco use disorder, quit 09/15/2013 (10 pack-year history)
Iron deficiency anemia diagnosed 01/2013
Gastroesophageal reflux disease diagnosed 05/2013
Appendectomy 07/23/2009 (uncomplicated laparoscopic)
Wisdom teeth extraction 11/08/2008
FAMILY HISTORY:
Maternal grandmother: Cervical cancer, ovarian cancer, dementia/Alzheimer's
Maternal aunt: Cervical cancer
Paternal grandfather: Type 2 diabetes, hypertension, kidney transplant
Maternal great-grandfather: Colon cancer
Multiple maternal great-uncles: Colon cancer
No family history of breast, uterine, or cardiac disease
SOCIAL HISTORY:
Tobacco: Former smoker, quit 09/15/2013 (10 pack-year history)
Alcohol: Not documented
Illicit drugs: History of IV heroin use, abstinent since 04/2011, occasional marijuana use
Sexual history: Single, sexually active, monogamous relationship since 05/2012
Previous relationship with military personnel ended 03/2012
Employment: Lives independently, employed
Contraception: Not currently using
Former plasma donor, discontinued 10/2013 due to positive syphilis screening
PROBLEM LIST:
History of brainstem pilocytic astrocytoma (C71.7) - Diagnosed 04/2010 with posterior fossa craniotomy and gross total resection 05/12/2010. Annual MRI surveillance shows post-surgical changes, no residual tumor. Most recent MRI 10/18/2013 normal. Followed by neurology with annual visits.
Hyperprolactinemia (E22.1) - Diagnosed 08/2013 with prolactin 45.2 ng/mL (normal <25). Referred to neurology for pituitary evaluation. Recent MRI 10/18/2013 shows normal pituitary gland. Not currently on treatment. Neurology follow-up scheduled.
Autoimmune hemolytic anemia with splenomegaly (D59.1) - Diagnosed 12/2012-01/2013. Positive direct Coombs test, elevated LDH 420 U/L, low haptoglobin <10 mg/dL, reticulocyte count 8.2%. Associated splenomegaly. Managed by primary care physician. On iron supplementation for concurrent iron deficiency.
Major depressive disorder, mild (F32.0) - Diagnosed 08/2012. Started sertraline 50mg daily 09/08/2012 with good response. Stable mood, no current suicidal ideation. Continues on current regimen.
Substance use disorder (heroin), in sustained remission (F11.21) - History of IV drug use, abstinent since 04/2011. Not currently in formal treatment program. Maintains abstinence, occasional marijuana use.
Iron deficiency anemia (D50.9) - Diagnosed 01/2013 concurrent with autoimmune hemolytic anemia. Started ferrous sulfate 325mg TID 01/14/2013. Recent Hgb 9.8 g/dL, Hct 29%, MCV 102 fL.
Gastroesophageal reflux disease (K21.9) - Diagnosed 05/2013. Managed with lifestyle modifications. Symptoms of nausea and vomiting, taking ondansetron and dicyclomine PRN.
RECENT LABS (Various dates 2013):
Prolactin: 45.2 ng/mL (08/22/2013, elevated)
CBC: Hgb 9.8, Hct 29%, MCV 102 fL (10/28/2013)
Direct Coombs: Positive (01/14/2013)
LDH: 420 U/L, Haptoglobin <10 mg/dL (01/14/2013)
MRI brain with contrast: Normal pituitary, post-surgical changes only (10/18/2013)
Pap smear: Normal cytology, HPV negative (11/15/2012)
Mammogram: BI-RADS 1, normal (02/28/2013)
```

## Clinical note templates
<a name="al-templates"></a>

Templates define the structure, sections, and formatting rules that the agent follows when generating clinical documentation. You must specify an output format by passing a configuration object to the `noteTemplateSettings` API parameter with every session. Ambient documentation supports two methods to specify the output format — managed templates or custom templates.

### Managed templates
<a name="al-managed-templates"></a>

Ambient documentation provides seven pre-built note templates. The configuration object for managed templates, `managedTemplate`, specifies the template through the `templateType` parameter. The default template is HISTORY\_AND\_PHYSICAL.


| Template | Description | Use case | 
| --- | --- | --- | 
| HISTORY\_AND\_PHYSICAL (default) | Summaries for key clinical documentation sections | General physical health encounters | 
| PHYSICAL\_SOAP | Physical health focused SOAP format | Physical health encounters using SOAP structure | 
| BEHAVIORAL\_SOAP | Behavioral health focused SOAP format | Behavioral health encounters using SOAP structure | 
| GIRPP | Progress-toward-goals format | Behavioral health — tracking patient progress | 
| BIRP | Behavioral patterns and responses format | Behavioral health — documenting behavioral patterns | 
| SIRP | Situational context of therapy format | Behavioral health — emphasizing situational context | 
| DAP | Simplified clinical documentation format | Brief or focused encounters | 

#### HISTORY\_AND\_PHYSICAL sections
<a name="al-managed-template-sections"></a>


| Section | Description | 
| --- | --- | 
| CHIEF COMPLAINT | Brief description of the patient’s reason for visiting the clinician | 
| HISTORY OF PRESENT ILLNESS | Information on the patient’s illness, including severity, onset, timing, current treatments, and affected areas | 
| REVIEW OF SYSTEMS | Patient-reported evaluation of symptoms across different body systems | 
| PAST MEDICAL HISTORY | Previous medical conditions, surgeries, and treatments | 
| PAST FAMILY HISTORY | Health conditions that run in the patient’s family | 
| PAST SOCIAL HISTORY | Social life, habits, occupation, and environmental factors affecting health | 
| PHYSICAL EXAMINATION | Clinician’s findings from physical examination of body systems and vital signs | 
| DIAGNOSTIC TESTING | Results and interpretations of laboratory tests, imaging studies, and other diagnostic procedures | 
| ASSESSMENT | Clinician’s assessment of patient’s health | 
| PLAN | Clinician-recommended medical treatments, lifestyle adjustments, and further appointments | 

#### PHYSICAL\_SOAP and BEHAVIORAL\_SOAP sections
<a name="al-soap-sections"></a>


| Section | Description | 
| --- | --- | 
| Subjective | The patient’s goals, experiences, and existing and past issues | 
| Objective | Data and facts about the patient | 
| Assessment | The clinician’s diagnosis of the patient’s situation | 
| Plan | Clinician-recommended next steps in treatment, including future interventions and referrals | 

**Note**  
PHYSICAL\_SOAP is optimized for physical health documentation. BEHAVIORAL\_SOAP is optimized for behavioral health documentation. Both share the same section structure.

#### GIRPP sections
<a name="al-girpp-sections"></a>


| Section | Description | 
| --- | --- | 
| Goal | The identified problem, challenge, or behavior to address through treatment | 
| Intervention | The specific treatment, method, or technique used by the clinician | 
| Response | How the patient responded to the intervention, including participation level and feedback | 
| Progress | The clinician’s assessment of movement toward treatment goals | 
| Plan | Clinician-recommended next steps in treatment, including future interventions, homework, and referrals | 

#### BIRP sections
<a name="al-birp-sections"></a>


| Section | Description | 
| --- | --- | 
| Behavior | The problems the patient presents and their response to treatment | 
| Intervention | The specific treatment, method, or technique used by the clinician | 
| Response | How the patient responded to the intervention | 
| Plan | Next steps in treatment | 

#### SIRP sections
<a name="al-sirp-sections"></a>


| Section | Description | 
| --- | --- | 
| Situation | The problem the patient presents and their goal for seeking therapy | 
| Intervention | The specific treatment, method, or technique used by the clinician | 
| Response | How the patient responded to the intervention | 
| Plan | Clinician-recommended next steps in treatment | 

#### DAP sections
<a name="al-dap-sections"></a>


| Section | Description | 
| --- | --- | 
| Data | The patient’s reasons for seeking treatment and information about the patient | 
| Assessment | The clinician’s diagnosis of the patient’s situation | 
| Plan | Clinician-recommended next steps in treatment | 

### Custom templates
<a name="al-custom-templates"></a>

Ambient documentation uses a two-layer customization model: Base and Output Specification. These two layers are managed in a configuration object, `customTemplate`. The `customTemplate` configuration object contains two parameters: `templateType` sets the Base template and `templateInstructions` contains the Output Specification.

The Base (`templateType`) sets the organization structure of the clinical facts detected during the conversation. The following base templates are supported:


| Base | Description | Use case | 
| --- | --- | --- | 
| HISTORY\_AND\_PHYSICAL | Summaries for key clinical documentation sections | General physical health encounters | 
| BEHAVIORAL\_SOAP | Behavioral health focused SOAP format | Behavioral health encounters using SOAP structure | 
| GIRPP | Progress-toward-goals format | Behavioral health — tracking patient progress | 
| BIRP | Behavioral patterns and responses format | Behavioral health — documenting behavioral patterns | 
| SIRP | Situational context of therapy format | Behavioral health — emphasizing situational context | 
| DAP | Simplified clinical documentation format | Brief or focused encounters | 

The Output Specification object (`templateInstructions`) is organized as an array of instructions, with a `sectionHeader` that defines the section name and `sectionInstructions` that combines instructions and a template for that section.

Customization instructions can include three types of directives:
+  **Verbosity instructions** — Control content conciseness or elaboration. Example: "Describe the chief complaint in 1 sentence or less."
+  **Template usage instructions** — Direct how the agent handles misalignment between the template and the encounter content. Example: "Follow the template exactly: if requested data is unavailable, write INFORMATION NOT FOUND."
+  **Style instructions** — Specify formatting, terminology, and reasoning requirements. Example: "Use numbered problems in the Assessment section."

Templates can be provided as text with placeholders, structured JSON schemas, or example previous notes.


| Method | Description | Use when | 
| --- | --- | --- | 
| Text template with placeholders | A template with section headers and placeholder fields (such as <chief\_complaint>) that the agent fills from the encounter | You want precise control over section layout and content placement | 
| Structured JSON template | A JSON schema defining fields, nesting, and per-field formatting rules | Your EHR requires structured data output rather than prose | 
| Example previous note | A prior clinical note provided as a reference for the desired format and style | A provider wants notes that match their existing documentation patterns | 

**Note**  
The service is stateless. To use a previous note as a style reference, your application must include it in the instructions for each session. The agent does not retain provider preferences across sessions.

### Example customization instruction
<a name="al-example-customization"></a>

The following example shows a customization instruction for a SOAP note using the `customTemplate` configuration object.

```
{
  "clinicalNoteGenerationSettings": {
    "noteTemplateSettings": {
      "customTemplate": {
        "templateType": "HISTORY_AND_PHYSICAL",
        "templateInstructions": [
          {
            "sectionHeader": "Subjective",
            "sectionInstruction": "You will be generating a SOAP note one section at a time, starting with the `S` section. Please use this template when generating the `S` section:\n<template>\nSUBJECTIVE:\nChief Complaint: <Brief statement, in patient's own words, if available>\nHistory of Present Illness: <Narrative description of current symptoms, onset, duration, quality, severity, timing, context, modifying factors, associated symptoms.>\nReview of Systems:\n• Constitutional: <fever, chills, weight changes, fatigue>\n• Cardiovascular: <chest pain, palpitations, shortness of breath>\n• Respiratory: <cough, dyspnea, wheezing>\n• GI: <nausea, vomiting, diarrhea, constipation, abdominal pain>\n• GU: <dysuria, frequency, urgency, hematuria>\n• Musculoskeletal: <joint pain, muscle weakness, back pain>\n• Neurological: <headache, dizziness, numbness, weakness>\n• Psychiatric: <mood changes, anxiety, sleep disturbances>\n• All other systems negative unless noted above Past Medical History: <List chronic conditions>\nPast Surgical History: <List previous surgeries with dates>\nMedications: <Current medications with doses>\nAllergies: <Drug allergies and reactions, or NKDA>\nSocial History: <Tobacco, alcohol, drugs, occupation, living situation>\nFamily History: <Relevant family medical history>\n</template>"
          }
        ]
      }
    }
  }
}
```

### Template best practices
<a name="al-template-best-practices"></a>

The agent achieves 97.7% average layout adherence with well-designed templates.
+  **Define your note structure with named section headers.** List each section of your desired note by name, using a consistent delimiter. The model uses these headers as structural anchors to place content in the correct location.
+  **Use descriptive placeholders** that explain what content belongs in each section. For example, `Chief Complaint: <Brief statement in patient’s own words, if available>`.
+  **Enumerate expected subsections** for multi-part fields. For sections that span multiple categories (such as body systems or problem lists), list them explicitly with representative values to indicate scope.
+  **Handle missing information gracefully.** Use phrasing like "if available" or "if applicable" within placeholders to signal that a section can be omitted when the encounter does not produce relevant content.
+  **Test templates across visit types.** A template that works for follow-up visits may not suit new patient encounters or wellness exams. Validate your templates against a representative sample of encounters before deploying broadly.

## Outputs
<a name="al-outputs"></a>

Ambient documentation generates three output files:

### Transcript file
<a name="al-transcript"></a>

The transcript file contains turn-by-turn transcription with word-level timestamps. Amazon Connect Health adds participant role detection, labeling each speaker as CLINICIAN or PATIENT. If a conversation has more than one participant in each category, each participant is assigned a number (for example, `CLINICIAN_0`, `CLINICIAN_1`).

### Clinical documentation and evidence mapping file
<a name="al-clinical-doc"></a>

The clinical documentation file contains the structured clinical note generated from the patient-clinician conversation and a section linking each generated statement back to its source in the conversation transcript or patient context input.

The file follows the managed template or customization instructions provided at the start of the session. Each section can contain visit-derived content (from the conversation) and context-derived content (from patient context input). Multiple output formats are supported: prose/free-text and structured JSON depending on template configuration. The evidence mapping section enables clinicians to verify the origin of any AI-generated content. Each mapping entry contains the generated sentence and the source transcript/context reference.

### After-visit summary file
<a name="al-after-visit"></a>

The after-visit summary file contains a patient-facing summary written in accessible language for a clinician’s review and finalization. It includes a plain-language description of the visit, current medications with dosage and frequency, clinician’s follow-up instructions, and action items for the patient.

The summary is generated from the clinical documentation file, not directly from the transcript, ensuring consistency between the clinical note and the patient-facing summary.

For complete API parameter details, request/response schemas, and streaming setup instructions, see the [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html).