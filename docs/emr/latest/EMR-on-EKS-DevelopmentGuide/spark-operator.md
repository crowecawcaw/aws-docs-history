

# Running Spark jobs with the Spark operator
<a name="spark-operator"></a>

Amazon EMR releases 6.10.0 and higher support the Kubernetes operator for Apache Spark, or *the Spark operator*, as a job submission model for Amazon EMR on EKS. With the Spark operator, you can deploy and manage Spark applications with the Amazon EMR release runtime on your own Amazon EKS clusters. Once you deploy the Spark operator in your Amazon EKS cluster, you can directly submit Spark applications with the operator. The operator manages the lifecycle of Spark applications.

**Note**  
Amazon EMR calculates pricing on Amazon EKS based on vCPU and memory consumption. This calculation applies to driver and executor pods. This calculation starts from when you download your Amazon EMR application image until the Amazon EKS pod terminates and is rounded to the nearest second. Pricing applies whenever pods run using an image derived from the Amazon EMR runtime, regardless of whether the image is stored in the public Amazon EMR Amazon ECR registry or your own private registry, and regardless of how the job is orchestrated (for example, the StartJobRun API, the Spark operator, or spark-submit).

**Topics**
+ [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md)
+ [Getting started with the Spark operator for Amazon EMR on EKS](spark-operator-gs.md)
+ [Use vertical autoscaling with the Spark operator for Amazon EMR on EKS](spark-operator-vas.md)
+ [Uninstalling the Spark operator for Amazon EMR on EKS](spark-operator-uninstall.md)
+ [Using monitoring configuration to monitor the Spark Kubernetes operator and Spark jobs](spark-operator-monitoring-configuration.md)
+ [Security and the Spark operator with Amazon EMR on EKS](spark-operator-security.md)