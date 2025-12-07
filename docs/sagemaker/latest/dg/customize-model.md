# Customizing models with Amazon SageMaker AI

Amazon SageMaker AI model customization is a capability that transforms the traditionally complex and
time-consuming process of customizing AI models from a months-long endeavor into a
streamlined workflow that can be completed in days. This feature addresses the critical
challenge faced by AI developers who need to customize foundation models with proprietary
data to create highly differentiated customer experiences.

The capability includes a new guided user interface that understands natural language
requirements, with a comprehensive suite of advanced model customization techniques, all
powered by serverless infrastructure that eliminates the operational overhead of
managing compute resources. Whether you're building legal research applications,
enhancing customer service chatbots, or developing domain-specific AI agents, this
feature accelerates your path from proof-of-concept to production deployment.

Features in Model Customization powered by Amazon Bedrock Evaluations may securely transmit data
across AWS Regions within your geography for processing. For more information, access
[Amazon Bedrock Evaluations documentation](../../../bedrock/latest/userguide/evaluation-judge.md "../../../bedrock/latest/userguide/evaluation-judge.md").

## Key concepts

**Serverless training**

A fully managed compute infrastructure that abstracts away all infrastructure
complexity, allowing you to focus purely on model development. This includes
automatic provisioning of GPU instances (P5, P4de, P4d, G5) based on model size and
training requirements, pre-optimized training recipes that incorporate best
practices for each customization technique, real-time monitoring with live metrics
and logs accessible through the UI, and automatic cleanup of resources after
training completion to optimize costs.

**Model customization techniques**

Comprehensive set of advanced methods including supervised fine-tuning (SFT),
direct preference optimization (DPO), reinforcement learning with verifiable rewards
(RLVR), and reinforcement learning with AI feedback (RLAIF).

**Custom model**

A specialized version of a base foundation model that has been adapted to a
specific use case by training it on your own data, resulting in an AI model that
retains the general capabilities of the original foundation model while adding
domain-specific knowledge, terminology, style, or behavior tailored to your
requirements.

**AI model customization assets**

Resources and artifacts used to train, refine, and evaluate custom models during
the model customization process. These assets include **datasets**, which are collections of training examples
(prompt-response pairs, domain-specific text, or labeled data) used to fine-tune a
foundation model to learn specific behaviors, knowledge, or styles, and **evaluators**, which are mechanisms for assessing and
improving model performance through either **_reward functions_** (code-based logic that
scores model outputs based on specific criteria, used in RLVR training and custom
scorer evaluation) or **_reward
prompts_** (natural language instructions that guide an
LLM to judge the quality of model responses, used in RLAIF training and
LLM-as-a-judge evaluation).

**Model package group**

A collection container that tracks all logged models from training jobs, providing a
centralized location for model versions and their lineage.

**Logged model**

The output created by SageMaker AI when running serverless training jobs. This
can be a fine-tuned model (successful job), a checkpoint (failed job with checkpoint),
or associated metadata (failed job without checkpoint).

**Registered model**

A logged model that has been marked for formal tracking and governance purposes,
enabling full lineage and lifecycle management.

**Lineage**

The automatically captured relationships between training jobs, input datasets, output
models, evaluation jobs, and deployments across SageMaker AI and Amazon Bedrock.

**Cross-account sharing**

The ability to share models, datasets, and evaluators across AWS accounts using AWS
Resource Access Manager (RAM) while maintaining complete lineage visibility.
