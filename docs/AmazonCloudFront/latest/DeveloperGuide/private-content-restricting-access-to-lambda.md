# Restrict access to an

AWS Lambda function URL origin

CloudFront provides _origin access control_ (OAC) for restricting
access to a Lambda function URL origin.

###### Topics

- [Create a new OAC](#create-oac-overview-lambda "#create-oac-overview-lambda")
- [Advanced settings for origin access
  control](#oac-advanced-settings-lambda "#oac-advanced-settings-lambda")
- [Example template code](#example-template-code-lambda-oac "#example-template-code-lambda-oac")

## Create a new OAC

Complete the steps described in the following topics to set up a new OAC in CloudFront.

###### Important

If you use `PUT` or `POST` methods with your Lambda function
URL, your users must compute the SHA256 of the body and include the payload hash
value of the request body in the `x-amz-content-sha256` header when
sending the request to CloudFront. Lambda doesn't support unsigned payloads.

###### Topics

- [Prerequisites](#oac-prerequisites-lambda "#oac-prerequisites-lambda")
- [Grant CloudFront permission to access
  the Lambda function URL](#oac-permission-to-access-lambda "#oac-permission-to-access-lambda")
- [Create the OAC](#create-oac-lambda "#create-oac-lambda")

### Prerequisites

Before you create and set up OAC, you must have a CloudFront distribution with a Lambda function
URL as the origin. To use OAC, you must specify `AWS_IAM` as the value
for the `AuthType` parameter. For more information, see [Use a Lambda function URL](DownloadDistS3AndCustomOrigins.md#concept_lambda_function_url "DownloadDistS3AndCustomOrigins.md#concept_lambda_function_url").

### Grant CloudFront permission to access

the Lambda function URL

Before you create an OAC or set it up in a CloudFront distribution, make sure that CloudFront
has permission to access the Lambda function URL. Do this after you create a CloudFront
distribution, but before you add the OAC to the Lambda function URL in the
distribution configuration.

###### Note

To update the IAM policy for the Lambda function URL, you must use the
AWS Command Line Interface (AWS CLI). Editing the IAM policy in the Lambda console isn't supported
at this time.

The following AWS CLI command grants the CloudFront service principal
(`cloudfront.amazonaws.com`) access to your Lambda function URL. The
`Condition` element in the policy allows CloudFront to access Lambda
_only_ when the request is on behalf of the CloudFront distribution
that contains the Lambda function URL. This is the distribution with the Lambda
function URL origin that you want to add OAC to.

###### Example : AWS CLI command to update a policy to allow read-only access for a CloudFront

distribution with OAC enabled

The following AWS CLI commands allows the CloudFront distribution
(`E1PDK09ESKHJWT`) access to your
Lambda `FUNCTION_URL_NAME`.

```
aws lambda add-permission \
--statement-id "AllowCloudFrontServicePrincipal" \
--action "lambda:InvokeFunctionUrl" \
--principal "cloudfront.amazonaws.com" \
--source-arn "arn:aws:cloudfront::`123456789012`:distribution/`E1PDK09ESKHJWT`" \
--function-name `FUNCTION_URL_NAME`
```

```
aws lambda add-permission \
--statement-id "AllowCloudFrontServicePrincipalInvokeFunction" \
--action "lambda:InvokeFunction" \
--principal "cloudfront.amazonaws.com" \
--source-arn "arn:aws:cloudfront::`123456789012`:distribution/`E1PDK09ESKHJWT`" \
--function-name `FUNCTION_URL_NAME`
```

###### Note

If you create a distribution and it doesn't have permission to your Lambda
function URL, you can choose **Copy CLI command** from the CloudFront
console, and then enter this command from your command line terminal. For more
information, see [Granting function access to AWS services](../../../lambda/latest/dg/access-control-resource-based.md#permissions-resource-serviceinvoke "../../../lambda/latest/dg/access-control-resource-based.md#permissions-resource-serviceinvoke") in the
_AWS Lambda Developer Guide_.

### Create the OAC

To create an OAC, you can use the AWS Management Console, CloudFormation, the AWS CLI, or the CloudFront API.

Console

###### To create an OAC

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Origin access**.
3. Choose **Create control setting**.
4. On the **Create new OAC** form, do the following:
   1. Enter a **Name** and (optionally) a
      **Description** for the OAC.
   2. For **Signing behavior**, we recommend that you leave the default
      setting (**Sign requests
      (recommended)**). For more information, see
      [Advanced settings for origin access
      control](#oac-advanced-settings-lambda "#oac-advanced-settings-lambda").

5. For **Origin type**, choose **Lambda**.
6. Choose **Create**.

###### Tip

After you create the OAC, make note of the
**Name**. You need this in the
following procedure.

###### To add an origin access control to a Lambda function URL in a distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose a distribution with a Lambda function URL that you want to add the OAC to, then
   choose the **Origins** tab.
3. Select the Lambda function URL that you want to add the OAC to, and then choose
   **Edit**.
4. Select **HTTPS only** for your origin's
   **Protocol**.
5. From the **Origin access control** dropdown, choose the OAC name
   that you want to use.
6. Choose **Save changes**.

The distribution starts deploying to all of the CloudFront edge locations. When an edge
location receives the new configuration, it signs all requests that it
sends to the Lambda function URL.

CloudFormation
To create an OAC with CloudFormation, use the `AWS::CloudFront::OriginAccessControl`
resource type. The following example shows the CloudFormation template syntax, in
YAML format, for creating an OAC.

```
Type: AWS::CloudFront::OriginAccessControl
Properties:
  OriginAccessControlConfig:
      Description: An optional description for the origin access control
      Name: ExampleOAC
      OriginAccessControlOriginType: lambda
      SigningBehavior: always
      SigningProtocol: sigv4
```

For more information, see [AWS::CloudFront::OriginAccessControl](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.md") in the _AWS CloudFormation User Guide_.

CLI
To create an origin access control with the AWS Command Line Interface (AWS CLI), use the **aws
cloudfront create-origin-access-control** command. You can use an input file to
provide the input parameters for the command, rather than specifying each individual
parameter as command line input.

###### To create an origin access control (CLI with input file)

1. Use the following command to create a file that's named
   `origin-access-control.yaml`. This file contains all of the input
   parameters for the **create-origin-access-control** command.

```

aws cloudfront create-origin-access-control --generate-cli-skeleton yaml-input > origin-access-control.yaml
```

2. Open the `origin-access-control.yaml` file that you just created.
   Edit the file to add a name for the OAC, a description (optional), and change the
   `SigningBehavior` to `always`. Then save the file.

For information about other OAC settings, see [Advanced settings for origin access
control](#oac-advanced-settings-lambda "#oac-advanced-settings-lambda"). 3. Use the following command to create the origin access control using the input
parameters from the `origin-access-control.yaml` file.

```

aws cloudfront create-origin-access-control --cli-input-yaml file://origin-access-control.yaml
```

Make note of the `Id` value in the command output. You need it to add the
OAC to a Lambda function URL in a CloudFront distribution.

###### To attach an OAC to a Lambda function URL in an existing distribution (CLI with input

file)

1. Use the following command to save the distribution configuration for the CloudFront
   distribution that you want to add the OAC to. The distribution
   must have a Lambda function URL as the origin.

```

aws cloudfront get-distribution-config --id `<CloudFront distribution ID>` --output yaml > dist-config.yaml
```

2.  Open the file that's named `dist-config.yaml` that you just
    created. Edit the file, making the following changes:

        * In the `Origins` object, add the OAC's ID to the field that's named
         `OriginAccessControlId`.
        * Remove the value from the field that's named `OriginAccessIdentity`, if
         one exists.
        * Rename the `ETag` field to `IfMatch`, but don't change the
         field's value.

    Save the file when finished.

3.  Use the following command to update the distribution to use the origin access
    control.

```

aws cloudfront update-distribution --id `<CloudFront distribution ID>` --cli-input-yaml file://dist-config.yaml
```

The distribution starts deploying to all of the CloudFront edge locations. When an edge
location receives the new configuration, it signs all requests that it
sends to the Lambda function URL.

API
To create an OAC with the CloudFront API, use [CreateOriginAccessControl](../../../cloudfront/latest/APIReference/API_CreateOriginAccessControl.md "../../../cloudfront/latest/APIReference/API_CreateOriginAccessControl.md"). For more information about the
fields that you specify in this API call, see the API reference
documentation for your AWS SDK or other API client.

After you create an OAC you can attach it to a Lambda function URL in a distribution,
using one of the following API calls:

- To attach it to an existing distribution, use [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md").
- To attach it to a new distribution, use [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md").

For both of these API calls, provide the OAC ID in the
`OriginAccessControlId` field, inside an origin. For more
information about the other fields that you specify in these API calls,
see and the API reference documentation for your AWS SDK or other API
client.

## Advanced settings for origin access

control

The CloudFront OAC feature includes advanced settings that are intended only for specific use
cases. Use the recommended settings unless you have a specific need for the advanced
settings.

OAC contains a setting named **Signing behavior** (in the console), or
`SigningBehavior` (in the API, CLI, and CloudFormation). This setting provides the
following options:

**Always sign origin requests (recommended setting)**

We recommend using this setting, named **Sign requests (recommended)**
in the console, or `always` in the API, CLI, and CloudFormation. With this
setting, CloudFront always signs all requests that it sends to the Lambda function
URL.

**Never sign origin requests**

This setting is named **Do not sign requests** in the console, or
`never` in the API, CLI, and CloudFormation. Use this setting to turn
off OAC for all origins in all distributions that use this OAC. This can
save time and effort compared to removing an OAC from all origins and
distributions that use it, one by one. With this setting, CloudFront doesn't sign
any requests that it sends to the Lambda function URL.

###### Warning

To use this setting, the Lambda function URL must be publicly accessible. If you use
this setting with a Lambda function URL that's not publicly accessible,
CloudFront can't access the origin. The Lambda function URL returns errors to
CloudFront and CloudFront passes those errors on to viewers. For more information,
see [Security and auth model for Lambda function URLs](../../../lambda/latest/dg/urls-auth.md "../../../lambda/latest/dg/urls-auth.md") in
the _AWS Lambda User Guide_.

**Don't override the viewer (client) `Authorization` header**

This setting is named **Do not override authorization header** in the
console, or `no-override` in the API, CLI, and CloudFormation. Use this setting when you
want CloudFront to sign origin requests only when the corresponding viewer request does not include
an `Authorization` header. With this setting, CloudFront passes on the
`Authorization` header from the viewer request when one is present, but signs the
origin request (adding its own `Authorization` header) when the viewer request
doesn't include an `Authorization` header.

###### Warning

- If you use this setting, you must specify the Signature
  Version 4 signing for the Lambda function URL instead of your
  CloudFront distribution's name or CNAME. When CloudFront forwards the
  `Authorization` header from the viewer
  request to the Lambda function URL, Lambda will validate the
  signature against the host of the Lambda URL domain. If the
  signature isn't based on the Lambda URL domain, the host in
  the signature won't match the host used by the Lambda URL
  origin. This means the request will fail, resulting in a
  signature validation error.

- To pass along the `Authorization` header from the
  viewer request, you _must_ add
  the `Authorization` header to a [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md") for
  all cache behaviors that use Lambda function URLs associated with
  this origin access control.

## Example template code

If your CloudFront origin is a Lambda function URL that's associated with an OAC, you can use
the following Python script to upload files to the Lambda function with the
`POST` method.

This code assumes that you configured the OAC with the default signing behavior set to
**Always sign origin requests** and that you didn't select the
**Do not override authorization header** setting.

This configuration allows the OAC to manage SigV4 authorization correctly with Lambda
by using the Lambda hostname. The payload is signed by using SigV4 from the IAM
identity that's authorized for the Lambda function URL, which is designated as the
`IAM_AUTH` type.

The template demonstrates how to handle signed payload hash values in the
x-amz-content-sha256 header for `POST` requests from the
client side. Specifically, this template is designed to manage form data payloads. The
template enables secure file uploads to a Lambda function URL through CloudFront, and uses
AWS authentication mechanisms to ensure that only authorized requests can access the
Lambda function.

###### The code includes the following functionality:

- Meets the requirement for including the payload hash in the
  x-amz-content-sha256 header
- Uses SigV4 authentication for secure AWS service access
- Supports file uploads by using multi-part form data
- Includes error handling for request exceptions

```
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import requests
import hashlib
import os


def calculate_body_hash(body):
    return hashlib.sha256(body).hexdigest()


def sign_request(request, credentials, region, service):
    sigv4 = SigV4Auth(credentials, service, region)
    sigv4.add_auth(request)


def upload_file_to_lambda(cloudfront_url, file_path, region):
    # AWS credentials
    session = boto3.Session()
    credentials = session.get_credentials()

    # Prepare the multipart form-data
    boundary = "------------------------boundary"

    # Read file content
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Get the filename from the path
    filename = os.path.basename(file_path)

    # Prepare the multipart body
    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f'Content-Type: application/octet-stream\r\n\r\n'
    ).encode('utf-8')
    body += file_content
    body += f'\r\n--{boundary}--\r\n'.encode('utf-8')

    # Calculate SHA256 hash of the entire body
    body_hash = calculate_body_hash(body)

    # Prepare headers
    headers = {
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'x-amz-content-sha256': body_hash
    }

    # Create the request
    request = AWSRequest(
        method='POST',
        url=cloudfront_url,
        data=body,
        headers=headers
    )

    # Sign the request
    sign_request(request, credentials, region, 'lambda')

    # Get the signed headers
    signed_headers = dict(request.headers)

    # Print request headers before sending
    print("Request Headers:")
    for header, value in signed_headers.items():
        print(f"{header}: {value}")

    try:
        # Send POST request with signed headers
        response = requests.post(
            cloudfront_url,
            data=body,
            headers=signed_headers
        )

        # Print response status and content
        print(f"\nStatus code: {response.status_code}")
        print("Response:", response.text)

        # Print response headers
        print("\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Usage
cloudfront_url = "https://d111111abcdef8.cloudfront.net"
file_path = r"filepath"
region = "us-east-1"  # example: "us-west-2"

upload_file_to_lambda(cloudfront_url, file_path, region)
```
