**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Security in Amazon EKS

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. For Amazon EKS, AWS is responsible for the Kubernetes control plane, which includes the control plane nodes and `etcd` database. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to Amazon EKS, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility includes the following areas.

      + The security configuration of the data plane, including the configuration of the security groups that allow traffic to pass from the Amazon EKS control plane into the customer VPC
      + The configuration of the nodes and the containers themselves
      + The node’s operating system (including updates and security patches)
      + Other associated application software:




      	- Setting up and managing network controls, such as firewall rules
      	- Managing platform-level identity and access management, either with or in addition to IAM
      + The sensitivity of your data, your company’s requirements, and applicable laws and regulations

  Amazon EKS is certified by multiple compliance programs for regulated and sensitive applications. Amazon EKS is compliant with [SOC](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/"), [PCI](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/"), [ISO](https://aws.amazon.com/compliance/iso-certified/ "https://aws.amazon.com/compliance/iso-certified/"), [FedRAMP-Moderate](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/"), [IRAP](https://aws.amazon.com/compliance/irap/ "https://aws.amazon.com/compliance/irap/"), [C5](https://aws.amazon.com/compliance/bsi-c5/ "https://aws.amazon.com/compliance/bsi-c5/"), [K-ISMS](https://aws.amazon.com/compliance/k-isms/ "https://aws.amazon.com/compliance/k-isms/"), [ENS High](https://aws.amazon.com/compliance/esquema-nacional-de-seguridad/ "https://aws.amazon.com/compliance/esquema-nacional-de-seguridad/"), [OSPAR](https://aws.amazon.com/compliance/OSPAR/ "https://aws.amazon.com/compliance/OSPAR/"), [HITRUST CSF](https://aws.amazon.com/compliance/hitrust/ "https://aws.amazon.com/compliance/hitrust/"), and is a [HIPAA](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/") eligible service. For more information, see [Learn how access control works in Amazon EKS](cluster-auth.md "cluster-auth.md").

This documentation helps you understand how to apply the shared responsibility model when using Amazon EKS. The following topics show you how to configure Amazon EKS to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Amazon EKS resources.

###### Note

Linux containers are made up of control groups (cgroups) and namespaces that help limit what a container can access, but all containers share the same Linux kernel as the host Amazon EC2 instance. Running a container as the root user (UID 0) or granting a container access to host resources or namespaces such as the host network or host PID namespace are strongly discouraged, because doing so reduces the effectiveness of the isolation that containers provide.

###### Topics

- [Secure Amazon EKS clusters with best practices](security-best-practices.md "security-best-practices.md")
- [Analyze vulnerabilities in Amazon EKS](configuration-vulnerability-analysis.md "configuration-vulnerability-analysis.md")
- [Compliance validation for Amazon EKS clusters](compliance.md "compliance.md")
- [Security considerations for Amazon Elastic Kubernetes Service](security-eks.md "security-eks.md")
- [Security considerations for Kubernetes](security-k8s.md "security-k8s.md")
- [Security considerations for Amazon EKS Auto Mode](auto-security.md "auto-security.md")
- [Identity and access management for Amazon EKS](security-iam.md "security-iam.md")
