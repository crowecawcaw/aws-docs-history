# Using Nova's Document Understanding via API

To illustrate how to use Amazon Nova for document QA (Question-Answering) or analysis, here’s a simplified example in Python.
We’ll use the AWS Bedrock API (via Boto3 SDK) to send a PDF document along with a question for the model to answer.

```

            `import base64
import base64
import json
import boto3

# Initialize Bedrock runtime client (adjust region as needed)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "us.amazon.nova-lite-v1:5" # using Nova Lite model in this example

# Read the document file (PDF) in binary mode
with open("my_document.pdf", "rb") as file:
 doc_bytes = file.read()

# Construct the conversation messages with document + question
messages = [
 {
 "role": "user",
 "content": [
 {
 "document": {
 "format": "pdf",
 "name": "Document1", # neutral name for the document
 "source": {
 "bytes": doc_bytes # embedding the PDF content directly
 }
 }
 },
 {
 "text": "Here is a question about the document: ... (your question) ... ?"
 }
 ]
 }
]

# Set inference parameters (optional)
inf_params = {"maxTokens": 4000, "topP": 0.1, "temperature": 0.3}

# Invoke the model
response = client.converse(modelId=MODEL_ID, messages=messages, inferenceConfig=inf_params)

# Extract and print the answer
answer_text = response["output"]["message"]["content"][0]["text"]
print(answer_text)`
```

If your input files are large (exceeding the 25 MB direct upload limit) or you have many files, you can store them in Amazon S3 and reference them.
This avoids sending the raw bytes over the request. When using S3, ensure the Bedrock service has permission to access the bucket/object. For example,
to reference a PDF in S3, your document source would use "s3Location" instead of "bytes", like so:

```
`messages = [
 {
 "role": "user",
 "content": [
 {
 "document": {
 "format": "pdf",
 "name": "Report2023",
 "source": {
 "s3Location": {
 "uri": "s3://your-bucket/path/to/document1.pdf",
 "bucketOwner": "123456789012"
 }
 }
 }
 },
 {
 "text": "Summarize the key findings from the Q3 2023 report."
 }
 ]
 }
]`
```

###### Note

Document names can include only alphanumeric characters, hyphens, parentheses, and square brackets.

The `name` field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.
