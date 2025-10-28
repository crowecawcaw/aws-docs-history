# Detecting text with an AWS Lambda function

AWS Lambda is a compute service that you can use to run code without provisioning or managing
servers. You can call Amazon Textract API operations from within an AWS Lambda function.
The following instructions show how to create a Lambda function in Python that calls
[DetectDocumentText](API_DetectDocumentText.md "API_DetectDocumentText.md").

The Lambda function returns a list of [Block](API_Block.md "API_Block.md") objects with information about the detected words and
lines of text. The instructions include example Python code that shows you how to call
the Lambda function with a document supplied from an Amazon S3 bucket or your local computer.
Images stored in Amazon S3 must be in single-page PDF or TIFF document format, or in JPEG or
PNG format. Local images must be in single-page PDF or TIFF format. The Python code
returns part of the JSON response for each Block type detected in the document.

For an example that uses Lambda functions to process documents at a large scale, see
[Amazon
Textract IDP CDK Constructs](https://github.com/aws-samples/amazon-textract-idp-cdk-constructs/ "https://github.com/aws-samples/amazon-textract-idp-cdk-constructs/") and
[Use machine learning to automate
and process documents at scale](https://s12d.com/aws-idp-scale-workshop "https://s12d.com/aws-idp-scale-workshop").

###### Topics

- [Step 1: Create an AWS Lambda function
  (console)](#example-lambda-create-function "#example-lambda-create-function")
- [Step 2: (Optional) Create a layer (console)](#example-lambda-create-layer "#example-lambda-create-layer")
- [Step 3: Add Python code (console)](#example-lambda-add-code "#example-lambda-add-code")
- [Step 4: Try your Lambda function](#example-lambda-test "#example-lambda-test")

## Step 1: Create an AWS Lambda function

(console)

In this step, you create an empty AWS Lambda function and an IAM execution role that
lets your function call the `DetectDocumentText` operation. If you are
supplying documents from Amazon S3, this step also shows you how to grant access to the
bucket that stores your documents.

Later you add the source code and optionally add a layer to the Lambda function.

###### To create an AWS Lambda function

(console)

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**. For more information, see
   [Create a Lambda Function with the Console](../../../lambda/latest/dg/getting-started-create-function.md "../../../lambda/latest/dg/getting-started-create-function.md").
3. Choose the following options:
   - Choose **Author from scratch**.
   - Enter a value for **Function name**.
   - For **Runtime**, choose **Python 3.9**.
   - For **Architecture**, choose **x86_64**.

4. Choose **Create function** to create the AWS Lambda
   function.
5. On the function page, choose the **Configuration** tab.
6. On the **Permissions** pane, under
   **Execution role**, choose the role name to open the role in the IAM
   console.
7. In the **Permissions** tab, choose
   **Add permissions** and then **Create inline policy**.
8. Choose the **JSON** tab and replace the policy with the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "textract:DetectDocumentText",
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "DetectDocumentText"
 }
 ]
}`

```

9. Choose **Review policy**.
10. Enter a name for the policy, for example _DetectDocumentText-access_.
11. Choose **Create policy**.
12. If you are storing documents for analysis in an Amazon S3 bucket, you must add
    an Amazon S3 access policy. To do this, repeat steps 7 to 11 in the AWS Lambda
    console and make the following changes.
    1. For step 8, use the following policy. Replace
       `bucket/folder path` with the Amazon S3
       bucket and folder path to the documents that you want to analyze.

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "S3Access",
     "Effect": "Allow",
     "Action": "s3:GetObject",
     "Resource": "arn:aws:s3:::`bucket/folder path`/*"
     }
     ]
    }`

    ```

    2. For step 10, choose a different policy name, such as _S3Bucket-access_.

## Step 2: (Optional) Create a layer (console)

To run this example, you don't need to perform this step. The
`DetectDocumentText` operation is included in the default Lambda
Python environment as part of AWS SDK for Python (Boto3). If other parts of
your Lambda function require recent AWS service updates that aren't in the default
Lambda Python environment, then perform this step to add the most recent Boto3 SDK release as a
layer to your function.

First, you create a zip file archive that contains the Boto3 SDK. Then, you create
a layer and add the zip file archive to the layer. For more information, see [Using
layers with your Lambda function](../../../lambda/latest/dg/invocation-layers.md#invocation-layers-using "../../../lambda/latest/dg/invocation-layers.md#invocation-layers-using").

###### To create and add a layer (console)

1. Open a command prompt and enter the following commands to create a
   deployment package with the most recent version of the AWS SDK.

```
pip install boto3 --target python/.
zip boto3-layer.zip -r python/

```

2. Note the name of the zip file (boto3-layer.zip), which you use in step 8 of this procedure.
3. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
4. In the navigation pane, choose **Layers**.
5. Choose **Create layer**.
6. Enter values for **Name** and
   **Description**.
7. For **Code entry type**, choose **Upload a .zip
   file** and select **Upload**.
8. In the dialog box, choose the zip file archive (boto3-layer.zip) that you created
   in step 1 of this procedure.
9. For
   **Compatible runtimes**, choose **Python 3.9**.
10. Choose **Create** to create the layer.
11. Choose the navigation pane menu icon.
12. In the navigation pane, choose **Functions**.
13. In the resources list, choose the function that you created previously in [Step 1: Create an AWS Lambda function
    (console)](#example-lambda-create-function "#example-lambda-create-function").
14. Choose the **Code** tab.
15. In the **Layers** section, choose **Add a
    layer**.
16. Choose **Custom layers**.
17. In **Custom layers**, choose the layer name that you entered in step 6.
18. In **Version** choose the layer version, which should be 1.
19. Choose **Add**.

## Step 3: Add Python code (console)

In this step, you add Python code to your Lambda function by using the
Lambda console code editor. The code detects text in a document with
`DetectDocumentText` and returns a list of Block objects with
information about the detected text. The document can be located in an Amazon S3 bucket
or a local computer. Images stored in Amazon S3 must be single-page PDF or TIFF format documents
or in JPEG or PNG format. Local images must be in single-page PDF or TIFF format.

###### To add Python code (console)

1. Navigate to the **Code** tab.
2. In the code editor, replace the code in
   **lambda_function.py** with the following code:

```

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
An AWS lambda function that analyzes documents with Amazon Textract.
"""
import json
import base64
import logging
import boto3

from botocore.exceptions import ClientError

# Set up logging.
logger = logging.getLogger(__name__)

# Get the boto3 client.
textract_client = boto3.client('textract')


def lambda_handler(event, context):
    """
    Lambda handler function
    param: event: The event object for the Lambda function.
    param: context: The context object for the lambda function.
    return: The list of Block objects recognized in the document
    passed in the event object.
    """

    try:

        # Determine document source.
        if 'image' in event:
            # Decode the image
            image_bytes = event['image'].encode('utf-8')
            img_b64decoded = base64.b64decode(image_bytes)
            image = {'Bytes': img_b64decoded}


        elif 'S3Object' in event:
            image = {'S3Object':
                     {'Bucket':  event['S3Object']['Bucket'],
                      'Name': event['S3Object']['Name']}
                     }

        else:
            raise ValueError(
                'Invalid source. Only image base 64 encoded image bytes or S3Object are supported.')


        # Analyze the document.
        response = textract_client.detect_document_text(Document=image)

        # Get the Blocks
        blocks = response['Blocks']

        lambda_response = {
            "statusCode": 200,
            "body": json.dumps(blocks)
        }

    except ClientError as err:
        error_message = "Couldn't analyze image. " + \
            err.response['Error']['Message']

        lambda_response = {
            'statusCode': 400,
            'body': {
                "Error": err.response['Error']['Code'],
                "ErrorMessage": error_message
            }
        }
        logger.error("Error function %s: %s",
            context.invoked_function_arn, error_message)

    except ValueError as val_error:
        lambda_response = {
            'statusCode': 400,
            'body': {
                "Error": "ValueError",
                "ErrorMessage": format(val_error)
            }
        }
        logger.error("Error function %s: %s",
            context.invoked_function_arn, format(val_error))

    return lambda_response

```

3. Choose **Deploy** to deploy your Lambda function.

## Step 4: Try your Lambda function

Now that you’ve created your Lambda function, you can invoke it to detect text in
a document. In this step, you use Python code on your computer to pass a local
document or a document in an Amazon S3 bucket to your Lambda function. Documents passed
from a local computer must be smaller than 6291456 bytes. If your documents are
larger, upload them to an Amazon S3 bucket and call the script with the Amazon S3 path to the
image. For information about uploading image files to an Amazon S3 bucket, see [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md").

Make sure you run the code in the same [AWS
Region](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in which you created the Lambda function. You can view the AWS
Region for your Lambda function in the navigation bar of the function details page in
the [Lambda console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").

If the AWS Lambda function returns a timeout error, extend the timeout period for
the Lambda function. For more information, see [Configuring function timeout (console)](../../../lambda/latest/dg/configuration-function-common.md#configuration-timeout-console "../../../lambda/latest/dg/configuration-function-common.md#configuration-timeout-console").

For more information about invoking a Lambda function from your code, see [Invoking AWS Lambda Functions](../../../lambda/latest/dg/invoking-lambda-functions.md "../../../lambda/latest/dg/invoking-lambda-functions.md").

###### To try your Lambda function

1.  If you haven't already done so, do the following:
    1. Make sure that the user has `lambda:InvokeFunction`
       permission. You can use the following policy:

    You can get the ARN for your Lambda function from the
    function overview in the [Lambda console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").

    To provide access, add permissions to your users, groups, or roles:

        * Users and groups in AWS IAM Identity Center:


        Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the *AWS IAM Identity Center User Guide*.
        * Users managed in IAM through an identity provider:


        Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
         in the *IAM User Guide*.
        * IAM users:




        	+ Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
        	+ (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

    2. Install and configure AWS SDK for Python. For more information,
       see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2.  Save the following code to a file named `client.py`:

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
Test code for running the Amazon Textract Lambda
function example code.
"""

import argparse
import logging
import base64
import json
import io
import boto3

from botocore.exceptions import ClientError
from PIL import Image, ImageDraw


logger = logging.getLogger(__name__)


def analyze_image(function_name, image):
    """Analyzes a document with an AWS Lambda function.
    :param image: The document that you want to analyze.
    :return The list of Block objects in JSON format.
    """

    lambda_client = boto3.client('lambda')

    lambda_payload = {}

    if image.startswith('s3://'):
        logger.info("Analyzing document from S3 bucket: %s", image)
        bucket, key = image.replace("s3://", "").split("/", 1)
        s3_object = {
            'Bucket': bucket,
            'Name': key
        }

        lambda_payload = {"S3Object": s3_object}

    else:
        with open(image, 'rb') as image_file:
            logger.info("Analyzing local document: %s ", image)
            image_bytes = image_file.read()
            data = base64.b64encode(image_bytes).decode("utf8")

            lambda_payload = {"image": data}

    # Call the lambda function with the document.

    response = lambda_client.invoke(FunctionName=function_name,
                                    Payload=json.dumps(lambda_payload))

    return json.loads(response['Payload'].read().decode())


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "function", help="The name of the AWS Lambda function that you want " \
        "to use to analyze the document.")
    parser.add_argument(
        "image", help="The document that you want to analyze.")


def main():
    """
    Entrypoint for script.
    """
    try:
        logging.basicConfig(level=logging.INFO,
                            format="%(levelname)s: %(message)s")

        # Get command line arguments.
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        # Get analysis results.
        result = analyze_image(args.function, args.image)
        status = result['statusCode']

        blocks = result['body']
        blocks = json.loads(blocks)

        if status == 200:

            for block in blocks:
                print('Type: ' + block['BlockType'])
                if block['BlockType'] != 'PAGE':
                    print('Detected: ' + block['Text'])
                    print('Confidence: ' + "{:.2f}".format(block['Confidence']) + "%")

                print('Id: {}'.format(block['Id']))
                if 'Relationships' in block:
                    print('Relationships: {}'.format(block['Relationships']))
                print('Bounding Box: {}'.format(block['Geometry']['BoundingBox']))
                print('Polygon: {}'.format(block['Geometry']['Polygon']))
                print()
            print("Blocks detected: " + str(len(blocks)))
        else:
            print(f"Error: {result['statusCode']}")
            print(f"Message: {result['body']}")

    except ClientError as error:
        logging.error(error)
        print(error)


if __name__ == "__main__":
    main()

```

3. Run the code. For the command line argument, supply the Lambda function name and the
   document that you want to analyze. You can supply a path to a local document, or you can use
   the Amazon S3 path to an document stored in an Amazon S3 bucket. For example:

```
python client.py `function_name s3://bucket/path/document.jpg`
```

If the document is in an Amazon S3 bucket. make sure that it is the same bucket that you
specified previously in step 12 of [Step 1: Create an AWS Lambda function
(console)](#example-lambda-create-function "#example-lambda-create-function").

If successful, your code returns a partial JSON response for each Block
type detected in the document.
