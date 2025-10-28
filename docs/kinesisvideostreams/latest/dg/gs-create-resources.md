# Create the Amazon Kinesis Video Streams and

AWS Secrets Manager resources for your IP camera RTSP URLs

Follow these procedures to create the streams and secrets needed in
AWS Secrets Manager. Do this step first, because you need the ARNs of the
created resources in the policies.

## Create Amazon Kinesis Video Streams

Create Amazon Kinesis Video Streams using the AWS Management Console, AWS CLI, or API.

In the AWS Management Console, open the [Amazon Kinesis Video Streams
console](https://console.aws.amazon.com/kinesisvideo/home/ "https://console.aws.amazon.com/kinesisvideo/home/"). Choose **Video streams** in the left navigation.

For more information, see [Create an Amazon Kinesis video stream](gs-createstream.md "gs-createstream.md").

## Create secrets in AWS Secrets Manager

In the AWS Management Console, open the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/landing "https://console.aws.amazon.com/secretsmanager/landing"). Choose **Secrets** in the left
navigation.

Verify that the appropriate Region is selected.

1. Choose **Store a new secret**.
   1. **Step 1: Choose secret type**
      - Select **Other type of
        secret**.
      - In the **Key/Value Pairs**
        section, add a key-value pair.

      **Key**:
      `MediaURI`

      ###### Note

      The key must be `MediaURI`. This
      is case-sensitive. If you enter it incorrectly,
      the application doesn't work.

      **Value**:
      `Your MediaURI`.

      **Example:**
      `rtsp://<YourCameraIPAddress>:<YourCameraRTSPPort>/YourCameraMediaURI`.

   2. **Step 2: Configure secret**. Give
      this secret a name. Name it whatever you
      want.
   3. **Step 3: Configure rotation -
      optional**. Choose
      **Next**.
   4. **Step 4: Review**. Choose
      **Store**.

2. If your secret does not display immediately, select the refresh button.

Choose the name of your secret. Make note of the **Secret ARN**. 3. Repeat this process for each MediaURI that you want to stream from.

###### Note

The AWS network blocks some public RTSP sources. You cannot access these from within the Amazon EC2 instance or if you are running unmanaged while connected to the VPN.

###### Important

Your camera RTSP URL should stream video in h.264 format. The fragment duration must not exceed the limit mentioned in [Producer SDK quotas](limits.md#producer-sdk-limits "limits.md#producer-sdk-limits").

Amazon Kinesis Video Streams Edge Agent only supports video.

Run `gst-discoverer-1.0 `Your RtspUrl`` to make sure that your camera is reachable from your device.

Save the ARNs for all of the streams and secrets that you created. You need
these for the next step.
