Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Working with S3 buckets with Amazon S3 compatible storage on Snowball Edge

With Amazon S3 compatible storage on Snowball Edge, you can create Amazon S3 buckets on your Snowball Edge devices to store and
retrieve objects on premises for applications that require local data access, local data
processing, and data residency. Amazon S3 compatible storage on Snowball Edge provides a new storage class, `SNOW`,
which uses the Amazon S3 APIs, and is designed to store data durably and
redundantly across multiple Snowball Edge devices. You can use the same APIs and
features on Snowball Edge buckets that you do on Amazon S3, including bucket lifecycle policies,
encryption, and tagging.

You can use Amazon S3 compatible storage on Snowball Edge using the
AWS Command Line Interface (AWS CLI) or programatically through the AWS Java SDK. With the AWS CLI, you can set up an s3api or s3control endpoint and interact with it through commands. We recommend using the s3api endpoint because the same endpoint can be used for bucket and object operations.

###### Note

The s3api endpoint is available for version 8004 and newer of the Snowball Edge software. To find the version of the Snowball Edge software installed on a device, use the `snowballEdge check-for-updates` command. To update a Snowball Edge device, see [Updating software on Snowball Edge devices](updating-device.md "updating-device.md").

## Using the AWS CLI

Follow these instructions to work with Amazon S3 buckets on your device
using the AWS CLI.

###### To set up the AWS CLI

1. Create a profile for object endpoints in
   `~/.aws/config`.

```
[profile `your-profile`]
aws_access_key_id = `your-access-id`
aws_secret_access_key = `your-access-key`
region = snow
ca_bundle = dev/apps/ca-certs/`your-ca_bundle`

```

2. Obtain a certificate from your device. For information, see the
   _[Snowball Edge Developer Guide](using-client-commands.md#snowball-edge-certificates-cli "using-client-commands.md#snowball-edge-certificates-cli")_.
3. If you installed the SDK in a virtual environment, activate it using the
   following command:

```
source `your-virtual-environment-name`/bin/activate
```

After you set up your operations, you can use the s3api SDK or s3control SDK to access S3 buckets on Snowball Edge with the
AWS CLI.

###### Example of accessing S3 bucket using the s3api SDK

```

aws s3api list-buckets --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`

```

###### Example of accessing S3 buckets using the s3control SDK

```

aws s3control list-regional-buckets --account-id `bucket-owner` --endpoint-url https://`s3ctrlapi-endpoint-ip` --profile `your-profile`

```

###### Example of accessing S3 objects using the s3api SDK

```

aws s3api list-objects-v2 --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`

```

## Using the Java SDK

Use the following example to work with Amazon S3 buckets and objects using the Java SDK.

```

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.http.SdkHttpClient;bg
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;

import java.net.URI;

AwsBasicCredentials creds = AwsBasicCredentials.create(accessKey, secretKey); // set creds by getting Access Key and Secret Key from snowball edge
SdkHttpClient httpClient = ApacheHttpClient.builder().tlsTrustManagersProvider(trustManagersProvider).build(); // set trust managers provider with client certificate from snowball edge
String s3SnowEndpoint = "10.0.0.0"; // set s3-snow object api endpoint from describe service

S3Client s3Client = S3Client.builder().httpClient(httpClient).region(Region.of("snow")).endpointOverride(new URI(s3SnowEndpoint)).credentialsProvider(StaticCredentialsProvider.create(creds)).build();

```

## Bucket ARN format

You can use the Amazon Resource Name (ARN) format listed here to identify an
Amazon S3 bucket on a Snowball Edge device:

```
arn:`partition`:s3:snow:`account-id`:`device`/`device-id`/bucket/`bucket-name`
```

Where `partition` is the partition of the Region where
you ordered your Snowball Edge device. `device-id` is the
job_id if the device is a standalone Snowball Edge device, or the
`cluster_id` if you have a Snowball Edge
cluster.

## Bucket location format

The bucket location format specifies the Snowball Edge device where the bucket will be created. The bucket location has the following format:

```
/device-id/bucket/bucket-name
```

For more information, see [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/s3api/create-bucket.html") in the AWS CLI Command Reference.
