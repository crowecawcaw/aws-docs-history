

# Prerequisites
<a name="face-liveness-prerequisites"></a>

 Prerequisites for using Amazon Rekognition Face Liveness include the following: 

1. Set up an AWS Account

1. Set up the Face Liveness AWS SDKs

1. Set up AWS Amplify resources

## Step 1: Set up an AWS account
<a name="face-liveness-prerequisites-setup"></a>

If you do not yet have an AWS account, complete the steps seen at [Create an AWS Account and User](setting-up.md#setting-up-iam) to create one.

## Step 2: Set up the Face Liveness AWS SDKs
<a name="face-liveness-prerequisites-sdks"></a>

If you haven't already, install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md). 

There are several ways to authenticate AWS SDK calls. The examples in this guide assume that you're using a default credentials profile for calling AWS CLI commands and AWS SDK API operations. 

See the [Granting Programmatic Access](https://docs.aws.amazon.com/rekognition/latest/dg/sdk-programmatic-access.html) page for more information on granting your user account access to your chosen AWS SDK. The page also explains how to use a profile on your local computer and how to run the sample code in AWS environments. 

Ensure that the user calling the Face Liveness operations has the correct permissions to call the operations, such as the `AmazonRekognitionFullAccess` and `AmazonS3FullAccess` permissions.

## Step 3: Set up AWS Amplify Resources
<a name="face-liveness-prerequisites-amplify"></a>

To integrate Amazon Rekognition Face Liveness in your app, you must set up the AWS Amplify SDK to use the FaceLivenessDetector Amplify component.

If you haven’t already, follow the instructions to set up the AWS Command Line Interface (AWS CLI) at [Getting Started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html). After the CLI is installed, complete the Configure Auth step steps seen at [the Amplify UI docs site](https://ui.docs.amplify.aws/react/connected-components/liveness#step-1-configure-auth)to set up your AWS Amplify resources.

## Best Practices for Detecting Face Liveness
<a name="face-liveness-best-practices"></a>

We recommend that you follow several best practices when using Amazon Rekognition Face Liveness. Face Liveness best practices include guidelines for where Face Liveness checks should be conducted, use of audit images, and choosing confidence score thresholds.

See [Recommendations for Usage of Face Liveness](recommendations-liveness.md) for the full list of best practices.