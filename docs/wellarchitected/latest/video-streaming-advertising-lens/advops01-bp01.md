# ADVOPS01-BP01 Assess trade-offs between ad serving architecture options and associated risks

When designing the ad serving infrastructure, evaluate the trade-offs between different
architectural approaches and their associated risks. This includes considering factors such
as performance, scalability, availability, security, and cost to determine the optimal
solution.

## Implementation guidance

- Assess the performance and scalability requirements of your
  ad serving workload, including peak traffic patterns and
  seasonal fluctuations. Evaluate architectures that can
  dynamically scale, such as serverless or containerized
  approaches.
- Analyze the availability and reliability needs of your ad
  serving infrastructure, ensuring that your architecture
  includes redundancy and fault tolerance mechanisms to
  maintain high uptime.
- Evaluate the security risks associated with your ad serving
  workload, such as bot attacks and ad fraud, and implement
  appropriate controls like web application firewalls and rate
  limiting.

## Key AWS services

### Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/")
- [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/")
- [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/")
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/")
- [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
- [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/")
- [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/ "https://aws.amazon.com/elasticloadbalancing/application-load-balancer/")
- [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")

### Resources

- [Building
  Applications with Serverless Architectures](https://aws.amazon.com/lambda/serverless-architectures-learn-more/ "https://aws.amazon.com/lambda/serverless-architectures-learn-more/")
