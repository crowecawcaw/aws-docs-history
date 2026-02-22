# Responsible AI Toolkit and content

moderation

## Responsible AI

Toolkit

Nova Forge provides a Responsible AI Toolkit that includes training and evaluation
data to align models to Amazon Nova's responsible AI guidelines during the training
process, and runtime controls to moderate model responses during inference.

**Training data** – Cases and scenarios emphasizing
responsible AI principles, safety considerations, and responsible technology
deployment are available for data mixing to align models responsibly during
continued pre-training.

**Evaluations** – Evaluations testing the model's
ability to detect and reject inappropriate, harmful, or incorrect content are
available as a benchmark task to determine the delta between base model performance
and custom model performance.

**Runtime controls** – By default, Amazon Nova's runtime
controls moderate model responses during inference. To modify these runtime
controls, request Amazon Nova's Customizable Content Moderation Settings by contacting an
Amazon Web Services account manager.

Safety is a shared responsibility between Amazon Web Services and its users. Changing the base
model or using continued pre-training to improve performance on a specific use case
can impact safety, fairness, and other properties of the new model. A robust
adaptation method minimizes changes to the safety, fairness, and other protections
built into base models while minimizing impact on model performance for tasks the
model was not customized for. End-to-end testing of applications on datasets
representative of use cases is required to determine if test results meet specific
expectations of safety, fairness, and other properties, as well as overall
effectiveness. For more information, see Amazon Web Services Responsible Use of AI Guide, Amazon Web Services
Responsible AI Policy, Amazon Web Services Acceptable Use Policy, and Amazon Web Services Service Terms.

## Customizable content

moderation

Customizable content moderation settings (CCMS) allow adjustment of controls
relevant to business requirements while maintaining essential, non-configurable
controls to ensure responsible use of AI.

These settings allow content generation through three available configurations:

- Security only
- Safety, sensitive content, and fairness combined
- All categories combined

The four content moderation categories are:

1. **Safety** – Covers dangerous activities,
   weapons, and controlled substances
2. **Sensitive content** – Includes profanity,
   nudity, and bullying
3. **Fairness** – Addresses bias and cultural
   considerations
4. **Security** – Involves cybercrime, malware,
   and malicious content

Regardless of your CCMS configuration, Amazon Nova enforces essential, non-configurable
controls to ensure responsible use of AI, such as controls to prevent harm to
children and preserve privacy.

When using CCMS, we recommend using Continued Pre-Training (CPT) and starting from a pre-RAI
alignment checkpoint (partially or fully pre-trained text-only) rather than the
fully-aligned production checkpoint. These checkpoints have not undergone safety
training or been steered toward specific RAI behaviors, allowing you to customize them more efficiently to your content moderation requirements.

###### Tip

When using CCMS with data mixing, consider adjusting the "rai" category percentage in your nova_data configuration to align with your specific content moderation requirements.

### Availability

CCMS is currently available for approved customers using:

- Amazon Nova Lite 1.0 and Pro 1.0 models
- Amazon Bedrock On-Demand inference
- The us-east-1 (N. Virginia) region

To enable CCMS for your Forge models, contact an Amazon Web Services account manager.
