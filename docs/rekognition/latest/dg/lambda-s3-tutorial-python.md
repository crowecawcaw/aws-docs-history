# Detecting Labels in an Image Using Lambda and Python

AWS Lambda is a compute service that you can use to run code without provisioning or
managing servers. You can call Rekognition API operations from within an Lambda function. The following
instructions show how to create a Lambda function in Python that calls `DetectLabels`.

The Lambda function calls `DetectLabels` and it returns an array of labels
detected in the image, as well as the level of confidence by which they were detected.

The instructions include sample Python code which shows you how to call the Lambda function
and supply it with an image sourced from an Amazon S3 bucket or your local computer.

Make sure your chosen images meet Rekognition’s limits. See [Guidelines and quotas](limits.md "limits.md") in Rekognition and the
[DetectLabels API Reference](../APIReference/API_DetectLabels.md "../APIReference/API_DetectLabels.md") for information on image file type and size limits.

##

Create an Lambda function (console)

In this step, you create an empty Lambda function and an IAM execution role that lets your
Lambda function call the `DetectLabels` operation. In later steps, you add the source
code and optionally add a layer to the Lambda function.

If you are using documents stored in an Amazon S3 bucket, this step also demonstrates how to
grant access to the bucket that stores your documents.

###### To create an AWS Lambda function

(console)

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**. For more information, see
   [Create a Lambda Function with the Console](../../../lambda/latest/dg/getting-started-create-function.md "../../../lambda/latest/dg/getting-started-create-function.md").
3. Choose the following options:
   - Choose **Author from scratch**.
   - Enter a value for **Function name**.
   - For **Runtime**, choose the most recent version of Python.
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
 "Action": "rekognition:DetectLabels",
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "DetectLabels"
 }
 ]
}`

```

9. Choose **Review policy**.
10. Enter a name for the policy, for example _DetectLabels-access_.
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

##

(Optional) Create a layer (console)

You don't need to perform this step to use a Lambda function and call
`DetectLabels`.

The `DetectLabels` operation is included in the default Lambda Python environment
as part of AWS SDK for Python (Boto3).

If other parts of your Lambda function require recent AWS service updates that aren't in
the default Lambda Python environment, then you can perform this step to add the most recent Boto3
SDK release as a layer to your function.

To add the SDK as a layer, you first create a zip file archive that contains the Boto3 SDK. Then, you create a
layer and add the zip file archive to the layer. For more information, see
[Using layers with your Lambda function](../../../lambda/latest/dg/invocation-layers.md#invocation-layers-using "../../../lambda/latest/dg/invocation-layers.md#invocation-layers-using").

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
9. For **Compatible runtimes**, choose the most recent version of
   Python.
10. Choose **Create** to create the layer.
11. Choose the navigation pane menu icon.
12. In the navigation pane, choose **Functions**.
13. In the resources list, choose the function that you created previously in .
14. Choose the **Code** tab.
15. In the **Layers** section, choose **Add a
    layer**.
16. Choose **Custom layers**.
17. In **Custom layers**, choose the layer name that you entered in step 6.
18. In **Version** choose the layer version, which should be 1.
19. Choose **Add**.

##

Add Python code (console)

In this step, you add your Python code to your Lambda function through the Lambda console
code editor. The code detects labels in a image using the `DetectLabels` operation. It
returns an array of labels detected in the image, as well as the level of confidence in the
labels detected.

The document you provide to the `DetectLabels` operation can be located in an
Amazon S3 bucket or a local computer.

###### To add Python code (console)

1. Navigate to the **Code** tab.
2. In the code editor, replace the code in
   **lambda_function.py** with the following code:

```
import boto3
import logging
from botocore.exceptions import ClientError
import json
import base64

# Instantiate logger
logger = logging.getLogger(__name__)

# connect to the Rekognition client
rekognition = boto3.client('rekognition')

def lambda_handler(event, context):

    try:
        image = None
        if 'S3Bucket' in event and 'S3Object' in event:
            s3 = boto3.resource('s3')
            s3_object = s3.Object(event['S3Bucket'], event['S3Object'])
            image = s3_object.get()['Body'].read()

        elif 'image' in event:
            image_bytes = event['image'].encode('utf-8')
            img_b64decoded = base64.b64decode(image_bytes)
            image = img_b64decoded


        elif image is None:
            raise ValueError('Missing image, check image or bucket path.')

        else:
            raise ValueError("Only base 64 encoded image bytes or S3Object are supported.")

        response = rekognition.detect_labels(Image={'Bytes': image})
        lambda_response = {
            "statusCode": 200,
            "body": json.dumps(response)
        }
        labels = [label['Name'] for label in response['Labels']]
        print("Labels found:")
        print(labels)

    except ClientError as client_err:

       error_message = "Couldn't analyze image: " + client_err.response['Error']['Message']

       lambda_response = {
           'statusCode': 400,
           'body': {
               "Error": client_err.response['Error']['Code'],
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

##

To add Python code (console)

Now that you’ve created your Lambda function, you can invoke it to detect labels in an image.

In this step, you run Python code on your computer, which passes a local image or an image
in an Amazon S3 bucket, to your Lambda function.

Make sure you run the code in the same AWS Region in which you created the Lambda function.
You can view the AWS Region for your Lambda function in the navigation bar of the function details page in the Lambda console.

If the Lambda function returns a timeout error, extend the timeout period for the Lambda
function. For more information, see
[Configuring function timeout (console)](../../../lambda/latest/dg/configuration-function-common.md#configuration-timeout-console "../../../lambda/latest/dg/configuration-function-common.md#configuration-timeout-console").

For more information about invoking a Lambda function from your code, see [Invoking AWS Lambda
Functions](../../../lambda/latest/dg/lambda-invocation.md "../../../lambda/latest/dg/lambda-invocation.md").

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
       see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2.  Save the following code to a file named `client.py`:

```
import boto3
import json
import base64
import pprint

# Replace with the name of your S3 bucket and image object key
bucket_name = "name of bucket"
object_key = "name of file in s3 bucket"
# If using a local file, supply the file name as the value of image_path below
image_path = ""

# Create session and establish connection to client['
session = boto3.Session(profile_name='developer-role')
s3 = session.client('s3', region_name="us-east-1")
lambda_client = session.client('lambda',  region_name="us-east-1")

# Replace with the name of your Lambda function
function_name = 'RekDetectLabels'

def analyze_image_local(img_path):

    print("Analyzing local image:")

    with open(img_path, 'rb') as image_file:
        image_bytes = image_file.read()
        data = base64.b64encode(image_bytes).decode("utf8")

        lambda_payload = {"image": data}

        # Invoke the Lambda function with the event payload
        response = lambda_client.invoke(
            FunctionName=function_name,
            Payload=(json.dumps(lambda_payload))
        )

        decoded = json.loads(response['Payload'].read().decode())
        pprint.pprint(decoded)

def analyze_image_s3(bucket_name, object_key):

    print("Analyzing image in S3 bucket:")

    # Load the image data from S3 into memory
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    image_data = response['Body'].read()
    image_data = base64.b64encode(image_data).decode("utf8")

     # Create the Lambda event payload
    event = {
        'S3Bucket': bucket_name,
        'S3Object': object_key,
        'ImageBytes': image_data
    }

    # Invoke the Lambda function with the event payload
    response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(event),
            )

    decoded = json.loads(response['Payload'].read().decode())
    pprint.pprint(decoded)

def main(path_to_image, name_s3_bucket, obj_key):

    if str(path_to_image) != "":
        analyze_image_local(path_to_image)
    else:
        analyze_image_s3(name_s3_bucket, obj_key)

if __name__ == "__main__":
    main(image_path, bucket_name, object_key)
```

3. Run the code. If the document is in an Amazon S3 bucket. make sure that it is the same bucket
   that you specified previously in step 12 of .

If successful, your code returns a partial JSON response for each Block
type detected in the document.
