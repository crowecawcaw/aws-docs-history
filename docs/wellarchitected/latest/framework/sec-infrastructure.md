# Infrastructure protection

Infrastructure protection encompasses control methodologies, such
as defense in depth, necessary to meet best practices and
organizational or regulatory obligations. Use of these
methodologies is critical for successful, ongoing operations in
either the cloud or on-premises.

In AWS, you can implement stateful and stateless packet
inspection, either by using AWS-native technologies or by using
partner products and services available through the AWS Marketplace. You should use Amazon Virtual Private Cloud (Amazon VPC) to create a private, secured, and scalable environment in
which you can define your topology—including gateways, routing
tables, and public and private subnets.

The following questions focus on these considerations for
security.

| SEC 5:  How do you protect your network resources?                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Any workload that has some form of network connectivity, whether it’s the<br>internet or a private network, requires multiple layers of defense to help protect<br>from external and internal network-based threats. |

| SEC 6:  How do you protect your compute resources?                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute resources in your workload require multiple layers of defense to help<br>protect from external and internal threats. Compute resources include EC2<br>instances, containers, AWS Lambda functions, database services, IoT devices, and<br>more. |

Multiple layers of defense are advisable in any type of
environment. In the case of infrastructure protection, many of
the concepts and methods are valid across cloud and on-premises
models. Enforcing boundary protection, monitoring points of
ingress and egress, and comprehensive logging, monitoring, and
alerting are all essential to an effective information security
plan.

AWS customers are able to tailor, or harden, the configuration of
an Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Container Service (Amazon ECS) container, or AWS Elastic Beanstalk
instance, and persist this configuration to an immutable Amazon
Machine Image (AMI). Then, whether launched by Auto Scaling or
launched manually, all new virtual servers (instances) launched
with this AMI receive the hardened configuration.
