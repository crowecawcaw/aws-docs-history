# MLREL-02: Adopt a machine learning microservice strategy

Where appropriate, a complex business problem can be usefully
decomposed into a series of machine learning models with a
loosely coupled implementation. This can be accomplished by
adopting a microservice instead of a monolithic architecture.
This approach replaces one large resource with multiple small
resources and can reduce the impact of a single failure on the
overall workload. This strategy enables distributed development
and improves scalability, enabling easier change management.

## Implementation plan

- **Adopt a microservice
  strategy** - Service-oriented architecture (SOA)
  is the practice of making software components reusable
  using service interfaces. Instead of building a monolithic
  application, where all functionality is contained in a
  single runtime, the application is instead broken into
  separate components. Microservices extend this by making
  components that are single-purpose and reusable. When
  building your architecture, divide components along
  business boundaries or logical domains. Adopt a philosophy
  that favors single-purpose applications that can be
  composed in different ways to deliver different end-user
  experiences.
- **Use AWS services in developing
  microservices** - Two popular approaches for
  developing microservices are using
  [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") and Docker containers with
  [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/"). With AWS Lambda, you can run code for
  virtually any type of application or backend service with
  zero administration. You pay only for the compute time you
  consume, and there is no charge when your code is not
  running. A common approach to reduce operational efforts
  for deployment is using a container- based deployment. AWS Fargate is a container management service that allows you
  to run serverless containers so you don’t have to worry
  about provisioning, configuring, and scaling clusters of
  virtual machines to run containers.

## Documents

- [Implementing
  Microservices on AWS](../../../whitepapers/latest/microservices-on-aws/microservices-on-aws.md "../../../whitepapers/latest/microservices-on-aws/microservices-on-aws.md")
- [Microservices
  on AWS](https://aws.amazon.com/microservices/ "https://aws.amazon.com/microservices/")
- [Break
  a Monolith Application into Microservices](https://aws.amazon.com/getting-started/hands-on/break-monolith-app-microservices-ecs-docker-ec2 "https://aws.amazon.com/getting-started/hands-on/break-monolith-app-microservices-ecs-docker-ec2")
- [AWS Lambda Documentation](../../../lambda/index.md "../../../lambda/index.md")
- [What
  is AWS Fargate?](../../../AmazonECS/latest/userguide/what-is-fargate.md "../../../AmazonECS/latest/userguide/what-is-fargate.md")

## Blogs

- [Deploying
  Python Flask microservices to AWS using open-source
  tools](https://aws.amazon.com/blogs/opensource/deploying-python-flask-microservices-to-aws-using-open-source-tools/ "https://aws.amazon.com/blogs/opensource/deploying-python-flask-microservices-to-aws-using-open-source-tools/")
- [Deploying
  machine learning models as serverless APIs](https://aws.amazon.com/blogs/machine-learning/deploying-machine-learning-models-as-serverless-apis/ "https://aws.amazon.com/blogs/machine-learning/deploying-machine-learning-models-as-serverless-apis/")
- [Integrating
  machine learning models into your Java-based
  microservices](https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/ "https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/")
- [Adopting
  machine learning in your microservices with DJL (Deep Java
  Library) and Spring Boot](https://aws.amazon.com/blogs/opensource/adopting-machine-learning-in-your-microservices-with-djl-deep-java-library-and-spring-boot/ "https://aws.amazon.com/blogs/opensource/adopting-machine-learning-in-your-microservices-with-djl-deep-java-library-and-spring-boot/")
- [Building,
  deploying, and operating containerized applications with
  AWS Fargate](https://aws.amazon.com/blogs/compute/building-deploying-and-operating-containerized-applications-with-aws-fargate/ "https://aws.amazon.com/blogs/compute/building-deploying-and-operating-containerized-applications-with-aws-fargate/")

## Videos

- [Breaking
  the Monolith Using AWS Container Services](https://www.youtube.com/watch?v=pu8UHomwTEI "https://www.youtube.com/watch?v=pu8UHomwTEI")
- [AWS New York Summit 2019: Migrating Monolithic Applications
  with the Strangler Pattern (FSV303)](https://www.youtube.com/watch?v=E2dnSg-IHdo "https://www.youtube.com/watch?v=E2dnSg-IHdo")

## Examples

- [Run
  a Serverless “Hello, World” with AWS Lambda](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/ "https://aws.amazon.com/getting-started/hands-on/run-serverless-code/")
