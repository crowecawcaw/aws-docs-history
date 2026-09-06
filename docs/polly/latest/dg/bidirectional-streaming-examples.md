

# Code examples
<a name="bidirectional-streaming-examples"></a>

The following example demonstrates a complete bidirectional streaming session. The program creates an async Amazon Polly client, opens a stream configured with the generative engine and MP3 output, sends text as a series of `TextEvent` messages, accumulates the returned `AudioEvent` chunks into an output file, and closes the stream with a `CloseStreamEvent`. Because input and output happen concurrently, audio data begins arriving before all text has been sent.

------
#### [ Java ]

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.polly.PollyAsyncClient;
import software.amazon.awssdk.services.polly.model.*;

import java.io.FileOutputStream;
import java.io.OutputStream;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Semaphore;
import org.reactivestreams.Publisher;
import org.reactivestreams.Subscription;

public class BidirectionalStreamExample {

    public static void main(String[] args) throws Exception {
        try (PollyAsyncClient pollyClient = PollyAsyncClient.builder()
                .region(Region.US_EAST_1)
                .build()) {

        StartSpeechSynthesisStreamRequest request = StartSpeechSynthesisStreamRequest.builder()
                .engine(Engine.GENERATIVE)
                .voiceId(VoiceId.TIFFANY)
                .outputFormat(OutputFormat.MP3)
                .sampleRate("24000")
                .build();

        try (OutputStream audioOutput = new FileOutputStream("output.mp3")) {

        StartSpeechSynthesisStreamResponseHandler responseHandler =
                StartSpeechSynthesisStreamResponseHandler.builder()
                        .subscriber(StartSpeechSynthesisStreamResponseHandler.Visitor.builder()
                                .onAudioEvent(audioEvent -> {
                                    try {
                                        byte[] audio = audioEvent.audioChunk().asByteArray();
                                        System.out.println("Received AudioEvent: " + audio.length + " bytes");
                                        audioOutput.write(audio);
                                    } catch (Exception e) {
                                        throw new RuntimeException(e);
                                    }
                                })
                                .onStreamClosedEvent(closedEvent -> {
                                    System.out.println("Stream closed. Characters synthesized: "
                                            + closedEvent.requestCharacters());
                                })
                                .onDefault(event -> {})
                                .build())
                        .onError(error -> {
                            System.err.println("Stream error: " + error.getMessage());
                        })
                        .build();

        String[] textChunks = {
                "The weather forecast for today shows clear skies ",
                "with temperatures reaching twenty five degrees. ",
                "Tomorrow we expect some cloud cover in the morning ",
                "but it should clear up by the afternoon. ",
                "The rest of the week looks mostly sunny ",
                "with a slight chance of rain on Friday. ",
                "Overall a great week to spend time outdoors."
        };

        Publisher<StartSpeechSynthesisStreamActionStream> inputPublisher = subscriber -> {
            subscriber.onSubscribe(new Subscription() {
                private final Semaphore permits = new Semaphore(0);
                private volatile boolean cancelled = false;

                @Override
                public void request(long n) {
                    permits.release((int) Math.min(n, Integer.MAX_VALUE));
                }

                @Override
                public void cancel() {
                    cancelled = true;
                    permits.release();
                }

                {
                    new Thread(() -> {
                        for (String chunk : textChunks) {
                            try { permits.acquire(); } catch (InterruptedException e) { return; }
                            if (cancelled) return;
                            System.out.println("Sending TextEvent: " + chunk.trim());
                            subscriber.onNext(StartSpeechSynthesisStreamActionStream.textEventBuilder()
                                    .text(chunk).textType(TextType.TEXT).build());
                            // Simulate delay between chunks (e.g. waiting for LLM tokens)
                            try { Thread.sleep(300); } catch (InterruptedException e) { return; }
                        }
                        if (!cancelled) {
                            subscriber.onNext(StartSpeechSynthesisStreamActionStream
                                    .closeStreamEventBuilder().build());
                            subscriber.onComplete();
                        }
                    }).start();
                }
            });
        };

        CompletableFuture<Void> future = pollyClient.startSpeechSynthesisStream(
                request, inputPublisher, responseHandler);

        future.join();
        } // audioOutput closed
        } // pollyClient closed
    }
}
```

------
#### [ JavaScript ]

```
import { PollyClient, StartSpeechSynthesisStreamCommand } from "@aws-sdk/client-polly";
import { createWriteStream } from "fs";

const client = new PollyClient({ region: "us-east-1" });

const textChunks = [
  "The weather forecast for today shows clear skies ",
  "with temperatures reaching twenty five degrees. ",
  "Tomorrow we expect some cloud cover in the morning ",
  "but it should clear up by the afternoon. ",
  "The rest of the week looks mostly sunny ",
  "with a slight chance of rain on Friday. ",
  "Overall a great week to spend time outdoors.",
];

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function* createInputEvents() {
  for (const chunk of textChunks) {
    console.log(`Sending TextEvent: ${chunk.trim()}`);
    yield {
      TextEvent: {
        Text: chunk,
        TextType: "text",
      },
    };
    // Simulate delay between chunks (e.g. waiting for LLM tokens)
    await sleep(300);
  }

  yield { CloseStreamEvent: {} };
}

async function synthesizeStream() {
  const command = new StartSpeechSynthesisStreamCommand({
    Engine: "generative",
    VoiceId: "Tiffany",
    OutputFormat: "mp3",
    SampleRate: "24000",
    ActionStream: createInputEvents(),
  });

  const response = await client.send(command);
  const outputStream = createWriteStream("output.mp3");

  for await (const event of response.EventStream) {
    if (event.AudioEvent) {
      console.log(`Received AudioEvent: ${event.AudioEvent.AudioChunk.length} bytes`);
      outputStream.write(event.AudioEvent.AudioChunk);
    } else if (event.StreamClosedEvent) {
      console.log(
        `Stream closed. Characters synthesized: ${event.StreamClosedEvent.RequestCharacters}`
      );
    }
  }

  outputStream.end();
}

synthesizeStream().catch(console.error);
```

------
#### [ Go ]

```
package main

import (
	"context"
	"fmt"
	"os"
	"strings"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/polly"
	"github.com/aws/aws-sdk-go-v2/service/polly/types"
)

func main() {
	ctx := context.Background()

	cfg, err := config.LoadDefaultConfig(ctx, config.WithRegion("us-east-1"))
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to load config: %v\n", err)
		os.Exit(1)
	}

	client := polly.NewFromConfig(cfg)

	output, err := client.StartSpeechSynthesisStream(ctx, &polly.StartSpeechSynthesisStreamInput{
		Engine:       types.EngineGenerative,
		VoiceId:      types.VoiceIdTiffany,
		OutputFormat: types.OutputFormatMp3,
		SampleRate:   aws.String("24000"),
	})
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to start stream: %v\n", err)
		os.Exit(1)
	}

	stream := output.GetStream()
	defer stream.Close()

	audioFile, err := os.Create("output.mp3")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to create output file: %v\n", err)
		os.Exit(1)
	}
	defer audioFile.Close()

	textChunks := []string{
		"The weather forecast for today shows clear skies ",
		"with temperatures reaching twenty five degrees. ",
		"Tomorrow we expect some cloud cover in the morning ",
		"but it should clear up by the afternoon. ",
		"The rest of the week looks mostly sunny ",
		"with a slight chance of rain on Friday. ",
		"Overall a great week to spend time outdoors.",
	}

	// Send text events in a goroutine
	go func() {
		for _, chunk := range textChunks {
			fmt.Printf("Sending TextEvent: %s\n", strings.TrimSpace(chunk))
			err := stream.Send(ctx, &types.StartSpeechSynthesisStreamActionStreamMemberTextEvent{
				Value: types.TextEvent{
					Text:     aws.String(chunk),
					TextType: types.TextTypeText,
				},
			})
			if err != nil {
				fmt.Fprintf(os.Stderr, "Failed to send text event: %v\n", err)
				return
			}
			// Simulate delay between chunks (e.g. waiting for LLM tokens)
			time.Sleep(300 * time.Millisecond)
		}

		// Signal end of input
		stream.Send(ctx, &types.StartSpeechSynthesisStreamActionStreamMemberCloseStreamEvent{
			Value: types.CloseStreamEvent{},
		})
	}()

	// Receive audio events
	for event := range stream.Events() {
		switch v := event.(type) {
		case *types.StartSpeechSynthesisStreamEventStreamMemberAudioEvent:
			fmt.Printf("Received AudioEvent: %d bytes\n", len(v.Value.AudioChunk))
			audioFile.Write(v.Value.AudioChunk)
		case *types.StartSpeechSynthesisStreamEventStreamMemberStreamClosedEvent:
			fmt.Printf("Stream closed. Characters synthesized: %d\n", v.Value.RequestCharacters)
		}
	}

	if err := stream.Err(); err != nil {
		fmt.Fprintf(os.Stderr, "Stream error: %v\n", err)
		os.Exit(1)
	}
}
```

------
#### [ Rust ]

```
use aws_sdk_polly::types::{
    CloseStreamEvent, Engine, OutputFormat,
    StartSpeechSynthesisStreamActionStream,
    StartSpeechSynthesisStreamEventStream, TextEvent, TextType, VoiceId,
};
use aws_sdk_polly::Client;
use std::fs::File;
use std::io::Write;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    let config = aws_config::defaults(aws_config::BehaviorVersion::latest())
        .region("us-east-1")
        .load()
        .await;

    let client = Client::new(&config);

    let text_chunks = vec![
        "The weather forecast for today shows clear skies ",
        "with temperatures reaching twenty five degrees. ",
        "Tomorrow we expect some cloud cover in the morning ",
        "but it should clear up by the afternoon. ",
        "The rest of the week looks mostly sunny ",
        "with a slight chance of rain on Friday. ",
        "Overall a great week to spend time outdoors.",
    ];

    let input_stream = async_stream::stream! {
        for chunk in &text_chunks {
            println!("Sending TextEvent: {}", chunk.trim());
            yield Ok(StartSpeechSynthesisStreamActionStream::TextEvent(
                TextEvent::builder().text(*chunk).text_type(TextType::Text).build().unwrap(),
            ));
            // Simulate delay between chunks (e.g. waiting for LLM tokens)
            sleep(Duration::from_millis(300)).await;
        }
        yield Ok(StartSpeechSynthesisStreamActionStream::CloseStreamEvent(
            CloseStreamEvent::builder().build(),
        ));
    };

    let mut output = client
        .start_speech_synthesis_stream()
        .engine(Engine::Generative)
        .voice_id(VoiceId::Tiffany)
        .output_format(OutputFormat::Mp3)
        .sample_rate("24000")
        .action_stream(input_stream.into())
        .send()
        .await
        .expect("Failed to start stream");

    let mut audio_file = File::create("output.mp3").expect("Failed to create output file");

    while let Ok(Some(event)) = output.event_stream.recv().await {
        match event {
            StartSpeechSynthesisStreamEventStream::AudioEvent(audio_event) => {
                if let Some(chunk) = audio_event.audio_chunk() {
                    let bytes = chunk.as_ref();
                    println!("Received AudioEvent: {} bytes", bytes.len());
                    audio_file.write_all(bytes).unwrap();
                }
            }
            StartSpeechSynthesisStreamEventStream::StreamClosedEvent(closed_event) => {
                println!(
                    "Stream closed. Characters synthesized: {}",
                    closed_event.request_characters()
                );
            }
            _ => {}
        }
    }
}
```

------