# Starting AWS HealthScribe streaming transcription

The following code example shows how to set up a AWS HealthScribe streaming transcription using the AWS SDKs.

###### Topics

- [SDK for Java 2.x](#health-scribe-java-stream "#health-scribe-java-stream")
- [Streaming transcription output examples](#health-scribe-streaming-output-example "#health-scribe-streaming-output-example")

## SDK for Java 2.x

The following example uses the SDK for Java 2.x to set up streaming and make a [StartMedicalScribeStream](../APIReference/API_streaming_StartMedicalScribeStream.md "../APIReference/API_streaming_StartMedicalScribeStream.md")
request.

```
package org.example;

import io.reactivex.rxjava3.core.BackpressureStrategy;
import io.reactivex.rxjava3.core.Flowable;
import org.reactivestreams.Publisher;
import org.reactivestreams.Subscriber;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.transcribestreaming.TranscribeStreamingAsyncClient;
import software.amazon.awssdk.services.transcribestreaming.model.ClinicalNoteGenerationSettings;
import software.amazon.awssdk.services.transcribestreaming.model.LanguageCode;
import software.amazon.awssdk.services.transcribestreaming.model.MediaEncoding;

import software.amazon.awssdk.services.transcribestreaming.model.MedicalScribeInputStream;
import software.amazon.awssdk.services.transcribestreaming.model.MedicalScribePostStreamAnalyticsSettings;
import software.amazon.awssdk.services.transcribestreaming.model.MedicalScribeSessionControlEventType;
import software.amazon.awssdk.services.transcribestreaming.model.MedicalScribeTranscriptEvent;
import software.amazon.awssdk.services.transcribestreaming.model.MedicalScribeTranscriptSegment;
import software.amazon.awssdk.services.transcribestreaming.model.StartMedicalScribeStreamRequest;
import software.amazon.awssdk.services.transcribestreaming.model.StartMedicalScribeStreamResponseHandler;
import software.amazon.awssdk.services.transcribestreaming.model.medicalscribeinputstream.DefaultConfigurationEvent;

import software.amazon.awssdk.http.nio.netty.NettyNioAsyncHttpClient;

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
import java.util.concurrent.CompletableFuture;


public class HealthScribeStreamingDemoApp {
    private static final int CHUNK_SIZE_IN_BYTES = 6400;
    private static final int SAMPLE_RATE = 16000;
    private static final Region REGION = Region.US_EAST_1;
    private static final String sessionId = "`1234abcd-12ab-34cd-56ef-123456SAMPLE`";
    private static final String bucketName = "`amzn-s3-demo-bucket`";
    private static final String resourceAccessRoleArn = "`arn:aws:iam::123456789012:role/resource-access-role`";
    private static TranscribeStreamingAsyncClient client;

    public static void main(String args[]) {

        client = TranscribeStreamingAsyncClient.builder()
                .credentialsProvider(getCredentials())
                .httpClientBuilder(NettyNioAsyncHttpClient.builder())
                .region(REGION)
                .build();
        try {
            StartMedicalScribeStreamRequest request = StartMedicalScribeStreamRequest.builder()
                    .languageCode(LanguageCode.EN_US.toString())
                    .mediaSampleRateHertz(SAMPLE_RATE)
                    .mediaEncoding(MediaEncoding.PCM.toString())
                    .sessionId(sessionId)
                    .build();

            MedicalScribeInputStream endSessionEvent = MedicalScribeInputStream.sessionControlEventBuilder()
                    .type(MedicalScribeSessionControlEventType.END_OF_SESSION)
                    .build();

            CompletableFuture<Void> result = client.startMedicalScribeStream(
                    request,
                    new AudioStreamPublisher(getStreamFromMic(), getConfigurationEvent(),endSessionEvent),
                    getMedicalScribeResponseHandler());
            result.get();
            client.close();
        } catch (Exception e) {
            System.err.println("Error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static AudioInputStream getStreamFromMic() throws LineUnavailableException {
        // Signed PCM AudioFormat with 16kHz, 16 bit sample size, mono
        AudioFormat format = new AudioFormat(SAMPLE_RATE, 16, 1, true, false);
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

        if (!AudioSystem.isLineSupported(info)) {
            System.out.println("Line not supported");
            throw new LineUnavailableException("The audio system microphone line is not supported.");
        }
        TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
        int bufferSize = (CHUNK_SIZE_IN_BYTES / format.getFrameSize()) * format.getFrameSize();
        line.open(format);
        line.start();

        // Create a wrapper class that can be closed when Enter is pressed
        AudioInputStream audioStream = new AudioInputStream(line);

        // Start a thread to monitor for Enter key
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
        monitorThread.setDaemon(true);  // Set as daemon thread so it doesn't prevent JVM shutdown
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

    private static StartMedicalScribeStreamResponseHandler getMedicalScribeResponseHandler() {

        return StartMedicalScribeStreamResponseHandler.builder()
            .onResponse(r -> {
                System.out.println("Received Initial response");
            })
            .onError(Throwable::printStackTrace)
            .onComplete(() -> {
                System.out.println("=== All records streamed successfully ===");
            })
            .subscriber(event -> {
                if (event instanceof MedicalScribeTranscriptEvent) {
                    MedicalScribeTranscriptSegment segment = ((MedicalScribeTranscriptEvent) event).transcriptSegment();
                    if (segment != null && segment.content() != null && !segment.content().isEmpty()) {
                        System.out.println(segment.content());
                    }
                }
            })
            .build();
    }

    private static DefaultConfigurationEvent getConfigurationEvent() {
        MedicalScribePostStreamAnalyticsSettings postStreamSettings = MedicalScribePostStreamAnalyticsSettings
                .builder()
                .clinicalNoteGenerationSettings(
                        ClinicalNoteGenerationSettings.builder()
                                .outputBucketName(bucketName)
                                .build()
                )
                .build();
        return (DefaultConfigurationEvent) MedicalScribeInputStream.configurationEventBuilder()
                .resourceAccessRoleArn(resourceAccessRoleArn)
                .postStreamAnalyticsSettings(postStreamSettings)
                .build();
    }

    private static class AudioStreamPublisher implements Publisher<MedicalScribeInputStream> {
        private final InputStream audioInputStream;
        private final MedicalScribeInputStream configEvent;
        private final MedicalScribeInputStream endSessionEvent;

        private AudioStreamPublisher(AudioInputStream audioInputStream,
                                     MedicalScribeInputStream configEvent,
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
            // Start with config event
            Flowable<MedicalScribeInputStream> configFlow = Flowable.just(configEvent);

            // Create audio chunk flowable
            Flowable<MedicalScribeInputStream> audioFlow = Flowable.create(emitter -> {
                byte[] buffer = new byte[CHUNK_SIZE_IN_BYTES];
                int bytesRead;

                try {
                    while (!emitter.isCancelled() && (bytesRead = audioInputStream.read(buffer)) > 0) {
                        byte[] audioData = bytesRead < buffer.length
                                ? Arrays.copyOfRange(buffer, 0, bytesRead)
                                : buffer;

                        MedicalScribeInputStream audioEvent = MedicalScribeInputStream.audioEventBuilder()
                                .audioChunk(SdkBytes.fromByteArray(audioData))
                                .build();

                        emitter.onNext(audioEvent);
                    }
                    emitter.onComplete();
                } catch (IOException e) {
                    emitter.onError(e);
                }
            }, BackpressureStrategy.BUFFER);

            // End with session end event
            Flowable<MedicalScribeInputStream> endFlow = Flowable.just(endSessionEvent);

            // Concatenate all flows
            return Flowable.concat(configFlow, audioFlow, endFlow);
        }
    }
}
```

## Streaming transcription output examples

After streaming is complete, AWS HealthScribe analyzes the stream contents and produces a transcript JSON file and a clinical note JSON file.
Here are examples of each
output type:

The following is an example of a AWS HealthScribe transcript file from a streaming session.

```
{
    "Conversation": {
        "ClinicalInsights": [{
            "Attributes": [],
            "Category": "MEDICAL_CONDITION",
            "InsightId": "`insightUUID1`",
            "InsightType": "ClinicalEntity",
            "Spans": [{
                "BeginCharacterOffset": 12,
                "Content": "pain",
                "EndCharacterOffset": 15,
                "SegmentId": "uuid1"
            }],
            "Type": "DX_NAME"
        }, {
            "Attributes": [],
            "Category": "TEST_TREATMENT_PROCEDURE",
            "InsightId": "`insightUUID2`",
            "InsightType": "ClinicalEntity",
            "Spans": [{
                "BeginCharacterOffset": 4,
                "Content": "mammogram",
                "EndCharacterOffset": 12,
                "SegmentId": "uuid2"
            }],
            "Type": "TEST_NAME"
        }, {
            "Attributes": [],
            "Category": "TEST_TREATMENT_PROCEDURE",
            "InsightId": "`insightUUID3`",
            "InsightType": "ClinicalEntity",
            "Spans": [{
                "BeginCharacterOffset": 15,
                "Content": "pap smear",
                "EndCharacterOffset": 23,
                "SegmentId": "uuid3"
            }],
            "Type": "TEST_NAME"
        }, {
            "Attributes": [],
            "Category": "MEDICATION",
            "InsightId": "`insightUUID4`",
            "InsightType": "ClinicalEntity",
            "Spans": [{
                "BeginCharacterOffset": 28,
                "Content": "phentermine",
                "EndCharacterOffset": 38,
                "SegmentId": "uuid4"
            }],
            "Type": "GENERIC_NAME"
        }, {
            "Attributes": [{
                "AttributeId": "attributeUUID1",
                "Spans": [{
                    "BeginCharacterOffset": 38,
                    "Content": "high",
                    "EndCharacterOffset": 41,
                    "SegmentId": "uuid5"
                }],
                "Type": "TEST_VALUE"
            }],
            "Category": "TEST_TREATMENT_PROCEDURE",
            "InsightId": "`insightUUID5`",
            "InsightType": "ClinicalEntity",
            "Spans": [{
                "BeginCharacterOffset": 14,
                "Content": "weight",
                "EndCharacterOffset": 19,
                "SegmentId": "uuid6"
            }],
            "Type": "TEST_NAME"
        }, {
            "Attributes": [],
            "Category": "ANATOMY",
            "InsightId": "`insightUUID6`",
            "InsightType": "ClinicalEntity",
            "Spans": [{
                "BeginCharacterOffset": 60,
                "Content": "heart",
                "EndCharacterOffset": 64,
                "SegmentId": "uuid7"
            }],
            "Type": "SYSTEM_ORGAN_SITE"
        }],
        "ConversationId": "`sampleConversationUUID`",
        "LanguageCode": "en-US",
        "SessionId": "`sampleSessionUUID`",
        "TranscriptItems": [{
            "Alternatives": [{
                "Confidence": 0.7925,
                "Content": "Okay"
            }],
            "BeginAudioTime": 0.16,
            "EndAudioTime": 0.6,
            "Type": "PRONUNCIATION"
        },
        {
            "Alternatives": [{
                "Confidence": 0,
                "Content": "."
            }],
            "BeginAudioTime": 0,
            "EndAudioTime": 0,
            "Type": "PUNCTUATION"
        },
        {
            "Alternatives": [{
                "Confidence": 1,
                "Content": "Good"
            }],
            "BeginAudioTime": 0.61,
            "EndAudioTime": 0.92,
            "Type": "PRONUNCIATION"
        },
        {
            "Alternatives": [{
                "Confidence": 1,
                "Content": "afternoon"
            }],
            "BeginAudioTime": 0.92,
            "EndAudioTime": 1.54,
            "Type": "PRONUNCIATION"
        },
        {
            "Alternatives": [{
                "Confidence": 0,
                "Content": "."
            }],
            "BeginAudioTime": 0,
            "EndAudioTime": 0,
            "Type": "PUNCTUATION"
        },
        {
            "Alternatives": [{
                "Confidence": 0.9924,
                "Content": "You"
            }],
            "BeginAudioTime": 1.55,
            "EndAudioTime": 1.88,
            "Type": "PRONUNCIATION"
        },
        {
            "Alternatives": [{
                "Confidence": 1,
                "Content": "lost"
            }],
            "BeginAudioTime": 1.88,
            "EndAudioTime": 2.19,
            "Type": "PRONUNCIATION"
        },
        {
            "Alternatives": [{
                "Confidence": 1,
                "Content": "one"
            }],
            "BeginAudioTime": 2.19,
            "EndAudioTime": 2.4,
            "Type": "PRONUNCIATION"
        },
        {
            "Alternatives": [{
                "Confidence": 1,
                "Content": "lb"
            }],
            "BeginAudioTime": 2.4,
            "EndAudioTime": 2.97,
            "Type": "PRONUNCIATION"
        }
        ],
        "TranscriptSegments": [{
            "BeginAudioTime": 0.16,
            "Content": "Okay.",
            "EndAudioTime": 0.6,
            "ParticipantDetails": {
                "ParticipantRole": "CLINICIAN_0"
            },
            "SectionDetails": {
                "SectionName": "SUBJECTIVE"
            },
            "SegmentId": "uuid1"
        }, {
            "BeginAudioTime": 0.61,
            "Content": "Good afternoon.",
            "EndAudioTime": 1.54,
            "ParticipantDetails": {
                "ParticipantRole": "CLINICIAN_0"
            },
            "SectionDetails": {
                "SectionName": "OTHER"
            },
            "SegmentId": "uuid2"
        }, {
            "BeginAudioTime": 1.55,
            "Content": "You lost one lb.",
            "EndAudioTime": 2.97,
            "ParticipantDetails": {
                "ParticipantRole": "CLINICIAN_0"
            },
            "SectionDetails": {
                "SectionName": "SUBJECTIVE"
            },
            "SegmentId": "uuid3"
        }, {
            "BeginAudioTime": 2.98,
            "Content": "Yeah, I think it, uh, do you feel more energy?",
            "EndAudioTime": 6.95,
            "ParticipantDetails": {
                "ParticipantRole": "CLINICIAN_0"
            },
            "SectionDetails": {
                "SectionName": "SUBJECTIVE"
            },
            "SegmentId": "uuid4"
        }, {
            "BeginAudioTime": 6.96,
            "Content": "Yes.",
            "EndAudioTime": 7.88,
            "ParticipantDetails": {
                "ParticipantRole": "CLINICIAN_0"
            },
            "SectionDetails": {
                "SectionName": "SUBJECTIVE"
            },
            "SegmentId": "uuid5"
        }, {
            "BeginAudioTime": 7.89,
            "Content": "Uh, how about craving for the carbohydrate or sugar or fat or anything?",
            "EndAudioTime": 17.93,
            "ParticipantDetails": {
                "ParticipantRole": "CLINICIAN_0"
            },
            "SectionDetails": {
                "SectionName": "SUBJECTIVE"
            },
            "SegmentId": "uuid6"
        }]
    }
}
```

The following is an example of a AWS HealthScribe clinical documentation insights file from a streaming session.

```
{
  "ClinicalDocumentation": {
    "Sections": [
      {
        "SectionName": "CHIEF_COMPLAINT",
        "Summary": [
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid1"
              },
              {
                "SegmentId": "uuid2"
              },
              {
                "SegmentId": "uuid3"
              },
              {
                "SegmentId": "uuid4"
              },
              {
                "SegmentId": "uuid5"
              },
              {
                "SegmentId": "uuid6"
              }
            ],
            "SummarizedSegment": "Weight loss."
          }
        ]
      },
      {
        "SectionName": "HISTORY_OF_PRESENT_ILLNESS",
        "Summary": [
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid7"
              },
              {
                "SegmentId": "uuid8"
              },
              {
                "SegmentId": "uuid9"
              },
              {
                "SegmentId": "uuid10"
              }
            ],
            "SummarizedSegment": "The patient is seen today for a follow-up of weight loss."
          },
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid11"
              },
              {
                "SegmentId": "uuid12"
              },
              {
                "SegmentId": "uuid13"
              }
            ],
            "SummarizedSegment": "They report feeling more energy and craving carbohydrates, sugar, and fat."
          },
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid14"
              },
              {
                "SegmentId": "uuid15"
              },
              {
                "SegmentId": "uuid16"
              }
            ],
            "SummarizedSegment": "The patient is up to date on their mammogram and pap smear."
          },
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid17"
              },
              {
                "SegmentId": "uuid18"
              },
              {
                "SegmentId": "uuid19"
              },
              {
                "SegmentId": "uuid20"
              }
            ],
            "SummarizedSegment": "The patient is taking phentermine and would like to continue."
          }
        ]
      },
      {
        "SectionName": "REVIEW_OF_SYSTEMS",
        "Summary": [
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid21"
              },
              {
                "SegmentId": "uuid22"
              }
            ],
            "SummarizedSegment": "Patient reports intermittent headaches, occasional chest pains but denies any recent fevers or chills."
          },
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid23"
              },
              {
                "SegmentId": "uuid24"
              }
            ],
            "SummarizedSegment": "No recent changes in vision, hearing, or any respiratory complaints."
          }
        ]
      },
      {
        "SectionName": "PAST_MEDICAL_HISTORY",
        "Summary": [
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid25"
              },
              {
                "SegmentId": "uuid26"
              }
            ],
            "SummarizedSegment": "Patient has a history of hypertension and was diagnosed with Type II diabetes 5 years ago."
          },
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid27"
              },
              {
                "SegmentId": "uuid28"
              }
            ],
            "SummarizedSegment": "Underwent an appendectomy in the early '90s and had a fracture in the left arm during childhood."
          }
        ]
      },
      {
        "SectionName": "ASSESSMENT",
        "Summary": [
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid29"
              },
              {
                "SegmentId": "uuid30"
              }
            ],
            "SummarizedSegment": "Weight loss"
          }
        ]
      },
      {
        "SectionName": "PLAN",
        "Summary": [
          {
            "EvidenceLinks": [
              {
                "SegmentId": "uuid31"
              },
              {
                "SegmentId": "uuid32"
              },
              {
                "SegmentId": "uuid33"
              },
              {
                "SegmentId": "uuid34"
              }
            ],
            "SummarizedSegment": "For the condition of Weight loss: The patient was given a 30-day supply of phentermine and was advised to follow up in 30 days."
          }
        ]
      }
    ],
    "SessionId": "`sampleSessionUUID`"
  }
}
```
