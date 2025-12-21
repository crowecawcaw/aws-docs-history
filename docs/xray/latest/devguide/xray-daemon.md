# AWS X-Ray daemon

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

###### Note

You can now use the CloudWatch agent to collect metrics, logs and traces from Amazon EC2 instances and on-premise
servers. CloudWatch agent version 1.300025.0 and later can collect traces from
[OpenTelemetry](xray-instrumenting-your-app.md#xray-instrumenting-opentel "xray-instrumenting-your-app.md#xray-instrumenting-opentel")
or [X-Ray](xray-instrumenting-your-app.md#xray-instrumenting-xray-sdk "xray-instrumenting-your-app.md#xray-instrumenting-xray-sdk") client SDKs, and send them to X-Ray. Using the CloudWatch agent instead of
the AWS Distro for OpenTelemetry (ADOT) Collector or X-Ray daemon to collect traces can help you reduce the number of agents that you manage.
See the [CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
topic in the CloudWatch User Guide for more information.

The AWS X-Ray daemon is a software application that listens for traffic on UDP port 2000,
gathers raw segment data, and relays it to the AWS X-Ray API. The daemon works in conjunction
with the AWS X-Ray SDKs and must be running so that data sent by the SDKs can reach the X-Ray
service. The X-Ray daemon is an open source project. You can follow the project and submit
issues and pull requests on GitHub: [github.com/aws/aws-xray-daemon](https://github.com/aws/aws-xray-daemon "https://github.com/aws/aws-xray-daemon")

On AWS Lambda and AWS Elastic Beanstalk, use those services' integration with X-Ray to run the daemon.
Lambda runs the daemon automatically any time a function is invoked for a sampled request. On
Elastic Beanstalk, [use the XRayEnabled configuration
option](xray-daemon-beanstalk.md "xray-daemon-beanstalk.md") to run the daemon on the instances in your environment. For more information,
see

To run the X-Ray daemon locally, on-premises, or on other AWS services, download it,
[run it](#xray-daemon-running "#xray-daemon-running"), and then [give it permission](#xray-daemon-permissions "#xray-daemon-permissions") to upload segment documents to
X-Ray.

## Downloading the daemon

You can download the daemon from Amazon S3, Amazon ECR, or Docker Hub, and then run it locally, or
install it on an Amazon EC2 instance on launch.

Amazon S3

###### X-Ray daemon installers and executables

- **Linux (executable)** – [`aws-xray-daemon-linux-3.x.zip`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-3.x.zip "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-3.x.zip") ([sig](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-3.x.zip.sig "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-3.x.zip.sig"))
- **Linux (RPM installer)** – [`aws-xray-daemon-3.x.rpm`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.rpm "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.rpm")
- **Linux (DEB installer)** – [`aws-xray-daemon-3.x.deb`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.deb "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.deb")
- **Linux (ARM64, executable)** – [`aws-xray-daemon-linux-arm64-3.x.zip`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-arm64-3.x.zip "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-arm64-3.x.zip") ([sig](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-arm64-3.x.zip.sig "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-arm64-3.x.zip.sig"))
- **Linux (ARM64, RPM installer)** – [`aws-xray-daemon-arm64-3.x.rpm`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-arm64-3.x.rpm "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-arm64-3.x.rpm")
- **Linux (ARM64, DEB installer)** – [`aws-xray-daemon-arm64-3.x.deb`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-arm64-3.x.deb "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-arm64-3.x.deb")
- **OS X (executable)** – [`aws-xray-daemon-macos-3.x.zip`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-macos-3.x.zip "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-macos-3.x.zip") ([sig](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-macos-3.x.zip.sig "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-macos-3.x.zip.sig"))
- **Windows (executable)** – [`aws-xray-daemon-windows-process-3.x.zip`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-process-3.x.zip "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-process-3.x.zip") ([sig](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-process-3.x.zip.sig "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-process-3.x.zip.sig"))
- **Windows (service)** – [`aws-xray-daemon-windows-service-3.x.zip`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-service-3.x.zip "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-service-3.x.zip") ([sig](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-service-3.x.zip.sig "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-windows-service-3.x.zip.sig"))

These links always point to the latest 3.x release of the daemon. To download a
specific release, do the following:

- If you want to download a release prior to version `3.3.0`, replace
  `3.x` with the version number. For example,
  `2.1.0`. Prior to version `3.3.0`, the
  only available architecture is `arm64`. For example,
  `2.1.0` and `arm64`.
- If you want to download a release after version `3.3.0`, replace
  `3.x` with the version number and `arch`
  with the architecture type.

X-Ray assets are replicated to buckets in every supported region. To use the bucket
closest to you or your AWS resources, replace the region in the above links with your
region.

```
https://s3.`us-west-2`.amazonaws.com/aws-xray-assets.`us-west-2`/xray-daemon/`aws-xray-daemon-3.x.rpm`
```

Amazon ECR
As of version 3.2.0 the daemon can be found on [Amazon ECR](https://gallery.ecr.aws/xray/aws-xray-daemon "https://gallery.ecr.aws/xray/aws-xray-daemon"). Before pulling an
image you should [authenticate
your docker client](../../../AmazonECR/latest/public/public-registries.md#public-registry-auth "../../../AmazonECR/latest/public/public-registries.md#public-registry-auth") to the Amazon ECR public registry.

Pull the latest released 3.x version tag by running the following command:

```
docker pull public.ecr.aws/xray/aws-xray-daemon:3.x
```

Prior or alpha releases can be downloaded by replacing `3.x` with
`alpha` or a specific version number. It is not recommended to use a daemon
image with an alpha tag in a production environment.

Docker Hub
The daemon can be found on [Docker Hub](https://hub.docker.com/r/amazon/aws-xray-daemon "https://hub.docker.com/r/amazon/aws-xray-daemon"). To download
the latest released 3.x version, run the following command:

```
docker pull amazon/aws-xray-daemon:3.x
```

Prior releases of the daemon can be released by replacing `3.x` with the
desired version.

## Verifying the daemon archive's signature

GPG signature files are included for daemon assets compressed in ZIP archives. The public
key is here: [`aws-xray.gpg`](https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray.gpg "https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray.gpg").

You can use the public key to verify that the daemon's ZIP archive is original and
unmodified. First, import the public key with [GnuPG](https://gnupg.org/index.html "https://gnupg.org/index.html").

###### To import the public key

1. Download the public key.

```
$ `BUCKETURL=https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2`
$ `wget $BUCKETURL/xray-daemon/aws-xray.gpg`
```

2. Import the public key into your keyring.

```
$ `gpg --import aws-xray.gpg`
gpg: /Users/me/.gnupg/trustdb.gpg: trustdb created
gpg: key 7BFE036BFE6157D3: public key "AWS X-Ray <aws-xray@amazon.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

Use the imported key to verify the signature of the daemon's ZIP archive.

###### To verify an archive's signature

1. Download the archive and signature file.

```
$ `BUCKETURL=https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2`
$ `wget $BUCKETURL/xray-daemon/aws-xray-daemon-linux-3.x.zip`
$ `wget $BUCKETURL/xray-daemon/aws-xray-daemon-linux-3.x.zip.sig`
```

2. Run `gpg --verify` to verify the signature.

```
$ `gpg --verify aws-xray-daemon-linux-3.x.zip.sig aws-xray-daemon-linux-3.x.zip`
gpg: Signature made Wed 19 Apr 2017 05:06:31 AM UTC using RSA key ID FE6157D3
gpg: Good signature from "AWS X-Ray <aws-xray@amazon.com>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: EA6D 9271 FBF3 6990 277F  4B87 7BFE 036B FE61 57D3
```

Note the warning about trust. A key is only trusted if you or someone you trust has signed
it. This does not mean that the signature is invalid, only that you have not verified the
public key.

## Running the daemon

Run the daemon locally from the command line. Use the `-o` option to run in
local mode, and `-n` to set the region.

```
~/Downloads$ `./xray -o -n us-east-2`
```

For detailed platform-specific instructions, see the following topics:

- **Linux (local)** – [Running the X-Ray daemon on Linux](xray-daemon-local.md#xray-daemon-local-linux "xray-daemon-local.md#xray-daemon-local-linux")
- **Windows (local)** – [Running the X-Ray daemon on Windows](xray-daemon-local.md#xray-daemon-local-windows "xray-daemon-local.md#xray-daemon-local-windows")
- **Elastic Beanstalk** – [Running the X-Ray daemon on AWS Elastic Beanstalk](xray-daemon-beanstalk.md "xray-daemon-beanstalk.md")
- **Amazon EC2** – [Running the X-Ray daemon on Amazon EC2](xray-daemon-ec2.md "xray-daemon-ec2.md")
- **Amazon ECS** – [Running the X-Ray daemon on Amazon ECS](xray-daemon-ecs.md "xray-daemon-ecs.md")

You can customize the daemon's behavior further by using command line options or a
configuration file. See [Configuring the AWS X-Ray daemon](xray-daemon-configuration.md "xray-daemon-configuration.md") for details.

## Giving the daemon permission to send data to

X-Ray

The X-Ray daemon uses the AWS SDK to upload trace data to X-Ray, and it needs AWS
credentials with permission to do that.

On Amazon EC2, the daemon uses the instance's instance profile role automatically. For
information about credentials required to run the daemon locally, see [running your application locally](security_iam_service-with-iam.md#xray-permissions-local "security_iam_service-with-iam.md#xray-permissions-local").

If you specify credentials in more than one location (credentials file, instance profile,
or environment variables), the SDK provider chain determines which credentials are used. For
more information about providing credentials to the SDK, see [Specifying Credentials](https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specifying-credentials "https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specifying-credentials") in the _AWS SDK for Go Developer
Guide_.

The IAM role or user that the daemon's credentials belong to must have permission to write
data to the service on your behalf.

- To use the daemon on Amazon EC2, create a new instance profile role or add the managed
  policy to an existing one.
- To use the daemon on Elastic Beanstalk, add the managed policy to the Elastic Beanstalk default instance
  profile role.
- To run the daemon locally, see [running your
  application locally](security_iam_service-with-iam.md#xray-permissions-local "security_iam_service-with-iam.md#xray-permissions-local").

For more information, see [Identity and access management for AWS X-Ray](security-iam.md "security-iam.md").

## X-Ray daemon logs

The daemon outputs information about its current configuration and segments that it sends
to AWS X-Ray.

```
2016-11-24T06:07:06Z [Info] Initializing AWS X-Ray daemon 2.1.0
2016-11-24T06:07:06Z [Info] Using memory limit of 49 MB
2016-11-24T06:07:06Z [Info] 313 segment buffers allocated
2016-11-24T06:07:08Z [Info] Successfully sent batch of 1 segments (0.123 seconds)
2016-11-24T06:07:09Z [Info] Successfully sent batch of 1 segments (0.006 seconds)
```

By default, the daemon outputs logs to STDOUT. If you run the daemon in the background,
use the `--log-file` command line option or a configuration file to set the log
file path. You can also set the log level and disable log rotation. See [Configuring the AWS X-Ray daemon](xray-daemon-configuration.md "xray-daemon-configuration.md") for
instructions.

On Elastic Beanstalk, the platform sets the location of the daemon logs. See [Running the X-Ray daemon on AWS Elastic Beanstalk](xray-daemon-beanstalk.md "xray-daemon-beanstalk.md") for details.
