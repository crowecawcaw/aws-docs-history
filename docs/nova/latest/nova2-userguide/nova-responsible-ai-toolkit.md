# Responsible AI Toolkit and content

moderation

## Responsible AI

toolkit

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
AWS account manager.

Safety is a shared responsibility between AWS and its users. Changing the base
model or using continued pre-training to improve performance on a specific use case
can impact safety, fairness, and other properties of the new model. A robust
adaptation method minimizes changes to the safety, fairness, and other protections
built into base models while minimizing impact on model performance for tasks the
model was not customized for. End-to-end testing of applications on datasets
representative of use cases is required to determine if test results meet specific
expectations of safety, fairness, and other properties, as well as overall
effectiveness. For more information, see Amazon Web Services Responsible Use of AI Guide, Amazon Web Services
Responsible AI Policy, Amazon Web Services Acceptable Use Policy, and Amazon Web Services Service Terms.
