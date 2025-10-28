# Evaluating and comparing Amazon SageMaker JumpStart text classification models

SageMaker AI JumpStart offers multiple text classification models that categorize text into predefined classes. These models handle tasks such as sentiment analysis, topic classification, and content moderation. Choosing the right model for production requires careful evaluation using key metrics including accuracy, F1-score, and Matthews Correlation Coefficient (MCC).

In this guide, you:

- Deploy multiple text classification models (DistilBERT and BERT) from the JumpStart catalog.
- Run comprehensive evaluations across balanced, skewed, and challenging datasets.
- Interpret advanced metrics including Matthews Correlation Coefficient (MCC) and Area Under the Curve Receiver Operating Characteristic scores.
- Make data-driven model selection decisions using systematic comparison frameworks.
- Set up production deployments with auto-scaling and CloudWatch monitoring.
  Download the complete evaluation framework: [JumpStart Model Evaluation Package](samples/sagemaker-text-classification-evaluation-2.md "samples/sagemaker-text-classification-evaluation-2.md"). **The package includes pre-run results with sample outputs** so you can preview the evaluation process and metrics before deploying models yourself.

## Prerequisites

Before you begin, make sure that you have the following:

- [AWS account with SageMaker AI permissions](gs-set-up.md "gs-set-up.md").
- [SageMaker AI Amazon SageMaker Studio access](onboard-quick-start.md "onboard-quick-start.md").
- Basic Python knowledge.
- Understanding of text classification concepts.

Time and cost: 45 minutes total time. Costs vary based on instance types and usage duration - see [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") for current rates.

This tutorial includes step-by-step cleanup instructions to help you remove all resources and avoid ongoing charges.

###### Topics

- [Set up your evaluation environment](jumpstart-text-classification-setup.md "jumpstart-text-classification-setup.md")
- [Select and deploy text classification models](jumpstart-text-classification-deploy.md "jumpstart-text-classification-deploy.md")
- [Evaluate and compare model performance](jumpstart-text-classification-evaluate.md "jumpstart-text-classification-evaluate.md")
- [Interpret your results](jumpstart-text-classification-interpret.md "jumpstart-text-classification-interpret.md")
- [Deploy your model at scale](jumpstart-text-classification-scale.md "jumpstart-text-classification-scale.md")
