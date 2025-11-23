# MLREL01-BP01 Use APIs to abstract change from model consuming

applications

APIs abstract changes from model-consuming applications, keeping
machine learning solutions flexible and resilient. Establishing an
abstraction layer between ML models and consuming applications
enables model updates, replacements, or enhancements without
disrupting existing workloads.

**Desired outcome:** You have a
flexible application and API design that isolates machine learning
model implementations from consuming applications. You make changes
to ML models with minimal or no disruption to existing applications.
Your ML endpoints are well-documented and accessible, and changes to
underlying models do not require extensive modifications to
downstream applications.

**Common anti-patterns:**

- Directly embedding model code within applications.
- Hardcoding model versions or parameter specifications in client
  applications.
- Lacking proper API documentation and version control.
- Designing rigid interfaces that break when model inputs or
  outputs change.
- Creating tight coupling between ML models and consuming
  applications.

**Benefits of establishing this best
practice:**

- Reduces downtime when updating or replacing ML models.
- Simplifies model deployment and versioning processes.
- Increases agility and flexibility when evolving ML capabilities.
- Lowers maintenance costs for applications using ML models.
- Enhances ability to A/B test different model versions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Abstracting changes from model-consuming applications requires
thoughtful API design and implementation. Create a well-designed
API layer between ML models and applications so that you can make
modifications to models without disrupting services. This approach
involves developing stable interfaces that hide underlying
complexity and implementation details of ML models.

When designing these APIs, focus on creating contracts that are
flexible enough to accommodate model evolution while maintaining
backward compatibility. Document APIs thoroughly so developers
consuming models understand how to interact with them correctly.
Consider implementing versioning strategies that allow introducing
new model capabilities while supporting existing clients.

### Implementation steps

1. **Adopt best practices in API
   design**. Expose ML endpoints through APIs so
   changes to the model can be introduced without disrupting
   upstream communications. Create a well-designed API contract
   that focuses on business capabilities rather than technical
   implementation details. Document your API in a central
   repository or documentation site so calling services can
   understand API routes and flags. Communicate changes to your
   API with calling services.
2. **Implement API versioning**.
   Use versioning strategies for APIs to enable backward
   compatibility while supporting new features. Consider using
   URL path versioning (for example,
   /v1/predict), header-based versioning, or
   query parameter versioning depending on organizational
   standards. This allows introducing new model versions
   without breaking existing client applications.
3. **Deploy models in Amazon SageMaker AI**. After training your model, deploy it
   using
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to get predictions. To establish a
   persistent endpoint for one prediction at a time, use
   SageMaker AI hosting services. For predictions on entire
   datasets, use SageMaker AI batch transform. SageMaker AI provides
   flexibility in deployment options, including
   [multi-model
   endpoints](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md"),
   [serverless
   inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md"), and
   [asynchronous
   inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md").
4. **Use Amazon API Gateway to create
   APIs**.
   [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") is a fully managed service that enables
   developers to create, publish, maintain, monitor, and secure
   APIs. Using API Gateway, you can create RESTful APIs and
   WebSocket APIs that enable real-time two-way communication
   applications. API Gateway supports containerized and
   serverless workloads, as well as web applications.
5. **Implement request and response
   transformations**. Use API Gateway's mapping
   templates to transform client requests to match your model's
   input format and transform model responses to maintain a
   consistent API contract. This allows changing model
   implementations without requiring client applications to
   change how they format requests or interpret responses.
6. **Add caching and
   throttling**. Configure API Gateway's caching
   capability to improve performance and reduce costs for
   frequently accessed predictions. Implement throttling to
   protect ML endpoints from traffic spikes and provide
   consistent performance. Use
   [SageMaker AI
   Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") to optimize endpoint
   configurations for optimal latency and cost performance.
7. **Monitor and analyze API
   usage**. Set up monitoring and logging for APIs to
   understand how they are being used and identify potential
   issues. Use
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") metrics and logs to track API performance,
   errors, and usage patterns. This data can optimize ML
   endpoints and identify opportunities for improvement.
8. **Consider inference components for
   shared endpoints**. Use
   [SageMaker AI
   inference components](../../../sagemaker/latest/dg/realtime-endpoints-deploy-models.md "../../../sagemaker/latest/dg/realtime-endpoints-deploy-models.md") to deploy multiple models to
   shared endpoints, improving resource utilization and
   reducing costs while maintaining API abstraction.

## Resources

**Related documents:**

- [Model
  deployment options in Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-deployment.md "../../../sagemaker/latest/dg/how-it-works-deployment.md")
- [What
  is Amazon API Gateway?](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md")
- [Real-time
  inference](../../../sagemaker/latest/dg/realtime-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints.md")
- [Multi-model
  endpoints](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Asynchronous
  inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")
- [Deploying
  ML models using SageMaker AI Serverless Inference](https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/ "https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/")
- [Optimize
  deployment cost of Amazon SageMaker AI JumpStart foundation
  models with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/ "https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/")

**Related videos:**

- [Amazon
  Sagemaker Serverless Inference](https://www.youtube.com/watch?v=esG_Q8egwMU "https://www.youtube.com/watch?v=esG_Q8egwMU")

**Related examples:**

- [Amazon SageMaker AI Examples Repository](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples")
- [Amazon SageMaker AI MLOps Workshop](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop "https://github.com/aws-samples/amazon-sagemaker-mlops-workshop")
