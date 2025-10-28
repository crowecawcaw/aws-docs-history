# Transcribing with the AWS SDKs

You can use SDKs for both batch and streaming transcriptions. If you're transcribing a media
file located in an Amazon S3 bucket, you're performing a batch transcription. If you're
transcribing a real-time stream of audio data, you're performing a streaming transcription.

For a list of the programming languages you can use with Amazon Transcribe, see
[Supported programming languages](supported-languages.md#supported-sdks "supported-languages.md#supported-sdks"). Note that streaming
transcriptions are not supported with all AWS SDKs. To view supported media formats
and other media requirements and constraints, see [Data input and output](how-input.md "how-input.md").

For more information on all available AWS SDKs and builder tools, refer to
[Tools to Build on AWS](https://aws.amazon.com/developer/tools "https://aws.amazon.com/developer/tools").

###### Tip

For additional examples using the AWS SDKs, including feature-specific,
scenario, and cross-service examples, refer to the [Code examples for Amazon Transcribe using AWS SDKs](service_code_examples.md "service_code_examples.md") chapter.

You can also find SDK code samples in these GitHub repositories:

- [AWS Code Examples](https://github.com/aws-samples "https://github.com/aws-samples")
- [Amazon Transcribe Examples](https://github.com/aws-samples/amazon-transcribe-examples "https://github.com/aws-samples/amazon-transcribe-examples")
  You can create batch transcriptions using the URI of a media file located in an Amazon S3
  bucket. If you're unsure how to create an Amazon S3 bucket or upload your file, refer to
  [Create your first S3
  bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md") and [Upload an object
  to your bucket](../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md "../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md").

Java

```
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.transcribe.TranscribeClient;
import software.amazon.awssdk.services.transcribe.model.*;
import software.amazon.awssdk.services.transcribestreaming.model.LanguageCode;

public class TranscribeDemoApp {
    private static final Region REGION = Region.`US_WEST_2`;
    private static TranscribeClient client;

    public static void main(String args[]) {

        client = TranscribeClient.builder()
                .credentialsProvider(getCredentials())
                .region(REGION)
                .build();

        String transcriptionJobName = "`my-first-transcription-job`";
        String mediaType = "`flac`"; // can be other types
        Media myMedia = Media.builder()
                .mediaFileUri("s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`")
                .build();

        String outputS3BucketName = "s3://`amzn-s3-demo-bucket`";
        // Create the transcription job request
        StartTranscriptionJobRequest request = StartTranscriptionJobRequest.builder()
                .transcriptionJobName(transcriptionJobName)
                .languageCode(LanguageCode.`EN_US`.toString())
                .mediaSampleRateHertz(`16000`)
                .mediaFormat(mediaType)
                .media(myMedia)
                .outputBucketName(outputS3BucketName)
                .build();

        // send the request to start the transcription job
        StartTranscriptionJobResponse startJobResponse = client.startTranscriptionJob(request);

        System.out.println("Created the transcription job");
        System.out.println(startJobResponse.transcriptionJob());

        // Create the get job request
        GetTranscriptionJobRequest getJobRequest = GetTranscriptionJobRequest.builder()
                .transcriptionJobName(transcriptionJobName)
                .build();

        // send the request to get the transcription job including the job status
        GetTranscriptionJobResponse getJobResponse = client.getTranscriptionJob(getJobRequest);

        System.out.println("Get the transcription job request");
        System.out.println(getJobResponse.transcriptionJob());
    }

    private static AwsCredentialsProvider getCredentials() {
        return DefaultCredentialsProvider.create();
    }

}
```

JavaScript

```
const { TranscribeClient, StartTranscriptionJobCommand } = require("@aws-sdk/client-transcribe"); // CommonJS import

const region = "`us-west-2`";
const credentials = {
  "accessKeyId": "",
  "secretAccessKey": "",
};

const input = {
  TranscriptionJobName: "`my-first-transcription-job`",
  LanguageCode: "`en-US`",
  Media: {
    MediaFileUri: "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`"
  },
  OutputBucketName: "`amzn-s3-demo-bucket`",
};

async function startTranscriptionRequest() {
  const transcribeConfig = {
    region,
    credentials
  };
  const transcribeClient = new TranscribeClient(transcribeConfig);
  const transcribeCommand = new StartTranscriptionJobCommand(input);
  try {
    const transcribeResponse = await transcribeClient.send(transcribeCommand);
    console.log("Transcription job created, the details:");
    console.log(transcribeResponse.TranscriptionJob);
  } catch(err) {
    console.log(err);
  }
}

startTranscriptionRequest();
```

Python

```
import time
import boto3

def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName = job_name,
        Media = {
            'MediaFileUri': file_uri
        },
        MediaFormat = '`flac`',
        LanguageCode = '`en-US`'
    )

    max_tries = `60`
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName = job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                print(
                    f"Download the transcript from\n"
                    f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}.")
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def main():
    transcribe_client = boto3.client('transcribe', region_name = 'us-west-2')
    file_uri = 's3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`'
    transcribe_file('Example-job', file_uri, transcribe_client)


if __name__ == '__main__':
    main()
```

You can create streaming transcriptions using a streamed media file or a live media
stream.

Note that the standard AWS SDK for Python (Boto3) is not supported for Amazon Transcribe
streaming. To start a streaming transcription using Python, use this
[async Python
SDK for Amazon Transcribe](https://github.com/awslabs/amazon-transcribe-streaming-sdk "https://github.com/awslabs/amazon-transcribe-streaming-sdk").

Java
The following example is a Java program that transcribes streaming audio.

To run this example, note the following:

- You must use the [AWS SDK for Java
  2.x](../../../sdk-for-java/latest/developer-guide/home.md "../../../sdk-for-java/latest/developer-guide/home.md").
- Clients must use Java 1.8 to be compatible with the
  [AWS SDK for Java
  2.x](../../../sdk-for-java/latest/developer-guide/home.md "../../../sdk-for-java/latest/developer-guide/home.md").
- The sample rate you specify must match the actual sample rate of your
  audio stream.

See also: [Retry
client for Amazon Transcribe streaming (Java SDK)](https://github.com/awsdocs/aws-doc-sdk-examples/tree/b320aeae1a3e650bffc23f9584a26a7ca177cbb2/javav2/example_code/transcribe/src/main/java/com/amazonaws/transcribestreaming "https://github.com/awsdocs/aws-doc-sdk-examples/tree/b320aeae1a3e650bffc23f9584a26a7ca177cbb2/javav2/example_code/transcribe/src/main/java/com/amazonaws/transcribestreaming"). This code manages the connection to
Amazon Transcribe and retries sending data when there are errors on the connection. For example, if
there is a transient error on the network, this client resends the request that
failed.

```
public class TranscribeStreamingDemoApp {
    private static final Region REGION = Region.`US_WEST_2`;
    private static TranscribeStreamingAsyncClient client;

    public static void main(String args[]) throws URISyntaxException, ExecutionException, InterruptedException, LineUnavailableException {

        client = TranscribeStreamingAsyncClient.builder()
                .credentialsProvider(getCredentials())
                .region(REGION)
                .build();

        CompletableFuture<Void> result = client.startStreamTranscription(getRequest(16_000),
                new AudioStreamPublisher(getStreamFromMic()),
                getResponseHandler());

        result.get();
        client.close();
    }

    private static InputStream getStreamFromMic() throws LineUnavailableException {

        // Signed PCM AudioFormat with 16,000 Hz, 16 bit sample size, mono
        int sampleRate = `16000`;
        AudioFormat format = new AudioFormat(sampleRate, 16, 1, true, false);
        DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

        if (!AudioSystem.isLineSupported(info)) {
            System.out.println("Line not supported");
            System.exit(0);
        }

        TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
        line.open(format);
        line.start();

        InputStream audioStream = new AudioInputStream(line);
        return audioStream;
    }

    private static AwsCredentialsProvider getCredentials() {
        return DefaultCredentialsProvider.create();
    }

    private static StartStreamTranscriptionRequest getRequest(Integer mediaSampleRateHertz) {
        return StartStreamTranscriptionRequest.builder()
                .languageCode(LanguageCode.`EN_US`.toString())
                .mediaEncoding(MediaEncoding.`PCM`)
                .mediaSampleRateHertz(mediaSampleRateHertz)
                .build();
    }

    private static StartStreamTranscriptionResponseHandler getResponseHandler() {
        return StartStreamTranscriptionResponseHandler.builder()
                .onResponse(r -> {
                    System.out.println("Received Initial response");
                })
                .onError(e -> {
                    System.out.println(e.getMessage());
                    StringWriter sw = new StringWriter();
                    e.printStackTrace(new PrintWriter(sw));
                    System.out.println("Error Occurred: " + sw.toString());
                })
                .onComplete(() -> {
                    System.out.println("=== All records stream successfully ===");
                })
                .subscriber(event -> {
                    List<Result> results = ((TranscriptEvent) event).transcript().results();
                    if (results.size() > 0) {
                        if (!results.get(0).alternatives().get(0).transcript().isEmpty()) {
                            System.out.println(results.get(0).alternatives().get(0).transcript());
                        }
                    }
                })
                .build();
    }

    private InputStream getStreamFromFile(String `myMediaFileName`) {
        try {
            File inputFile = new File(getClass().getClassLoader().getResource(myMediaFileName).getFile());
            InputStream audioStream = new FileInputStream(inputFile);
            return audioStream;
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    private static class AudioStreamPublisher implements Publisher<AudioStream> {
        private final InputStream inputStream;
        private static Subscription currentSubscription;


        private AudioStreamPublisher(InputStream inputStream) {
            this.inputStream = inputStream;
        }

        @Override
        public void subscribe(Subscriber<? super AudioStream> s) {

            if (this.currentSubscription == null) {
                this.currentSubscription = new SubscriptionImpl(s, inputStream);
            } else {
                this.currentSubscription.cancel();
                this.currentSubscription = new SubscriptionImpl(s, inputStream);
            }
            s.onSubscribe(currentSubscription);
        }
    }

    public static class SubscriptionImpl implements Subscription {
        private static final int CHUNK_SIZE_IN_BYTES = 1024 * 1;
        private final Subscriber<? super AudioStream> subscriber;
        private final InputStream inputStream;
        private ExecutorService executor = Executors.newFixedThreadPool(1);
        private AtomicLong demand = new AtomicLong(0);

        SubscriptionImpl(Subscriber<? super AudioStream> s, InputStream inputStream) {
            this.subscriber = s;
            this.inputStream = inputStream;
        }

        @Override
        public void request(long n) {
            if (n <= 0) {
                subscriber.onError(new IllegalArgumentException("Demand must be positive"));
            }

            demand.getAndAdd(n);

            executor.submit(() -> {
                try {
                    do {
                        ByteBuffer audioBuffer = getNextEvent();
                        if (audioBuffer.remaining() > 0) {
                            AudioEvent audioEvent = audioEventFromBuffer(audioBuffer);
                            subscriber.onNext(audioEvent);
                        } else {
                            subscriber.onComplete();
                            break;
                        }
                    } while (demand.decrementAndGet() > 0);
                } catch (Exception e) {
                    subscriber.onError(e);
                }
            });
        }

        @Override
        public void cancel() {
            executor.shutdown();
        }

        private ByteBuffer getNextEvent() {
            ByteBuffer audioBuffer = null;
            byte[] audioBytes = new byte[CHUNK_SIZE_IN_BYTES];

            int len = 0;
            try {
                len = inputStream.read(audioBytes);

                if (len <= 0) {
                    audioBuffer = ByteBuffer.allocate(0);
                } else {
                    audioBuffer = ByteBuffer.wrap(audioBytes, 0, len);
                }
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }

            return audioBuffer;
        }

        private AudioEvent audioEventFromBuffer(ByteBuffer bb) {
            return AudioEvent.builder()
                    .audioChunk(SdkBytes.fromByteBuffer(bb))
                    .build();
        }
    }
}
```

JavaScript

```
const {
  TranscribeStreamingClient,
  StartStreamTranscriptionCommand,
} = require("@aws-sdk/client-transcribe-streaming");
const { createReadStream } = require("fs");
const { join } = require("path");

const audio = createReadStream(join(__dirname, "`my-media-file`.`flac`"), { highWaterMark: 1024 * 16});

const LanguageCode = "`en-US`";
const MediaEncoding = "`pcm`";
const MediaSampleRateHertz = "`16000`";
const credentials = {
  "accessKeyId": "",
  "secretAccessKey": "",
};
async function startRequest() {
  const client = new TranscribeStreamingClient({
    region: "`us-west-2`",
    credentials
  });

  const params = {
    LanguageCode,
    MediaEncoding,
    MediaSampleRateHertz,
    AudioStream: (async function* () {
      for await (const chunk of audio) {
        yield {AudioEvent: {AudioChunk: chunk}};
      }
    })(),
  };
  const command = new StartStreamTranscriptionCommand(params);
  // Send transcription request
  const response = await client.send(command);
  // Start to print response
  try {
    for await (const event of response.TranscriptResultStream) {
      console.log(JSON.stringify(event));
    }
  } catch(err) {
    console.log("error")
    console.log(err)
  }
}
startRequest();
```

Python
The following example is a Python program that transcribes streaming audio.

To run this example, note the following:

- You must use this
  [SDK for
  Python](https://github.com/awslabs/amazon-transcribe-streaming-sdk "https://github.com/awslabs/amazon-transcribe-streaming-sdk") .
- The sample rate you specify must match the actual sample rate of your
  audio stream.

```
import asyncio
# This example uses aiofile for asynchronous file reads.
# It's not a dependency of the project but can be installed
# with `pip install aiofile`.
import aiofile

from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent

"""
Here's an example of a custom event handler you can extend to
process the returned transcription results as needed. This
handler will simply print the text out to your interpreter.
"""
class MyEventHandler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        # Here's an example to get started.
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                print(alt.transcript)


async def basic_transcribe():
    # Set up our client with your chosen Region
    client = TranscribeStreamingClient(region = "`us-west-2`")

    # Start transcription to generate async stream
    stream = await client.start_stream_transcription(
        language_code = "`en-US`",
        media_sample_rate_hz = `16000`,
        media_encoding = "`pcm`",
    )

    async def write_chunks():
        # NOTE: For pre-recorded files longer than 5 minutes, the sent audio
        # chunks should be rate limited to match the real-time bitrate of the
        # audio stream to avoid signing issues.
        async with aiofile.AIOFile('`filepath`/`my-media-file`.`flac`', 'rb') as afp:
            reader = aiofile.Reader(afp, chunk_size = 1024 * 16)
            async for chunk in reader:
                await stream.input_stream.send_audio_event(audio_chunk = chunk)
        await stream.input_stream.end_stream()

    # Instantiate our handler and start processing events
    handler = MyEventHandler(stream.output_stream)
    await asyncio.gather(write_chunks(), handler.handle_events())

loop = asyncio.get_event_loop()
loop.run_until_complete(basic_transcribe())
loop.close()
```

C++
Refer to the Code examples chapter for the
[streaming C++ SDK example](../../../code-library/latest/ug/cpp_1_transcribe-streaming_code_examples.md "../../../code-library/latest/ug/cpp_1_transcribe-streaming_code_examples.md") .

## Using this service with an AWS SDK

AWS software development kits (SDKs) are available for many popular programming languages. Each SDK provides an API, code examples, and documentation that
make it easier for developers to build applications in their preferred language.

| SDK documentation                                                                         | Code examples                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AWS SDK for C++](../../../sdk-for-cpp.md "../../../sdk-for-cpp.md")                      | [AWS SDK for C++ code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp")                          |
| [AWS CLI](../../../cli.md "../../../cli.md")                                              | [AWS CLI code examples](../../../code-library/latest/ug/cli_2_code_examples.md "../../../code-library/latest/ug/cli_2_code_examples.md")                                                |
| [AWS SDK for Go](../../../sdk-for-go.md "../../../sdk-for-go.md")                         | [AWS SDK for Go code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2")                         |
| [AWS SDK for Java](../../../sdk-for-java.md "../../../sdk-for-java.md")                   | [AWS SDK for Java code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2")                   |
| [AWS SDK for JavaScript](../../../sdk-for-javascript.md "../../../sdk-for-javascript.md") | [AWS SDK for JavaScript code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3") |
| [AWS SDK for Kotlin](../../../sdk-for-kotlin.md "../../../sdk-for-kotlin.md")             | [AWS SDK for Kotlin code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin")                 |
| [AWS SDK for .NET](../../../sdk-for-net.md "../../../sdk-for-net.md")                     | [AWS SDK for .NET code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3")               |
| [AWS SDK for PHP](../../../sdk-for-php.md "../../../sdk-for-php.md")                      | [AWS SDK for PHP code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php")                          |
| [AWS Tools for PowerShell](../../../powershell.md "../../../powershell.md")               | [AWS Tools for PowerShell code examples](../../../code-library/latest/ug/powershell_5_code_examples.md "../../../code-library/latest/ug/powershell_5_code_examples.md")                 |
| [AWS SDK for Python (Boto3)](../../../pythonsdk.md "../../../pythonsdk.md")               | [AWS SDK for Python (Boto3) code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python")         |
| [AWS SDK for Ruby](../../../sdk-for-ruby.md "../../../sdk-for-ruby.md")                   | [AWS SDK for Ruby code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby")                       |
| [AWS SDK for Rust](../../../sdk-for-rust.md "../../../sdk-for-rust.md")                   | [AWS SDK for Rust code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1")                   |
| [AWS SDK for SAP ABAP](../../../sdk-for-sapabap.md "../../../sdk-for-sapabap.md")         | [AWS SDK for SAP ABAP code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap")           |
| [AWS SDK for Swift](../../../sdk-for-swift.md "../../../sdk-for-swift.md")                | [AWS SDK for Swift code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift")                    | For examples specific to this service, see [Code examples for Amazon Transcribe using AWS SDKs](service_code_examples.md "service_code_examples.md"). ###### Example availability Can't find what you need? Request a code example by using the **Provide feedback** link at the bottom of this page. |
