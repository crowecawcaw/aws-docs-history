# GStreamer element parameter

reference

To send video to the Amazon Kinesis Video Streams producer C++ SDK, you specify `kvssink`
as the _sink_, or final destination of the pipeline. This
reference provides information about `kvssink` required and optional
parameters. For more information, see [Example: Kinesis Video Streams producer SDK GStreamer
Plugin - kvssink](examples-gstreamer-plugin.md "examples-gstreamer-plugin.md").

**Topics**

- [Provide credentials to
  kvssink](#credentials-to-kvssink "#credentials-to-kvssink")
- [Provide a region to
  kvssink](#kvssink-region "#kvssink-region")
- [kvssink optional
  parameters](#kvssink-optional-parameters "#kvssink-optional-parameters")

## Provide credentials to

`kvssink`

To allow the `kvssink` GStreamer element to make requests to AWS,
provide AWS credentials for it to use when it calls the Amazon Kinesis Video Streams service.
The credential provider chain looks for credentials in the following
order:

To set up AWS IoT credentials, see [Controlling access to Kinesis Video Streams resources using AWS IoT](how-iot.md "how-iot.md").

The `iot-credentials` parameter value must start with
`iot-certificate,` and be followed by a comma-separated
list of the following
`key`=`value`
pairs.

| Key              | Required | Description                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ca-path`        | Yes      | File path to the CA certificate used to<br>establish trust with the backend service through<br>TLS.<br>Example**Example:**<br>`/`file`/`path`/`to`/certificate.pem`                                                                                                                                                                                         |
| `cert-path`      | Yes      | File path to the X.509 certificate.<br>Example**Example:**<br>`/`file`/`path`/`to`/`certificateID`-certificate.pem.crt`                                                                                                                                                                                                                                     |
| `endpoint`       | Yes      | The AWS IoT Core credential endpoint provider<br>endpoint for your AWS account. See the [AWS IoT Developer Guide](../../../iot/latest/developerguide/authorizing-direct-aws.md "../../../iot/latest/developerguide/authorizing-direct-aws.md").<br>Example**Example:**<br>``credential-account-specific-prefix`.credentials.iot.`aws-region`.amazonaws.com` |
| `key-path`       | Yes      | File path to the private key used in the<br>public/private key pair.<br>Example**Example:**<br>`/`file`/`path`/`to`/`certificateID`-private.pem.key`                                                                                                                                                                                                        |
| `role-aliases`   | Yes      | The name of the role alias pointing to the<br>AWS IAM role to use when connecting to<br>AWS IoT Core.<br>Example**Example:**<br>`KvsCameraIoTRoleAlias`                                                                                                                                                                                                     |
| `iot-thing-name` | No       | The `iot-thing-name` is optional. If<br>`iot-thing-name` is not provided, the<br>`stream-name` parameter value is<br>used.<br>Example**Example:**<br>`kvs_example_camera`                                                                                                                                                                                   |

###### Example

**Example:**

```
gst-launch-1.0 -v ... ! kvssink stream-name="`YourStream`" aws-region="`YourRegion`" iot-certificate="iot-certificate,endpoint=`credential-account-specific-prefix`.credentials.iot.`aws-region`.amazonaws.com,cert-path=`certificateID`-certificate.pem.crt,key-path=`certificateID`-private.pem.key,ca-path=`certificate`.pem,role-aliases=`YourRoleAlias`,iot-thing-name=`YourThingName`"
```

To have `kvssink` use credentials from the environment, set
the following environment variables:

| Environment Variable Name | Required | Description                                                                                                                  |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `AWS_ACCESS_KEY_ID`       | Yes      | The AWS access key that's used to access<br>Amazon Kinesis Video Streams.                                                    |
| `AWS_SECRET_ACCESS_KEY`   | Yes      | The AWS secret key associated with the access<br>key.                                                                        |
| `AWS_SESSION_TOKEN`       | No       | Specifies the required session token value if you use<br>temporary security credentials directly from AWS STS<br>operations. |

Setting the environment variable changes the value used until the end
of your shell session, or until you set the variable to a different
value. To make the variables persistent across future sessions, set them
in your shell's startup script.

To specify credentials directly as a `kvssink` parameter,
set the following parameters:

| `kvssink` Parameter Name | Required | Description                                                                                                                  |
| ------------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `access-key`             | Yes      | The AWS access key that's used to access<br>Amazon Kinesis Video Streams.                                                    |
| `secret-key`             | Yes      | The AWS secret key associated with the access<br>key.                                                                        |
| `session-token`          | No       | Specifies the required session token value if you use<br>temporary security credentials directly from AWS STS<br>operations. |

###### Example

**Using static credentials:**

```
gst-launch-1.0 -v ... ! kvssink stream-name="`YourStream`" aws-region="`YourRegion`" access-key="`AKIDEXAMPLE`" secret-key="`SKEXAMPLE`"
```

###### Example

**Using temporary
credentials:**

```
gst-launch-1.0 -v ... ! kvssink stream-name="`YourStream`" aws-region="`YourRegion`" access-key="`AKIDEXAMPLE`" secret-key="`SKEXAMPLE`" session-token="`STEXAMPLE`"
```

###### Important

If you've selected one of the previous methods, you can't use the
`credential-path`
`kvssink` parameter.

| `kvssink` Parameter Name | Required | Description                                                           |
| ------------------------ | -------- | --------------------------------------------------------------------- |
| `credential-path`        | Yes      | Path to the text file containing credentials in a<br>specific format. |

The text file must contain credentials in one of the following
formats:

- CREDENTIALS `YourAccessKey`
  `YourSecretKey`
- CREDENTIALS `YourAccessKey`
  `Expiration`
  `YourSecretKey`
  `SessionToken`

###### Example

**Example:** Your
``credentials`.txt`file
 is located at`/home/ubuntu` and contains the following:

`CREDENTIALS `AKIDEXAMPLE 2023-08-10T22:43:00Z
SKEXAMPLE STEXAMPLE``

To use it in `kvssink`, type:

```
gst-launch-1.0 -v ... ! kvssink stream-name="`YourStream`" aws-region="`YourRegion`" credential-path="/home/ubuntu/`credentials`.txt"
```

###### Note

The expiration time should be at least 5 + 30 + 3 = **38** seconds in the future. The grace period is
defined as the `IOT_CREDENTIAL_FETCH_GRACE_PERIOD`
variable in [`IotCredentialProvider.h`](https://github.com/awslabs/amazon-kinesis-video-streams-producer-c/blob/master/src/source/Common/IotCredentialProvider.h "https://github.com/awslabs/amazon-kinesis-video-streams-producer-c/blob/master/src/source/Common/IotCredentialProvider.h"). If the
credentials are too close to the expiration when you start
`kvssink`, you receive the error code
`0x52000049 -
 STATUS_INVALID_TOKEN_EXPIRATION`.

###### Important

`kvssink` doesn't modify the credentials file. If
you're using temporary credentials, the credentials file must be
updated by an outside source before the expiration time minus
the grace period.

## Provide a region to

`kvssink`

The following is the region lookup order:

1. `AWS_DEFAULT_REGION` environment variable is reviewed
   first. If it is set, that region is used to configure the
   client.
2. `aws-region` parameter is reviewed next. If it is set,
   that region is used to configure the client.
3. If neither of the previous methods were used, `kvssink` defaults to `us-west-2`.

## `kvssink` optional

parameters

The `kvssink` element has the following optional parameters. For
more information about these parameters, see [Kinesis video stream structures](producer-reference-structures-stream.md "producer-reference-structures-stream.md").

| Parameter                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Unit/ Type                     | Default                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ---------------------------- |
| `stream-name`             | The name of the destination Amazon Kinesis video stream. ImportantIf no stream-name is specified, the default stream<br>name will be used: “DEFAULT_STREAM“. If a stream with<br>that default name does not already exist, it will be<br>created.                                                                                                                                                                                                                                                                                                                |                                |                              |
| `absolute-fragment-times` | Whether to use absolute fragment times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Boolean                        | true                         |
| `access-key`              | The AWS access key that's used to access Kinesis Video Streams.<br>You must either have AWS credentials set or provide this<br>parameter. To provide this information, type the<br>following:<br>`<br>export AWS_ACCESS_KEY_ID=<br>`                                                                                                                                                                                                                                                                                                                             |                                |                              |
| `avg-bandwidth-bps`       | The expected average bandwidth for the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Bits per second                | 4194304                      |
| `aws-region`              | The AWS Region to use.<br>NoteYou can also provide the region with the<br>`AWS_DEFAULT_REGION` environment<br>variable. The environment variables take precedence if<br>both the environment variable and kvssink parameters are<br>set.<br>ImportantThe region will default to `us-west-2` if<br>not otherwise specified.                                                                                                                                                                                                                                       | String                         | `"us-west-2"`                |
| `buffer-duration`         | The stream buffer duration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Seconds                        | 120                          |
| `codec-id`                | The codec ID of the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String                         | `"V_MPEG4/ISO/AVC"`          |
| `connection-staleness`    | The time after, which the stream staleness callback is<br>called.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Seconds                        | 60                           |
| `content-type`            | The content type of the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String                         | `"video/h264"`               |
| `fragment-acks`           | Whether to use fragment ACKs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean                        | true                         |
| `fragment-duration`       | The fragment duration that you want.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Milliseconds                   | 2000                         |
| `framerate`               | The expected frame rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Frames per second              | 25                           |
| `frame-timecodes`         | Whether to use frame timecodes or generate timestamps using<br>the current time callback.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Boolean                        | true                         |
| `key-frame-fragmentation` | Whether to produce fragments on a key frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean                        | true                         |
| `log-config`              | The log configuration path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String                         | `"../kvs_log_configuration"` |
| `max-latency`             | The maximum latency for the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Seconds                        | 60                           |
| `recalculate-metrics`     | Whether to recalculate the metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean                        | true                         |
| `replay-duration`         | The duration to roll the current reader backward to replay<br>during an error if restarting is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Seconds                        | 40                           |
| `restart-on-error`        | Whether to restart when an error occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean                        | true                         |
| `retention-period`        | The length of time the stream is preserved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Hours                          | 2                            |
| `rotation-period`         | The key rotation period. For more information, see [Rotating AWS KMS<br>Keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").                                                                                                                                                                                                                                                                                                                                                                            | Seconds                        | 3600                         |
| `secret-key`              | The AWS secret key that's used to access Kinesis Video Streams.<br>You must either have AWS credentials set or provide this<br>parameter.<br>`<br>export AWS_SECRET_ACCESS_KEY=<br>`                                                                                                                                                                                                                                                                                                                                                                             |                                |                              |
| `session-token`           | Specifies the required session token value if you use<br>temporary security credentials directly from AWS STS<br>operations.                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                |                              |
| `storage-size`            | The device storage size in mebibyte (MiB). For information<br>about configuring device storage, see [StorageInfo](producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo "producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo").                                                                                                                                                                                                                                                  | Mebibyte (MiB)                 | 128                          |
| `streaming-type`          | The streaming type. Valid values include:<br>• 0: real time<br>• 1: near real time (not currently supported)<br>• 2: offline                                                                                                                                                                                                                                                                                                                                                                                                                                     | Enum `GstKvsSinkStreamingType` | 0: real time                 |
| `timecode-scale`          | The MKV timecode scale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Milliseconds                   | 1                            |
| `track-name`              | The MKV track name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String                         | `"kinesis_video"`            |
| `iot-certificate`         | AWS IoT credentials to be used in the<br>`kvssink` element.<br>`iot-certificate` accepts the following keys<br>and values:<br>NoteThe `iot-thing-name` is **optional**. If<br>`iot-thing-name` is not provided, the<br>`stream-name` parameter value is<br>used.<br>• `endpoint`=`iotcredentialsproviderendpoint`<br>• `cert-path`=`/localdirectorypath<br>/to/certificate`<br>• `key-path`=`/localdirectorypath<br>/to/private/key`<br>• `ca-path`=`/localdirectorypath/to/ca-cert`<br>• `role-aliases`=`role-aliases`<br>• `iot-thing-name`=`YourIotThingName` | String                         | None                         |
