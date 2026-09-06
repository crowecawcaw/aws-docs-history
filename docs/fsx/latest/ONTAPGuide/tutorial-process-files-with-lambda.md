

# Process files serverlessly using Lambda
<a name="tutorial-process-files-with-lambda"></a>

File processing workflows often start with files that arrive on an NFS or SMB file share — scanned documents from branch offices, images uploaded by field teams, audio captured from contact centers, or data files delivered by partners.

With an Amazon S3 access point attached to the FSx for ONTAP volume, AWS Lambda functions read and write the files directly using the Amazon S3 API. File-level operations can be processed serverlessly against the same data your users and applications access over NFS and SMB.

This tutorial shows three common file processing patterns. Each example reads a file from the volume through the access point, processes it with an AWS service or library, and writes the result back to the volume.


| Example | Input | Processing | Output | 
| --- | --- | --- | --- | 
| [Example 1: Generate image thumbnails](#tutorial-lambda-thumbnail) | JPEG image | Pillow (image library) | Resized thumbnail | 
| [Example 2: Extract text from documents](#tutorial-lambda-textract) | PDF document | Amazon Textract | Extracted text (JSON) | 
| [Example 3: Transcribe audio files](#tutorial-lambda-transcribe) | MP3 audio | Amazon Transcribe | Transcript (JSON) | 

**Note**  
This tutorial takes approximately **40 to 60 minutes** to complete. The AWS services used incur charges for the resources you create. If you complete all the steps, including the **Clean up** section promptly, the expected cost is less than **$1** in the US East (N. Virginia) AWS Region. This estimate does not include ongoing charges for the FSx for ONTAP volume itself.

## Prerequisites
<a name="tutorial-lambda-prerequisites"></a>

Before you begin, make sure you have the following:
+ An FSx for ONTAP volume with an Amazon S3 access point attached. For instructions on creating an access point, see [Creating an access point](fsxn-creating-access-points.md).
+ The access point alias for your access point. You can find this in the Amazon FSx console or by running `aws fsx describe-s3-access-point-attachments`.
+ AWS CLI version 1 or version 2 installed and configured. The `aws lambda invoke` commands in this tutorial include the `--cli-binary-format raw-in-base64-out` option, which is required in AWS CLI version 2 so that raw JSON payloads are not interpreted as base64. If you use AWS CLI version 1, omit that option.
+ IAM permissions for the caller (the user or role running this tutorial) to invoke Lambda functions (`lambda:CreateFunction`, `lambda:InvokeFunction`), access the Amazon S3 access point (`s3:GetObject`, `s3:PutObject`), and pass the Lambda execution role (`iam:PassRole`).

**Note**  
This tutorial uses the default Lambda configuration, where functions run in a managed network outside your VPC. In that case, the access point must have an **internet** network origin so the function can reach it. If you attach your Lambda function to a VPC, you can instead use a VPC network origin on the access point; the VPC must have an Amazon S3 Gateway or Interface endpoint. For more information, see [Configuring network access for Amazon S3 access points](configuring-network-access-for-s3-access-points.md).

## Step 1: Upload sample files
<a name="tutorial-lambda-upload-samples"></a>

Download the following sample files and upload them to your FSx for ONTAP volume through the access point. Replace `{{my-ap-alias-ext-s3alias}}` with your access point alias throughout this tutorial.
+ **Sample image:** Download the [NASA Blue Marble image](https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73909/world.topo.bathy.200412.3x5400x2700.jpg) (public domain, 2.4 MB) and save it as `sample-image.jpg`.
+ **Sample audio:** Download the [sample audio file](https://d1.awsstatic.com/tmt/create-audio-transcript-transcribe/transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3) from the [Amazon Transcribe getting started tutorial](https://docs.aws.amazon.com/hands-on/latest/create-audio-transcript-transcribe/create-audio-transcript-transcribe.html) (410 KB) and save it as `sample-audio.mp3`.

Upload the sample files to your FSx for ONTAP volume through the access point.

```
$ aws s3 cp sample-image.jpg s3://{{my-ap-alias-ext-s3alias}}/samples/images/sample-image.jpg
aws s3 cp sample-audio.mp3 s3://{{my-ap-alias-ext-s3alias}}/samples/audio/sample-audio.mp3
```

**Note**  
The sample image is a NASA Blue Marble photograph (public domain, 2.4 MB). The sample audio is from the [Amazon Transcribe getting started tutorial](https://docs.aws.amazon.com/hands-on/latest/create-audio-transcript-transcribe/create-audio-transcript-transcribe.html) (410 KB). The sample PDF is generated in [Example 2: Extract text from documents](#tutorial-lambda-textract).

## Step 2: Create the Lambda execution role
<a name="tutorial-lambda-create-role"></a>

Lambda functions assume an execution role to interact with other AWS services. For this tutorial, attach the AWS-managed `AWSLambdaBasicExecutionRole` policy for CloudWatch Logs logging, then add an inline policy that grants access to the Amazon S3 access point and to the Textract and Transcribe APIs the examples use.

### To create the Lambda execution role
<a name="tutorial-lambda-create-role-steps"></a>

Replace `{{region}}`, `{{account-id}}`, and `{{access-point-name}}` with your values.

1. Save the following trust policy as `trust-policy.json`.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {"Service": "lambda.amazonaws.com"},
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

1. Save the following inline permissions policy as `permissions-policy.json`. It grants access to the access point and to the additional services the examples use.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": ["s3:GetObject", "s3:PutObject", "s3:ListBucket"],
               "Resource": [
                   "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}",
                   "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": ["textract:DetectDocumentText"],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "transcribe:StartTranscriptionJob",
                   "transcribe:GetTranscriptionJob"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

1. Create the role, attach the managed logging policy, and attach the inline policy.

   ```
   $ aws iam create-role \
       --role-name {{fsxn-lambda-file-processor}} \
       --assume-role-policy-document file://trust-policy.json
   
   aws iam attach-role-policy \
       --role-name {{fsxn-lambda-file-processor}} \
       --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   
   aws iam put-role-policy \
       --role-name {{fsxn-lambda-file-processor}} \
       --policy-name fsxn-access-point-policy \
       --policy-document file://permissions-policy.json
   ```

## Integrating into your workflow
<a name="tutorial-lambda-workflow-integration"></a>

The examples in this tutorial use manual invocation with a test event. In production, you can trigger these functions automatically using the following approaches:
+ **Amazon EventBridge schedule.** Run the function on a recurring schedule (for example, every hour or daily) to process new files. The function can list files through the access point and process any that have not been processed yet. For more information, see [Schedule Lambda functions using EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html) in the *Amazon EventBridge User Guide*.
+ **Amazon API Gateway.** Expose the function as an HTTP API so that users or applications can request processing of a specific file on demand. For more information, see [Build an API Gateway REST API with Lambda integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html) in the *Amazon API Gateway Developer Guide*.
+ **Step Functions.** Orchestrate multi-step file processing pipelines that combine multiple Lambda functions. For example, a workflow that extracts text from a document, translates it, and writes the result back to the volume. For more information, see [Call Lambda with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html) in the *AWS Step Functions Developer Guide*.

## Example 1: Generate image thumbnails
<a name="tutorial-lambda-thumbnail"></a>

This example reads a JPEG image from your FSx for ONTAP volume, resizes it to a 200-pixel thumbnail using the Pillow image library, and writes the thumbnail back to the volume.

**Lambda function code**

Save the following code as `lambda_function.py`.

```
import boto3
from io import BytesIO
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['access_point_alias']
    key = event['key']

    # Read the image from FSx through the access point
    response = s3.get_object(Bucket=bucket, Key=key)
    image_data = response['Body'].read()

    # Resize to thumbnail
    img = Image.open(BytesIO(image_data))
    img.thumbnail((200, 200))

    # Write the thumbnail back to FSx
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    buffer.seek(0)

    thumbnail_key = key.rsplit('.', 1)[0] + '_thumbnail.jpg'
    s3.put_object(
        Bucket=bucket,
        Key=thumbnail_key,
        Body=buffer.getvalue(),
        ContentType='image/jpeg'
    )

    return {
        'original_size': len(image_data),
        'thumbnail_size': len(buffer.getvalue()),
        'thumbnail_key': thumbnail_key
    }
```

**Create and invoke the function**

This function requires the Pillow library. Create a deployment package that includes Pillow built for the Lambda Linux runtime.

```
$ # Create a deployment package with Pillow for Lambda (Linux)
mkdir package && pip install Pillow -t package/ \
    --platform manylinux2014_x86_64 --only-binary=:all:
cd package && zip -r ../thumbnail-function.zip .
cd .. && zip thumbnail-function.zip lambda_function.py

# Create the function
aws lambda create-function \
    --function-name {{fsxn-thumbnail-generator}} \
    --runtime python3.12 \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::{{account-id}}:role/{{fsxn-lambda-file-processor}} \
    --zip-file fileb://thumbnail-function.zip \
    --timeout 30 \
    --memory-size 256

# Invoke with a test event
aws lambda invoke \
    --function-name {{fsxn-thumbnail-generator}} \
    --cli-binary-format raw-in-base64-out \
    --payload '{"access_point_alias": "{{my-ap-alias-ext-s3alias}}", "key": "samples/images/sample-image.jpg"}' \
    response.json

cat response.json
```

**Verify the result**

```
$ aws s3 ls s3://{{my-ap-alias-ext-s3alias}}/samples/images/
2024-01-23 12:19:32    2566770 sample-image.jpg
2024-01-23 12:25:49       7065 sample-image_thumbnail.jpg
```

The original 2.4 MB image (5400 × 2700 pixels) was resized to a 7 KB thumbnail (200 × 100 pixels).

## Example 2: Extract text from documents
<a name="tutorial-lambda-textract"></a>

This example reads a PDF document from your FSx for ONTAP volume, sends it to Amazon Textract to extract the text, and writes the extracted text as a JSON file back to the volume.

**Create and upload a sample PDF**

For this example, you need a PDF document on your FSx for ONTAP volume. The following Python script generates a simple invoice PDF and uploads it through the access point. Run this script on your local machine (not in Lambda).

```
$ pip install fpdf2 boto3
```

```
# create_invoice.py — run locally to generate and upload a sample PDF
from fpdf import FPDF
import boto3

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 15, "INVOICE", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.set_font("Helvetica", "", 12)
pdf.cell(0, 8, "Invoice Number: INV-2024-00142", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 8, "Date: January 15, 2024", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 8, "Customer: Example Corp", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_font("Helvetica", "B", 12)
pdf.cell(80, 8, "Description", border=1)
pdf.cell(30, 8, "Qty", border=1, align="C")
pdf.cell(40, 8, "Unit Price", border=1, align="R")
pdf.cell(40, 8, "Amount", border=1, align="R")
pdf.ln()
pdf.set_font("Helvetica", "", 12)
for desc, qty, price, amt in [
    ("Cloud Storage Service", "1", "$2,400.00", "$2,400.00"),
    ("Data Transfer (TB)", "5", "$90.00", "$450.00"),
    ("Technical Support", "1", "$500.00", "$500.00"),
]:
    pdf.cell(80, 8, desc, border=1)
    pdf.cell(30, 8, qty, border=1, align="C")
    pdf.cell(40, 8, price, border=1, align="R")
    pdf.cell(40, 8, amt, border=1, align="R")
    pdf.ln()

s3 = boto3.client('s3')
s3.put_object(
    Bucket='{{my-ap-alias-ext-s3alias}}',
    Key='samples/documents/invoice.pdf',
    Body=pdf.output(),
    ContentType='application/pdf'
)
print("Uploaded invoice.pdf")
```

```
$ python3 create_invoice.py
```

**Lambda function code**

Save the following code as `lambda_function.py`.

```
import boto3
import json

s3 = boto3.client('s3')
textract = boto3.client('textract')

def lambda_handler(event, context):
    bucket = event['access_point_alias']
    key = event['key']

    # Read the PDF from FSx through the access point
    response = s3.get_object(Bucket=bucket, Key=key)
    document_bytes = response['Body'].read()

    # Extract text with Textract
    textract_response = textract.detect_document_text(
        Document={'Bytes': document_bytes}
    )

    lines = [
        block['Text']
        for block in textract_response['Blocks']
        if block['BlockType'] == 'LINE'
    ]

    # Write extracted text as JSON back to FSx
    result = {
        'source_file': key,
        'total_lines': len(lines),
        'extracted_text': lines
    }

    output_key = key.rsplit('.', 1)[0] + '_extracted.json'
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=json.dumps(result, indent=2),
        ContentType='application/json'
    )

    return {
        'lines_extracted': len(lines),
        'output_key': output_key
    }
```

**Create and invoke the function**

```
$ zip textract-function.zip lambda_function.py

aws lambda create-function \
    --function-name {{fsxn-text-extractor}} \
    --runtime python3.12 \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::{{account-id}}:role/{{fsxn-lambda-file-processor}} \
    --zip-file fileb://textract-function.zip \
    --timeout 30 \
    --memory-size 256

aws lambda invoke \
    --function-name {{fsxn-text-extractor}} \
    --cli-binary-format raw-in-base64-out \
    --payload '{"access_point_alias": "{{my-ap-alias-ext-s3alias}}", "key": "samples/documents/invoice.pdf"}' \
    response.json

cat response.json
```

Example output:

```
{"lines_extracted": 22, "output_key": "samples/documents/invoice_extracted.json"}
```

## Example 3: Transcribe audio files
<a name="tutorial-lambda-transcribe"></a>

This example starts an Amazon Transcribe job for an audio file stored on your FSx for ONTAP volume. Amazon Transcribe reads the audio file directly from the access point using the access point alias in the media file URI. When the job completes, the function writes the transcript back to the volume.

**Lambda function code**

Save the following code as `lambda_function.py`.

```
import boto3
import json
import time
import urllib.request

s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    bucket = event['access_point_alias']
    key = event['key']
    media_format = key.rsplit('.', 1)[-1]  # mp3, wav, etc.

    # Start a Transcribe job pointing to the file on FSx
    job_name = f"fsxn-{int(time.time())}"
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': f's3://{bucket}/{key}'},
        MediaFormat=media_format,
        LanguageCode='en-US'
    )

    # Wait for the job to complete
    while True:
        status = transcribe.get_transcription_job(
            TranscriptionJobName=job_name
        )
        state = status['TranscriptionJob']['TranscriptionJobStatus']
        if state in ('COMPLETED', 'FAILED'):
            break
        time.sleep(5)

    if state == 'FAILED':
        raise Exception(
            status['TranscriptionJob'].get('FailureReason', 'Unknown error')
        )

    # Download the transcript
    transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    with urllib.request.urlopen(transcript_uri) as resp:
        transcript_data = json.loads(resp.read())

    transcript_text = transcript_data['results']['transcripts'][0]['transcript']

    # Write the transcript back to FSx
    result = {
        'source_file': key,
        'job_name': job_name,
        'transcript': transcript_text
    }

    output_key = key.rsplit('.', 1)[0] + '_transcript.json'
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=json.dumps(result, indent=2),
        ContentType='application/json'
    )

    return {
        'transcript_length': len(transcript_text),
        'output_key': output_key
    }
```

**Create and invoke the function**

```
$ zip transcribe-function.zip lambda_function.py

aws lambda create-function \
    --function-name {{fsxn-audio-transcriber}} \
    --runtime python3.12 \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::{{account-id}}:role/{{fsxn-lambda-file-processor}} \
    --zip-file fileb://transcribe-function.zip \
    --timeout 120

aws lambda invoke \
    --function-name {{fsxn-audio-transcriber}} \
    --cli-binary-format raw-in-base64-out \
    --payload '{"access_point_alias": "{{my-ap-alias-ext-s3alias}}", "key": "samples/audio/sample-audio.mp3"}' \
    --cli-read-timeout 180 \
    response.json

cat response.json
```

**Note**  
The Transcribe job typically takes 15 to 45 seconds to complete. The function's timeout is set to 120 seconds to allow for this.

## Considerations
<a name="tutorial-lambda-considerations"></a>
+ **Internet origin required for default configuration.** By default, Lambda accesses Amazon S3 from managed infrastructure outside your VPC, which requires an internet-origin access point. If you attach your Lambda function to a VPC, you can use a VPC-origin access point instead. See the prerequisites for details.
+ **File size limits.** Lambda functions have a maximum memory of 10 GB and a maximum execution time of 15 minutes. For large files, consider using range reads (`GetObject` with `Range` header) or streaming the response.
+ **Textract limits.** The synchronous `DetectDocumentText` API accepts documents up to 10 MB and 1 page. For multi-page documents, use the asynchronous `StartDocumentTextDetection` API.
+ **Transcribe reads directly from the access point.** Amazon Transcribe accepts the access point alias in the `MediaFileUri` parameter (`s3://{{ap-alias}}/{{key}}`). The Lambda function does not need to download and re-upload the audio file.
+ **File system user permissions.** The file system user associated with the access point must have read permission on input files and write permission on output directories.

## Clean up
<a name="tutorial-lambda-clean-up"></a>

To avoid ongoing charges, delete the resources you created in this tutorial.

```
$ # Delete Lambda functions
aws lambda delete-function --function-name {{fsxn-thumbnail-generator}}
aws lambda delete-function --function-name {{fsxn-text-extractor}}
aws lambda delete-function --function-name {{fsxn-audio-transcriber}}

# Delete the IAM role and policies
aws iam delete-role-policy \
    --role-name {{fsxn-lambda-file-processor}} \
    --policy-name fsxn-access-point-policy
aws iam detach-role-policy \
    --role-name {{fsxn-lambda-file-processor}} \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam delete-role --role-name {{fsxn-lambda-file-processor}}

# Delete sample files from your FSx volume
aws s3 rm s3://{{my-ap-alias-ext-s3alias}}/samples/ --recursive
```