# ADVOPS02-BP01 Implement monitoring across each layer of your

advertising stack including infrastructure, applications, and user experience

Ensuring operational excellence in advertising workloads requires
a holistic approach to monitoring. This best practice emphasizes
the importance of implementing comprehensive monitoring solutions
that span all layers of the advertising stack. The advertising
stack includes the ad-serving infrastructure, data pipelines,
application performance, and user experience. By monitoring these
various components, you can gain a complete understanding of the
overall health and performance of your advertising workload. This
understanding helps you identify and address issues, optimize
resource utilization, and deliver a seamless customer experience.
With a multi-layered monitoring approach, you can proactively
detect and resolve problems before they impact your business.

## Implementation guidance

Monitor and set KPIs and SLOs for infrastructure services using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") for services like
[Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")
and [Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/"). Set up CloudWatch Alarms for resource utilization,
performance, and availability.

## Resources

- [Observability using native Amazon CloudWatch and AWS X-Ray for serverless modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/ "https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/")
- [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/ "https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/")
