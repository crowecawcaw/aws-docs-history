**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a cluster with Amazon EKS Auto Mode

This chapter explains how to create an Amazon EKS cluster with Auto Mode enabled using various tools and interfaces. Auto Mode simplifies cluster creation by automatically configuring and managing the cluster’s compute, networking, and storage infrastructure. You’ll learn how to create an Auto Mode cluster using the AWS CLI, AWS Management Console, or the eksctl command line tool.

###### Note

EKS Auto Mode requires Kubernetes version 1.29 or greater.

Choose your preferred tool based on your needs: The AWS Management Console provides a visual interface ideal for learning about EKS Auto Mode features and creating individual clusters. The AWS CLI is best suited for scripting and automation tasks, particularly when integrating cluster creation into existing workflows or CI/CD pipelines. The eksctl CLI offers a Kubernetes-native experience and is recommended for users familiar with Kubernetes tooling who want simplified command line operations with sensible defaults.

Before you begin, ensure you have the necessary prerequisites installed and configured, including appropriate IAM permissions to create EKS clusters. To learn how to install CLI tools such as `kubectl`, `aws`, and `eksctl`, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").

You can use the AWS CLI, AWS Management Console, or eksctl CLI to create a cluster with Amazon EKS Auto Mode.

###### Topics

- [Create an EKS Auto Mode Cluster with the eksctl CLI](automode-get-started-eksctl.md "automode-get-started-eksctl.md")
- [Create an EKS Auto Mode Cluster with the AWS CLI](automode-get-started-cli.md "automode-get-started-cli.md")
- [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md "automode-get-started-console.md")
