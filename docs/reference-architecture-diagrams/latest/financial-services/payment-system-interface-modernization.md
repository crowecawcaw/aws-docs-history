

# Payment system interface modernization on AWS

Publication date: **April 6, 2022 ([Diagram history](diagram-history.md))**

This architecture shows you how to build a microservices-based payment system to handle scale and optimized performance with improved container-based deployment, and using API and event-based models for handling different channels in payment.

## Payment system interface modernization on AWS diagram
<a name="payment-system-diagram"></a>

![Diagram showing a microservices-based payment system on AWS using Amazon EKS and Amazon MSK.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/payment-system-interface-moderization.png)


The following steps describe the architecture:

1. Users initiate transactions to the payment interface system using mobile apps integrated with the payment system, or through bank-provided apps.

1. The request receiver accepts the request at the bank data center.

1. The request is routed to payment interface services in the AWS network from the bank using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. A request from a merchant or other client arrives directly from the internet.

1. The request passes through [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) and is received through the [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), which routes requests to services using a Amazon VPC endpoint and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/) (NLB). 

1. In AWS, the request for payment interface services is received by the [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) (Amazon EKS) cluster's [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) (ALB) ingress controller.

1. Ingress rules redirect the request to a targeted microservice for purposes such as payment, balance, virtual payment address (VPA), merchant, account, and so on.

1. Payment interface services reach the bank hardware security model (HSM), core banking systems hosted inside the bank using Direct Connect.

1. Payment interface services perform create, read, update, and delete (CRUD) operations in the [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (Amazon RDS) unified payment interface (UPI) database.

1. Payment interface services maintain sessions in [Amazon ElastiCache (Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/).

1. Payment interface services communicate with each other with an event-driven model using topics in [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) (Amazon MSK).

1. Payment interface microservices provide observability by using [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

1. Use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) (IAM), [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS), and [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) to ensure role-based access, securing credentials, and data.

1. Payment interface near real-time transaction data is consumed by other systems in the bank DC using an Amazon RDS replica over Direct Connect.

1. Payment interface microservices container images are maintained inside [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) (Amazon ECR).

## Further reading
<a name="payment-system-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 