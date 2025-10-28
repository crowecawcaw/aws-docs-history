# What are AWS Deep Learning Containers?

AWS Deep Learning Containers are pre-built Docker images that make it easier to run popular deep learning frameworks and tools on AWS.
They provide a consistent, up-to-date, secure, and optimized runtime environment for your deep learning applications
hosted on AWS infrastructure. To get started, see [Getting Started with AWS Deep Learning Containers](getting-started.md "getting-started.md").

## Key Features

### Pre-Installed Deep Learning Frameworks

AWS Deep Learning Containers include pre-installed and configured versions of leading deep learning frameworks such as TensorFlow and PyTorch.
This eliminates the need to build and maintain your own Docker images from scratch.

### Hardware Acceleration

AWS Deep Learning Containers are optimized for CPU-based, GPU-accelerated, and AWS silicon-based deep learning. They support CUDA, cuDNN,
and other necessary libraries for leveraging the power of GPU-based Amazon EC2 instances, as well as AWS-designed chips like
Graviton CPUs and GPUs, AWS Trainium, and Intel's Habana-Gaudi processors.

### AWS Service Integration

AWS Deep Learning Containers seamlessly integrate with a variety of AWS services, including SageMaker AI, Amazon Elastic Container Service (ECS),
Amazon Elastic Kubernetes Service (EKS), Amazon EC2, and AWS ParallelCluster. This makes it easy to deploy and run your deep learning
models and applications on AWS infrastructure.

### Secure and Regularly Updated

AWS regularly maintains and updates the AWS Deep Learning Containers to ensure you have access to the latest versions of deep learning frameworks
and dependencies. This helps keep your AWS-based deep learning environment secure and up-to-date, without the overhead of managing
security patches and updates yourself. Keeping your deep learning containers updated with the latest security patches can be a
resource-intensive task, but AWS Deep Learning Containers eliminate this burden by providing regular, automatic updates. This ensures your deep learning
environment remains secure and current, without requiring significant manual effort on your part. By automating the update process,
AWS Deep Learning Containers allow you to focus on developing your deep learning models and applications, rather than worrying about the underlying
infrastructure and security upkeep, which can improve your team's productivity and allow you to more efficiently leverage the latest
deep learning capabilities in your AWS-hosted projects.

## Use Cases

AWS Deep Learning Containers are particularly useful in the following AWS-based deep learning scenarios:

### Model Training

Use AWS Deep Learning Containers to train your deep learning models on CPU-based, GPU-accelerated, or AWS silicon-powered Amazon EC2 instances,
or leverage multi-node training on AWS ParallelCluster or SageMaker Hyperpod.

### Model Deployment

Deploy your trained models using the AWS Deep Learning Containers for scalable, production-ready inference on AWS, such as through SageMaker AI.

### Experimentation and Prototyping

Quickly spin up deep learning development environments on AWS using the pre-configured containers. AWS Deep Learning Containers are the default
option for notebook in SageMaker AI Studio, making it easy to get started with experimentation and prototyping.

### Continuous Integration and Delivery

Integrate the containers into your AWS-based CI/CD pipelines, such as those using Amazon ECS or Amazon EKS,
for consistent, automated deep learning workloads.
