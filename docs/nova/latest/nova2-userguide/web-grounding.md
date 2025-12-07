# Web Grounding

Web Grounding enhances Nova models by connecting them to real-time information beyond their
knowledge cutoff, which results in more accurate and reliable responses.

###### Topics

- [How Web Grounding works](#how-web-grounding-works "#how-web-grounding-works")
- [How to Use Web Grounding](#enable-web-grounding "#enable-web-grounding")
- [Regional availability](#web-grounding-availability "#web-grounding-availability")
- [Response structure](#web-grounding-response-structure "#web-grounding-response-structure")
- [Grounding safety](#web-grounding-safety "#web-grounding-safety")
- [Error handling](#web-grounding-error-handling "#web-grounding-error-handling")
- [Permissions Required for Built in Tools](#permissions "#permissions")

## How Web Grounding works

When Web Grounding is enabled for a prompt, the following steps are performed:

1. **Request configuration** - Your application sends a user
   prompt to the Amazon Bedrock API with nova_grounding enabled as a systemTool.
2. **Search&Analysis** - The model determines if search
   is needed, performs one or more searches es for relevant information, and evaluates
   whether additional searches are required to expand its understanding or dive deeper on
   specific subtopics.
3. **Response generation** - Amazon Nova automatically
   synthesizes information from search results to generate a final API response grounded in
   real-time information, complete with citations to its sources.

## How to Use Web Grounding

To include Web Grounding in your results, specify ty the following systemTool parameter in
your toolConfig block:

```
import boto3
tool_config = {
    "tools": [{
        "systemTool": {"name": "nova_grounding"}
    }]
}

response = client.converse(
    modelId="us.amazon.nova-2-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [{
            "text": "What is the latest news about renewable energy sources?"
        }]
    }],
    toolConfig=tool_config,
    inferenceConfig={"maxTokens": 10000, "temperature": 0}

print(output_with_citations)
```

## Regional availability

Web Grounding is currently only available in US regions and supported only by US CRIS
profiles. You can use Web Grounding by calling the specific Nova 2 model with the cross-region
inference profile: "us.amazon.nova-2-lite-v1:0"

## Response structure

The following is an example response. The response has been shortened for brevity:

```
n">{
    "text": ".
    - **Solar energy** is leading growth with a 31% increase in generation in early 2025, outpacing wind's 7.7% growth",
    "citationsContent": {
        "citations": [
            {
                "location": {
                    "web": {
                        "url": "rfi.fr/en/environment/20251008-renewables-overtake-coal-but-growth-slows-amid-us-and-china-report-shows",
                        "domain": "rfi.fr"
                    }
                }
            }
        ]
    }
}
```

Each citation includes:

text

The response text incorporating information from web sources.

citationsContent

Array of citations with source information.

citations

A container within citationsContent that holds the location of a citation.

location

A container within citations that holds the source of a citation.

web

A container within location that holds the web source details.

url

The full web address (URL) of the citation's source.

domain

The root domain of the source url.

## Grounding safety

Your data never leaves AWS infrastructure. Model-generated queries stay within AWS
services and are never sent to the broader internet. Our expansive internal web search index
and knowledge graphs prioritize trustworthy and high-quality sources and filter malicious
content on ingress. Web Grounding further refines the information at runtime by
cross-referencing from multiple sources. Finally, we protect your application against indirect
prompt injection and misinformation with runtime filtering (note that this mitigation is
limited for non-English.)

## Error handling

Do not include a toolSpec entry with the name nova_grounding. Including a tool with this
name will result in an error. The following is a list of potential errors that can occur when
using Web Grounding:

malformed_tool_use

The model generated an invalid tool use request. Retry with a clearer prompt or
different parameters.

max_tokens

The response exceeded the maximum token limit.

malformed_model_output

The model generated invalid output. This is typically a transient error - retry the
request.

## Permissions Required for Built in Tools

1. **Enable BedrockFullAccess on your IAM role** - If your
   role has BedrockFullAccess, it will have automatic access to Web Grounding.
2. **Add Specific Permissions (if needed)** - If you require
   more granular access control, add this policy to your role's IAM policy, replacing the
   account ID with your AWS account ID:

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

Web Grounding has the aws:requestedRegion condition key set to "unspecified". If your
existing policies or Service Control Policies (SCPs) enforce this condition, you may encounter
access issues. Updating the condition to allow an "unspecified" requestedRegion can resolve
this problem.

###### Note

If you enable the Web Grounding tool, you are responsible for your use, and any use by
your end users, of output that incorporates grounded information. You will know when your
output includes grounded information from citations or links to the source material. You
must retain and display these citations and links in the output you provide to your end
users.

###### Note

Web Grounding is an additional cost. For more information see [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
