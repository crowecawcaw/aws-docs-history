# MLREL-01: Use APIs to abstract change from model consuming applications

Use a flexible application and API design to abstract change from
model consuming applications. Ensure that changes to an ML model
are introduced with minimal or no interruption to existing
workload capabilities. Minimize the changes across other
downstream applications.

## Implementation plan

- **Adopt best practices in use of
  APIs** -Expose your ML endpoints through APIs so
  that changes to the model can be introduced without
  disrupting upstream communications. Document your API in a
  central repository or documentation site so that any
  calling services can easily understand your API routes and
  flags. Ensure that any changes to your API are communicated
  with any calling services.
- **Deploy a model in Amazon SageMaker AI**- After you train your model, you can
  deploy it using
  [Amazon](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")
  [SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")
  to get predictions. To establish a persistent endpoint to
  get one prediction at a time, use SageMaker AI hosting
  services. To get predictions for an entire dataset, use
  SageMaker AI batch transform.
- **Use Amazon API Gateway to create
  APIs** -
  [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") is a fully managed service that enables
  developers to create, publish, maintain, monitor, and
  secure APIs. Using API Gateway, you can create RESTful
  APIs and WebSocket APIs that enable real-time two-way
  communication applications. API Gateway supports
  containerized and serverless workloads, as well as web
  applications.

## Documents

- [Deploy
  a Model in Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-deployment.md "../../../sagemaker/latest/dg/how-it-works-deployment.md")
- [What
  is Amazon API Gateway?](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md")
- [API Gateway Pattern](../../../prescriptive-guidance/latest/modernization-integrating-microservices/api-gateway-pattern.md "../../../prescriptive-guidance/latest/modernization-integrating-microservices/api-gateway-pattern.md")

## Blogs

- [Build
  a serverless frontend for an Amazon SageMaker AI
  endpoint](https://aws.amazon.com/blogs/machine-learning/build-a-serverless-frontend-for-an-amazon-sagemaker-endpoint/ "https://aws.amazon.com/blogs/machine-learning/build-a-serverless-frontend-for-an-amazon-sagemaker-endpoint/")
- [Creating
  a machine learning-powered REST API with Amazon API Gateway mapping templates and](https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker "https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker")
  [Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker "https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker")
- [Deploying
  machine learning models with serverless templates](https://aws.amazon.com/blogs/compute/deploying-machine-learning-models-with-serverless-templates/ "https://aws.amazon.com/blogs/compute/deploying-machine-learning-models-with-serverless-templates/")

## Videos

- [Deploy
  Your ML Models to Production at Scale with Amazon SageMaker AI](https://www.youtube.com/watch?v=KFuc2KWrTHs "https://www.youtube.com/watch?v=KFuc2KWrTHs")

## Examples

- [AWS Solutions Constructs aws-apigateway-sagemaker
  endpoint](../../../solutions/latest/constructs/aws-apigateway-sagemakerendpoint.md "../../../solutions/latest/constructs/aws-apigateway-sagemakerendpoint.md")
- [AWS MLOps Framework](https://aws.amazon.com/solutions/implementations/aws-mlops-framework/?did=sl_card&trk=sl_card "https://aws.amazon.com/solutions/implementations/aws-mlops-framework/?did=sl_card&trk=sl_card")
- [Amazon SageMaker AI Safe Deployment Pipeline](https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline "https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline")
- [Amazon SageMaker AI Inference Client Application](https://github.com/aws-samples/amazon-sagemaker-inference-client "https://github.com/aws-samples/amazon-sagemaker-inference-client")
