

# eks-nodegroup-supported-version-check
<a name="eks-nodegroup-supported-version-check"></a>

Checks if an Amazon Elastic Kubernetes Service (EKS) nodegroup is running the oldest supported version. 



**Identifier:** EKS\_NODEGROUP\_SUPPORTED\_VERSION\_CHECK

**Resource Types:** AWS::EKS::Nodegroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Middle East (UAE) Region

**Parameters:**

oldestVersionSupportedType: String  
Value of the oldest version of Kubernetes supported on AWS.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d733c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).