# Run example Amazon Bedrock API requests using an Amazon SageMaker AI notebook

This section guides you through trying out some common operations in Amazon Bedrock with an Amazon SageMaker AI notebook to test that your Amazon Bedrock role permissions are set up properly. Before you run the following examples, you should check that you have fulfilled the following prerequisites:

**Prerequisites**

- You have an AWS account and have permissions to access a role with the necessary permissions for Amazon Bedrock. Otherwise, follow the steps at [I already have an AWS account](getting-started.md#getting-started-bedrock-role "getting-started.md#getting-started-bedrock-role").
- Carry out the following steps to set up IAM permissions for SageMaker AI and create a notebook:

      1. Modify the [trust policy](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#term_trust-policy "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#term_trust-policy") of the Amazon Bedrock role that you set up in [I already have an AWS account](getting-started.md#getting-started-bedrock-role "getting-started.md#getting-started-bedrock-role") through the [console](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-managingrole_edit-trust-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-managingrole_edit-trust-policy"), [CLI](../../../IAM/latest/UserGuide/roles-managingrole-editing-cli.md#roles-managingrole_edit-trust-policy-cli "../../../IAM/latest/UserGuide/roles-managingrole-editing-cli.md#roles-managingrole_edit-trust-policy-cli"), or [API](../../../IAM/latest/UserGuide/roles-managingrole-editing-api.md#roles-managingrole_edit-trust-policy-api "../../../IAM/latest/UserGuide/roles-managingrole-editing-api.md#roles-managingrole_edit-trust-policy-api"). Attach the following trust policy to the role to allow both the Amazon Bedrock and SageMaker AI services to assume the Amazon Bedrock role:



      JSON





      ```
      `{
       "Version":"2012-10-17",
       "Statement": [
       {
       "Sid": "BedrockTrust",
       "Effect": "Allow",
       "Principal": {
       "Service": "bedrock.amazonaws.com"
       },
       "Action": "sts:AssumeRole"
       },
       {
       "Sid": "SagemakerTrust",
       "Effect": "Allow",
       "Principal": {
       "Service": "sagemaker.amazonaws.com"
       },
       "Action": "sts:AssumeRole"
       }
       ]
      }`

      ```
      2. Sign into the Amazon Bedrock role whose trust policy you just modified.
      3. Follow the steps at [Create an Amazon SageMaker AI Notebook Instance for the tutorial](../../../sagemaker/latest/dg/gs-setup-working-env.md "../../../sagemaker/latest/dg/gs-setup-working-env.md") and specify the ARN of the Amazon Bedrock role that you created to create an SageMaker AI notebook instance.
      4. When the **Status** of the notebook instance is **InService**, choose the instance and then choose **Open JupyterLab**.

  After you open up your SageMaker AI notebook, you can try out the following examples:

###### Topics

- [List the foundation models that Amazon Bedrock has to offer](#getting-started-api-ex-sm-listfm "#getting-started-api-ex-sm-listfm")
- [Submit a text prompt to a model and generate a response](#getting-started-api-ex-sm-converse "#getting-started-api-ex-sm-converse")

## List the foundation models that Amazon Bedrock has to offer

The following example runs the [ListFoundationModels](../APIReference/API_ListFoundationModels.md "../APIReference/API_ListFoundationModels.md") operation using an Amazon Bedrock client. `ListFoundationModels` lists the foundation models (FMs) that are available in Amazon Bedrock in your Region. Run the following SDK for Python script to create an Amazon Bedrock client and test the [ListFoundationModels](../APIReference/API_ListFoundationModels.md "../APIReference/API_ListFoundationModels.md") operation:

```
"""
Lists the available Amazon Bedrock models in an &AWS-Region;.
"""
import logging
import json
import boto3


from botocore.exceptions import ClientError


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def list_foundation_models(bedrock_client):
    """
    Gets a list of available Amazon Bedrock foundation models.

    :return: The list of available bedrock foundation models.
    """

    try:
        response = bedrock_client.list_foundation_models()
        models = response["modelSummaries"]
        logger.info("Got %s foundation models.", len(models))
        return models

    except ClientError:
        logger.error("Couldn't list foundation models.")
        raise


def main():
    """Entry point for the example. Change aws_region to the &AWS-Region;
    that you want to use."""

    aws_region = "us-east-1"

    bedrock_client = boto3.client(service_name="bedrock", region_name=aws_region)

    fm_models = list_foundation_models(bedrock_client)
    for model in fm_models:
        print(f"Model: {model["modelName"]}")
        print(json.dumps(model, indent=2))
        print("---------------------------\n")

    logger.info("Done.")

if __name__ == "__main__":
    main()

```

If the script is successful, the response returns a list of foundation models that are available in Amazon Bedrock.

## Submit a text prompt to a model and generate a response

The following example runs the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") operation using an Amazon Bedrock client. `Converse` lets you submit a prompt to generate a model response. Run the following SDK for Python script to create an Amazon Bedrock runtime client and test the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") operation:

```
# Use the Conversation API to send a text message to Amazon Titan Text G1 - Express.

import boto3
from botocore.exceptions import ClientError

# Create an Amazon Bedrock Runtime client.
brt = boto3.client("bedrock-runtime")

# Set the model ID, e.g., Amazon Titan Text G1 - Express.
model_id = "amazon.titan-text-express-v1"

# Start a conversation with the user message.
user_message = "Describe the purpose of a 'hello world' program in one line."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = brt.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```

If the command is successful, the response returns the text generated by the model in response to the prompt.
