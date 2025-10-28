# Running Spark jobs with the Spark operator

Amazon EMR releases 6.10.0 and higher support the Kubernetes operator for Apache Spark, or
_the Spark operator_, as a job submission model for Amazon EMR on EKS. With the
Spark operator, you can deploy and manage Spark applications with the Amazon EMR release runtime
on your own Amazon EKS clusters. Once you deploy the Spark operator in your Amazon EKS cluster, you
can directly submit Spark applications with the operator. The operator manages the lifecycle
of Spark applications.

###### Note

Amazon EMR calculates pricing on Amazon EKS based on vCPU and memory consumption. This calculation applies to driver and executor pods. This calculation
starts from when you download your Amazon EMR application image until the Amazon EKS pod terminates and is rounded to the nearest second.

###### Topics

- [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md "spark-operator-setup.md")
- [Getting started with the Spark operator for
  Amazon EMR on EKS](spark-operator-gs.md "spark-operator-gs.md")
- [Use vertical autoscaling with the Spark operator for
  Amazon EMR on EKS](spark-operator-vas.md "spark-operator-vas.md")
- [Uninstalling the Spark operator for
  Amazon EMR on EKS](spark-operator-uninstall.md "spark-operator-uninstall.md")
- [Using monitoring configuration to monitor the Spark Kubernetes operator and Spark jobs](spark-operator-monitoring-configuration.md "spark-operator-monitoring-configuration.md")
- [Security and the Spark operator with
  Amazon EMR on EKS](spark-operator-security.md "spark-operator-security.md")
