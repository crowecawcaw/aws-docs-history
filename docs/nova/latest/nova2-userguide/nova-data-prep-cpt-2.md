# Preparing data for CPT on Amazon Nova 2

CPT on Amazon Nova 2 trains on raw text to help the model acquire deeper knowledge of specific domains, terminology, and writing patterns. This page describes the data format, supported features, constraints, and best practices for preparing CPT training data for Amazon Nova 2 models.

###### Tip

To validate your dataset format before starting a training job, see [Validation tools](nova-data-preparation.md#nova-data-validation-tools "nova-data-preparation.md#nova-data-validation-tools").

###### Topics

- [Data format](#nova-2-cpt-data-overview "#nova-2-cpt-data-overview")
- [Sample inputs](#nova-2-cpt-data-examples "#nova-2-cpt-data-examples")
- [Supported features](#nova-2-cpt-supported-features "#nova-2-cpt-supported-features")
- [General/Text understanding](#cpt-general-constraints "#cpt-general-constraints")
- [Preparing structured business datasets for CPT](#nova-cpt-2-structured-data "#nova-cpt-2-structured-data")
- [The way data is presented matters](#nova-cpt-2-data-presentation "#nova-cpt-2-data-presentation")
- [Packing samples for CPT](#nova-cpt-2-packing "#nova-cpt-2-packing")

## Data format

CPT training and validation datasets must be JSONL files, where each line is a JSON object containing a single `text` field with a string value. Text entries should contain naturally flowing, high-quality content that represents the target domain.

Required. A string containing the training content for this example.

```
{"text": "`training content`"}
```

###### Note

When using datamixing, run the first job with `max_steps=2`. This will help create optimizations in the cluster for data access and validate that all the datamixes are available.

## Sample inputs

The following shows a basic CPT JSONL dataset with multiple text samples:

```
{"text": "AWS stands for Amazon Web Services"}
{"text": "Amazon SageMaker is a fully managed machine learning service"}
{"text": "Amazon Bedrock is a fully managed service for foundation models"}
```

## Supported features

The following table summarizes feature support for CPT on Amazon Nova 2.

CPT feature support| Feature | CPT on Amazon Nova 2 |
| --- | --- |
| Text understanding | Supported on Nova 2.0 Lite. See [General/Text understanding](#cpt-general-constraints "#cpt-general-constraints"). |
| Image understanding | Not supported |
| Video understanding | Not supported |
| Document understanding | Not supported |
| Tool calling | Not supported |
| Reasoning | Not supported |

## General/Text understanding

This section summarizes the general constraints and best practices for preparing CPT on Amazon Nova 2 training data.

**Constraints**

General dataset constraints| Constraint | Details |
| --- | --- |
| Dataset format | JSONL (one JSON object per line) with a `text` string field. |
| Supported modalities | Text only |
| Recommended data volume | Tens of billions of tokens of domain-specific content for best results. |

**Best practices**

- Use naturally flowing, high-quality content that represents your target domain.
- Training data quality is the most crucial determining factor for the success of continuous pre-training. While CPT data is often described as "unlabeled," how data is structured, formatted, and presented determines whether the model will acquire the knowledge and skills required for your business use case.
- After CPT, plan to run additional instruction tuning (SFT or RFT) so the model can use the newly acquired knowledge to complete useful tasks.

**Sample input**

```
{"text": "AWS stands for Amazon Web Services"}
{"text": "Amazon SageMaker is a fully managed machine learning service"}
{"text": "Amazon Bedrock is a fully managed service for foundation models"}
```

## Preparing structured business datasets for CPT

Most businesses possess rich repositories of structured data: product catalogs, user profiles, transaction logs, form submissions, API calls, and operational metadata. At first glance, this looks very different from the unstructured web text typically used in standard pre-training.

To effectively learn from structured business data, think carefully about downstream tasks and design the data presentation to force the model to learn the right predictive relationships.

To unlock the full potential of continuous pre-training, consider:

- What tasks the model should perform at inference time
- What information is present in the raw data
- How to structure that data so the model learns to extract and manipulate the information correctly

Simply dumping structured data into training won't teach the model to reason about it. Actively shape the data presentation to guide what the model learns.

###### Structured data for CPT in the literature

CPT can pack domain facts into the model but often fails to make those facts retrievable and manipulable when inputs or tasks shift. Controlled experiments show that without diverse augmentation during pretraining, models memorize facts in brittle ways that remain hard to extract even after later instruction tuning, and they recommend injecting instruction like signals early in training. For semi structured data, randomized serialization and other augmentations reduce schema overfitting, which is why CPT should be interleaved with instruction style tasks rather than run first and IFT later. Finance focused work further finds that jointly mixing CPT and instruction data at batch time improves generalization and reduces forgetting versus the sequential recipe. Qwen technical report converges on the same pattern by integrating high quality instruction data into pretraining itself, which boosts in context learning and preserves instruction following while acquiring new domain knowledge.

Data augmentation for semi structured corpora is a key lever. Synthetic graph aware CPT expands small domain sets into entity linked corpora that explicitly teach relationships and compounds with retrieval at inference time. Joint CPT plus instruction mixing outperforms sequential pipelines in finance and balancing domain with general data lowers degradation on general skills. Very large scale domain CPT can also retain broad ability and even allow trade offs through model merging, yet still points to instruction tuning as an essential next step, reinforcing the value of introducing instruction signals during CPT.

###### Injecting diversity through randomization and shuffling

A general strategy that helps to teach model effectively from the structured and semi structured datasets is to shuffle the order of fields in the datasets, and even randomly drop out some keys.

Shuffling the fields forces the model to read what each value means instead of where it appears and learn the relationships between all the fields. For example, in case of an video game posted on amazon store, when "Title," "Platform," "Price," "Condition," and "Edition" arrive in different permutations, the model can't rely on "the third slot is platform"; it must bind labels to values and learn the bilateral relationships among attributes: title ⇄ platform, platform ⇄ price, condition ⇄ price. So it can, for example, infer a likely platform from a game name and an observed price, or estimate a plausible price range given a title and platform.

Randomly dropping keys during serialization acts like feature dropout: it prevents co-adaptation on any one field and forces the model to recover missing information from the remaining evidence. If "Platform" is absent, the model must pick it up from the title string or compatibility text; if "Price" is hidden, it has to triangulate from platform, edition, and condition. This builds symmetry (A→B and B→A), robustness to messy real-world listings, and schema invariance when fields are missing, renamed, or reordered.

A shopping-style example makes it concrete. Serialize the same item multiple ways—"Title: 'Elden Ring' | Platform: PlayStation 5 | Condition: Used—Like New | Price: $34.99" and a permutation like "Price: $34.99 | Title: 'Elden Ring' | Condition: Used—Like New | Platform: PlayStation 5"—and on some passes drop "Platform" while leaving "Compatible with PS5" in the description. Train complementary objectives such as predicting platform from {title, price} and predicting a price bucket from {title, platform}. Because order and even presence of keys vary, the only stable strategy is to learn the true relationships between attributes rather than memorize a template.

## The way data is presented matters

LLMs learn by predicting the next token from what they have already seen. The order of fields and events shown during training decides what the model can learn. If the training format matches the real task, the loss lands on the exact decision tokens. If fields are tossed together without structure, the model learns shortcuts or memorizes popularity and then fails when asked to choose among options.

Show the situation first, then the options, then the decision. If the model should also learn about outcomes or explanations, put them after the decision.

## Packing samples for CPT

###### What is packing?

Packing means filling each sequence window in the training data with multiple whole examples so the window is dense with real tokens, not padding.

###### Why it matters

During training, a maximum context length is set (for example, 8,192 tokens). Batches are shaped to [batch size × context length]. If a training example is shorter than the context length, the remaining positions are padded. Padding still runs through attention and MLP kernels even if loss is masked, so compute is paid for tokens that carry no learning signal.

###### How to do packing

To pack multiple samples, concatenate multiple training samples with a `[DOC]` separator between them (note the space before and after `[DOC]`), such that the full length stays within the desired context length.

An example packed document looks like this:

```
{"text": "training sample 1 [DOC] training sample 2 [DOC] training sample 3"}
```
