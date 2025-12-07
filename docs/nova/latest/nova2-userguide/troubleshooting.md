# Troubleshooting

This section provides solutions to common issues when working with Amazon Nova models.

## Authentication and setup

Missing permissions

**Symptoms:** Unable to access Nova models or features

**Solution:**

- Ensure your IAM role has AmazonBedrockFullAccess or appropriate permissions
- Request specific model access through the Amazon Bedrock console
- Verify permissions for model access and tool usage

## Model access denied

Model access request fails

**Solution:**

- Request specific model access through the Amazon Bedrock console
- Verify your account has been granted access to the requested model
- Check regional availability of the model

## Regional availability issues

Feature not available in selected region

**Solution:**

- Web Grounding is only available in US regions with US CRIS profiles
- Verify the model and features are available in your selected region
- Switch to a supported region if necessary

## Timeout configuration

Requests timing out before completion

**Cause:** Default timeout too short for complex operations

**Solution:** Configure extended timeout settings

```
from botocore.config import Config

bedrock = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
    config=Config(
        connect_timeout=3600,  # 60 minutes
        read_timeout=3600      # 60 minutes
    )
)
```

###### Note

Amazon Nova inference requests can take up to 60 minutes for complex operations.

## API response issues

Understanding stop reasons:

end_turn

Normal completion. No action needed.

max_tokens

Token limit reached. Solution: Increase `maxTokens` parameter in `inferenceConfig`.

content_filtered

Content violated AWS Responsible AI policy. Solution: Review and modify your input to comply with content policies.

malformed_model_output

Invalid output format. Solution: Check your output schema and constraints; verify JSON schema is properly formatted.

malformed_tool_use

Invalid tool call format. Solution: Verify tool definitions match expected schema; check tool input parameters are correctly formatted.

service_unavailable

Built-in tool service unavailable. Solution: Retry the request after a brief delay; check AWS service health dashboard.

invalid_query

Invalid query to built-in tool. Solution: Review query format and parameters; ensure query meets tool requirements.

max_tool_invocations

Tool retries exhausted. Solution: Simplify the task or break it into smaller steps; review tool error messages for specific issues.

## Reasoning mode errors

Truncated responses with high reasoning effort

**Solution:** For high reasoning effort, unset these parameters: `temperature`, `topP`, `maxToken`. This allows the model to use optimal settings for complex reasoning tasks.

Insufficient tokens for reasoning

**Error:** "maxTokens is insufficient"

**Solution:** Automatically retry with increased limit

```
token_limits = {
    "low": 15000,
    "medium": 30000,
    "high": 50000
}

try:
    response = client.converse(
        modelId="us.amazon.nova-2-lite-v1:0",
        messages=messages,
        inferenceConfig={
            "maxTokens": token_limits[max_effort]
        },
        additionalModelRequestFields={
            "reasoningConfig": {
                "type": "enabled",
                "maxReasoningEffort": max_effort
            }
        }
    )
except Exception as e:
    if "maxTokens is insufficient" in str(e):
        higher_limit = int(token_limits[max_effort] * 1.5)
        # Retry with higher limit
```

## Tool use issues

### Schema validation failures

Tool schema validation errors

**Solution:**

- Limit JSON schemas to two layers of nesting for best performance
- Ensure all required fields are properly defined
- Validate schema against JSON Schema specification

Model not using tools correctly

**Solution:**

- Ensure tool name clearly describes its purpose
- Provide detailed description of tool functionality
- Explicitly define input schema with clear parameter descriptions
- Include examples in the description when helpful

Inconsistent tool calling behavior

**Solution:** Set temperature to 0 for tool calling:

```
inferenceConfig={
    "temperature": 0,
    "maxTokens": 10000
}
```

This enables greedy decoding for more reliable tool use.

Tool choice conflicts

**Problem:** Error when using custom tools with web search or code interpreter

**Solution:** Do not include a custom toolSpec with name `nova_grounding` - this conflicts with the system tool. Use the system tool configuration instead:

```
# Correct - use system tool
tool_config = {
    "tools": [{
        "systemTool": {"name": "nova_grounding"}
    }]
}

# Incorrect - don't create custom tool with this name
# tool_config = {
#     "tools": [{
#         "toolSpec": {"name": "nova_grounding", ...}
#     }]
# }
```

### Web Grounding issues

Access control problems

**Problem:** Web Grounding and Code Interpreter not working

**Solution:** Ensure your IAM policy includes:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["bedrock:InvokeTool"],
      "Resource": ["arn:aws:bedrock::{YOUR_ACCOUNT_ID}:system-tool/amazon.nova_grounding"]
    }
  ]
}
```

Service Control Policy issues

**Problem:** Web Grounding blocked by SCP

**Solution:** If you have Service Control Policies with `aws:requestedRegion` condition, update them to allow "unspecified" region for Web Grounding functionality.

### Media processing limitations

Poor understanding of multilingual content in images/videos

**Limitation:** Nova models have limited understanding of multilingual content in visual media

**Workaround:**

- Provide text translations alongside images
- Use text-based inputs for multilingual content when possible

People identification

**Problem:** Model refuses to identify people in images

**Expected Behavior:** Models will refuse to identify or name individuals in images, documents, or videos for privacy and safety reasons

**Workaround:** Ask about general characteristics or context instead of specific identities

Spatial reasoning limitations

**Problem:** Inaccurate localization or layout analysis

**Limitation:** Limited capabilities for precise spatial reasoning

**Workaround:**

- Use bounding box detection for object localization
- Provide clear reference points in your prompts
- Break complex spatial queries into simpler components

Small text in images/videos

**Problem:** Cannot read small text in media

**Solution:**

- Crop images to focus on relevant text sections
- Increase resolution of source media
- Provide text separately if available

### Document and file handling

Unsupported content

**Problem:** PDF processing fails

**Causes:**

- PDFs with CMYK color profiles
- PDFs containing SVG images

**Solution:**

- Convert PDFs to RGB color profile
- Rasterize SVG images before including in PDFs

Token estimation

**Problem:** Unexpected token usage with PDFs

**Guideline:** Estimate approximately 2,560 tokens per standard 8.5×11" PDF page

**Solution:** Adjust `maxTokens` accordingly based on document length
