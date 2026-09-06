

# Examine the code
<a name="producersdk-android-writecode"></a>

In this section of the [Android producer library procedure](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-android.html), you examine the example code. 

The Android test application (`AmazonKinesisVideoDemoApp`) shows the following coding pattern:
+ Create an instance of `KinesisVideoClient`.
+ Create an instance of `MediaSource`.
+ Start streaming. Start the `MediaSource`, and it starts sending data to the client.

The following sections provide details.



## Create an instance of KinesisVideoClient
<a name="producersdk-android-review-code-create-client"></a>

You create the `[KinesisVideoClient](https://github.com/aws-amplify/aws-sdk-android/blob/main/aws-android-sdk-kinesisvideo/src/main/java/com/amazonaws/kinesisvideo/client/KinesisVideoClient.java)` object by calling the `[createKinesisVideoClient](https://github.com/aws-amplify/aws-sdk-android/blob/main/aws-android-sdk-kinesisvideo/src/main/java/com/amazonaws/mobileconnectors/kinesisvideo/client/KinesisVideoAndroidClientFactory.java)` operation.

```
mKinesisVideoClient = KinesisVideoAndroidClientFactory.createKinesisVideoClient(
                    getActivity(),
                    KinesisVideoDemoApp.KINESIS_VIDEO_REGION,
                    KinesisVideoDemoApp.getCredentialsProvider());
```

For `KinesisVideoClient` to make network calls, it needs credentials to authenticate. You pass in an instance of `AWSCredentialsProvider`, which reads your Amazon Cognito credentials from the `awsconfiguration.json` file that you modified in the previous section.

## Create an instance of MediaSource
<a name="producersdk-android-review-code-create-mediasource"></a>

To send bytes to your Kinesis video stream, you must produce the data. Amazon Kinesis Video Streams provides the `[MediaSource](https://github.com/aws-amplify/aws-sdk-android/blob/main/aws-android-sdk-kinesisvideo/src/main/java/com/amazonaws/kinesisvideo/internal/client/mediasource/MediaSource.java)` interface, which represents the data source.

For example, the Kinesis Video Streams Android library provides the `[AndroidCameraMediaSource](https://github.com/aws-amplify/aws-sdk-android/blob/main/aws-android-sdk-kinesisvideo/src/main/java/com/amazonaws/mobileconnectors/kinesisvideo/mediasource/android/AndroidCameraMediaSource.java)` implementation of the `MediaSource` interface. This class reads data from one of the device's cameras.

In the following code example (from the `[fragment/StreamConfigurationFragment.java](https://github.com/awslabs/aws-sdk-android-samples/blob/main/AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/fragment/StreamConfigurationFragment.java)` file), the configuration for the media source is created:

```
private AndroidCameraMediaSourceConfiguration getCurrentConfiguration() {
return new AndroidCameraMediaSourceConfiguration(
        AndroidCameraMediaSourceConfiguration.builder()
                .withCameraId(mCamerasDropdown.getSelectedItem().getCameraId())
                .withEncodingMimeType(mMimeTypeDropdown.getSelectedItem().getMimeType())
                .withHorizontalResolution(mResolutionDropdown.getSelectedItem().getWidth())
                .withVerticalResolution(mResolutionDropdown.getSelectedItem().getHeight())
                .withCameraFacing(mCamerasDropdown.getSelectedItem().getCameraFacing())
                .withIsEncoderHardwareAccelerated(
                        mCamerasDropdown.getSelectedItem().isEndcoderHardwareAccelerated())
                .withFrameRate(FRAMERATE_20)
                .withRetentionPeriodInHours(RETENTION_PERIOD_48_HOURS)
                .withEncodingBitRate(BITRATE_384_KBPS)
                .withCameraOrientation(-mCamerasDropdown.getSelectedItem().getCameraOrientation())
                .withNalAdaptationFlags(StreamInfo.NalAdaptationFlags.NAL_ADAPTATION_ANNEXB_CPD_AND_FRAME_NALS)
                .withIsAbsoluteTimecode(false));
}
```

In the following code example (from the `[fragment/StreamingFragment.java](https://github.com/awslabs/aws-sdk-android-samples/blob/main/AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/fragment/StreamingFragment.java)` file), the media source is created:

```
mCameraMediaSource = (AndroidCameraMediaSource) mKinesisVideoClient
    .createMediaSource(mStreamName, mConfiguration);
```

## Start the media source
<a name="producersdk-android-review-code-start-mediasource"></a>

Start the media source so that it can begin generating data and sending it to the client. The following code example is from the `[fragment/StreamingFragment.java](https://github.com/awslabs/aws-sdk-android-samples/blob/main/AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/fragment/StreamingFragment.java)` file:

```
mCameraMediaSource.start();
```

