# Continued pre-training (CPT)

Continued pre-training (CPT) is a training technique that extends the pre-training phase
of a foundation model by exposing it to additional unlabeled text from
specific domains or corpora. Unlike supervised fine-tuning, which requires labeled
input-output pairs, CPT trains on raw documents to help the model acquire deeper knowledge of
new domains, learn domain-specific terminology and writing patterns, and adapt to particular
content types or subject areas.

This approach is particularly valuable when you have large volumes (tens of billions of
tokens) of domain-specific text data, such as legal documents, medical literature, technical
documentation, or proprietary business content, and you want the model to develop native
fluency in that domain. Generally, after the CPT stage, the model needs to undergo additional
instruction tuning stages to enable the model to use the newly acquired knowledge and complete
useful tasks.

###### Supported models

CPT is available for the following Amazon Nova models:

- Nova 1.0 (Micro, Lite, Pro)
- Nova 2.0 (Lite)

Choose Nova 1.0 when the following applies:

- Your use case requires standard language understanding without advanced
  reasoning.
- You want to optimize for lower training and inference costs.
- Your focus is on teaching the model domain-specific knowledge and behaviors rather
  than complex reasoning tasks.
- You have already validated performance on Nova 1.0 and don't need additional
  capabilities.

###### Note

The larger model is not always better. Consider the cost-performance tradeoff and your
specific business requirements when selecting between Nova 1.0 and Nova 2.0 models.
