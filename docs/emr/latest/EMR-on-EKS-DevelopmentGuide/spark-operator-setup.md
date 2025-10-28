# Setting up the Spark operator for Amazon EMR on EKS

Complete the following tasks to get set up before you install the Spark operator on
Amazon EKS. If you've already signed up for Amazon Web Services (AWS) and have used Amazon EKS, you are
almost ready to use Amazon EMR on EKS. Complete the following tasks to get set up for the Spark
operator on Amazon EKS. If you've already completed any of the prerequisites, you can skip
those and move on to the next one.

- [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  – If you've already installed the
  AWS CLI, confirm that you have the latest version.
- [Set up kubectl and eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
  – eksctl is a command line tool that you use to
  communicate with Amazon EKS.
- [Install Helm](../../../eks/latest/userguide/helm.md "../../../eks/latest/userguide/helm.md") – The
  Helm package manager for Kubernetes helps you install and manage applications on your
  Kubernetes cluster.
- [Get started with Amazon EKS – eksctl](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md")
  – Follow the steps to create a new Kubernetes
  cluster with nodes in Amazon EKS.
- [Select an Amazon EMR
  base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md") (release 6.10.0 or higher) – the Spark
  operator is supported with Amazon EMR releases 6.10.0 and higher.
