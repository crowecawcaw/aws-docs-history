

# EDI on AWS supported configurations
<a name="eco-supported-configs"></a>

For a list of configurations that ECO supports, see [Supported configurations](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) in the *AMS Accelerate User Guide*.

EDI on AWS supports the following AWS Regions, languages, and operating systems:
+ **AWS Regions:**
  + US East (N. Virginia)
  + US West (Oregon)
  + Asia Pacific (Singapore)
  + Europe (Ireland)
  + Europe (Paris)
  + South America (São Paulo)
  + Asia Pacific (Mumbai)
  + Asia Pacific (Sydney)
+ **Language** – English.
+ **Operating systems** – See the AMS Accelerate [Service description](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html) documentation.

## EDI version support policy for Amazon EKS versions
<a name="eco-sup-config-eks"></a>

To keep your EDI environment up to date and secure, it's important to understand the EDI support policy as it relates to Amazon Elastic Kubernetes Service (Amazon EKS) versions.

EDI on AWS uses Amazon EKS to facilitate core functions of the data platform. Given this dependency, we recommend that you upgrade to the latest EDI version as soon as it becomes available to enable standard support on Amazon EKS. If you stay on a previous EDI version and exceed the standard Amazon EKS support window, Amazon EKS offers an extended support option that provides an additional year of support. To learn more and estimate future Amazon EKS costs, see [Amazon EKS extended support for Kubernetes versions pricing](https://aws.amazon.com/blogs/containers/amazon-eks-extended-support-for-kubernetes-versions-pricing/).

Your Amazon EKS clusters are automatically transitioned from standard support to extended support, with no further actions for you. If you remain on extended support, AWS continues to support your EDI version up to the previous two EDI versions. AWS also supports up to the last day of the extended Amazon EKS support version.

For example, if the latest EDI version is M24, then AWS supports M23 up to March 2026. When Amazon EKS versions reach the end of extended support, AWS force-upgrades the Amazon EKS service. Adhering to the policy helps maintain support for your EDI instance and provides you with access to the latest features and security updates.

For a list of end of support dates for Kubernetes, see the [Amazon EKS Kubernetes release calendar](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#kubernetes-release-calendar) in the *Amazon EKS User Guide*.

The following table provides an example summary of supported EDI versions. You can get the latest information from your E-SDM.


| EDI version | OSDU Forum Release Date | EDI Solution Release Date | End of Amazon EKS standard support | End of extended support | 
| --- | --- | --- | --- | --- | 
| M24(EKS 1.32) | October 2024 | July 2025 | March 2026 | March 2027 | 
| M23(EKS 1.29) | May 2024 | August 2024 | March 2025 | March 2026 | 