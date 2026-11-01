

# Release note
<a name="model-customize-release-note"></a>

**The SageMaker AI model customization images**

**Support plan**
+ Major versions: 12 months after next major release
+ Minor versions: 6 months after next minor release
+ Patch versions: No guaranteed support (upgrade to latest patch)

The following table summarizes the distinct container images used by model family for SageMaker AI training jobs and HyperPod recipes. LoRA and full fine-tuning recipes use the same container image unless otherwise noted.



| Model family | Distinct container images | Notes | 
| --- | --- | --- | 
| Llama | `hyperpod-recipes:llmft-v1.0.0`; `hyperpod-recipes:verl-v1.0.0-eks`; `hyperpod-recipes:verl-v1.0.0-smtj`; `hyperpod-recipes-verl-0-7-0:verl-v1.1.4-smtj`; `hyperpod-checkpointless-training:v1.0.0`; `sagemaker-evaluation:latest` | Covers standard SFT and DPO, GRPO-based recipes, VERL 0.7 recipes, checkpointless training, and open-source evaluation. | 
| Qwen | `hyperpod-recipes:llmft-v1.0.0`; `hyperpod-recipes:verl-v1.0.0-eks`; `hyperpod-recipes:verl-v1.0.0-smtj`; `hyperpod-recipes-verl-0-7-0:verl-v1.1.4-smtj`; `mtrl-recipes:rft-trainer-v1.0.0`; `sagemaker-evaluation:latest` | Includes shared open-weight training images and service-only MTRL workflows. | 
| DeepSeek | `hyperpod-recipes:llmft-v1.0.0`; `hyperpod-recipes:verl-v1.0.0-eks`; `hyperpod-recipes:verl-v1.0.0-smtj`; `sagemaker-evaluation:latest` | Uses the shared open-weight training and evaluation images. | 
| GPT-OSS | `hyperpod-recipes:llmft-v1.0.0`; `hyperpod-recipes:verl-v1.0.0-eks`; `hyperpod-recipes:verl-v1.0.0-smtj`; `hyperpod-recipes-verl-0-7-0:verl-v1.1.4-smtj`; `hyperpod-checkpointless-training:v1.0.0`; `mtrl-recipes:rft-trainer-v1.0.0`; `sagemaker-evaluation:latest` | Includes checkpointless training and service-only MTRL workflows. | 
| Gemma | `hyperpod-recipes-verl-0-7-0:verl-v1.1.4-smtj-tf58`; `mtrl-recipes:rft-trainer-v1.0.0`; `sagemaker-evaluation:latest` | Uses a Gemma-specific VERL image track. | 
| Nemotron | `hyperpod-recipes-verl-0-7-0:verl-v1.1.0-smtj-vllm012`; `hyperpod-recipes-verl-0-7-0:verl-v1.1.2-smtj-megatron`; `sagemaker-evaluation:latest` | Uses Nemotron-specific VERL image tracks for Nano and Lightning variants. | 
| Nova | `nova-fine-tune-repo:*`; `nova-evaluation-repo:*`; `nova-distillation-repo:*`; `mtrl-recipes:rft-trainer-v1.0.0` | Uses dedicated Nova repositories instead of the shared `hyperpod-recipes` image family. | 

**AWS Regions support**



| Region | Code | Serverless SMTJ support | 
| --- | --- | --- | 
| Asia Pacific (Mumbai) | ap-south-1 | no | 
| Asia Pacific (Singapore) | ap-southeast-1 | no | 
| Asia Pacific (Sydney) | ap-southeast-2 | no | 
| Asia Pacific (Tokyo) | ap-northeast-1 | yes | 
| Europe (Frankfurt) | eu-central-1 | no | 
| Europe (Ireland) | eu-west-1 | yes | 
| Europe (Stockholm) | eu-north-1 | no | 
| South America (São Paulo) | sa-east-1 | no | 
| US East (N. Virginia) | us-east-1 | yes | 
| US East (Ohio) | us-east-2 | no | 
| US West (N. California) | us-west-1 | no | 
| US West (Oregon) | us-west-2 | yes | 