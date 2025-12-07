# Release note

**The SageMaker AI model customization images**

**Support plan**

- Major versions: 12 months after next major release
- Minor versions: 6 months after next minor release
- Patch versions: No guaranteed support (upgrade to latest patch)
  Below are the release notes for Base Deep Learning Containers for Amazon EKS (EKS) and SageMaker AI
  training jobs (SMTJ):

| Version | Type | Service | Image URL                                                                          |
| ------- | ---- | ------- | ---------------------------------------------------------------------------------- |
| 1.0.0   | CUDA | EKS     | `652744875666.dkr.ecr.amazonaws.com/hyperpod-model-customization:verl-eks-v1.0.0`  |
| 1.0.0   | CUDA | SMTJ    | `652744875666.dkr.ecr.amazonaws.com/hyperpod-model-customization:verl-smtj-v1.0.0` |
| 1.0.0   | CUDA | SMJT    | `652744875666.dkr.ecr.amazonaws.com/hyperpod-model-customization:v1-v1.0.0`        |
| 1.0.0   | CUDA | SMTJ    | `652744875666.dkr.ecr.amazonaws.com/hyperpod-model-customization:llama-90b-v1.0.0` |

**AWS Regions support**

| Region                    | Code           | Serverless SMTJ support |
| ------------------------- | -------------- | ----------------------- |
| Asia Pacific (Mumbai)     | ap-south-1     | no                      |
| Asia Pacific (Singapore)  | ap-southeast-1 | no                      |
| Asia Pacific (Sydney)     | ap-southeast-2 | no                      |
| Asia Pacific (Tokyo)      | ap-northeast-1 | yes                     |
| Europe (Frankfurt)        | eu-central-1   | no                      |
| Europe (Ireland)          | eu-west-1      | yes                     |
| Europe (Stockholm)        | eu-north-1     | no                      |
| South America (São Paulo) | sa-east-1      | no                      |
| US East (N. Virginia)     | us-east-1      | yes                     |
| US East (Ohio)            | us-east-2      | no                      |
| US West (N. California)   | us-west-1      | no                      |
| US West (Oregon)          | us-west-2      | yes                     |
