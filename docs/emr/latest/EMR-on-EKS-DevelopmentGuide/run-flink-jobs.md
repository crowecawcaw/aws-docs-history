# Running Flink jobs with Amazon EMR on EKS

Amazon EMR releases 6.13.0 and higher support Amazon EMR on EKS with Apache Flink, or the Flink
Kubernetes operator, as a job submission model for Amazon EMR on EKS. With Amazon EMR on EKS with Apache
Flink, you can deploy and manage Flink applications with the Amazon EMR release runtime on your own Amazon
EKS clusters. Once you deploy the Flink Kubernetes operator in your Amazon EKS cluster, you can directly submit
Flink applications with the operator. The operator manages the lifecycle of Flink applications.

###### Topics

- [Setting up and using the Flink Kubernetes operator](jobruns-flink-kubernetes-operator.md "jobruns-flink-kubernetes-operator.md")
- [Using Flink Native Kubernetes](jobruns-flink-native-kubernetes.md "jobruns-flink-native-kubernetes.md")
- [Customizing Docker images for Flink and FluentD](jobruns-flink-docker-flink-fluentd.md "jobruns-flink-docker-flink-fluentd.md")
- [Monitoring Flink Kubernetes operator and Flink jobs](jobruns-flink-monitoring.md "jobruns-flink-monitoring.md")
- [How Flink supports high availability and job resiliency](jobruns-flink-resiliency.md "jobruns-flink-resiliency.md")
- [Using Autoscaler for Flink applications](jobruns-flink-autoscaler.md "jobruns-flink-autoscaler.md")
- [Maintenance and troubleshooting for Flink jobs on Amazon EMR on EKS](jobruns-flink-troubleshooting.md "jobruns-flink-troubleshooting.md")
- [Supported releases for Amazon EMR on EKS with
  Apache Flink](jobruns-flink-security-release-versions.md "jobruns-flink-security-release-versions.md")
