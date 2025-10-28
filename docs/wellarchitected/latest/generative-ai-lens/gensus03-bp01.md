# GENSUS03-BP01 Leverage smaller models to reduce carbon

footprint

To manage computational demands and costs of deploying large
language models, implement model optimization techniques. This best
practice aims to increase AI operational efficiency by reducing
resource consumption while meeting performance goals. Strategies
like quantization, pruning, and model distillation help lower
operational expenses, improve response times, and promote
environmental sustainability. This approach enables you to deploy
efficient, cost-effective, and eco-friendly AI solutions, allowing
for application scaling without excessive costs or environmental
impact.

**Desired outcome:** After
implementing model optimization practices, you will have
cost-effective and carbon-effective AI solutions.

**Benefits of establishing this best
practice:**
[Optimize
resource utilization](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md") - Minimize environmental impact by
maximizing the efficiency of generative AI resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To effectively reduce the computational requirements of generative
AI models without compromising performance, it is essential to
implement a combination of optimization techniques such as
quantization, pruning, and the adoption of efficient model
architectures. Quantization involves reducing the precision of the
numbers used to represent the model's weights and activations.
This technique can decrease the model size and speed up inference
times with minimal impact on performance. Pruning, on the other
hand, involves removing redundant or unnecessary parameters from
the model. By identifying and alleviating weights that contribute
little to the model's predictions, pruning can lead to more
compact and efficient models.

In addition to these techniques, leveraging efficient model
architectures specifically designed for reduced computational
requirements can further enhance performance. Instead of relying
on large, general-purpose models, fine-tuning smaller models
tailored to specific use cases can often yield comparable results
with less computational resources. This approach allows for more
targeted optimization and can lead to more efficient deployments.

Amazon Bedrock supports this through its model distillation
feature. Model distillation involves training a smaller, more
efficient model to mimic the performance of a larger, more complex
model. This process results in a distilled model that maintains
similar performance levels while requiring fewer resources. By
utilizing such techniques, organizations can reduce computational
costs, making generative AI more accessible and scalable for a
wider range of applications.

With Amazon SageMaker AI, you can improve the performance of your
generative AI models by applying inference optimization techniques
to attain lower resource utilization and costs. Choose which of
the supported optimization techniques to apply, including
quantization, speculative decoding, and compilation. After your
model is optimized, you can run an evaluation to see performance
metrics for latency, throughput, and price.

### Implementation steps

1. Select optimization techniques.
   - Evaluate considerations between model size, speed, and
     accuracy. Evaluate the effect on tasks and overall
     performance
   - Use SageMaker AI inference optimization techniques like LoRa
     and quantization
   - Use Amazon Bedrock Model Distillation feature to knowledge
     transfer from a larger model to a smaller model

2. Evaluate optimized models.
   - Compare performance with original models
   - Assess resource savings and verify accuracy and
     functionality taking edge cases into considerations

## Resources

**Related practices:**

- [SUS02-BP01](../framework/sus_sus_user_a2.md "../framework/sus_sus_user_a2.md")
- [SUS05-BP02](../framework/sus_sus_hardware_a3.md "../framework/sus_sus_hardware_a3.md")
- [SUS02-BP03](../sustainability-pillar/sus_sus_user_a4.md "../sustainability-pillar/sus_sus_user_a4.md")

**Related guides, videos, and documentation:**

- [A
  guide to Amazon BedrockModel Distillation (preview)](https://aws.amazon.com/blogs/machine-learning/a-guide-to-amazon-bedrock-model-distillation-preview/ "https://aws.amazon.com/blogs/machine-learning/a-guide-to-amazon-bedrock-model-distillation-preview/")
- [Fine-tune
  large language models with Amazon SageMaker AI Autopilot](https://aws.amazon.com/blogs/machine-learning/fine-tune-large-language-models-with-amazon-sagemaker-autopilot/ "https://aws.amazon.com/blogs/machine-learning/fine-tune-large-language-models-with-amazon-sagemaker-autopilot/")
- [Inference
  optimization for Amazon SageMaker AI models](../../../sagemaker/latest/dg/model-optimize.md "../../../sagemaker/latest/dg/model-optimize.md")
- [Quantum-amenable
  pruning of large language models and large vision models using
  block coordinate descent](https://aws.amazon.com/blogs/quantum-computing/quantum-amenable-pruning-of-large-language-models-and-large-vision-models-using-block-coordinate-descent/ "https://aws.amazon.com/blogs/quantum-computing/quantum-amenable-pruning-of-large-language-models-and-large-vision-models-using-block-coordinate-descent/")
- [Improve
  the relevance of query responses with a reranked model in
  Amazon Bedrock](../../../bedrock/latest/userguide/rerank.md "../../../bedrock/latest/userguide/rerank.md")

**Related examples:**

- [LLM
  Rank pruning](https://github.com/amazon-science/llm-rank-pruning "https://github.com/amazon-science/llm-rank-pruning")
- [Optimizing
  Generative AI LLM Inference Deployment on AWS GPUs By
  Leveraging Quantization](https://github.com/aws-samples/optimizing-llm-inference-with-quantization "https://github.com/aws-samples/optimizing-llm-inference-with-quantization")
- [Amazon SageMaker AI inference optimization toolkit for generative AI
  using quantization](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-launches-the-updated-inference-optimization-toolkit-for-generative-ai/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-launches-the-updated-inference-optimization-toolkit-for-generative-ai/")

**Related tools:**

- [Amazon Bedrock](https://aws.amazon.com/bedrock/?nc2=type_a "https://aws.amazon.com/bedrock/?nc2=type_a")
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/ "https://aws.amazon.com/sagemaker-ai/")
- [AWSCloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
