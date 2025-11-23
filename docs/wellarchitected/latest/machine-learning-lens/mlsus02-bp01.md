# MLSUS02-BP01 Consider AI services and pre-trained

models

Using AI services and pre-trained models can significantly reduce
the resources needed for machine learning workloads, enabling you to
quickly implement AI capabilities without developing custom models
from scratch.

**Desired outcome:** You identify
opportunities to use managed AI services or pre-trained models
instead of building custom models, reducing the environmental impact
of training and deploying ML solutions while accelerating time to
market. By using existing capabilities through APIs or fine-tuning
pre-trained models, you minimize computational resources required
for data preparation, model training, and deployment.

**Common anti-patterns:**

- Building custom models from scratch when suitable managed
  services already exist.
- Collecting and processing large datasets unnecessarily when
  pre-trained models could be utilized.
- Ignoring transfer learning opportunities that could reduce
  training time and computational resources.
- Overlooking model optimization techniques that could reduce
  inference resource requirements.

**Benefits of establishing this best
practice:**

- Reduced environmental impact through decreased computational
  resource usage.
- Lower operational costs for ML development and deployment.
- Faster time-to-market for ML-powered solutions.
- Access to state-of-the-art models without specialized ML
  expertise.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning solutions, evaluate whether you
truly need to build a custom model or if existing services and
pre-trained models can meet your requirements. Many common use
cases like image recognition, natural language processing, or
recommendation systems can use pre-built capabilities available
through APIs. These managed services handle the underlying
infrastructure, data processing, and model maintenance, reducing
both environmental impact and operational overhead.

If fully managed services don't meet your specific requirements,
consider starting with pre-trained models that you can fine-tune
with your data. This approach, known as transfer learning, allows
you to benefit from models that have already undergone
resource-intensive training on large datasets. By fine-tuning, you
can achieve similar or better performance than training from
scratch while using significantly fewer computational resources.

For example, instead of training a computer vision model from
scratch, you could use a pre-trained image recognition model from
Amazon Rekognition or fine-tune a model available through
SageMaker AI JumpStart with your specific images. This approach
reduces the carbon footprint associated with extensive model
training while delivering high-quality results.

### Implementation steps

1. **Assess your ML use case
   requirements**. Before developing an ML solution,
   clearly define your requirements and success criteria.
   Understand the specific problem you're trying to solve, the
   data you have available, and the performance metrics that
   matter for your application.
2. **Explore AWS AI services**.
   [AWS AI services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/") provide ready-to-use capabilities through
   APIs for common ML tasks. These services include
   [Amazon Rekognition](https://aws.amazon.com/rekognition/ "https://aws.amazon.com/rekognition/") for image and video analysis,
   [Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/") for natural language processing,
   [Amazon
   Forecast](https://aws.amazon.com/forecast/ "https://aws.amazon.com/forecast/") for time-series forecasting, and
   [Amazon Personalize](https://aws.amazon.com/personalize/ "https://aws.amazon.com/personalize/") for personalization and recommendations.
3. **Evaluate foundation models in Amazon
   Bedrock**.
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") provides serverless access to leading
   foundation models from AI companies like Anthropic, Cohere,
   AI21 Labs, and Amazon's own Nova models through a single
   API. These models can handle tasks like text generation,
   summarization, chatbots, and content creation without
   requiring model training.
4. **Explore pre-trained models from AWS Marketplace**.
   [AWS Marketplace](https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1 "https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1") offers over 1,400 ML-related assets that
   you can subscribe to, including pre-trained models for
   various industry-specific use cases that can be deployed
   with minimal configuration.
5. **Leverage SageMaker AI
   JumpStart**.
   [SageMaker AI
   JumpStart](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md") provides pre-trained, open-source models
   for a wide range of problem types to get started with
   machine learning. You can incrementally train and fine-tune
   these models before deployment, reducing the computational
   resources needed compared to training from scratch.
6. **Consider Hugging Face
   models**.
   [Hugging
   Face with Amazon SageMaker AI](../../../sagemaker/latest/dg/hugging-face.md "../../../sagemaker/latest/dg/hugging-face.md") enables you to use
   thousands of pre-trained transformer models for NLP,
   computer vision, and audio tasks. These models can be
   fine-tuned with your specific data to achieve high-quality
   results with minimal training.
7. **Implement efficient fine-tuning
   techniques**. When customizing pre-trained models,
   use efficient fine-tuning methods like parameter-efficient
   fine-tuning (PEFT), low-rank adaptation (LoRA), or
   quantization to minimize computational resources while
   maintaining performance.
8. **Monitor resource usage and
   optimize**. After deploying your solution,
   continuously monitor its resource consumption and
   performance. Look for opportunities to optimize through
   model compression, quantization, or pruning to further
   reduce computational requirements.
9. **Leverage expanded pre-trained model
   libraries**. Use the expanded
   [SageMaker AI
   JumpStart](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md") catalog which now includes broader
   selection of pre-trained models and industry-specific
   solutions, reducing the need for custom model development
   and associated computational resources.
10. **For generative AI workloads,
    implement retrieval-augmented generation (RAG)**.
    For generative AI applications requiring domain-specific
    knowledge, consider using
    [retrieval-augmented
    generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/ "https://aws.amazon.com/what-is/retrieval-augmented-generation/") with SageMaker AI JumpStart foundation models
    instead of fine-tuning large models, which can significantly
    reduce computational resources while improving accuracy.

## Resources

**Related documents:**

- [AWS AI Services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/")
- [SageMaker AI
  JumpStart pretrained models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
- [Choose
  the best data source for your Amazon SageMaker AI training
  job](https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/ "https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/")
- [Pre-trained
  machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models "https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models")
- [Resources
  for using Hugging Face with Amazon SageMaker AI](../../../sagemaker/latest/dg/hugging-face.md "../../../sagemaker/latest/dg/hugging-face.md")
- [Optimize
  AI/ML workloads for sustainability: Part 2, model
  development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/")
