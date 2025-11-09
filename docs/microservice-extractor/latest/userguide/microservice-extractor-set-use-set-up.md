AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Set up AWS Microservice Extractor for .NET

Perform the following steps to set up AWS Microservice Extractor for .NET.

1. Verify that you have completed the [prerequisite steps](microservice-extractor-prerequisites.md "microservice-extractor-prerequisites.md")
   to use Microservice Extractor.
2. From the Microservice Extractor landing page, choose **Get
   started**.
3. From the **Setup Microservice Extractor** page, select an AWS region where to store and analyze source code metadata.

###### Note

Your source code never leaves your local system. Microservice Extractor will upload source code metadata to an Amazon S3 bucket you have designated from your AWS account. Microservice Extractor’s scalable backend will process source code metadata ephemerally and write the results in the same S3 bucket. Please see the Data Privacy FAQ for more information. 4. Select either an
AWS named profile or existing AWS CLI/SDK credentials. You can select an
AWS named profile from the dropdown list, update an existing named
profile, or **Add a named profile**. Microservice Extractor uses the
credentials from your AWS profile to share your Microservice Extractor usage data
with AWS to make the Microservice Extractor tool better. For more information about
named profiles, see [Named profiles
for the AWS CLI](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-using-profiles") in the _AWS CLI User
Guide_.

###### Note

When using Single Sign-on capabilities such as AWS IAM Identity
Center be sure to choose the option for AWS CLI/SDK credentials. 5. Select the Amazon S3 bucket in which to store your source code metadata by typing the bucket name and selecting it. If the bucket does not exist, a Region selection will appear for you to create a bucket. Select or create a prefix for your Amazon S3 bucket. 6. (Optional) You may enter Amazon Resource Name (ARN) of the AWS KMS key (SSE-KMS) to use for server-side encryption of the objects Microservice Extractor will store in S3 bucket on your behalf. If you leave this empty, Microservice Extractor will use default server-side encryption with Amazon S3 managed encryption keys (SSE-S3) to store source code metadata. 7. To use AI-based recommendations, select the check box to **Enable
automated groupings**. When the check box is selected, your
code metadata is stored in an Amazon S3 bucket.

###### Note

Your code metadata is never moved from the designated Amazon S3
bucket.

You can select the Amazon S3 bucket in which to store your code by typing the
bucket name and selecting it. If the bucket does not exist, a Region
selection will appear for you to create a bucket. Select or create a prefix
for your Amazon S3 bucket. 8. Add or update the **Working directory** used to store the
output from the application analysis and extraction of your application. You
cannot change this directory after the application is set up. 9. **Microservice Extractor usage data sharing** is enabled by default.
To view the types of data collected, see [Information
collected](microservice-extractor-information-collected.md "microservice-extractor-information-collected.md"). Clear
the check box selection to disable usage data sharing. 10. Choose **Next** to onboard your application.
