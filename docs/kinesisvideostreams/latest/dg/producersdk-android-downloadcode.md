# Download and configure the Android

producer library code

In this section of the Android producer library procedure, you download the Android
example code and open the project in Android Studio.

For prerequisites and other details about this example, see [Using the Android producer
library](producer-sdk-android.md "producer-sdk-android.md").

1. Create a directory, and then clone the AWS Mobile SDK for Android from the GitHub
   repository.

```
git clone https://github.com/awslabs/aws-sdk-android-samples
```

2. Open [Android
   Studio](https://developer.android.com/studio/index.html "https://developer.android.com/studio/index.html").
3. In the opening screen, choose **Open an existing Android Studio
   project**.
4. Navigate to the
   `aws-sdk-android-samples/AmazonKinesisVideoDemoApp`
   directory, and choose **OK**.
5. Open the
   `AmazonKinesisVideoDemoApp/src/main/res/raw/awsconfiguration.json`
   file.

In the `CredentialsProvider` node, provide the identity pool ID from the **To
set up an identity pool** procedure in the [Prerequisites](producer-sdk-android.md#producersdk-android-prerequisites "producer-sdk-android.md#producersdk-android-prerequisites")
section, and provide your AWS Region (for example, `us-west-2`).

In the `CognitoUserPool` node, provide the App client secret, App client ID, and Pool
ID from the **To set up a user pool** procedure in the [Prerequisites](producer-sdk-android.md#producersdk-android-prerequisites "producer-sdk-android.md#producersdk-android-prerequisites")
section, and provide your AWS Region (for example, `us-west-2`). 6. Your `awsconfiguration.json` file will look similar to the
following:

```
{
  "Version": "1.0",
  "CredentialsProvider": {
    "CognitoIdentity": {
      "Default": {
        "PoolId": "us-west-2:01234567-89ab-cdef-0123-456789abcdef",
        "Region": "us-west-2"
      }
    }
  },
  "IdentityManager": {
    "Default": {}
  },
  "CognitoUserPool": {
    "Default": {
      "AppClientSecret": "abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmno",
      "AppClientId": "0123456789abcdefghijklmnop",
      "PoolId": "us-west-2_qRsTuVwXy",
      "Region": "us-west-2"
    }
  }
}
```

7. Update the
   `AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/KinesisVideoDemoApp.java`
   with your Region (in the following sample, it’s set to **US_WEST_2**):

```

public class KinesisVideoDemoApp extends Application {
    public static final String TAG = KinesisVideoDemoApp.class.getSimpleName();
    public static Regions KINESIS_VIDEO_REGION = Regions.US_WEST_2;

```

For information about AWS Region constants, see [Regions](https://aws-amplify.github.io/aws-sdk-android/docs/reference/com/amazonaws/regions/Regions.html "https://aws-amplify.github.io/aws-sdk-android/docs/reference/com/amazonaws/regions/Regions.html").
