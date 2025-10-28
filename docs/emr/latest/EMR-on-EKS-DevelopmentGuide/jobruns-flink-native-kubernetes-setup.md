# Setting up Flink Native Kubernetes for Amazon EMR on EKS

Complete the following tasks to get set up before you can run an application with the Flink CLI on
Amazon EMR on EKS. If you've already signed up for Amazon Web Services (AWS) and have used Amazon EKS,
you are almost ready to use Amazon EMR on EKS. If you've already completed any of the prerequisites,
you can skip those and move on to the next one.

- [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  – If you've already installed the
  AWS CLI, confirm that you have the latest version.
- [Get started with Amazon EKS – eksctl](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md")
  – Follow the steps to create a new Kubernetes
  cluster with nodes in Amazon EKS.
- [Select an Amazon EMR
  base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md") (release 6.13.0 or higher) – the Flink Kubernetes command
  is supported with Amazon EMR releases 6.13.0 and higher.
- Confirm that the JobManager service account has appropriate permissions to create and watch TaskManager
  pods. For more information, see [Flink JobManager service account security requirements for Native Kubernetes](jobruns-flink-native-kubernetes-security-requirements.md "jobruns-flink-native-kubernetes-security-requirements.md").
- Set up your local [AWS credentials profile](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md").
- [Create or updating a kubeconfig file for an Amazon EKS cluster](../../../eks/latest/userguide/create-kubeconfig.md "../../../eks/latest/userguide/create-kubeconfig.md") on which you want to run the Flink applications.
