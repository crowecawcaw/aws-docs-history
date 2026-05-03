# Regional availability

Amazon Bedrock gives you three options so you can match the routing behavior of your inference calls to the scale, compliance, and cost requirements of your workload.

###### Process to enabling Bedrock models in GovCloud

Accessing Bedrock foundation models in AWS GovCloud (US) requires initiating the access request through the standard AWS account linked to your GovCloud account. You must first agree to the model's End User License Agreement (EULA) in a standard region (`us-east-1` or `us-west-2`), then enable the model in your GovCloud account. You can do this in two ways:

- **Console:** Sign in to your linked standard AWS account, open the Amazon Bedrock Chat/Text playground, choose the model, and run a prompt to establish the EULA.
- **AWS CLI:** Run `aws bedrock list-foundation-models` to get the model ID, then `aws bedrock list-foundation-model-agreement-offers --model-id <model-id>` to get the offer token, and finally `aws bedrock create-foundation-model-agreement --model-id <model-id> --offer-token <offerToken>`.
  After completing either method, go to your GovCloud account and enable the model via the Model Access page. It may take a few minutes for entitlements to propagate. For the full walkthrough, see [Process to enabling Bedrock models in GovCloud](https://repost.aws/articles/ARUT8Sy76NTUmRN7kuiU0UXQ "https://repost.aws/articles/ARUT8Sy76NTUmRN7kuiU0UXQ").

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

| [Jamba 1.5 Large](model-card-ai21-labs-jamba-1-5-large.md "model-card-ai21-labs-jamba-1-5-large.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | Yes    | No        | No  |

| [Jamba 1.5 Mini](model-card-ai21-labs-jamba-1-5-mini.md "model-card-ai21-labs-jamba-1-5-mini.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                         | Yes    | No        | No  |

## Amazon

| [Nova 2 Sonic](model-card-amazon-nova-2-sonic.md "model-card-amazon-nova-2-sonic.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                             | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                  | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                              | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                              | Yes    | No        | No  |

| [Nova 2 Lite](model-card-amazon-nova-2-lite.md "model-card-amazon-nova-2-lite.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                          | No     | Yes       | Yes |
| `us-east-2` (Ohio)                                                                 | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                        | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                               | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                            | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                              | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)                                                         | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                           | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                               | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                               | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                              | No     | Yes       | Yes |
| `eu-west-2` (London)                                                               | No     | No        | Yes |
| `eu-west-3` (Paris)                                                                | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                               | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                           | No     | No        | Yes |
| `ap-northeast-2` (Seoul)                                                           | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                              | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                       | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                          | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)                                                         | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                       | No     | No        | Yes |
| `ap-southeast-5` (Malaysia)                                                        | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                     | No     | No        | Yes |
| `ap-southeast-7` (Thailand)                                                        | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                          | No     | No        | Yes |
| `me-central-1` (UAE)                                                               | No     | No        | Yes |

| [Amazon Nova Multimodal Embeddings](model-card-amazon-amazon-nova-multimodal-embeddings.md "model-card-amazon-amazon-nova-multimodal-embeddings.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                            | Yes    | No        | No  |

| [Titan Image Generator G1 v2](model-card-amazon-titan-image-generator-g1-v2.md "model-card-amazon-titan-image-generator-g1-v2.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                          | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                               | Yes    | No        | No  |

| [Titan Text Embeddings V2](model-card-amazon-titan-text-embeddings-v2.md "model-card-amazon-titan-text-embeddings-v2.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                 | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                        | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                      | Yes    | No        | No  |
| `us-gov-east-1` (GovCloud)                                                                                                | Yes    | No        | No  |
| `us-gov-west-1` (GovCloud)                                                                                                | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                                   | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                                                | Yes    | No        | No  |
| `eu-central-2` (Zurich)                                                                                                   | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                                                  | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                      | Yes    | No        | No  |
| `eu-south-2` (Spain)                                                                                                      | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                     | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                      | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                                                       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                  | Yes    | No        | No  |
| `ap-northeast-2` (Seoul)                                                                                                  | Yes    | No        | No  |
| `ap-northeast-3` (Osaka)                                                                                                  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                     | Yes    | No        | No  |
| `ap-south-2` (Hyderabad)                                                                                                  | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                 | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                   | Yes    | No        | No  |

| [Titan Text Large](model-card-amazon-titan-text-large.md "model-card-amazon-titan-text-large.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                         | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                              | Yes    | No        | No  |

| [Titan Multimodal Embeddings G1](model-card-amazon-titan-multimodal-embeddings-g1.md "model-card-amazon-titan-multimodal-embeddings-g1.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                   | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                                        | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                                                     | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                                                                  | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                                       | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                                        | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                                                                         | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                                       | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                                   | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                                     | Yes    | No        | No  |

| [Titan Embeddings G1 - Text](model-card-amazon-titan-embeddings-g1---text.md "model-card-amazon-titan-embeddings-g1---text.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                       | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                            | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                                                      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                        | Yes    | No        | No  |

| [Titan Embeddings G1 - Text v2](model-card-amazon-titan-text-embeddings-v2-2.md "model-card-amazon-titan-text-embeddings-v2-2.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                          | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                               | Yes    | No        | No  |

| [Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md") | Region                   | In-Region | Geo | Global |
| ---------------------------------------------------------------------------- | ------------------------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                    | Legacy (EOL: 2026-09-30) | No        | No  |

| Rerank                     | Region | In-Region | Geo | Global |
| -------------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon)       | Yes    | No        | No  |
| `ca-central-1` (Canada)    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)   | Yes    | No        | No  |

| [Nova Sonic](model-card-amazon-nova-sonic.md "model-card-amazon-nova-sonic.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                        | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                        | Yes    | No        | No  |

| [Nova Pro](model-card-amazon-nova-pro.md "model-card-amazon-nova-pro.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                 | Yes    | Yes       | No  |
| `us-east-2` (Ohio)                                                        | No     | Yes       | No  |
| `us-west-1` (N. California)                                               | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                      | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)                                                | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                | No     | Yes       | No  |
| `eu-north-1` (Stockholm)                                                  | No     | Yes       | No  |
| `eu-south-1` (Milan)                                                      | No     | Yes       | No  |
| `eu-south-2` (Spain)                                                      | No     | Yes       | No  |
| `eu-west-1` (Ireland)                                                     | No     | Yes       | No  |
| `eu-west-2` (London)                                                      | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                       | No     | Yes       | No  |
| `ap-southeast-2` (Sydney)                                                 | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                | Yes    | No        | No  |
| `il-central-1` (Tel Aviv)                                                 | No     | Yes       | No  |
| `me-central-1` (UAE)                                                      | Yes    | No        | No  |

| [Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                    | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                        | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                     | Yes    | No        | No  |

| [Nova Lite](model-card-amazon-nova-lite.md "model-card-amazon-nova-lite.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                    | Yes    | Yes       | No  |
| `us-east-2` (Ohio)                                                           | No     | Yes       | No  |
| `us-west-1` (N. California)                                                  | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                         | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)                                                   | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                   | No     | Yes       | No  |
| `eu-north-1` (Stockholm)                                                     | Yes    | Yes       | No  |
| `eu-south-1` (Milan)                                                         | No     | Yes       | No  |
| `eu-south-2` (Spain)                                                         | No     | Yes       | No  |
| `eu-west-1` (Ireland)                                                        | No     | Yes       | No  |
| `eu-west-2` (London)                                                         | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                          | No     | Yes       | No  |
| `ap-northeast-1` (Tokyo)                                                     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                    | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                   | Yes    | No        | No  |
| `il-central-1` (Tel Aviv)                                                    | No     | Yes       | No  |
| `me-central-1` (UAE)                                                         | Yes    | No        | No  |

| [Nova Canvas](model-card-amazon-nova-canvas.md "model-card-amazon-nova-canvas.md") | Region                   | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------- | ------------------------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                          | Legacy (EOL: 2026-09-30) | No        | No  |
| `eu-west-1` (Ireland)                                                              | Yes                      | No        | No  |
| `ap-northeast-1` (Tokyo)                                                           | Yes                      | No        | No  |

| [Nova Micro](model-card-amazon-nova-micro.md "model-card-amazon-nova-micro.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                       | Yes    | Yes       | No  |
| `us-east-2` (Ohio)                                                              | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                            | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)                                                      | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                      | No     | Yes       | No  |
| `eu-north-1` (Stockholm)                                                        | No     | Yes       | No  |
| `eu-south-1` (Milan)                                                            | No     | Yes       | No  |
| `eu-south-2` (Spain)                                                            | No     | Yes       | No  |
| `eu-west-1` (Ireland)                                                           | No     | Yes       | No  |
| `eu-west-2` (London)                                                            | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                             | No     | Yes       | No  |
| `ap-southeast-2` (Sydney)                                                       | Yes    | No        | No  |
| `il-central-1` (Tel Aviv)                                                       | No     | Yes       | No  |

| [Nova Premier](model-card-amazon-nova-premier.md "model-card-amazon-nova-premier.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                             | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                    | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                  | No     | Yes       | No  |

## Anthropic

| [Claude Mythos Preview](model-card-anthropic-claude-mythos-preview.md "model-card-anthropic-claude-mythos-preview.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                              | Yes    | No        | No  |

| [Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md "model-card-anthropic-claude-sonnet-4.md") | Region | In-Region                | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | No     | Yes                      | Yes |
| `us-east-2` (Ohio)                                                                                   | No     | Legacy (EOL: 2026-10-14) | Yes |
| `us-west-1` (N. California)                                                                          | No     | Yes                      | No  |
| `us-west-2` (Oregon)                                                                                 | No     | Yes                      | Yes |
| `eu-central-1` (Frankfurt)                                                                           | No     | Yes                      | No  |
| `eu-north-1` (Stockholm)                                                                             | No     | Yes                      | No  |
| `eu-south-1` (Milan)                                                                                 | No     | Yes                      | No  |
| `eu-south-2` (Spain)                                                                                 | No     | Yes                      | No  |
| `eu-west-1` (Ireland)                                                                                | No     | Yes                      | Yes |
| `eu-west-3` (Paris)                                                                                  | No     | Yes                      | No  |
| `ap-northeast-1` (Tokyo)                                                                             | No     | No                       | Yes |
| `il-central-1` (Tel Aviv)                                                                            | No     | Yes                      | No  |

| Claude Opus 4             | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | No     | Yes       | No  |

| [Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md "model-card-anthropic-claude-sonnet-4-6.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                  | No     | Yes       | Yes |
| `us-east-2` (Ohio)                                                                                         | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                                                | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                                       | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                                                    | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                                                      | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)                                                                                 | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                                    | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                                   | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                                                       | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                                       | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                                      | No     | Yes       | Yes |
| `eu-west-2` (London)                                                                                       | Yes    | Yes       | Yes |
| `eu-west-3` (Paris)                                                                                        | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                                       | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                                   | No     | No        | Yes |
| `ap-northeast-2` (Seoul)                                                                                   | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                                   | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                                                      | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                                   | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                               | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                                  | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)                                                                                 | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                               | No     | Yes       | Yes |
| `ap-southeast-5` (Malaysia)                                                                                | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                                             | No     | Yes       | Yes |
| `ap-southeast-7` (Thailand)                                                                                | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                                  | No     | No        | Yes |
| `me-central-1` (UAE)                                                                                       | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                                     | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                                   | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                                    | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                                    | No     | No        | Yes |

| [Claude Opus 4.7](model-card-anthropic-claude-opus-4-7.md "model-card-anthropic-claude-opus-4-7.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | Yes    | Yes       | Yes |
| `us-east-2` (Ohio)                                                                                   | Yes    | Yes       | Yes |
| `us-west-1` (N. California)                                                                          | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                                 | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                                              | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                                                | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)                                                                           | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                              | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                             | Yes    | Yes       | Yes |
| `eu-south-1` (Milan)                                                                                 | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                                 | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                                | Yes    | Yes       | Yes |
| `eu-west-2` (London)                                                                                 | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                                                  | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                                 | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                             | Yes    | Yes       | Yes |
| `ap-northeast-2` (Seoul)                                                                             | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                             | No     | Yes       | Yes |
| `ap-south-1` (Mumbai)                                                                                | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                             | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                         | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                            | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)                                                                           | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                         | No     | Yes       | Yes |
| `ap-southeast-5` (Malaysia)                                                                          | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                                       | No     | Yes       | Yes |
| `ap-southeast-7` (Thailand)                                                                          | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                            | No     | No        | Yes |
| `me-central-1` (UAE)                                                                                 | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                               | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                             | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                              | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                              | No     | No        | Yes |

| [Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md "model-card-anthropic-claude-opus-4-6.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | No     | Yes       | Yes |
| `us-east-2` (Ohio)                                                                                   | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                                          | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                                 | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                                              | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                                                | No     | Yes       | Yes |
| `eu-central-1` (Frankfurt)                                                                           | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                              | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                             | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                                                 | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                                 | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                                | No     | Yes       | Yes |
| `eu-west-2` (London)                                                                                 | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                                                  | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                                 | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                             | No     | No        | Yes |
| `ap-northeast-2` (Seoul)                                                                             | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                             | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                                                | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                             | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                         | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                            | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)                                                                           | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                         | No     | Yes       | Yes |
| `ap-southeast-5` (Malaysia)                                                                          | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                                       | No     | Yes       | Yes |
| `ap-southeast-7` (Thailand)                                                                          | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                            | No     | No        | Yes |
| `me-central-1` (UAE)                                                                                 | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                               | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                             | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                              | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                              | No     | No        | Yes |

| [Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md "model-card-anthropic-claude-opus-4-5.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | No     | Yes       | Yes |
| `us-east-2` (Ohio)                                                                                   | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                                          | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                                 | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                                              | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                                                | No     | No        | Yes |
| `eu-central-1` (Frankfurt)                                                                           | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                              | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                             | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                                                 | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                                 | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                                | No     | Yes       | Yes |
| `eu-west-2` (London)                                                                                 | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                                                  | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                                 | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                             | No     | No        | Yes |
| `ap-northeast-2` (Seoul)                                                                             | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                             | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                                                | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                             | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                         | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                            | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)                                                                           | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                         | No     | No        | Yes |
| `ap-southeast-5` (Malaysia)                                                                          | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                                       | No     | No        | Yes |
| `ap-southeast-7` (Thailand)                                                                          | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                            | No     | No        | Yes |
| `me-central-1` (UAE)                                                                                 | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                               | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                             | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                              | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                              | No     | No        | Yes |

| [Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md "model-card-anthropic-claude-haiku-4-5.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                               | Yes    | Yes       | Yes |
| `us-east-2` (Ohio)                                                                                      | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                                             | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                                    | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                                                 | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                                                   | No     | No        | Yes |
| `eu-central-1` (Frankfurt)                                                                              | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                                 | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                                | Yes    | Yes       | Yes |
| `eu-south-1` (Milan)                                                                                    | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                                    | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                                   | Yes    | Yes       | Yes |
| `eu-west-2` (London)                                                                                    | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                                                     | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                                    | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                                | Yes    | No        | Yes |
| `ap-northeast-2` (Seoul)                                                                                | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                                | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                                                   | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                                | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                            | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                               | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)                                                                              | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                            | Yes    | Yes       | Yes |
| `ap-southeast-5` (Malaysia)                                                                             | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                                          | No     | Yes       | Yes |
| `ap-southeast-7` (Thailand)                                                                             | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                               | No     | No        | Yes |
| `me-central-1` (UAE)                                                                                    | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                                  | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                                | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                                 | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                                 | No     | No        | Yes |

| [Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md "model-card-anthropic-claude-sonnet-4-5.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                  | No     | Yes       | Yes |
| `us-east-2` (Ohio)                                                                                         | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                                                | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                                       | No     | Yes       | Yes |
| `us-gov-east-1` (GovCloud)                                                                                 | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)                                                                                 | No     | Yes       | No  |
| `ca-central-1` (Canada)                                                                                    | No     | Yes       | Yes |
| `ca-west-1` (Calgary)                                                                                      | No     | No        | Yes |
| `eu-central-1` (Frankfurt)                                                                                 | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                                    | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                                   | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                                                       | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                                       | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                                      | No     | Yes       | Yes |
| `eu-west-2` (London)                                                                                       | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                                                        | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                                       | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                                   | No     | No        | Yes |
| `ap-northeast-2` (Seoul)                                                                                   | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                                   | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                                                      | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                                   | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                               | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                                  | No     | Yes       | Yes |
| `ap-southeast-3` (Jakarta)                                                                                 | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                               | No     | Yes       | Yes |
| `ap-southeast-5` (Malaysia)                                                                                | No     | No        | Yes |
| `ap-southeast-6` (New Zealand)                                                                             | No     | Yes       | Yes |
| `ap-southeast-7` (Thailand)                                                                                | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                                  | No     | No        | Yes |
| `me-central-1` (UAE)                                                                                       | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                                     | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                                   | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                                    | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                                    | No     | No        | Yes |

| [Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md "model-card-anthropic-claude-opus-4-1.md") | Region | In-Region                | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | No     | Legacy (EOL: 2026-05-31) | No  |
| `us-east-2` (Ohio)                                                                                   | No     | Legacy (EOL: 2026-05-31) | No  |
| `us-west-2` (Oregon)                                                                                 | No     | Legacy (EOL: 2026-05-31) | No  |

| [Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md "model-card-anthropic-claude-3-haiku.md") | Region                   | In-Region                | Geo | Global |
| ------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                         | Legacy (EOL: 2026-09-10) | Yes                      | No  |
| `us-east-2` (Ohio)                                                                                | No                       | Legacy (EOL: 2026-09-10) | No  |
| `us-west-2` (Oregon)                                                                              | Legacy (EOL: 2026-09-10) | Yes                      | No  |
| `us-gov-east-1` (GovCloud)                                                                        | No                       | Yes                      | No  |
| `us-gov-west-1` (GovCloud)                                                                        | Yes                      | No                       | No  |
| `ca-central-1` (Canada)                                                                           | Yes                      | No                       | No  |
| `eu-central-1` (Frankfurt)                                                                        | Legacy (EOL: 2026-09-10) | Yes                      | No  |
| `eu-central-2` (Zurich)                                                                           | Yes                      | No                       | No  |
| `eu-west-1` (Ireland)                                                                             | Legacy (EOL: 2026-09-10) | Yes                      | No  |
| `eu-west-2` (London)                                                                              | Yes                      | No                       | No  |
| `eu-west-3` (Paris)                                                                               | Legacy (EOL: 2026-09-10) | Yes                      | No  |
| `ap-northeast-1` (Tokyo)                                                                          | Legacy (EOL: 2026-09-10) | No                       | No  |
| `ap-northeast-2` (Seoul)                                                                          | Yes                      | No                       | No  |
| `ap-south-1` (Mumbai)                                                                             | Yes                      | No                       | No  |
| `ap-southeast-1` (Singapore)                                                                      | Yes                      | No                       | No  |
| `ap-southeast-2` (Sydney)                                                                         | Legacy (EOL: 2026-09-10) | No                       | No  |
| `sa-east-1` (São Paulo)                                                                           | Yes                      | No                       | No  |

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
| `us-gov-east-1` (GovCloud) | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud) | Yes    | No        | No  |
| `eu-central-1` (Frankfurt) | No     | Yes       | No  |
| `eu-north-1` (Stockholm)   | No     | Yes       | No  |
| `eu-west-1` (Ireland)      | No     | Yes       | No  |
| `eu-west-2` (London)       | Yes    | No        | No  |
| `eu-west-3` (Paris)        | No     | Yes       | No  |

| Claude 3.5 Sonnet V2:0    | Region | In-Region | Geo | Global |
| ------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia) | No     | Yes       | No  |
| `us-east-2` (Ohio)        | No     | Yes       | No  |
| `us-west-2` (Oregon)      | Yes    | Yes       | No  |
| `ap-southeast-2` (Sydney) | Yes    | No        | No  |

| [Claude 3.5 Haiku](model-card-anthropic-claude-3-5-haiku.md "model-card-anthropic-claude-3-5-haiku.md") | Region                   | In-Region                | Geo | Global |
| ------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                               | No                       | Legacy (EOL: 2026-06-19) | No  |
| `us-east-2` (Ohio)                                                                                      | No                       | Legacy (EOL: 2026-06-19) | No  |
| `us-west-2` (Oregon)                                                                                    | Legacy (EOL: 2026-06-19) | Legacy (EOL: 2026-06-19) | No  |

| Claude 3.5 Sonnet            | Region | In-Region | Geo | Global |
| ---------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)    | Yes    | Yes       | No  |
| `us-east-2` (Ohio)           | No     | Yes       | No  |
| `us-west-2` (Oregon)         | Yes    | Yes       | No  |
| `us-gov-east-1` (GovCloud)   | No     | Yes       | No  |
| `us-gov-west-1` (GovCloud)   | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)   | Yes    | Yes       | No  |
| `eu-central-2` (Zurich)      | Yes    | No        | No  |
| `eu-west-1` (Ireland)        | No     | Yes       | No  |
| `eu-west-3` (Paris)          | No     | Yes       | No  |
| `ap-northeast-1` (Tokyo)     | Yes    | No        | No  |
| `ap-northeast-2` (Seoul)     | Yes    | No        | No  |
| `ap-southeast-1` (Singapore) | Yes    | No        | No  |

## Cohere

| [Embed v4](model-card-cohere-embed-v4.md "model-card-cohere-embed-v4.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                 | Yes    | Yes       | Yes |
| `us-east-2` (Ohio)                                                        | No     | Yes       | Yes |
| `us-west-1` (N. California)                                               | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                      | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                   | No     | No        | Yes |
| `eu-central-1` (Frankfurt)                                                | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                   | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                  | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                      | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                      | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                     | Yes    | Yes       | Yes |
| `eu-west-2` (London)                                                      | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                       | No     | Yes       | Yes |
| `ap-northeast-1` (Tokyo)                                                  | Yes    | No        | Yes |
| `ap-northeast-2` (Seoul)                                                  | No     | No        | Yes |
| `ap-northeast-3` (Osaka)                                                  | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                     | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                  | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                              | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                 | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)                                                | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                              | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                   | No     | No        | Yes |

| [Embed English](model-card-cohere-embed-english.md "model-card-cohere-embed-english.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                     | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                  | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                               | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                    | Yes    | No        | No  |
| `eu-west-2` (London)                                                                     | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                 | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                    | Yes    | No        | No  |
| `ap-southeast-1` (Singapore)                                                             | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                  | Yes    | No        | No  |

| [Embed Multilingual](model-card-cohere-embed-multilingual.md "model-card-cohere-embed-multilingual.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                               | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                    | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                 | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                              | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                   | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                    | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                                     | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                   | Yes    | No        | No  |
| `ap-southeast-1` (Singapore)                                                                            | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                               | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                 | Yes    | No        | No  |

| [Rerank 3.5](model-card-cohere-rerank-3-5.md "model-card-cohere-rerank-3-5.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                       | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                            | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                         | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                        | Yes    | No        | No  |

| [Command R](model-card-cohere-command-r.md "model-card-cohere-command-r.md") | Region                   | In-Region | Geo | Global |
| ---------------------------------------------------------------------------- | ------------------------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                    | Legacy (EOL: 2026-08-19) | No        | No  |
| `us-west-2` (Oregon)                                                         | Legacy (EOL: 2026-08-19) | No        | No  |

| [Command R+](model-card-cohere-command-r-plus.md "model-card-cohere-command-r-plus.md") | Region                   | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------- | ------------------------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                               | Legacy (EOL: 2026-08-19) | No        | No  |
| `us-west-2` (Oregon)                                                                    | Legacy (EOL: 2026-08-19) | No        | No  |

## DeepSeek

| [DeepSeek V3.2](model-card-deepseek-deepseek-v3-2.md "model-card-deepseek-deepseek-v3-2.md") | Region | In-Region | Geo | Global |
| -------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                    | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                           | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                         | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                     | Yes    | No        | No  |
| `eu-west-2` (London)                                                                         | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                     | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                        | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                    | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                   | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                      | Yes    | No        | No  |

| [DeepSeek-V3.1](model-card-deepseek-deepseek-v3-1.md "model-card-deepseek-deepseek-v3-1.md") | Region | In-Region | Geo | Global |
| -------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)                                                                           | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                         | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                     | Yes    | No        | No  |
| `eu-west-2` (London)                                                                         | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                     | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                        | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                    | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                   | Yes    | No        | No  |

| [DeepSeek-R1](model-card-deepseek-deepseek-r1.md "model-card-deepseek-deepseek-r1.md") | Region | In-Region | Geo | Global |
| -------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                              | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                     | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                   | No     | Yes       | No  |

## Google

| [Gemma 3 27B PT](model-card-google-gemma-3-27b-pt.md "model-card-google-gemma-3-27b-pt.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                   | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                          | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                        | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                        | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                       | Yes    | No        | No  |
| `eu-west-2` (London)                                                                        | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                    | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                       | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                   | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                     | Yes    | No        | No  |

| [Gemma 3 12B IT](model-card-google-gemma-3-12b-it.md "model-card-google-gemma-3-12b-it.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                   | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                          | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                        | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                        | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                       | Yes    | No        | No  |
| `eu-west-2` (London)                                                                        | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                    | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                       | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                   | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                     | Yes    | No        | No  |

| [Gemma 3 4B IT](model-card-google-gemma-3-4b-it.md "model-card-google-gemma-3-4b-it.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                       | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                     | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                     | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                    | Yes    | No        | No  |
| `eu-west-2` (London)                                                                     | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                 | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                    | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                  | Yes    | No        | No  |

## Luma

| Ray V2:0             | Region | In-Region | Geo | Global |
| -------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon) | Yes    | No        | No  |

## Meta

| [Llama 4 Maverick 17B Instruct](model-card-meta-llama-4-maverick-17b-instruct.md "model-card-meta-llama-4-maverick-17b-instruct.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                            | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                   | No     | Yes       | No  |
| `us-west-1` (N. California)                                                                                                          | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                 | No     | Yes       | No  |

| [Llama 4 Scout 17B Instruct](model-card-meta-llama-4-scout-17b-instruct.md "model-card-meta-llama-4-scout-17b-instruct.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                   | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                          | No     | Yes       | No  |
| `us-west-1` (N. California)                                                                                                 | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                        | No     | Yes       | No  |

| [Llama 3 70B Instruct](model-card-meta-llama-3-70b-instruct.md "model-card-meta-llama-3-70b-instruct.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                 | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                      | Yes    | No        | No  |
| `us-gov-west-1` (GovCloud)                                                                                | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                   | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                      | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                     | Yes    | No        | No  |

| [Llama 3 8B Instruct](model-card-meta-llama-3-8b-instruct.md "model-card-meta-llama-3-8b-instruct.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                              | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                   | Yes    | No        | No  |
| `us-gov-west-1` (GovCloud)                                                                             | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                  | Yes    | No        | No  |

| [Llama 3.3 70B Instruct](model-card-meta-llama-3-3-70b-instruct.md "model-card-meta-llama-3-3-70b-instruct.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                       | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                              | Yes    | Yes       | No  |
| `us-west-2` (Oregon)                                                                                            | No     | Yes       | No  |

| [Llama 3.2 90B Instruct](model-card-meta-llama-3-2-90b-instruct.md "model-card-meta-llama-3-2-90b-instruct.md") | Region | In-Region                | Geo | Global |
| --------------------------------------------------------------------------------------------------------------- | ------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                       | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-east-2` (Ohio)                                                                                              | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-west-2` (Oregon)                                                                                            | No     | Legacy (EOL: 2026-07-07) | No  |

| [Llama 3.2 11B Instruct](model-card-meta-llama-3-2-11b-instruct.md "model-card-meta-llama-3-2-11b-instruct.md") | Region | In-Region                | Geo | Global |
| --------------------------------------------------------------------------------------------------------------- | ------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                       | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-east-2` (Ohio)                                                                                              | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-west-2` (Oregon)                                                                                            | No     | Legacy (EOL: 2026-07-07) | No  |

| [Llama 3.2 3B Instruct](model-card-meta-llama-3-2-3b-instruct.md "model-card-meta-llama-3-2-3b-instruct.md") | Region | In-Region                | Geo | Global |
| ------------------------------------------------------------------------------------------------------------ | ------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                    | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-east-2` (Ohio)                                                                                           | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-west-2` (Oregon)                                                                                         | No     | Legacy (EOL: 2026-07-07) | No  |
| `eu-central-1` (Frankfurt)                                                                                   | No     | Legacy (EOL: 2026-07-07) | No  |
| `eu-west-1` (Ireland)                                                                                        | No     | Legacy (EOL: 2026-07-07) | No  |
| `eu-west-3` (Paris)                                                                                          | No     | Legacy (EOL: 2026-07-07) | No  |

| [Llama 3.2 1B Instruct](model-card-meta-llama-3-2-1b-instruct.md "model-card-meta-llama-3-2-1b-instruct.md") | Region | In-Region                | Geo | Global |
| ------------------------------------------------------------------------------------------------------------ | ------ | ------------------------ | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                    | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-east-2` (Ohio)                                                                                           | No     | Legacy (EOL: 2026-07-07) | No  |
| `us-west-2` (Oregon)                                                                                         | No     | Legacy (EOL: 2026-07-07) | No  |
| `eu-central-1` (Frankfurt)                                                                                   | No     | Legacy (EOL: 2026-07-07) | No  |
| `eu-west-1` (Ireland)                                                                                        | No     | Legacy (EOL: 2026-07-07) | No  |
| `eu-west-3` (Paris)                                                                                          | No     | Legacy (EOL: 2026-07-07) | No  |

| [Llama 3.1 405B Instruct](model-card-meta-llama-3-1-405b-instruct.md "model-card-meta-llama-3-1-405b-instruct.md") | Region                   | In-Region                | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------ | ------------------------ | --- | ------ |
| `us-east-2` (Ohio)                                                                                                 | No                       | Legacy (EOL: 2026-07-07) | No  |
| `us-west-2` (Oregon)                                                                                               | Legacy (EOL: 2026-07-07) | No                       | No  |

| [Llama 3.1 70B Instruct](model-card-meta-llama-3-1-70b-instruct.md "model-card-meta-llama-3-1-70b-instruct.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                       | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                              | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                            | Yes    | Yes       | No  |

| [Llama 3.1 8B Instruct](model-card-meta-llama-3-1-8b-instruct.md "model-card-meta-llama-3-1-8b-instruct.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                    | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                           | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                         | Yes    | Yes       | No  |

## MiniMax

| [MiniMax M2](model-card-minimax-minimax-m2.md "model-card-minimax-minimax-m2.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                         | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                              | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                              | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                             | Yes    | No        | No  |
| `eu-west-2` (London)                                                              | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                          | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                             | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                         | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                           | Yes    | No        | No  |

| [MiniMax M2.1](model-card-minimax-minimax-m2-1.md "model-card-minimax-minimax-m2-1.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                               | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                      | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                              | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                    | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                   | Yes    | No        | No  |
| `eu-west-2` (London)                                                                    | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                   | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                               | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                              | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                 | Yes    | No        | No  |

| [MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                               | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                    | Yes    | No        | No  |

| [MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                               | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                      | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                    | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                              | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                    | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                   | Yes    | No        | No  |
| `eu-west-2` (London)                                                                    | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                   | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                               | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                              | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                 | Yes    | No        | No  |

## Mistral AI

| [Magistral Small 2509](model-card-mistral-ai-magistral-small-2509.md "model-card-mistral-ai-magistral-small-2509.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                             | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                    | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                  | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                  | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                 | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                  | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                              | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                 | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                             | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                               | Yes    | No        | No  |

| [Pixtral Large](model-card-mistral-ai-pixtral-large.md "model-card-mistral-ai-pixtral-large.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                        | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                               | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                             | No     | Yes       | No  |
| `eu-central-1` (Frankfurt)                                                                       | No     | Yes       | No  |
| `eu-north-1` (Stockholm)                                                                         | No     | Yes       | No  |
| `eu-west-1` (Ireland)                                                                            | No     | Yes       | No  |
| `eu-west-3` (Paris)                                                                              | No     | Yes       | No  |

| Mistral Large 2407   | Region | In-Region | Geo | Global |
| -------------------- | ------ | --------- | --- | ------ |
| `us-west-2` (Oregon) | Yes    | No        | No  |

| [Mistral Small](model-card-mistral-ai-mistral-small.md "model-card-mistral-ai-mistral-small.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                        | Yes    | No        | No  |

| [Mistral Large](model-card-mistral-ai-mistral-large.md "model-card-mistral-ai-mistral-large.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                        | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                             | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                          | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                            | Yes    | No        | No  |
| `eu-west-2` (London)                                                                             | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                              | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                            | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                        | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                          | Yes    | No        | No  |

| [Voxtral Small 24B 2507](model-card-mistral-ai-voxtral-small-24b-2507.md "model-card-mistral-ai-voxtral-small-24b-2507.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                   | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                          | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                        | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                        | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                       | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                        | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                    | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                       | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                   | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                     | Yes    | No        | No  |

| [Mixtral 8x7B Instruct](model-card-mistral-ai-mixtral-8x7b-instruct.md "model-card-mistral-ai-mixtral-8x7b-instruct.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                     | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                                  | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                    | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                     | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                                                      | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                    | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                  | Yes    | No        | No  |

| [Mistral 7B Instruct](model-card-mistral-ai-mistral-7b-instruct.md "model-card-mistral-ai-mistral-7b-instruct.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                          | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                               | Yes    | No        | No  |
| `ca-central-1` (Canada)                                                                                            | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                              | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                               | Yes    | No        | No  |
| `eu-west-3` (Paris)                                                                                                | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                              | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                          | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                            | Yes    | No        | No  |

| [Voxtral Mini 3B 2507](model-card-mistral-ai-voxtral-mini-3b-2507.md "model-card-mistral-ai-voxtral-mini-3b-2507.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                             | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                    | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                  | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                  | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                 | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                  | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                              | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                 | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                             | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                               | Yes    | No        | No  |

| [Mistral Large 3](model-card-mistral-ai-mistral-large-3.md "model-card-mistral-ai-mistral-large-3.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                              | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                     | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                   | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                               | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                  | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                              | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                | Yes    | No        | No  |

| [Ministral 14B 3.0](model-card-mistral-ai-ministral-14b-3-0.md "model-card-mistral-ai-ministral-14b-3-0.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                    | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                           | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                         | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                         | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                        | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                         | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                     | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                        | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                    | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                      | Yes    | No        | No  |

| [Ministral 3 8B](model-card-mistral-ai-ministral-3-8b.md "model-card-mistral-ai-ministral-3-8b.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                           | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                  | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                               | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                            | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                               | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                           | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                             | Yes    | No        | No  |

| [Ministral 3B](model-card-mistral-ai-ministral-3b.md "model-card-mistral-ai-ministral-3b.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                     | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                            | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                          | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                          | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                         | Yes    | No        | No  |
| `eu-west-2` (London)                                                                          | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                      | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                         | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                     | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                       | Yes    | No        | No  |

| [Devstral 2 123B](model-card-mistral-ai-devstral-2-123b.md "model-card-mistral-ai-devstral-2-123b.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                              | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                     | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                   | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                             | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                               | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                   | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                  | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                   | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                               | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                  | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                              | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                             | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                | Yes    | No        | No  |

## Moonshot AI

| [Kimi K2.5](model-card-moonshot-ai-kimi-k2-5.md "model-card-moonshot-ai-kimi-k2-5.md") | Region | In-Region | Geo | Global |
| -------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                              | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                     | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                   | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                               | Yes    | No        | No  |
| `eu-west-2` (London)                                                                   | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                               | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                  | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                              | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                             | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                | Yes    | No        | No  |

## NVIDIA

| [NVIDIA Nemotron Nano 12B v2 VL BF16](model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md "model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                                  | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                                                         | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                                                       | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                                                       | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                                                      | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                                                       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                                                   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                                                      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                                                  | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                                                    | Yes    | No        | No  |

| [NVIDIA Nemotron Nano 9B v2](model-card-nvidia-nvidia-nemotron-nano-9b-v2.md "model-card-nvidia-nvidia-nemotron-nano-9b-v2.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                       | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                              | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                            | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                            | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                           | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                            | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                        | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                           | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                       | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                         | Yes    | No        | No  |

| [Nemotron Nano 3 30B](model-card-nvidia-nemotron-nano-3-30b.md "model-card-nvidia-nemotron-nano-3-30b.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                  | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                         | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                       | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                       | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                      | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                  | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                    | Yes    | No        | No  |

| [NVIDIA Nemotron 3 Super 120B](model-card-nvidia-nemotron-super-3-120b.md "model-card-nvidia-nemotron-super-3-120b.md") | Region | In-Region | Geo | Global |
| ----------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                               | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                      | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                    | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                    | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                   | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                    | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                   | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                               | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                 | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                                              | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                                                | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                                              | Yes    | No        | No  |

## OpenAI

| [GPT OSS Safeguard 120B](model-card-openai-gpt-oss-safeguard-120b.md "model-card-openai-gpt-oss-safeguard-120b.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                           | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                  | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                               | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                            | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                               | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                           | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                             | Yes    | No        | No  |

| [gpt-oss-120b](model-card-openai-gpt-oss-120b.md "model-card-openai-gpt-oss-120b.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                             | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                    | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                  | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                            | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                              | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                  | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                 | Yes    | No        | No  |
| `eu-west-2` (London)                                                                  | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                              | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                 | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                             | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                            | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                               | Yes    | No        | No  |

| [GPT OSS Safeguard 20B](model-card-openai-gpt-oss-safeguard-20b.md "model-card-openai-gpt-oss-safeguard-20b.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                        | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                               | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                             | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                             | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                            | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                             | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                         | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                            | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                        | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                          | Yes    | No        | No  |

| [gpt-oss-20b](model-card-openai-gpt-oss-20b.md "model-card-openai-gpt-oss-20b.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                          | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                 | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                               | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                         | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                           | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                               | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                              | Yes    | No        | No  |
| `eu-west-2` (London)                                                               | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                           | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                              | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                          | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                         | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                            | Yes    | No        | No  |

## Qwen

| [Qwen3 Coder Next](model-card-qwen-qwen3-coder-next.md "model-card-qwen-qwen3-coder-next.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                     | Yes    | No        | No  |
| `eu-west-2` (London)                                                                          | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                     | Yes    | No        | No  |

| [Qwen3 Coder 480B A35B Instruct](model-card-qwen-qwen3-coder-480b-a35b-instruct.md "model-card-qwen-qwen3-coder-480b-a35b-instruct.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)                                                                                                                      | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                                    | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                                                                | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                                    | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                                | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                                   | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                               | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                                                              | Yes    | No        | No  |

| [Qwen3 235B A22B 2507](model-card-qwen-qwen3-235b-a22b-2507.md "model-card-qwen-qwen3-235b-a22b-2507.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-2` (Ohio)                                                                                        | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                      | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                                | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                                  | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                      | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                      | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                  | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                     | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                 | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                                | Yes    | No        | No  |

| [Qwen3 VL 235B A22B](model-card-qwen-qwen3-vl-235b-a22b.md "model-card-qwen-qwen3-vl-235b-a22b.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                           | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                  | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                               | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                            | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                               | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                           | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                             | Yes    | No        | No  |

| [Qwen3 Next 80B A3B](model-card-qwen-qwen3-next-80b-a3b.md "model-card-qwen-qwen3-next-80b-a3b.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                           | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                  | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                               | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                            | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                               | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                           | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                             | Yes    | No        | No  |

| [Qwen3 32B](model-card-qwen-qwen3-32b.md "model-card-qwen-qwen3-32b.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                       | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                     | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                               | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                 | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                     | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                    | Yes    | No        | No  |
| `eu-west-2` (London)                                                     | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                 | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                    | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                               | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                  | Yes    | No        | No  |

| [Qwen3-Coder-30B-A3B-Instruct](model-card-qwen-qwen3-coder-30b-a3b-instruct.md "model-card-qwen-qwen3-coder-30b-a3b-instruct.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                         | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                                                | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                                              | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                                                                        | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                                                                          | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                                                                              | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                                                                             | Yes    | No        | No  |
| `eu-west-2` (London)                                                                                                              | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                                                                          | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                                                                             | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                                                                         | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                                                                        | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                                                                           | Yes    | No        | No  |

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

| [Stable Image Control Structure](model-card-stability-ai-stable-image-control-structure.md "model-card-stability-ai-stable-image-control-structure.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                               | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                                      | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                                    | No     | Yes       | No  |

| [Stable Image Conservative Upscale](model-card-stability-ai-stable-image-conservative-upscale.md "model-card-stability-ai-stable-image-conservative-upscale.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                                        | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                                               | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                                             | No     | Yes       | No  |

| [Stable Image Fast Upscale](model-card-stability-ai-stable-image-fast-upscale.md "model-card-stability-ai-stable-image-fast-upscale.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                       | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                     | No     | Yes       | No  |

| [Stable Image Control Sketch](model-card-stability-ai-stable-image-control-sketch.md "model-card-stability-ai-stable-image-control-sketch.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                      | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                             | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                           | No     | Yes       | No  |

| [Stable Image Search and Recolor](model-card-stability-ai-stable-image-search-and-recolor.md "model-card-stability-ai-stable-image-search-and-recolor.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                                  | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                                         | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                                       | No     | Yes       | No  |

| [Stable Image Creative Upscale](model-card-stability-ai-stable-image-creative-upscale.md "model-card-stability-ai-stable-image-creative-upscale.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                            | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                                   | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                                 | No     | Yes       | No  |

| [Stable Image Erase Object](model-card-stability-ai-stable-image-erase-object.md "model-card-stability-ai-stable-image-erase-object.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                       | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                     | No     | Yes       | No  |

| [Stable Image Inpaint](model-card-stability-ai-stable-image-inpaint.md "model-card-stability-ai-stable-image-inpaint.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                 | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                        | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                      | No     | Yes       | No  |

| [Stable Image Outpaint](model-card-stability-ai-stable-image-outpaint.md "model-card-stability-ai-stable-image-outpaint.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                    | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                           | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                         | No     | Yes       | No  |

| [Stable Image Search and Replace](model-card-stability-ai-stable-image-search-and-replace.md "model-card-stability-ai-stable-image-search-and-replace.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                                  | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                                         | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                                       | No     | Yes       | No  |

| [Stable Image Style Transfer](model-card-stability-ai-stable-image-style-transfer.md "model-card-stability-ai-stable-image-style-transfer.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                      | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                             | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                           | No     | Yes       | No  |

| [Stable Image Style Guide](model-card-stability-ai-stable-image-style-guide.md "model-card-stability-ai-stable-image-style-guide.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                             | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                    | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                  | No     | Yes       | No  |

| [Stable Image Remove Background](model-card-stability-ai-stable-image-remove-background.md "model-card-stability-ai-stable-image-remove-background.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                                                               | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                                                                                                      | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                                                                                                    | No     | Yes       | No  |

## TwelveLabs

| [Marengo Embed 3.0](model-card-twelvelabs-marengo-embed-3-0.md "model-card-twelvelabs-marengo-embed-3-0.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------------------------------------ | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                    | Yes    | Yes       | No  |
| `eu-west-1` (Ireland)                                                                                        | No     | Yes       | No  |
| `ap-northeast-2` (Seoul)                                                                                     | Yes    | No        | No  |

| [Marengo Embed v2.7](model-card-twelvelabs-marengo-embed-v2-7.md "model-card-twelvelabs-marengo-embed-v2-7.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                                       | No     | Yes       | No  |
| `eu-west-1` (Ireland)                                                                                           | No     | Yes       | No  |

| [Pegasus v1.2](model-card-twelvelabs-pegasus-v1-2.md "model-card-twelvelabs-pegasus-v1-2.md") | Region | In-Region | Geo | Global |
| --------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                     | Yes    | Yes       | Yes |
| `us-east-2` (Ohio)                                                                            | No     | Yes       | Yes |
| `us-west-1` (N. California)                                                                   | No     | Yes       | Yes |
| `us-west-2` (Oregon)                                                                          | No     | Yes       | Yes |
| `ca-central-1` (Canada)                                                                       | No     | No        | Yes |
| `ca-west-1` (Calgary)                                                                         | No     | No        | Yes |
| `eu-central-1` (Frankfurt)                                                                    | No     | Yes       | Yes |
| `eu-central-2` (Zurich)                                                                       | No     | Yes       | Yes |
| `eu-north-1` (Stockholm)                                                                      | No     | Yes       | Yes |
| `eu-south-1` (Milan)                                                                          | No     | Yes       | Yes |
| `eu-south-2` (Spain)                                                                          | No     | Yes       | Yes |
| `eu-west-1` (Ireland)                                                                         | No     | Yes       | Yes |
| `eu-west-2` (London)                                                                          | No     | Yes       | Yes |
| `eu-west-3` (Paris)                                                                           | No     | Yes       | Yes |
| `ap-east-2` (Taipei)                                                                          | No     | No        | Yes |
| `ap-northeast-1` (Tokyo)                                                                      | No     | No        | Yes |
| `ap-northeast-2` (Seoul)                                                                      | Yes    | No        | Yes |
| `ap-northeast-3` (Osaka)                                                                      | No     | No        | Yes |
| `ap-south-1` (Mumbai)                                                                         | No     | No        | Yes |
| `ap-south-2` (Hyderabad)                                                                      | No     | No        | Yes |
| `ap-southeast-1` (Singapore)                                                                  | No     | No        | Yes |
| `ap-southeast-2` (Sydney)                                                                     | No     | No        | Yes |
| `ap-southeast-3` (Jakarta)                                                                    | No     | No        | Yes |
| `ap-southeast-4` (Melbourne)                                                                  | No     | No        | Yes |
| `ap-southeast-5` (Malaysia)                                                                   | No     | No        | Yes |
| `ap-southeast-7` (Thailand)                                                                   | No     | No        | Yes |
| `il-central-1` (Tel Aviv)                                                                     | No     | No        | Yes |
| `me-central-1` (UAE)                                                                          | No     | No        | Yes |
| `me-south-1` (Bahrain)                                                                        | No     | No        | Yes |
| `af-south-1` (Cape Town)                                                                      | No     | No        | Yes |
| `sa-east-1` (São Paulo)                                                                       | No     | No        | Yes |
| `mx-central-1` (Mexico)                                                                       | No     | No        | Yes |

## Writer

| [Palmyra Vision 7B](model-card-writer-palmyra-vision-7b.md "model-card-writer-palmyra-vision-7b.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                                            | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                                   | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                                                 | Yes    | No        | No  |

| [Palmyra X5](model-card-writer-palmyra-x5.md "model-card-writer-palmyra-x5.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                       | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                              | No     | Yes       | No  |
| `us-west-1` (N. California)                                                     | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                            | No     | Yes       | No  |

| [Palmyra X4](model-card-writer-palmyra-x4.md "model-card-writer-palmyra-x4.md") | Region | In-Region | Geo | Global |
| ------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                       | No     | Yes       | No  |
| `us-east-2` (Ohio)                                                              | No     | Yes       | No  |
| `us-west-1` (N. California)                                                     | No     | Yes       | No  |
| `us-west-2` (Oregon)                                                            | No     | Yes       | No  |

## Z.AI

| [GLM 4.7 Flash](model-card-zai-glm-4-7-flash.md "model-card-zai-glm-4-7-flash.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                                          | Yes    | No        | No  |
| `us-east-2` (Ohio)                                                                 | Yes    | No        | No  |
| `us-west-2` (Oregon)                                                               | Yes    | No        | No  |
| `eu-central-1` (Frankfurt)                                                         | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                                           | Yes    | No        | No  |
| `eu-south-1` (Milan)                                                               | Yes    | No        | No  |
| `eu-west-1` (Ireland)                                                              | Yes    | No        | No  |
| `eu-west-2` (London)                                                               | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                                           | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                                              | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                                          | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                                         | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                                            | Yes    | No        | No  |

| [GLM 4.7](model-card-zai-glm-4-7.md "model-card-zai-glm-4-7.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                        | Yes    | No        | No  |
| `us-east-2` (Ohio)                                               | Yes    | No        | No  |
| `us-west-2` (Oregon)                                             | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                         | Yes    | No        | No  |
| `eu-west-2` (London)                                             | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                         | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                            | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                        | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                       | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                          | Yes    | No        | No  |

| [GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                  | Yes    | No        | No  |
| `us-west-2` (Oregon)                                       | Yes    | No        | No  |

| [GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md") | Region | In-Region | Geo | Global |
| ---------------------------------------------------------- | ------ | --------- | --- | ------ |
| `us-east-1` (N. Virginia)                                  | Yes    | No        | No  |
| `us-east-2` (Ohio)                                         | Yes    | No        | No  |
| `us-west-2` (Oregon)                                       | Yes    | No        | No  |
| `eu-north-1` (Stockholm)                                   | Yes    | No        | No  |
| `eu-west-2` (London)                                       | Yes    | No        | No  |
| `ap-northeast-1` (Tokyo)                                   | Yes    | No        | No  |
| `ap-south-1` (Mumbai)                                      | Yes    | No        | No  |
| `ap-southeast-2` (Sydney)                                  | Yes    | No        | No  |
| `ap-southeast-3` (Jakarta)                                 | Yes    | No        | No  |
| `sa-east-1` (São Paulo)                                    | Yes    | No        | No  |
