**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Common use cases in Amazon EKS

Amazon EKS offers robust managed Kubernetes services on AWS, designed to optimize containerized applications. The following are a few of the most common use cases of Amazon EKS, helping you leverage its strengths for your specific needs.

**Deploying high-availability applications**

Using [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/"), you can make sure that your applications are highly available across multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

**Building microservices architectures**

Use Kubernetes service discovery features with [AWS Cloud Map](https://aws.amazon.com/cloud-map/ "https://aws.amazon.com/cloud-map/") or [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice/ "https://aws.amazon.com/vpc/lattice/") to build resilient systems.

**Automating software release processes**

Manage continuous integration and continuous deployment (CI/CD) pipelines that simplify the process of automated building, testing, and deployment of applications.
For declarative continuous deployment, see [Continuous Deployment with Argo CD](argocd.md "argocd.md").

**Running serverless applications**

Use [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/") with Amazon EKS to run serverless applications. This means you can focus solely on application development, while Amazon EKS and Fargate handle the underlying infrastructure.

**Executing machine learning workloads**

Amazon EKS is compatible with popular machine learning frameworks such as [TensorFlow](https://www.tensorflow.org/ "https://www.tensorflow.org/"), [MXNet](https://mxnet.apache.org/ "https://mxnet.apache.org/"), and [PyTorch](https://pytorch.org/ "https://pytorch.org/"). With GPU support, you can handle even complex machine learning tasks effectively.

**Deploying consistently on-premises and in the cloud**

To simplify running Kubernetes in on-premises environments, you can use the same Amazon EKS clusters, features, and tools to run self-managed nodes on [AWS Outposts](eks-outposts.md "eks-outposts.md") or can use [Amazon EKS Hybrid Nodes](hybrid-nodes-overview.md "hybrid-nodes-overview.md") with your own infrastructure. For self-contained, air-gapped environments, you can use [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/ "https://aws.amazon.com/eks/eks-anywhere/") to automate Kubernetes cluster lifecycle management on your own infrastructure.

**Running cost-effective batch processing and big data workloads**

Utilize [Spot Instances](https://aws.amazon.com/ec2/spot/ "https://aws.amazon.com/ec2/spot/") to run your batch processing and big data workloads such as [Apache Hadoop](https://aws.amazon.com/emr/details/hadoop/what-is-hadoop/ "https://aws.amazon.com/emr/details/hadoop/what-is-hadoop/") and [Spark](https://aws.amazon.com/big-data/what-is-spark/ "https://aws.amazon.com/big-data/what-is-spark/"), at a fraction of the cost. This lets you take advantage of unused Amazon EC2 capacity at discounted prices.

**Managing AWS resources from Kubernetes**

Use [AWS Controllers for Kubernetes (ACK)](ack.md "ack.md") to create and manage AWS resources directly from your Kubernetes cluster using native Kubernetes APIs.

**Building platform engineering abstractions**

Create custom Kubernetes APIs that compose multiple resources into higher-level abstractions using [kro (Kube Resource Orchestrator)](kro.md "kro.md").

**Securing applications and ensuring compliance**

Implement strong security practices and maintain compliance with Amazon EKS, which integrates with AWS security services such as [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM), [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") (Amazon VPC), and [AWS Key Management Service](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") (AWS KMS). This ensures data privacy and protection as per industry standards.
