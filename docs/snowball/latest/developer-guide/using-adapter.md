Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Transferring files using the Amazon S3 adapter for data migration to or from Snowball Edge

Following is an overview of the Amazon S3 adapter, which you can use to transfer data
programmatically to and from S3 buckets already on the AWS Snowball Edge device using Amazon S3 REST API actions. This Amazon S3 REST
API support is limited to a subset of actions. You can use this subset of actions with one
of the AWS SDKs to transfer data programmatically. You can also use the subset of supported
AWS Command Line Interface (AWS CLI) commands for Amazon S3 to transfer data programmatically.

If your solution uses the AWS SDK for Java version 1.11.0 or newer, you must use the following
`S3ClientOptions`:

- `disableChunkedEncoding()` – Indicates that chunked encoding is
  not supported with the interface.
- `setPathStyleAccess(true)` – Configures the interface to use
  path-style access for all requests.
  For more information, see [Class S3ClientOptions.Builder](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/S3ClientOptions.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/S3ClientOptions.md") in the _Amazon AppStream SDK for Java_.

###### Important

We recommend that you use only one method at a time to read and write data to a local
bucket on an AWS Snowball Edge device. Using both the NFS interface and the Amazon S3 adapter on the same bucket at
the same time can result in read/write conflicts.

[AWS Snowball Edge quotas](limits.md "limits.md") details the limits.

For AWS services to work properly on a Snowball Edge, you must allow the ports
for the services. For details, see [Port requirements for AWS services on a Snowball Edge](port-requirements.md "port-requirements.md").

###### Topics

- [Downloading and installing the AWS CLI version
  1.16.14 for use with the Amazon S3 adapter](#aws-cli-version "#aws-cli-version")
- [Using the AWS CLI and API operations on Snowball Edge devices](#using-adapter-cli-specify-region "#using-adapter-cli-specify-region")
- [Getting and using local Amazon S3 credentials on Snowball Edge](#adapter-credentials "#adapter-credentials")
- [Unsupported Amazon S3 features for the Amazon S3 adapter on Snowball Edge](#snowball-edge-s3-unsupported-features "#snowball-edge-s3-unsupported-features")
- [Batching small files to improve data transfer performance to Snowball Edge](batching-small-files.md "batching-small-files.md")
- [Supported AWS CLI commands for data transfer to or from Snowball Edge](using-adapter-cli.md "using-adapter-cli.md")
- [Supported Amazon S3 REST API actions on Snowball Edge for data transfer](using-adapter-supported-api.md "using-adapter-supported-api.md")

## Downloading and installing the AWS CLI version

1.16.14 for use with the Amazon S3 adapter

Currently, Snowball Edge devices support only version 1.16.14 and earlier of the
AWS CLI for use with the Amazon S3 adapter. Newer versions of the AWS CLI are not compatible with the Amazon S3 adapter because they do not support all of the functionality of the S3 adapter.

###### Note

If you are using Amazon S3 compatible storage on Snowball Edge, you can use the latest version of the AWS CLI. To download and use the latest version, see [AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

### Install the AWS CLI on Linux operating systems

Run this chained command:

```

curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-1.16.14.zip" -o "awscli-bundle.zip";unzip awscli-bundle.zip;sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws;/usr/local/bin/aws --version;

```

### Install the AWS CLI on Windows operating systems

Download and run the installer file for your operating system:

- [32‐bit installer bundled with Python 2](https://s3.amazonaws.com/aws-cli/AWSCLI32-1.16.14.msi "https://s3.amazonaws.com/aws-cli/AWSCLI32-1.16.14.msi")
- [32‐bit installer bundled with Python 3](https://s3.amazonaws.com/aws-cli/AWSCLI32PY3-1.16.14.msi "https://s3.amazonaws.com/aws-cli/AWSCLI32PY3-1.16.14.msi")
- [64‐bit installer bundled with Python 2](https://s3.amazonaws.com/aws-cli/AWSCLI64-1.16.14.msi "https://s3.amazonaws.com/aws-cli/AWSCLI64-1.16.14.msi")
- [64‐bit installer bundled with Python 3](https://s3.amazonaws.com/aws-cli/AWSCLI64PY3-1.16.14.msi "https://s3.amazonaws.com/aws-cli/AWSCLI64PY3-1.16.14.msi")
- [Setup file including 32‐ and 64‐bit installers that will automatically install the correct version](https://s3.amazonaws.com/aws-cli/AWSCLISetup-1.16.14.exe "https://s3.amazonaws.com/aws-cli/AWSCLISetup-1.16.14.exe")

## Using the AWS CLI and API operations on Snowball Edge devices

When using the AWS CLI or API operations to issue IAM, Amazon S3, and Amazon EC2 commands on
Snowball Edge, you must specify the Region as "`snow`." You can do this
using `AWS configure` or within the command itself, as in the
following examples.

```
aws configure --profile abc
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: 1234567
Default region name [None]: snow
Default output format [None]: json
```

Or

```
aws s3 ls  --endpoint http://192.0.2.0:8080 --region snow --profile snowballEdge
```

### Authorization with the Amazon S3 API interface for

AWS Snowball Edge

When you use the Amazon S3 adapter, every interaction is signed with the AWS Signature Version 4
algorithm by default. This authorization is used only to verify the data traveling from its
source to the interface. All encryption and decryption happens on the device. Unencrypted data
is never stored on the device.

When using the interface, keep the following in mind:

- To get the local Amazon S3 credentials to sign your requests to the
  AWS Snowball Edge device, run the `snowballEdge list-access-keys` and
  `snowballEdge get-secret-access-keys` Snowball Edge client
  commands. For more information, see [Configuring and using the Snowball Edge Client](using-client-commands.md "using-client-commands.md"). These local Amazon S3 credentials include a
  pair of keys: an access key and a secret key. These keys are only valid for
  the devices associated with your job. They can't be used in the AWS Cloud because they have no AWS Identity and Access Management (IAM)
  counterpart.
- The encryption key is not changed by what AWS credentials you use. Signing with the
  Signature Version 4 algorithm is only used to verify the data traveling from its source
  to the interface. Thus, this signing never factors into the encryption keys used to
  encrypt your data on the Snowball.

## Getting and using local Amazon S3 credentials on Snowball Edge

Every interaction with a Snowball Edge is signed with the AWS Signature Version 4
algorithm. For more information about the algorithm, see [Signature Version 4 Signing
Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS General Reference_.

You can get the local Amazon S3 credentials to sign your requests to the Snowball Edge
client Edge device by running the `snowballEdge list-access-keys` and
`snowballEdge get-secret-access-key` Snowball Edge client information,
see [Getting credentials for a Snowball Edge](using-client-commands.md#client-credentials "using-client-commands.md#client-credentials"). These local
Amazon S3 credentials include a pair of keys: an access key ID and a secret key. These
credentials are only valid for the devices that are associated with your job. They can't
be used in the AWS Cloud because they have no IAM counterpart.

You can add these credentials to the AWS credentials file on your server. The default
credential profiles file is typically located at `~/.aws/credentials`, but
the location can vary per platform. This file is shared by many of the AWS SDKs and by
the AWS CLI. You can save local credentials with a profile name as in the following
example.

```
[snowballEdge]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### Configuring the AWS CLI to use the S3 adapter on a Snowball Edge as the endpoint

When you use the AWS CLI to issue a command to the AWS Snowball Edge device, you specify that
the endpoint is the Amazon S3 adapter. You have the choice of using the HTTPS endpoint, or
an unsecured HTTP endpoint, as shown following.

**HTTPS secured endpoint**

```
aws s3 ls --endpoint https://192.0.2.0:8443 --ca-bundle `path/to/certificate` --profile snowballEdge
```

**HTTP unsecured endpoint**

```
aws s3 ls --endpoint http://192.0.2.0:8080 --profile snowballEdge
```

If you use the HTTPS endpoint of `8443`, your data is securely
transferred from your server to the Snowball Edge. This encryption is ensured with
a certificate that's generated by the Snowball Edge when it gets a new IP
address. After you have your certificate, you can save it to a local
`ca-bundle.pem` file. Then you can configure your AWS CLI profile to
include the path to your certificate, as described following.

###### To associate your certificate with the interface endpoint

1. Connect the Snowball Edge to power and the network, and turn it
   on.
2. After the device has finished booting up, make a note of its IP address on
   your local network.
3. From a terminal on your network, make sure you can ping the Snowball
   Edge.
4. Run the `snowballEdge get-certificate` command in your
   terminal. For more information on this command, see [Managing public key certificates on Snowball Edge](snowball-edge-certificates-cli.md "snowball-edge-certificates-cli.md").
5. Save the output of the `snowballEdge get-certificate` command
   to a file, for example `ca-bundle.pem`.
6. Run the following command from your terminal.

```
aws configure set profile.snowballEdge.ca_bundle /path/to/ca-bundle.pem
```

After you complete the procedure, you can run CLI commands with these local
credentials, your certificate, and your specified endpoint, as in the following
example.

```
aws s3 ls --endpoint https://192.0.2.0:8443 --profile snowballEdge
```

## Unsupported Amazon S3 features for the Amazon S3 adapter on Snowball Edge

Using the Amazon S3 adapter, you can programmatically transfer data to and from a
Snowball Edge with Amazon S3 API actions. However, not all Amazon S3 transfer features and API
actions are supported for use with a Snowball Edge device when using the Amazon S3 adapter. For example, the following
features and actions are not supported for use with Snowball Edge:

- [TransferManager](../../../sdk-for-java/latest/developer-guide/examples-s3-transfermanager.md "../../../sdk-for-java/latest/developer-guide/examples-s3-transfermanager.md") – This utility transfers files from a local
  environment to Amazon S3 with the SDK for Java. Consider using the supported API actions or
  AWS CLI commands with the interface instead.
- [GET Bucket (List Objects)
  Version 2](../../../AmazonS3/latest/API/v2-RESTBucketGET.md "../../../AmazonS3/latest/API/v2-RESTBucketGET.md") – This implementation of the GET action returns some
  or all (up to 1,000) of the objects in a bucket. Consider using the [GET Bucket (List Objects) Version
  1](../../../AmazonS3/latest/API/RESTBucketGET.md "../../../AmazonS3/latest/API/RESTBucketGET.md") action or the [ls](../../../cli/latest/reference/s3/ls.md "../../../cli/latest/reference/s3/ls.md")
  AWS CLI command.
- [ListBuckets](../../../AmazonS3/latest/API/API_ListBuckets.md "../../../AmazonS3/latest/API/API_ListBuckets.md") – The ListBuckets with the object endpoint is not supported. The following command does not work with Amazon S3 compatible storage on Snowball Edge:

```

aws s3 ls --endpoint `https://192.0.2.0` --profile `profile`

```
