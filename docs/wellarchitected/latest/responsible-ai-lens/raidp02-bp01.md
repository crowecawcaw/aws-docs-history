# RAIDP02-BP01 Validate the representativeness of datasets for

the use case

Consider whether your datasets accurately reflect the real-world
conditions where your system will be used. Gather examples that
represent your users while filtering out data from contexts that
don't match your use case. This is especially relevant for
fine-tuning, alignment, and calibration sets, and for evaluation
sets since testing on unrepresentative data can make it seem that
your system works better (or worse) than it really does. Ask
yourself: "Does this dataset reflect how my system will be used
and exclude scenarios that are not part of my use case?"
Document what you've included and excluded so you know where your
results might not be sufficient.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Determine who will consistently use your system and how
   they'll use it by thinking through your real deployment
   scenario. Consider how users typically interact with systems
   like yours and what kinds of inputs they'll give you. This
   assists you to understand the representative data for your
   actual use case.
2. Check whether your datasets match real user inputs by
   comparing what's in your datasets against what you've
   documented about your use case context. Look for gaps where
   you're missing certain user groups, missing typical
   interaction styles, or including data from scenarios that
   don't match how your system could be used.
3. Clean up your datasets by removing examples that don't match
   your use case and adding examples that fill important gaps.
   Focus on your fine-tuning, alignment, calibration, and
   evaluation datasets since these directly affect how your
   system behaves and how accurately you can measure its
   performance.
4. Record what you included and excluded from your datasets, so
   the limitations are known. Keep track of which user groups or
   scenarios might not be well-covered so you understand your
   evaluation limitations.

## Resources

**Related documents:**

- [Training
  data labeling using humans with Amazon SageMaker Ground Truth](../../../sagemaker/latest/dg/sms.md "../../../sagemaker/latest/dg/sms.md")
- [Using
  Amazon Augmented AI for Human Review](../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md "../../../sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.md")
- [Data
  lineage in Amazon DataZone](../../../datazone/latest/userguide/datazone-data-lineage.md "../../../datazone/latest/userguide/datazone-data-lineage.md")
- [Dataset
  Representativeness and Downstream Task Fairness](https://arxiv.org/abs/2407.00170 "https://arxiv.org/abs/2407.00170")
- [NIST
  Towards a Standard for Identifying and Managing Bias in
  Artificial Intelligence](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf")
- [Policy
  advice and best practices on bias and fairness in AI](https://link.springer.com/article/10.1007/s10676-024-09746-w "https://link.springer.com/article/10.1007/s10676-024-09746-w")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems
