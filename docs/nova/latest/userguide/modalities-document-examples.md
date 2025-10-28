# Document understanding examples

The following example demonstrates how to invoke document understanding. Note that this example includes a question about projected growth that the model will attempt to answer regardless of what content is in your document.

```
`import base64
import json
import boto3

client = boto3.client(
 "bedrock-runtime",
 region_name="us-east-1",
)
MODEL_ID = "us.amazon.nova-lite-v1:0"

with open('`my_document.pdf`', "rb") as file:
 doc_bytes = file.read()
messages =[
 {
 "role": "user",
 "content": [
 {
 "document": {
 "format": "pdf",
 "name": "DocumentPDFmessages",
 "source": {
 "bytes": doc_bytes
 }
 }
 },
 {
 "text": """`How many qubits of growth is projected by 2026 by the industry, and how does the actual trajectory differ?`"""
 }
 ]
}

]

inf_params = {"maxTokens": 300, "topP": 0.1, "temperature": 0.3}

model_response = client.converse(modelId=MODEL_ID, messages=messages, inferenceConfig=inf_params)

print("\n[Full Response]")
print(json.dumps(model_response, indent=2))

print("\n[Response Content Text]")
print(model_response['output']['message']['content'][0]['text'])`
```

For passing large document files or multiple document files, where the overall payload is greater than 25 MB, you can use Amazon S3. The following example demonstrates how to use Amazon S3 to upload documents to Amazon Nova:

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
 "document": {
 "format": "pdf",
 "name": "sample_doc",
 "source": {
 "s3Location": {
 #Replace the s3 bucket URI
 "uri": "`s3://demo-bucket/document1.pdf`",
 "bucketOwner" : "`123456789012`"
 }
 }
 }
 },
 {"text": "Describe the following document"}
 ]
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

###### Note

Document names can include only alphanumeric characters, hyphens, parentheses, and square brackets.

The `name` field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.
