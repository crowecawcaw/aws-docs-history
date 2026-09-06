

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS add-ons for local clusters on AWS Outposts configured with EC2 instance store
<a name="eks-outposts-instance-store-local-cluster-addons"></a>

Local clusters on AWS Outposts configured with EC2 instance store support Amazon EKS add-ons. The following add-ons have been validated for use with local clusters. Additional add-ons will be validated over time.

**Note**  
If your Outpost is configured with Amazon EBS instead of EC2 instance store, the architecture described in this topic isn’t available for your Outpost. Outposts configured with EBS will continue to use the existing local clusters implementation, which doesn’t support Amazon EKS add-ons.  
If you are interested in creating a local cluster on an EBS-backed Outpost using the updated local clusters architecture, contact your AWS account team.

## Validated add-ons
<a name="eks-outposts-instance-store-local-cluster-addons-validated"></a>


| Add-on | Description | 
| --- | --- | 
|  [Amazon VPC CNI plugin for Kubernetes](managing-vpc-cni.md)  | Provides native VPC networking for pods. | 
|  [kube-proxy](managing-kube-proxy.md)  | Maintains network rules on nodes for Kubernetes Service communication. | 
|  [CoreDNS](managing-coredns.md)  | Provides DNS resolution for Kubernetes Services. | 
|  [EKS Pod Identity Agent](pod-id-agent-setup.md)  | Enables pods to use EKS Pod Identity to authenticate to AWS services. | 

Customer-managed versions of the Amazon VPC CNI plugin, `kube-proxy`, and CoreDNS are automatically installed when you create a local cluster. You can optionally install the managed versions of these add-ons.

**Important**  
EKS Pod Identity and IRSA depend on AWS STS in the AWS Region. During network disconnects, workloads that use these mechanisms cannot obtain new credentials. For more information, see [Prepare local Amazon EKS clusters on AWS Outposts configured with EC2 instance store for network disconnects](eks-outposts-instance-store-network-disconnects.md).

## Add-ons not yet validated
<a name="eks-outposts-instance-store-local-cluster-addons-not-validated"></a>

Add-ons not listed above have not been validated for use with local clusters. Using unvalidated add-ons is not recommended.

As additional add-ons are validated, this page will be updated.

## Alternative CNI plugins
<a name="eks-outposts-instance-store-local-cluster-addons-alternative-cni"></a>

Amazon VPC CNI is the officially supported CNI for Amazon EKS deployments on Outposts. If you want to use an alternative CNI plugin, see [Alternate CNI plugins for Amazon EKS clusters](alternate-cni-plugins.md).