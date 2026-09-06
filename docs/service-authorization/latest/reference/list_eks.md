

# Actions, resources, and condition keys for Amazon Elastic Kubernetes Service
<a name="list_eks"></a>

Amazon Elastic Kubernetes Service (service prefix: `eks`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eks/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eks/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eks/latest/userguide/IAM_policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/eks/eks.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic Kubernetes Service](#list_eks-operations)
+ [Actions defined by Amazon Elastic Kubernetes Service](#list_eks-actions-as-permissions)
+ [Permission-only actions for Amazon Elastic Kubernetes Service](#list_eks-permission-only-actions)
+ [Resource types defined by Amazon Elastic Kubernetes Service](#list_eks-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic Kubernetes Service](#list_eks-policy-keys)

## API operations defined by Amazon Elastic Kubernetes Service
<a name="list_eks-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_eks-actions-as-permissions).




- **   ActivateCertificateAuthority  **
  - **IAM action:**  [eks:ActivateCertificateAuthority](#list_eks-action-ActivateCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateAccessPolicy  **
  - **IAM action:**  [eks:AssociateAccessPolicy](#list_eks-action-AssociateAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateEncryptionConfig  **
  - **IAM action:**  [eks:AssociateEncryptionConfig](#list_eks-action-AssociateEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateIdentityProviderConfig  **
  - **IAM action:**  [eks:AssociateIdentityProviderConfig](#list_eks-action-AssociateIdentityProviderConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CancelUpdate  **
  - **IAM action:**  [eks:CancelUpdate](#list_eks-action-CancelUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessEntry  **
  - **IAM action:**  [eks:CreateAccessEntry](#list_eks-action-CreateAccessEntry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   CreateAddon  **
  - **IAM action:**  [eks:CreateAddon](#list_eks-action-CreateAddon)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   CreateCapability  **
  - **IAM action:**  [eks:CreateCapability](#list_eks-action-CreateCapability)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   CreateCertificateAuthority  **
  - **IAM action:**  [eks:CreateCertificateAuthority](#list_eks-action-CreateCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCluster  **
  - **IAM action:**  [eks:CreateAccessEntry](#list_eks-action-CreateAccessEntry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:CreateCluster](#list_eks-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com, eks.amazonaws.com / **Access level:** Write

- **   CreateEksAnywhereSubscription  **
  - **IAM action:**  [eks:CreateEksAnywhereSubscription](#list_eks-action-CreateEksAnywhereSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFargateProfile  **
  - **IAM action:**  [eks:CreateFargateProfile](#list_eks-action-CreateFargateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   CreateNodegroup  **
  - **IAM action:**  [eks:CreateNodegroup](#list_eks-action-CreateNodegroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   CreatePodIdentityAssociation  **
  - **IAM action:**  [eks:CreatePodIdentityAssociation](#list_eks-action-CreatePodIdentityAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** pods.eks.amazonaws.com / **Access level:** Write

- **   DeleteAccessEntry  **
  - **IAM action:**  [eks:DeleteAccessEntry](#list_eks-action-DeleteAccessEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAddon  **
  - **IAM action:**  [eks:DeleteAddon](#list_eks-action-DeleteAddon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCapability  **
  - **IAM action:**  [eks:DeleteCapability](#list_eks-action-DeleteCapability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCertificateAuthority  **
  - **IAM action:**  [eks:DeleteCertificateAuthority](#list_eks-action-DeleteCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [eks:DeleteCluster](#list_eks-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEksAnywhereSubscription  **
  - **IAM action:**  [eks:DeleteEksAnywhereSubscription](#list_eks-action-DeleteEksAnywhereSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFargateProfile  **
  - **IAM action:**  [eks:DeleteFargateProfile](#list_eks-action-DeleteFargateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNodegroup  **
  - **IAM action:**  [eks:DeleteNodegroup](#list_eks-action-DeleteNodegroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePodIdentityAssociation  **
  - **IAM action:**  [eks:DeletePodIdentityAssociation](#list_eks-action-DeletePodIdentityAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterCluster  **
  - **IAM action:**  [eks:DeregisterCluster](#list_eks-action-DeregisterCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccessEntry  **
  - **IAM action:**  [eks:DescribeAccessEntry](#list_eks-action-DescribeAccessEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAddon  **
  - **IAM action:**  [eks:DescribeAddon](#list_eks-action-DescribeAddon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAddonConfiguration  **
  - **IAM action:**  [eks:DescribeAddonConfiguration](#list_eks-action-DescribeAddonConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAddonVersions  **
  - **IAM action:**  [eks:DescribeAddonVersions](#list_eks-action-DescribeAddonVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCapability  **
  - **IAM action:**  [eks:DescribeCapability](#list_eks-action-DescribeCapability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificateAuthority  **
  - **IAM action:**  [eks:DescribeCertificateAuthority](#list_eks-action-DescribeCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCluster  **
  - **IAM action:**  [eks:DescribeCluster](#list_eks-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterVersions  **
  - **IAM action:**  [eks:DescribeClusterVersions](#list_eks-action-DescribeClusterVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEksAnywhereSubscription  **
  - **IAM action:**  [eks:DescribeEksAnywhereSubscription](#list_eks-action-DescribeEksAnywhereSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFargateProfile  **
  - **IAM action:**  [eks:DescribeFargateProfile](#list_eks-action-DescribeFargateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIdentityProviderConfig  **
  - **IAM action:**  [eks:DescribeIdentityProviderConfig](#list_eks-action-DescribeIdentityProviderConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInsight  **
  - **IAM action:**  [eks:DescribeInsight](#list_eks-action-DescribeInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInsightsRefresh  **
  - **IAM action:**  [eks:DescribeInsightsRefresh](#list_eks-action-DescribeInsightsRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNodegroup  **
  - **IAM action:**  [eks:DescribeNodegroup](#list_eks-action-DescribeNodegroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePodIdentityAssociation  **
  - **IAM action:**  [eks:DescribePodIdentityAssociation](#list_eks-action-DescribePodIdentityAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUpdate  **
  - **IAM action:**  [eks:DescribeUpdate](#list_eks-action-DescribeUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateAccessPolicy  **
  - **IAM action:**  [eks:DisassociateAccessPolicy](#list_eks-action-DisassociateAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateIdentityProviderConfig  **
  - **IAM action:**  [eks:DisassociateIdentityProviderConfig](#list_eks-action-DisassociateIdentityProviderConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAccessEntries  **
  - **IAM action:**  [eks:ListAccessEntries](#list_eks-action-ListAccessEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccessPolicies  **
  - **IAM action:**  [eks:ListAccessPolicies](#list_eks-action-ListAccessPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAddons  **
  - **IAM action:**  [eks:ListAddons](#list_eks-action-ListAddons) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociatedAccessPolicies  **
  - **IAM action:**  [eks:ListAssociatedAccessPolicies](#list_eks-action-ListAssociatedAccessPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCapabilities  **
  - **IAM action:**  [eks:ListCapabilities](#list_eks-action-ListCapabilities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCertificateAuthorities  **
  - **IAM action:**  [eks:ListCertificateAuthorities](#list_eks-action-ListCertificateAuthorities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [eks:ListClusters](#list_eks-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEksAnywhereSubscriptions  **
  - **IAM action:**  [eks:ListEksAnywhereSubscriptions](#list_eks-action-ListEksAnywhereSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFargateProfiles  **
  - **IAM action:**  [eks:ListFargateProfiles](#list_eks-action-ListFargateProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityProviderConfigs  **
  - **IAM action:**  [eks:ListIdentityProviderConfigs](#list_eks-action-ListIdentityProviderConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInsights  **
  - **IAM action:**  [eks:ListInsights](#list_eks-action-ListInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNodegroups  **
  - **IAM action:**  [eks:ListNodegroups](#list_eks-action-ListNodegroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPodIdentityAssociations  **
  - **IAM action:**  [eks:ListPodIdentityAssociations](#list_eks-action-ListPodIdentityAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [eks:ListTagsForResource](#list_eks-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUpdates  **
  - **IAM action:**  [eks:ListUpdates](#list_eks-action-ListUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterCluster  **
  - **IAM action:**  [eks:RegisterCluster](#list_eks-action-RegisterCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   StartInsightsRefresh  **
  - **IAM action:**  [eks:StartInsightsRefresh](#list_eks-action-StartInsightsRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [eks:TagResource](#list_eks-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [eks:UntagResource](#list_eks-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessEntry  **
  - **IAM action:**  [eks:UpdateAccessEntry](#list_eks-action-UpdateAccessEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAddon  **
  - **IAM action:**  [eks:UpdateAddon](#list_eks-action-UpdateAddon)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   UpdateCapability  **
  - **IAM action:**  [eks:UpdateCapability](#list_eks-action-UpdateCapability)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** eks.amazonaws.com / **Access level:** Write

- **   UpdateClusterConfig  **
  - **IAM action:**  [eks:CreateAccessEntry](#list_eks-action-CreateAccessEntry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [eks:UpdateClusterConfig](#list_eks-action-UpdateClusterConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com, eks.amazonaws.com / **Access level:** Write

- **   UpdateClusterVersion  **
  - **IAM action:**  [eks:UpdateClusterVersion](#list_eks-action-UpdateClusterVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEksAnywhereSubscription  **
  - **IAM action:**  [eks:UpdateEksAnywhereSubscription](#list_eks-action-UpdateEksAnywhereSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNodegroupConfig  **
  - **IAM action:**  [eks:UpdateNodegroupConfig](#list_eks-action-UpdateNodegroupConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNodegroupVersion  **
  - **IAM action:**  [eks:UpdateNodegroupVersion](#list_eks-action-UpdateNodegroupVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePodIdentityAssociation  **
  - **IAM action:**  [eks:UpdatePodIdentityAssociation](#list_eks-action-UpdatePodIdentityAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** pods.eks.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Elastic Kubernetes Service
<a name="list_eks-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateCertificateAuthority](https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html)  **
  - **Description:** Grants permission to activate a certificate authority for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateAccessPolicy.html)  **
  - **Description:** Grants permission to associate an Amazon EKS access policy to an Amazon EKS access entry
  - **Resource types (\*required):** [access-entry\*](#list_eks-resource-access-entry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:accessScope](#list_eks-eks_accessScope)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:namespaces](#list_eks-eks_namespaces)<br />[eks:policyArn](#list_eks-eks_policyArn)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** Write

- **   [AssociateEncryptionConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateEncryptionConfig.html)  **
  - **Description:** Grants permission to associate encryption configuration to a cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:encryptionConfigProviderKeyArns](#list_eks-eks_encryptionConfigProviderKeyArns)
  - **Access level:** Write

- **   [AssociateIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociateIdentityProviderConfig.html)  **
  - **Description:** Grants permission to associate an identity provider configuration to a cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)<br />[eks:clientId](#list_eks-eks_clientId)<br />[eks:issuerUrl](#list_eks-eks_issuerUrl)
  - **Access level:** Write

- **   [CancelUpdate](https://docs.aws.amazon.com/eks/latest/APIReference/API_CancelUpdate.html)  **
  - **Description:** Grants permission to cancel an in-progress Kubernetes version update for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateAccessEntry.html)  **
  - **Description:** Grants permission to create an Amazon EKS access entry
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** Write

- **   [CreateAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateAddon.html)  **
  - **Description:** Grants permission to create an Amazon EKS add-on
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [podidentityassociation](#list_eks-resource-podidentityassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCapability.html)  **
  - **Description:** Grants permission to create a capability for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCertificateAuthority](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCertificateAuthority.html)  **
  - **Description:** Grants permission to create a certificate authority for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create an Amazon EKS cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)<br />[eks:authenticationMode](#list_eks-eks_authenticationMode)<br />[eks:blockStorageEnabled](#list_eks-eks_blockStorageEnabled)<br />[eks:bootstrapClusterCreatorAdminPermissions](#list_eks-eks_bootstrapClusterCreatorAdminPermissions)<br />[eks:bootstrapSelfManagedAddons](#list_eks-eks_bootstrapSelfManagedAddons)<br />[eks:computeConfigEnabled](#list_eks-eks_computeConfigEnabled)<br />[eks:controlPlaneEgressMode](#list_eks-eks_controlPlaneEgressMode)<br />[eks:controlPlaneScalingTier](#list_eks-eks_controlPlaneScalingTier)<br />[eks:deletionProtection](#list_eks-eks_deletionProtection)<br />[eks:elasticLoadBalancingEnabled](#list_eks-eks_elasticLoadBalancingEnabled)<br />[eks:encryptionConfigProviderKeyArns](#list_eks-eks_encryptionConfigProviderKeyArns)<br />[eks:endpointPrivateAccess](#list_eks-eks_endpointPrivateAccess)<br />[eks:endpointPublicAccess](#list_eks-eks_endpointPublicAccess)<br />[eks:kubeApiServerConfig](#list_eks-eks_kubeApiServerConfig)<br />[eks:kubeControllerManagerConfig](#list_eks-eks_kubeControllerManagerConfig)<br />[eks:kubernetesVersion](#list_eks-eks_kubernetesVersion)<br />[eks:kubeSchedulerConfig](#list_eks-eks_kubeSchedulerConfig)<br />[eks:loggingType/${type}](#list_eks-eks_loggingType___type_)<br />[eks:supportType](#list_eks-eks_supportType)<br />[eks:zonalShiftEnabled](#list_eks-eks_zonalShiftEnabled)
  - **Access level:** Write

- **   [CreateEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateEksAnywhereSubscription.html)  **
  - **Description:** Grants permission to create an EKS Anywhere subscription
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateFargateProfile.html)  **
  - **Description:** Grants permission to create an AWS Fargate profile
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreateNodegroup.html)  **
  - **Description:** Grants permission to create an Amazon EKS Nodegroup
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_CreatePodIdentityAssociation.html)  **
  - **Description:** Grants permission to create an EKS Pod Identity association
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteAccessEntry.html)  **
  - **Description:** Grants permission to delete an Amazon EKS access entry
  - **Resource types (\*required):** [access-entry\*](#list_eks-resource-access-entry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** Write

- **   [DeleteAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteAddon.html)  **
  - **Description:** Grants permission to delete an Amazon EKS add-on
  - **Resource types (\*required):** [addon\*](#list_eks-resource-addon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [podidentityassociation](#list_eks-resource-podidentityassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteCapability.html)  **
  - **Description:** Grants permission to delete a capability from an Amazon EKS cluster
  - **Resource types (\*required):** [capability\*](#list_eks-resource-capability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCertificateAuthority](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteCertificateAuthority.html)  **
  - **Description:** Grants permission to delete a certificate authority from an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteEksAnywhereSubscription.html)  **
  - **Description:** Grants permission to describe an EKS Anywhere subscription
  - **Resource types (\*required):** [eks-anywhere-subscription\*](#list_eks-resource-eks-anywhere-subscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteFargateProfile.html)  **
  - **Description:** Grants permission to delete an AWS Fargate profile
  - **Resource types (\*required):** [fargateprofile\*](#list_eks-resource-fargateprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeleteNodegroup.html)  **
  - **Description:** Grants permission to delete an Amazon EKS Nodegroup
  - **Resource types (\*required):** [nodegroup\*](#list_eks-resource-nodegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeletePodIdentityAssociation.html)  **
  - **Description:** Grants permission to delete an EKS Pod Identity association
  - **Resource types (\*required):** [podidentityassociation\*](#list_eks-resource-podidentityassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DeregisterCluster.html)  **
  - **Description:** Grants permission to deregister an External cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAccessEntry.html)  **
  - **Description:** Grants permission to describe an Amazon EKS access entry
  - **Resource types (\*required):** [access-entry\*](#list_eks-resource-access-entry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** Read

- **   [DescribeAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddon.html)  **
  - **Description:** Grants permission to retrieve descriptive information about an Amazon EKS add-on
  - **Resource types (\*required):** [addon\*](#list_eks-resource-addon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAddonConfiguration](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonConfiguration.html)  **
  - **Description:** Grants permission to list configuration options about an Amazon EKS add-on
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAddonVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html)  **
  - **Description:** Grants permission to retrieve descriptive version information about the add-ons that Amazon EKS Add-ons supports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCapability.html)  **
  - **Description:** Grants permission to describe a capability for an Amazon EKS cluster
  - **Resource types (\*required):** [capability\*](#list_eks-resource-capability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificateAuthority](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCertificateAuthority.html)  **
  - **Description:** Grants permission to retrieve descriptive information about a certificate authority for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCluster.html)  **
  - **Description:** Grants permission to retrieve descriptive information about an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeClusterVersions.html)  **
  - **Description:** Grants permission to retrieve descriptive information about Kubernetes versions that Amazon EKS clusters support
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeEksAnywhereSubscription.html)  **
  - **Description:** Grants permission to describe an EKS Anywhere subscription
  - **Resource types (\*required):** [eks-anywhere-subscription\*](#list_eks-resource-eks-anywhere-subscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFargateProfile](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeFargateProfile.html)  **
  - **Description:** Grants permission to retrieve descriptive information about an AWS Fargate profile associated with a cluster
  - **Resource types (\*required):** [fargateprofile\*](#list_eks-resource-fargateprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeIdentityProviderConfig.html)  **
  - **Description:** Grants permission to retrieve descriptive information about an Idp config associated with a cluster
  - **Resource types (\*required):** [identityproviderconfig\*](#list_eks-resource-identityproviderconfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInsight](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeInsight.html)  **
  - **Description:** Grants permission to retrieve descriptive information of a detected insight for a specified cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInsightsRefresh](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeInsightsRefresh.html)  **
  - **Description:** Grants permission to retrieve the status of the latest on-demand cluster insights refresh operation
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeNodegroup.html)  **
  - **Description:** Grants permission to retrieve descriptive information about an Amazon EKS nodegroup
  - **Resource types (\*required):** [nodegroup\*](#list_eks-resource-nodegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribePodIdentityAssociation.html)  **
  - **Description:** Grants permission to describe an EKS Pod Identity association
  - **Resource types (\*required):** [podidentityassociation\*](#list_eks-resource-podidentityassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUpdate](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html)  **
  - **Description:** Grants permission to retrieve a given update for a given Amazon EKS cluster/nodegroup/add-on (in the specified or default region)
  - **Resource types (\*required):** [addon](#list_eks-resource-addon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [capability](#list_eks-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [nodegroup](#list_eks-resource-nodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateAccessPolicy](https://docs.aws.amazon.com/eks/latest/APIReference/API_DisassociateAccessPolicy.html)  **
  - **Description:** Grants permission to disassociate an Amazon EKS access policy from an Amazon EKS acces entry
  - **Resource types (\*required):** [access-entry\*](#list_eks-resource-access-entry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:accessScope](#list_eks-eks_accessScope)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:namespaces](#list_eks-eks_namespaces)<br />[eks:policyArn](#list_eks-eks_policyArn)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** Write

- **   [DisassociateIdentityProviderConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_DisassociateIdentityProviderConfig.html)  **
  - **Description:** Grants permission to delete an asssociated Idp config
  - **Resource types (\*required):** [identityproviderconfig\*](#list_eks-resource-identityproviderconfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAccessEntries](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAccessEntries.html)  **
  - **Description:** Grants permission to list all Amazon EKS access entries
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAccessPolicies.html)  **
  - **Description:** Grants permission to list Amazon EKS access policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAddons](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html)  **
  - **Description:** Grants permission to list the Amazon EKS add-ons in your AWS account (in the specified or default region) for a given cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociatedAccessPolicies](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAssociatedAccessPolicies.html)  **
  - **Description:** Grants permission to list associated access policy on and Amazon EKS access entry
  - **Resource types (\*required):** [access-entry\*](#list_eks-resource-access-entry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** List

- **   [ListCapabilities](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCapabilities.html)  **
  - **Description:** Grants permission to list capabilities for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCertificateAuthorities](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListCertificateAuthorities.html)  **
  - **Description:** Grants permission to list the certificate authorities for an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListClusters.html)  **
  - **Description:** Grants permission to list the Amazon EKS clusters in your AWS account (in the specified or default region)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDashboardData](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListDashboardData.html)  **
  - **Description:** Grants permission to list dashboard data. The Amazon EKS Dashboard aggregates information about cluster resources across multiple accounts and regions. The dashboard includes information about EC2 Instances and EKS Cluster versions
  - **Resource types (\*required):** [dashboard\*](#list_eks-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDashboardResources](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListDashboardResources.html)  **
  - **Description:** Grants permission to list dashboard resources. The Amazon EKS Dashboard aggregates information about cluster resources across multiple accounts and regions. The dashboard includes information about EC2 Instances and EKS Cluster versions
  - **Resource types (\*required):** [dashboard\*](#list_eks-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEksAnywhereSubscriptions](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListEksAnywhereSubscriptions.html)  **
  - **Description:** Grants permission to list EKS Anywhere subscriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFargateProfiles](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListFargateProfiles.html)  **
  - **Description:** Grants permission to list the AWS Fargate profiles in your AWS account (in the specified or default region) associated with a given cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdentityProviderConfigs](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListIdentityProviderConfigs.html)  **
  - **Description:** Grants permission to list the Idp configs in your AWS account (in the specified or default region) associated with a given cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInsights](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html)  **
  - **Description:** Grants permission to list all detected insights for a specified cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNodegroups](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListNodegroups.html)  **
  - **Description:** Grants permission to list the Amazon EKS nodegroups in your AWS account (in the specified or default region) attached to given cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPodIdentityAssociations](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListPodIdentityAssociations.html)  **
  - **Description:** Grants permission to list EKS Pod Identity associations
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for the specified resource
  - **Resource types (\*required):** [addon](#list_eks-resource-addon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [capability](#list_eks-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_eks-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_eks-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eks-anywhere-subscription](#list_eks-resource-eks-anywhere-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fargateprofile](#list_eks-resource-fargateprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [identityproviderconfig](#list_eks-resource-identityproviderconfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [nodegroup](#list_eks-resource-nodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUpdates](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListUpdates.html)  **
  - **Description:** Grants permission to list the updates for a given Amazon EKS cluster/nodegroup/add-on (in the specified or default region)
  - **Resource types (\*required):** [addon](#list_eks-resource-addon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [capability](#list_eks-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [nodegroup](#list_eks-resource-nodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RegisterCluster](https://docs.aws.amazon.com/eks/latest/APIReference/API_RegisterCluster.html)  **
  - **Description:** Grants permission to register an External cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Write

- **   [StartInsightsRefresh](https://docs.aws.amazon.com/eks/latest/APIReference/API_StartInsightsRefresh.html)  **
  - **Description:** Grants permission to initiate an on-demand refresh operation for cluster insights, getting the latest analysis outside of the standard refresh schedule
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag the specified resource
  - **Resource types (\*required):** [access-entry](#list_eks-resource-access-entry) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Resource types (\*required):** [addon](#list_eks-resource-addon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [capability](#list_eks-resource-capability) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_eks-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_eks-resource-dashboard) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [eks-anywhere-subscription](#list_eks-resource-eks-anywhere-subscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [fargateprofile](#list_eks-resource-fargateprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [identityproviderconfig](#list_eks-resource-identityproviderconfig) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [nodegroup](#list_eks-resource-nodegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [podidentityassociation](#list_eks-resource-podidentityassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_eks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/eks/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag the specified resource
  - **Resource types (\*required):** [access-entry](#list_eks-resource-access-entry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Resource types (\*required):** [addon](#list_eks-resource-addon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [capability](#list_eks-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_eks-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_eks-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [eks-anywhere-subscription](#list_eks-resource-eks-anywhere-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [fargateprofile](#list_eks-resource-fargateprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [identityproviderconfig](#list_eks-resource-identityproviderconfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [nodegroup](#list_eks-resource-nodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Resource types (\*required):** [podidentityassociation](#list_eks-resource-podidentityassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eks-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccessEntry](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAccessEntry.html)  **
  - **Description:** Grants permission to update an Amazon EKS access entry
  - **Resource types (\*required):** [access-entry\*](#list_eks-resource-access-entry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username)
  - **Access level:** Write

- **   [UpdateAddon](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html)  **
  - **Description:** Grants permission to update Amazon EKS add-on configurations, such as the VPC-CNI version
  - **Resource types (\*required):** [addon\*](#list_eks-resource-addon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [podidentityassociation](#list_eks-resource-podidentityassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCapability](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateCapability.html)  **
  - **Description:** Grants permission to update a capability for an Amazon EKS cluster
  - **Resource types (\*required):** [capability\*](#list_eks-resource-capability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateClusterConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html)  **
  - **Description:** Grants permission to update Amazon EKS cluster configurations (eg: API server endpoint access)
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:authenticationMode](#list_eks-eks_authenticationMode)<br />[eks:blockStorageEnabled](#list_eks-eks_blockStorageEnabled)<br />[eks:computeConfigEnabled](#list_eks-eks_computeConfigEnabled)<br />[eks:controlPlaneEgressMode](#list_eks-eks_controlPlaneEgressMode)<br />[eks:controlPlaneScalingTier](#list_eks-eks_controlPlaneScalingTier)<br />[eks:deletionProtection](#list_eks-eks_deletionProtection)<br />[eks:elasticLoadBalancingEnabled](#list_eks-eks_elasticLoadBalancingEnabled)<br />[eks:endpointPrivateAccess](#list_eks-eks_endpointPrivateAccess)<br />[eks:endpointPublicAccess](#list_eks-eks_endpointPublicAccess)<br />[eks:kubeApiServerConfig](#list_eks-eks_kubeApiServerConfig)<br />[eks:kubeControllerManagerConfig](#list_eks-eks_kubeControllerManagerConfig)<br />[eks:kubeSchedulerConfig](#list_eks-eks_kubeSchedulerConfig)<br />[eks:loggingType/${type}](#list_eks-eks_loggingType___type_)<br />[eks:supportType](#list_eks-eks_supportType)<br />[eks:zonalShiftEnabled](#list_eks-eks_zonalShiftEnabled)
  - **Access level:** Write

- **   [UpdateClusterVersion](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html)  **
  - **Description:** Grants permission to update the Kubernetes version of an Amazon EKS cluster
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:kubernetesVersion](#list_eks-eks_kubernetesVersion)
  - **Access level:** Write

- **   [UpdateEksAnywhereSubscription](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateEksAnywhereSubscription.html)  **
  - **Description:** Grants permission to update an EKS Anywhere subscription
  - **Resource types (\*required):** [eks-anywhere-subscription\*](#list_eks-resource-eks-anywhere-subscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNodegroupConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupConfig.html)  **
  - **Description:** Grants permission to update Amazon EKS nodegroup configurations (eg: min/max/desired capacity or labels)
  - **Resource types (\*required):** [nodegroup\*](#list_eks-resource-nodegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNodegroupVersion](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html)  **
  - **Description:** Grants permission to update the Kubernetes version of an Amazon EKS nodegroup
  - **Resource types (\*required):** [nodegroup\*](#list_eks-resource-nodegroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePodIdentityAssociation](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdatePodIdentityAssociation.html)  **
  - **Description:** Grants permission to update an EKS Pod Identity association
  - **Resource types (\*required):** [podidentityassociation\*](#list_eks-resource-podidentityassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Elastic Kubernetes Service
<a name="list_eks-permission-only-actions"></a>

The following actions are defined by Amazon Elastic Kubernetes Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccessKubernetesApi](https://docs.aws.amazon.com/eks/latest/userguide/view-workloads.html)  **
  - **Description:** Grants permission to view Kubernetes objects via AWS EKS console
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [MutateViaKubernetesApi](https://docs.aws.amazon.com/eks/latest/userguide/mutate-workloads.html)  **
  - **Description:** Grants permission to modify Kubernetes objects via AWS console
  - **Resource types (\*required):** [cluster\*](#list_eks-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Elastic Kubernetes Service
<a name="list_eks-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html)  | arn:${Partition}:eks:${Region}:${Account}:access-entry/${ClusterName}/${IamIdentityType}/${IamIdentityAccountID}/${IamIdentityName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_)<br />[eks:accessEntryType](#list_eks-eks_accessEntryType)<br />[eks:clusterName](#list_eks-eks_clusterName)<br />[eks:kubernetesGroups](#list_eks-eks_kubernetesGroups)<br />[eks:principalArn](#list_eks-eks_principalArn)<br />[eks:username](#list_eks-eks_username) | 
|  [access-policy](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html)  | arn:${Partition}:eks::aws:cluster-access-policy/${AccessPolicyName} |   | 
|  [addon](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)  | arn:${Partition}:eks:${Region}:${Account}:addon/${ClusterName}/${AddonName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [capability](https://docs.aws.amazon.com/eks/latest/userguide/capabilities.html)  | arn:${Partition}:eks:${Region}:${Account}:capability/${ClusterName}/${CapabilityType}/${CapabilityName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html)  | arn:${Partition}:eks:${Region}:${Account}:cluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [dashboard](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard.html)  | arn:${Partition}:eks:${Region}:${Account}:dashboard/${DashboardName} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [eks-anywhere-subscription](https://anywhere.eks.amazonaws.com/docs/clustermgmt/support/cluster-license/)  | arn:${Partition}:eks:${Region}:${Account}:eks-anywhere-subscription/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [fargateprofile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html)  | arn:${Partition}:eks:${Region}:${Account}:fargateprofile/${ClusterName}/${FargateProfileName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [identityproviderconfig](https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html)  | arn:${Partition}:eks:${Region}:${Account}:identityproviderconfig/${ClusterName}/${IdentityProviderType}/${IdentityProviderConfigName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [nodegroup](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)  | arn:${Partition}:eks:${Region}:${Account}:nodegroup/${ClusterName}/${NodegroupName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 
|  [podidentityassociation](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)  | arn:${Partition}:eks:${Region}:${Account}:podidentityassociation/${ClusterName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_eks-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic Kubernetes Service
<a name="list_eks-policy-keys"></a>

Amazon Elastic Kubernetes Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by a key that is present in the request the user makes to the EKS service | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by a tag key and value pair | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the list of all the tag key names present in the request the user makes to the EKS service | ArrayOfString | 
|   [eks:accessEntryType](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the access entry type present in the access entry requests the user makes to the EKS service | String | 
|   [eks:accessScope](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the accessScope present in the associate / disassociate access policy requests the user makes to the EKS service | String | 
|   [eks:authenticationMode](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the authenticationMode present in the create / update cluster request | String | 
|   [eks:blockStorageEnabled](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the block storage enabled parameter in the create / update cluster request | Bool | 
|   [eks:bootstrapClusterCreatorAdminPermissions](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the bootstrapClusterCreatorAdminPermissions present in the create cluster request | Bool | 
|   [eks:bootstrapSelfManagedAddons](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the bootstrapSelfManagedAddons present in the create cluster request | Bool | 
|   [eks:clientId](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the clientId present in the associateIdentityProviderConfig request the user makes to the EKS service | String | 
|   [eks:clusterName](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the clusterName present in the access entry requests the user makes to the EKS service | String | 
|   [eks:computeConfigEnabled](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the compute config enabled parameter in the create / update cluster request | Bool | 
|   [eks:controlPlaneEgressMode](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the control plane egress mode specified in the create / update cluster request | String | 
|   [eks:controlPlaneScalingTier](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the control plane scaling tier in the create / update cluster request | String | 
|   [eks:deletionProtection](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the deletion protection setting in the create / update cluster request | Bool | 
|   [eks:elasticLoadBalancingEnabled](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the elastic load balancing enabled parameter in the create / update cluster request | Bool | 
|   [eks:encryptionConfigProviderKeyArns](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the KMS key ARNs in the create cluster / Associate Encryption Config request | ArrayOfARN | 
|   [eks:endpointPrivateAccess](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the endpoint private access setting in the create / update cluster request | Bool | 
|   [eks:endpointPublicAccess](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the endpoint public access setting in the create / update cluster request | Bool | 
|   [eks:issuerUrl](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the issuerUrl present in the associateIdentityProviderConfig request the user makes to the EKS service | String | 
|   [eks:kubeApiServerConfig](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by whether the kube-api-server configuration is present in the create / update cluster request | Bool | 
|   [eks:kubeControllerManagerConfig](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by whether the kube-controller-manager configuration is present in the create / update cluster request | Bool | 
|   [eks:kubeSchedulerConfig](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by whether the kube-scheduler configuration is present in the create / update cluster request | Bool | 
|   [eks:kubernetesGroups](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the kubernetesGroups present in the access entry requests the user makes to the EKS service | ArrayOfString | 
|   [eks:kubernetesVersion](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the Kubernetes version in the create cluster/ update cluster version request | String | 
|   [eks:loggingType/${type}](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the cluster logging enabled and type parameter in the create / update cluster request | Bool | 
|   [eks:namespaces](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the namespaces present in the associate / disassociate access policy requests the user makes to the EKS service | ArrayOfString | 
|   [eks:policyArn](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the policyArn present in the access entry requests the user makes to the EKS service | ARN | 
|   [eks:principalArn](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the principalArn present in the access entry requests requests the user makes to the EKS service | ARN | 
|   [eks:supportType](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the supportType present in the create / update cluster request | String | 
|   [eks:username](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the Kubernetes username present in the access entry requests the user makes to the EKS service | String | 
|   [eks:zonalShiftEnabled](https://docs.aws.amazon.com/eks/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the zonal shift enabled setting in the create / update cluster request | Bool | 