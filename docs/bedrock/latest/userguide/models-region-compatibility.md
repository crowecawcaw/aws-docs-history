# Regional availability

Amazon Bedrock gives you three options so you can match the routing behavior of your inference calls to the scale, compliance, and cost requirements of your workload.

- **In-Region:** Your requests never leave the AWS Region you specify. Use this when regulations require strict single-Region data processing.
- **Geographic (Geo):** Bedrock intelligently routes within a defined geography (US, EU, Japan, or Australia) to maximize throughput while keeping data within regional boundaries. Use this when you have data residency requirements tied to a geography rather than a single Region.
- **Global:** Bedrock routes across all commercial Regions worldwide for the highest throughput and lowest cost. Use this when you have no data residency constraints and want the best performance and price.

## Inference options at a glance

|                    | **In-Region**                                                           | **Geographic (Geo) Cross-Region**                                                                                         | **Global Cross-Region**                                                      |
| ------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **How it works**   | Request is processed entirely within the single AWS Region you specify  | Bedrock automatically routes to the optimal Region within a defined geography (US, EU, APAC, JP, AU)                      | Bedrock routes to any commercial Region worldwide for optimal performance    |
| **Data residency** | Strictly within one Region                                              | Within geographic boundaries (e.g., all EU Regions); prompts and outputs may move within the geography but not outside it | No geographic restrictions; data may be processed in any commercial Region   |
| **Throughput**     | Limited to single-Region capacity; subject to per-Region service quotas | Higher than In-Region; absorbs regional traffic spikes within the geography                                               | Highest throughput; leverages global capacity                                |
| **Pricing**        | Standard on-demand pricing for that Region                              | Priced at source Region rates; no surcharge for cross-Region routing                                                      | Priced at source Region rates; no surcharge for cross-Region routing         |
| **modelId format** | Direct model ID: `anthropic.claude-3-5-sonnet-20241022-v2:0`            | Geography prefix + model ID: `us.anthropic.claude-3-5-sonnet-20241022-v2:0`                                               | Global prefix + model ID: `global.anthropic.claude-3-5-sonnet-20241022-v2:0` |
| **Best for**       | Strict single-Region compliance; Provisioned Throughput workloads       | Data residency regulations scoped to a geography (e.g., GDPR in EU, data sovereignty requirements)                        | Maximum throughput and cost efficiency with no data residency constraints    |

Now, let us look at Regional availability across all the models supported by Amazon Bedrock.

## AI21 Labs

| Jamba 1.5 Large           | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |

| Jamba 1.5 Mini            | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |

## Amazon

| Nova 2 Sonic              | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-north-1` (Stockholm)  | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |

| Nova 2 Lite                     | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | No     | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | Yes       | Yes |
| `ca-west-1` (Calgary)           | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | No     | No        | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | No        | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |

| Nova 2 Multimodal Embeddings | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | No        | No  |

| Titan Image Generator V2:0 | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |

| Titan Embed Text V2:0      | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `us-gov-east-1` (GovCloud) | Yes    | No        | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-central-2` (Zurich)    | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-south-2` (Spain)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `eu-west-3` (Paris)        | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-northeast-2` (Seoul)   | Yes    | No        | No  |
| `ap-northeast-3` (Osaka)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-south-2` (Hyderabad)   | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Titan Tg1 Large           | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |

| Titan Embed Image          | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `eu-west-3` (Paris)        | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Titan Embed Text           | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |

| Titan Embed G1 Text 02    | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |

| Nova Reel V1:1            | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |

| Rerank                     | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |

| Nova Sonic                | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)  | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |

| Nova Pro                    | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | Yes    | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-1` (N. California) | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)  | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)  | No     | Yes       | No  |
| `eu-north-1` (Stockholm)    | No     | Yes       | No  |
| `eu-south-1` (Milan)        | No     | Yes       | No  |
| `eu-south-2` (Spain)        | No     | Yes       | No  |
| `eu-west-1` (Ireland)       | No     | Yes       | No  |
| `eu-west-2` (London)        | Yes    | No        | No  |
| `eu-west-3` (Paris)         | No     | Yes       | No  |
| `ap-southeast-2` (Sydney)   | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)  | Yes    | No        | No  |
| `il-central-1` (Tel Aviv)   | No     | Yes       | No  |
| `me-central-1` (UAE)        | Yes    | No        | No  |

| Nova Reel                 | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |

| Nova Lite                   | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | Yes    | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-1` (N. California) | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)  | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)  | No     | Yes       | No  |
| `eu-north-1` (Stockholm)    | Yes    | Yes       | No  |
| `eu-south-1` (Milan)        | No     | Yes       | No  |
| `eu-south-2` (Spain)        | No     | Yes       | No  |
| `eu-west-1` (Ireland)       | No     | Yes       | No  |
| `eu-west-2` (London)        | Yes    | No        | No  |
| `eu-west-3` (Paris)         | No     | Yes       | No  |
| `ap-northeast-1` (Tokyo)    | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)   | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)  | Yes    | No        | No  |
| `il-central-1` (Tel Aviv)   | No     | Yes       | No  |
| `me-central-1` (UAE)        | Yes    | No        | No  |

| Nova Canvas               | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |

| Nova Micro                 | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | Yes       | No  |
| `us-east-2` (Ohio)         | No     | Yes       | No  |
| `us-west-2` (Oregon)       | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | No     | Yes       | No  |
| `eu-north-1` (Stockholm)   | No     | Yes       | No  |
| `eu-south-1` (Milan)       | No     | Yes       | No  |
| `eu-south-2` (Spain)       | No     | Yes       | No  |
| `eu-west-1` (Ireland)      | No     | Yes       | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `eu-west-3` (Paris)        | No     | Yes       | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `il-central-1` (Tel Aviv)  | No     | Yes       | No  |

| Nova Premier              | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

## Anthropic

| Claude Sonnet 4             | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | Yes |
| `us-east-2` (Ohio)          | No     | Yes       | Yes |
| `us-west-1` (N. California) | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)  | No     | Yes       | No  |
| `eu-north-1` (Stockholm)    | No     | Yes       | No  |
| `eu-south-1` (Milan)        | No     | Yes       | No  |
| `eu-south-2` (Spain)        | No     | Yes       | No  |
| `eu-west-1` (Ireland)       | No     | Yes       | Yes |
| `eu-west-3` (Paris)         | No     | Yes       | No  |
| `ap-northeast-1` (Tokyo)    | No     | No        | Yes |
| `il-central-1` (Tel Aviv)   | No     | Yes       | No  |

| Claude Opus 4             | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Claude Sonnet 4.6               | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | No     | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | Yes       | Yes |
| `ca-west-1` (Calgary)           | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-central-2` (Zurich)         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | Yes    | Yes       | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | No     | No        | Yes |
| `ap-northeast-3` (Osaka)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-south-2` (Hyderabad)        | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | Yes       | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |
| `me-south-1` (Bahrain)          | No     | No        | Yes |
| `af-south-1` (Cape Town)        | No     | No        | Yes |
| `sa-east-1` (São Paulo)         | No     | No        | Yes |
| `mx-central-1` (Mexico)         | No     | No        | Yes |

| Claude Opus 4.6                 | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | No     | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | Yes       | Yes |
| `ca-west-1` (Calgary)           | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-central-2` (Zurich)         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | No     | Yes       | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | No     | No        | Yes |
| `ap-northeast-3` (Osaka)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-south-2` (Hyderabad)        | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | Yes       | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |
| `me-south-1` (Bahrain)          | No     | No        | Yes |
| `af-south-1` (Cape Town)        | No     | No        | Yes |
| `sa-east-1` (São Paulo)         | No     | No        | Yes |
| `mx-central-1` (Mexico)         | No     | No        | Yes |

| Claude Opus 4.5                 | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | No     | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | Yes       | Yes |
| `ca-west-1` (Calgary)           | No     | No        | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-central-2` (Zurich)         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | No     | Yes       | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | No     | No        | Yes |
| `ap-northeast-3` (Osaka)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-south-2` (Hyderabad)        | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | No        | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |
| `me-south-1` (Bahrain)          | No     | No        | Yes |
| `af-south-1` (Cape Town)        | No     | No        | Yes |
| `sa-east-1` (São Paulo)         | No     | No        | Yes |
| `mx-central-1` (Mexico)         | No     | No        | Yes |

| Claude Haiku 4.5                | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | No     | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | Yes       | Yes |
| `ca-west-1` (Calgary)           | No     | No        | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-central-2` (Zurich)         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | No     | Yes       | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | No     | No        | Yes |
| `ap-northeast-3` (Osaka)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-south-2` (Hyderabad)        | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | Yes       | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |
| `me-south-1` (Bahrain)          | No     | No        | Yes |
| `af-south-1` (Cape Town)        | No     | No        | Yes |
| `sa-east-1` (São Paulo)         | No     | No        | Yes |
| `mx-central-1` (Mexico)         | No     | No        | Yes |

| Claude Sonnet 4.5               | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | No     | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | Yes       | Yes |
| `ca-west-1` (Calgary)           | No     | No        | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-central-2` (Zurich)         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | No     | Yes       | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | No     | No        | Yes |
| `ap-northeast-3` (Osaka)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-south-2` (Hyderabad)        | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | Yes       | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |
| `me-south-1` (Bahrain)          | No     | No        | Yes |
| `af-south-1` (Cape Town)        | No     | No        | Yes |
| `sa-east-1` (São Paulo)         | No     | No        | Yes |
| `mx-central-1` (Mexico)         | No     | No        | Yes |

| Claude Opus 4.1           | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Claude 3 Haiku               | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | Yes       | No  |
| `us-east-2` (Ohio)           | No     | Yes       | No  |
| `us-west-2` (Oregon)         | Yes    | Yes       | No  |
| `us-gov-west-1` (GovCloud)   | Yes    | No        | No  |
| `ca-central-1` (Canada)      | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)   | Yes    | Yes       | No  |
| `eu-central-2` (Zurich)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)        | Yes    | Yes       | No  |
| `eu-west-2` (London)         | Yes    | No        | No  |
| `eu-west-3` (Paris)          | Yes    | Yes       | No  |
| `ap-northeast-1` (Tokyo)     | Yes    | No        | No  |
| `ap-northeast-2` (Seoul)     | Yes    | No        | No  |
| `ap-south-1` (Mumbai)        | Yes    | No        | No  |
| `ap-southeast-1` (Singapore) | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)    | Yes    | No        | No  |
| `sa-east-1` (São Paulo)      | Yes    | No        | No  |

| Claude 3 Sonnet            | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | Yes       | No  |
| `us-west-2` (Oregon)       | Yes    | Yes       | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | Yes       | No  |
| `eu-west-1` (Ireland)      | Yes    | Yes       | No  |
| `eu-west-3` (Paris)        | Yes    | Yes       | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Claude 3.7 Sonnet          | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | No     | Yes       | No  |
| `us-east-2` (Ohio)         | No     | Yes       | No  |
| `us-west-2` (Oregon)       | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | No     | Yes       | No  |
| `eu-north-1` (Stockholm)   | No     | Yes       | No  |
| `eu-west-1` (Ireland)      | No     | Yes       | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `eu-west-3` (Paris)        | No     | Yes       | No  |

| Claude 3.5 Sonnet V2:0     | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | No     | Yes       | No  |
| `us-east-2` (Ohio)         | No     | Yes       | No  |
| `us-west-2` (Oregon)       | Yes    | Yes       | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |

| Claude 3.5 Haiku          | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | Yes    | Yes       | No  |

| Claude 3.5 Sonnet            | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | Yes       | No  |
| `us-east-2` (Ohio)           | No     | Yes       | No  |
| `us-west-2` (Oregon)         | Yes    | Yes       | No  |
| `us-gov-west-1` (GovCloud)   | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)   | Yes    | Yes       | No  |
| `eu-central-2` (Zurich)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)        | No     | Yes       | No  |
| `eu-west-3` (Paris)          | No     | Yes       | No  |
| `ap-northeast-1` (Tokyo)     | Yes    | No        | No  |
| `ap-northeast-2` (Seoul)     | Yes    | No        | No  |
| `ap-southeast-1` (Singapore) | Yes    | No        | No  |

## Cohere

| Embed V4:0                   | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | Yes       | Yes |
| `us-east-2` (Ohio)           | No     | Yes       | Yes |
| `us-west-1` (N. California)  | No     | Yes       | Yes |
| `us-west-2` (Oregon)         | No     | Yes       | Yes |
| `ca-central-1` (Canada)      | No     | No        | Yes |
| `eu-central-1` (Frankfurt)   | No     | Yes       | Yes |
| `eu-central-2` (Zurich)      | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)     | No     | Yes       | Yes |
| `eu-south-1` (Milan)         | No     | Yes       | Yes |
| `eu-south-2` (Spain)         | No     | Yes       | Yes |
| `eu-west-1` (Ireland)        | Yes    | Yes       | Yes |
| `eu-west-2` (London)         | No     | Yes       | Yes |
| `eu-west-3` (Paris)          | No     | Yes       | Yes |
| `ap-northeast-1` (Tokyo)     | Yes    | No        | Yes |
| `ap-northeast-2` (Seoul)     | No     | No        | Yes |
| `ap-northeast-3` (Osaka)     | No     | No        | Yes |
| `ap-south-1` (Mumbai)        | No     | No        | Yes |
| `ap-south-2` (Hyderabad)     | No     | No        | Yes |
| `ap-southeast-1` (Singapore) | No     | No        | Yes |
| `ap-southeast-2` (Sydney)    | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)   | No     | No        | Yes |
| `ap-southeast-4` (Melbourne) | No     | No        | Yes |
| `sa-east-1` (São Paulo)      | No     | No        | Yes |

| Embed English                | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | No        | No  |
| `us-west-2` (Oregon)         | Yes    | No        | No  |
| `ca-central-1` (Canada)      | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)   | Yes    | No        | No  |
| `eu-west-1` (Ireland)        | Yes    | No        | No  |
| `eu-west-2` (London)         | Yes    | No        | No  |
| `eu-west-3` (Paris)          | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)     | Yes    | No        | No  |
| `ap-south-1` (Mumbai)        | Yes    | No        | No  |
| `ap-southeast-1` (Singapore) | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)    | Yes    | No        | No  |
| `sa-east-1` (São Paulo)      | Yes    | No        | No  |

| Embed Multilingual           | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | No        | No  |
| `us-west-2` (Oregon)         | Yes    | No        | No  |
| `ca-central-1` (Canada)      | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)   | Yes    | No        | No  |
| `eu-west-1` (Ireland)        | Yes    | No        | No  |
| `eu-west-2` (London)         | Yes    | No        | No  |
| `eu-west-3` (Paris)          | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)     | Yes    | No        | No  |
| `ap-south-1` (Mumbai)        | Yes    | No        | No  |
| `ap-southeast-1` (Singapore) | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)    | Yes    | No        | No  |
| `sa-east-1` (São Paulo)      | Yes    | No        | No  |

| Rerank V3 5:0              | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |

| Command R                 | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |

| Command R Plus            | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |

## DeepSeek

| Deepseek V3.2              | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Deepseek                   | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |

| Deepseek R1               | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

## Google

| Gemma 3 27B It            | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Gemma 3 12B It            | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Gemma 3 4B It             | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

## Luma

| Ray V2:0             | Region | In-Region | Geo | Global |
| -------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon) | Yes    | No        | No  |

## Meta

| Llama4 Maverick 17B Instruct | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | No     | Yes       | No  |
| `us-east-2` (Ohio)           | No     | Yes       | No  |
| `us-west-1` (N. California)  | No     | Yes       | No  |
| `us-west-2` (Oregon)         | No     | Yes       | No  |

| Llama4 Scout 17B Instruct   | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-1` (N. California) | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

| Llama3 70B Instruct        | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |

| Llama3 8B Instruct         | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |

| Llama3.3 70B Instruct     | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | Yes    | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Llama3.2 90B Instruct     | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Llama3.2 11B Instruct     | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Llama3.2 3B Instruct       | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | No     | Yes       | No  |
| `us-east-2` (Ohio)         | No     | Yes       | No  |
| `us-west-2` (Oregon)       | No     | Yes       | No  |
| `eu-central-1` (Frankfurt) | No     | Yes       | No  |
| `eu-west-1` (Ireland)      | No     | Yes       | No  |
| `eu-west-3` (Paris)        | No     | Yes       | No  |

| Llama3.2 1B Instruct       | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | No     | Yes       | No  |
| `us-east-2` (Ohio)         | No     | Yes       | No  |
| `us-west-2` (Oregon)       | No     | Yes       | No  |
| `eu-central-1` (Frankfurt) | No     | Yes       | No  |
| `eu-west-1` (Ireland)      | No     | Yes       | No  |
| `eu-west-3` (Paris)        | No     | Yes       | No  |

| Llama3.1 405B Instruct | Region | In-Region | Geo | Global |
| ---------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)     | No     | Yes       | No  |
| `us-west-2` (Oregon)   | Yes    | No        | No  |

| Llama3.1 70B Instruct     | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | Yes    | Yes       | No  |

| Llama3.1 8B Instruct      | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | Yes    | Yes       | No  |

## MiniMax

| Minimax M2                | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Minimax M2.1               | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

## Mistral AI

| Magistral Small 2509      | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Pixtral Large 2502         | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | No     | Yes       | No  |
| `us-east-2` (Ohio)         | No     | Yes       | No  |
| `us-west-2` (Oregon)       | No     | Yes       | No  |
| `eu-central-1` (Frankfurt) | No     | Yes       | No  |
| `eu-north-1` (Stockholm)   | No     | Yes       | No  |
| `eu-west-1` (Ireland)      | No     | Yes       | No  |
| `eu-west-3` (Paris)        | No     | Yes       | No  |

| Mistral Large 2407   | Region | In-Region | Geo | Global |
| -------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon) | Yes    | No        | No  |

| Mistral Small 2402        | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |

| Mistral Large 2402        | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `ca-central-1` (Canada)   | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `eu-west-3` (Paris)       | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Voxtral Small 24B 2507    | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Mixtral 8X7B Instruct V0:1 | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `eu-west-3` (Paris)        | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Mistral 7B Instruct V0:2  | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `ca-central-1` (Canada)   | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `eu-west-3` (Paris)       | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Voxtral Mini 3B 2507      | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Mistral Large 3 675B Instruct | Region | In-Region | Geo | Global |
| ----------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)     | Yes    | No        | No  |
| `us-east-2` (Ohio)            | Yes    | No        | No  |
| `us-west-2` (Oregon)          | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)      | Yes    | No        | No  |
| `ap-south-1` (Mumbai)         | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)     | Yes    | No        | No  |
| `sa-east-1` (São Paulo)       | Yes    | No        | No  |

| Ministral 3 14B Instruct  | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Ministral 3 8B Instruct   | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Ministral 3 3B Instruct   | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Devstral 2 123B            | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

## Moonshot AI

| Kimi K2 Thinking          | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

## Moonshot AI

| Kimi K2.5                  | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

## NVIDIA

| Nemotron Nano 12B         | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Nemotron Nano 9B          | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Nemotron Nano 3 30B       | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

## OpenAI

| Gpt Oss Safeguard 120B    | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Gpt Oss 120B 1:0           | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Gpt Oss Safeguard 20B     | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Gpt Oss 20B 1:0            | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

## Qwen

| Qwen3 Coder Next          | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |

| Qwen3 Coder 480B A35B      | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |

| Qwen3 235B A22B 2507       | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |

| Qwen3 Vl 235B A22B        | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Qwen3 Next 80B A3B        | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | No        | No  |
| `us-east-2` (Ohio)        | Yes    | No        | No  |
| `us-west-2` (Oregon)      | Yes    | No        | No  |
| `eu-south-1` (Milan)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)     | Yes    | No        | No  |
| `eu-west-2` (London)      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)   | Yes    | No        | No  |

| Qwen3 32B                  | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Qwen3 Coder 30B A3B        | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

## Stability AI

| Sd3.5 Large          | Region | In-Region | Geo | Global |
| -------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon) | Yes    | No        | No  |

| Stable Image Core V1:1 | Region | In-Region | Geo | Global |
| ---------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon)   | Yes    | No        | No  |

| Stable Image Ultra V1:1 | Region | In-Region | Geo | Global |
| ----------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon)    | Yes    | No        | No  |

| Stable Image Control Structure | Region | In-Region | Geo | Global |
| ------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)      | No     | Yes       | No  |
| `us-east-2` (Ohio)             | No     | Yes       | No  |
| `us-west-2` (Oregon)           | No     | Yes       | No  |

| Stable Conservative Upscale | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

| Stable Fast Upscale       | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Image Control Sketch | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

| Stable Image Search Recolor | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

| Stable Creative Upscale   | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Image Erase Object | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Image Inpaint      | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Outpaint           | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Image Search Replace | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

| Stable Style Transfer     | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Image Style Guide  | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| Stable Image Remove Background | Region | In-Region | Geo | Global |
| ------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)      | No     | Yes       | No  |
| `us-east-2` (Ohio)             | No     | Yes       | No  |
| `us-west-2` (Oregon)           | No     | Yes       | No  |

## TwelveLabs

| Marengo Embed 3.0         | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | Yes    | Yes       | No  |
| `eu-west-1` (Ireland)     | No     | Yes       | No  |
| `ap-northeast-2` (Seoul)  | Yes    | No        | No  |

| Marengo Embed 2.7         | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `eu-west-1` (Ireland)     | No     | Yes       | No  |

| Pegasus 1.2                     | Region | In-Region | Geo | Global |
| ------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)       | Yes    | Yes       | Yes |
| `us-east-2` (Ohio)              | No     | Yes       | Yes |
| `us-west-1` (N. California)     | No     | Yes       | Yes |
| `us-west-2` (Oregon)            | No     | Yes       | Yes |
| `ca-central-1` (Canada)         | No     | No        | Yes |
| `ca-west-1` (Calgary)           | No     | No        | Yes |
| `eu-central-1` (Frankfurt)      | No     | Yes       | Yes |
| `eu-central-2` (Zurich)         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)        | No     | Yes       | Yes |
| `eu-south-1` (Milan)            | No     | Yes       | Yes |
| `eu-south-2` (Spain)            | No     | Yes       | Yes |
| `eu-west-1` (Ireland)           | No     | Yes       | Yes |
| `eu-west-2` (London)            | No     | Yes       | Yes |
| `eu-west-3` (Paris)             | No     | Yes       | Yes |
| `ap-east-2` (Malaysia)          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)        | No     | No        | Yes |
| `ap-northeast-2` (Seoul)        | Yes    | No        | Yes |
| `ap-northeast-3` (Osaka)        | No     | No        | Yes |
| `ap-south-1` (Mumbai)           | No     | No        | Yes |
| `ap-south-2` (Hyderabad)        | No     | No        | Yes |
| `ap-southeast-1` (Singapore)    | No     | No        | Yes |
| `ap-southeast-2` (Sydney)       | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)      | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)    | No     | No        | Yes |
| `ap-southeast-5` (Auckland)     | No     | No        | Yes |
| `ap-southeast-7` (Kuala Lumpur) | No     | No        | Yes |
| `il-central-1` (Tel Aviv)       | No     | No        | Yes |
| `me-central-1` (UAE)            | No     | No        | Yes |
| `me-south-1` (Bahrain)          | No     | No        | Yes |
| `af-south-1` (Cape Town)        | No     | No        | Yes |
| `sa-east-1` (São Paulo)         | No     | No        | Yes |
| `mx-central-1` (Mexico)         | No     | No        | Yes |

## Writer

| Palmyra X5                  | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-1` (N. California) | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

| Palmyra X4                  | Region | In-Region | Geo | Global |
| --------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)   | No     | Yes       | No  |
| `us-east-2` (Ohio)          | No     | Yes       | No  |
| `us-west-1` (N. California) | No     | Yes       | No  |
| `us-west-2` (Oregon)        | No     | Yes       | No  |

## Z.AI

| Glm 4.7 Flash              | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-south-1` (Milan)       | Yes    | No        | No  |
| `eu-west-1` (Ireland)      | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |

| Glm 4.7                    | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)  | Yes    | No        | No  |
| `us-east-2` (Ohio)         | Yes    | No        | No  |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)   | Yes    | No        | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta) | Yes    | No        | No  |
| `sa-east-1` (São Paulo)    | Yes    | No        | No  |
