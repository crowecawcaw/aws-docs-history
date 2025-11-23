# RAIRC03-BP08 Measure explainability of system behavior

Consider metrics for explainability based on user studies that
quantitatively measure stakeholders' ability to understand system
outputs, including their comprehension of confidence scores,
reasoning paths, and limitations, while also tracking the
effectiveness of provided explanations across different user groups
and expertise levels. This can include objective metrics (such as
task completion rates when acting on AI explanations) and subjective
assessments (like user satisfaction scores and trust ratings). Pay
particular attention to whether users can accurately identify when
to rely on or question the system's outputs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Create baseline measurement approaches that check whether
   users can correctly interpret what your system is telling them
   and why. Include the user groups from your RAIBR02 risk
   assessment who need to understand system outputs, and design
   simple comprehension tests for confidence scores, reasoning
   paths, and system limitations.
2. Design objective testing that measures how successfully users
   complete tasks when they rely on your system's explanations.
   Build tests that track task completion rates, decision
   accuracy, and time to completion when users act on AI
   explanations and when they work without them. Test across
   different expertise levels to see where your explanations
   assist users to make better decisions and where they might
   mislead people.
3. Build subjective assessment tools that capture user
   satisfaction, trust levels, and confidence in your system's
   explanations. Create simple rating scales and feedback
   collection methods that show whether users feel your
   explanations are helpful, trustworthy, and simple to
   understand. Track how these subjective measures vary across
   different user groups so you can spot where your explanations
   work well and where they fall short.
4. Test whether users can accurately judge when to trust or
   question your system's outputs by creating scenarios where the
   system should and shouldn't be trusted. Build measurement
   approaches that check if users correctly identify high
   confidence as compared to low confidence situations and
   whether they appropriately rely on or override system
   recommendations. This testing assists you to catch cases where
   users might over- or under-trust your system.

## Resources

**Related documents:**

- [Advanced
  tracing and evaluation of generative AI agents using LangChain
  and Amazon SageMaker AI AI MLFlow](https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/ "https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/")

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [AWS EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Amazon Simple Notification Service](https://aws.amazon.com/pm/sns/ "https://aws.amazon.com/pm/sns/")
