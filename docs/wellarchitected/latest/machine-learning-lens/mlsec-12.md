# MLSEC-12: Restrict access to intended legitimate consumers

Use least-privileged permissions to invoke the deployed model
endpoint. For consumers who are external to the workload
environment, provide access via a secure API.

## Implementation plan

- **Use secure inference API
  endpoints** - Host the model so that a consumer
  of the model can perform inference against it securely.
  Enable consumers using the API to define the
  relationship, restrict access to the base model, and
  provide monitoring of model interactions.
- **Secure inference
  endpoints** - Only authorized parties should
  make inferences against the ML model. Treat inference
  endpoints as you would any other HTTPS API. Ensure that
  you follow guidance from the AWS Well-Architected
  Framework to provide network controls, such as
  restricting access to specific IP ranges, and bot
  control. The HTTPS requests for these API calls should
  be signed, so that the requester identity can be
  verified, and the requested data is protected in transit.

## Documents

- [Amazon SageMaker AI: Real-time Inference](../../../sagemaker/latest/dg/realtime-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints.md")
- [Give
  SageMaker AI Hosted Endpoints Access to Resources in Your
  Amazon VPC](../../../sagemaker/latest/dg/host-vpc.md "../../../sagemaker/latest/dg/host-vpc.md")
- [Register
  and Deploy Models with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")

## Blogs

- [Integrating
  machine learning models into your Java-based
  microservices](https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/ "https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/")
- [How
  Financial Institutions can use AWS to Address Regulatory
  Reporting](https://aws.amazon.com/blogs/architecture/how-banks-can-use-aws-to-meet-compliance/ "https://aws.amazon.com/blogs/architecture/how-banks-can-use-aws-to-meet-compliance/")
- [Secure
  deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/ "https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/")

## Videos

- [AWS re:Invent 2019: End-to-End machine learning using Spark
  and Amazon SageMaker AI](https://www.youtube.com/watch?v=FKgivdwzO5g "https://www.youtube.com/watch?v=FKgivdwzO5g")

## Examples

- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops "https://github.com/aws-samples/amazon-sagemaker-secure-mlops")
- [Accelerating
  Machine Learning Development with Data Science as a
  Service from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/ "https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/")
