# Single-shot video generation examples

The following examples provide sample code for various single-shot (6 seconds) video generation tasks.

Text to video

```
`# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import boto3

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client("bedrock-runtime")

model_input = {
 "taskType": "TEXT_VIDEO",
 "textToVideoParams": {
 "text": "Closeup of a large seashell in the sand, gentle waves flow around the shell. Camera zoom in."
 },
 "videoGenerationConfig": {
 "durationSeconds": 6,
 "fps": 24,
 "dimension": "1280x720",
 "seed": 0, # Change the seed to get a different result
 },
}
try:
 # Start the asynchronous video generation job.
 invocation = bedrock_runtime.start_async_invoke(
 modelId="amazon.nova-reel-v1:1",
 modelInput=model_input,
 outputDataConfig={
 "s3OutputDataConfig": {
 "s3Uri": "s3://my-nova-videos"
 }
 }
 )

 # Print the response JSON.
 print("Response:")
 print(json.dumps(invocation, indent=2, default=str))

except Exception as e:
 # Implement error handling here.
 message = e.response["Error"]["Message"]
 print(f"Error: {message}")`
```

Image to video

```
`# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import json
import boto3
import base64

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client("bedrock-runtime")

# Load the input image as a Base64 string. Note, the image resolution
# must be exactly 1280x720.
input_image_path = "images/first-frame.png"
with open(input_image_path, "rb") as f:
 input_image_bytes = f.read()
 input_image_base64 = base64.b64encode(input_image_bytes).decode("utf-8")

model_input = {
 "taskType": "TEXT_VIDEO",
 "textToVideoParams": {
 "text": "Dolly forward over a gentle river",
 "images": [
 {
 "format": "png",
 "source": {
 "bytes": input_image_base64
 }
 }
 ]
 },
 "videoGenerationConfig": {
 "durationSeconds": 6,
 "fps": 24,
 "dimension": "1280x720",
 "seed": 0
 },
}

# Start the asynchronous video generation job.
invocation = bedrock_runtime.start_async_invoke(
 modelId="amazon.nova-reel-v1:1",
 modelInput=model_input,
 outputDataConfig={
 "s3OutputDataConfig": {
 "s3Uri": "s3://my-nova-videos"
 }
 },
)

# Print the response JSON.
print("Response:")
print(json.dumps(invocation, indent=2, default=str))`
```

Query job status

```
`import json
import boto3

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client("bedrock-runtime")

invocation = bedrock_runtime.get_async_invoke(
 invocationArn="arn:AWS:bedrock:us-east-1:`account-id`:async-invoke/`invocation-id`"
)

# Print the JSON response
print(json.dumps(invocation, indent=2, default=str))

invocation_arn = invocation["invocationArn"]
status = invocation["status"]
if (status == "Completed"):
 bucket_uri = invocation["outputDataConfig"]["s3OutputDataConfig"]["s3Uri"]
 video_uri = bucket_uri + "/output.mp4"
 print(f"Video is available at: {video_uri}")

elif (status == "InProgress"):
 start_time = invocation["submitTime"]
 print(f"Job {invocation_arn} is in progress. Started at: {start_time}")

elif (status == "Failed"):
 failure_message = invocation["failureMessage"]
 print(f"Job {invocation_arn} failed. Failure message: {failure_message}")`
```

Listing jobs

```
`import json
import boto3

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client("bedrock-runtime")

# List the 10 most recently completed jobs.
completed_jobs = bedrock_runtime.list_async_invokes(
 maxResults=10, # (Optional)
 statusEquals="Completed", # (Optional) Can be "Completed", "InProgress", or "Failed".
 # Omit this argument to list all jobs, regardless of status.
 # Note: There are other supported arguments not demonstrated here.
)

# Print the JSON response
print(json.dumps(completed_jobs, indent=2, default=str))

# Loop through the completed jobs and print their invocation ARNs.
for job in completed_jobs["asyncInvokeSummaries"]:
 print(job["invocationArn"])`
```

Text to video using REST API

```
`# Invoke the Amazon Nova Reel model to create a video and monitor the status
# of the async job.

# tested with Python 3.12
import json
import time
import uuid
import boto3
import requests as req
import botocore.session

from botocore.auth import SigV4Auth
from typing import Dict, List, Tuple
from botocore.awsrequest import AWSRequest

## ------ Initialize constants to invoke the general async function to call REST APIs for Bedrock ------------
SERVICE_NAME: str = 'bedrock'
MAX_TIME: int = 3600
BUCKET_FOR_VIDEO_CONTENT: str = "s3://`your-bucket-name-here`"
# Region and model id to use
REGION: str = 'us-east-1'
MODEL_ID: str = 'amazon.nova-reel-v1:1'

## ------------------------------------------------------------------------------------------------------------

def get_inference(model_id: str, region: str, payload: List) -> Tuple:
 print(f"making an inference request to {model_id}, payload={payload}")
 try:
 ## Initialize the runtime rest API to be called for the endpoint
 endpoint: str = f"https://{SERVICE_NAME}-runtime.{region}.amazonaws.com/async-invoke"
 print(endpoint)
 #endpoint = f"https://{SERVICE_NAME}-runtime.{region}.amazonaws.com/model/{model_id}/async-invoke"

 # Converting the payload dictionary into a JSON-formatted string to be sent in the HTTP request
 request_body = json.dumps(payload[1])
 print(json.dumps(payload[1], indent=2))

 # Creating an AWSRequest object for a POST request with the service specified endpoint, JSON request body, and HTTP headers
 request = AWSRequest(method='POST',
 url=endpoint,
 data=request_body,
 headers={'content-type': 'application/json'})

 # Initializing a botocore session
 session = botocore.session.Session()

 # Adding a SigV4 authentication information to the AWSRequest object, signing the request
 sigv4 = SigV4Auth(session.get_credentials(), SERVICE_NAME, region)
 sigv4.add_auth(request)

 # Prepare the request by formatting it correctly
 prepped = request.prepare()

 # Send the HTTP POST request to the prepared URL with the specified headers and JSON-formatted request body, storing the response
 response = req.post(prepped.url, headers=prepped.headers, data=request_body)

 if response.status_code == 200:
 return (payload[0], response.json())
 else:
 print(f"Error: Received status code {response.status_code}, Response: {response.text}")
 return None
 except Exception as e:
 print(f"Exception occurred: {e}")
 return None


def print_async_job_status(arn, region=REGION):
 # Create the Bedrock Runtime client.
 bedrock_runtime = boto3.client("bedrock-runtime", region_name=region)

 invocation = bedrock_runtime.get_async_invoke(
 invocationArn=arn
 )

 # Print the JSON response
 print(json.dumps(invocation, indent=2, default=str))

 invocation_arn = invocation["invocationArn"]
 status = invocation["status"]
 if (status == "Completed"):
 bucket_uri = invocation["outputDataConfig"]["s3OutputDataConfig"]["s3Uri"]
 video_uri = bucket_uri + "/output.mp4"
 print(f"Video is available at: {video_uri}")

 elif (status == "InProgress"):
 start_time = invocation["submitTime"]
 print(f"Job {invocation_arn} is in progress. Started at: {start_time}")

 elif (status == "Failed"):
 failure_message = invocation["failureMessage"]
 print(f"Job {invocation_arn} failed. Failure message: {failure_message}")
 return status

# Function to create the payload
def create_payload(prompt: str, model_id: str, bucket: str) -> Dict:

 payload = {
 "modelId": model_id,
 "modelInput": {
 "taskType": "TEXT_VIDEO",
 "textToVideoParams": {
 "text": prompt
 },
 "videoGenerationConfig": {
 "durationSeconds": 6,
 "fps": 24,
 "dimension": "1280x720",
 "seed": 0
 }
 },
 "outputDataConfig": {
 "s3OutputDataConfig": {
 "s3Uri": bucket
 }
 },
 "clientRequestToken": str(uuid.uuid4())
 }
 return payload

## Initialize the number of prompts you want to invoke on the bedrock specific model
prompts = ["galaxies receding", "event horizon of a black hole"]
payloads: List = [(i, create_payload(p, MODEL_ID, BUCKET_FOR_VIDEO_CONTENT)) for i, p in enumerate(prompts)]

# Start timing before sending the request
print(f"going to make {len(prompts)} requests")
start_time = time.perf_counter()
responses = [get_inference(MODEL_ID, REGION, prompt) for prompt in payloads]
# Calculate the elapsed time
elapsed_time = time.perf_counter() - start_time
print(f"Total time taken for {len(prompts)} calls made: {elapsed_time:.2f} seconds")

invocation_arns = []
for r in responses:
 print(f"response={r}")
 invocation_arns.append(r[1]['invocationArn'])

jobs_total = len(invocation_arns)
jobs_completed = 0
st = time.time()
while True:
 for arn in invocation_arns:
 status = print_async_job_status(arn)
 print(f"arn={arn}, status={status}")
 if status == "Completed":
 jobs_completed += 1
 if jobs_completed == jobs_total:
 print(f"all jobs completed, exiting")
 break
 if time.time() - st > MAX_TIME:
 print(f"{MAX_TIME}s elapsed but seems like all jobs are still not completed, exiting")
 break
 time.sleep(60)
print("all done")`
```
