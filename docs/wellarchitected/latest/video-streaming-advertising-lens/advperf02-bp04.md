# ADVPERF02-BP04 Use a specialized instance family and features

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

AWS Nitro Enclaves enables customers to create isolated compute environments to further help protect and securely process highly sensitive data such as personally identifiable information (PII) and intellectual property data within their Amazon EC2 instances. Nitro Enclaves assist customers to reduce the threat surface area for their most sensitive data processing applications. Enclaves offers an isolated, hardened, and highly constrained environment to host security-critical applications. Nitro Enclaves enables a range of use cases that deal with the processing of highly sensitive data, such as securing private keys, tokenization, and multi-party collaboration. The isolation, cryptographic attestation, and integration with AWS Key Management Service capabilities of Nitro Enclaves are key features that provide customers with a practical approach to setting up multi-party collaboration.

## Resources

- [Choosing
  an AWS compute service](../../../decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.md "../../../decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.md")
- [Scaling
  distributed training with AWS Trainium and Amazon EKS](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/ "https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/")
- [AWS Inferentia2 builds on AWS Inferentia1 by delivering 4x higher throughput and 10x lower latency](https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/ "https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/")
- [Introducing Unified ID 2.0 Private Operator Services on AWS Using Nitro Enclaves](https://aws.amazon.com/blogs/industries/introducing-unified-id-2-0-private-operator-services-on-aws-using-nitro-enclaves/ "https://aws.amazon.com/blogs/industries/introducing-unified-id-2-0-private-operator-services-on-aws-using-nitro-enclaves/")
- [Use AWS Nitro Enclaves to perform computation of multiple sensitive datasets](https://aws.amazon.com/blogs/compute/leveraging-aws-nitro-enclaves-to-perform-computation-of-multiple-sensitive-datasets/ "https://aws.amazon.com/blogs/compute/leveraging-aws-nitro-enclaves-to-perform-computation-of-multiple-sensitive-datasets/")
