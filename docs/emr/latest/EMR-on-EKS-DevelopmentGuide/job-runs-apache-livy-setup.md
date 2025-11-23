# Setting up Apache Livy for Amazon EMR on EKS

Before you can install Apache Livy on your Amazon EKS cluster, you must install and configure a set of prerequisite tools. These include the AWS CLI, which is a foundational command-line tool for working
with AWS resources, command-line tools for working with Amazon EKS, and a controller that's used in this use case to make your cluster application available to the internet and to route network traffic.

- [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  – If you've already installed the AWS CLI, confirm that you have the
  latest version.
- [Set up kubectl and eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")

– eksctl is a command line tool that you use to communicate with Amazon EKS.

- [Install Helm](../../../eks/latest/userguide/helm.md "../../../eks/latest/userguide/helm.md") – The Helm package manager for Kubernetes helps
  you install and manage applications on your Kubernetes cluster.
- [Get started with Amazon EKS – eksctl](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md")
  – Follow the steps to create a new Kubernetes cluster
  with nodes in Amazon EKS.
- [Select an Amazon EMR release
  label](docker-custom-images-tag.md "docker-custom-images-tag.md") – the Apache Livy is supported with Amazon EMR releases 7.1.0 and higher.
- [Install the ALB controller](../../../eks/latest/userguide/aws-load-balancer-controller.md "../../../eks/latest/userguide/aws-load-balancer-controller.md")
  – the ALB controller manages AWS ELB for Kubernetes clusters. It creates an AWS Network Load Balancer (NLB) when you create a Kubernetes Ingress while setting up Apache Livy.
