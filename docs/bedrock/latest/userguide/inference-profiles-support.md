# Supported Regions and models for inference profiles

For a list of Region codes and endpoints supported in Amazon Bedrock, see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md#bedrock_region "../../../general/latest/gr/bedrock.md#bedrock_region"). This topic describes predefined inference profiles that you can use and the Regions and models that support application inference profiles.

###### Topics

- [Supported cross-Region inference profiles](#inference-profiles-support-system "#inference-profiles-support-system")
- [Supported Regions and models for application inference profiles](#inference-profiles-support-user "#inference-profiles-support-user")

## Supported cross-Region inference profiles

You can carry out [cross-Region inference](cross-region-inference.md "cross-region-inference.md") with cross-Region (system-defined) inference profiles. Cross-Region inference allows you to seamlessly manage unplanned traffic bursts by utilizing compute across different AWS Regions. With cross-Region inference, you can distribute traffic across multiple AWS Regions.

Cross-region (system-defined) inference profiles are named after the model that they support and defined by the Regions that they support. To understand how a cross-region inference profile handles your requests, review the following definitions:

- **Source Region** – The Region from which you make the API request that specifies the inference profile.
- **Destination Region** – A Region to which the Amazon Bedrock service can route the request from your source Region.

When you invoke a cross-Region inference profile in Amazon Bedrock, your request originates from a source Region and is automatically routed to one of the destination Regions defined in that profile, optimizing for performance. The destination Regions for Global cross-Region inference profiles include all commercial Regions.

###### Note

The destination Regions in a cross-Region inference profile can include _opt-in Regions_, which are Regions that you must explicitly enable at AWS account or Organization level.
To learn more, see [Enable or disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md"). When using a cross-Region inference profile,
your inference request can be routed to any of the destination Regions in the profile, even if you did not opt-in to such Regions in your account.

Service Control Policies (SCPs) and AWS Identity and Access Management (IAM) policies work together to control where cross-Region inference is allowed. Using SCPs,
you can control which Regions Amazon Bedrock can use for inference, and using IAM policies, you can define which users or roles have permission to run inference.
If any destination Region in a cross-Region inference profile is blocked in your SCPs, the request will fail even if other Regions remain allowed. To
ensure efficient operation with cross-region inference, you can update your SCPs and IAM policies to allow all required Amazon Bedrock inference actions
(for example, `bedrock:InvokeModel*` or `bedrock:CreateModelInvocationJob`) in all destination Regions included in your chosen
inference profile. To learn more, see [Enabling Amazon Bedrock cross-Region inference in multi-account environments.](https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/ "https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/")

###### Note

Some inference profiles route to different destination Regions depending on the source Region from which you call it. For example, if you call `us.anthropic.claude-3-haiku-20240307-v1:0` from US East (Ohio), it can route requests to `us-east-1`, `us-east-2`, or `us-west-2`, but if you call it from US West (Oregon), it can route requests to only `us-east-1` and `us-west-2`.

To check the source and destination Regions for an inference profile, you can do one of the following:

- Expand the corresponding section in the [list of supported cross-region inference profiles](inference-profiles-support.md "inference-profiles-support.md").
- Send a [GetInferenceProfile](../APIReference/API_GetInferenceProfile.md "../APIReference/API_GetInferenceProfile.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") from a source Region and specify the Amazon Resource Name (ARN) or ID of the inference profile in the `inferenceProfileIdentifier` field. The `models` field in the response maps to a list of model ARNs, in which you can identify each destination Region.

###### Note

Global cross-Region inference profile for a specific model can change over time as AWS adds more commercial Regions where your requests can be processed.
However, if an inference profile is tied to a geography (such as US, EU, or APAC), its destination Region list will never change. AWS might create new inference
profiles that incorporate new Regions. You can update your systems to use these inference profiles by changing the IDs in your setup to the new ones.

The Global cross-region inference profile is currently only supported on Anthropic Claude Sonnet 4 model for the following source Regions:
US West (Oregon), US East (N. Virginia), US East (Ohio), Europe (Ireland), and Asia Pacific (Tokyo). The destination Regions for Global inference profile
include all commercial AWS Regions.

Expand one of the following sections to see information about a cross-Region inference profile, the source Regions from which it can be called, and the destination Regions to which it can route requests.

To call the GLOBAL Amazon Nova 2 Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
global.amazon.nova-2-lite-v1:0
```

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| ap-east-2      | Commercial AWS Regions<br>ap-east-2      |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| ap-northeast-2 | Commercial AWS Regions<br>ap-northeast-2 |
| ap-south-1     | Commercial AWS Regions<br>ap-south-1     |
| ap-southeast-1 | Commercial AWS Regions<br>ap-southeast-1 |
| ap-southeast-2 | Commercial AWS Regions<br>ap-southeast-2 |
| ap-southeast-3 | Commercial AWS Regions<br>ap-southeast-3 |
| ap-southeast-4 | Commercial AWS Regions<br>ap-southeast-4 |
| ap-southeast-5 | Commercial AWS Regions<br>ap-southeast-5 |
| ap-southeast-7 | Commercial AWS Regions<br>ap-southeast-7 |
| ca-central-1   | Commercial AWS Regions<br>ca-central-1   |
| ca-west-1      | Commercial AWS Regions<br>ca-west-1      |
| eu-central-1   | Commercial AWS Regions<br>eu-central-1   |
| eu-north-1     | Commercial AWS Regions<br>eu-north-1     |
| eu-south-1     | Commercial AWS Regions<br>eu-south-1     |
| eu-south-2     | Commercial AWS Regions<br>eu-south-2     |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| eu-west-2      | Commercial AWS Regions<br>eu-west-2      |
| eu-west-3      | Commercial AWS Regions<br>eu-west-3      |
| il-central-1   | Commercial AWS Regions<br>il-central-1   |
| me-central-1   | Commercial AWS Regions<br>me-central-1   |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-1      | Commercial AWS Regions<br>us-west-1      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |

To call the GLOBAL Anthropic Claude Opus 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
global.anthropic.claude-opus-4-5-20251101-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| ap-northeast-2 | Commercial AWS Regions<br>ap-northeast-2 |
| ap-northeast-3 | Commercial AWS Regions<br>ap-northeast-3 |
| ap-south-1     | Commercial AWS Regions<br>ap-south-1     |
| ap-south-2     | Commercial AWS Regions<br>ap-south-2     |
| ap-southeast-1 | Commercial AWS Regions<br>ap-southeast-1 |
| ap-southeast-2 | Commercial AWS Regions<br>ap-southeast-2 |
| ap-southeast-3 | Commercial AWS Regions<br>ap-southeast-3 |
| ap-southeast-4 | Commercial AWS Regions<br>ap-southeast-4 |
| ca-central-1   | Commercial AWS Regions<br>ca-central-1   |
| eu-central-1   | Commercial AWS Regions<br>eu-central-1   |
| eu-central-2   | Commercial AWS Regions<br>eu-central-2   |
| eu-north-1     | Commercial AWS Regions<br>eu-north-1     |
| eu-south-1     | Commercial AWS Regions<br>eu-south-1     |
| eu-south-2     | Commercial AWS Regions<br>eu-south-2     |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| eu-west-2      | Commercial AWS Regions<br>eu-west-2      |
| eu-west-3      | Commercial AWS Regions<br>eu-west-3      |
| sa-east-1      | Commercial AWS Regions<br>sa-east-1      |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-1      | Commercial AWS Regions<br>us-west-1      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |
| me-south-1     | Commercial AWS Regions<br>me-south-1     |
| af-south-1     | Commercial AWS Regions<br>af-south-1     |
| me-central-1   | Commercial AWS Regions<br>me-central-1   |
| il-central-1   | Commercial AWS Regions<br>il-central-1   |

To call the GLOBAL TwelveLabs Pegasus v1.2 inference profile, specify the following inference profile ID in one of the source Regions:

```
global.twelvelabs.pegasus-1-2-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-pegasus.md "model-parameters-pegasus.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| af-south-1     | Commercial AWS Regions<br>af-south-1     |
| ap-east-2      | Commercial AWS Regions<br>ap-east-2      |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| ap-northeast-2 | Commercial AWS Regions<br>ap-northeast-2 |
| ap-northeast-3 | Commercial AWS Regions<br>ap-northeast-3 |
| ap-south-1     | Commercial AWS Regions<br>ap-south-1     |
| ap-south-2     | Commercial AWS Regions<br>ap-south-2     |
| ap-southeast-1 | Commercial AWS Regions<br>ap-southeast-1 |
| ap-southeast-2 | Commercial AWS Regions<br>ap-southeast-2 |
| ap-southeast-3 | Commercial AWS Regions<br>ap-southeast-3 |
| ap-southeast-4 | Commercial AWS Regions<br>ap-southeast-4 |
| ap-southeast-5 | Commercial AWS Regions<br>ap-southeast-5 |
| ap-southeast-7 | Commercial AWS Regions<br>ap-southeast-7 |
| ca-central-1   | Commercial AWS Regions<br>ca-central-1   |
| ca-west-1      | Commercial AWS Regions<br>ca-west-1      |
| eu-central-1   | Commercial AWS Regions<br>eu-central-1   |
| eu-central-2   | Commercial AWS Regions<br>eu-central-2   |
| eu-north-1     | Commercial AWS Regions<br>eu-north-1     |
| eu-south-1     | Commercial AWS Regions<br>eu-south-1     |
| eu-south-2     | Commercial AWS Regions<br>eu-south-2     |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| eu-west-2      | Commercial AWS Regions<br>eu-west-2      |
| eu-west-3      | Commercial AWS Regions<br>eu-west-3      |
| il-central-1   | Commercial AWS Regions<br>il-central-1   |
| me-central-1   | Commercial AWS Regions<br>me-central-1   |
| me-south-1     | Commercial AWS Regions<br>me-south-1     |
| mx-central-1   | Commercial AWS Regions<br>mx-central-1   |
| sa-east-1      | Commercial AWS Regions<br>sa-east-1      |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-1      | Commercial AWS Regions<br>us-west-1      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |

To call the Global Anthropic Claude Haiku 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
global.anthropic.claude-haiku-4-5-20251001-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| ap-northeast-2 | Commercial AWS Regions<br>ap-northeast-2 |
| ap-northeast-3 | Commercial AWS Regions<br>ap-northeast-3 |
| ap-south-1     | Commercial AWS Regions<br>ap-south-1     |
| ap-south-2     | Commercial AWS Regions<br>ap-south-2     |
| ap-southeast-1 | Commercial AWS Regions<br>ap-southeast-1 |
| ap-southeast-2 | Commercial AWS Regions<br>ap-southeast-2 |
| ap-southeast-3 | Commercial AWS Regions<br>ap-southeast-3 |
| ap-southeast-4 | Commercial AWS Regions<br>ap-southeast-4 |
| ca-central-1   | Commercial AWS Regions<br>ca-central-1   |
| eu-central-1   | Commercial AWS Regions<br>eu-central-1   |
| eu-central-2   | Commercial AWS Regions<br>eu-central-2   |
| eu-north-1     | Commercial AWS Regions<br>eu-north-1     |
| eu-south-1     | Commercial AWS Regions<br>eu-south-1     |
| eu-south-2     | Commercial AWS Regions<br>eu-south-2     |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| eu-west-2      | Commercial AWS Regions<br>eu-west-2      |
| eu-west-3      | Commercial AWS Regions<br>eu-west-3      |
| sa-east-1      | Commercial AWS Regions<br>sa-east-1      |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-1      | Commercial AWS Regions<br>us-west-1      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |
| me-central-1   | Commercial AWS Regions<br>me-central-1   |
| il-central-1   | Commercial AWS Regions<br>il-central-1   |
| me-south-1     | Commercial AWS Regions<br>me-south-1     |

To call the Global Claude Sonnet 4 inference profile, specify the following inference profile ID in one of the source Regions:

```
global.anthropic.claude-sonnet-4-20250514-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |

To call the Global Claude Sonnet 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
global.anthropic.claude-sonnet-4-5-20250929-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| af-south-1     | Commercial AWS Regions<br>af-south-1     |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| ap-northeast-2 | Commercial AWS Regions<br>ap-northeast-2 |
| ap-northeast-3 | Commercial AWS Regions<br>ap-northeast-3 |
| ap-south-1     | Commercial AWS Regions<br>ap-south-1     |
| ap-south-2     | Commercial AWS Regions<br>ap-south-2     |
| ap-southeast-1 | Commercial AWS Regions<br>ap-southeast-1 |
| ap-southeast-2 | Commercial AWS Regions<br>ap-southeast-2 |
| ap-southeast-3 | Commercial AWS Regions<br>ap-southeast-3 |
| ap-southeast-4 | Commercial AWS Regions<br>ap-southeast-4 |
| ca-central-1   | Commercial AWS Regions<br>ca-central-1   |
| ca-west-1      | Commercial AWS Regions<br>ca-west-1      |
| eu-central-1   | Commercial AWS Regions<br>eu-central-1   |
| eu-central-2   | Commercial AWS Regions<br>eu-central-2   |
| eu-north-1     | Commercial AWS Regions<br>eu-north-1     |
| eu-south-1     | Commercial AWS Regions<br>eu-south-1     |
| eu-south-2     | Commercial AWS Regions<br>eu-south-2     |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| eu-west-2      | Commercial AWS Regions<br>eu-west-2      |
| eu-west-3      | Commercial AWS Regions<br>eu-west-3      |
| sa-east-1      | Commercial AWS Regions<br>sa-east-1      |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-1      | Commercial AWS Regions<br>us-west-1      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |
| me-central-1   | Commercial AWS Regions<br>me-central-1   |
| il-central-1   | Commercial AWS Regions<br>il-central-1   |

To call the Global Cohere Embed v4 inference profile, specify the following inference profile ID in one of the source Regions:

```
global.cohere.embed-v4:0
```

For more information about inference parameters for this model, see [Link](model-parameters-embed.md "model-parameters-embed.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                      |
| -------------- | ---------------------------------------- |
| ap-northeast-1 | Commercial AWS Regions<br>ap-northeast-1 |
| ap-northeast-2 | Commercial AWS Regions<br>ap-northeast-2 |
| ap-northeast-3 | Commercial AWS Regions<br>ap-northeast-3 |
| ap-south-1     | Commercial AWS Regions<br>ap-south-1     |
| ap-south-2     | Commercial AWS Regions<br>ap-south-2     |
| ap-southeast-1 | Commercial AWS Regions<br>ap-southeast-1 |
| ap-southeast-2 | Commercial AWS Regions<br>ap-southeast-2 |
| ap-southeast-3 | Commercial AWS Regions<br>ap-southeast-3 |
| ap-southeast-4 | Commercial AWS Regions<br>ap-southeast-4 |
| ca-central-1   | Commercial AWS Regions<br>ca-central-1   |
| eu-central-1   | Commercial AWS Regions<br>eu-central-1   |
| eu-central-2   | Commercial AWS Regions<br>eu-central-2   |
| eu-north-1     | Commercial AWS Regions<br>eu-north-1     |
| eu-south-1     | Commercial AWS Regions<br>eu-south-1     |
| eu-south-2     | Commercial AWS Regions<br>eu-south-2     |
| eu-west-1      | Commercial AWS Regions<br>eu-west-1      |
| eu-west-2      | Commercial AWS Regions<br>eu-west-2      |
| eu-west-3      | Commercial AWS Regions<br>eu-west-3      |
| sa-east-1      | Commercial AWS Regions<br>sa-east-1      |
| us-east-1      | Commercial AWS Regions<br>us-east-1      |
| us-east-2      | Commercial AWS Regions<br>us-east-2      |
| us-west-1      | Commercial AWS Regions<br>us-west-1      |
| us-west-2      | Commercial AWS Regions<br>us-west-2      |

To call the US Amazon Nova 2 Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
us.amazon.nova-2-lite-v1:0
```

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                 |
| -------------- | --------------------------------------------------- |
| ca-central-1   | ca-central-1<br>us-east-1<br>us-east-2<br>us-west-2 |
| ca-west-1      | ca-west-1<br>us-east-1<br>us-east-2<br>us-west-2    |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2    |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2                 |

To call the US Anthropic Claude 3 Haiku inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-haiku-20240307-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2              |

To call the US Anthropic Claude 3 Opus inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-opus-20240229-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions    |
| -------------- | ---------------------- |
| us-east-1      | us-east-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2 |

To call the US Anthropic Claude 3 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-sonnet-20240229-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions    |
| -------------- | ---------------------- |
| us-east-1      | us-east-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2 |

To call the US Anthropic Claude 3.5 Haiku inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-5-haiku-20241022-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Anthropic Claude 3.5 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-5-sonnet-20240620-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions    |
| -------------- | ---------------------- |
| us-east-1      | us-east-1<br>us-west-2 |
| us-east-2      | us-east-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2 |

To call the US Anthropic Claude 3.5 Sonnet v2 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-5-sonnet-20241022-v2:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Anthropic Claude 3.7 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-3-7-sonnet-20250219-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Anthropic Claude Haiku 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-haiku-4-5-20251001-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                 |
| -------------- | --------------------------------------------------- |
| ca-central-1   | ca-central-1<br>us-east-1<br>us-east-2<br>us-west-2 |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2    |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2                 |

To call the US Anthropic Claude Opus 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-opus-4-5-20251101-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                 |
| -------------- | --------------------------------------------------- |
| ca-central-1   | ca-central-1<br>us-east-1<br>us-east-2<br>us-west-2 |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2    |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2                 |

To call the US Anthropic Claude Sonnet 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-sonnet-4-5-20250929-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                 |
| -------------- | --------------------------------------------------- |
| ca-central-1   | ca-central-1<br>us-east-1<br>us-east-2<br>us-west-2 |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2                 |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2    |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2                 |

To call the US Claude Opus 4 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-opus-4-20250514-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Claude Opus 4.1 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-opus-4-1-20250805-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Claude Sonnet 4 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.anthropic.claude-sonnet-4-20250514-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Cohere Embed v4 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.cohere.embed-v4:0
```

For more information about inference parameters for this model, see [Link](model-parameters-embed.md "model-parameters-embed.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US DeepSeek-R1 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.deepseek.r1-v1:0
```

For more information about inference parameters for this model, see [Link](https://www.deepseek.com/ "https://www.deepseek.com/").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Llama 4 Maverick 17B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama4-maverick-17b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Llama 4 Scout 17B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama4-scout-17b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Meta Llama 3.1 70B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-1-70b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Meta Llama 3.1 8B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-1-8b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Meta Llama 3.1 Instruct 405B inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-1-405b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Meta Llama 3.2 11B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-2-11b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2              |

To call the US Meta Llama 3.2 1B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-2-1b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2              |

To call the US Meta Llama 3.2 3B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-2-3b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2              |

To call the US Meta Llama 3.2 90B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-2-90b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-west-2              |

To call the US Meta Llama 3.3 70B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
us.meta.llama3-3-70b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Mistral Pixtral Large 25.02 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.mistral.pixtral-large-2502-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-mistral.md "model-parameters-mistral.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Nova Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
us.amazon.nova-lite-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Nova Micro inference profile, specify the following inference profile ID in one of the source Regions:

```
us.amazon.nova-micro-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Nova Premier inference profile, specify the following inference profile ID in one of the source Regions:

```
us.amazon.nova-premier-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Nova Pro inference profile, specify the following inference profile ID in one of the source Regions:

```
us.amazon.nova-pro-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Pegasus v1.2 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.twelvelabs.pegasus-1-2-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-pegasus.md "model-parameters-pegasus.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Stable Image Conservative Upscale inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-conservative-upscale-v1:0
```

For more information about inference parameters for this model, see [Link](stable-image-services.md "stable-image-services.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Control Sketch inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-control-sketch-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Control Structure inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-control-structure-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Creative Upscale inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-creative-upscale-v1:0
```

For more information about inference parameters for this model, see [Link](stable-image-services.md "stable-image-services.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Erase Object inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-erase-object-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Fast Upscale inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-fast-upscale-v1:0
```

For more information about inference parameters for this model, see [Link](stable-image-services.md "stable-image-services.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Inpaint inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-inpaint-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Outpaint inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-outpaint-v1:0
```

For more information about inference parameters for this model, see [Link](stable-image-services.md "stable-image-services.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Remove Background inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-remove-background-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Search and Recolor inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-search-recolor-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Search and Replace inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-search-replace-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Style Guide inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-image-style-guide-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US Stable Image Style Transfer inference profile, specify the following inference profile ID in one of the source Regions:

```
us.stability.stable-style-transfer-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-stability-diffusion.md "model-parameters-stability-diffusion.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US TwelveLabs Marengo Embed 3.0 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.twelvelabs.marengo-embed-3-0-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-marengo.md "model-parameters-marengo.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                 |
| -------------- | ----------------------------------- |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2 |

To call the US TwelveLabs Marengo Embed v2.7 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.twelvelabs.marengo-embed-2-7-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-marengo.md "model-parameters-marengo.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |

To call the US Writer Palmyra X4 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.writer.palmyra-x4-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-writer-palmyra.md "model-parameters-writer-palmyra.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US Writer Palmyra X5 inference profile, specify the following inference profile ID in one of the source Regions:

```
us.writer.palmyra-x5-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-writer-palmyra.md "model-parameters-writer-palmyra.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                              |
| -------------- | ------------------------------------------------ |
| us-east-1      | us-east-1<br>us-east-2<br>us-west-2              |
| us-east-2      | us-east-1<br>us-east-2<br>us-west-2              |
| us-west-1      | us-east-1<br>us-east-2<br>us-west-1<br>us-west-2 |
| us-west-2      | us-east-1<br>us-east-2<br>us-west-2              |

To call the US-GOV Claude 3 Haiku inference profile, specify the following inference profile ID in one of the source Regions:

```
us-gov.anthropic.claude-3-haiku-20240307-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions            |
| -------------- | ------------------------------ |
| us-gov-east-1  | us-gov-east-1<br>us-gov-west-1 |

To call the US-GOV Claude 3.5 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
us-gov.anthropic.claude-3-5-sonnet-20240620-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions            |
| -------------- | ------------------------------ |
| us-gov-east-1  | us-gov-east-1<br>us-gov-west-1 |

To call the US-GOV Claude 3.7 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
us-gov.anthropic.claude-3-7-sonnet-20250219-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions            |
| -------------- | ------------------------------ |
| us-gov-east-1  | us-gov-east-1<br>us-gov-west-1 |

To call the US-GOV Claude Sonnet 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
us-gov.anthropic.claude-sonnet-4-5-20250929-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions |
| -------------- | ------------------- |
| us-gov-east-1  | us-gov-west-1       |
| us-gov-west-1  | us-gov-west-1       |

To call the APAC Anthropic Claude 3 Haiku inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.anthropic.claude-3-haiku-20240307-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |

To call the APAC Anthropic Claude 3 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.anthropic.claude-3-sonnet-20240229-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |

To call the APAC Anthropic Claude 3.5 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.anthropic.claude-3-5-sonnet-20240620-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2 |

To call the APAC Anthropic Claude 3.5 Sonnet v2 inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.anthropic.claude-3-5-sonnet-20241022-v2:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2               |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2               |
| ap-northeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2               |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2               |
| ap-south-2     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2               |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2               |

To call the APAC Anthropic Claude 3.7 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.anthropic.claude-3-7-sonnet-20250219-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-northeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-south-2     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2 |

To call the APAC Claude Sonnet 4 inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.anthropic.claude-sonnet-4-20250514-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ap-east-2      | ap-east-2<br>ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4      |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-northeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-south-2     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-southeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4                   |
| ap-southeast-4 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-southeast-5 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-5 |
| ap-southeast-7 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-7 |
| me-central-1   | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>me-central-1   |

To call the APAC Nova Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.amazon.nova-lite-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ap-east-2      | ap-east-2<br>ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4      |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4                   |
| ap-southeast-4 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-southeast-5 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-5 |
| ap-southeast-7 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-7 |
| me-central-1   | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>me-central-1   |

To call the APAC Nova Micro inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.amazon.nova-micro-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ap-east-2      | ap-east-2<br>ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4      |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4                   |
| ap-southeast-5 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-5 |
| ap-southeast-7 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-7 |
| me-central-1   | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>me-central-1   |

To call the APAC Nova Pro inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.amazon.nova-pro-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ap-east-2      | ap-east-2<br>ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4      |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-south-1     | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-1 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-southeast-1<br>ap-southeast-2                                                                     |
| ap-southeast-3 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4                   |
| ap-southeast-4 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4                                     |
| ap-southeast-5 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-5 |
| ap-southeast-7 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>ap-southeast-7 |
| me-central-1   | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4<br>me-central-1   |

To call the APAC Pegasus v1.2 inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.twelvelabs.pegasus-1-2-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-pegasus.md "model-parameters-pegasus.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-4 |

To call the APAC TwelveLabs Marengo Embed v2.7 inference profile, specify the following inference profile ID in one of the source Regions:

```
apac.twelvelabs.marengo-embed-2-7-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-marengo.md "model-parameters-marengo.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ap-northeast-2 | ap-northeast-1<br>ap-northeast-2<br>ap-northeast-3<br>ap-south-1<br>ap-south-2<br>ap-southeast-1<br>ap-southeast-2<br>ap-southeast-3<br>ap-southeast-4 |

To call the AU AU Anthropic Claude Sonnet 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
au.anthropic.claude-sonnet-4-5-20250929-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions              |
| -------------- | -------------------------------- |
| ap-southeast-2 | ap-southeast-2<br>ap-southeast-4 |
| ap-southeast-4 | ap-southeast-2<br>ap-southeast-4 |

To call the AU Anthropic Claude Haiku 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
au.anthropic.claude-haiku-4-5-20251001-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions              |
| -------------- | -------------------------------- |
| ap-southeast-2 | ap-southeast-2<br>ap-southeast-4 |
| ap-southeast-4 | ap-southeast-2<br>ap-southeast-4 |

To call the CA Nova Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
ca.amazon.nova-lite-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions       |
| -------------- | ------------------------- |
| ca-central-1   | ca-central-1<br>ca-west-1 |
| ca-west-1      | ca-central-1<br>ca-west-1 |

To call the EU Amazon Nova 2 Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.amazon.nova-2-lite-v1:0
```

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                              |
| -------------- | -------------------------------------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |

To call the EU Anthropic Claude 3 Haiku inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-3-haiku-20240307-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                    |
| -------------- | -------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-west-1<br>eu-west-3 |

To call the EU Anthropic Claude 3 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-3-sonnet-20240229-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                    |
| -------------- | -------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-west-1<br>eu-west-3 |

To call the EU Anthropic Claude 3.5 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-3-5-sonnet-20240620-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                    |
| -------------- | -------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-west-1<br>eu-west-3 |

To call the EU Anthropic Claude 3.7 Sonnet inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-3-7-sonnet-20250219-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                  |
| -------------- | ---------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |

To call the EU Anthropic Claude Haiku 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-haiku-4-5-20251001-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------ |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-central-2   | eu-central-1<br>eu-central-2<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-2      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-2<br>eu-west-3    |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |

To call the EU Anthropic Claude Opus 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-opus-4-5-20251101-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------ |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-central-2   | eu-central-1<br>eu-central-2<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-2      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-2<br>eu-west-3    |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |

To call the EU Anthropic Claude Sonnet 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-sonnet-4-5-20250929-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------ |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-central-2   | eu-central-1<br>eu-central-2<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-2      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-2<br>eu-west-3    |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |

To call the EU Claude Sonnet 4 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.anthropic.claude-sonnet-4-20250514-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------ |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| il-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3<br>il-central-1 |

To call the EU Cohere Embed v4 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.cohere.embed-v4:0
```

For more information about inference parameters for this model, see [Link](model-parameters-embed.md "model-parameters-embed.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                              |
| -------------- | -------------------------------------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |

To call the EU Meta Llama 3.2 1B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.meta.llama3-2-1b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                    |
| -------------- | -------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-west-1<br>eu-west-3 |

To call the EU Meta Llama 3.2 3B Instruct inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.meta.llama3-2-3b-instruct-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-meta.md "model-parameters-meta.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                    |
| -------------- | -------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-west-1<br>eu-west-3 |

To call the EU Mistral Pixtral Large 25.02 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.mistral.pixtral-large-2502-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-mistral.md "model-parameters-mistral.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                  |
| -------------- | ---------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3 |

To call the EU Nova Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.amazon.nova-lite-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| il-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-west-1<br>eu-west-3<br>il-central-1 |

To call the EU Nova Micro inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.amazon.nova-micro-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| il-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-west-1<br>eu-west-3<br>il-central-1 |

To call the EU Nova Pro inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.amazon.nova-pro-v1:0
```

For more information about inference parameters for this model, see [Link](../../../nova/latest/userguide/getting-started-schema.md "../../../nova/latest/userguide/getting-started-schema.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-west-1<br>eu-west-3                               |
| il-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-west-1<br>eu-west-3<br>il-central-1 |

To call the EU TwelveLabs Marengo Embed 3.0 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.twelvelabs.marengo-embed-3-0-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-marengo.md "model-parameters-marengo.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                              |
| -------------- | -------------------------------------------------------------------------------- |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |

To call the EU TwelveLabs Marengo Embed v2.7 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.twelvelabs.marengo-embed-2-7-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-marengo.md "model-parameters-marengo.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                              |
| -------------- | -------------------------------------------------------------------------------- |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |

To call the EU TwelveLabs Pegasus v1.2 inference profile, specify the following inference profile ID in one of the source Regions:

```
eu.twelvelabs.pegasus-1-2-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-pegasus.md "model-parameters-pegasus.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------ |
| eu-central-1   | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-central-2   | eu-central-1<br>eu-central-2<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3 |
| eu-north-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-1     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-south-2     | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-1      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |
| eu-west-2      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-2<br>eu-west-3    |
| eu-west-3      | eu-central-1<br>eu-north-1<br>eu-south-1<br>eu-south-2<br>eu-west-1<br>eu-west-3                 |

To call the JP Amazon Nova 2 Lite inference profile, specify the following inference profile ID in one of the source Regions:

```
jp.amazon.nova-2-lite-v1:0
```

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions              |
| -------------- | -------------------------------- |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-3 |

To call the JP Anthropic Claude Haiku 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
jp.anthropic.claude-haiku-4-5-20251001-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions              |
| -------------- | -------------------------------- |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-3 |
| ap-northeast-3 | ap-northeast-1<br>ap-northeast-3 |

To call the JP Anthropic Claude Sonnet 4.5 inference profile, specify the following inference profile ID in one of the source Regions:

```
jp.anthropic.claude-sonnet-4-5-20250929-v1:0
```

For more information about inference parameters for this model, see [Link](model-parameters-claude.md "model-parameters-claude.md").

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:

| Source Regions | Destination Regions              |
| -------------- | -------------------------------- |
| ap-northeast-1 | ap-northeast-1<br>ap-northeast-3 |
| ap-northeast-3 | ap-northeast-1<br>ap-northeast-3 |

## Supported Regions and models for application inference profiles

Application inference profiles can be created for all models in the following AWS Regions:

- ap-northeast-1
- ap-northeast-2
- ap-south-1
- ap-southeast-1
- ap-southeast-2
- ca-central-1
- eu-central-1
- eu-west-1
- eu-west-2
- eu-west-3
- sa-east-1
- us-east-1
- us-east-2
- us-gov-east-1
- us-west-2

Application inference profiles can be created from all models and inference profiles supported in Amazon Bedrock. For more information about models supported in Amazon Bedrock, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").
