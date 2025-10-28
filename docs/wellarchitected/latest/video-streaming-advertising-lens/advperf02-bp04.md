# ADVPERF02-BP04 Use a specialized instance family

For advertising workloads, consider using a specialized instance
family like compute-optimized for ad serving, storage-optimized
for in-memory database, Trainium-based for machine learning (ML),
and Inferentia-based for ML inferences.

## Implementation guidance

[Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")
provides a

[wide
selection of instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") optimized to fit different
use cases.

The Amazon EC2 Compute Optimized instance family (C series) is a
great match for compute-intensive workloads such as batch
processing, media encoding, ad serving, bidding, and distributed
analytics.

The Amazon EC2 Storage Optimized instance family (I series) are
next-generation, storage-optimized instances designed to run
applications that require high throughput and real-time latency
access to data on local SSD storage. These instances help
customers running real-time database workloads with Aerospike,
where low latency local NVMe storage is required.

Amazon EC2 Accelerated Computing instances (powered by
[AWS Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/")) are purpose built for high performance, deep
learning, and model training, while offering up to 50%
cost-to-train savings over comparable GPU-based instances.

AWS Inferentia accelerators are designed by AWS to deliver high
performance at the lowest cost in Amazon EC2 for your deep
learning (DL) and generative AI inference applications. 

## Resources

- [Choosing
  an AWS compute service](../../../decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.md "../../../decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.md")
- [Scaling
  distributed training with AWS Trainium and Amazon EKS](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/ "https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/")
- [Scale
  your machine learning workloads on Amazon ECS powered by AWS Trainium instances](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks "https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks")
- [AWS Inferentia2 builds on AWS Inferentia1 by delivering 4x higher throughput and 10x lower latency](https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/ "https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/")
