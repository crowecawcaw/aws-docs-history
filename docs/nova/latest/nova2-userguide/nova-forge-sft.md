

# Supervised Fine-Tuning
<a name="nova-forge-sft"></a>

Amazon Nova Forge data mixing allows you to combine your custom training data with Amazon Nova's proprietary training data during supervised fine-tuning (SFT). This helps preserve the model's general capabilities while specializing it for your target domain. Data mixing is available on two platforms:
+ **SageMaker HyperPod** – Use YAML recipe files to configure data mixing with both text and multimodal data. Supports LoRA and full-rank SFT.
+ **SageMaker Training Jobs** – Use the serverless `CreateTrainingJob` API with `ServerlessJobConfig` for text-only SFT with data mixing. Supports LoRA and full-rank.

**Topics**
+ [Data mixing on SageMaker HyperPod](nova-forge-sft-datamix-smhp.md)
+ [Data mixing on SageMaker Training Jobs](nova-forge-sft-datamix-smtj.md)