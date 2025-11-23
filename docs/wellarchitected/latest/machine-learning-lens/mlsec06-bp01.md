# MLSEC06-BP01 Restrict access to intended legitimate

consumers

Use least privilege permissions to invoke the deployed model
endpoint. For consumers who are external to the workload
environment, provide access using a secure API.

**Desired outcome:** You establish
secure inference API endpoints that allow only authorized parties to
access your ML models. You create a controlled environment where
model access is restricted based on legitimate business needs, while
maintaining monitoring capabilities to track interactions with your
models. Your ML endpoints are protected using the same security
principles applied to other HTTPS APIs, providing data protection in
transit and proper authentication.

**Common anti-patterns:**

- Allowing public access to model endpoints without proper
  authentication.
- Using overly permissive IAM roles for model endpoint access.
- Failing to implement network controls for inference endpoints.
- Not monitoring or logging model inference activities.
- Using the same credentials for development and production model
  access.

**Benefits of establishing this best
practice:**

- Reduced risk of unauthorized model access and potential data
  exfiltration.
- Enhanced control over who can use your ML models and when.
- Improved monitoring and auditability of model usage.
- Protection of intellectual property embedded in models.
- Improves adherence to regulatory requirements for data security.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing your ML model endpoints is critical to protect both your
intellectual property and the data processed by these models. By
treating ML inference endpoints with the same security rigor as
other HTTPS APIs, you can maintain a strong security posture while
enabling legitimate business use. You need to implement proper
authentication, network controls, and monitoring to verify that
only authorized parties can access your models.

When deploying machine learning models in production, you should
consider the model as a valuable asset that requires protection.
This means implementing layers of security controls including
network isolation through VPC configuration, strong authentication
mechanisms, and continuous monitoring of inference activities. For
external consumers, create a dedicated API layer that enforces
security policies and controls access.

### Implementation steps

1. **Plan your access control
   strategy**. Define which users or applications need
   access to your model endpoints and what specific permissions
   they require. Follow the principle of least privilege,
   granting only the minimum permissions necessary for each
   consumer to perform their required tasks.
2. **Set up secure inference API
   endpoints**. Host your ML models so that consumers
   can perform inference against them securely. Use
   [Amazon SageMaker AI endpoints](../../../sagemaker/latest/dg/realtime-endpoints-manage.md "../../../sagemaker/latest/dg/realtime-endpoints-manage.md") with proper authentication and
   authorization controls. Use
   [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") to automatically
   benchmark and optimize your model deployments for the best
   security-performance balance, and select optimal compute
   instances and configurations while maintaining security
   controls. This approach defines the relationship between the
   model and its consumers, restricts access to the base model,
   and provides monitoring capabilities for model interactions.
3. **Implement network security
   controls**. Configure your SageMaker AI inference
   endpoints within a VPC to isolate network traffic. Use
   security groups to define inbound and outbound traffic
   rules, and consider using
   [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") for private connectivity to your
   endpoints. Follow guidance from the
   [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") to implement proper
   network controls, such as restricting access to specific IP
   ranges and implementing bot protection.
4. **Configure authentication and
   authorization**. Sign HTTPS requests for API calls
   so that requester identity can be verified. Use
   [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") to control who has access
   to your SageMaker AI resources and what actions they can
   perform. Consider using
   [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") for managing user identities if your API is
   accessed by external users.
5. **Deploy endpoints in a secure VPC
   configuration**. Use
   [VPC
   endpoints](../../../vpc/latest/privatelink/vpc-endpoints.md "../../../vpc/latest/privatelink/vpc-endpoints.md") to privately connect your VPC to supported
   AWS services without requiring an internet gateway. Follow
   the guidance in
   [Give
   SageMaker AI Hosted Endpoints Access to Resources in Your
   Amazon VPC](../../../sagemaker/latest/dg/host-vpc.md "../../../sagemaker/latest/dg/host-vpc.md") to configure your endpoint for VPC access.
6. **Implement encryption for data in
   transit and at rest**. Configure your endpoints to
   use HTTPS for API calls. Encrypt model artifacts and data at
   rest using
   [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). Use client-side encryption
   for sensitive data when appropriate.
7. **Set up monitoring and
   logging**. Configure
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to monitor your endpoints and
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to log API calls. Implement
   [SageMaker AI
   Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to detect drift and data quality issues
   in your production models.
8. **Use model registry for
   governance**. Implement
   [SageMaker AI
   MLflow Model Registry](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to catalog and manage versions
   of your models, control which model versions are deployed,
   and maintain an audit trail of model approvals and
   deployments.
9. **Implement proper API design
   patterns**. Design your inference API following
   REST best practices. Include proper input validation, error
   handling, and rate limiting to protect against abuse.
   Consider implementing an
   [API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") in front of your SageMaker AI endpoint for
   additional controls.
10. **Conduct regular security
    reviews**. Periodically review the security
    configuration of your endpoints, check for over-permissive
    policies, and validate that access logs show only expected
    patterns of usage.
11. **Implement guardrails for AI
    models**. For AI endpoints, implement content
    filtering and validation controls to provide responsible
    outputs, stop harmful content generation, and maintain
    appropriate use of the models.

## Resources

**Related documents:**

- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [Real-time
  Inference](../../../sagemaker/latest/dg/realtime-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints.md")
- [Give
  SageMaker AI Hosted Endpoints Access to Resources in Your Amazon VPC](../../../sagemaker/latest/dg/host-vpc.md "../../../sagemaker/latest/dg/host-vpc.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Integrating
  machine learning models into your Java-based
  microservices](https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/ "https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/")
- [How
  Financial Institutions can use AWS to Address Regulatory
  Reporting](https://aws.amazon.com/blogs/architecture/how-banks-can-use-aws-to-meet-compliance/ "https://aws.amazon.com/blogs/architecture/how-banks-can-use-aws-to-meet-compliance/")
- [Secure
  deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/ "https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/")
- [Accelerating
  Machine Learning Development with Data Science as a Service
  from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/ "https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/")

**Related videos:**

- [End-to-End
  machine learning using Spark and Amazon SageMaker AI](https://www.youtube.com/watch?v=FKgivdwzO5g "https://www.youtube.com/watch?v=FKgivdwzO5g")

**Related examples:**

- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops "https://github.com/aws-samples/amazon-sagemaker-secure-mlops")
