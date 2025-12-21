# Continued Pre-Training and Mid-Training

###### Note

Detailed documentation is provided once subscribed

Nova Forge CPT offers advanced capabilities beyond standard CPT, including access to
intermediate checkpoints and data mixing with Nova's pre-training corpus. These features
enable more efficient domain adaptation and better preservation of the model's general
capabilities.

## What are intermediate checkpoints and

why are they needed?

Intermediate checkpoints are snapshots of the Amazon Nova model saved at different
stages of the pre-training, before the model reaches its final production-ready
state. During model development, Amazon Nova undergoes multiple training phases: initial
pre-training with constant learning rate, learning rate ramp-down, context extension
training, and finally instruction-following alignment and safety training. For CPT,
intermediate checkpoints are often preferable to the final Prod checkpoint because
they are more plastic and receptive to domain adaptation. The Prod checkpoint has
undergone extensive instruction-following alignment and safety training, which
optimizes the model for general conversational use but can make it resistant to
learning new domain-specific patterns during CPT. In contrast, Partially and Fully
pre-trained text only checkpoints retain the model's pre-training characteristics.
They haven't been heavily steered toward specific behaviors, making them more
efficient starting points for domain adaptation. When performing large-scale CPT
(>10B tokens), starting from intermediate checkpoints typically results in faster
convergence, better training stability, and more effective domain knowledge
acquisition. However, for small-scale CPT (<10B tokens), or when
instruction-following capabilities need to be preserved, the Prod checkpoint may be
more appropriate as it allows domain adaptation while maintaining the model's
conversational abilities.

Multiple intermediate checkpoints are necessary for CPT because they offer
different levels of model plasticity that affect how efficiently the model can
absorb new domain knowledge. The final Prod checkpoint has undergone extensive
instruction-following alignment and safety training, which optimizes it for general
conversational use but makes it resistant to learning new domain-specific patterns.
In other words, It has been hardened through post-training. In contrast, earlier
checkpoints retain the model's pre-training characteristics and haven't been heavily
steered toward specific behaviors, making them more plastic and receptive to domain
adaptation.

To achieve the best training efficiency, multiple intermediate checkpoints are
provided.

## What checkpoints are available?

###### Nova 1.0

Amazon Nova 1.0 family has three models (Micro, Lite, Pro) and for each model there
are three checkpoints available.

- PRE-TRAINED -
  [`nova-<micro/lite/pro>/pretraining-text-partial`]:
  This is the checkpoint after the constant learning rate stage of Amazon Nova
  pre-training where the model is trained on trillions of text tokens.
- MID-TRAINED -
  [`nova-<micro/lite/pro>/pretraining-text-full`]: This
  is the text-only checkpoint after all the stages of Amazon Nova pre-training and
  mid-training with trillions of text tokens have finished. Use these if the
  model specifically should not have seen any multi-modal data.
- MID-TRAINED - [`nova-<lite/pro>/pretraining-mm-full`]:
  This is the checkpoint after all the stages of Amazon Nova pre-training and
  mid-training, including multi-modal data, with trillions of tokens have been
  processed.
- POST-TRAINED - [`nova-<micro/lite/pro>/prod`]: This is the fully
  aligned final checkpoint of the model that has gone through all the
  pre-training and post training steps.

###### Nova 2.0

There are three Amazon Nova Lite 2.0 checkpoints.

- PRE-TRAINED - [`nova-lite-2/pretraining-text-RD`]: This is the
  checkpoint after the constant learning rate and ramp-down stages of Amazon Nova
  pre-training where the model is trained on trillions of tokens.
- MID-TRAINED - [`nova-lite-2/pretraining-text-CE`]: This
  checkpoint allows intermediate volumes of unstructured data to be introduced
  with a more conservative learning rate than pre-training, absorbing
  domain-specific knowledge while avoiding catastrophic forgetting.
- POST-TRAINED - [`nova-lite-2/prod`]: This is the fully aligned final
  checkpoint of the model that has gone through all the pertaining and post
  training steps.

The following table elaborates on the different conditions for pre- and
mid-training.

| Data Type                                                                                                       | Perform                         | With Checkpoint |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------- |
| Large-scale unstructured raw domain data (documents, logs,<br>articles, code, etc.)                             | Continued Pre-Training          | Pre-Trained     |
| Large-scale unstructured raw domain data (documents, logs,<br>articles, code, etc.)                             | Mid-Training                    | Pre-Trained     |
| Smaller volumes of unstructured raw data. Structured reasoning<br>traces / CoT data                             | Mid-Training                    | Mid-Trained     |
| Structured demonstrations (high-quality input-output pairs,<br>curated task instructions, multi-turn dialogues) | Full Fine-Tuning                | Mid-Trained     |
| Structured demonstrations (high-quality input-output pairs,<br>curated task instructions, multi-turn dialogues) | Parameter Efficient Fine-Tuning | Post-Trained    |

## Which checkpoint to use?

Partially pre-trained text only and fully pre-trained text only checkpoints
typically converge faster and require fewer training steps for domain adaptation.
However, they have no instruction tuning and would need to undergo post training
steps to be able to perform useful tasks and follow instructions. GA checkpoint may
require more steps to adapt but provides safer starting point for small-scale
experiments and will maintain some of it post training capabilities even after CPT
training.

In general, with large training datasets (>10B tokens), start from partially
pre-trained text only or fully pre-trained text only checkpoints for more efficient
and stable training, as the model's knowledge base will be substantially modified.
With small datasets (<10B tokens), use the GA checkpoint to preserve
instruction-following capabilities while adapting to the domain.

## How to use data mixing for 1.0 or 2.0

models?

When performing CPT with a new domain data, it is highly beneficial to mix the new
data with some of the data used previously in the pre-training stage of the model.
Mixing old data with new domain data solves two problems:

- Forgetting control: Prevents catastrophic forgetting by preserving
  existing skills and knowledge of the model. Without data mixing, training
  exclusively on narrow domain data causes the model to overwrite general
  capabilities. For example, a model trained only on legal documents might
  lose its ability to code or do math. Mixing the general domain datasets
  preserves these general skills while acquiring the new domain.
- Optimization stability: Maintains training stability by anchoring the
  model's internal representations. During CPT, the model's learned features
  are modified and data mixing provides gradients from diverse sources that
  guide this adaptation smoothly. Without it, training on narrow distributions
  can cause gradient instability, where the model's representations shift too
  drastically, leading to training divergence, loss spikes, or collapse of
  existing capabilities. This is the stability-plasticity tradeoff: the model
  should be plastic enough to learn new domain knowledge, but stable enough
  not to break what it already knows.

###### Nova CPT Data Mixing Capabilities

Access to Amazon Nova pre-training data and checkpoints is one of the core
offerings of the Amazon Nova CPT customization. Amazon Nova CPT customization enables easy
mixing of domain data with Amazon Nova's pre-training corpus. Further, the sampling
ratio of the specific Amazon Nova data categories (e.g., code, math, reasoning, etc)
can be changed and their proportions controlled to complement domain data. This
allows reinforcement of capabilities that align with the use case while adapting
the model to the specific domain.

###### Finding the Optimal Mixing Ratio

The optimal ratio of Amazon Nova data versus domain data depends on the dataset's
domain, complexity, size, quality, and the importance of maintaining general
capabilities. This ratio must be discovered through experimentation. An
experiment framework to decide on how much Amazon Nova data to mix is as
follows.

Select a representative subset of domain data (e.g., 5B tokens) and keep this
constant across all experimental runs.

Run small-scale CPT experiments varying only the amount of Amazon Nova data mixed
in:

- No mixing: 100% domain → 5B domain only (total 5B)
- Light mixing: 90% domain → 5B domain + ~0.56B Amazon Nova (total ~5.56B)
- Medium mixing: 70% domain → 5B domain + ~2.14B Amazon Nova (total
  ~7.14B)
- Heavy mixing: 50% domain → 5B domain + 5B Amazon Nova (total 10B)

Evaluate each checkpoint on in domain and general domain benchmarks. Also evaluate
the starting checkpoint (Amazon Nova checkpoint before any training).

- Does customer-domain performance stay roughly constant across runs? It
  usually should, since each run saw the same number of domain tokens. If
  domain performance improves with more mixing, Amazon Nova data provides useful
  regularization.
- Do general benchmark scores improve as mixing is increased?
  - Expected behavior is that the general capabilities should improve
    monotonically as more Amazon Nova data is added.
  - Measure multiple general benchmarks: MMLU (general knowledge),
    HumanEval (coding), GSM8K (math), or specific benchmarks of
    interest.

- Select the mixing ratio that maintains domain performance while delivering
  acceptable general capabilities for the use cases. Factor in the additional
  cost of training with more data mixing.

Once the optimal mixing ratio has been identified, run full-scale CPT using the
complete domain dataset with the selected mixing ratio.

###### Limitations

Current CPT only supports text data and does not support any customer multi-modal
datasets.
