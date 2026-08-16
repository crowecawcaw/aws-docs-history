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
| `us-east-1` (N. Virginia) | | | |

[Jamba 1.5 Mini](model-card-ai21-labs-jamba-1-5-mini.md "model-card-ai21-labs-jamba-1-5-mini.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |

## Amazon

[Nova 2 Sonic](model-card-amazon-nova-2-sonic.md "model-card-amazon-nova-2-sonic.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Nova 2 Lite](model-card-amazon-nova-2-lite.md "model-card-amazon-nova-2-lite.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |

[Amazon Nova Multimodal Embeddings](model-card-amazon-amazon-nova-multimodal-embeddings.md "model-card-amazon-amazon-nova-multimodal-embeddings.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-gov-west-1` (GovCloud) | | | |

[Titan Image Generator G1 v2](model-card-amazon-titan-image-generator-g1-v2.md "model-card-amazon-titan-image-generator-g1-v2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |

[Titan Text Embeddings V2](model-card-amazon-titan-text-embeddings-v2.md "model-card-amazon-titan-text-embeddings-v2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-east-1` (GovCloud) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Titan Multimodal Embeddings G1](model-card-amazon-titan-multimodal-embeddings-g1.md "model-card-amazon-titan-multimodal-embeddings-g1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Titan Embeddings G1 - Text](model-card-amazon-titan-embeddings-g1---text.md "model-card-amazon-titan-embeddings-g1---text.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Titan Embeddings G1 - Text v2](model-card-amazon-titan-text-embeddings-v2-2.md "model-card-amazon-titan-text-embeddings-v2-2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |

[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-30) | | |

Rerank| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Nova Sonic](model-card-amazon-nova-sonic.md "model-card-amazon-nova-sonic.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `eu-north-1` (Stockholm) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Nova Pro](model-card-amazon-nova-pro.md "model-card-amazon-nova-pro.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |

[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `eu-west-1` (Ireland) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Nova Lite](model-card-amazon-nova-lite.md "model-card-amazon-nova-lite.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |

[Nova Canvas](model-card-amazon-nova-canvas.md "model-card-amazon-nova-canvas.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-30) | | |
| `eu-west-1` (Ireland) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Nova Micro](model-card-amazon-nova-micro.md "model-card-amazon-nova-micro.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `il-central-1` (Tel Aviv) | | | |

[Nova Premier](model-card-amazon-nova-premier.md "model-card-amazon-nova-premier.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

## Anthropic

[Claude Opus 5](model-card-anthropic-claude-opus-5.md "model-card-anthropic-claude-opus-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |
| `us-gov-west-1` (GovCloud West) | | | |
| `us-gov-east-1` (GovCloud East) | | | |

[Claude Sonnet 5](model-card-anthropic-claude-sonnet-5.md "model-card-anthropic-claude-sonnet-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |
| `us-gov-west-1` (GovCloud West) | | | |
| `us-gov-east-1` (GovCloud East) | | | |

[Claude Mythos 5](model-card-anthropic-claude-mythos-5.md "model-card-anthropic-claude-mythos-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |

[Claude Fable 5](model-card-anthropic-claude-fable-5.md "model-card-anthropic-claude-fable-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Mythos Preview](model-card-anthropic-claude-mythos-preview.md "model-card-anthropic-claude-mythos-preview.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `ap-southeast-4` (Melbourne) | | | |

[Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md "model-card-anthropic-claude-sonnet-4.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `us-west-1` (N. California) | | Legacy (EOL: 2026-10-14) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `eu-central-1` (Frankfurt) | | Legacy (EOL: 2026-10-14) | |
| `eu-north-1` (Stockholm) | | Legacy (EOL: 2026-10-14) | |
| `eu-south-1` (Milan) | | Legacy (EOL: 2026-10-14) | |
| `eu-south-2` (Spain) | | Legacy (EOL: 2026-10-14) | |
| `eu-west-1` (Ireland) | | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `eu-west-3` (Paris) | | Legacy (EOL: 2026-10-14) | |
| `il-central-1` (Tel Aviv) | | Legacy (EOL: 2026-10-14) | |
| `ap-east-2` (Taipei) | | Legacy (EOL: 2026-10-14) | |
| `ap-northeast-1` (Tokyo) | | Legacy (EOL: 2026-10-14) | Legacy (EOL: 2026-10-14) |
| `ap-northeast-2` (Seoul) | | Legacy (EOL: 2026-10-14) | |
| `ap-northeast-3` (Osaka) | | Legacy (EOL: 2026-10-14) | |
| `ap-south-1` (Mumbai) | | Legacy (EOL: 2026-10-14) | |
| `ap-south-2` (Hyderabad) | | Legacy (EOL: 2026-10-14) | |
| `ap-southeast-1` (Singapore) | | Legacy (EOL: 2026-10-14) | |
| `ap-southeast-2` (Sydney) | | Legacy (EOL: 2026-10-14) | |
| `ap-southeast-3` (Jakarta) | | Legacy (EOL: 2026-10-14) | |
| `ap-southeast-4` (Melbourne) | | Legacy (EOL: 2026-10-14) | |
| `ap-southeast-5` (Malaysia) | | Legacy (EOL: 2026-10-14) | |
| `ap-southeast-7` (Thailand) | | Legacy (EOL: 2026-10-14) | |

Claude Opus 4| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md "model-card-anthropic-claude-sonnet-4-6.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Opus 4.8](model-card-anthropic-claude-opus-4-8.md "model-card-anthropic-claude-opus-4-8.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `us-gov-west-1` (GovCloud West) | | | |
| `us-gov-east-1` (GovCloud East) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Opus 4.7](model-card-anthropic-claude-opus-4-7.md "model-card-anthropic-claude-opus-4-7.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md "model-card-anthropic-claude-opus-4-6.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md "model-card-anthropic-claude-opus-4-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md "model-card-anthropic-claude-haiku-4-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md "model-card-anthropic-claude-sonnet-4-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-east-1` (GovCloud) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

[Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md "model-card-anthropic-claude-opus-4-1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2027-01-08) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2027-01-08) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2027-01-08) | |

[Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md "model-card-anthropic-claude-3-haiku.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-09-10) | | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-09-10) | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-09-10) | | |
| `us-gov-east-1` (GovCloud) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-09-10) | | |
| `eu-central-2` (Zurich) | | | |
| `eu-west-1` (Ireland) | Legacy (EOL: 2026-09-10) | | |
| `eu-west-2` (London) | Legacy (EOL: 2026-09-10) | | |
| `eu-west-3` (Paris) | Legacy (EOL: 2026-09-10) | | |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-09-10) | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | Legacy (EOL: 2026-09-10) | | |
| `sa-east-1` (São Paulo) | | | |

Claude 3 Sonnet| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `eu-west-1` (Ireland) | | Legacy (EOL: 2026-07-30) | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | Legacy (EOL: 2026-07-30) | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | Legacy (EOL: 2026-07-30) | | |
| `sa-east-1` (São Paulo) | | | |

Claude 3.7 Sonnet| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-30) | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `eu-north-1` (Stockholm) | | Legacy (EOL: 2026-07-30) | |
| `eu-west-1` (Ireland) | | Legacy (EOL: 2026-07-30) | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | Legacy (EOL: 2026-07-30) | |
| `ap-south-1` (Mumbai) | | | |

Claude 3.5 Sonnet V2:0| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2026-07-30) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-30) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2026-07-30) | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | Legacy (EOL: 2026-07-30) | |

Claude 3.5 Sonnet| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-30) | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `eu-central-1` (Frankfurt) | Legacy (EOL: 2026-07-30) | Legacy (EOL: 2026-07-30) | |
| `eu-central-2` (Zurich) | Legacy (EOL: 2026-07-30) | | |
| `eu-west-1` (Ireland) | | Legacy (EOL: 2026-07-30) | |
| `eu-west-3` (Paris) | | Legacy (EOL: 2026-07-30) | |
| `ap-northeast-1` (Tokyo) | Legacy (EOL: 2026-07-30) | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |

## Cohere

[Embed v4](model-card-cohere-embed-v4.md "model-card-cohere-embed-v4.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `sa-east-1` (São Paulo) | | | |

[Embed English](model-card-cohere-embed-english.md "model-card-cohere-embed-english.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Embed Multilingual](model-card-cohere-embed-multilingual.md "model-card-cohere-embed-multilingual.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Rerank 3.5](model-card-cohere-rerank-3-5.md "model-card-cohere-rerank-3-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `ap-northeast-1` (Tokyo) | | | |

[Command R](model-card-cohere-command-r.md "model-card-cohere-command-r.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-08-19) | | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-08-19) | | |

[Command R+](model-card-cohere-command-r-plus.md "model-card-cohere-command-r-plus.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | Legacy (EOL: 2026-08-19) | | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-08-19) | | |

## DeepSeek

[DeepSeek V3.2](model-card-deepseek-deepseek-v3-2.md "model-card-deepseek-deepseek-v3-2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

[DeepSeek-V3.1](model-card-deepseek-deepseek-v3-1.md "model-card-deepseek-deepseek-v3-1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |

[DeepSeek-R1](model-card-deepseek-deepseek-r1.md "model-card-deepseek-deepseek-r1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

## Google

[Gemma 4 31B](model-card-google-gemma-4-31b.md "model-card-google-gemma-4-31b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |

[Gemma 4 26B-A4B](model-card-google-gemma-4-26b-a4b.md "model-card-google-gemma-4-26b-a4b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |

[Gemma 4 E2B](model-card-google-gemma-4-e2b.md "model-card-google-gemma-4-e2b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |

[Gemma 3 27B PT](model-card-google-gemma-3-27b-pt.md "model-card-google-gemma-3-27b-pt.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Gemma 3 12B IT](model-card-google-gemma-3-12b-it.md "model-card-google-gemma-3-12b-it.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Gemma 3 4B IT](model-card-google-gemma-3-4b-it.md "model-card-google-gemma-3-4b-it.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

## Luma

Ray V2:0| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |

## Meta

[Llama 4 Maverick 17B Instruct](model-card-meta-llama-4-maverick-17b-instruct.md "model-card-meta-llama-4-maverick-17b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |

[Llama 4 Scout 17B Instruct](model-card-meta-llama-4-scout-17b-instruct.md "model-card-meta-llama-4-scout-17b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |

[Llama 3 70B Instruct](model-card-meta-llama-3-70b-instruct.md "model-card-meta-llama-3-70b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-west-2` (London) | | | |
| `ap-south-1` (Mumbai) | | | |

[Llama 3 8B Instruct](model-card-meta-llama-3-8b-instruct.md "model-card-meta-llama-3-8b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-west-2` (London) | | | |
| `ap-south-1` (Mumbai) | | | |

[Llama 3.3 70B Instruct](model-card-meta-llama-3-3-70b-instruct.md "model-card-meta-llama-3-3-70b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Llama 3.2 90B Instruct](model-card-meta-llama-3-2-90b-instruct.md "model-card-meta-llama-3-2-90b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2026-07-07) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-07) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2026-07-07) | |

[Llama 3.2 11B Instruct](model-card-meta-llama-3-2-11b-instruct.md "model-card-meta-llama-3-2-11b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2026-07-07) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-07) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2026-07-07) | |

[Llama 3.2 3B Instruct](model-card-meta-llama-3-2-3b-instruct.md "model-card-meta-llama-3-2-3b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2026-07-07) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-07) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2026-07-07) | |
| `eu-central-1` (Frankfurt) | | Legacy (EOL: 2026-07-07) | |
| `eu-west-1` (Ireland) | | Legacy (EOL: 2026-07-07) | |
| `eu-west-3` (Paris) | | Legacy (EOL: 2026-07-07) | |

[Llama 3.2 1B Instruct](model-card-meta-llama-3-2-1b-instruct.md "model-card-meta-llama-3-2-1b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | Legacy (EOL: 2026-07-07) | |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-07) | |
| `us-west-2` (Oregon) | | Legacy (EOL: 2026-07-07) | |
| `eu-central-1` (Frankfurt) | | Legacy (EOL: 2026-07-07) | |
| `eu-west-1` (Ireland) | | Legacy (EOL: 2026-07-07) | |
| `eu-west-3` (Paris) | | Legacy (EOL: 2026-07-07) | |

[Llama 3.1 405B Instruct](model-card-meta-llama-3-1-405b-instruct.md "model-card-meta-llama-3-1-405b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | | Legacy (EOL: 2026-07-07) | |
| `us-west-2` (Oregon) | Legacy (EOL: 2026-07-07) | | |

[Llama 3.1 70B Instruct](model-card-meta-llama-3-1-70b-instruct.md "model-card-meta-llama-3-1-70b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Llama 3.1 8B Instruct](model-card-meta-llama-3-1-8b-instruct.md "model-card-meta-llama-3-1-8b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

## MiniMax

[MiniMax M2](model-card-minimax-minimax-m2.md "model-card-minimax-minimax-m2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[MiniMax M2.1](model-card-minimax-minimax-m2-1.md "model-card-minimax-minimax-m2-1.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

[MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |

[MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

## Mistral AI

[Magistral Small 2509](model-card-mistral-ai-magistral-small-2509.md "model-card-mistral-ai-magistral-small-2509.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Pixtral Large](model-card-mistral-ai-pixtral-large.md "model-card-mistral-ai-pixtral-large.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-3` (Paris) | | | |

Mistral Large 2407| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |

[Mistral Small](model-card-mistral-ai-mistral-small.md "model-card-mistral-ai-mistral-small.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |

[Mistral Large](model-card-mistral-ai-mistral-large.md "model-card-mistral-ai-mistral-large.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Voxtral Small 24B 2507](model-card-mistral-ai-voxtral-small-24b-2507.md "model-card-mistral-ai-voxtral-small-24b-2507.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Mixtral 8x7B Instruct](model-card-mistral-ai-mixtral-8x7b-instruct.md "model-card-mistral-ai-mixtral-8x7b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Mistral 7B Instruct](model-card-mistral-ai-mistral-7b-instruct.md "model-card-mistral-ai-mistral-7b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Voxtral Mini 3B 2507](model-card-mistral-ai-voxtral-mini-3b-2507.md "model-card-mistral-ai-voxtral-mini-3b-2507.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Mistral Large 3](model-card-mistral-ai-mistral-large-3.md "model-card-mistral-ai-mistral-large-3.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Ministral 14B 3.0](model-card-mistral-ai-ministral-14b-3-0.md "model-card-mistral-ai-ministral-14b-3-0.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Ministral 3 8B](model-card-mistral-ai-ministral-3-8b.md "model-card-mistral-ai-ministral-3-8b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Ministral 3B](model-card-mistral-ai-ministral-3b.md "model-card-mistral-ai-ministral-3b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Devstral 2 123B](model-card-mistral-ai-devstral-2-123b.md "model-card-mistral-ai-devstral-2-123b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

## Moonshot AI

[Kimi K2.5](model-card-moonshot-ai-kimi-k2-5.md "model-card-moonshot-ai-kimi-k2-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

## NVIDIA

[NVIDIA Nemotron Nano 12B v2 VL BF16](model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md "model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `us-gov-east-1` (GovCloud) | | | |

[NVIDIA Nemotron Nano 9B v2](model-card-nvidia-nvidia-nemotron-nano-9b-v2.md "model-card-nvidia-nvidia-nemotron-nano-9b-v2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `us-gov-east-1` (GovCloud) | | | |

[Nemotron Nano 3 30B](model-card-nvidia-nemotron-nano-3-30b.md "model-card-nvidia-nemotron-nano-3-30b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `us-gov-east-1` (GovCloud) | | | |

[NVIDIA Nemotron 3 Super 120B](model-card-nvidia-nemotron-super-3-120b.md "model-card-nvidia-nemotron-super-3-120b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `us-gov-east-1` (GovCloud) | | | |

## OpenAI

[GPT-5.6 Sol](model-card-openai-gpt-56-sol.md "model-card-openai-gpt-56-sol.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |

[Daybreak Red: GPT-5.6 Cyber](model-card-openai-gpt-56-cyber.md "model-card-openai-gpt-56-cyber.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | | | |

[Daybreak Blue: GPT-5.6 Sol](model-card-openai-gpt-daybreak-blue-56-sol.md "model-card-openai-gpt-daybreak-blue-56-sol.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | | | |

[GPT-5.6 Terra](model-card-openai-gpt-56-terra.md "model-card-openai-gpt-56-terra.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |

[GPT-5.6 Luna](model-card-openai-gpt-56-luna.md "model-card-openai-gpt-56-luna.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-6` (New Zealand) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |

[GPT-5.5](model-card-openai-gpt-55.md "model-card-openai-gpt-55.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |

[GPT-5.4](model-card-openai-gpt-54.md "model-card-openai-gpt-54.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `us-gov-west-1` (GovCloud) | | | |

[GPT OSS Safeguard 120B](model-card-openai-gpt-oss-safeguard-120b.md "model-card-openai-gpt-oss-safeguard-120b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[gpt-oss-120b](model-card-openai-gpt-oss-120b.md "model-card-openai-gpt-oss-120b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `us-gov-east-1` (GovCloud) | | | |

[GPT OSS Safeguard 20B](model-card-openai-gpt-oss-safeguard-20b.md "model-card-openai-gpt-oss-safeguard-20b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[gpt-oss-20b](model-card-openai-gpt-oss-20b.md "model-card-openai-gpt-oss-20b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |
| `us-gov-west-1` (GovCloud) | | | |
| `us-gov-east-1` (GovCloud) | | | |

## Qwen

[Qwen3 Coder Next](model-card-qwen-qwen3-coder-next.md "model-card-qwen-qwen3-coder-next.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `eu-west-2` (London) | | | |
| `ap-southeast-2` (Sydney) | | | |

[Qwen3 Coder 480B A35B Instruct](model-card-qwen-qwen3-coder-480b-a35b-instruct.md "model-card-qwen-qwen3-coder-480b-a35b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |

[Qwen3 235B A22B 2507](model-card-qwen-qwen3-235b-a22b-2507.md "model-card-qwen-qwen3-235b-a22b-2507.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |

[Qwen3 VL 235B A22B](model-card-qwen-qwen3-vl-235b-a22b.md "model-card-qwen-qwen3-vl-235b-a22b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Qwen3 Next 80B A3B](model-card-qwen-qwen3-next-80b-a3b.md "model-card-qwen-qwen3-next-80b-a3b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `sa-east-1` (São Paulo) | | | |

[Qwen3 32B](model-card-qwen-qwen3-32b.md "model-card-qwen-qwen3-32b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

[Qwen3-Coder-30B-A3B-Instruct](model-card-qwen-qwen3-coder-30b-a3b-instruct.md "model-card-qwen-qwen3-coder-30b-a3b-instruct.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

## Stability AI

Sd3.5 Large| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |

Stable Image Core V1:1| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |

Stable Image Ultra V1:1| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |

[Stable Image Control Structure](model-card-stability-ai-stable-image-control-structure.md "model-card-stability-ai-stable-image-control-structure.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Conservative Upscale](model-card-stability-ai-stable-image-conservative-upscale.md "model-card-stability-ai-stable-image-conservative-upscale.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Fast Upscale](model-card-stability-ai-stable-image-fast-upscale.md "model-card-stability-ai-stable-image-fast-upscale.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Control Sketch](model-card-stability-ai-stable-image-control-sketch.md "model-card-stability-ai-stable-image-control-sketch.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Search and Recolor](model-card-stability-ai-stable-image-search-and-recolor.md "model-card-stability-ai-stable-image-search-and-recolor.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Creative Upscale](model-card-stability-ai-stable-image-creative-upscale.md "model-card-stability-ai-stable-image-creative-upscale.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Erase Object](model-card-stability-ai-stable-image-erase-object.md "model-card-stability-ai-stable-image-erase-object.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Inpaint](model-card-stability-ai-stable-image-inpaint.md "model-card-stability-ai-stable-image-inpaint.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Outpaint](model-card-stability-ai-stable-image-outpaint.md "model-card-stability-ai-stable-image-outpaint.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Search and Replace](model-card-stability-ai-stable-image-search-and-replace.md "model-card-stability-ai-stable-image-search-and-replace.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Style Transfer](model-card-stability-ai-stable-image-style-transfer.md "model-card-stability-ai-stable-image-style-transfer.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Style Guide](model-card-stability-ai-stable-image-style-guide.md "model-card-stability-ai-stable-image-style-guide.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Stable Image Remove Background](model-card-stability-ai-stable-image-remove-background.md "model-card-stability-ai-stable-image-remove-background.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

## TwelveLabs

[Marengo Embed 3.0](model-card-twelvelabs-marengo-embed-3-0.md "model-card-twelvelabs-marengo-embed-3-0.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `eu-west-1` (Ireland) | | | |
| `ap-northeast-2` (Seoul) | | | |

[Marengo Embed v2.7](model-card-twelvelabs-marengo-embed-v2-7.md "model-card-twelvelabs-marengo-embed-v2-7.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `eu-west-1` (Ireland) | | | |

[Pegasus v1.2](model-card-twelvelabs-pegasus-v1-2.md "model-card-twelvelabs-pegasus-v1-2.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |
| `ca-central-1` (Canada) | | | |
| `ca-west-1` (Calgary) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-central-2` (Zurich) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-south-2` (Spain) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `eu-west-3` (Paris) | | | |
| `ap-east-2` (Taipei) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-northeast-2` (Seoul) | | | |
| `ap-northeast-3` (Osaka) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-south-2` (Hyderabad) | | | |
| `ap-southeast-1` (Singapore) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `ap-southeast-4` (Melbourne) | | | |
| `ap-southeast-5` (Malaysia) | | | |
| `ap-southeast-7` (Thailand) | | | |
| `il-central-1` (Tel Aviv) | | | |
| `me-central-1` (UAE) | | | |
| `me-south-1` (Bahrain) | | | |
| `af-south-1` (Cape Town) | | | |
| `sa-east-1` (São Paulo) | | | |
| `mx-central-1` (Mexico) | | | |

## Writer

[Palmyra Vision 7B](model-card-writer-palmyra-vision-7b.md "model-card-writer-palmyra-vision-7b.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |

[Palmyra X5](model-card-writer-palmyra-x5.md "model-card-writer-palmyra-x5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |

[Palmyra X4](model-card-writer-palmyra-x4.md "model-card-writer-palmyra-x4.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-1` (N. California) | | | |
| `us-west-2` (Oregon) | | | |

## xAI

[Grok 4.3](model-card-xai-grok-4-3.md "model-card-xai-grok-4-3.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-west-2` (Oregon) | | | |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |

## Z.AI

[GLM 4.7 Flash](model-card-zai-glm-4-7-flash.md "model-card-zai-glm-4-7-flash.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-central-1` (Frankfurt) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-south-1` (Milan) | | | |
| `eu-west-1` (Ireland) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

[GLM 4.7](model-card-zai-glm-4-7.md "model-card-zai-glm-4-7.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |

[GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-west-2` (Oregon) | | | |

[GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md")| Region | In-Region | Geo | Global |
| --- | --- | --- | --- |
| `us-east-1` (N. Virginia) | | | |
| `us-east-2` (Ohio) | | | |
| `us-west-2` (Oregon) | | | |
| `eu-north-1` (Stockholm) | | | |
| `eu-west-2` (London) | | | |
| `ap-northeast-1` (Tokyo) | | | |
| `ap-south-1` (Mumbai) | | | |
| `ap-southeast-2` (Sydney) | | | |
| `ap-southeast-3` (Jakarta) | | | |
| `sa-east-1` (São Paulo) | | | |
