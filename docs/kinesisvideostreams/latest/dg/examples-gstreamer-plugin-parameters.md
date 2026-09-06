

# GStreamer element parameter reference
<a name="examples-gstreamer-plugin-parameters"></a>

To send video to the Amazon Kinesis Video Streams producer C\+\+ SDK, you specify `kvssink` as the *sink*, or final destination of the pipeline. This reference provides information about `kvssink` required and optional parameters. For more information, see [Example: Kinesis Video Streams producer SDK GStreamer Plugin - kvssink](examples-gstreamer-plugin.md).

**Topics**
+ [Provide credentials to `kvssink`](#credentials-to-kvssink)
+ [Provide a region to `kvssink`](#kvssink-region)
+ [`kvssink` optional parameters](#kvssink-optional-parameters)

## Provide credentials to `kvssink`
<a name="credentials-to-kvssink"></a>

To allow the `kvssink` GStreamer element to make requests to AWS, provide AWS credentials for it to use when it calls the Amazon Kinesis Video Streams service. The credential provider chain looks for credentials in the following order:

### 1. AWS IoT credentials
<a name="collapsible-section-1"></a>

To set up AWS IoT credentials, see [Controlling access to Kinesis Video Streams resources using AWS IoT](how-iot.md).

The `iot-credentials` parameter value must start with `iot-certificate,` and be followed by a comma-separated list of the following {{key}}={{value}} pairs.



| Key | Required | Description | 
| --- | --- | --- | 
| ca-path | Yes | File path to the CA certificate used to establish trust with the backend service through TLS.**Example:** ` /{{file}}/{{path}}/{{to}}/certificate.pem` | 
| cert-path | Yes | File path to the X.509 certificate. **Example:** `/{{file}}/{{path}}/{{to}}/{{certificateID}}-certificate.pem.crt` | 
| endpoint | Yes | The AWS IoT Core credential endpoint provider endpoint for your AWS account. See the [AWS IoT Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html).**Example:** `{{credential-account-specific-prefix}}.credentials.iot.{{aws-region}}.amazonaws.com` | 
| key-path | Yes | File path to the private key used in the public/private key pair. **Example:** `/{{file}}/{{path}}/{{to}}/{{certificateID}}-private.pem.key` | 
| role-aliases | Yes | The name of the role alias pointing to the AWS IAM role to use when connecting to AWS IoT Core. **Example:** `{{KvsCameraIoTRoleAlias}}` | 
| iot-thing-name | No | The `iot-thing-name` is optional. If `iot-thing-name` is not provided, the `stream-name` parameter value is used.**Example:** `{{kvs_example_camera}}` | 

**Example**  
**Example:**  

```
gst-launch-1.0 -v ... ! kvssink stream-name="{{YourStream}}" aws-region="{{YourRegion}}" iot-certificate="iot-certificate,endpoint={{credential-account-specific-prefix}}.credentials.iot.{{aws-region}}.amazonaws.com,cert-path={{certificateID}}-certificate.pem.crt,key-path={{certificateID}}-private.pem.key,ca-path={{certificate}}.pem,role-aliases={{YourRoleAlias}},iot-thing-name={{YourThingName}}"
```

### 2. Environment variables
<a name="collapsible-section-2"></a>

To have `kvssink` use credentials from the environment, set the following environment variables:



| Environment Variable Name | Required | Description | 
| --- | --- | --- | 
| AWS\_ACCESS\_KEY\_ID | Yes | The AWS access key that's used to access Amazon Kinesis Video Streams. | 
| AWS\_SECRET\_ACCESS\_KEY | Yes | The AWS secret key associated with the access key. | 
| AWS\_SESSION\_TOKEN | No | Specifies the required session token value if you use temporary security credentials directly from AWS STS operations. | 

Setting the environment variable changes the value used until the end of your shell session, or until you set the variable to a different value. To make the variables persistent across future sessions, set them in your shell's startup script.

### 3. `access-key`, `secret-key` parameters
<a name="collapsible-section-3"></a>

To specify credentials directly as a `kvssink` parameter, set the following parameters:



| `kvssink` Parameter Name | Required | Description | 
| --- | --- | --- | 
| access-key | Yes | The AWS access key that's used to access Amazon Kinesis Video Streams. | 
| secret-key | Yes | The AWS secret key associated with the access key. | 
| session-token | No | Specifies the required session token value if you use temporary security credentials directly from AWS STS operations. | 

**Example**  
**Using static credentials:**  

```
gst-launch-1.0 -v ... ! kvssink stream-name="{{YourStream}}" aws-region="{{YourRegion}}" access-key="{{AKIDEXAMPLE}}" secret-key="{{SKEXAMPLE}}"
```

**Example**  
**Using temporary credentials:**  

```
gst-launch-1.0 -v ... ! kvssink stream-name="{{YourStream}}" aws-region="{{YourRegion}}" access-key="{{AKIDEXAMPLE}}" secret-key="{{SKEXAMPLE}}" session-token="{{STEXAMPLE}}"
```

### 4. Credential file
<a name="collapsible-section-4"></a>

**Important**  
If you've selected one of the previous methods, you can't use the `credential-path` `kvssink` parameter.



| `kvssink` Parameter Name | Required | Description | 
| --- | --- | --- | 
| credential-path | Yes | Path to the text file containing credentials in a specific format. | 

The text file must contain credentials in one of the following formats:
+ CREDENTIALS {{YourAccessKey}} {{YourSecretKey}}
+ CREDENTIALS {{YourAccessKey}} {{Expiration}} {{YourSecretKey}} {{SessionToken}}

**Example**  
**Example:** Your `{{credentials}}.txt` file is located at `/home/ubuntu` and contains the following:   
`CREDENTIALS {{AKIDEXAMPLE 2023-08-10T22:43:00Z SKEXAMPLE STEXAMPLE}}`  
To use it in `kvssink`, type:   

```
gst-launch-1.0 -v ... ! kvssink stream-name="{{YourStream}}" aws-region="{{YourRegion}}" credential-path="/home/ubuntu/{{credentials}}.txt" 
```
The expiration time should be at least 5 \+ 30 \+ 3 = **38** seconds in the future. The grace period is defined as the `IOT_CREDENTIAL_FETCH_GRACE_PERIOD` variable in [`IotCredentialProvider.h`](https://github.com/awslabs/amazon-kinesis-video-streams-producer-c/blob/master/src/source/Common/IotCredentialProvider.h). If the credentials are too close to the expiration when you start `kvssink`, you receive the error code `0x52000049 - STATUS_INVALID_TOKEN_EXPIRATION`.
`kvssink` doesn't modify the credentials file. If you're using temporary credentials, the credentials file must be updated by an outside source before the expiration time minus the grace period. 

## Provide a region to `kvssink`
<a name="kvssink-region"></a>

The following is the region lookup order:

1. `AWS_DEFAULT_REGION` environment variable is reviewed first. If it is set, that region is used to configure the client.

1. `aws-region` parameter is reviewed next. If it is set, that region is used to configure the client.

1. If neither of the previous methods were used, `kvssink` defaults to `us-west-2`. 

## `kvssink` optional parameters
<a name="kvssink-optional-parameters"></a>

The `kvssink` element has the following optional parameters. For more information about these parameters, see [Kinesis video stream structures](producer-reference-structures-stream.md).



| Parameter | Description | Unit/ Type | Default | 
| --- | --- | --- | --- | 
| stream-name  | The name of the destination Amazon Kinesis video stream.  If no stream-name is specified, the default stream name will be used: “DEFAULT\_STREAM“. If a stream with that default name does not already exist, it will be created.  |  |  | 
| absolute-fragment-times | Whether to use absolute fragment times. | Boolean | true | 
| access-key | The AWS access key that's used to access Kinesis Video Streams. <br />You must either have AWS credentials set or provide this parameter. To provide this information, type the following:<pre>export AWS_ACCESS_KEY_ID=</pre> |  |  | 
| avg-bandwidth-bps | The expected average bandwidth for the stream.  | Bits per second | 4194304 | 
| aws-region | The AWS Region to use. You can also provide the region with the `AWS_DEFAULT_REGION` environment variable. The environment variables take precedence if both the environment variable and kvssink parameters are set.  The region will default to `us-west-2` if not otherwise specified.  | String | "us-west-2" | 
| buffer-duration | The stream buffer duration.  | Seconds | 120 | 
| codec-id | The codec ID of the stream. | String | "V\_MPEG4/ISO/AVC" | 
| connection-staleness | The time after, which the stream staleness callback is called. | Seconds | 60 | 
| content-type | The content type of the stream. | String | "video/h264" | 
| fragment-acks | Whether to use fragment ACKs. | Boolean | true | 
| fragment-duration | The fragment duration that you want. | Milliseconds | 2000 | 
| framerate | The expected frame rate. | Frames per second | 25 | 
| frame-timecodes | Whether to use frame timecodes or generate timestamps using the current time callback.  | Boolean | true | 
| key-frame-fragmentation | Whether to produce fragments on a key frame. | Boolean | true | 
| log-config | The log configuration path. | String | "../kvs\_log\_configuration" | 
| max-latency | The maximum latency for the stream. | Seconds | 60 | 
| recalculate-metrics | Whether to recalculate the metrics. | Boolean | true | 
| replay-duration | The duration to roll the current reader backward to replay during an error if restarting is enabled. | Seconds | 40 | 
| restart-on-error | Whether to restart when an error occurs. | Boolean | true | 
| retention-period | The length of time the stream is preserved. | Hours | 2 | 
| rotation-period | The key rotation period. For more information, see [Rotating AWS KMS Keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html). | Seconds | 3600 | 
| secret-key | The AWS secret key that's used to access Kinesis Video Streams.<br />You must either have AWS credentials set or provide this parameter.<pre>export AWS_SECRET_ACCESS_KEY=</pre> |  |  | 
| session-token | Specifies the required session token value if you use temporary security credentials directly from AWS STS operations. |  |  | 
| storage-size | The device storage size in mebibyte (MiB). For information about configuring device storage, see [StorageInfo](producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo). | Mebibyte (MiB) | 128 | 
| streaming-type | The streaming type. Valid values include: +  0: real time <br />+  1: near real time (not currently supported) <br />+  2: offline  | Enum GstKvsSinkStreamingType | 0: real time | 
| timecode-scale | The MKV timecode scale. | Milliseconds | 1 | 
| track-name | The MKV track name. | String | "kinesis\_video" | 
| iot-certificate | AWS IoT credentials to be used in the `kvssink` element. <br />`iot-certificate` accepts the following keys and values:  The `iot-thing-name` is **optional**. If `iot-thing-name` is not provided, the `stream-name` parameter value is used. +  `endpoint`=`iotcredentialsproviderendpoint` <br />+  `cert-path`=`/localdirectorypath /to/certificate` <br />+  `key-path`=`/localdirectorypath /to/private/key` <br />+  `ca-path`=`/localdirectorypath/to/ca-cert` <br />+  `role-aliases`=`role-aliases` <br />+  `iot-thing-name`=`YourIotThingName`  | String | None | 