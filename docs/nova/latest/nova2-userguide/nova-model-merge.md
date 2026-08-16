# Model Merge

###### Important

Throughout this doc, we will reference "base model" as one of the two models.
It can be the original foundation model (e.g. Nova Lite 2.0) if no
[iterative training](nova-iterative-training.md "nova-iterative-training.md") was run, or the output of the
previous [iterative training](nova-iterative-training.md "nova-iterative-training.md") run.

After fine-tuning completes, your customized model goes through an **optional
user-configurable** model merging step that blends the newly learned knowledge with
the capabilities of the "base model". This process ensures that your final model retains the original
intelligence of the "base model" while incorporating the specialized behavior learned during
the latest fine-tuning training run. Model merging mitigates a phenomenon known as _catastrophic
forgetting_, where a model loses previously learned knowledge after being
fine-tuned on new data.

## Model merge applicability by training type

Model merging is only configurable for SFT training. The following table summarizes
the model merge behavior for each training type:

| Training type                                                                                            | Model merge behavior                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Supervised Fine-Tuning (SFT)](nova-fine-tune.md "nova-fine-tune.md")                                    | User-configurable model merging is applied. You can control the merge weight<br>between the fine-tuned model and the base model as described in this document. |
| [Reinforcement Fine-Tuning (RFT)](nova-reinforcement-fine-tuning.md "nova-reinforcement-fine-tuning.md") | No model merging. The trained model checkpoint is output directly as the final<br>model. There is no base model involved in a merge step.                      |
| [Continued Pre-Training (CPT)](nova-cpt.md "nova-cpt.md")                                                | No model merging. The trained model checkpoint is output directly as the final<br>model. There is no base model involved in a merge step.                      |

## When to use model merging

You should enable model merging when:

- **General capabilities degrade after fine-tuning.**
  If your fine-tuned model loses performance on tasks outside your training data
  (for example, math, reasoning, or coding), merging blends back base model knowledge
  to recover those skills.
- **Iterative/continual training.**
  When fine-tuning on top of a previously customized checkpoint, merging is essential
  to retain skills learned in earlier rounds. Without it, each new round can overwrite
  what the previous round taught.

You may **not need** model merging when:

- **You want to only maximize target task performance**
  and general capability retention is not a concern.
- **Hill climbing.**
  You want to continue iterating on the same dataset to optimize eval performance
  further.
- **You are using reasoning-based fine-tuning.**
  Studies have shown reasoning-based SFT significantly mitigates catastrophic
  forgetting.

## How to configure model merging weights

The default value of `model_importance_score.fine_tuned_model` is 1.0,
meaning the training output checkpoint uses the fine-tuned weights entirely, with no
blending from the "base model". The default works well when your training data is comprehensive
and closely represents your target task.

You can control how the final model balances specialization versus general knowledge
by setting the `model_importance_score` in your [hyperparameters](nova-sft-2-smtj.md#nova-2-selecting-hyperparameters "nova-sft-2-smtj.md#nova-2-selecting-hyperparameters"). For example:

```

    training_config:
    # ...
      model_importance_score:
        fine_tuned_model: 0.75 # set value between 0.0 to 1.0 inclusive

```

`model_importance_score.fine_tuned_model` values closer to 1.0 make the model
lean toward your fine-tuned data, while values closer to 0.0 preserve more of the base
model's general capabilities. In the above example, the final trained model is produced
by merging 75% fine tuned model on the specific dataset with 25% of the "base model".

If you notice that your fine-tuned model loses general capabilities (for example,
degraded performance on tasks outside your training data), reduce `model_importance_score.fine_tuned_model` to blend in more of the "base model"'s
knowledge.

###### Note

Even though we can configure the weights of the model merge process, the user cannot choose which models
to merge with. In other words, it will always be between the "base model" and the fine-tuned model of
the current training run. The "base model" can be the original foundation model (e.g. Nova Lite 2.0),
or the output of the previous [iterative training](nova-iterative-training.md "nova-iterative-training.md") run.

## Choosing model merge weights

The `model_importance_score.fine_tuned_model` parameter controls the
balance between your fine-tuned model and the base model. Start with these
guidelines:

| Scenario                                                    | Recommended starting weight       | Rationale                                                                                                                                            |
| ----------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single-round SFT with comprehensive training data           | *_1.0_<br>• (default, no merging) | Your training data covers the target task well; merging would dilute<br>learned behavior without benefit.                                            |
| Single-round SFT where general capabilities degrade         | **0.7–0.9**                       | Blends in enough base model knowledge to recover general skills<br>(math, reasoning, coding) while preserving most of the fine-tuned<br>performance. |
| Iterative/continual SFT (building on a previous checkpoint) | **0.3–0.7**                       | Lower weights retain more knowledge from prior training rounds.<br>Without merging, later rounds can overwrite skills learned in earlier<br>rounds.  |
| Exploratory / unsure                                        | **0.7**                           | A reasonable middle ground; adjust based on evaluation<br>results.                                                                                   |

**General principle:** Higher weights (closer to 1.0)
maximize target task performance but risk losing general capabilities. Lower weights
(closer to 0.0) preserve the base model's broad skills but reduce specialization.
There is no universally optimal value — the right weight depends on your dataset size,
domain overlap with the base model, and which capabilities you need to retain.

###### Tip

If your training data includes reasoning traces (chain-of-thought), you can
typically use a higher merge weight (or skip merging entirely at 1.0), because
reasoning-augmented data acts as a regularizer that preserves general
capabilities.

## Evaluating your merge weight

After training completes, evaluate the merged model to confirm the merge weight is
appropriate. You don't need multiple training runs — a single evaluation pass can tell
you whether to adjust.

- **Target task performance** — Run your
  domain-specific evaluation (accuracy, F1, extraction score, etc.) on a held-out
  test set. Compare against the base model (before any fine-tuning) to confirm
  fine-tuning improved performance. If the gain over the base model is smaller
  than expected, your merge weight may be too low — the base model's weights are
  diluting what was learned during training.
- **General capability spot-check** — Prompt the
  merged model with a few tasks outside your training domain (for example, a math
  word problem, a summarization request, or a coding question). Compare the
  responses qualitatively against the base model. If the merged model's responses
  are noticeably worse than the base model — incoherent, refusing to answer, or
  producing gibberish on tasks the base model handles well — your merge weight is
  too high and the model has lost general capabilities.

## How merging works: Full-rank fine-tuning

Full-rank training produces a complete set of model weights. During merging, each
parameter is computed as a weighted blend:

```

# Weighted interpolation
Merged Model = (1 - model_importance_score.fine_tuned_model) * Base Model + model_importance_score.fine_tuned_model * Fine-Tuned Model

```

For example, with `model_importance_score.fine_tuned_model = 0.3`, the
merged model is 70% "base model" knowledge and 30% fine-tuned knowledge.

## How merging works: LoRA fine-tuning

LoRA (Low-Rank Adaptation) learns a compact pair of low-rank matrices (A and B)
that represent the adaptation as a low-rank update. During the model merge process,
each A and B LoRA matrix is scaled by the `model_importance_score.fine_tuned_model` as shown below. In these formulas, `alpha` is the LoRA scaling factor (`peft.lora_tuning.alpha` in your
training recipe) and `rank` is the LoRA rank. For the available `alpha` values, see the [LoRA
SFT training recipe](https://github.com/aws/sagemaker-hyperpod-recipes/blob/main/recipes_collection/recipes/fine-tuning/nova/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_lora_sft.yaml "https://github.com/aws/sagemaker-hyperpod-recipes/blob/main/recipes_collection/recipes/fine-tuning/nova/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_lora_sft.yaml").

Note that, at this point, the A and B matrices only contains knowledge from the latest
fine-tuning run. It has no knowledge of previous training runs. The knowledge from
previous training runs will come from the model merge with "base model" or the previous stage LoRA
adapter merge described below.

```

Scaled_A = sqrt(model_importance_score.fine_tuned_model) * sqrt(alpha/rank) * A
Scaled_B = sqrt(model_importance_score.fine_tuned_model) * sqrt(alpha/rank) * B

```

**LoRA training produces two model artifacts: a fully merged model and a set of merged LoRA adapters**.
Let's take a look at each of them separately.

**Fully merged model**

The LoRA update is scaled and added to the "base model":

```

Merged Model = Base Model + (Scaled_B @ Scaled_A)

```

Now the `Merged Model` has knowledge from both the current training
run as well as inheriting some knowledge from the `Base Model` depending
on the user configured `model_importance_score.fine_tuned_model`.

**Merged LoRA adapters**

How the LoRA adapters are merged depends on whether you are performing
single-stage or iterative training.

- For single-stage LoRA training (no iterative training), the
  fine-tuned LoRA adapters are saved directly without merging,
  because there isn't a previous set of LoRA adapters to merge with.
- In [iterative
  all-LoRA workflows](nova-iterative-training.md#nova-iterative-technique-consistency "nova-iterative-training.md#nova-iterative-technique-consistency"), the adapters from each stage are merged into a
  single set:

```

Merged = Stage1_Scaled_B @ Stage1_Scaled_A + Stage2_Scaled_B @ Stage2_Scaled_A

```

The `Merged` LoRA adapters will contain knowledge of previous
training iterations as well as the latest fine-tuning knowledge, based on
the user-defined `model_importance_score.fine_tuned_model`.

Also, please pay close attention to the [iterative training
restrictions](nova-iterative-training.md#nova-iterative-technique-consistency "nova-iterative-training.md#nova-iterative-technique-consistency") on mixing LoRA and Full-rank training.

These merged adapters `Merged_B` and `Merged_A` reflect the
complete training history and are used for [on-demand
inference](nova-model-bedrock-inference.md#custom-fine-tune-odi "nova-model-bedrock-inference.md#custom-fine-tune-odi").
