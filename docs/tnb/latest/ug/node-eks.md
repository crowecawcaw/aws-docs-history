

# AWS.Compute.EKS
<a name="node-eks"></a>

Provide the name of the cluster, the desired Kubernetes version, and a role that allows the Kubernetes control plane to manage the AWS resources required for your NFs. Multus container network interface (CNI) plugins are enabled. You can attach multiple network interfaces and apply advanced network configuration to the Kubernetes-based network functions. You also specify the cluster endpoint access and the subnets for your cluster.

## Syntax
<a name="node-eks-syntax"></a>

```
tosca.nodes.AWS.Compute.EKS:
  capabilities:
    multus:
      properties:
        enabled: Boolean
        multus\_role: String
    ebs\_csi:
      properties:
        enabled: Boolean
        version: String      
  properties:
    version: String
    access: String
    cluster\_role: String
    tags: List
    ip\_family: String        
  requirements:
    subnets: List
```

## Capabilities
<a name="node-eks-capabilities"></a><a name="node_eks_multus"></a>`multus`

Optional. Properties that define the Multus container network interface (CNI) usage. 

If you include `multus`, specify the `enabled` and `multus_role` properties.

 `enabled`    
Indicates whether the default Multus capability is enabled.  
Required: Yes  
Type: Boolean

 `multus_role`    
The role for Multus network interface management.  
Required: Yes  
Type: String<a name="node_eks_ebs_csi"></a>`ebs_csi`

Properties that define the Amazon EBS Container Storage Interface (CSI) driver installed in the Amazon EKS cluster.

Enable this plugin to use Amazon EKS self-managed nodes on AWS Outposts, AWS Local Zones, or AWS Regions. For more information, see [Amazon Elastic Block Store CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) in the **Amazon EKS User Guide**.

 `enabled`    
Indicates whether the default Amazon EBS CSI driver is installed.  
Required: No  
Type: Boolean

 `version`    
The version of the Amazon EBS CSI driver add-on. The version must match one of the versions returned by the *DescribeAddonVersions* action. For more information, see [DescribeAddonVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html) in the *Amazon EKS API Reference*   
Required: No  
Type: String

## Properties
<a name="node-eks-properties"></a>

 `version`    
The Kubernetes version for the cluster. AWS Telco Network Builder supports Kubernetes versions 1.27 through 1.34.  
Required: Yes  
Type: String  
Possible values: 1.27 \| 1.28 \| 1.29 \| 1.30 \| 1.31 \| 1.32 \| 1.33 \| 1.34

 `access`    
The cluster endpoint access.  
Required: Yes  
Type: String  
Possible values: `PRIVATE` \| `PUBLIC` \| `ALL`

 `cluster_role`    
The role for cluster management.  
Required: Yes  
Type: String

 `tags`    
Tags to be attached to the resource.  
Required: No  
Type: List

 `ip_family`    
Indicates the IP family for service and pod addresses in the cluster.  
Allowed value: `IPv4`, `IPv6`  
Default value: `IPv4`  
Required: No  
Type: String

## Requirements
<a name="node-eks-requirements"></a>

 `subnets`    
An [AWS.Networking.Subnet](node-subnet.md) node.  
Required: Yes  
Type: List

## Example
<a name="node-eks-example"></a>

```
SampleEKS:
  type: tosca.nodes.AWS.Compute.EKS
  properties:
    version: "1.26"
    access: "ALL"
    cluster_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/{{SampleRole}}"
    ip_family: "IPv6"
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing" 
  capabilities:
    multus:
      properties:
        enabled: true
        multus_role: "arn:aws:iam::${AWS::TNB::AccountId}:role/{{MultusRole}}"
    ebs_csi:
      properties:
        enabled: true
        version: "v1.16.0-eksbuild.1"        
  requirements:
    subnets:
    - SampleSubnet01
    - SampleSubnet02
```