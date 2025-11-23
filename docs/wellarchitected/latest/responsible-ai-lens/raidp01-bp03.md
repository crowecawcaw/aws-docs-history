# RAIDP01-BP03 Identify auxiliary datasets needed to operate your

system

Auxiliary data covers additional data that affects your system
behavior beyond the training, validation, and evaluation datasets,
such as knowledge bases used at inference time by RAG systems.
Identify auxiliary data sources that affect system behavior during
operation. Determine whether auxiliary datasets should be identical
between evaluation and deployment environments or if differences are
acceptable based on your use case requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Map auxiliary data sources your system uses during operation,
   like knowledge bases for retrieval, reference databases for
   fact checking, or real-time feeds for updates. Look at your
   system architecture to determine where additional data is
   pulled in and affects behavior. This assists you to see the
   complete data picture beyond just training datasets.
2. Find gaps where auxiliary data could fill coverage holes by
   analyzing what your training and evaluation data is missing.
   Check for underrepresented groups, missing domain knowledge,
   or outdated information. For example, if training data lacks
   recent events, you might need auxiliary news feeds.
3. Source auxiliary data that complements rather than duplicates
   your existing datasets by exploring databases, APIs, sensor
   feeds, and knowledge bases. Verify that auxiliary sources
   bring new perspectives or fill specific gaps instead of
   repeating patterns you already captured.
4. Plan to run tests on whether auxiliary datasets improve system
   capabilities using experiments comparing performance with and
   without the auxiliary data. Build simple tests showing whether
   auxiliary information assists with edge cases, accuracy, or
   underrepresented user groups.
5. Plan auxiliary data management by deciding which data should
   stay identical between testing and deployment versus which can
   differ. Build processes for updating auxiliary data when it
   becomes stale and create checks that verify datasets still
   match operational needs.

## Resources

**Related documents:**

- [An
  introduction to preparing your own dataset for LLM
  training](https://aws.amazon.com/blogs/machine-learning/an-introduction-to-preparing-your-own-dataset-for-llm-training/ "https://aws.amazon.com/blogs/machine-learning/an-introduction-to-preparing-your-own-dataset-for-llm-training/")
- [Prepare
  ML Data with Amazon SageMaker AI Data Wrangler](../../../sagemaker/latest/dg/data-wrangler.md "../../../sagemaker/latest/dg/data-wrangler.md")
- [What
  is RAG (Retrieval-Augmented Generation)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/ "https://aws.amazon.com/what-is/retrieval-augmented-generation/")
- [Build
  verifiable explainability into financial services workflows with Automated Reasoning checks for Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/build-verifiable-explainability-into-financial-services-workflows-with-automated-reasoning-checks-for-amazon-bedrock-guardrails/ "https://aws.amazon.com/blogs/machine-learning/build-verifiable-explainability-into-financial-services-workflows-with-automated-reasoning-checks-for-amazon-bedrock-guardrails/")
- [Revisiting
  the Auxiliary Data in Backdoor Purification](https://arxiv.org/html/2502.07231v1 "https://arxiv.org/html/2502.07231v1")
- [Learning
  to Group Auxiliary Datasets for Molecule](https://arxiv.org/pdf/2307.04052 "https://arxiv.org/pdf/2307.04052")
- [Unanswerability
  Evaluation for Retrieval Augmented Generation](https://arxiv.org/html/2412.12300v1 "https://arxiv.org/html/2412.12300v1")
- [Training a
  Helpful and Harmless Assistant with Reinforcement Learning
  from Human Feedback](https://arxiv.org/abs/2204.05862 "https://arxiv.org/abs/2204.05862")
- [AI
  Benchmarks and Datasets for LLM Evaluation](https://arxiv.org/html/2412.01020v1#S4 "https://arxiv.org/html/2412.01020v1#S4")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.4.3 Data Resources
