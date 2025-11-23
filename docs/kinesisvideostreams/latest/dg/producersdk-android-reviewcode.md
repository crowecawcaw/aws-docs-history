# Run and verify the code

To run the Android example application for the [Android producer library](producer-sdk-android.md "producer-sdk-android.md"), do
the following.

1. Connect to an Android device.
2. Choose **Run**, **Run...**, and choose
   **Edit configurations...**.
3. Choose the plus icon (**+**), **Android App**. In the
   **Name** field, enter `AmazonKinesisVideoDemoApp`. In the
   **Module** pulldown, choose **AmazonKinesisVideoDemoApp**. Choose
   **OK**.
4. Choose **Run**, **Run**.
5. In the **Select Deployment Target** screen, choose your
   connected device, and choose **OK**.
6. In the **AWSKinesisVideoDemoApp** application on the device,
   choose **Create new account**.
7. Enter values for **USERNAME**, **Password**,
   **Given name**, **Email address**, and
   **Phone number**, and then choose **Sign
   up**.

###### Note

These values have the following constraints:

    * **Password:** Must contain uppercase
     and lowercase letters, numbers, and special characters. You can
     change these constraints in your User pool page on the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
    * **Email address:** Must be a valid
     address so that you can receive a confirmation code.
    * **Phone number:** Must be in the following format:
     `+`<Country
     code>``<Number>``, for example,
     `+12065551212`.

8. Enter the code that you receive by email, and choose **Confirm**. Choose
   **Ok**.
9. On the next page, keep the default values, and choose **Stream**.
10. Sign in to the AWS Management Console and open the [Kinesis Video Streams console](https://console.aws.amazon.com//kinesisvideo/home/ "https://console.aws.amazon.com//kinesisvideo/home/") in the US West (Oregon) Region.

On the **Manage Streams** page, choose
**demo-stream**. 11. The streaming video plays in the embedded player. You might need to wait a
short time (up to ten seconds under typical bandwidth and processor conditions)
while the frames accumulate before the video appears.

###### Note

If the device's screen rotates (for example, from portrait to landscape),
the application stops streaming video.
The code example creates a stream. As the `MediaSource` in the code starts,
it begins sending frames from the camera to the `KinesisVideoClient`. The
client then sends the data to a Kinesis video stream named **demo-stream**.
