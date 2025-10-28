# Tutorial: Connect from a containerized application hosted on Amazon Elastic Kubernetes Service

This tutorial walks you through the steps required to set up an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to host a containerized application that connects
to Amazon Keyspaces using SigV4 authentication.

Amazon EKS is a managed service that eliminates the need to install, operate, and maintain your own Kubernetes
control plane. [Kubernetes](https://kubernetes.io/docs/concepts/overview/ "https://kubernetes.io/docs/concepts/overview/") is an open-source system that
automates the management, scaling, and deployment of containerized applications.

The tutorial provides step-by-step guidance to configure, build, and deploy a
containerized Java application to Amazon EKS. In the last step you run the application to write
data to an Amazon Keyspaces table.

###### Topics

- [Prerequisites for connecting from Amazon EKS to Amazon Keyspaces](EKS-tutorial-prerequisites.md "EKS-tutorial-prerequisites.md")
- [Step 1: Configure the Amazon EKS cluster and setup IAM permissions](EKS-tutorial-step1.md "EKS-tutorial-step1.md")
- [Step 2: Configure the application](EKS-tutorial-step2.md "EKS-tutorial-step2.md")
- [Step 3: Create the application image and upload the Docker file to your Amazon ECR repository](EKS-tutorial-step3.md "EKS-tutorial-step3.md")
- [Step 4: Deploy the application to Amazon EKS and write
  data to your table](EKS-tutorial-step4.md "EKS-tutorial-step4.md")
- [Step 5: (Optional) Cleanup](EKS-tutorial-step5.md "EKS-tutorial-step5.md")
