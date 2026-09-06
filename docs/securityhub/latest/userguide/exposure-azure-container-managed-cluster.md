

# Remediating exposures for Azure Kubernetes Service clusters
<a name="exposure-azure-container-managed-cluster"></a>

AWS Security Hub can generate exposure findings for Azure Kubernetes Service (AKS) clusters.

On the Security Hub console, the AKS cluster involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources. 

**Contents**
+ [Misconfiguration traits for Azure Kubernetes Service clusters](#azure-aks-misconfiguration)
  + [The Azure Kubernetes Service cluster is running an unsupported Kubernetes version](#aks-unsupported-kubernetes-version)
  + [The Azure Kubernetes Service cluster has unencrypted Kubernetes secrets](#unencrypted-kubernetes-secrets)
+ [Reachability traits for Azure Kubernetes Service clusters](#azure-aks-reachability)
  + [The Azure Kubernetes Service cluster allows public access](#internet-reachable)

## Misconfiguration traits for Azure Kubernetes Service clusters
<a name="azure-aks-misconfiguration"></a>

Here are misconfiguration traits for Azure Kubernetes Service clusters and suggested remediation steps.

### The Azure Kubernetes Service cluster is running an unsupported Kubernetes version
<a name="aks-unsupported-kubernetes-version"></a>

 The AKS cluster is running a Kubernetes version that is no longer supported by Microsoft. Unsupported Kubernetes versions stop receiving security patches and bug fixes, which leaves known vulnerabilities in the control plane and node components unaddressed and exposes the cluster to attack. Following security best practices, keep the cluster on a supported Kubernetes version. 

**Remediation: Upgrade to a supported Kubernetes version**  
 Upgrade the cluster control plane and node pools to a supported Kubernetes version. Because minor versions cannot be skipped, upgrade sequentially through each minor version and apply the latest patch. Review the breaking changes for each version before upgrading. 

 Consider enabling automatic upgrades to stay current. For more information, see [Supported Kubernetes versions in AKS](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions) in the Microsoft Azure documentation. 

### The Azure Kubernetes Service cluster has unencrypted Kubernetes secrets
<a name="unencrypted-kubernetes-secrets"></a>

 By default, the cluster stores Kubernetes secrets in the etcd data store without encryption by a customer-controlled key. Without encryption at rest using a key management service, anyone who gains access to the underlying etcd data can read sensitive secret values such as credentials and tokens. Following data protection best practices, enable KMS etcd encryption so that Kubernetes secrets are encrypted at rest with a key in Azure Key Vault. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Enable KMS etcd encryption**  
 Configure the cluster to use Key Management Service (KMS) etcd encryption with a key stored in Azure Key Vault. Grant the cluster identity encrypt and decrypt permissions on the key. Re-encrypt existing secrets after you enable the feature. Enable soft delete and purge protection on the key vault so the key can't be lost. For more information, see [KMS etcd encryption in AKS](https://learn.microsoft.com/en-us/azure/aks/use-kms-etcd-encryption) in the Microsoft Azure documentation. 

 Enable soft delete and purge protection on the key vault so the key cannot be lost. For more information, see [KMS etcd encryption in AKS](https://learn.microsoft.com/en-us/azure/aks/use-kms-etcd-encryption) in the Microsoft Azure documentation. 

**Store secrets in Azure Key Vault**  
 To avoid storing sensitive values as Kubernetes secrets in etcd at all, use the Azure Key Vault provider for the Secrets Store CSI Driver to mount secrets, keys, and certificates from Azure Key Vault into pods at runtime. For more information, see [Azure Key Vault provider for Secrets Store CSI Driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver) in the Microsoft Azure documentation. 

## Reachability traits for Azure Kubernetes Service clusters
<a name="azure-aks-reachability"></a>

Here are reachability traits for Azure Kubernetes Service clusters and suggested remediation steps.

### The Azure Kubernetes Service cluster allows public access
<a name="internet-reachable"></a><a name="potentially-internet-reachable"></a>

 The API server is the endpoint that you use to communicate with your cluster's Kubernetes control plane. The cluster is reachable from the internet when the API server endpoint is public, or when workloads are exposed through a public load balancer or ingress. Public endpoints increase your attack surface and the risk of unauthorized access to your Kubernetes API server. Attackers can potentially access or modify cluster resources and read sensitive data. Following security best practices, restrict access to your cluster's API server and workloads to only necessary IP ranges. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Restrict access to the API server**  
 Use a private cluster so the API server is reachable only from within your virtual network, or configure authorized IP ranges to limit which source addresses can reach the public API server endpoint. For more information, see [Private Azure Kubernetes Service clusters](https://learn.microsoft.com/en-us/azure/aks/private-clusters) in the Microsoft Azure documentation. 

**Limit public exposure of workloads**  
 Review services exposed through public load balancers or ingress, and restrict or remove public exposure where it is not required. Use internal load balancers, network security group rules, and a web application firewall on a controlled ingress point for workloads that must be reached from the internet. For more information, see [Networking concepts for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network) in the Microsoft Azure documentation. 