# Web Grounding

Web Grounding enables Amazon Nova to search the web for current information and provide responses with citations. This feature is useful for queries requiring up-to-date information beyond the model's training data.

###### Topics

- [How Web Grounding works](#how-web-grounding-works "#how-web-grounding-works")
- [How to use Web Grounding](#enable-web-grounding "#enable-web-grounding")
- [Regional availability](#web-grounding-availability "#web-grounding-availability")
- [Response structure](#web-grounding-response-structure "#web-grounding-response-structure")
- [Grounding safety](#web-grounding-safety "#web-grounding-safety")
- [Error handling](#web-grounding-error-handling "#web-grounding-error-handling")
- [Permissions required for built in tools](#permissions "#permissions")

## How Web Grounding works

When Web Grounding is enabled for a prompt, the following steps are performed:

1. **Request Configuration**: Your application sends a user prompt to the Amazon Bedrock API with nova_grounding enabled as a `systemTool`.
2. **Search & Analysis**: The model determines if search is needed, performs one or more searches for relevant information, and evaluates whether additional searches are required to expand its understanding or dive deeper on specific subtopics.
3. **Response generation**: Amazon Nova automatically synthesizes information from search results to generate a final API response grounded in real-time information, complete with citations to its sources.

## How to use Web Grounding

For full examples of code that utilizes Web Grounding, see the Code Samples section.

To include Web Grounding in your results, specify the following `systemTool` parameter in your toolConfig block:

```
import boto3
from botocore.config import Config

# Create the Bedrock Runtime client with extended timeout
bedrock = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
    config=Config(read_timeout=3600)
)

# Define the tool configuration
tool_config = {
    "tools": [{
        "systemTool": {
            "name": "nova_grounding"
        }
    }]
}

# Send the request
response = bedrock.converse(
    modelId="us.amazon.nova-2-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [{"text": "What are the latest developments in quantum computing?"}]
    }],
    toolConfig=tool_config
)

# Extract text with interleaved citations
output_with_citations = ""
content_list = response["output"]["message"]["content"]
for content in content_list:
    if "text" in content:
        output_with_citations += content["text"]
    elif "citationsContent" in content:
        citations = content["citationsContent"]["citations"]
        for citation in citations:
            url = citation["location"]["web"]["url"]
            output_with_citations += f" [{url}]"

print(output_with_citations)
```

## Regional availability

Web Grounding is currently only available in US regions and supported only by US CRIS profiles.

## Response structure

The following is an example response. The response has been shortened for brevity:

```
{
  "output": {
    "message": {
      "content": [
        {
          "text": "Recent quantum computing developments include...",
          "citationsContent": [
            {
              "location": {
                "web": {
                  "url": "https://example.com/quantum-news",
                  "domain": "example.com"
                }
              }
            }
          ]
        }
      ]
    }
  }
}
```

Each citation includes:

- `text`: A segment of the model's generated response.
- `citationsContent`: The primary container for the citation data related to a text segment.
- `citations`: A container within `citationsContent` that holds the location of a citation.
- `location`: A container within `citations` that holds the source of a citation.
- `web`: A container within `location` that holds the web source details.
- `url`: The full web address (URL) of the citation's source.
- `domain`: The root domain of the source url.

## Grounding safety

Your data never leaves AWS infrastructure. Model-generated queries stay within AWS services and are never sent to the broader internet. Our expansive internal web search index and knowledge graphs prioritize trustworthy and high-quality sources and filter malicious content on ingress. Finally, we protect your application against indirect prompt injection and misinformation with runtime filtering (note that this mitigation is limited for non-English languages).

## Error handling

Do not include a `toolSpec` entry with the name `nova_grounding`. Including a tool with this name will result in an error.

The following is a list of potential errors that can occur when using Web Grounding:

- `malformed_tool_use`
- `max_tokens`
- `malformed_model_output`

## Permissions required for built in tools

To ensure your role can access Web Grounding on Amazon Bedrock, you have two options:

1. **Enable BedrockFullAccess on your IAM role**: If your role has BedrockFullAccess, it will have automatic access to Web Grounding.
2. **Add Specific Permissions (if needed)**: If you require more granular access control, add this policy to your role's IAM policy, replacing the account ID with your AWS account ID:

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["bedrock:InvokeTool"],
            "Resource": ["arn:aws:bedrock::{111122223333}:system-tool/amazon.nova_grounding"]
        }
    ]
}
```

Web Grounding has the `aws:requestedRegion` condition key set to "unspecified". If your existing policies or Service Control Policies (SCPs) enforce this condition, you may encounter access issues. Updating the condition to allow an "unspecified" requestedRegion can resolve this problem.

###### Note

If you enable the Web Grounding tool, you are responsible for your use, and any use by your end users, of output that incorporates grounded information. You will know when your output includes grounded information from citations or links to the source material. You must retain and display these citations and links in the output you provide to your end users.

###### Note

Web Grounding is an additional cost. For more information, go to [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
