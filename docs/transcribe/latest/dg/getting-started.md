# Getting started with Amazon Transcribe

Before you can create transcriptions, you have a few prerequisites:

- [Sign up for an
  AWS account](#getting-started-sign-up "#getting-started-sign-up")
- [Install the AWS CLI and SDKs](#getting-started-api "#getting-started-api") (if
  you're using the AWS Management Console for your transcriptions, you can skip this
  step)
- [Configure IAM
  credentials](#getting-started-iam "#getting-started-iam")
- [Set up an Amazon S3
  bucket](#getting-started-s3 "#getting-started-s3")
- [Create an IAM
  policy](#getting-started-policy "#getting-started-policy")
  Once you complete these prerequisites, you're ready to transcribe. Select your preferred transcription
  method from the following list to get started.

- [AWS CLI](getting-started-cli.md "getting-started-cli.md")
- [AWS Management Console](getting-started-console.md "getting-started-console.md")
- [AWS SDK](getting-started-sdk.md "getting-started-sdk.md")
- [HTTP](getting-started-http-websocket.md "getting-started-http-websocket.md")
- [WebSockets](getting-started-http-websocket.md "getting-started-http-websocket.md")

###### Tip

If you're new to Amazon Transcribe or would like to explore our features, we recommend using
the [AWS Management Console](https://console.aws.amazon.com/transcribe "https://console.aws.amazon.com/transcribe"). This is also the easiest
option if you'd like to start a stream using your computer microphone.

Because streaming using HTTP/2 and WebSockets is more complicated than the other
transcription methods, we recommend reviewing the [Setting up a streaming transcription](streaming-setting-up.md "streaming-setting-up.md") section before getting started with these methods.
**Note that we strongly recommend using an SDK for streaming transcriptions.**

## Signing up for an AWS account

You can sign up for a [free tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") account or
a [paid account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html"). Both options give you access to all AWS services. The free tier has a trial period during which you can explore AWS services and estimate your usage. Once your trial period expires, you can
migrate to a paid account. Fees are accrued on a pay-as-you-use basis; see [Amazon Transcribe Pricing](https://aws.amazon.com/transcribe/pricing/ "https://aws.amazon.com/transcribe/pricing/") for
details.

###### Tip

When setting up your account, make note of your AWS account ID because
you need it to create IAM entities.

## Installing the AWS CLI and SDKs

To use the Amazon Transcribe API, you must first install the AWS CLI. The current
AWS CLI is version 2. You can find installation instructions for
[Linux](../../../cli/latest/userguide/install-cliv2-linux.md "../../../cli/latest/userguide/install-cliv2-linux.md"),
[Mac](../../../cli/latest/userguide/install-cliv2-mac.md "../../../cli/latest/userguide/install-cliv2-mac.md"),
[Windows](../../../cli/latest/userguide/install-cliv2-windows.md "../../../cli/latest/userguide/install-cliv2-windows.md"),
and [Docker](../../../cli/latest/userguide/install-cliv2-docker.md "../../../cli/latest/userguide/install-cliv2-docker.md")
in the [_AWS Command Line Interface User Guide_](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

Once you have the AWS CLI installed, you must [configure](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") it for your security credentials and
AWS Region.

If you want to use Amazon Transcribe with an SDK, select your preferred language for installation
instructions:

- [.NET](../../../sdk-for-net/v3/developer-guide/quick-start.md "../../../sdk-for-net/v3/developer-guide/quick-start.md")
- [C++](../../../sdk-for-cpp/v1/developer-guide/getting-started.md "../../../sdk-for-cpp/v1/developer-guide/getting-started.md")
- [Go](https://aws.github.io/aws-sdk-go-v2/docs/ "https://aws.github.io/aws-sdk-go-v2/docs/")
- [Java V2](../../../sdk-for-java/latest/developer-guide/setup.md "../../../sdk-for-java/latest/developer-guide/setup.md")
- [JavaScript](../../../sdk-for-javascript/v3/developer-guide/getting-started.md "../../../sdk-for-javascript/v3/developer-guide/getting-started.md")
- [PHP V3](../../../sdk-for-php/v3/developer-guide/getting-started_installation.md "../../../sdk-for-php/v3/developer-guide/getting-started_installation.md")
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html") (batch transcriptions)
- [Python](https://github.com/awslabs/amazon-transcribe-streaming-sdk "https://github.com/awslabs/amazon-transcribe-streaming-sdk")
  (streaming transcriptions)
- [Ruby V3](../../../sdk-for-ruby/v3/developer-guide/setup-install.md "../../../sdk-for-ruby/v3/developer-guide/setup-install.md")
- [Rust](https://crates.io/crates/aws-sdk-transcribe "https://crates.io/crates/aws-sdk-transcribe") (batch
  transcriptions)
- [Rust](https://crates.io/crates/aws-sdk-transcribestreaming "https://crates.io/crates/aws-sdk-transcribestreaming") (streaming
  transcriptions)

## Configure IAM credentials

When you create an AWS account, you begin with one sign-in identity that has
complete access to all AWS services and resources in your account. This identity is
called the AWS account root user and is accessed by signing in with the email address
and password that you used to create the account.

We strongly recommend that you do not use the root user for your everyday tasks. Safeguard
your root user credentials and use them to perform the tasks that only the root user can perform.

As a best practice, require users—including those that require administrator
access—to use federation with an identity provider to access AWS services by
using temporary credentials.

A federated identity is any user who accesses AWS services by using
credentials provided through an identity source. When federated identities access
AWS accounts, they assume roles, and the roles provide temporary
credentials.

For centralized access management, we recommend that you use [AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"). You can create users and groups in IAM Identity Center.
Or you can connect and synchronize to a set of users and groups in your own identity
source for use across all your AWS accounts and applications. For more
information, see [Identity and Access Management for Amazon Transcribe](security-iam.md "security-iam.md").

To learn more about IAM best practices, refer to [Security best practices in
IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

## Creating an Amazon S3 bucket

Amazon S3 is a secure object storage service. Amazon S3 stores your files (called
_objects_) in containers (called _buckets_).

To run a batch transcription, you must first upload your media files into an Amazon S3 bucket. If
you don't specify an Amazon S3 bucket for your transcription output, Amazon Transcribe puts your
transcript in a temporary AWS-managed Amazon S3 bucket. Transcription output in AWS-managed
buckets is automatically deleted after 90 days.

Learn how to [Create your first S3 bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md")
and [Upload an object to your
bucket](../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md "../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md").

## Creating an IAM policy

To manage access in AWS, you must create policies and attach them to
IAM identities (users, groups, or roles) or AWS resources. A policy
defines the permissions of the entity it is attached to. For example, a role can only access a media
file located in your Amazon S3 bucket if you've attached a policy to that role which grants
it access. If you want to further restrict that role, you can instead limit its access to a specific file
within an Amazon S3 bucket.

To learn more about using AWS policies see:

- [Policies
  and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
- [Creating
  IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")
- [How Amazon Transcribe works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")

For example policies you can use with Amazon Transcribe, see
[Amazon Transcribe identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). If you want to generate custom
policies, consider using the
[AWS
Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html "https://awspolicygen.s3.amazonaws.com/policygen.html").

You can add a policy using the AWS Management Console, AWS CLI, or
AWS SDK. For instructions, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api").

Policies have the format:

Amazon Resource Names (ARNs) uniquely identify all AWS resources, such as an
Amazon S3 bucket. You can use ARNs in your policy to grant permissions for specific actions to
use specific resources. For example, if you want to grant read access to an Amazon S3 bucket
and its sub-folders, you can add the following code to your trust policy's `Statement`
section:

```
{
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:ListBucket"
        ],
        "Resource": [
            "arn:aws:s3:::`amzn-s3-demo-bucket`",
            "arn:aws:s3:::`amzn-s3-demo-bucket/*`"
        ]
}
```

Here's an example policy that grants Amazon Transcribe read (`GetObject`,
`ListBucket`) and write (`PutObject`) permissions to an
Amazon S3 bucket, `amzn-s3-demo-bucket`, and its sub-folders:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket/*`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket/*`"
 ]
 }
 ]
}`

```
