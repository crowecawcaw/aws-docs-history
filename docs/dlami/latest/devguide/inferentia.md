# Recommended Inferentia Instances

AWS Inferentia instances are designed to provide high performance and cost efficiency for deep learning model inference workloads.
Specifically, Inf2 instance types use AWS Inferentia chips and the [AWS Neuron SDK](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/ "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/"), which is integrated with popular machine learning frameworks
such as TensorFlow and PyTorch.

Customers can use Inf2 instances to run large scale machine learning inference applications such as search, recommendation engines,
computer vision, speech recognition, natural language processing, personalization, and fraud detection, at the lowest cost in the cloud.

###### Note

The size of your model should be a factor in choosing an instance. If your model exceeds an
instance's available RAM, choose a different instance type with enough memory for
your application.

- [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/ "https://aws.amazon.com/ec2/instance-types/inf2/") have up to up to 16 AWS Inferentia chips and 100 Gbps of networking throughput.
  For more information about getting started with AWS Inferentia DLAMIs, see [The AWS Inferentia Chip With DLAMI](tutorial-inferentia.md "tutorial-inferentia.md").

###### Next Up

[Recommended Trainium Instances](trainium.md "trainium.md")
