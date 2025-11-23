# RAIDP03-BP01 Address data that may be unsafe or inappropriate

for your use case

To perpetuate dataset safety throughout the AI system lifecycle,
establish definitions of safe and unsafe content for your use case.
Create specific criteria for content exclusion across training,
evaluation, and auxiliary datasets, considering both direct harms
and contextual inappropriateness. Implement automated and human
review filtering processes, with protective measures for reviewers.
Document safety definitions and filtering decisions and regularly
audit datasets to verify effective removal of unsafe content while
maintaining necessary testing scenarios.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Define what unsafe content looks like for your specific use
   case by creating objective definitions that align with your
   release criteria.
2. Consider implementing filters and other mechanisms to filter
   out potentially unsafe or inappropriate content. There may be
   scenarios where human review is appropriate and helpful in
   identifying problematic content that models might miss or
   misclassify. Depending on your use case, seek legal guidance
   about whether and how to build in processes to filter training
   data for illegal content such as known child sexual abuse
   material (CSAM) or adopt additional measures to mitigate risks
   related to CSAM and exploitative content.
3. Implement protection systems for dataset labelers. For
   example, set content warnings, exposure limits, and support
   Resources. Create rotation schedules and anonymous reporting
   channels for reviewer wellbeing.
4. Measure filtering effectiveness regularly. For example, track
   removal rates of unsafe content while verifying preservation
   of necessary test scenarios.
5. Document safety decisions you make to create an audit trail of
   what content gets filtered out and why, so you can explain
   your choices and improve your process over time.

## Resources

**Related documents:**

- [Flag
  harmful content using Amazon Comprehend toxicity
  detection](https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/ "https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/")
- [Trust
  and safety](../../../comprehend/latest/dg/trust-safety.md "../../../comprehend/latest/dg/trust-safety.md")
- [Automate
  media content filtering with AWS](https://aws.amazon.com/blogs/media/automate-media-content-filtering-with-aws/ "https://aws.amazon.com/blogs/media/automate-media-content-filtering-with-aws/")
- [Data-Centric
  Safety and Ethical Measures for Data and AI Governance](https://arxiv.org/pdf/2506.10217 "https://arxiv.org/pdf/2506.10217")
- [AEGIS2.0:
  A Diverse AI Safety Dataset and Risks Taxonomy for Alignment
  of LLM Guardrails](https://openreview.net/pdf?id=0MvGCv35wi "https://openreview.net/pdf?id=0MvGCv35wi")
- [BEAVERTAILS:
  Towards Improved Safety Alignment of LLM via a
  Human-Preference Dataset](https://papers.nips.cc/paper_files/paper/2023/file/4dbb61cb68671edc4ca3712d70083b9f-Paper-Datasets_and_Benchmarks.pdf "https://papers.nips.cc/paper_files/paper/2023/file/4dbb61cb68671edc4ca3712d70083b9f-Paper-Datasets_and_Benchmarks.pdf")
- [CISA
  AI Data Security Guidelines - Best Practices for Securing Data
  Used to Train & Operate AI Systems](https://media.defense.gov/2025/May/22/2003720601/-1/-1/0/CSI_AI_DATA_SECURITY.PDF "https://media.defense.gov/2025/May/22/2003720601/-1/-1/0/CSI_AI_DATA_SECURITY.PDF")
- [Training
  curriculum on AI and data protection Fundamentals of Secure AI
  Systems with Personal Data](https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf "https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf")
- [AI
  Privacy Risks & Mitigations - Large Language Models
  (LLMs)](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf "https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf")
- [Thorn
  Generative AI Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/ "https://www.thorn.org/blog/generative-ai-principles/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")A.7.2 Data for development and enhancement of
  AI system
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems
