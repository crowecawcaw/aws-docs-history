

# Remediating exposures for GCP Google Kubernetes Engine clusters

AWS Security Hub can generate exposure findings for GCP Google Kubernetes Engine (GKE) clusters.

On the Security Hub console, the GCP GKE cluster involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Misconfiguration traits for GCP Google Kubernetes Engine clusters](#gcp-gke-misconfiguration)
  + [The GKE cluster is using an unsupported version of Kubernetes](#unsupported-kubernetes-version)
  + [The GKE cluster has unencrypted Kubernetes secrets](#unencrypted-kubernetes-secrets)
+ [Reachability traits for GCP Google Kubernetes Engine clusters](#gcp-gke-reachability)
  + [The GKE cluster is reachable from the public internet](#internet-reachable)

## Misconfiguration traits for GCP Google Kubernetes Engine clusters
<a name="gcp-gke-misconfiguration"></a>

Here are misconfiguration traits for GCP Google Kubernetes Engine clusters and suggested remediation steps.

### The GKE cluster is using an unsupported version of Kubernetes
<a name="unsupported-kubernetes-version"></a>

 The cluster's control plane runs a Kubernetes minor version whose standard support has ended. Unless the cluster is in the Extended channel, that version no longer gets security patches, so known Kubernetes vulnerabilities stay unfixed. Following security best practices, run your GKE clusters on Kubernetes versions in standard support. 

**Remediation: Upgrade to a Kubernetes version in standard support**  
 Upgrade the control plane to a Kubernetes version in standard support, one minor version at a time, and then upgrade the node pools. Before each upgrade, check for APIs that the new version removes, and test the upgrade first. Extended channel clusters still get patches, but this trait clears only on a version in standard support. For more information, see [Upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) and [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) on the Google Cloud website. 

### The GKE cluster has unencrypted Kubernetes secrets
<a name="unencrypted-kubernetes-secrets"></a>

 Application-layer secrets encryption is off for the cluster, so only Google's default encryption at rest protects its Kubernetes secrets, and you don't control the key. With application-layer secrets encryption, GKE encrypts secrets with a key that you manage in Cloud Key Management Service (Cloud KMS). Following data protection best practices, turn on application-layer secrets encryption for your GKE clusters. 

**Remediation: Turn on application-layer secrets encryption**  
 Grant the Kubernetes Engine service agent the Cloud KMS CryptoKey Encrypter/Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on a Cloud KMS key in the cluster's region, and then turn on application-layer secrets encryption with that key. The update restarts the control plane, and a zonal cluster's control plane is briefly unavailable. Don't destroy or disable the key while the cluster uses it. For more information, see [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) on the Google Cloud website. 

## Reachability traits for GCP Google Kubernetes Engine clusters
<a name="gcp-gke-reachability"></a>

Here are reachability traits for GCP Google Kubernetes Engine clusters and suggested remediation steps.

### The GKE cluster is reachable from the public internet
<a name="internet-reachable"></a><a name="potentially-internet-reachable"></a>

 The cluster is reachable from the public internet when a network scan finds an open port on its control plane's public endpoint. Google calls this endpoint the external endpoint. The cluster might be reachable when that endpoint is on and authorized networks aren't, so the endpoint accepts connections from any address. Attackers can then use leaked credentials or exploit Kubernetes API server vulnerabilities from anywhere on the internet. Following standard security principles, restrict internet access to the control planes of your GKE clusters. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Remove internet access to the control plane**  
 Turn off the control plane's external endpoint, and use the DNS-based endpoint, which Google recommends, or the internal endpoint instead. The DNS-based endpoint is reachable from the internet, but Identity and Access Management (IAM) policies control who can use it. Before you turn off the external endpoint, move its clients to another endpoint. For more information, see [Network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation) on the Google Cloud website. 

**Turn on authorized networks**  
 Turn on authorized networks, and limit them to the address ranges that need access to the control plane. Include every legitimate client, such as deployment pipelines and administrator networks, or those clients lose access. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work) on the Google Cloud website. 