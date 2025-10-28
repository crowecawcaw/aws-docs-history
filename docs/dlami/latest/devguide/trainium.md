# Recommended Trainium Instances

AWS Trainium instances are designed to provide high performance and cost efficiency for deep learning model inference workloads.
Specifically, Trn1 instance types use AWS Trainium chips and the [AWS Neuron SDK](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/ "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/"), which is integrated with popular machine learning frameworks
such as TensorFlow and PyTorch.

Customers can use Trn1 instances to run large scale machine learning inference applications such as search, recommendation engines,
computer vision, speech recognition, natural language processing, personalization, and fraud detection, at the lowest cost in the cloud.

###### Note

The size of your model should be a factor in choosing an instance. If your model exceeds an
instance's available RAM, choose a different instance type with enough memory for
your application.

- [Amazon EC2 Trn1 Instances](https://aws.amazon.com/ec2/instance-types/trn1/ "https://aws.amazon.com/ec2/instance-types/trn1/") have up to up to 16 AWS Trainium chips and 100 Gbps of networking throughput.
