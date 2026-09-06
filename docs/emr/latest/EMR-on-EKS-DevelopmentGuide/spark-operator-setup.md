

# Setting up the Spark operator for Amazon EMR on EKS
<a name="spark-operator-setup"></a>

Complete the following tasks to get set up before you install the Spark operator on Amazon EKS. If you've already signed up for Amazon Web Services (AWS) and have used Amazon EKS, you are almost ready to use Amazon EMR on EKS. Complete the following tasks to get set up for the Spark operator on Amazon EKS. If you've already completed any of the prerequisites, you can skip those and move on to the next one.
+ **[Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) ** – If you've already installed the AWS CLI, confirm that you have the latest version.
+ **[Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) ** – eksctl is a command line tool that you use to communicate with Amazon EKS.
+ **[Install Helm](https://docs.aws.amazon.com/eks/latest/userguide/helm.html)** – The Helm package manager for Kubernetes helps you install and manage applications on your Kubernetes cluster. 
+ **[Get started with Amazon EKS – eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) ** – Follow the steps to create a new Kubernetes cluster with nodes in Amazon EKS.
+ **[Select an Amazon EMR base image URI](docker-custom-images-tag.md) (release 6.10.0 or higher)** – the Spark operator is supported with Amazon EMR releases 6.10.0 and higher.