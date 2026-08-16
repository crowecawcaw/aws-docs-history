# Global cross-Region inference

Global cross-Region inference extends cross-Region inference beyond geographic
boundaries, enabling the routing of inference requests to supported commercial
AWS Regions worldwide.

## Benefits of global cross-Region inference

With global cross-Region inference for the Anthropic Claude Sonnet
4.5 model, you get the following advantages over a geographic cross-Region inference
profile:

- **Cost-efficiency** – You save approximately
  10% on both input and output token pricing compared to geographic
  cross-Region inference. Amazon Bedrock calculates the price based on the AWS Region
  from which you make the request (the source AWS Region).
- **Streamlined monitoring** – When using
  global cross-Region inference, CloudWatch and CloudTrail continue to record log entries
  in your source AWS Region, simplifying observability and management. Even
  though your requests are processed across different AWS Regions worldwide,
  you maintain a centralized view of your application's performance and usage
  patterns through your familiar AWS monitoring tools.
- **Worldwide request routing** – With global
  cross-Region inference, your requests can be processed by compute across
  supported commercial AWS Regions worldwide rather than within a single
  geography.

## Global cross-Region inference considerations

Note the following information about Global cross-Region inference:

- For default cross-Region throughput quotas when using Global
  inference profiles, see the **Global Cross-region
  model inference requests per minute for ${Model}** and
 **Global Cross-region model inference tokens per
 minute for ${Model}** values in [Amazon Bedrock service
  quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") in the _AWS General
  Reference_.

You can request, view, and manage quotas for the Global Cross-Region
Inference Profile from the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/bedrock/quotas "https://console.aws.amazon.com/servicequotas/home/services/bedrock/quotas") or by using AWS CLI commands in your
**source region**.

## IAM policy requirements for global cross-Region inference

To enable global cross-Region inference for your users, you must apply a
three-part IAM policy to the role. The following is an example IAM policy to
provide granular control. You can replace `<REQUESTING REGION>` in
the example policy with the AWS Region you are operating in.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GrantGlobalCrisInferenceProfileRegionAccess",
            "Effect": "Allow",
            "Action": "bedrock:InvokeModel",
            "Resource": [
                "arn:aws:bedrock:<REQUESTING REGION>:<ACCOUNT>:inference-profile/global.<MODEL NAME>"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "<REQUESTING REGION>"
                }
            }
        },
        {
            "Sid": "GrantGlobalCrisInferenceProfileInRegionModelAccess",
            "Effect": "Allow",
            "Action": "bedrock:InvokeModel",
            "Resource": [
                "arn:aws:bedrock:<REQUESTING REGION>::foundation-model/<MODEL NAME>"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "<REQUESTING REGION>",
                    "bedrock:InferenceProfileArn": "arn:aws:bedrock:<REQUESTING REGION>:<ACCOUNT>:inference-profile/global.<MODEL NAME>"
                }
            }
        },
        {
            "Sid": "GrantGlobalCrisInferenceProfileGlobalModelAccess",
            "Effect": "Allow",
            "Action": "bedrock:InvokeModel",
            "Resource": [
                "arn:aws:bedrock:::foundation-model/<MODEL NAME>"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "unspecified",
                    "bedrock:InferenceProfileArn": "arn:aws:bedrock:<REQUESTING REGION>:<ACCOUNT>:inference-profile/global.<MODEL NAME>"
                }
            }
        }
    ]
}
```

The first part of the policy grants access to the Regional inference profile in
your requesting AWS Region. The second part provides access to the Regional FM
resource. The third part grants access to the global FM resource, which enables the
cross-Region routing capability.

When implementing these policies, include all three resource Amazon Resource
Names (ARNs) in your IAM statements:

- The Regional inference profile ARN follows the pattern
  `arn:aws:bedrock:REGION:ACCOUNT:inference-profile/global.MODEL-NAME`.
  Use this ARN to grant access to the global inference profile in the source
  AWS Region.
- The Regional FM uses
  `arn:aws:bedrock:REGION::foundation-model/MODEL-NAME`. Use
  this ARN to grant access to the FM in the source AWS Region.
- The global FM requires
  `arn:aws:bedrock:::foundation-model/MODEL-NAME`. Use this ARN
  to grant access to the FM in different global AWS Regions.

The global FM ARN has no AWS Region or account specified, which is intentional
and required for the cross-Region functionality.

### Disable global cross-Region inference

You can choose from two primary approaches to implement deny policies to
global CRIS for specific IAM roles, each with different use cases and
implications:

- **Remove an IAM policy** – The first
  method involves removing one or more of the three required IAM
  policies from user permissions. Because global CRIS requires all three
  policies to function, removing a policy will result in denied
  access.
- **Implement a deny policy** – The second
  approach is to implement an explicit deny policy that specifically
  targets global CRIS inference profiles. This method provides clear
  documentation of your security intent and makes sure that even if
  someone accidentally adds the required allow policies later, the
  explicit deny will take precedence. The deny policy should use a
  `StringEquals` condition matching the pattern
  `"aws:RequestedRegion": "unspecified"`. This pattern
  specifically targets inference profiles with the `global`
  prefix.

When implementing deny policies, it's crucial to understand that global CRIS
changes how the `aws:RequestedRegion` field behaves. Traditional
AWS Region-based deny policies that use `StringEquals` conditions
with specific AWS Region names such as `"aws:RequestedRegion":
 "us-west-2"` will not work as expected with global CRIS. The service
sets this field to `global` rather than the actual
destination AWS Region. However, as mentioned earlier,
`"aws:RequestedRegion": "unspecified"` will result in the deny
effect.

## Service Control Policy requirements for Global cross-Region inference

For Global cross-Region inference, if your organization's security policy uses
SCPs to block unused Regions, you must update your region-specific SCP conditions to
allow access with `"aws:RequestedRegion": "unspecified"`. This condition
is specific to Amazon Bedrock Global cross-Region inference and ensures that requests can be
routed to all supported AWS commercial Regions.

The following example SCP blocks all AWS API calls outside of approved Regions
while allowing Amazon Bedrock Global cross-Region inference calls that use
`"unspecified"` as the Region for global routing:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAllOutsideApprovedRegions",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": [
                        "us-east-1",
                        "us-east-2",
                        "us-west-2",
                        "unspecified"
                    ]
                }
            }
        }
    ]
}
```

### Disable global cross-Region inference

Organizations with data residency or compliance requirements should assess
whether Global cross-Region inference fits their compliance framework, since
requests may be processed in other supported AWS commercial Regions. To
explicitly disable Global cross-Region inference, implement the following SCP
policy:

```
{
    "Effect": "Deny",
    "Action": "bedrock:*",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:RequestedRegion": "unspecified"
        },
        "ArnLike": {
            "bedrock:InferenceProfileArn": "arn:aws:bedrock:*:*:inference-profile/global.*"
        }
    }
}
```

This SCP explicitly denies Global cross-Region inference because the
`"aws:RequestedRegion"` is `"unspecified"` and the
`"ArnLike"` condition targets inference profiles with the
`global` prefix in the ARN.

### AWS Control Tower implementation

Manually editing SCPs managed by AWS Control Tower is strongly discouraged
as it can cause drift. Instead, use the mechanisms provided by Control Tower to
manage these exceptions. The core principles involve either extending existing
region-deny controls or enabling regions and then applying a custom, conditional
blocking policy.

For detailed, step-by-step guidance on implementing cross-Region inference
with Control Tower, see the blog post [Enable Amazon Bedrock cross-Region inference in multi-account
environments](https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/ "https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/"). This covers extending existing Region deny SCPs,
enabling denied regions with custom SCPs, and using Customizations for AWS
Control Tower (CfCT) to deploy custom SCPs as infrastructure as code.

## Request limit increases for global cross-Region inference

When using global CRIS inference profiles, you can use global CRIS from over 20
supported source AWS Regions. This is a global limit. To view, manage, or
increase quotas for global cross-Region inference profiles, use the Service Quotas
console or AWS CLI in the requested source AWS Region.

Complete the following steps to request a limit increase:

1. Sign in to the Service Quotas console in your AWS account.
2. In the navigation pane, choose **AWS
   services**.
3. From the list of services, find and choose **Amazon Bedrock**.
4. In the list of quotas for Amazon Bedrock, use the search filter to find the specific
   global CRIS quotas. For example:

   - Global cross-Region model inference tokens per minute for
     Anthropic Claude Sonnet 4.5 V1

5. Select the quota you want to increase.
6. Choose **Request increase at account
   level**.
7. Enter your desired new quota value.
8. Choose **Request** to submit your
   request.

When calculating your required quota increase, account for
the burndown rate. The burndown rate is the rate at which input and output tokens are
converted into token quota usage for the throttling system. The following models
have a **5x burn down rate for output tokens (1 output token
consumes 5 tokens from your quotas)**:

- Anthropic Claude Opus 4
- Anthropic Claude Sonnet 4.5
- Anthropic Claude Sonnet 4
- Anthropic Claude 3.7 Sonnet

For all other models, the burndown rate is **1:1** (1
output token consumes 1 token from your quota). For input tokens, the token to quota
ratio is 1:1. The calculation for the total number of tokens per request is as
follows:

`Input token count + Cache write input tokens + (Output token count x
 Burndown rate)`

## Use Global cross-Region inference

To use global cross-Region inference with Anthropic's Claude Sonnet 4.5,
developers must complete the following key steps:

- **Use the global inference profile ID** –
  When making API calls to Amazon Bedrock, specify the global Anthropic's Claude Sonnet
  4.5 inference profile ID
  (`global.anthropic.claude-sonnet-4-5-20250929-v1:0`) instead
  of a AWS Region-specific model ID.
- **Configure IAM permissions** – Grant
  appropriate IAM permissions to access the inference profile and FMs in
  potential destination AWS Regions.

Global cross-Region inference is supported for:

- On-demand model inference
- Batch inference
- Agents
- Model evaluation
- Prompt management
- Prompt flows

###### Note

Global inference profile is supported for On-demand model inference, Batch
inference, Agents, Model evaluation, Prompt management, and Prompt flows.

## Implement global cross-Region inference

Implementing global cross-Region inference with Anthropic's Claude Sonnet 4.5 is
straightforward, requiring only a few changes to your existing application code. The
following is an example of how to update your code in Python:

```
import boto3
import json
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
model_id = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
response = bedrock.converse(
    messages=[{"role": "user", "content": [{"text": "Explain cloud computing in 2 sentences."}]}],
    modelId=model_id,
)

print("Response:", response['output']['message']['content'][0]['text'])
print("Token usage:", response['usage'])
print("Total tokens:", response['usage']['totalTokens'])
```
