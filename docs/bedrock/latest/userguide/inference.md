

# Making inference requests
<a name="inference"></a>

Inference is the process of generating an output from an input provided to a model. Before you can send an inference request to Amazon Bedrock, you need to allow your role to perform the model invocation API actions. This depends on the endpoint you are using. For new applications, we recommend the `bedrock-runtime` endpoint.

**`bedrock-runtime` endpoint (recommended)**

If your role has the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess) AWS managed policy attached, you can skip this section. Otherwise, attach the following permissions to allow inference through the `bedrock-runtime` endpoint (Converse, Invoke, Chat Completions, and Responses APIs):

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "ModelInvocationPermissions",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:GetInvoke",
                "bedrock:CancelInvoke",
                "bedrock:DeleteInvoke",
                "bedrock:GetInferenceProfile",
                "bedrock:ListInferenceProfiles",
                "bedrock:RenderPrompt",
                "bedrock:GetCustomModel",
                "bedrock:ListCustomModels",
                "bedrock:GetImportedModel",
                "bedrock:ListImportedModels",
                "bedrock:GetProvisionedModelThroughput",
                "bedrock:ListProvisionedModelThroughputs",
                "bedrock:GetGuardrail",
                "bedrock:ListGuardrails",
                "bedrock:ApplyGuardrail"
            ],
            "Resource": "*"
        }
    ]
}
```

**`bedrock-mantle` endpoint**

If your role has the `AmazonBedrockMantleInferenceAccess` AWS managed policy attached, you can skip this section. Otherwise, attach the following permissions to allow inference through the `bedrock-mantle` endpoint (Responses API, Chat Completions, Messages API):

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "MantleInferencePermissions",
            "Effect": "Allow",
            "Action": [
                "bedrock-mantle:CreateInference",
                "bedrock-mantle:GetProject",
                "bedrock-mantle:ListProjects",
                "bedrock-mantle:ListTagsForResources"
            ],
            "Resource": "*"
        }
    ]
}
```

**Important**  
If you scope your policy to specific resources instead of using `"Resource": "*"`, the [Responses API](bedrock-mantle.md#bedrock-mantle-responses) on the `bedrock-runtime` endpoint needs two resources rather than one. In addition to the inference target, creating a response requires `bedrock:InvokeModel` on your account's default project, and retrieving, canceling, or deleting a stored response requires `bedrock:GetInvoke`, `bedrock:CancelInvoke`, or `bedrock:DeleteInvoke` on that same project. The following policy grants the minimum:  

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "CreateResponses",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/openai.*",
                "arn:aws:bedrock:*:111122223333:inference-profile/*.openai.*",
                "arn:aws:bedrock:*:111122223333:project/default"
            ]
        },
        {
            "Sid": "ManageStoredResponses",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetInvoke",
                "bedrock:CancelInvoke",
                "bedrock:DeleteInvoke"
            ],
            "Resource": "arn:aws:bedrock:*:111122223333:project/default"
        }
    ]
}
```
The Converse, Invoke, and Chat Completions APIs don't require a project resource. For more information about the default project, see [Projects (OpenAI-compatible)](projects.md).

For a detailed breakdown of each permission, see [Prerequisites for running model inference](inference-prereq.md).

**Topics**
+ [Inference using Invoke API](inference-api.md)
+ [Inference using Converse API](conversation-inference.md)
+ [Responses API](bedrock-mantle.md)
+ [Chat Completions API](inference-chat-completions-mantle.md)
+ [Inference using Anthropic Messages API](inference-messages-api.md)
+ [Influence response generation with inference parameters](inference-parameters.md)
+ [Get validated JSON results from models](structured-output.md)
+ [Enhance model responses with model reasoning](inference-reasoning.md)
+ [Optimize model inference for latency](latency-optimized-inference.md)
+ [Supported Regions and models for running model inference](inference-supported.md)