# Machine learning for healthcare

Artificial intelligence/machine learning (AI/ML) is being applied
to a growing set of problems across healthcare, such as
prioritizing treatments, predicting health outcomes, guiding
provider workflows, and streamlining revenue cycle operations. A
key strength of AI/ML technology is the ability to continually
learn from real-world data and improve performance over time.
However, healthcare applications of AI/ML pose unique problems,
including regulatory oversight, design control obligations, and
interpretability requirements imposed by stakeholders. Machine
learning development is often performed in concert with
traditional analytics and can leverage elements of the
infrastructure described in the [Healthcare analytics](healthcare-analytics.md "healthcare-analytics.md") scenario.

Characteristics of machine learning for healthcare architectures
include:

- Data for training models is commonly extracted from production
  systems within payer and provider organizations, such as EHRs,
  medical imaging systems, claims and revenue cycle solutions,
  scanned or faxed documents, biobanks, and genomics data
  stores. Healthcare tends to be high dimensional, multi-modal,
  and often suffers from missingness due to the episodic nature
  of care resource consumption.
- Data lakes are well suited to landing, preparing, and storing
  health datasets for ML. The traditional data silos of
  healthcare data can hamper training models that perform well.
  Extracting data from multiple systems and data modalities can
  improve model performance and transferability between
  settings.
- Healthcare analytics tools may be used for exploratory data
  analysis before machine learning development.
- Data is commonly extracted in bulk, cleaned, and prepared for
  use training models. Data for inferencing may also be
  processed in batches, or in real-time using streaming data
  integrations such as HL7 v2, FHIR, or other interoperability
  standards. Data lineage should be tracked, providing a map of
  various data sources and transformation steps that the data
  flows through.
- Organizations may use identifiable health data for ML
  development. In such cases, organizations must adhere to the
  principle of least access, protecting health data from
  inappropriate access while enabling data scientists to run ML
  workflows. De-identifying health data before making it
  accessible to ML teams can mitigate privacy and security
  concerns.
- Federated Learning (FL) may be adopted to facilitate
  multi-centric, collaborative ML modeling when data privacy and
  anonymity is required. Federated paradigm has been proven to
  be domain-agnostic and framework independent for distributed
  modeling training. The heterogeneous datasets from diverse
  sources and patient populations are desired to build a robust
  and accurate ML model. To overcome the privacy concern and
  complex data sharing process, FL in healthcare can be used to
  rapidly and securely develop new ML models without data
  ownership hurdles.
- Stakeholders may require explainability and repeatability of
  models employed in healthcare, especially in care delivery and
  revenue cycle use cases. Validating a model may require that
  structure and output of the model have _face
  validity_ and align with medical knowledge.
- Thresholds of acceptable model performance may follow from the
  risks and benefits of the outcome modeled. For example, if the
  outcome being modeled is high risk to patients or high cost,
  then stakeholders may demand that models display high
  [precision](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall")
  (confidence in a positive prediction). Alternatively, if the
  model is used for a low risk, low cost, yet high benefit,
  stakeholders may prioritize higher
  [recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall")
  from models.
- Model deployments should be automated with pipelines to
  minimize human touchpoints, deploy data integration workloads
  consistently and repeatedly, and formalize how code is
  promoted from development to production.
- Healthcare AI/ML models often need to be integrated in the
  workflows of healthcare providers, patients, and other actors
  to have utility. This may require integrating systems (such as
  an EHR), updating workflows, and retraining providers. It may
  also require integration with medical equipment and require
  regulatory oversight.
- Model performance should be monitored after deployment in
  production. The complexity and variability of health data
  makes it especially important to monitor the health of
  inferencing pipelines.

## Machine learning resources

Refer to the following resources to learn more about our best
practices for machine learning.

**Documentation and blogs**

- [AWS Config and Best Practices for AI and ML](../../../config/latest/developerguide/operational-best-practices-for-AI-and-ML.md "../../../config/latest/developerguide/operational-best-practices-for-AI-and-ML.md")
- [Model
  Explainability with AWS Artificial Intelligence and Machine
  Learning Solutions](https://aws.amazon.com/blogs/machine-learning/whitepaper-machine-learning-best-practices-in-healthcare-and-life-sciences/ "https://aws.amazon.com/blogs/machine-learning/whitepaper-machine-learning-best-practices-in-healthcare-and-life-sciences/")
- [Detect
  machine learning (ML) model drift in production
  (video)](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

**Whitepapers**

- [Machine
  Learning Best Practices in Healthcare and Life
  Sciences](https://aws.amazon.com/blogs/machine-learning/whitepaper-machine-learning-best-practices-in-healthcare-and-life-sciences/ "https://aws.amazon.com/blogs/machine-learning/whitepaper-machine-learning-best-practices-in-healthcare-and-life-sciences/")
- [Model
  Explainability with AWS Artificial Intelligence and Machine
  Learning Solutions](../../../whitepapers/latest/model-explainability-aws-ai-ml/model-explainability-aws-ai-ml.md "../../../whitepapers/latest/model-explainability-aws-ai-ml/model-explainability-aws-ai-ml.md")
