# MLSUS-12: Use efficient silicon

Use the most efficient instance type compatible with your ML
workload.

## Implementation plan

AWS offers several purpose-built compute architectures that
are optimized to minimize the sustainability impact of ML
workloads:

- **For CPU-based ML inference, use
  AWS Graviton3** - These processors offer the best
  performance per watt in Amazon EC2. They use up to 60%
  less energy than comparable EC2 instances.
  [Graviton3](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")
  processors deliver up to three times better performance
  compared to Graviton2 processors for ML workloads, and
  they
  [support
  bfloat16](https://youtu.be/9NEQbFLtDmg?t=3613 "https://youtu.be/9NEQbFLtDmg?t=3613").
- **For deep learning inference, use
  AWS Inferentia** - The Amazon EC2 Inf2 instances
  offer up to 50% better performance/watt over comparable
  Amazon EC2 instances because they and the underlying
  [Inferentia2
  accelerators](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/") are purpose built to run DL models at
  scale. Inf2 instances help you meet your sustainability
  goals when deploying ultra-large models.
- **For training, use AWS
  Trainium** - The Amazon EC2 trn1 instances based
  on the custom designed
  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/") chips offer up to 50% cost-to-train
  savings over comparable Amazon EC2 instances. When using a
  Trainium-based instance cluster,
  the total energy consumption for training BERT Large from
  scratch is approximately 25% lower compared to a
  same-sized cluster of comparable accelerated EC2
  instances.

## Documents

- [Instances
  with AWS Inferentia](../../../AWSEC2/latest/UserGuide/accelerated-computing-instances.md#aws-inferentia-instances "../../../AWSEC2/latest/UserGuide/accelerated-computing-instances.md#aws-inferentia-instances")
- [Use
  instance types with the least impact](../sustainability-pillar/use-instance-types-with-the-least-impact.md "../sustainability-pillar/use-instance-types-with-the-least-impact.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 3, deployment and
  monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/")
- [Achieving
  1.85x higher performance for deep learning based object detection with an AWS Neuron compiled YOLOv4 model on AWS Inferentia](https://aws.amazon.com/blogs/machine-learning/improving-performance-for-deep-learning-based-object-detection-with-an-aws-neuron-compiled-yolov4-model-on-aws-inferentia/ "https://aws.amazon.com/blogs/machine-learning/improving-performance-for-deep-learning-based-object-detection-with-an-aws-neuron-compiled-yolov4-model-on-aws-inferentia/")
- [Deploying
  TensorFlow OpenPose on AWS Inferentia-based Inf1 instances
  for significant price performance improvements](https://aws.amazon.com/blogs/machine-learning/deploying-tensorflow-openpose-on-aws-inferentia-based-inf1-instances-for-significant-price-performance-improvements/ "https://aws.amazon.com/blogs/machine-learning/deploying-tensorflow-openpose-on-aws-inferentia-based-inf1-instances-for-significant-price-performance-improvements/")
- [Amazon EC2 Update – Inf1 Instances with AWS Inferentia Chips for
  High Performance Cost-Effective Inferencing](https://aws.amazon.com/blogs/aws/amazon-ec2-update-inf1-instances-with-aws-inferentia-chips-for-high-performance-cost-effective-inferencing/ "https://aws.amazon.com/blogs/aws/amazon-ec2-update-inf1-instances-with-aws-inferentia-chips-for-high-performance-cost-effective-inferencing/")
