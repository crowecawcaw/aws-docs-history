# Video understanding examples

The following example shows how to send a video prompt to Amazon Nova Model with [InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md").

```
`# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import base64
import boto3
import json
# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client(
 "bedrock-runtime",
 region_name="us-east-1",
)

MODEL_ID = "us.amazon.nova-lite-v1:0"
# Open the image you'd like to use and encode it as a Base64 string.
with open("media/cooking-quesadilla.mp4", "rb") as video_file:
 binary_data = video_file.read()
 base_64_encoded_data = base64.b64encode(binary_data)
 base64_string = base_64_encoded_data.decode("utf-8")
# Define your system prompt(s).
system_list= [
 {
 "text": "You are an expert media analyst. When the user provides you with a video, provide 3 potential video titles"
 }
]
# Define a "user" message including both the image and a text prompt.
message_list = [
 {
 "role": "user",
 "content": [
 {
 "video": {
 "format": "mp4",
 "source": {
 "bytes": video // Binary array (Converse API) or Base64-encoded string (Invoke API)
 },
 }
 },
 {
 "text": "Provide video titles for this clip."
 },
 ],
 }
]
# Configure the inference parameters.
inf_params = {"maxTokens": 300, "topP": 0.1, "topK": 20, "temperature": 0.3}

native_request = {
 "schemaVersion": "messages-v1",
 "messages": message_list,
 "system": system_list,
 "inferenceConfig": inf_params,
}
# Invoke the model and extract the response body.
response = client.invoke_model(modelId=MODEL_ID, body=json.dumps(native_request))
model_response = json.loads(response["body"].read())
# Pretty print the response JSON.
print("[Full Response]")
print(json.dumps(model_response, indent=2))
# Print the text content for easy readability.
content_text = model_response["output"]["message"]["content"][0]["text"]
print("\n[Response Content Text]")
print(content_text)`
```

The following example shows how to send a video using an Amazon S3 location to Amazon Nova
with [InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md").

```
`import base64
import boto3
import json
# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client(
 "bedrock-runtime",
 region_name="us-east-1",
)

MODEL_ID = "us.amazon.nova-lite-v1:0"
# Define your system prompt(s).
system_list = [
 {
 "text": "You are an expert media analyst. When the user provides you with a video, provide 3 potential video titles"
 }
]
# Define a "user" message including both the image and a text prompt.
message_list = [
 {
 "role": "user",
 "content": [
 {
 "video": {
 "format": "mp4",
 "source": {
 "s3Location": {
 "uri": "`s3://my_bucket/my_video.mp4`",
 "bucketOwner": "`111122223333`"
 }
 }
 }
 },
 {
 "text": "Provide video titles for this clip."
 }
 ]
 }
]
# Configure the inference parameters.
inf_params = {"maxTokens": 300, "topP": 0.1, "topK": 20, "temperature": 0.3}

native_request = {
 "schemaVersion": "messages-v1",
 "messages": message_list,
 "system": system_list,
 "inferenceConfig": inf_params,
}
# Invoke the model and extract the response body.
response = client.invoke_model(modelId=MODEL_ID, body=json.dumps(native_request))
model_response = json.loads(response["body"].read())
# Pretty print the response JSON.
print("[Full Response]")
print(json.dumps(model_response, indent=2))
# Print the text content for easy readability.
content_text = model_response["output"]["message"]["content"][0]["text"]
print("\n[Response Content Text]")
print(content_text)`
```
