# Using Apache Livy with Amazon EMR on EKS

With Amazon EMR releases 7.1.0 and higher, you can use Apache Livy to submit jobs on Amazon EMR on EKS. Using Apache Livy,
you can set up your own Apache Livy REST endpoint and use it to deploy and manage Spark applications on your
Amazon EKS clusters. After you install Livy in your Amazon EKS cluster, you can use the Livy endpoint to submit Spark applications to your Livy server.
The server manages the lifecycle of the Spark applications.

###### Note

Amazon EMR calculates pricing on Amazon EKS based on vCPU and memory consumption. This calculation applies to driver and executor pods. This calculation
starts from when you download your Amazon EMR application image until the Amazon EKS pod terminates and is rounded to the nearest second.

###### Topics

- [Setting up Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-setup.md "job-runs-apache-livy-setup.md")
- [Getting started with Apache Livy on Amazon EMR on EKS](job-runs-apache-livy-install.md "job-runs-apache-livy-install.md")
- [Running a Spark application with Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-run-spark.md "job-runs-apache-livy-run-spark.md")
- [Uninstalling Apache Livy with Amazon EMR on EKS](job-runs-apache-livy-uninstall.md "job-runs-apache-livy-uninstall.md")
- [Security for Apache Livy with Amazon EMR on EKS](job-runs-apache-livy-security.md "job-runs-apache-livy-security.md")
- [Installation properties for Apache Livy on Amazon EMR on EKS releases](job-runs-apache-livy-installation-properties.md "job-runs-apache-livy-installation-properties.md")
- [Troubleshoot common environment-variable format errors](job-runs-apache-livy-troubleshooting.md "job-runs-apache-livy-troubleshooting.md")
