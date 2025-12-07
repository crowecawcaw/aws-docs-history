# Remediating exposures for Amazon EKS clusters

AWS Security Hub can generate exposure findings for Amazon Elastic Kubernetes Service (Amazon EKS) clusters.

The Amazon EKS cluster involved in an exposure finding and its identifying information are listed in
the **Resource** section of the finding details. You can retrieve these
resource details on the Security Hub console or programmatically with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

###### Contents

- [Misconfiguration traits for Amazon EKS clusters](exposure-eks-cluster.md#eks-cluster-misconfiguration "exposure-eks-cluster.md#eks-cluster-misconfiguration")
  - [The Amazon EKS cluster allows public access](exposure-eks-cluster.md#internet-reachable "exposure-eks-cluster.md#internet-reachable")
  - [The Amazon EKS cluster uses an unsupported Kubernetes version](exposure-eks-cluster.md#unsupported-kubernetes-version "exposure-eks-cluster.md#unsupported-kubernetes-version")
  - [The Amazon EKS cluster uses unencrypted Kubernetes secrets](exposure-eks-cluster.md#unencrypted-kubernetes-secrets "exposure-eks-cluster.md#unencrypted-kubernetes-secrets")

- [Vulnerability traits for Amazon EKS clusters](exposure-eks-cluster.md#vulnerability "exposure-eks-cluster.md#vulnerability")
  - [The Amazon EKS cluster has a container with network-exploitable software vulnerabilities with a high likelihood of exploitation](exposure-eks-cluster.md#high-priority-vulnerability "exposure-eks-cluster.md#high-priority-vulnerability")
  - [The Amazon EKS cluster has a container with software vulnerabilities](exposure-eks-cluster.md#low-priority-vulnerability "exposure-eks-cluster.md#low-priority-vulnerability")

- [The Amazon EKS cluster has a container with an End-Of-Life operating system](exposure-eks-cluster.md#end-of-life-operating-system-detected "exposure-eks-cluster.md#end-of-life-operating-system-detected")
- [The Amazon EKS cluster has a container with malicious software packages](exposure-eks-cluster.md#malicious-package "exposure-eks-cluster.md#malicious-package")
- [The EKS cluster has malicious files](exposure-eks-cluster.md#malicious-file "exposure-eks-cluster.md#malicious-file")

## Misconfiguration traits for Amazon EKS clusters

Here are misconfiguration traits for Amazon EKS clusters and suggested remediation steps.

### The Amazon EKS cluster allows public access

The Amazon EKS cluster endpoint is the endpoint that you use to communicate with your cluster’s Kubernetes API server.
By default, this endpoint is public to the internet.
Public endpoints increase your attack surface area and the risk of unauthorized access to your Kubernetes API server, potentially allowing attackers to access or modify cluster resources or access sensitive data.
Following security best practices, AWS recommends restricting access to your EKS cluster endpoint to only necessary IP ranges.

###### Modify endpoint access

In the exposure finding, open the resource.
This will open the affected Amazon EKS cluster.
You can configure your cluster to use private access, public access, or both. With private access, Kubernetes API requests that originate within your cluster’s VPC use the private VPC endpoint.
With public access, Kubernetes API requests that originate from outside your cluster’s VPC use the public endpoint.

###### Modify or remove public access to the cluster

To modify endpoint access for an existing cluster, see [Modifying cluster endpoint access](../../../eks/latest/userguide/cluster-endpoint.md#modify-endpoint-access "../../../eks/latest/userguide/cluster-endpoint.md#modify-endpoint-access") in the _Amazon Elastic Kubernetes Service User Guide_.
Implement more restrictive rules based on specific IP ranges or security groups.
If limited public access is necessary, restrict access to specific CIDR block ranges or use prefix lists.

### The Amazon EKS cluster uses an unsupported Kubernetes version

Amazon EKS supports each Kubernetes version for a limited period of time.
Running clusters with unsupported Kubernetes versions can expose your environment to security vulnerabilities, as CVE patches will stop being released for outdated versions.
Unsupported versions may contain known security vulnerabilities that can be exploited by attackers and lack security features that may be available in newer versions.
Following security best practices, AWS recommends keeping your Kubernetes version updated.

###### Update Kubernetes version

In the exposure finding, open the resource.
This will open the affected Amazon EKS cluster.
Before updating your cluster, review [Available versions on standard support](../../../eks/latest/userguide/kubernetes-versions.md#version-deprecation "../../../eks/latest/userguide/kubernetes-versions.md#version-deprecation") in the _Amazon Elastic Kubernetes Service User Guide_ for a list of currently supported Kubernetes versions.

### The Amazon EKS cluster uses unencrypted Kubernetes secrets

Kubernetes secrets are, by default, stored unencrypted in the API server’s underlying data store (etcd).
Anyone with API access or with access to etcd can retrieve or modify a secret. To prevent this, you should encrypt Kubernetes secrets at rest.
If Kubernetes Secrets are unencrypted, they are vulnerable to unauthorized access if etcd is compromised.
Since secrets often contain sensitive information like passwords and API tokens, their exposure could lead to unauthorized access to other applications and data.
Following security best practices, AWS recommends encrypting all sensitive information stored in Kubernetes secrets.

###### Encrypt Kubernetes secrets

Amazon EKS supports the encryption of Kubernetes secrets using KMS keys through envelope encryption.

To enable encryption of Kubernetes secrets for your EKS cluster, see [Encrypt Kubernetes secrets with KMS on existing clusters](../../../eks/latest/userguide/enable-kms.md "../../../eks/latest/userguide/enable-kms.md") in the _Amazon EKS User Guide_.

## Vulnerability traits for Amazon EKS clusters

Here are the vulnerability traits for Amazon EKS clusters.

### The Amazon EKS cluster has a container with network-exploitable software vulnerabilities with a high likelihood of exploitation

Software packages that are installed on EKS clusters can be exposed to Common Vulnerabilities and Exposures (CVEs).
Critical CVEs pose significant security risks to your AWS environment.
Unauthorized users can exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Critical vulnerabilities with high exploitation likelihood represent immediate security threats, as exploit code may already be publicly available and actively used by attackers or automated scanning tools.
Following security best practices, AWS recommends patching these vulnerabilities to protect your instance from attack.

###### Update affected instances

Update your container images to newer versions that include security fixes for the identified vulnerabilities.
This typically involves rebuilding your container images with updated base images or dependencies, then deploying the new images to your Amazon EKS cluster.

### The Amazon EKS cluster has a container with software vulnerabilities

Software packages that are installed on Amazon EKS clusters can be exposed to Common Vulnerabilities and Exposures (CVEs).
Noncritical CVEs represent security weaknesses with lower severity or exploitability compared to critical CVEs.
While these vulnerabilities pose less immediate risk, attackers can still exploit these unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Following security best practices, AWS recommends patching these vulnerabilities to protect your instance from attack.

###### Update affected instances

Update your container images to newer versions that include security fixes for the identified vulnerabilities.
This typically involves rebuilding your container images with updated base images or dependencies, then deploying the new images to your Amazon EKS cluster.

## The Amazon EKS cluster has a container with an End-Of-Life operating system

The Amazon EKS container image relies on an end-of-life operating system that is no longer supported or maintained by the original developer.
This exposes the container to security vulnerabilities and potential attacks.
When operating systems reach end-of-life, vendors typically stop releasing new security advisories.
Existing security advisories may also be removed from vendor feeds.
As a result, Amazon Inspector could potentially stop generating findings for known CVEs, creating further gaps in security coverage.

See [Discontinued operating systems](../../../inspector/latest/user/supported.md#formerly-supported-os "../../../inspector/latest/user/supported.md#formerly-supported-os") in the _Amazon Inspector User Guide_ for information about operating systems that have reached end of life that can be detected by Amazon Inspector.

###### Update to a supported operating system version

We recommend updating to a supported version of the operating system.
In the exposure finding, open the resource to access the affected resource.
Before updating the operating system version in your container image, review available versions in [Supported Operating Systems](../../../inspector/latest/user/supported.md#supported-os "../../../inspector/latest/user/supported.md#supported-os") in the _Amazon Inspector User Guide_ for a list of currently supported OS versions.
After updating your container image, rebuild and redeploy your containers to the Amazon EKS cluster.

## The Amazon EKS cluster has a container with malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your Amazon EKS cluster, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, AWS recommends removing malicious packages to protect your cluster from potential attacks.

###### Remove malicious packages

Review the malicious package details in the **References** section of the **Vulnerability** tab of the trait to understand the threat.
Remove the identified malicious packages from your container images.
Then, delete the pods with the compromised image.
Update your Kubernetes deployments to use the updated container images.
Then, deploy your changes and redeploy your pods.

## The EKS cluster has malicious files

Malicious files contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious files pose an active and critical threat to your cluster, as attackers can execute malicious code automatically without exploiting a vulnerability.
Following security best practices, AWS recommends removing malicious files to protect your cluster from potential attacks.

###### Remove malicious files

To identify the specific Amazon Elastic Block Store (Amazon EBS) volume that has malicious files, review the **Resources** section of the trait's finding details.
Once you have identified the volume with the malicious file, remove the identified malicious files.
After removing the malicious files, consider performing a scan to ensure that all files that may have been installed by the malicious file have been removed.
For more information, see [Starting On-demand malware scan in GuardDuty](../../../guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.md "../../../guardduty/latest/ug/malware-protection-getting-started-on-demand-scan.md") in the .
