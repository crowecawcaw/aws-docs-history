# Image understanding examples

The following example shows how to send a image prompt to Amazon Nova Model with [InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md").

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
with open("media/sunset.png", "rb") as image_file:
 binary_data = image_file.read()
 base_64_encoded_data = base64.b64encode(binary_data)
 base64_string = base_64_encoded_data.decode("utf-8")
# Define your system prompt(s).
system_list = [ {
 "text": "You are an expert artist. When the user provides you with an image, provide 3 potential art titles"
 }
]
# Define a "user" message including both the image and a text prompt.
message_list = [
 {
 "role": "user",
 "content": [
 {
 "image": {
 "format": "png",
 "source": {
 "bytes": image // Binary array (Converse API) or Base64-encoded string (Invoke API)
 },
 }
 },
 {
 "text": "Provide art titles for this image."
 }
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

For passing large image files or multiple image files, where the overall payload is greater than 25 MB, you can use Amazon S3. The following example demonstrates how to use Amazon S3 to upload images to Amazon Nova:

```
`import boto3
import json
import base64
# Create a Bedrock Runtime client
client = boto3.client("bedrock-runtime",
 region_name="us-east-1",
 )
PRO_MODEL_ID = "us.amazon.nova-pro-v1:0"
LITE_MODEL_ID = "us.amazon.nova-lite-v1:0"
MICRO_MODEL_ID = "us.amazon.nova-micro-v1:0"
PREMIER_MODEL_ID = "us.amazon.nova-premier-v1:0"
messages = [
 {
 "role": "user",
 "content": [
 {
 "image": {
 "format": "png",
 "source": {
 "s3Location": {
 #Replace the s3 bucket URI
 "uri": "`s3://demo-bucket/cat.png`"
 "bucketOwner" : "`123456789012`"
 }
 },
 }
 },
 {"text": "Describe the following image"},
 ],
 }
]
inf_params = {"maxTokens": 300, "topP": 0.1, "temperature": 0.3}
model_response = client.converse(
 modelId=LITE_MODEL_ID, messages=messages, inferenceConfig=inf_params
)
print("\n[Full Response]")
print(json.dumps(model_response, indent=2))
print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])`
```
