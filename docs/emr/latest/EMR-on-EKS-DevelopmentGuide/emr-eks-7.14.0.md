

# Amazon EMR on EKS 7.14.0 releases
<a name="emr-eks-7.14.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.14.0 release in general, see [Amazon EMR 7.14.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7140-release.html) in the *Amazon EMR Release Guide*.

## Changes and features
<a name="emr-eks-7.14.0-changes"></a>

The following features are included with the 7.14.0 release of Amazon EMR on EKS:
+ **Spark Connect on Amazon EMR on EKS** – Amazon EMR on EKS clusters running emr-7.14.0 now support Spark Connect endpoints with token-based authentication. For setup and configuration, see [Run interactive sessions with Amazon EMR on EKS through Spark Connect](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-spark-connect.html) in the *Amazon EMR on EKS Development Guide*.
+ **Amazon EMR on EKS job runner pod graceful termination** – The Amazon EMR on EKS `jobsubmitter.gracefulTermination` configuration is enabled by default in emr-7.14.0 and subsequent 7.x releases. For setup and configuration, see [Using job submitter classification](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-job-submitter.html) in the *Amazon EMR on EKS Development Guide*.
+ **Livy endpoint stability after Kubernetes token rotation** – Fixed an issue where Amazon EMR on EKS managed Livy endpoints could become unusable after the Kubernetes service-account token rotates, previously requiring a pod restart to recover. Livy now automatically refreshes its credentials when the projected service-account token is rotated.
+ **Amazon EMR on EKS on IPv6 Amazon EKS clusters** – Amazon EMR on EKS now supports running workloads on IPv6 Amazon EKS clusters for emr-7.14.0 and subsequent releases. For setup and configuration, see [Running EMR on EKS on IPv6 clusters](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-ipv6.html) in the *Amazon EMR on EKS Development Guide*.
+ **Fixed Spark Operator applications on IPv6-only Amazon EKS clusters** – Spark Operator applications on IPv6-only Amazon EKS clusters no longer fail to submit due to a malformed Kubernetes API server URL for emr-7.14.0 and subsequent 7.x releases. For setup and configuration, see [Running EMR on EKS on IPv6 clusters](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-ipv6.html) in the *Amazon EMR on EKS Development Guide*.