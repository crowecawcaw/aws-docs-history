# Controlling access to Kinesis Video Streams resources using AWS IoT

This section describes how to enable a device (for example, a camera) to send audio and video data to one
particular Kinesis video stream only. You can do this by using the AWS IoT credentials provider and an AWS Identity and Access Management (IAM)
role.

Devices can use X.509 certificates to connect to AWS IoT using TLS mutual authentication protocols. Other
AWS services (for example, Kinesis Video Streams) don't support certificate-based authentication, but can be called using AWS
credentials in AWS Signature Version 4 format. The Signature Version 4 algorithm typically requires the caller to
have an access key ID and a secret access key. AWS IoT has a credentials provider that allows you to use the built-in
X.509 certificate as the unique device identity to authenticate AWS requests (for example, requests to Kinesis Video Streams).
This removes the need to store an access key ID and a secret access key on your device.

The credentials provider authenticates a client (in this case, a Kinesis Video Streams SDK that's running on the camera that
you want to send data to a video stream) using an X.509 certificate and issues a temporary, limited-privilege
security token. You can use the token to sign and authenticate any AWS request (in this case, a call to the
Kinesis Video Streams). For more information, see [Authorizing Direct Calls
to AWS Services](../../../iot/latest/developerguide/authorizing-direct-aws.md "../../../iot/latest/developerguide/authorizing-direct-aws.md").

This way of authenticating your camera's requests to Kinesis Video Streams requires you to create and configure an IAM role
and attach appropriate IAM policies to the role so that the AWS IoT credentials provider can assume the role on your
behalf.

For more information about AWS IoT, see [AWS IoT Core
Documentation](../../../iot.md "../../../iot.md"). For more information about IAM, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/").

###### Topics

- [AWS IoT ThingName as stream name](#how-iot-thingnamestreamname "#how-iot-thingnamestreamname")
- [AWS IoT CertificateId as stream name](#how-iot-iotcertstreamname "#how-iot-iotcertstreamname")
- [Use AWS IoT credentials to stream to a hard-coded stream name](#how-iot-hard-coded-stream "#how-iot-hard-coded-stream")

## AWS IoT ThingName as stream name

###### Topics

- [Step 1: Create an AWS IoT thing type and an AWS IoT thing](#how-iot-create-thing-type "#how-iot-create-thing-type")
- [Step 2: Create an IAM role to be assumed by AWS IoT](#how-iot-add-iot-policy "#how-iot-add-iot-policy")
- [Step 3: Create and configure the X.509 certificate](#how-iot-create-cert-keys "#how-iot-create-cert-keys")
- [Step 4: Test the AWS IoT credentials with your Kinesis video stream](#how-iot-test-it "#how-iot-test-it")
- [Step 5: Deploying AWS IoT certificates and credentials on your camera's
  file system and streaming data to your video stream](#how-iot-deploy "#how-iot-deploy")

### Step 1: Create an AWS IoT thing type and an AWS IoT thing

In AWS IoT, a thing is a representation of a specific device or logical entity. In this case, an AWS IoT thing
represents your Kinesis video stream that you want to configure resource-level access control. In order to create a thing,
first, you must create an AWS IoT thing type. You can use AWS IoT thing types to store description and configuration
information that's common to all things associated with the same thing type.

1. The following example command creates a thing type
   `kvs_example_camera`:

```
aws --profile default iot create-thing-type --thing-type-name kvs_example_camera > iot-thing-type.json
```

2. This example command creates the `kvs_example_camera_stream` thing of the
   `kvs_example_camera` thing type:

```
aws --profile default  iot create-thing --thing-name kvs_example_camera_stream --thing-type-name kvs_example_camera > iot-thing.json
```

### Step 2: Create an IAM role to be assumed by AWS IoT

IAM roles are similar to users, in that a role is an AWS identity with permissions policies that
determine what the identity can and can't do in AWS. A role can be assumed by anyone who needs it. When you
assume a role, it provides you with temporary security credentials for your role session.

The role that you create in this step can be assumed by AWS IoT to obtain temporary credentials from the
security token service (STS) when performing credential authorization requests from the client. In this case,
the client is the Kinesis Video Streams SDK that's running on your camera.

Perform the following steps to create and configure this IAM role:

1. Create an IAM role.

The following example command creates an IAM role called
`KVSCameraCertificateBasedIAMRole`:

```
aws --profile default iam create-role --role-name KVSCameraCertificateBasedIAMRole --assume-role-policy-document 'file://iam-policy-document.json' > iam-role.json
```

You can use the following trust policy JSON for the
`iam-policy-document.json`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.iot.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Next, attach a permissions policy to the IAM role that you previously created. This
   permissions policy allows selective access control (a subset of supported operations) for an AWS resource.
   In this case, the AWS resource is the video stream that you want your camera to send data. In other words,
   once all the configuration steps are complete, this camera will be able to send data only to this video
   stream.

```
aws --profile default iam put-role-policy --role-name KVSCameraCertificateBasedIAMRole --policy-name KVSCameraIAMPolicy --policy-document 'file://iam-permission-document.json'
```

You can use the following IAM policy JSON for the
`iam-permission-document.json`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:DescribeStream",
 "kinesisvideo:PutMedia",
 "kinesisvideo:TagStream",
 "kinesisvideo:GetDataEndpoint"
 ],
 "Resource": "arn:aws:kinesisvideo:*:*:stream/${credentials-iot:ThingName}/*"
 }
 ]
}`

```

Note that this policy authorizes the specified actions only on a video
stream (AWS resource) that is specified by the placeholder
`(${credentials-iot:ThingName})`. This placeholder takes on
the value of the AWS IoT thing attribute `ThingName` when the AWS IoT
credentials provider sends the video stream name in the
request. 3. Next, create a Role Alias for your IAM role. Role alias is an alternate data model that
points to the IAM role. An AWS IoT credentials provider request must include a role-alias to indicate which
IAM role to assume to obtain the temporary credentials from the STS.

The following sample command creates a role alias called
`KvsCameraIoTRoleAlias`,

```
aws --profile default iot create-role-alias --role-alias KvsCameraIoTRoleAlias --role-arn $(jq --raw-output '.Role.Arn' iam-role.json) --credential-duration-seconds 3600 > iot-role-alias.json
```

4. Now you can create the policy that will enable AWS IoT to assume role with the
   certificate (once it is attached) using the role alias.

The following sample command creates a policy for AWS IoT called
`KvsCameraIoTPolicy`.

```
aws --profile default iot create-policy --policy-name KvsCameraIoTPolicy --policy-document 'file://iot-policy-document.json'
```

You can use the following command to create the
`iot-policy-document.json` document JSON:

```
cat > iot-policy-document.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iot:AssumeRoleWithCertificate"
            ],
            "Resource": "$(jq --raw-output '.roleAliasArn' iot-role-alias.json)"
        }
    ]
}
EOF
```

### Step 3: Create and configure the X.509 certificate

Communication between a device (your video stream) and AWS IoT is protected
through the use of X.509 certificates.

1. Create the certificate to which you must attach the policy for AWS IoT that you previously
   created.

```
aws --profile default iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem --public-key-outfile public.pem.key --private-key-outfile private.pem.key > certificate
```

2. Attach the policy for AWS IoT (`KvsCameraIoTPolicy` created previously) to this
   certificate.

```
aws --profile default iot attach-policy --policy-name KvsCameraIoTPolicy --target $(jq --raw-output '.certificateArn' certificate)
```

3. Attach your AWS IoT thing (`kvs_example_camera_stream`) to the
   certificate you just created:

```
aws --profile default iot attach-thing-principal --thing-name kvs_example_camera_stream --principal $(jq --raw-output '.certificateArn' certificate)
```

4. To authorize requests through the AWS IoT credentials provider, you need the AWS IoT credentials
   endpoint, which is unique to your AWS account ID. You can use the following command to get the AWS IoT credentials endpoint.

```
aws --profile default iot describe-endpoint --endpoint-type iot:CredentialProvider --output text > iot-credential-provider.txt
```

5. In addition to the X.509 certificate created previously, you must also have a CA certificate
   to establish trust with the backend service through TLS. You can get the CA certificate using the following
   command:

```
curl --silent 'https://www.amazontrust.com/repository/SFSRootCAG2.pem' --output cacert.pem
```

### Step 4: Test the AWS IoT credentials with your Kinesis video stream

Now you can test the AWS IoT credentials that you've set up so far.

1. First, create a Kinesis video stream that you want to test this
   configuration with.

###### Important

Create a video stream with a name that is identical to the AWS IoT thing
name that you created in the previous step
(`kvs_example_camera_stream`).

```
aws kinesisvideo create-stream --data-retention-in-hours 24 --stream-name kvs_example_camera_stream
```

2. Next, call the AWS IoT credentials provider to get the temporary
   credentials:

```
curl --silent -H "x-amzn-iot-thingname:kvs_example_camera_stream" --cert certificate.pem --key private.pem.key https://IOT_GET_CREDENTIAL_ENDPOINT/role-aliases/KvsCameraIoTRoleAlias/credentials --cacert ./cacert.pem > token.json
```

###### Note

You can use the following command to get the `IOT_GET_CREDENTIAL_ENDPOINT`:

```
IOT_GET_CREDENTIAL_ENDPOINT=`cat iot-credential-provider.txt`
```

The output JSON contains the `accessKey`,
`secretKey`, and the `sessionToken`, which you can
use to access the Kinesis Video Streams. 3. For your test, you can use these credentials to invoke the Kinesis Video Streams
`DescribeStream` API for the sample
`kvs_example_camera_stream` video stream.

```
AWS_ACCESS_KEY_ID=$(jq --raw-output '.credentials.accessKeyId' token.json) AWS_SECRET_ACCESS_KEY=$(jq --raw-output '.credentials.secretAccessKey' token.json) AWS_SESSION_TOKEN=$(jq --raw-output '.credentials.sessionToken' token.json) aws kinesisvideo describe-stream --stream-name kvs_example_camera_stream
```

### Step 5: Deploying AWS IoT certificates and credentials on your camera's

file system and streaming data to your video stream

###### Note

The steps in this section describe sending media to a Kinesis video stream from a camera that's using the
[Use the C++ producer library](producer-sdk-cpp.md "producer-sdk-cpp.md").

1. Copy the X.509 certificate, the private key, and the CA certificate generated in the previous
   steps to your camera's file system. Specify the paths for where these files are stored, the role alias name,
   and the AWS IoT credentials endpoint for running the `gst-launch-1.0` command or your sample application.
2. The following sample command uses AWS IoT certificate authorization to send video to Kinesis Video Streams:

```
gst-launch-1.0 rtspsrc location=rtsp://`YourCameraRtspUrl` short-header=TRUE ! rtph264depay ! video/x-h264,format=avc,alignment=au ! h264parse ! kvssink stream-name="kvs_example_camera_stream" aws-region="`YourAWSRegion`" iot-certificate="iot-certificate,endpoint=`credential-account-specific-prefix`.credentials.iot.`aws-region`.amazonaws.com,cert-path=/path/to/certificate.pem,key-path=/path/to/private.pem.key,ca-path=`/path/to/cacert.pem`,role-aliases=KvsCameraIoTRoleAlias"
```

## AWS IoT CertificateId as stream name

To represent your device (for example, your camera) through an AWS IoT thing, but authorize a different stream
name, then you can use the AWS IoT `certificateId` attribute as your stream name and provide Kinesis Video Streams
permissions on the stream using AWS IoT. The steps for accomplishing this are similar to the ones previously outlined,
with a few changes.

- Modify the permissions policy to your IAM role (`iam-permission-document.json`)
  as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:DescribeStream",
 "kinesisvideo:PutMedia",
 "kinesisvideo:TagStream",
 "kinesisvideo:GetDataEndpoint"
 ],
 "Resource": "arn:aws:kinesisvideo:*:*:stream/${credentials-iot:AwsCertificateId}/*"
 }
 ]
}`

```

###### Note

The resource ARN uses certificate ID as the placeholder for the stream name. The IAM
permission will work when you use the certificate ID as the stream name. Get the certificate ID from the
certificate so that you can use that as stream name in the following describe stream API call.

```
export CERTIFICATE_ID=`cat certificate | jq --raw-output '.certificateId'`
```

- Verify this change using the Kinesis Video Streams describe-stream CLI command:

```
AWS_ACCESS_KEY_ID=$(jq --raw-output '.credentials.accessKeyId' token.json) AWS_SECRET_ACCESS_KEY=$(jq --raw-output '.credentials.secretAccessKey' token.json) AWS_SESSION_TOKEN=$(jq --raw-output '.credentials.sessionToken' token.json) aws kinesisvideo describe-stream --stream-name ${CERTIFICATE_ID}
```

- Pass the certificateId to the AWS IoT credentials provider in the [sample application](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/samples/kvs_gstreamer_sample.cpp "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/samples/kvs_gstreamer_sample.cpp") in the Kinesis Video Streams C++ SDK:

```
credential_provider = make_unique<IotCertCredentialProvider>(iot_get_credential_endpoint,
        cert_path,
        private_key_path,
        role_alias,
        ca_cert_path,
        certificateId);
```

###### Note

Note that you're passing the `thingname` to the AWS IoT
credentials provider. You can use `getenv` to pass the thingname
to the demo application similar to passing the other AWS IoT attributes. Use
the certificate ID as the stream name in the command line parameters when
you are running the sample application.

## Use AWS IoT credentials to stream to a hard-coded stream name

To represent your device (for example, your camera) through an AWS IoT thing, but authorize
streaming to a specific Amazon Kinesis video stream, provide Amazon Kinesis Video Streams permissions on the stream
using AWS IoT. The process is similar to the previous sections, with a few changes.

Modify the permissions policy to your IAM role (`iam-permission-document.json`) as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:DescribeStream",
 "kinesisvideo:PutMedia",
 "kinesisvideo:TagStream",
 "kinesisvideo:GetDataEndpoint"
 ],
 "Resource": "arn:aws:kinesisvideo:*:*:stream/`YourStreamName`/*"
 }
 ]
}`

```

Copy the X.509 certificate, private key, and CA certificate generated in the previous
steps to your camera's file system.

Specify the paths for where these files are stored, the role alias name, the AWS IoT thing
name, and the AWS IoT credentials endpoint for running the `gst-launch-1.0` command or your
sample application.

The following sample command uses AWS IoT certificate authorization to send video to Amazon Kinesis Video Streams:

```
gst-launch-1.0 rtspsrc location=rtsp://`YourCameraRtspUrl` short-header=TRUE ! rtph264depay ! video/x-h264,format=avc,alignment=au ! h264parse ! kvssink stream-name="`YourStreamName`" aws-region="`YourAWSRegion`" iot-certificate="iot-certificate,endpoint=`credential-account-specific-prefix`.credentials.iot.`aws-region`.amazonaws.com,cert-path=/path/to/certificate.pem,key-path=/path/to/private.pem.key,ca-path=`/path/to/cacert.pem`,role-aliases=KvsCameraIoTRoleAlias,iot-thing-name=`YourThingName`"
```
