# Regional availability by models

Amazon Bedrock gives you three options so you can match the routing behavior of your inference calls to the scale, compliance, and cost requirements of your workload.

###### Process to enabling Bedrock models in GovCloud

Accessing Bedrock foundation models in AWS GovCloud (US) requires initiating the access request through the standard AWS account linked to your GovCloud account. You must first agree to the model's End User License Agreement (EULA) in a standard region (`us-east-1` or `us-west-2`), then enable the model in your GovCloud account. You can do this in two ways:

- **Console:** Sign in to your linked standard AWS account, open the Amazon Bedrock Chat/Text playground, choose the model, and run a prompt to establish the EULA.
- **AWS CLI:** Run `aws bedrock list-foundation-models` to get the model ID, then `aws bedrock list-foundation-model-agreement-offers --model-id <model-id>` to get the offer token, and finally `aws bedrock create-foundation-model-agreement --model-id <model-id> --offer-token <offerToken>`.
  After completing either method, go to your GovCloud account and enable the model via the Model Access page. It may take a few minutes for entitlements to propagate. For the full walkthrough, see [Process to enabling Bedrock models in GovCloud](https://repost.aws/articles/ARUT8Sy76NTUmRN7kuiU0UXQ "https://repost.aws/articles/ARUT8Sy76NTUmRN7kuiU0UXQ").

- **In-Region:** Your requests never leave the AWS Region you specify. Use this when regulations require strict single-Region data processing.
- **Geographic (Geo):** Bedrock routes your request to a Region within a defined geography (US, EU, Japan, or Australia), keeping data within that geography. Use this when you have data residency requirements tied to a geography rather than a single Region.
- **Global:** Bedrock routes your request to a supported commercial Region worldwide. For some models, global cross-Region inference is priced lower per token than geographic cross-Region inference. Use this when you have no data residency constraints.

## Inference options at a glance

|                     | **In-Region**                                                             | **Geographic (Geo) Cross-Region**                                                                                         | **Global Cross-Region**                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **How it works**    | Request is processed entirely within the single AWS Region you specify    | Bedrock routes the request to a Region within a defined geography (US, EU, APAC, JP, AU)                                  | Bedrock routes the request to any supported commercial Region worldwide                                                                                    |
| **Data residency**  | Strictly within one Region                                                | Within geographic boundaries (e.g., all EU Regions); prompts and outputs may move within the geography but not outside it | No geographic restrictions; data may be processed in any commercial Region                                                                                 |
| **Request routing** | Processed in the Region you specify; subject to per-Region service quotas | Routed to a Region within the geography                                                                                   | Routed to a supported commercial Region worldwide                                                                                                          |
| **Pricing**         | Standard on-demand pricing for that Region                                | Priced at source Region rates; no surcharge for cross-Region routing                                                      | Priced at source Region rates; no surcharge for cross-Region routing. For some models, the per-token price is lower than geographic cross-Region inference |
| **modelId format**  | Direct model ID: `anthropic.claude-3-5-sonnet-20241022-v2:0`              | Geography prefix + model ID: `us.anthropic.claude-3-5-sonnet-20241022-v2:0`                                               | Global prefix + model ID: `global.anthropic.claude-3-5-sonnet-20241022-v2:0`                                                                               |
| **Best for**        | Strict single-Region compliance; Provisioned Throughput workloads         | Data residency regulations scoped to a geography (e.g., GDPR in EU, data sovereignty requirements)                        | Cost efficiency with no data residency constraints                                                                                                         |

Now, let us look at Regional availability across all the models supported by Amazon Bedrock.

## AI21 Labs

[Jamba 1.5 Large](model-card-ai21-labs-jamba-1-5-large.md "model-card-ai21-labs-jamba-1-5-large.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-11-26) | not-supported | not-supported |

[Jamba 1.5 Mini](model-card-ai21-labs-jamba-1-5-mini.md "model-card-ai21-labs-jamba-1-5-mini.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-11-26) | not-supported | not-supported |

## Amazon

[Nova 2 Sonic](model-card-amazon-nova-2-sonic.md "model-card-amazon-nova-2-sonic.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |

[Nova 2 Lite](model-card-amazon-nova-2-lite.md "model-card-amazon-nova-2-lite.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | not-supported | supported | supported |
| `eu-west-2` (London) | not-supported | not-supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |

[Amazon Nova Multimodal Embeddings](model-card-amazon-amazon-nova-multimodal-embeddings.md "model-card-amazon-amazon-nova-multimodal-embeddings.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |

[Titan Image Generator G1 v2](model-card-amazon-titan-image-generator-g1-v2.md "model-card-amazon-titan-image-generator-g1-v2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[Titan Text Embeddings V2](model-card-amazon-titan-text-embeddings-v2.md "model-card-amazon-titan-text-embeddings-v2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `us-gov-east-1` (GovCloud) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-central-2` (Zurich) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-south-2` (Spain) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-northeast-2` (Seoul) | supported | not-supported | not-supported |
| `ap-northeast-3` (Osaka) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-south-2` (Hyderabad) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Titan Multimodal Embeddings G1](model-card-amazon-titan-multimodal-embeddings-g1.md "model-card-amazon-titan-multimodal-embeddings-g1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Titan Embeddings G1 - Text](model-card-amazon-titan-embeddings-g1---text.md "model-card-amazon-titan-embeddings-g1---text.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |

[Titan Embeddings G1 - Text v2](model-card-amazon-titan-text-embeddings-v2-2.md "model-card-amazon-titan-text-embeddings-v2-2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md") — `amazon.nova-reel-v1:1`| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |

Rerank| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |

[Nova Sonic](model-card-amazon-nova-sonic.md "model-card-amazon-nova-sonic.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-14) | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-09-14) | not-supported | not-supported |

[Nova Pro](model-card-amazon-nova-pro.md "model-card-amazon-nova-pro.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-1` (N. California) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | not-supported |
| `eu-north-1` (Stockholm) | not-supported | supported | not-supported |
| `eu-south-1` (Milan) | not-supported | supported | not-supported |
| `eu-south-2` (Spain) | not-supported | supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | not-supported | supported | not-supported |
| `ap-northeast-1` (Tokyo) | not-supported | supported | not-supported |
| `ap-northeast-2` (Seoul) | not-supported | supported | not-supported |
| `ap-south-1` (Mumbai) | not-supported | supported | not-supported |
| `ap-southeast-1` (Singapore) | not-supported | supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `il-central-1` (Tel Aviv) | not-supported | supported | not-supported |
| `me-central-1` (UAE) | supported | not-supported | not-supported |

[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md") — `amazon.nova-reel-v1:0`| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |
| `eu-west-1` (Ireland) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |

[Nova Lite](model-card-amazon-nova-lite.md "model-card-amazon-nova-lite.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | not-supported |
| `us-east-2` (Ohio) | supported | supported | not-supported |
| `us-west-1` (N. California) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | supported | supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | not-supported | supported | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | not-supported |
| `eu-north-1` (Stockholm) | supported | supported | not-supported |
| `eu-south-1` (Milan) | not-supported | supported | not-supported |
| `eu-south-2` (Spain) | not-supported | supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | not-supported | supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | supported | not-supported |
| `ap-northeast-2` (Seoul) | not-supported | supported | not-supported |
| `ap-south-1` (Mumbai) | not-supported | supported | not-supported |
| `ap-southeast-1` (Singapore) | not-supported | supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `il-central-1` (Tel Aviv) | not-supported | supported | not-supported |
| `me-central-1` (UAE) | supported | not-supported | not-supported |

[Nova Canvas](model-card-amazon-nova-canvas.md "model-card-amazon-nova-canvas.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |
| `eu-west-1` (Ireland) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-09-30) | not-supported | not-supported |

[Nova Micro](model-card-amazon-nova-micro.md "model-card-amazon-nova-micro.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | not-supported |
| `eu-north-1` (Stockholm) | not-supported | supported | not-supported |
| `eu-south-1` (Milan) | not-supported | supported | not-supported |
| `eu-south-2` (Spain) | not-supported | supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | not-supported | supported | not-supported |
| `ap-northeast-1` (Tokyo) | not-supported | supported | not-supported |
| `ap-northeast-2` (Seoul) | not-supported | supported | not-supported |
| `ap-south-1` (Mumbai) | not-supported | supported | not-supported |
| `ap-southeast-1` (Singapore) | not-supported | supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | supported | not-supported |
| `il-central-1` (Tel Aviv) | not-supported | supported | not-supported |

[Nova Premier](model-card-amazon-nova-premier.md "model-card-amazon-nova-premier.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

## Anthropic

[Claude Opus 5](model-card-anthropic-claude-opus-5.md "model-card-anthropic-claude-opus-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-4` (Melbourne) | supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |
| `us-gov-west-1` (GovCloud West) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud East) | not-supported | supported | not-supported |

[Claude Sonnet 5](model-card-anthropic-claude-sonnet-5.md "model-card-anthropic-claude-sonnet-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |
| `us-gov-west-1` (GovCloud West) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud East) | not-supported | supported | not-supported |

[Claude Mythos 5](model-card-anthropic-claude-mythos-5.md "model-card-anthropic-claude-mythos-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |

[Claude Fable 5](model-card-anthropic-claude-fable-5.md "model-card-anthropic-claude-fable-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | not-supported | supported |
| `eu-central-2` (Zurich) | not-supported | not-supported | supported |
| `eu-north-1` (Stockholm) | not-supported | not-supported | supported |
| `eu-south-1` (Milan) | not-supported | not-supported | supported |
| `eu-south-2` (Spain) | not-supported | not-supported | supported |
| `eu-west-1` (Ireland) | not-supported | not-supported | supported |
| `eu-west-2` (London) | not-supported | not-supported | supported |
| `eu-west-3` (Paris) | not-supported | not-supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Mythos Preview](model-card-anthropic-claude-mythos-preview.md "model-card-anthropic-claude-mythos-preview.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `ap-southeast-4` (Melbourne) | supported | not-supported | not-supported |

[Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md "model-card-anthropic-claude-sonnet-4.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `us-west-1` (N. California) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `eu-central-1` (Frankfurt) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `eu-north-1` (Stockholm) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `eu-south-1` (Milan) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `eu-south-2` (Spain) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `eu-west-1` (Ireland) | not-supported | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `eu-west-3` (Paris) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `il-central-1` (Tel Aviv) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-east-2` (Taipei) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-northeast-1` (Tokyo) | not-supported | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `ap-northeast-2` (Seoul) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-northeast-3` (Osaka) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-south-1` (Mumbai) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-south-2` (Hyderabad) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-southeast-1` (Singapore) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-southeast-2` (Sydney) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-southeast-3` (Jakarta) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-southeast-4` (Melbourne) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-southeast-5` (Malaysia) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |
| `ap-southeast-7` (Thailand) | not-supported | Legacy (EOL: 2026-10-14) | not-supported |

Claude Opus 4| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md "model-card-anthropic-claude-sonnet-4-6.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | not-supported | supported | supported |
| `eu-west-2` (London) | supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Opus 4.8](model-card-anthropic-claude-opus-4-8.md "model-card-anthropic-claude-opus-4-8.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `us-gov-west-1` (GovCloud West) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud East) | not-supported | supported | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | supported | supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Opus 4.7](model-card-anthropic-claude-opus-4-7.md "model-card-anthropic-claude-opus-4-7.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md "model-card-anthropic-claude-opus-4-6.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | not-supported | supported | supported |
| `eu-west-2` (London) | supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md "model-card-anthropic-claude-opus-4-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | not-supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md "model-card-anthropic-claude-haiku-4-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | supported | supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md "model-card-anthropic-claude-sonnet-4-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |
| `us-gov-west-1` (GovCloud) | not-supported | supported | not-supported |
| `ca-central-1` (Canada) | not-supported | supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | not-supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

[Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md "model-card-anthropic-claude-opus-4-1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2027-01-08) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2027-01-08) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2027-01-08) | not-supported |

[Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md "model-card-anthropic-claude-3-haiku.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-10) | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-09-10) | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-09-10) | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-09-10) | supported | not-supported |
| `eu-central-2` (Zurich) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | Legacy (EOL: 2026-09-10) | supported | not-supported |
| `eu-west-2` (London) | Legacy (EOL: 2026-09-10) | not-supported | not-supported |
| `eu-west-3` (Paris) | Legacy (EOL: 2026-09-10) | supported | not-supported |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-09-10) | not-supported | not-supported |
| `ap-northeast-2` (Seoul) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-1` (Singapore) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | Legacy (EOL: 2026-09-10) | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

Claude 3 Sonnet| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-west-1` (Ireland) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-1` (Singapore) | not-supported | supported | not-supported |
| `ap-southeast-2` (Sydney) | Legacy (EOL: 2026-07-30) | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

Claude 3.7 Sonnet| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-north-1` (Stockholm) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-west-1` (Ireland) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `ap-south-1` (Mumbai) | not-supported | supported | not-supported |

Claude 3.5 Sonnet V2:0| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `ap-northeast-2` (Seoul) | not-supported | supported | not-supported |
| `ap-south-1` (Mumbai) | not-supported | supported | not-supported |
| `ap-southeast-1` (Singapore) | not-supported | supported | not-supported |
| `ap-southeast-2` (Sydney) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |

Claude 3.5 Sonnet| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-central-2` (Zurich) | Legacy (EOL: 2026-07-30) | not-supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `eu-west-3` (Paris) | not-supported | Legacy (EOL: 2026-07-30) | not-supported |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-07-30) | not-supported | not-supported |
| `ap-northeast-2` (Seoul) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | not-supported | supported | not-supported |
| `ap-southeast-1` (Singapore) | supported | not-supported | not-supported |

## Cohere

[Embed v4](model-card-cohere-embed-v4.md "model-card-cohere-embed-v4.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |

[Embed English](model-card-cohere-embed-english.md "model-card-cohere-embed-english.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-1` (Singapore) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Embed Multilingual](model-card-cohere-embed-multilingual.md "model-card-cohere-embed-multilingual.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-1` (Singapore) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Rerank 3.5](model-card-cohere-rerank-3-5.md "model-card-cohere-rerank-3-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |

[Command R](model-card-cohere-command-r.md "model-card-cohere-command-r.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-08-19) | not-supported | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-08-19) | not-supported | not-supported |

[Command R+](model-card-cohere-command-r-plus.md "model-card-cohere-command-r-plus.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-08-19) | not-supported | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-08-19) | not-supported | not-supported |

## DeepSeek

[DeepSeek V3.2](model-card-deepseek-deepseek-v3-2.md "model-card-deepseek-deepseek-v3-2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[DeepSeek-V3.1](model-card-deepseek-deepseek-v3-1.md "model-card-deepseek-deepseek-v3-1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |

[DeepSeek-R1](model-card-deepseek-deepseek-r1.md "model-card-deepseek-deepseek-r1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

## Google

[Gemma 4 31B](model-card-google-gemma-4-31b.md "model-card-google-gemma-4-31b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |

[Gemma 4 26B-A4B](model-card-google-gemma-4-26b-a4b.md "model-card-google-gemma-4-26b-a4b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |

[Gemma 4 E2B](model-card-google-gemma-4-e2b.md "model-card-google-gemma-4-e2b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |

[Gemma 3 27B PT](model-card-google-gemma-3-27b-pt.md "model-card-google-gemma-3-27b-pt.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Gemma 3 12B IT](model-card-google-gemma-3-12b-it.md "model-card-google-gemma-3-12b-it.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Gemma 3 4B IT](model-card-google-gemma-3-4b-it.md "model-card-google-gemma-3-4b-it.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

## Luma

Ray V2:0| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

## Meta

[Llama 4 Maverick 17B Instruct](model-card-meta-llama-4-maverick-17b-instruct.md "model-card-meta-llama-4-maverick-17b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-1` (N. California) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Llama 4 Scout 17B Instruct](model-card-meta-llama-4-scout-17b-instruct.md "model-card-meta-llama-4-scout-17b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-1` (N. California) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Llama 3 70B Instruct](model-card-meta-llama-3-70b-instruct.md "model-card-meta-llama-3-70b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |

[Llama 3 8B Instruct](model-card-meta-llama-3-8b-instruct.md "model-card-meta-llama-3-8b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |

[Llama 3.3 70B Instruct](model-card-meta-llama-3-3-70b-instruct.md "model-card-meta-llama-3-3-70b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Llama 3.2 90B Instruct](model-card-meta-llama-3-2-90b-instruct.md "model-card-meta-llama-3-2-90b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |

[Llama 3.2 11B Instruct](model-card-meta-llama-3-2-11b-instruct.md "model-card-meta-llama-3-2-11b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |

[Llama 3.2 3B Instruct](model-card-meta-llama-3-2-3b-instruct.md "model-card-meta-llama-3-2-3b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `eu-west-1` (Ireland) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `eu-west-3` (Paris) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |

[Llama 3.2 1B Instruct](model-card-meta-llama-3-2-1b-instruct.md "model-card-meta-llama-3-2-1b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-west-2` (Oregon) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `eu-west-1` (Ireland) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `eu-west-3` (Paris) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |

[Llama 3.1 405B Instruct](model-card-meta-llama-3-1-405b-instruct.md "model-card-meta-llama-3-1-405b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | not-supported | Legacy (EOL: 2026-07-07) | not-supported |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-07) | not-supported | not-supported |

[Llama 3.1 70B Instruct](model-card-meta-llama-3-1-70b-instruct.md "model-card-meta-llama-3-1-70b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | supported | supported | not-supported |

[Llama 3.1 8B Instruct](model-card-meta-llama-3-1-8b-instruct.md "model-card-meta-llama-3-1-8b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | supported | supported | not-supported |

## MiniMax

[MiniMax M2](model-card-minimax-minimax-m2.md "model-card-minimax-minimax-m2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[MiniMax M2.1](model-card-minimax-minimax-m2-1.md "model-card-minimax-minimax-m2-1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

## Mistral AI

[Magistral Small 2509](model-card-mistral-ai-magistral-small-2509.md "model-card-mistral-ai-magistral-small-2509.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Pixtral Large](model-card-mistral-ai-pixtral-large.md "model-card-mistral-ai-pixtral-large.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | not-supported |
| `eu-north-1` (Stockholm) | not-supported | supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | supported | not-supported |
| `eu-west-3` (Paris) | not-supported | supported | not-supported |

Mistral Large 2407| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[Mistral Small](model-card-mistral-ai-mistral-small.md "model-card-mistral-ai-mistral-small.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |

[Mistral Large](model-card-mistral-ai-mistral-large.md "model-card-mistral-ai-mistral-large.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Voxtral Small 24B 2507](model-card-mistral-ai-voxtral-small-24b-2507.md "model-card-mistral-ai-voxtral-small-24b-2507.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Mixtral 8x7B Instruct](model-card-mistral-ai-mixtral-8x7b-instruct.md "model-card-mistral-ai-mixtral-8x7b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Mistral 7B Instruct](model-card-mistral-ai-mistral-7b-instruct.md "model-card-mistral-ai-mistral-7b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ca-central-1` (Canada) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `eu-west-3` (Paris) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Voxtral Mini 3B 2507](model-card-mistral-ai-voxtral-mini-3b-2507.md "model-card-mistral-ai-voxtral-mini-3b-2507.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Mistral Large 3](model-card-mistral-ai-mistral-large-3.md "model-card-mistral-ai-mistral-large-3.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Ministral 14B 3.0](model-card-mistral-ai-ministral-14b-3-0.md "model-card-mistral-ai-ministral-14b-3-0.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Ministral 3 8B](model-card-mistral-ai-ministral-3-8b.md "model-card-mistral-ai-ministral-3-8b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Ministral 3B](model-card-mistral-ai-ministral-3b.md "model-card-mistral-ai-ministral-3b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Devstral 2 123B](model-card-mistral-ai-devstral-2-123b.md "model-card-mistral-ai-devstral-2-123b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

## Moonshot AI

[Kimi K2.5](model-card-moonshot-ai-kimi-k2-5.md "model-card-moonshot-ai-kimi-k2-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

## NVIDIA

[NVIDIA Nemotron Nano 12B v2 VL BF16](model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md "model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |

[NVIDIA Nemotron Nano 9B v2](model-card-nvidia-nvidia-nemotron-nano-9b-v2.md "model-card-nvidia-nvidia-nemotron-nano-9b-v2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |

[Nemotron Nano 3 30B](model-card-nvidia-nemotron-nano-3-30b.md "model-card-nvidia-nemotron-nano-3-30b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |

[NVIDIA Nemotron 3 Super 120B](model-card-nvidia-nemotron-super-3-120b.md "model-card-nvidia-nemotron-super-3-120b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |

## OpenAI

[GPT-5.6 Sol](model-card-openai-gpt-56-sol.md "model-card-openai-gpt-56-sol.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | not-supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | not-supported | supported |
| `eu-central-2` (Zurich) | not-supported | not-supported | supported |
| `eu-north-1` (Stockholm) | not-supported | not-supported | supported |
| `eu-south-1` (Milan) | not-supported | not-supported | supported |
| `eu-south-2` (Spain) | not-supported | not-supported | supported |
| `eu-west-1` (Ireland) | not-supported | not-supported | supported |
| `eu-west-2` (London) | not-supported | not-supported | supported |
| `eu-west-3` (Paris) | not-supported | not-supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |

[Daybreak Red: GPT-5.6 Cyber](model-card-openai-gpt-56-cyber.md "model-card-openai-gpt-56-cyber.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |

[Daybreak Blue: GPT-5.6 Sol](model-card-openai-gpt-daybreak-blue-56-sol.md "model-card-openai-gpt-daybreak-blue-56-sol.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |

[GPT-5.6 Terra](model-card-openai-gpt-56-terra.md "model-card-openai-gpt-56-terra.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | not-supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | not-supported | supported |
| `eu-central-2` (Zurich) | not-supported | not-supported | supported |
| `eu-north-1` (Stockholm) | not-supported | not-supported | supported |
| `eu-south-1` (Milan) | not-supported | not-supported | supported |
| `eu-south-2` (Spain) | not-supported | not-supported | supported |
| `eu-west-1` (Ireland) | not-supported | not-supported | supported |
| `eu-west-2` (London) | not-supported | not-supported | supported |
| `eu-west-3` (Paris) | not-supported | not-supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |

[GPT-5.6 Luna](model-card-openai-gpt-56-luna.md "model-card-openai-gpt-56-luna.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | not-supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | not-supported | supported |
| `eu-central-2` (Zurich) | not-supported | not-supported | supported |
| `eu-north-1` (Stockholm) | not-supported | not-supported | supported |
| `eu-south-1` (Milan) | not-supported | not-supported | supported |
| `eu-south-2` (Spain) | not-supported | not-supported | supported |
| `eu-west-1` (Ireland) | not-supported | not-supported | supported |
| `eu-west-2` (London) | not-supported | not-supported | supported |
| `eu-west-3` (Paris) | not-supported | not-supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |

[GPT-5.5](model-card-openai-gpt-55.md "model-card-openai-gpt-55.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |

[GPT-5.4](model-card-openai-gpt-54.md "model-card-openai-gpt-54.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | not-supported | not-supported |

[GPT OSS Safeguard 120B](model-card-openai-gpt-oss-safeguard-120b.md "model-card-openai-gpt-oss-safeguard-120b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[gpt-oss-120b](model-card-openai-gpt-oss-120b.md "model-card-openai-gpt-oss-120b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |

[GPT OSS Safeguard 20B](model-card-openai-gpt-oss-safeguard-20b.md "model-card-openai-gpt-oss-safeguard-20b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[gpt-oss-20b](model-card-openai-gpt-oss-20b.md "model-card-openai-gpt-oss-20b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
| `us-gov-west-1` (GovCloud) | supported | supported | not-supported |
| `us-gov-east-1` (GovCloud) | not-supported | supported | not-supported |

## Qwen

[Qwen3 Coder Next](model-card-qwen-qwen3-coder-next.md "model-card-qwen-qwen3-coder-next.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |

[Qwen3 Coder 480B A35B Instruct](model-card-qwen-qwen3-coder-480b-a35b-instruct.md "model-card-qwen-qwen3-coder-480b-a35b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |

[Qwen3 235B A22B 2507](model-card-qwen-qwen3-235b-a22b-2507.md "model-card-qwen-qwen3-235b-a22b-2507.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |

[Qwen3 VL 235B A22B](model-card-qwen-qwen3-vl-235b-a22b.md "model-card-qwen-qwen3-vl-235b-a22b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Qwen3 Next 80B A3B](model-card-qwen-qwen3-next-80b-a3b.md "model-card-qwen-qwen3-next-80b-a3b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Qwen3 32B](model-card-qwen-qwen3-32b.md "model-card-qwen-qwen3-32b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[Qwen3-Coder-30B-A3B-Instruct](model-card-qwen-qwen3-coder-30b-a3b-instruct.md "model-card-qwen-qwen3-coder-30b-a3b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

## Stability AI

Sd3.5 Large| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

Stable Image Core V1:1| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

Stable Image Ultra V1:1| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[Stable Image Control Structure](model-card-stability-ai-stable-image-control-structure.md "model-card-stability-ai-stable-image-control-structure.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Conservative Upscale](model-card-stability-ai-stable-image-conservative-upscale.md "model-card-stability-ai-stable-image-conservative-upscale.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Fast Upscale](model-card-stability-ai-stable-image-fast-upscale.md "model-card-stability-ai-stable-image-fast-upscale.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Control Sketch](model-card-stability-ai-stable-image-control-sketch.md "model-card-stability-ai-stable-image-control-sketch.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Search and Recolor](model-card-stability-ai-stable-image-search-and-recolor.md "model-card-stability-ai-stable-image-search-and-recolor.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Creative Upscale](model-card-stability-ai-stable-image-creative-upscale.md "model-card-stability-ai-stable-image-creative-upscale.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Erase Object](model-card-stability-ai-stable-image-erase-object.md "model-card-stability-ai-stable-image-erase-object.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Inpaint](model-card-stability-ai-stable-image-inpaint.md "model-card-stability-ai-stable-image-inpaint.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Outpaint](model-card-stability-ai-stable-image-outpaint.md "model-card-stability-ai-stable-image-outpaint.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Search and Replace](model-card-stability-ai-stable-image-search-and-replace.md "model-card-stability-ai-stable-image-search-and-replace.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Style Transfer](model-card-stability-ai-stable-image-style-transfer.md "model-card-stability-ai-stable-image-style-transfer.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Style Guide](model-card-stability-ai-stable-image-style-guide.md "model-card-stability-ai-stable-image-style-guide.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Stable Image Remove Background](model-card-stability-ai-stable-image-remove-background.md "model-card-stability-ai-stable-image-remove-background.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

## TwelveLabs

[Marengo Embed 3.0](model-card-twelvelabs-marengo-embed-3-0.md "model-card-twelvelabs-marengo-embed-3-0.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | supported | not-supported |
| `ap-northeast-2` (Seoul) | supported | not-supported | not-supported |

[Marengo Embed v2.7](model-card-twelvelabs-marengo-embed-v2-7.md "model-card-twelvelabs-marengo-embed-v2-7.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `eu-west-1` (Ireland) | not-supported | supported | not-supported |

[Pegasus v1.2](model-card-twelvelabs-pegasus-v1-2.md "model-card-twelvelabs-pegasus-v1-2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | not-supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | supported | supported |
| `eu-central-2` (Zurich) | not-supported | supported | supported |
| `eu-north-1` (Stockholm) | not-supported | supported | supported |
| `eu-south-1` (Milan) | not-supported | supported | supported |
| `eu-south-2` (Spain) | not-supported | supported | supported |
| `eu-west-1` (Ireland) | not-supported | supported | supported |
| `eu-west-2` (London) | not-supported | supported | supported |
| `eu-west-3` (Paris) | not-supported | supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |
| `mx-central-1` (Mexico) | not-supported | not-supported | supported |

## Writer

[Palmyra Vision 7B](model-card-writer-palmyra-vision-7b.md "model-card-writer-palmyra-vision-7b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[Palmyra X5](model-card-writer-palmyra-x5.md "model-card-writer-palmyra-x5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-1` (N. California) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

[Palmyra X4](model-card-writer-palmyra-x4.md "model-card-writer-palmyra-x4.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | not-supported |
| `us-east-2` (Ohio) | not-supported | supported | not-supported |
| `us-west-1` (N. California) | not-supported | supported | not-supported |
| `us-west-2` (Oregon) | not-supported | supported | not-supported |

## xAI

[Grok 4.3](model-card-xai-grok-4-3.md "model-card-xai-grok-4-3.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | supported | supported | not-supported |
| `us-east-1` (N. Virginia) | supported | supported | not-supported |
| `us-east-2` (Ohio) | supported | supported | not-supported |

[Grok 4.6](model-card-xai-grok-4-6.md "model-card-xai-grok-4-6.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | not-supported | supported | supported |
| `us-east-2` (Ohio) | not-supported | supported | supported |
| `us-west-1` (N. California) | not-supported | supported | supported |
| `us-west-2` (Oregon) | not-supported | supported | supported |
| `ca-central-1` (Canada) | not-supported | not-supported | supported |
| `ca-west-1` (Calgary) | not-supported | not-supported | supported |
| `eu-central-1` (Frankfurt) | not-supported | not-supported | supported |
| `eu-central-2` (Zurich) | not-supported | not-supported | supported |
| `eu-north-1` (Stockholm) | not-supported | not-supported | supported |
| `eu-south-1` (Milan) | not-supported | not-supported | supported |
| `eu-south-2` (Spain) | not-supported | not-supported | supported |
| `eu-west-1` (Ireland) | not-supported | not-supported | supported |
| `eu-west-2` (London) | not-supported | not-supported | supported |
| `eu-west-3` (Paris) | not-supported | not-supported | supported |
| `ap-east-2` (Taipei) | not-supported | not-supported | supported |
| `ap-northeast-1` (Tokyo) | not-supported | not-supported | supported |
| `ap-northeast-2` (Seoul) | not-supported | not-supported | supported |
| `ap-northeast-3` (Osaka) | not-supported | not-supported | supported |
| `ap-south-1` (Mumbai) | not-supported | not-supported | supported |
| `ap-south-2` (Hyderabad) | not-supported | not-supported | supported |
| `ap-southeast-1` (Singapore) | not-supported | not-supported | supported |
| `ap-southeast-2` (Sydney) | not-supported | not-supported | supported |
| `ap-southeast-3` (Jakarta) | not-supported | not-supported | supported |
| `ap-southeast-4` (Melbourne) | not-supported | not-supported | supported |
| `ap-southeast-5` (Malaysia) | not-supported | not-supported | supported |
| `ap-southeast-6` (New Zealand) | not-supported | not-supported | supported |
| `ap-southeast-7` (Thailand) | not-supported | not-supported | supported |
| `il-central-1` (Tel Aviv) | not-supported | not-supported | supported |
| `me-central-1` (UAE) | not-supported | not-supported | supported |
| `me-south-1` (Bahrain) | not-supported | not-supported | supported |
| `af-south-1` (Cape Town) | not-supported | not-supported | supported |
| `sa-east-1` (São Paulo) | not-supported | not-supported | supported |

## Z.AI

[GLM 4.7 Flash](model-card-zai-glm-4-7-flash.md "model-card-zai-glm-4-7-flash.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-central-1` (Frankfurt) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-south-1` (Milan) | supported | not-supported | not-supported |
| `eu-west-1` (Ireland) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[GLM 4.7](model-card-zai-glm-4-7.md "model-card-zai-glm-4-7.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |

[GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |

[GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | supported | not-supported | not-supported |
| `us-east-2` (Ohio) | supported | not-supported | not-supported |
| `us-west-2` (Oregon) | supported | not-supported | not-supported |
| `eu-north-1` (Stockholm) | supported | not-supported | not-supported |
| `eu-west-2` (London) | supported | not-supported | not-supported |
| `ap-northeast-1` (Tokyo) | supported | not-supported | not-supported |
| `ap-south-1` (Mumbai) | supported | not-supported | not-supported |
| `ap-southeast-2` (Sydney) | supported | not-supported | not-supported |
| `ap-southeast-3` (Jakarta) | supported | not-supported | not-supported |
| `sa-east-1` (São Paulo) | supported | not-supported | not-supported |
