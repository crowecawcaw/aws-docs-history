

# Data retrieval APIs for Amazon Elastic Kubernetes Service
<a name="amazonelastickubernetesservice"></a>

Amazon Elastic Kubernetes Service provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="eks-AccessKubernetesApi"></a>[AccessKubernetesApi](https://docs.aws.amazon.com/eks/latest/userguide/view-workloads.html) | View Kubernetes objects via AWS EKS console | Read | 
| <a name="eks-DescribeAccessEntry"></a>[DescribeAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAccessEntry.html) | Describe an Amazon EKS access entry | Read | 
| <a name="eks-DescribeAddon"></a>[DescribeAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddon.html) | Retrieve descriptive information about an Amazon EKS add-on | Read | 
| <a name="eks-DescribeAddonConfiguration"></a>[DescribeAddonConfiguration](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonConfiguration.html) | List configuration options about an Amazon EKS add-on | Read | 
| <a name="eks-DescribeAddonVersions"></a>[DescribeAddonVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html) | Retrieve descriptive version information about the add-ons that Amazon EKS Add-ons supports | Read | 
| <a name="eks-DescribeCapability"></a>[DescribeCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCapability.html) | Describe a capability for an Amazon EKS cluster | Read | 
| <a name="eks-DescribeCertificateAuthority"></a>[DescribeCertificateAuthority](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCertificateAuthority.html) | Retrieve descriptive information about a certificate authority for an Amazon EKS cluster | Read | 
| <a name="eks-DescribeCluster"></a>[DescribeCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCluster.html) | Retrieve descriptive information about an Amazon EKS cluster | Read | 
| <a name="eks-DescribeClusterVersions"></a>[DescribeClusterVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeClusterVersions.html) | Retrieve descriptive information about Kubernetes versions that Amazon EKS clusters support | Read | 
| <a name="eks-DescribeEksAnywhereSubscription"></a>[DescribeEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeEksAnywhereSubscription.html) | Describe an EKS Anywhere subscription | Read | 
| <a name="eks-DescribeFargateProfile"></a>[DescribeFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeFargateProfile.html) | Retrieve descriptive information about an AWS Fargate profile associated with a cluster | Read | 
| <a name="eks-DescribeIdentityProviderConfig"></a>[DescribeIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeIdentityProviderConfig.html) | Retrieve descriptive information about an Idp config associated with a cluster | Read | 
| <a name="eks-DescribeInsight"></a>[DescribeInsight](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeInsight.html) | Retrieve descriptive information of a detected insight for a specified cluster | Read | 
| <a name="eks-DescribeInsightsRefresh"></a>[DescribeInsightsRefresh](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeInsightsRefresh.html) | Retrieve the status of the latest on-demand cluster insights refresh operation | Read | 
| <a name="eks-DescribeNodegroup"></a>[DescribeNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeNodegroup.html) | Retrieve descriptive information about an Amazon EKS nodegroup | Read | 
| <a name="eks-DescribePodIdentityAssociation"></a>[DescribePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribePodIdentityAssociation.html) | Describe an EKS Pod Identity association | Read | 
| <a name="eks-DescribeUpdate"></a>[DescribeUpdate](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html) | Retrieve a given update for a given Amazon EKS cluster/nodegroup/add-on (in the specified or default region) | Read | 
| <a name="eks-ListAccessEntries"></a>[ListAccessEntries](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAccessEntries.html) | List all Amazon EKS access entries | List | 
| <a name="eks-ListAccessPolicies"></a>[ListAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAccessPolicies.html) | List Amazon EKS access policies | List | 
| <a name="eks-ListAddons"></a>[ListAddons](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html) | List the Amazon EKS add-ons in your AWS account (in the specified or default region) for a given cluster | List | 
| <a name="eks-ListAssociatedAccessPolicies"></a>[ListAssociatedAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAssociatedAccessPolicies.html) | List associated access policy on and Amazon EKS access entry | List | 
| <a name="eks-ListCapabilities"></a>[ListCapabilities](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCapabilities.html) | List capabilities for an Amazon EKS cluster | List | 
| <a name="eks-ListCertificateAuthorities"></a>[ListCertificateAuthorities](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCertificateAuthorities.html) | List the certificate authorities for an Amazon EKS cluster | List | 
| <a name="eks-ListClusters"></a>[ListClusters](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListClusters.html) | List the Amazon EKS clusters in your AWS account (in the specified or default region) | List | 
| <a name="eks-ListDashboardData"></a>[ListDashboardData](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListDashboardData.html) | List dashboard data. The Amazon EKS Dashboard aggregates information about cluster resources across multiple accounts and regions. The dashboard includes information about EC2 Instances and EKS Cluster versions | Read | 
| <a name="eks-ListDashboardResources"></a>[ListDashboardResources](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListDashboardResources.html) | List dashboard resources. The Amazon EKS Dashboard aggregates information about cluster resources across multiple accounts and regions. The dashboard includes information about EC2 Instances and EKS Cluster versions | Read | 
| <a name="eks-ListEksAnywhereSubscriptions"></a>[ListEksAnywhereSubscriptions](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListEksAnywhereSubscriptions.html) | List EKS Anywhere subscriptions | List | 
| <a name="eks-ListFargateProfiles"></a>[ListFargateProfiles](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListFargateProfiles.html) | List the AWS Fargate profiles in your AWS account (in the specified or default region) associated with a given cluster | List | 
| <a name="eks-ListIdentityProviderConfigs"></a>[ListIdentityProviderConfigs](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListIdentityProviderConfigs.html) | List the Idp configs in your AWS account (in the specified or default region) associated with a given cluster | List | 
| <a name="eks-ListInsights"></a>[ListInsights](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html) | List all detected insights for a specified cluster | List | 
| <a name="eks-ListNodegroups"></a>[ListNodegroups](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListNodegroups.html) | List the Amazon EKS nodegroups in your AWS account (in the specified or default region) attached to given cluster | List | 
| <a name="eks-ListPodIdentityAssociations"></a>[ListPodIdentityAssociations](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListPodIdentityAssociations.html) | List EKS Pod Identity associations | List | 
| <a name="eks-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListTagsForResource.html) | List tags for the specified resource | Read | 
| <a name="eks-ListUpdates"></a>[ListUpdates](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListUpdates.html) | List the updates for a given Amazon EKS cluster/nodegroup/add-on (in the specified or default region) | List | 