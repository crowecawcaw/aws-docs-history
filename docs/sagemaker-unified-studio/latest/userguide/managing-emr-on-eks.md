# Amazon EMR on EKS in Amazon SageMaker Unified Studio

You can connect to Amazon EMR on EKS in Amazon SageMaker Unified Studio.

Amazon EMR on EKS allows you to run open-source big data frameworks on Amazon EKS.
With Amazon EMR on EKS, you can focus on running analytics workloads while Amazon EMR on EKS builds,
configures, and manages containers for open-source applications.

Amazon EMR on EKS virtual clusters require an Amazon EKS cluster with compatible configurations.
Amazon EMR on EKS operates by creating an Amazon EMR on EKS virtual cluster on top of your existing Amazon EKS cluster.
You then interact with the Amazon EMR on EKS virtual cluster directly for interactive session management.
For more information, see
[What is Amazon EMR on EKS?](../../../emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.md "../../../emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.md")

## Spark History Server for Amazon EMR on EKS in Amazon SageMaker Unified Studio

You can use the Spark History Server in a notebook session to view details such as tasks, executors and logs about Spark queries.

You can explore the Spark History Server for an active Amazon EMR on EKS interactive session.
To do this, navigate to your project's JupyterLab IDE and select your Amazon EMR on EKS connection.
After any Spark query is executed, choose the **Spark History Server** embedded link.
