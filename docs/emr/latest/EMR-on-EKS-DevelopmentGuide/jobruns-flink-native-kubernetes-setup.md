

# Setting up Flink Native Kubernetes for Amazon EMR on EKS
<a name="jobruns-flink-native-kubernetes-setup"></a>

Complete the following tasks to get set up before you can run an application with the Flink CLI on Amazon EMR on EKS. If you've already signed up for Amazon Web Services (AWS) and have used Amazon EKS, you are almost ready to use Amazon EMR on EKS. If you've already completed any of the prerequisites, you can skip those and move on to the next one.
+ **[Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) ** – If you've already installed the AWS CLI, confirm that you have the latest version.
+ **[Get started with Amazon EKS – eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) ** – Follow the steps to create a new Kubernetes cluster with nodes in Amazon EKS.
+ **[Select an Amazon EMR base image URI](docker-custom-images-tag.md) (release 6.13.0 or higher)** – the Flink Kubernetes command is supported with Amazon EMR releases 6.13.0 and higher.
+ Confirm that the JobManager service account has appropriate permissions to create and watch TaskManager pods. For more information, see [Flink JobManager service account security requirements for Native Kubernetes](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-native-kubernetes-security-requirements.html).
+ Set up your local [AWS credentials profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
+ [Create or updating a kubeconfig file for an Amazon EKS cluster ](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html)on which you want to run the Flink applications.