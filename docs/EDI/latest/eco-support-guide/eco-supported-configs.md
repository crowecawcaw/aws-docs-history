

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

EDI on AWS uses Amazon EKS to facilitate core functions of the data platform. Given this dependency, we recommend that you upgrade to the latest EDI version as soon as it becomes available to enable standard support on Amazon EKS. If you stay on a previous EDI version and exceed the standard Amazon EKS support window, Amazon EKS offers an extended support option that provides an additional year of support. To learn more and estimate future Amazon EKS costs, see [Amazon EKS Kubernetes release calendar](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#kubernetes-release-calendar) in the *Amazon EKS User Guide*.

Your Amazon EKS clusters are automatically transitioned from standard support to extended support, with no further actions for you. If you remain on extended support, AWS continues to support your EDI version up to the previous two EDI versions. AWS also supports up to the last day of the extended Amazon EKS support version.

For example, if the latest EDI version is M25, then AWS supports M24 up to March 2027. When Amazon EKS versions reach the end of extended support, AWS force-upgrades the Amazon EKS service. Adhering to the policy helps maintain support for your EDI instance and provides you with access to the latest features and security updates.

For a list of end of support dates for Kubernetes, see the [Amazon EKS Kubernetes release calendar](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#kubernetes-release-calendar) in the *Amazon EKS User Guide*.

The following table provides an example summary of supported EDI versions. You can get the latest information from your E-SDM.


| EDI version | Cluster version | OSDU Forum Release Date | EDI Solution Release Date | End of Amazon EKS standard support | End of extended support | 
| --- | --- | --- | --- | --- | --- | 
| EDI 2.1 | M25.4 (EKS 1.35) | May 2025 | August 2026 | March 2027 | March 2028 | 
| EDI 2.0 | M25.3 (EKS 1.35) | May 2025 | June 2026 | March 2027 | March 2028 | 
| EDI 1.2 | M25.2 (EKS 1.34) | May 2025 | December 2025 | December 2026 | December 2027 | 
| EDI 1.1 | M24 (EKS 1.32) | October 2024 | July 2025 | March 2026 | March 2027 | 

## EDI deployment models
<a name="eco-sup-config-deployment"></a>

EDI on AWS supports two distinct deployment architectures to accommodate your varying security and operational requirements. The choice between these models fundamentally affects how end users, applications, and external systems access the platform's core services.
+ **Private deployment** – In a private deployment, all critical EDI components are hosted within your network perimeter and can only be accessed through private connectivity mechanisms. Consequently, all OSDU APIs, EDI UI, and Airflow URLs are exclusively accessible through your network.
+ **Public deployment** – In a public deployment, EDI components are accessible through public internet endpoints with standard HTTPS/TLS encryption. Users and integrated systems can access the OSDU APIs, EDI UI, and Airflow URL from any location with internet connectivity, subject to authentication and authorization controls.

You must inform the EDI Cloud Operations (ECO) team of the chosen deployment model during the initial onboarding phase. This decision drives critical architectural choices, including the following:
+ Network configuration (VPC endpoints, Transit Gateway attachments, DNS resolution)
+ Security group and network ACL rules
+ Certificate provisioning and management
+ Monitoring and logging endpoint configuration