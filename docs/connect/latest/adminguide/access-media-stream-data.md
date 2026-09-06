

# Develop live media streaming in Connect Customer
<a name="access-media-stream-data"></a>

To help you get started with development using live media streaming, Connect Customer includes the following Kinesis Video Streams repository that contains a basic example of how to consume audio data from your Kinesis Video Streams: [https://github.com/amazon-connect/connect-kvs-consumer-demo](https://github.com/amazon-connect/connect-kvs-consumer-demo) 

This demo builds upon the high level abstractions provided by the Kinesis Video Streams Parser Library to read the `AUDIO_TO_CUSTOMER` and `AUDIO_FROM_CUSTOMER` tracks published by Connect Customer. It stores this data as a raw PCM file. This file can be transformed, transcoded, or played back.