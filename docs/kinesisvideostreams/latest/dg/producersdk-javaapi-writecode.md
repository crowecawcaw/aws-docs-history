# Write and examine the code

In this section of the [Java
producer library procedure](producer-sdk-javaapi.md "producer-sdk-javaapi.md"), you write and examine the Java example code that
you downloaded in the previous section.

The Java test application ([`DemoAppMain`](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/blob/master/src/main/demo/com/amazonaws/kinesisvideo/demoapp/DemoAppMain.java "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/blob/master/src/main/demo/com/amazonaws/kinesisvideo/demoapp/DemoAppMain.java")) shows the following coding
pattern:

- Create an instance of `KinesisVideoClient`.
- Create an instance of `MediaSource`.
- Register the `MediaSource` with the client.
- Start streaming. Start the `MediaSource` and it starts sending data to the
  client.
  The following sections provide details.

## Create an instance

of KinesisVideoClient

You create the `KinesisVideoClient` object by calling the
`createKinesisVideoClient` operation.

```
final KinesisVideoClient kinesisVideoClient = KinesisVideoJavaClientFactory
    .createKinesisVideoClient(
        Regions.US_WEST_2,
        AuthHelper.getSystemPropertiesCredentialsProvider());
```

For `KinesisVideoClient` to make network calls, it needs credentials to
authenticate. You pass in an instance of
`SystemPropertiesCredentialsProvider`, which reads
`AWSCredentials` for the default profile in the credentials
file:

```
[default]
aws_access_key_id = ABCDEFGHIJKLMOPQRSTU
aws_secret_access_key = AbCd1234EfGh5678IjKl9012MnOp3456QrSt7890
```

## Create an

instance of MediaSource

To send bytes to your Kinesis video stream, you must produce the data. Amazon Kinesis Video Streams provides the
`MediaSource` interface, which represents the data source.

For example, the Kinesis Video Streams Java library provides the
`ImageFileMediaSource` implementation of the `MediaSource`
interface. This class only reads data from a series of media files rather than a
Kinesis video stream, but you can use it for testing the code.

```
final MediaSource bytesMediaSource = createImageFileMediaSource();
```

## Register the

MediaSource with the client

Register the media source that you created with the
`KinesisVideoClient` so that it knows about the client (and can then
send data to the client).

```
kinesisVideoClient.registerMediaSource(mediaSource);
```

## Start the media

source

Start the media source so that it can begin generating data and send it to the client.

```
bytesMediaSource.start();
```
