# Nova Forge access and setup for SageMaker AI Hyperpod

## Responsible AI Toolkit and Content Moderation

**Content moderation settings**: Amazon Nova Forge customers have access to Customizable Content Moderation Settings (CCMS) for Amazon Nova Lite 1.0 and Pro 1.0 models. CCMS allows you to adjust content moderation controls to align with your specific business requirements while maintaining essential responsible AI safeguards. To determine if your business use case qualifies for CCMS, contact your Amazon Web Services account manager.

Nova Forge provides a Responsible AI toolkit that includes training data, evaluation benchmarks, and runtime controls to help you align your models with Nova's responsible AI guidelines.

**Training data**: The "RAI" category in data mixing contains cases and scenarios emphasizing responsible AI principles, safety considerations, and responsible technology deployment. Use these to align your models responsibly during continued pre-training.

**Evaluations**: Benchmark tasks are available to test your model's ability to detect and reject inappropriate, harmful, or incorrect content. Use these evaluations to measure the difference between base model performance and your custom model performance.

**Runtime controls**: By default, Nova's runtime controls moderate model responses during inference. To modify these controls for your specific business case, request Customizable Content Moderation Settings (CCMS) by contacting your Amazon Web Services account manager.

### Shared Responsibility for Safety

Safety is a shared responsibility between Amazon Web Services and our customers. Changing the base model or using continued pre-training to improve performance on a specific use case can impact safety, fairness, and other properties of the new model.

We use a robust adaptation method to minimize changes to the safety, fairness, and other protections built into our base models while minimizing impact on model performance for tasks the model was not customized for.

You are responsible for:

- End-to-end testing of their applications on datasets representative of their use cases
- Deciding if test results meet their specific expectations of safety, fairness, and other properties, as well as overall effectiveness

For more information, see the Amazon Web Services Responsible Use of AI Guide, Amazon Web Services Responsible AI Policy, AWS Acceptable Use Policy, and AWS Service Terms for the services you plan to use.

### Customizable Content Moderation Settings (CCMS)

CCMS allows you to adjust controls relevant to your business requirements while maintaining essential, non-configurable controls that ensure responsible use of AI.

These settings allow content generation through three available configurations:

- Security only
- Safety, sensitive content, and fairness combined
- All categories combined

The four content moderation categories are:

1. **Safety** – Covers dangerous activities, weapons, and controlled substances
2. **Sensitive content** – Includes profanity, nudity, and bullying
3. **Fairness** – Addresses bias and cultural considerations
4. **Security** – Involves cybercrime, malware, and malicious content

Regardless of your CCMS configuration, Amazon Amazon Nova enforces essential, non-configurable controls to ensure responsible use of AI, such as controls to prevent harm to children and preserve privacy.

#### Recommendations for Using CCMS

When using CCMS, we recommend using Continuous Pre Training (CPT) and starting from a pre-RAI alignment checkpoint (PRE-TRAINING-Early, PRE-TRAINING-Mid, or PRE-TRAINING-Final) rather than the GA/FINAL checkpoint. These checkpoints have not undergone safety training or been steered toward specific RAI behaviors, allowing you to customize them more efficiently to your content moderation requirements.

**Tip**: When using CCMS with data mixing, consider adjusting the "rai" category percentage in your nova_data configuration to align with your specific content moderation requirements.

#### Availability

CCMS is currently available for approved customers using:

- Nova Lite 1.0 and Pro 1.0 models
- Amazon Bedrock On-Demand inference
- The us-east-1 (N. Virginia) region

To enable CCMS for your Forge models, contact your Amazon Web Services account manager.
