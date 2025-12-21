# MLREL01-BP02 Adopt a machine learning microservice

strategy

Machine learning systems can be effectively implemented through a
microservice architecture that breaks down complex business problems
into smaller, loosely coupled components. This approach enables
distributed development, improves scalability, and facilitates
change management while reducing the impact of single failures on
the overall workload.

**Desired outcome:** You decompose
complex business problems into manageable components with clear
interfaces. You have a more resilient ML system architecture that
can scale individual components independently, enable faster
iterations, and allow specialized teams to work simultaneously on
different parts of the solution. Your organization benefits from
improved fault isolation, simplified testing, and greater
flexibility to update or replace individual ML models without
affecting the entire system.

**Common anti-patterns:**

- Building monolithic ML applications where functionality is
  tightly coupled in a single runtime.
- Creating overly complex microservices that serve multiple
  purposes.
- Implementing microservices without clear business domain
  boundaries.
- Neglecting proper service interfaces and communication patterns
  between microservices.
- Overlooking the operational complexity introduced by distributed
  systems.

**Benefits of establishing this best
practice:**

- Improves resilience through isolation of failures to individual
  components.
- Enhances scalability by allowing independent scaling of
  individual services.
- Accelerates development cycles through parallel work streams.
- Simplifies testing and deployment of individual components.
- Provides flexibility to use different technologies for different
  ML model requirements.
- Aligns technical components with business domains.
- Eases integration of new ML models and capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing ML systems, adopt a microservice architecture to
break down complex problems into manageable components. Rather
than creating one large monolithic application that handles the
entirety of of your machine learning workflow, you can develop
specialized services that handle specific functions like data
preprocessing, model training, inference, and business logic
integration. This approach is particularly valuable for machine
learning applications where different models may have varying
resource requirements, development cycles, and deployment
frequencies.

Microservices provide the flexibility to use different
technologies for different parts of your ML system. For example,
you might use Python-based services for data science tasks while
implementing Java-based services for integration with enterprise
systems. By establishing clear service interfaces, you verify that
these components work together seamlessly while maintaining
freedom.

When designing your ML microservices, focus on business domains
rather than technical functions. Instead of creating a generic
prediction service, you might create more specific services like
_customer churn prediction_ or
_product recommendation_ that align with
business capabilities. This domain-driven approach makes your
architecture more intuitive and adaptable to changing business
needs.

### Implementation steps

1. **Adopt a microservice
   strategy**. Implement a service-oriented
   architecture (SOA) by making software components reusable
   through service interfaces. Break your monolithic
   application into separate components along business
   boundaries or logical domains. Focus on building
   single-purpose applications that can be composed in
   different ways to deliver various end-user experiences.
   Design clear APIs between services to implement proper
   isolation and communication patterns.
2. **Define domain boundaries**.
   Analyze your machine learning workflow and identify natural
   boundaries between different functional areas. Map out the
   data flow and determine where service boundaries make sense.
   Consider creating separate microservices for data ingestion,
   preprocessing, feature engineering, model training, model
   serving, and business logic integration. Verify that each
   microservice has a clear, single responsibility within your
   ML system.
3. **Choose appropriate AWS
   services**. Select AWS services that best support
   your microservice architecture.
   [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") provides serverless compute that scales
   automatically and charges only for the compute time
   consumed. For container-based deployments, use
   [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/") to run containers without managing
   infrastructure. Consider
   [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") or
   [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/") for container orchestration needs, and
   [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") to manage and secure your microservice
   APIs.
4. **Implement model serving
   infrastructure**. Set up efficient model serving
   using services like
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") for deploying, monitoring, and scaling ML
   models. SageMaker AI endpoints provide a managed solution for
   hosting models and handling inference requests.
   Alternatively, use
   [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") for lightweight, event-driven inferencing or
   containers on
   [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/") for more complex requirements.
5. **Establish communication
   patterns**. Design how your microservices will
   communicate with each other. Use synchronous REST APIs for
   direct request-response patterns, and asynchronous
   communication through
   [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") or
   [Amazon SQS](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/") for event-driven architectures. Implement
   [AWS EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") to create event-driven workflows between
   your ML microservices and other AWS services.
6. **Implement monitoring and
   observability**. Set up comprehensive monitoring
   for your ML microservices using
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"). Track operational metrics like latency,
   throughput, and error rates along with ML-specific metrics
   such as prediction accuracy or drift. Implement distributed
   tracing with
   [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/") to troubleshoot issues across service
   boundaries and identify performance bottlenecks.
7. **Automate deployments**.
   Implement CI/CD pipelines using
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") and
   [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/") to automate the testing and deployment of
   your ML microservices. Use infrastructure as code with
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") to define and provision your microservice
   infrastructure consistently.
8. **Implement security best
   practices**. Secure your ML microservices by
   implementing proper authentication and authorization using
   [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") or
   [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/"). Use
   [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/") to protect your APIs from common web exploits,
   and encrypt sensitive data using
   [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to improve data privacy and adhere to regulatory
   requirements.

## Resources

**Related documents:**

- [Implementing
  Microservices on AWS](../../../whitepapers/latest/microservices-on-aws/microservices-on-aws.md "../../../whitepapers/latest/microservices-on-aws/microservices-on-aws.md")
- [AWS Lambda Documentation](../../../lambda/index.md "../../../lambda/index.md")
- [Architect
  for AWS Fargate for Amazon ECS](../../../AmazonECS/latest/userguide/what-is-fargate.md "../../../AmazonECS/latest/userguide/what-is-fargate.md")
- [What
  is Amazon SageMaker AI?](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md")
- [What
  is the AWS Serverless Application Model (AWS SAM)?](../../../serverless-application-model/latest/developerguide/what-is-sam.md "../../../serverless-application-model/latest/developerguide/what-is-sam.md")
- [Build
  and deploy ML inference applications from scratch using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/build-and-deploy-ml-inference-applications-from-scratch-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/build-and-deploy-ml-inference-applications-from-scratch-using-amazon-sagemaker/")

**Related examples:**

- [Run
  a Serverless "Hello, World" with AWS Lambda](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/ "https://aws.amazon.com/getting-started/hands-on/run-serverless-code/")
