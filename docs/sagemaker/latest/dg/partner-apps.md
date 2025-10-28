# Amazon SageMaker Partner AI Apps overview

With Amazon SageMaker Partner AI Apps, users get access to generative AI and machine learning (ML) development
applications built, published, and distributed by industry-leading application
providers. Partner AI Apps are certified to run on SageMaker AI. With Partner AI Apps, users can accelerate and improve
how they build solutions based on foundation models (FM) and classic ML models without
compromising the security of their sensitive data. The data stays completely within their
trusted security configuration and is never shared with a third party. 

## How it works

Partner AI Apps are full application stacks that include an Amazon Elastic Kubernetes Service cluster and an array of
accompanying services that can include Application Load Balancer, Amazon Relational Database Service, Amazon Simple Storage Service buckets, Amazon Simple Queue Service queues,
and Redis caches.

These service applications can be shared across all users in a SageMaker AI domain and are
provisioned by an admin. After provisioning the application by purchasing a subscription
through the AWS Marketplace, the admin can give users in the SageMaker AI domain permissions to access the
Partner AI App directly from Amazon SageMaker Studio, Amazon SageMaker Unified Studio (preview), or using a pre-signed URL. For information
about launching an application from Studio, see [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").

Partner AI Apps offers the following benefits for administrators and users. 

- Administrators use the SageMaker AI console to browse, discover, select, and provision the
  Partner AI Apps for use by their data science and ML teams. After the Partner AI Apps are deployed, SageMaker AI
  runs them on service-managed AWS accounts. This significantly reduces the operational
  overhead associated with building and operating these applications, and contributes to the
  security and privacy of customer data.
- Data scientists and ML developers can access Partner AI Apps from within their ML development
  environment in Amazon SageMaker Studio or Amazon SageMaker Unified Studio (preview). They can use the Partner AI Apps to analyze their
  data, experiments, and models created on SageMaker AI. This minimizes context switching and helps
  accelerate building foundation models and bringing new generative AI capabilities to
  market.

## Integration with AWS services

Partner AI Apps uses the existing AWS Identity and Access Management (IAM) configuration for authorization and
authentication. As a result, users don’t need to provide separate credentials to access each
Partner AI App from Amazon SageMaker Studio. For more information about authorization and authentication with
Partner AI Apps, see [Set up Partner AI Apps](partner-app-onboard.md "partner-app-onboard.md").

Partner AI Apps also integrates with Amazon CloudWatch to provide operational monitoring and
management. Customers can also browse Partner AI Apps, and get details about them, such as features,
customer experience, and pricing, from the AWS Management Console. For
information about Amazon CloudWatch, see [How Amazon CloudWatch works](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.md").

Partner AI applications such as Deepchecks support integration with Amazon Bedrock to enable LLM-based evaluation features such as
"LLM as a judge" evaluations and automated annotation capabilities. When Amazon Bedrock integration is enabled,
the Partner AI App uses your customer-managed Amazon Bedrock account to access foundation models, ensuring that your
data remains within your trusted security configuration. For more information about configuring
Amazon Bedrock integration, see [Configure Amazon Bedrock integration](partner-app-onboard.md#partner-app-onboard-admin-bedrock "partner-app-onboard.md#partner-app-onboard-admin-bedrock").

## Supported types

Partner AI Apps support the following types:

- Comet
- Deepchecks
- Fiddler
- Lakera Guard

When the admin launches a Partner AI App, they must select the configuration of the instance cluster
that the Partner AI App is launched with. This configuration is known as the Partner AI App's tier. A Partner AI App's
tier can be one of the following values:

- `small`
- `medium`
- `large`

The following sections give information about each of the Partner AI App types, and details about the
Partner AI App's tier values.

Comet provides an end-to-end model evaluation platform for AI developers,
with LLM evaluations, experiment tracking, and production monitoring.

We recommend the following Partner AI App tiers based on the workload:

- `small` – Recommended for up to 5 users and 20 running jobs.
- `medium` – Recommended for up to 50 users and 100 running jobs.
- `large` – Recommended for up to 500 users and more than 100 running
  jobs.

###### Note

SageMaker AI does not support viewing the Comet UI as part of the output
of a Jupyter notebook.

AI application developers and stakeholders can use Deepchecks to continuously
validate LLM-based applications including characteristics, performance metrics, and
potential pitfalls throughout the entire lifecycle from pre-deployment and internal
experimentation to production.

We recommend the following Partner AI App tiers based on the speed desired for the workload:

- `small` – Processes 200 tokens per second.
- `medium` – Processes 500 tokens per second.
- `large` – Processes 1300 tokens per second.
  The Fiddler AI Observability Platform facilitates validating, monitoring, and
  analyzing ML models in production, including tabular, deep learning, computer vision, and
  natural language processing models.

We recommend the following Partner AI App tiers based on the speed desired for the workload:

- `small` – Processing 10MM events across 5 models, 100 features, and
  20 iterations takes about 53 minutes.
- `medium` – Processing 10MM events across 5 models, 100 features, and
  20 iterations takes about 23 minutes.
- `large` – Processing 10MM events across 5 models, 100 features, and
  100 iterations takes about 27 minutes.

Lakera Guard is a low-latency AI application firewall to secure generative
AI applications from gen AI-specific threats.

We recommend the following Partner AI App tiers based on the workload:

- `small` – Recommended for up to 20 Robotic Process Automations
  (RPAs).
- `medium` – Recommended for up to 100 RPAs.
- `large` – Recommended for up to 200 RPAs.
