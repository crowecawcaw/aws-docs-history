

# RFT
<a name="customizing-models-rft"></a>

Reinforcement Fine-Tuning (RFT) uses reinforcement learning to optimize model behavior based on reward signals rather than explicit input-output examples. Amazon SageMaker AI supports two RFT variants: RLVR (Reinforcement Learning with Verifiable Rewards) and RLAIF (Reinforcement Learning from AI Feedback).

## RLVR
<a name="technique-rlvr"></a>

RLVR uses a code-based reward function that programmatically verifies whether model outputs are correct. Best suited for tasks with objectively right or wrong answers.

### When to use
<a name="rlvr-when-to-use"></a>
+ Your task has verifiable correct answers (math, code, factual questions)
+ You can write a scoring function that evaluates response correctness
+ You want to improve factual accuracy and reduce hallucinations

### Dataset format
<a name="rlvr-dataset-format"></a>

Each record contains a prompt and reward model metadata. The reward function evaluates model-generated responses during training.

```
{
  "data_source": "openai/gsm8k",
  "prompt": [
    {
      "content": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? Let's think step by step and output the final answer after \"####\".",
      "role": "user"
    }
  ],
  "ability": "math",
  "reward_model": {
    "ground_truth": "72",
    "style": "rule"
  }
}
```

Required fields:
+ `prompt` — array of message objects with `role` and `content`
+ `reward_model.style` — set to `"rule"` for programmatic verification
+ `reward_model.ground_truth` — the correct answer for verification

To implement your own Lambda-based reward function, see [RLVR - Custom Lambda](model-customize-open-weight-samples.md#model-customize-open-weight-samples-RLVR4). For the supported Lambda response envelopes, see [Sample Lambda Output Payload](model-customize-evaluation-preset-custom-scorers.md#model-customize-evaluation-custom-scorers-lambda-output).

**Note**  
If your Lambda reward function returns a malformed payload, RLVR jobs can fail with `InvalidLambdaResponseException`. Return exactly one of the supported response envelopes described in [Sample Lambda Output Payload](model-customize-evaluation-preset-custom-scorers.md#model-customize-evaluation-custom-scorers-lambda-output) and make sure each result includes a matching `id`.

### Preset reward functions
<a name="rlvr-preset-reward-functions"></a>
+ `gsm8k` — Grade school math verification
+ `prime_code` — Code correctness verification
+ `prime_math` — Mathematical reasoning verification

### Python SDK example
<a name="rlvr-sdk-example"></a>

Use `RLVRTrainer` for serverless RLVR customization jobs:

```
from sagemaker.train import RLVRTrainer

trainer = RLVRTrainer(
    model_id="meta-textgeneration-llama-3-1-8b-instruct",
    train_data="s3://my-bucket/rlvr-train.jsonl",
    hyperparameters={
        "preset_reward_function": "gsm8k",
        "learning_rate": 1e-5,
        "max_epochs": 1,
        "global_batch_size": 128,
        "lora_rank": 16,
    },
)

trainer.train()
```

To run RLVR with FFT, use the same dataset format and remove LoRA-specific hyperparameters such as `lora_rank` and `lora_alpha`.

### RLVR LoRA hyperparameters
<a name="hyperparameters-rlvr-lora-rft"></a>

**Note**  
The tables below show the hyperparameters available when you use [serverless model customization](customize-model.md). Other hyperparameters are preset by Amazon SageMaker AI using optimized defaults. When you use [SageMaker AI Training Jobs](customizing-models-training-jobs.md) or [HyperPod](customizing-models-hyperpod.md), you can access the full list of hyperparameters available in the recipes. See the [SageMaker AI Recipes repository](https://github.com/aws/sagemaker-hyperpod-recipes) to get a recipe and access all hyperparameters.


| Parameter | Type | Required? | Range / Values | Description | 
| --- | --- | --- | --- | --- | 
| preset\_reward\_function | string | Required | gsm8k, prime\_code, prime\_math | Preset reward function for verification. | 
| learning\_rate | float | Required | 1e-07–1e-03 | Step size for weight updates. Set lower for RL (e.g., 1e-5). | 
| lr\_warmup\_steps\_ratio | float | Required | 0–1 | Fraction of steps for LR warmup. | 
| max\_epochs | integer | Required | 1–100 | Number of passes through the dataset. | 
| global\_batch\_size | integer | Required | 128, 256, 512, 1024 | Total samples per optimizer step. | 
| max\_prompt\_length | integer | Required | 512–16384 | Maximum tokens for prompt portion. | 
| weight\_decay | float | Required | 0.0–1.0 | L2 regularization coefficient. | 
| clip\_ratio | float | Required | 0.1–1.5 | GRPO clipping parameter. Limits policy change per update. | 
| kl\_loss\_coef | float | Required | 0–0.1 | KL divergence penalty weight. Prevents policy drift. | 
| rollout\_n | integer | Required | 1, 2, 4, 8, 16, 32 | Candidate responses per prompt during rollouts. | 
| rollout\_temperature | float | Required | 0.01–2.0 | Temperature for rollout generation. | 
| lora\_rank | integer | Required | 8, 16, 32, 64, 128 | LoRA rank. Dimensionality of low-rank matrices. | 
| lora\_alpha | integer | Required | 16, 32, 64, 128, 256 | LoRA scaling factor. Effective LR scales as alpha/rank. | 
| warmup\_steps | integer | Required | -1–100 | Absolute warmup steps (-1 for auto). | 
| min\_lr | float | Required | 0.0–1.0 | Minimum learning rate floor. | 
| clip\_ratio\_high | float | Required | 0.0–0.5 | Upper clipping threshold. | 
| clip\_ratio\_low | float | Required | 0.0–0.5 | Lower clipping threshold. | 
| temperature | float | Required | 0.0–2.0 | Sampling temperature for evaluation. | 
| use\_kl\_loss | boolean | Required | true, false | Add KL divergence penalty to loss. | 
| train\_val\_split\_ratio | float | Optional | 0.0–1.0 | Train/validation split. | 

### RLVR FFT hyperparameters
<a name="hyperparameters-rlvr-fft-rft"></a>

Same parameters as RLVR LoRA without `lora_rank` and `lora_alpha`.

## RLAIF
<a name="technique-rlaif"></a>

RLAIF uses another LLM as a judge to evaluate model responses based on a natural language reward prompt. Best suited for tasks with subjective quality criteria that are difficult to evaluate programmatically.

### When to use
<a name="rlaif-when-to-use"></a>
+ Your quality criteria are subjective (helpfulness, safety, tone)
+ You can describe what "good" looks like in natural language
+ You want to scale feedback beyond what human annotation can provide

### Dataset format
<a name="rlaif-dataset-format"></a>

Each record contains a prompt and reward model metadata. The LLM judge evaluates model-generated responses during training.

```
{
  "data_source": "WeOpenML/PandaLM",
  "prompt": [
    {
      "role": "user",
      "content": "Below are two responses for a given task...Evaluate the responses and generate a reference answer.\n\n### Instruction:\nCompare the given products..."
    }
  ],
  "ability": "pairwise-judging",
  "reward_model": {
    "style": "llmj",
    "ground_truth": "2\n\n### Reason: Response 2 provides a more detailed comparison..."
  }
}
```

Required fields:
+ `prompt` — array of message objects with `role` and `content`
+ `reward_model.style` — set to `"llmj"` for LLM-as-judge
+ `reward_model.ground_truth` — reference judgment for calibration

### Judge templates
<a name="rlaif-judge-templates"></a>

The following preset judge templates are provided in the training container. Set `judge_prompt_template` to one of these values:


| Value | Container path | Use case | Example | 
| --- | --- | --- | --- | 
| cot.jinja | /opt/ml/code/verl/cot.jinja | Chain-of-thought judging | [RLAIF - Chain of Thought](model-customize-open-weight-samples.md#model-customize-open-weight-samples-rlaif2) | 
| evaluate.jinja | /opt/ml/code/verl/evaluate.jinja | General response comparison and scoring | [Reinforcement Learning from AI Feedback (RLAIF) - Pair-Wise Judging](model-customize-open-weight-samples.md#model-customize-open-weight-samples-rlaif) | 
| faithfulness.jinja | /opt/ml/code/verl/faithfulness.jinja | Groundedness and source faithfulness | [RLAIF - Faithfulness](model-customize-open-weight-samples.md#model-customize-open-weight-samples-rlaif3) | 
| summarize.jinja | /opt/ml/code/verl/summarize.jinja | Summarization quality | [RLAIF - Summarization](model-customize-open-weight-samples.md#model-customize-open-weight-samples-rlaif4) | 

To replace a preset template with your own Jinja prompt, see [RLAIF - Custom Prompt](model-customize-open-weight-samples.md#model-customize-open-weight-samples-rlaif5).

### Python SDK example
<a name="rlaif-sdk-example"></a>

Use `RLAIFTrainer` for serverless RLAIF customization jobs:

```
from sagemaker.train import RLAIFTrainer

trainer = RLAIFTrainer(
    model_id="meta-textgeneration-llama-3-1-8b-instruct",
    train_data="s3://my-bucket/rlaif-train.jsonl",
    hyperparameters={
        "judge_prompt_template": "evaluate.jinja",
        "learning_rate": 1e-5,
        "max_epochs": 1,
        "global_batch_size": 128,
        "lora_rank": 16,
    },
)

trainer.train()
```

To run RLAIF with FFT, use the same dataset format and remove LoRA-specific hyperparameters such as `lora_rank` and `lora_alpha`.

### RLAIF LoRA hyperparameters
<a name="hyperparameters-rlaif-lora-rft"></a>

Same parameters as RLVR LoRA with the following difference:


| Parameter | Type | Required? | Range / Values | Description | 
| --- | --- | --- | --- | --- | 
| judge\_prompt\_template | string | Optional | cot.jinja, evaluate.jinja, faithfulness.jinja, summarize.jinja | Template for LLM judge evaluation. Replaces preset\_reward\_function. For the corresponding container paths and example prompts, see [Judge templates](#rlaif-judge-templates). | 

### RLAIF FFT hyperparameters
<a name="hyperparameters-rlaif-fft-rft"></a>

Same parameters as RLAIF LoRA without `lora_rank` and `lora_alpha`.