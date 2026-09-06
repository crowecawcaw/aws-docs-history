

# Amazon Nova recipes
<a name="nova-model-recipes"></a>

You can get an Amazon Nova recipe from the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes) repository. An Amazon Nova recipe is a [YAML](https://yaml.org/) configuration file that provides details to SageMaker on how to run your model customization job. It provides the base model name, sets training hyperparameters, defines optimization settings, and includes any additional options required to fine-tune or train the model successfully.

You can also access Amazon Nova recipes through SageMaker AI Monarch and JumpStart by navigating to the SageMaker JumpStart model hub, selecting AWS, and browsing Amazon Nova models to find their associated recipes. Both SageMaker AI Monarch and JumpStart provide sample notebooks for each recipe, which include all the necessary steps to modify the recipes and run customization jobs using SageMaker training jobs or SageMaker HyperPod environments.

To access the recipes pages in Amazon SageMaker Studio, the execution role must have the following permissions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::*model-customization-recipes*"
            ]
        }
    ]
}
```

------

To execute the sample notebooks on SageMaker training jobs and SageMaker HyperPod, use one of the following SageMaker distribution image versions: `2.7.1+`, `2.8.0+`, `3.2.1+`, `3.3.0+`. This applies to both SageMaker AI Monarch and JumpStart.

**Topics**
+ [Getting Amazon Nova recipes](#nova-model-get-recipes)
+ [Getting Amazon Nova Forge recipes](#nova-model-get-forge-recipes)
+ [Available models and algorithms](#nova-model-algorithm)
+ [Amazon Nova 2.0 Lite](#nova-model-recipes-reference-novalite2)

## Getting Amazon Nova recipes
<a name="nova-model-get-recipes"></a>

To get a base Amazon Nova recipe, clone the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes) repository by running the following command.

```
git clone https://github.com/aws/sagemaker-hyperpod-recipes.git
```

The base recipes are available at [`recipes_collection/recipes/`](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/).

```
cd recipes_collection/recipes/
```

The Amazon Nova customization recipes are in the following folders.



| Recipe type | Folder | 
| --- | --- | 
| SFT (Full-rank and PEFT) | [fine-tuning/nova](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova) | 
| Evaluation | [evaluation/nova](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/evaluation/nova) | 
| CPT | [training/nova](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training) | 

## Getting Amazon Nova Forge recipes
<a name="nova-model-get-forge-recipes"></a>

To access specialized Amazon Nova Forge recipes for SageMaker HyperPod jobs, please [set up your access to Amazon Nova Forge](nova-forge-access.md) and then follow [this workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US/02-smhp-rig/03-nova-forge) to set up the Forge version of the SageMaker HyperPod CLI. For SageMaker Training Jobs, the AWS Console and SageMaker Python SDK will automatically access Forge recipes.

## Available models and algorithms
<a name="nova-model-algorithm"></a>

The following table summarizes the availability of customization for Amazon Nova 2.0 models and supported algorithms using SageMaker. For Amazon Nova 1.0 model customization, see the [Amazon Nova 1.0 recipes](https://docs.aws.amazon.com/nova/latest/userguide/nova-model-recipes.html).


| Model name | Model ID | Fine-tuning | Notes | 
| --- |--- |--- |--- |
| Amazon Nova Lite 2.0 | amazon.nova-2-lite-v1:0:256k | Yes |  +  SFT - Accepts either text and/or image or text and/or video as the input and produces text as output. A single job can't combine text, image, and video in the same run. <br />+  RFT - Accepts text as input for single-turn conversations and produces text as output. <br />+  CPT - Accepts text as input.   | 

## Amazon Nova 2.0 Lite
<a name="nova-model-recipes-reference-novalite2"></a>

The table below lists detailed information of the Amazon Nova 2.0 Lite recipes reference. Scroll horizontally to view the full table, including Image URIs and compute instance types.



| Model | Category/Sub-category | Technique | Recipe Name | Image URI (Training Jobs) | Image URI (SageMaker HyperPod) | Compute Instance | 
| --- | --- | --- | --- | --- | --- | --- | 
| Nova 2.0 Lite | Training | Continued Pre Training | nova\_lite\_2\_0\_p5x8\_gpu\_pretrain.yaml | N/A | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-CPT-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | Parameter Efficient Fine Tuning | Fine Tuning | nova\_lite\_2\_0\_p5\_gpu\_lora\_sft.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | Full-Rank Fine Tuning | Fine Tuning | nova\_lite\_2\_0\_p5\_gpu\_sft.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | Parameter Efficient RFT | Fine Tuning | nova\_lite\_v2\_smtj\_p5\_p5en\_gpu\_lora\_rft.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-RFT-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-RFT-TRAIN-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | Full Rank RFT | Fine Tuning | nova\_lite\_v2\_smtj\_p5en\_gpu\_rft.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-RFT-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-RFT-TRAIN-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | Bring Your Own Data | Evaluation | nova\_lite\_2\_0\_p5\_48xl\_gpu\_bring\_your\_own\_dataset\_eval.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | General Text Benchmark | Evaluation | nova\_lite\_2\_0\_p5\_48xl\_gpu\_general\_text\_benchmark\_eval.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | RFT Evaluation | Evaluation | nova\_lite\_2\_0\_p5\_48xl\_gpu\_rft\_eval.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 
| Nova 2.0 Lite | LLM Rubric Based Judge | Evaluation | nova\_lite\_2\_0\_p5\_48xl\_gpu\_rubric\_llm\_judge\_eval.yaml | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-V2-latest | ml.p5.48xlarge, ml.p5en.48xlarge | 