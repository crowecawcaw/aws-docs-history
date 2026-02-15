# Reinforcement Fine-Tuning (RFT) on SageMaker AI Hyperpod

Reinforcement Fine-Tuning (RFT) is a machine learning technique that improves model
performance through feedback signals—measurable scores or rewards indicating response
quality—rather than direct supervision with exact correct answers. Unlike traditional
supervised fine-tuning that learns from input-output pairs, RFT uses reward functions to
evaluate model responses and iteratively optimizes the model to maximize these rewards.

This approach is particularly effective for tasks where defining the exact correct output
is challenging, but you can reliably measure response quality. RFT enables models to learn
complex behaviors and preferences through trial and feedback, making it ideal for applications
requiring nuanced decision-making, creative problem-solving, or adherence to specific quality
criteria that can be programmatically evaluated.

###### When to use RFT

Use RFT when you can define clear, measurable success criteria but struggle to provide
exact correct outputs for training. It's ideal for tasks where quality is subjective or
multifaceted—such as creative writing, code optimization, or complex reasoning—where
multiple valid solutions exist but some are clearly better than others.

RFT works best when you have the following:

- A reliable reward function that can evaluate model outputs programmatically
- Need to align model behavior with specific preferences or constraints
- Situations where traditional supervised fine-tuning falls short because collecting
  high-quality labeled examples is expensive or impractical
  Consider RFT for applications requiring iterative improvement, personalization, or
  adherence to complex business rules that can be encoded as reward signals.

###### What RFT is best suited for

RFT excels in domains where output quality can be objectively measured but optimal
responses are difficult to define upfront:

- **Mathematical problem-solving**: Verifiable correctness
  with multiple solution paths
- **Code generation and optimization**: Testable execution
  results and performance metrics
- **Scientific reasoning tasks**: Logical consistency and
  factual accuracy
- **Structured data analysis**: Programmatically verifiable
  outputs
- **Multi-step reasoning**: Tasks requiring step-by-step
  logical progression
- **Tool usage and API calls**: Success measurable by
  execution results
- **Complex workflows**: Adherence to specific constraints
  and business rules
  RFT works exceptionally well when you need to balance multiple competing objectives like
  accuracy, efficiency, and style.

###### When to use reasoning mode for RFT training

Amazon Nova 2.0 supports reasoning mode during RFT training. The following modes are
available:

- **none**: No reasoning (omit the reasoning_effort
  field)
- **low**: Minimal reasoning overhead
- **high**: Maximum reasoning capability (default when
  reasoning_effort is specified)

###### Note

There is no medium option for RFT. If the reasoning_effort field is absent from your
configuration, reasoning is disabled.

Use high reasoning for the following:

- Complex analytical tasks
- Mathematical problem-solving
- Multi-step logical deduction
- Tasks where step-by-step thinking adds value
  Use none (omit reasoning_effort) or low reasoning for the following:

- Simple factual queries
- Direct classifications
- Speed and cost optimization
- Straightforward question-answering

###### Important

Higher reasoning modes increase training time and cost, inference latency and cost, but
also increase model capability for complex reasoning tasks.

###### Supported models

RFT onSageMaker AI Hyperpod supports Amazon Nova Lite 2.0 (amazon.nova-2-lite-v1:0:256k).

###### Major steps

The RFT process involves four key phases:

- **Implementing an evaluator**: Create a reward function
  to programmatically score model responses based on your quality criteria.
- **Uploading prompts**: Prepare and upload training data
  in the specified conversational format with reference data for evaluation.
- **Starting a job**: Launch the reinforcement fine-tuning
  process with your configured parameters.
- **Monitoring**: Track training progress through metrics
  dashboards to ensure the model learns effectively.
  Each step builds on the previous one, with the evaluator serving as the foundation that
  guides the entire training process by providing consistent feedback signals.

###### Topics

- [RFT on Nova 2.0](nova-hp-rft-nova2.md "nova-hp-rft-nova2.md")
