

# Setting up Apache Livy for Amazon EMR on EKS
<a name="job-runs-apache-livy-setup"></a>

Before you can install Apache Livy on your Amazon EKS cluster, you must install and configure a set of prerequisite tools. These include the AWS CLI, which is a foundational command-line tool for working with AWS resources, command-line tools for working with Amazon EKS, and a controller that's used in this use case to make your cluster application available to the internet and to route network traffic.
+ **[Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) ** – If you've already installed the AWS CLI, confirm that you have the latest version.
+ **[Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) ** – eksctl is a command line tool that you use to communicate with Amazon EKS.
+ **[Install Helm](https://docs.aws.amazon.com/eks/latest/userguide/helm.html)** – The Helm package manager for Kubernetes helps you install and manage applications on your Kubernetes cluster. 
+ **[Get started with Amazon EKS – eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) ** – Follow the steps to create a new Kubernetes cluster with nodes in Amazon EKS.
+ **[Select an Amazon EMR release label](docker-custom-images-tag.md)** – the Apache Livy is supported with Amazon EMR releases 7.1.0 and higher.
+ **[Install the ALB controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)** – the ALB controller manages AWS Elastic Load Balancing for Kubernetes clusters. It creates an AWS Network Load Balancer (NLB) when you create a Kubernetes Ingress while setting up Apache Livy.